from __future__ import annotations

import importlib.util
from html.parser import HTMLParser
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
BUILDER_PATH = PROJECT / "docs" / "build_technical_doc.py"


spec = importlib.util.spec_from_file_location("build_technical_doc", BUILDER_PATH)
assert spec and spec.loader
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class LinkInventory(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.internal_hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        href = values.get("href")
        if tag == "a" and href and href.startswith("#"):
            self.internal_hrefs.append(href)


def test_polish_toc_links_match_generated_heading_ids() -> None:
    source = """## Spis treści

1. [Przepływ wiadomości](#1-przepływ-wiadomości)
2. [Workflow 01 — Intake](#2-workflow-01--intake)
3. [Bezpieczeństwo](#3-bezpieczeństwo)

## 1. Przepływ wiadomości

## 2. Workflow 01 — Intake

## 3. Bezpieczeństwo
"""

    rendered = builder.render_markdown(source)
    inventory = LinkInventory()
    inventory.feed(rendered)

    missing = [href for href in inventory.internal_hrefs if href[1:] not in inventory.ids]
    assert missing == []
