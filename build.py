#!/usr/bin/env python3
"""Torpie Digital static site builder.

Zero-dependency generator. Shared layout and components live here;
page content lives in pages/*.py. Run `python3 build.py` from the
site root to regenerate every page plus sitemap.xml and robots.txt.
"""

import importlib
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
BASE_URL = "https://torpiedigital.com"

PAGES = [
    ("home", "", "Home"),
    ("websites", "websites/", "Websites"),
    ("plans", "plans/", "Plans"),
    ("work", "work/", "Work"),
    ("pricing", "pricing/", "Pricing"),
    ("about", "about/", "About"),
]

NAV_ITEMS = [
    ("Websites", "/websites/"),
    ("Plans", "/plans/"),
    ("Work", "/work/"),
    ("Pricing", "/pricing/"),
    ("About", "/about/"),
]

LOGO_MARK = (
    '<svg class="logo__mark" viewBox="0 0 40 40" aria-hidden="true" focusable="false">'
    '<rect x="2" y="2" width="36" height="36" rx="9" fill="#1E6B4F"/>'
    '<path d="M11 21.5 L17 27.5 L29 13.5" fill="none" stroke="#FAF8F4" '
    'stroke-width="4.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

CHECK_CHIP = (
    '<span class="chip" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" '
    'stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke="currentColor">'
    '<path d="M4 12.5 L10 18.5 L20 6.5"/></svg></span>'
)


def check_item(text):
    return f'<li>{CHECK_CHIP}<span>{text}</span></li>'


def check_list(items, inline=False, extra_class=""):
    cls = "check-list" + (" check-list--inline" if inline else "")
    if extra_class:
        cls += " " + extra_class
    lis = "".join(check_item(t) for t in items)
    return f'<ul class="{cls}">{lis}</ul>'


def eyebrow(text, center=False):
    cls = "eyebrow eyebrow--center" if center else "eyebrow"
    return f'<span class="{cls}">{text}</span>'


def browser_frame(url_label, placeholder_label, image=None, alt=""):
    if image:
        body = f'<img src="{image}" alt="{alt}" loading="lazy" width="1280" height="840">'
    else:
        body = (
            '<div class="placeholder-shot">'
            '<svg viewBox="0 0 24 24" fill="none" stroke="#1E6B4F" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<rect x="3" y="4" width="18" height="14" rx="2"/>'
            '<path d="M3 9h18M7 6.5h.01M10 6.5h.01"/></svg>'
            f'<span>{placeholder_label}</span></div>'
        )
    return (
        '<figure class="browser-frame reveal">'
        '<div class="browser-frame__bar"><span class="browser-frame__dots">'
        '<span></span><span></span><span></span></span>'
        f'<span class="browser-frame__url">{url_label}</span></div>'
        f'<div class="browser-frame__body">{body}</div></figure>'
    )


def faq_section(heading, items, dark_cta=None, section_class="section"):
    details = "".join(
        f'<details><summary>{q}</summary>'
        f'<div class="faq__answer">{a}</div></details>'
        for q, a in items
    )
    return (
        f'<section class="{section_class}" aria-labelledby="faq-heading">'
        '<div class="container">'
        '<div class="section-head section-head--center">'
        f'<h2 id="faq-heading">{heading}</h2></div>'
        f'<div class="faq reveal">{details}</div></div></section>'
    )


def faq_schema(items):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in items
        ],
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


def dark_cta(heading, body, button_label="Get a quote", button_href="/about/#contact"):
    body_html = f"<p>{body}</p>" if body else ""
    return (
        '<section class="section section--dark" aria-labelledby="final-cta-heading">'
        '<div class="container center reveal">'
        f'<h2 id="final-cta-heading">{heading}</h2>{body_html}'
        f'<p class="mt-4"><a class="btn btn-primary" data-track-cta="final-cta" '
        f'href="{button_href}">{button_label}</a></p>'
        "</div></section>"
    )


def head(title, description, path, extra_schema=""):
    canonical = BASE_URL + "/" + path
    org_schema = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Torpie Digital",
        "url": BASE_URL,
        "description": "Torpie Digital builds custom websites for local businesses "
                       "and takes care of them after launch: hosting, updates, "
                       "reviews, and Google presence.",
        "founder": {"@type": "Person", "name": "Aiden Torpie"},
        "areaServed": "United States",
        "address": {"@type": "PostalAddress", "addressRegion": "NY",
                    "addressCountry": "US"},
    }
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Torpie Digital">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#1E6B4F">
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<!-- GOOGLE SEARCH CONSOLE: paste the verification meta tag on the next line before launch -->
<!-- <meta name="google-site-verification" content="TOKEN"> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/css/main.css">
<script type="application/ld+json">{json.dumps(org_schema)}</script>
{extra_schema}
</head>"""


def header(active_path):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == active_path else ""}>{label}</a>'
        for label, href in NAV_ITEMS
    )
    return f"""<body>
<a class="skip-link" href="#main">Skip to main content</a>
<div class="announcement" data-announcement hidden>
  <div class="container announcement__inner">
    <span>Founding client rates are open. Lock in your price. <a href="/pricing/">See pricing</a></span>
    <button class="announcement__close" type="button" data-announcement-close aria-label="Dismiss announcement">&#10005;</button>
  </div>
</div>
<header class="site-header">
  <div class="container site-header__inner">
    <a class="logo" href="/" aria-label="Torpie Digital home">
      {LOGO_MARK}
      <span class="logo__wordmark">torpie digital</span>
    </a>
    <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav" aria-label="Menu">
      <svg class="icon-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
    <nav class="site-nav" id="site-nav" data-nav aria-label="Main">
      {links}
      <a class="btn btn-primary" data-track-cta="nav" href="/about/#contact">Get a quote</a>
    </nav>
  </div>
</header>
<main id="main">"""


FOOTER = f"""</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo" href="/" aria-label="Torpie Digital home">
          {LOGO_MARK}
          <span class="logo__wordmark">torpie digital</span>
        </a>
        <p class="footer-tagline">Websites that work for a living.</p>
      </div>
      <nav class="footer-nav" aria-label="Footer">
        <a href="/websites/">Websites</a>
        <a href="/plans/">Plans</a>
        <a href="/work/">Work</a>
        <a href="/pricing/">Pricing</a>
        <a href="/about/">About</a>
      </nav>
      <div class="flow">
        <p>[EMAIL] &middot; [PHONE]</p>
        <p>Remote-based in New York. Serving local businesses everywhere.</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Torpie Digital</span>
      <a href="/about/#contact">Get a quote</a>
    </div>
  </div>
</footer>
<div class="sticky-cta" data-sticky-cta>
  <a class="btn btn-primary btn-block" data-track-cta="sticky-mobile" href="/about/#contact">Get a quote</a>
</div>
<script src="/assets/js/main.js" defer></script>
</body>
</html>"""


def build():
    for module_name, path, _label in PAGES:
        page = importlib.import_module(f"pages.{module_name}")
        active = "/" + path if path else "/"
        html = (
            head(page.TITLE, page.DESCRIPTION, path, getattr(page, "EXTRA_SCHEMA", ""))
            + header(active)
            + page.BODY
            + FOOTER
        )
        out = ROOT / path / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"built {out.relative_to(ROOT)}")

    urls = "".join(
        f"<url><loc>{BASE_URL}/{path}</loc></url>" for _m, path, _l in PAGES
    )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urls}</urlset>",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n", encoding="utf-8"
    )
    print("built sitemap.xml, robots.txt")


if __name__ == "__main__":
    build()
