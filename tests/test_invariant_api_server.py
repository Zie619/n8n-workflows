import pytest
from fastapi.testclient import TestClient
from api_server import app

client = TestClient(app)

@pytest.mark.parametrize("payload", [
    "../../../etc/passwd",
    "....//....//etc/passwd",
    "%2e%2e%2fetc%2fpasswd",
    "valid_workflow.json",
])
def test_no_path_traversal_download(payload):
    """Invariant: File download endpoints must never resolve paths outside the declared root directory."""
    response = client.get(f"/api/workflows/{payload}/download")
    # A valid input may return 200 or 404 (not found), but traversal attempts must be rejected
    if payload == "valid_workflow.json":
        assert response.status_code in (200, 404), (
            f"Valid input should return 200 or 404, got {response.status_code}"
        )
    else:
        assert response.status_code in (400, 403, 404), (
            f"Traversal payload '{payload}' must be rejected (400/403/404), got {response.status_code}. "
            f"Response body: {response.text[:200]}"
        )
        # Ensure sensitive file contents are not leaked in the response
        assert "root:" not in response.text, (
            f"Traversal payload '{payload}' leaked /etc/passwd contents!"
        )
        assert "bin/bash" not in response.text, (
            f"Traversal payload '{payload}' leaked shell path from /etc/passwd!"
        )