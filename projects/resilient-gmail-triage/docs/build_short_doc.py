from __future__ import annotations

import urllib.request
from pathlib import Path

from build_technical_doc import embed_images, render_markdown, render_mermaid_blocks

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "DOKUMENTACJA_REKRUTACYJNA_PL.md"
HTML_OUT = ROOT / "DOKUMENTACJA_REKRUTACYJNA_PL.html"
PDF_OUT = ROOT / "DOKUMENTACJA_REKRUTACYJNA_PL.pdf"
MERMAID_URL = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"


def build_html() -> Path:
    rendered = render_markdown(SOURCE.read_text(encoding="utf-8"))
    rendered = render_mermaid_blocks(rendered)
    rendered = embed_images(rendered)
    with urllib.request.urlopen(MERMAID_URL, timeout=60) as response:
        mermaid_js = response.read().decode("utf-8")

    page = f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Automatyczna obsługa skrzynki kontaktowej</title>
<style>
:root{{--ink:#172033;--muted:#536174;--line:#d8e0e9;--blue:#176b87;--pale:#eff7f9;--white:#fff}}
*{{box-sizing:border-box}}
body{{margin:0;background:#eef2f6;color:var(--ink);font-family:Inter,"Segoe UI",Arial,sans-serif;line-height:1.48}}
main{{max-width:900px;margin:30px auto;padding:52px 64px;background:var(--white);box-shadow:0 6px 18px #1720331a}}
h1{{margin:0 0 24px;color:#124f68;font-size:38px;line-height:1.08;letter-spacing:-.025em}}
h2{{margin:42px 0 18px;padding-bottom:9px;border-bottom:2px solid #75b5c4;color:#124f68;font-size:25px;line-height:1.18}}
h3{{margin:22px 0 8px;font-size:16px;color:#21364b}}
p{{margin:9px 0}}
strong{{color:#142b3d}}
a{{color:#075f84}}
blockquote{{margin:24px 0;padding:14px 18px;background:var(--pale);border:1px solid #bcd9df;border-radius:8px;color:#29495a}}
ul,ol{{padding-left:22px;margin:9px 0}}
li{{margin:4px 0}}
table{{width:100%;border-collapse:collapse;margin:13px 0 17px;font-size:12.5px}}
th,td{{padding:7px 8px;border:1px solid var(--line);vertical-align:top;text-align:left}}
th{{background:#e7f2f5;color:#17384a}}
code{{font-family:"SFMono-Regular",Consolas,monospace;font-size:.9em;background:#edf2f6;padding:1px 4px;border-radius:3px}}
pre code{{background:transparent;padding:0}}
.mermaid{{margin:14px 0;padding:10px;background:#f8fbfc;border:1px solid var(--line);border-radius:8px;text-align:center}}
.mermaid svg{{max-width:100%!important;height:auto!important}}
img{{display:block;max-width:100%;max-height:320px;width:auto;height:auto;margin:12px auto 18px;border:1px solid #c8d3de;border-radius:7px}}
main>h1:first-child{{margin-top:125px;font-size:43px;max-width:680px}}
main>h1:first-child~p{{max-width:700px}}
@page{{size:A4;margin:13mm 13mm 14mm}}
@media print{{
  body{{background:#fff;font-size:9.25pt;line-height:1.38}}
  main{{max-width:none;margin:0;padding:0;box-shadow:none}}
  main>h1:first-child{{margin-top:48mm;font-size:30pt}}
  h1{{font-size:30pt}}
  h2{{break-before:page;margin-top:0;font-size:17pt;break-after:avoid}}
  h3{{font-size:11pt;break-after:avoid;margin-top:14px}}
  p{{margin:6px 0}}
  ul,ol{{margin:6px 0}}
  li{{margin:2px 0}}
  table{{font-size:7.4pt;margin:8px 0 10px;break-inside:avoid}}
  th,td{{padding:4px 5px}}
  blockquote,img,.mermaid{{break-inside:avoid}}
  blockquote{{margin:12px 0;padding:9px 11px}}
  img{{max-height:58mm;margin:8px auto 10px}}
  img[alt*="Lokalna konsola"]{{max-height:92mm}}
  .mermaid{{max-height:83mm;margin:8px 0;padding:5px}}
  .mermaid svg{{max-height:79mm!important}}
}}
</style>
</head>
<body><main>{rendered}</main>
<script>{mermaid_js}</script>
<script>
mermaid.initialize({{startOnLoad:true,theme:'base',securityLevel:'strict',flowchart:{{htmlLabels:true,useMaxWidth:true}},themeVariables:{{primaryColor:'#e7f2f5',primaryTextColor:'#172033',primaryBorderColor:'#176b87',lineColor:'#536174',secondaryColor:'#eff7f9',tertiaryColor:'#ffffff'}}}});
</script>
</body></html>"""
    HTML_OUT.write_text(page, encoding="utf-8")
    return HTML_OUT


def build_pdf(html_path: Path) -> Path:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(html_path.as_uri(), wait_until="networkidle", timeout=120_000)
        page.wait_for_function("document.querySelectorAll('.mermaid svg').length >= 1", timeout=120_000)
        page.pdf(
            path=str(PDF_OUT),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()
    return PDF_OUT


def main() -> None:
    html_path = build_html()
    pdf_path = build_pdf(html_path)
    print(f"Wrote {html_path}")
    print(f"Wrote {pdf_path}")


if __name__ == "__main__":
    main()
