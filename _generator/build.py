#!/usr/bin/env python3
"""
Build script for India Everyday Tools.
Generates every static .html page from shared header/footer templates
plus per-page content. Run: python3 build.py
Output goes to the project root (same folder as this script).
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "India Everyday Tools"
SITE_URL = "https://www.india-everyday-tools.onrender.com"  # placeholder — update after you buy a domain

FONT_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&'
    'family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
)

NAV_ITEMS = [
    ("Home", "index.html"),
    ("All Tools", "all-tools.html"),
    ("Categories", "all-tools.html#categories"),
    ("Popular Tools", "index.html#popular"),
]

BRAND_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="7" x2="16" y2="7"/><line x1="8" y1="11" x2="8" y2="11"/><line x1="12" y1="11" x2="12" y2="11"/><line x1="16" y1="11" x2="16" y2="11"/><line x1="8" y1="15" x2="8" y2="15"/><line x1="12" y1="15" x2="12" y2="15"/><line x1="16" y1="15" x2="16" y2="15"/></svg>'


def nav_html(mobile=False):
    cls = "" if not mobile else ""
    links = []
    for label, href in NAV_ITEMS:
        links.append(f'<a href="{href}">{label}</a>')
    return "\n      ".join(links)


def header_html():
    nav = nav_html()
    return f"""  <header class="site-header">
    <div class="header-inner container">
      <a href="index.html" class="brand">
        <span class="brand-mark">{BRAND_SVG}</span>
        <span>India Everyday Tools<small>Simple tools for everyday calculations</small></span>
      </a>
      <nav class="main-nav" aria-label="Primary">
        {nav}
      </nav>
      <div class="header-actions">
        <form class="header-search search-wrap" id="headerSearchForm" role="search">
          {ICON_SEARCH_SM}
          <input type="text" id="headerSearchInput" placeholder="Search for a calculator..." aria-label="Search for a calculator" autocomplete="off">
          <div class="search-results" id="headerSearchResults"></div>
        </form>
        <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
      </div>
    </div>
    <div class="mobile-panel">
      <form class="header-search search-wrap" role="search" onsubmit="return false;">
        {ICON_SEARCH_SM}
        <input type="text" placeholder="Search for a calculator..." aria-label="Search for a calculator" oninput="document.getElementById('headerSearchInput').value=this.value; document.getElementById('headerSearchInput').dispatchEvent(new Event('input'));">
      </form>
      <nav aria-label="Mobile">
        {nav}
      </nav>
    </div>
  </header>"""


ICON_SEARCH_SM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>'


def footer_html():
    return """  <footer class="site-footer">
    <div class="footer-inner">
      <div>
        <div class="footer-brand">India Everyday Tools</div>
        <p>Free, fast, everyday calculators and converters for India. Every calculation runs locally in your browser — no sign-up, no data collection.</p>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="all-tools.html">All Calculators</a></li>
          <li><a href="all-tools.html#categories">Categories</a></li>
          <li><a href="index.html#popular">Popular Tools</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="privacy-policy.html">Privacy Policy</a></li>
          <li><a href="terms-of-use.html">Terms of Use</a></li>
          <li><a href="disclaimer.html">Disclaimer</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      &copy; <span id="footerYear"></span> <strong>India Everyday Tools</strong>. All calculations are for general informational purposes only.
    </div>
  </footer>
  <script>document.getElementById('footerYear').textContent = new Date().getFullYear();</script>"""


def page(*, title, description, slug, body, extra_head="", extra_scripts="", canonical=None, og_type="website"):
    canonical_url = canonical or f"{SITE_URL}/{slug}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical_url}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical_url}">
<meta name="twitter:card" content="summary">
<meta name="robots" content="index, follow">
{FONT_LINK}
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><rect width=%2224%22 height=%2224%22 rx=%226%22 fill=%22%23E34234%22/></svg>">
{extra_head}
</head>
<body>
{header_html()}
<main>
{body}
</main>
{footer_html()}
<script src="assets/js/main.js"></script>
{extra_scripts}
</body>
</html>
"""


def breadcrumb(current, current_label=None):
    label = current_label or current
    return f"""  <nav class="breadcrumb" aria-label="Breadcrumb">
    <div class="container">
      <a href="index.html">Home</a> <span class="sep">/</span> <a href="all-tools.html">All Tools</a> <span class="sep">/</span> <span class="current">{label}</span>
    </div>
  </nav>"""


def faq_html(items):
    out = []
    for q, a in items:
        out.append(f"""      <details class="faq-item">
        <summary>{q} <span class="plus">+</span></summary>
        <p>{a}</p>
      </details>""")
    return "\n".join(out)


def calc_page(*, slug, title, meta_desc, h1, intro, calc_card_inner, info_sections, faq_items, related_ids, related_container_id="relatedTools", extra_script=""):
    """Assemble a full calculator page: hero head + calc card + info + faq + related."""
    body = f"""{breadcrumb(slug, h1)}
  <section class="calc-page-head">
    <div class="container">
      <h1>{h1}</h1>
      <p class="intro">{intro}</p>
    </div>
  </section>
  <section class="calc-layout">
    <div class="calc-card">
{calc_card_inner}
    </div>
  </section>
  <section class="calc-info">
{info_sections}
    <h2>Frequently Asked Questions</h2>
{faq_html(faq_items)}
    <h2>Related Calculators</h2>
    <div class="related-tools" id="{related_container_id}"></div>
  </section>"""
    script = f"""<script>
  renderRelated('#{related_container_id}', {related_ids!r});
</script>
{extra_script}"""
    return page(title=title, description=meta_desc, slug=slug, body=body, extra_scripts=script)


def write(slug, html):
    path = os.path.join(ROOT, slug)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", slug)


if __name__ == "__main__":
    print("Run generate_pages.py to build the full site (this file only holds shared helpers).")
