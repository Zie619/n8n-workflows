from __future__ import annotations

import base64
import html
import mimetypes
import re
import urllib.request
from pathlib import Path

import markdown
from markdown.extensions.toc import TocExtension

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "DOKUMENTACJA_TECHNICZNA_PL.md"
HTML_OUT = ROOT / "DOKUMENTACJA_TECHNICZNA_PL.html"
PDF_OUT = ROOT / "DOKUMENTACJA_TECHNICZNA_PL.pdf"
MERMAID_URL = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"


def github_slugify(value: str, separator: str) -> str:
    """Keep Unicode letters and emulate the anchors used in the Markdown TOC."""
    value = html.unescape(value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    return re.sub(r"\s", separator, value)


def render_markdown(source: str) -> str:
    return markdown.markdown(
        source,
        extensions=[
            "fenced_code",
            "tables",
            TocExtension(slugify=github_slugify),
            "sane_lists",
        ],
        output_format="html",
    )


def broken_internal_links(rendered: str) -> list[str]:
    ids = set(re.findall(r'\sid="([^"]+)"', rendered))
    hrefs = re.findall(r'\shref="#([^"]+)"', rendered)
    return [f"#{target}" for target in hrefs if target not in ids]


def embed_images(rendered: str) -> str:
    def replace(match: re.Match[str]) -> str:
        before, src, after = match.groups()
        if src.startswith(("data:", "http://", "https://")):
            return match.group(0)
        path = (ROOT / src).resolve()
        if not path.is_file() or ROOT not in path.parents:
            raise FileNotFoundError(f"Missing or unsafe image path: {src}")
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        payload = base64.b64encode(path.read_bytes()).decode("ascii")
        return f'<img{before}src="data:{mime};base64,{payload}"{after}>'

    return re.sub(r'<img([^>]*?)src="([^"]+)"([^>]*?)>', replace, rendered)


def render_mermaid_blocks(rendered: str) -> str:
    pattern = re.compile(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>', re.DOTALL
    )
    return pattern.sub(lambda m: f'<div class="mermaid">{html.unescape(m.group(1))}</div>', rendered)


def build_html() -> Path:
    source = SOURCE.read_text(encoding="utf-8")
    rendered = render_markdown(source)
    broken_links = broken_internal_links(rendered)
    if broken_links:
        raise ValueError(f"Broken internal links: {broken_links}")
    rendered = render_mermaid_blocks(rendered)
    rendered = embed_images(rendered)
    with urllib.request.urlopen(MERMAID_URL, timeout=60) as response:
        mermaid_js = response.read().decode("utf-8")

    page = f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dokumentacja techniczna — Resilient Gmail Triage</title>
<style>
:root{{--ink:#18212f;--muted:#5d6b7c;--line:#d9e1ea;--soft:#f4f7fa;--blue:#2563eb;--navy:#0f172a;--cyan:#0891b2;--amber:#b45309;}}
*{{box-sizing:border-box}}
body{{margin:0;background:#e8edf3;color:var(--ink);font:15px/1.58 Inter,Segoe UI,Arial,sans-serif}}
main{{max-width:1120px;margin:32px auto;background:#fff;padding:52px 64px;box-shadow:0 12px 40px #0f172a1c;border-radius:14px}}
h1{{font-size:34px;line-height:1.16;color:var(--navy);border-bottom:4px solid var(--blue);padding-bottom:16px}}
h2{{font-size:26px;color:var(--navy);margin-top:48px;padding-top:10px;border-top:1px solid var(--line)}}
h3{{font-size:19px;color:#1e3a5f;margin-top:30px}}
h4{{font-size:16px;color:#334155}}
p,li{{max-width:95ch}}
a{{color:var(--blue);text-decoration:none}}
blockquote{{margin:18px 0;padding:13px 18px;border-left:5px solid var(--amber);background:#fff8e8;color:#4b5563}}
code{{font-family:Consolas,JetBrains Mono,monospace;background:#eef2f7;padding:1px 5px;border-radius:4px;font-size:.91em}}
pre{{background:#0f172a;color:#e2e8f0;padding:18px 20px;border-radius:9px;overflow:auto;white-space:pre-wrap;word-break:break-word}}
pre code{{background:transparent;padding:0;color:inherit}}
table{{border-collapse:collapse;width:100%;margin:18px 0;font-size:13px;break-inside:avoid;page-break-inside:avoid}}
th{{background:#eaf1fb;color:#1e3a5f;text-align:left}}
th,td{{border:1px solid var(--line);padding:8px 10px;vertical-align:top}}
tr:nth-child(even) td{{background:#fafbfd}}
thead{{display:table-header-group}}
img{{display:block;max-width:100%;height:auto;margin:18px auto 28px;border:1px solid #cad5e1;border-radius:8px;box-shadow:0 5px 18px #0f172a1f}}
.mermaid{{margin:22px 0;padding:20px;background:#f8fafc;border:1px solid var(--line);border-radius:10px;text-align:center;overflow:hidden}}
.mermaid svg{{max-width:100%!important;height:auto!important}}
hr{{border:0;border-top:1px solid var(--line);margin:38px 0}}
#spis-treści + ol,#spis-treści + ul{{columns:2;column-gap:42px}}
@page{{size:A4;margin:15mm 14mm 17mm}}
@media print{{body{{background:#fff;font-size:10.5pt}}main{{max-width:none;margin:0;padding:0;box-shadow:none;border-radius:0}}hr{{display:none}}.page-break{{break-before:page;page-break-before:always}}h1{{font-size:25pt}}h2{{font-size:18pt;break-before:page;break-after:avoid;margin-top:0}}h3{{font-size:14pt;break-after:avoid}}h4{{break-after:avoid}}pre,blockquote,img,.mermaid{{break-inside:avoid}}table{{font-size:8.4pt;break-inside:avoid;page-break-inside:avoid}}thead{{display:table-header-group}}a{{color:inherit}}}}
</style>
</head>
<body><main>{rendered}</main>
<script>{mermaid_js}</script>
<script>
mermaid.initialize({{startOnLoad:true,theme:'base',securityLevel:'strict',flowchart:{{htmlLabels:true,useMaxWidth:true}},themeVariables:{{primaryColor:'#eaf1fb',primaryTextColor:'#18212f',primaryBorderColor:'#2563eb',lineColor:'#475569',secondaryColor:'#ecfeff',tertiaryColor:'#f8fafc'}}}});
</script>
</body></html>"""
    HTML_OUT.write_text(page, encoding="utf-8")
    return HTML_OUT


def build_pdf(html_path: Path) -> Path:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(html_path.as_uri(), wait_until="networkidle", timeout=120_000)
        page.wait_for_function(
            "document.querySelectorAll('.mermaid svg').length >= 4", timeout=120_000
        )
        page.pdf(
            path=str(PDF_OUT),
            format="A4",
            print_background=True,
            margin={"top": "15mm", "right": "14mm", "bottom": "17mm", "left": "14mm"},
        )
        browser.close()
    return PDF_OUT


if __name__ == "__main__":
    html_path = build_html()
    pdf_path = build_pdf(html_path)
    print(f"HTML={html_path} ({html_path.stat().st_size} bytes)")
    print(f"PDF={pdf_path} ({pdf_path.stat().st_size} bytes)")
