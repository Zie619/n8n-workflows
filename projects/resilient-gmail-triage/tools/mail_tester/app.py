from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import secrets
import smtplib
import ssl
import subprocess
import sys
import threading
import webbrowser
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from email.message import EmailMessage
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Callable, Protocol, cast
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
STATIC_ROOT = ROOT / "static"
DEFAULT_FIXTURES = ROOT / "fixtures.json"
MAX_BATCH_SIZE = 12
MAX_REQUEST_BYTES = 20_000
MAX_SUBJECT_LENGTH = 200
MAX_BODY_LENGTH = 5_000


@dataclass(frozen=True)
class Scenario:
    id: str
    category: str
    urgency: str
    title: str
    description: str
    subject: str
    body: str


@dataclass(frozen=True)
class PreparedMessage:
    scenario_id: str
    category: str
    urgency: str
    subject: str
    body: str


@dataclass(frozen=True)
class MailRequest:
    mode: str
    scenario_ids: tuple[str, ...] = ()
    subject: str = ""
    body: str = ""

    @classmethod
    def from_payload(cls, payload: dict) -> "MailRequest":
        if not isinstance(payload, dict):
            raise ValueError("request body must be an object")
        mode = str(payload.get("mode", "")).strip()
        raw_ids = payload.get("scenarioIds", [])
        if not isinstance(raw_ids, list) or not all(isinstance(item, str) for item in raw_ids):
            raise ValueError("scenarioIds must be a list of strings")
        return cls(
            mode=mode,
            scenario_ids=tuple(raw_ids),
            subject=str(payload.get("subject", "")),
            body=str(payload.get("body", "")),
        )


@dataclass(frozen=True)
class AppConfig:
    transport: str
    recipient: str
    sender: str
    audit_path: Path

    @property
    def live_send_enabled(self) -> bool:
        return self.transport in {"gmail-api", "smtp"} and bool(self.recipient)


class Sender(Protocol):
    def send(self, *, recipient: str, subject: str, body: str) -> dict: ...


def _require_string(row: dict, key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"scenario field {key} must be a non-empty string")
    return value.strip()


def load_scenarios(path: Path = DEFAULT_FIXTURES) -> dict[str, Scenario]:
    rows = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(rows, list) or not rows:
        raise ValueError("fixtures must contain a non-empty list")
    scenarios: dict[str, Scenario] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("every scenario must be an object")
        scenario = Scenario(
            id=_require_string(row, "id"),
            category=_require_string(row, "category"),
            urgency=_require_string(row, "urgency"),
            title=_require_string(row, "title"),
            description=_require_string(row, "description"),
            subject=_require_string(row, "subject"),
            body=_require_string(row, "body"),
        )
        if scenario.id in scenarios:
            raise ValueError(f"duplicate scenario id: {scenario.id}")
        validate_custom_message(scenario.subject, scenario.body)
        scenarios[scenario.id] = scenario
    return scenarios


def validate_custom_message(subject: str, body: str) -> tuple[str, str]:
    subject = str(subject).strip()
    body = str(body).strip()
    if not subject or len(subject) > MAX_SUBJECT_LENGTH:
        raise ValueError(f"subject must contain 1-{MAX_SUBJECT_LENGTH} characters")
    if not body or len(body) > MAX_BODY_LENGTH:
        raise ValueError(f"body must contain 1-{MAX_BODY_LENGTH} characters")
    if "\r" in subject or "\n" in subject:
        raise ValueError("subject must not contain line breaks")
    return subject, body


def resolve_messages(
    request: MailRequest,
    scenarios: dict[str, Scenario],
    *,
    rng: random.Random,
    now_token: str,
) -> list[PreparedMessage]:
    if request.mode == "selected":
        if not request.scenario_ids:
            raise ValueError("select at least one scenario")
        if len(request.scenario_ids) > MAX_BATCH_SIZE:
            raise ValueError(f"maximum batch size is {MAX_BATCH_SIZE}")
        if len(set(request.scenario_ids)) != len(request.scenario_ids):
            raise ValueError("scenario list contains duplicates")
        unknown = [item for item in request.scenario_ids if item not in scenarios]
        if unknown:
            raise ValueError("unknown scenario id")
        selected = [scenarios[item] for item in request.scenario_ids]
    elif request.mode == "random":
        if not scenarios:
            raise ValueError("no scenarios are available")
        selected = [rng.choice(list(scenarios.values()))]
    elif request.mode == "custom":
        subject, body = validate_custom_message(request.subject, request.body)
        selected = [
            Scenario(
                id="custom",
                category="UNKNOWN",
                urgency="unknown",
                title="Własna wiadomość",
                description="Treść wpisana przez użytkownika",
                subject=subject,
                body=body,
            )
        ]
    else:
        raise ValueError("mode must be selected, random or custom")

    prepared: list[PreparedMessage] = []
    for index, scenario in enumerate(selected, 1):
        marker = f"[E2E-{now_token}-{index:02d}]"
        prepared.append(
            PreparedMessage(
                scenario_id=scenario.id,
                category=scenario.category,
                urgency=scenario.urgency,
                subject=f"{marker} {scenario.subject}"[:MAX_SUBJECT_LENGTH],
                body=scenario.body,
            )
        )
    return prepared


class DryRunSender:
    def send(self, *, recipient: str, subject: str, body: str) -> dict:
        digest = hashlib.sha256(f"{recipient}\0{subject}\0{body}".encode()).hexdigest()[:16]
        return {"id": f"dry-{digest}", "transport": "dry-run"}


class GmailApiSender:
    def __init__(self, python: Path | None = None, google_api: Path | None = None):
        hermes_home = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
        self.python = Path(python or os.environ.get("HERMES_PYTHON", sys.executable))
        self.google_api = Path(
            google_api
            or os.environ.get(
                "HERMES_GOOGLE_API",
                hermes_home / "skills/productivity/google-workspace/scripts/google_api.py",
            )
        )
        if not self.google_api.is_file():
            raise FileNotFoundError(
                "gmail-api transport requires the optional Hermes Google Workspace adapter; "
                "set HERMES_GOOGLE_API or use an authenticated SMTP relay"
            )

    def send(self, *, recipient: str, subject: str, body: str) -> dict:
        result = subprocess.run(
            [
                str(self.python),
                str(self.google_api),
                "gmail",
                "send",
                "--to",
                recipient,
                "--subject",
                subject,
                "--body",
                body,
            ],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=90,
        )
        if result.returncode != 0:
            raise RuntimeError("Gmail API send failed")
        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError as error:
            raise RuntimeError("Gmail API returned invalid JSON") from error
        if not payload.get("id"):
            raise RuntimeError("Gmail API did not return a message ID")
        return {"id": payload["id"], "threadId": payload.get("threadId"), "transport": "gmail-api"}


class SMTPSender:
    def __init__(
        self,
        *,
        host: str,
        port: int,
        from_address: str,
        username: str | None,
        password: str | None,
        starttls: bool,
        smtp_factory: Callable = smtplib.SMTP,
    ):
        self.host = host
        self.port = port
        self.from_address = from_address
        self.username = username
        self.password = password
        self.starttls = starttls
        self.smtp_factory = smtp_factory

    def send(self, *, recipient: str, subject: str, body: str) -> dict:
        message = EmailMessage()
        message["From"] = self.from_address
        message["To"] = recipient
        message["Subject"] = subject
        message.set_content(body)
        with self.smtp_factory(self.host, self.port, timeout=30) as smtp:
            if self.starttls:
                smtp.starttls(context=ssl.create_default_context())
            if self.username:
                if self.password is None:
                    raise RuntimeError("SMTP password is required when username is set")
                smtp.login(self.username, self.password)
            refused = smtp.send_message(message)
        if refused:
            raise RuntimeError("SMTP server refused one or more recipients")
        digest = hashlib.sha256(message.as_bytes()).hexdigest()[:16]
        return {"id": f"smtp-{digest}", "transport": "smtp"}


def config_from_environment() -> AppConfig:
    return AppConfig(
        transport=os.environ.get("TEST_MAIL_TRANSPORT", "dry-run").strip().lower(),
        recipient=os.environ.get("TEST_MAIL_RECIPIENT", "").strip(),
        sender=os.environ.get("TEST_MAIL_FROM", "test-console@example.invalid").strip(),
        audit_path=Path(os.environ.get("TEST_MAIL_AUDIT_PATH", ".runtime/test-mailer-audit.jsonl")),
    )


def sender_from_environment(config: AppConfig) -> Sender:
    if config.transport == "dry-run":
        return DryRunSender()
    if not config.recipient:
        raise ValueError("TEST_MAIL_RECIPIENT is required for live sending")
    if config.transport == "gmail-api":
        return GmailApiSender()
    if config.transport == "smtp":
        host = os.environ.get("TEST_MAIL_SMTP_HOST", "127.0.0.1")
        port = int(os.environ.get("TEST_MAIL_SMTP_PORT", "1025"))
        username = os.environ.get("TEST_MAIL_SMTP_USERNAME") or None
        password = os.environ.get("TEST_MAIL_SMTP_PASSWORD") or None
        starttls = os.environ.get("TEST_MAIL_SMTP_STARTTLS", "false").lower() in {"1", "true", "yes"}
        return SMTPSender(
            host=host,
            port=port,
            from_address=config.sender,
            username=username,
            password=password,
            starttls=starttls,
        )
    raise ValueError("TEST_MAIL_TRANSPORT must be dry-run, gmail-api or smtp")


class MailService:
    def __init__(self, *, config: AppConfig, sender: Sender, scenarios: dict[str, Scenario]):
        self.config = config
        self.sender = sender
        self.scenarios = scenarios
        self._audit_lock = threading.Lock()

    def public_config(self) -> dict:
        return {
            "transport": self.config.transport,
            "recipient": self.config.recipient or "nie skonfigurowano",
            "liveSendEnabled": self.config.live_send_enabled,
            "maxBatchSize": MAX_BATCH_SIZE,
            "limits": {"subject": MAX_SUBJECT_LENGTH, "body": MAX_BODY_LENGTH},
        }

    def send_request(self, request: MailRequest, *, confirmed_count: int) -> list[dict]:
        token = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
        messages = resolve_messages(request, self.scenarios, rng=random.SystemRandom(), now_token=token)
        if confirmed_count != len(messages):
            raise ValueError("confirmation count does not match the prepared message count")
        results = []
        for message in messages:
            response = self.sender.send(
                recipient=self.config.recipient,
                subject=message.subject,
                body=message.body,
            )
            result = {
                "scenarioId": message.scenario_id,
                "category": message.category,
                "urgency": message.urgency,
                "subject": message.subject,
                "messageId": response["id"],
                "transport": response.get("transport", self.config.transport),
            }
            self._write_audit(message, result)
            results.append(result)
        return results

    def _write_audit(self, message: PreparedMessage, result: dict) -> None:
        row = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "scenario_id": message.scenario_id,
            "category": message.category,
            "urgency": message.urgency,
            "recipient": self.config.recipient,
            "subject": message.subject,
            "body_sha256": hashlib.sha256(message.body.encode()).hexdigest(),
            "message_id": result["messageId"],
            "transport": result["transport"],
        }
        path = self.config.audit_path
        with self._audit_lock:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")


class MailTesterServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, handler, *, service: MailService, csrf_token: str):
        super().__init__(address, handler)
        self.service = service
        self.csrf_token = csrf_token


class RequestHandler(BaseHTTPRequestHandler):
    @property
    def app_server(self) -> MailTesterServer:
        return cast(MailTesterServer, self.server)

    def log_message(self, format: str, *args) -> None:
        sys.stderr.write("mail-tester: " + format % args + "\n")

    def _security_headers(self) -> None:
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'",
        )
        self.send_header("Cache-Control", "no-store")

    def _send_json(self, status: int, payload: dict | list) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(status)
        self._security_headers()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_static(self, filename: str, content_type: str) -> None:
        path = STATIC_ROOT / filename
        if not path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        body = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self._security_headers()
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/":
            self._serve_static("index.html", "text/html; charset=utf-8")
        elif path == "/app.js":
            self._serve_static("app.js", "text/javascript; charset=utf-8")
        elif path == "/styles.css":
            self._serve_static("styles.css", "text/css; charset=utf-8")
        elif path == "/api/config":
            payload = self.app_server.service.public_config()
            payload["csrfToken"] = self.app_server.csrf_token
            self._send_json(HTTPStatus.OK, payload)
        elif path == "/api/scenarios":
            self._send_json(HTTPStatus.OK, [asdict(item) for item in self.app_server.service.scenarios.values()])
        elif path == "/healthz":
            self._send_json(HTTPStatus.OK, {"status": "ok"})
        else:
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "not found"})

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/send":
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return
        if self.headers.get("X-CSRF-Token") != self.app_server.csrf_token:
            self._send_json(HTTPStatus.FORBIDDEN, {"error": "invalid request token"})
            return
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "invalid content length"})
            return
        if content_length <= 0 or content_length > MAX_REQUEST_BYTES:
            self._send_json(HTTPStatus.REQUEST_ENTITY_TOO_LARGE, {"error": "request body is too large"})
            return
        try:
            payload = json.loads(self.rfile.read(content_length))
            request = MailRequest.from_payload(payload)
            confirmed_count = int(payload.get("confirmedCount", -1))
            results = self.app_server.service.send_request(request, confirmed_count=confirmed_count)
        except (ValueError, json.JSONDecodeError) as error:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": str(error)})
            return
        except Exception:
            self._send_json(HTTPStatus.BAD_GATEWAY, {"error": "transport failed; no automatic retry was attempted"})
            return
        self._send_json(HTTPStatus.OK, {"sent": len(results), "results": results})


def main() -> int:
    parser = argparse.ArgumentParser(description="Local web console for safe email triage tests")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8040, type=int)
    parser.add_argument("--fixtures", default=DEFAULT_FIXTURES, type=Path)
    parser.add_argument("--open", action="store_true")
    args = parser.parse_args()

    if args.host not in {"127.0.0.1", "localhost", "::1"}:
        raise SystemExit("Refusing non-loopback bind; put an authenticated reverse proxy in front first")

    config = config_from_environment()
    service = MailService(
        config=config,
        sender=sender_from_environment(config),
        scenarios=load_scenarios(args.fixtures),
    )
    server = MailTesterServer((args.host, args.port), RequestHandler, service=service, csrf_token=secrets.token_urlsafe(32))
    url = f"http://{args.host}:{args.port}"
    print(f"Test Mail Console: {url}")
    print(f"Transport: {config.transport}; recipient: {config.recipient or 'not configured'}")
    if args.open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
