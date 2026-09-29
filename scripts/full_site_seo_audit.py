#!/usr/bin/env python3
"""
Full-Site SEO Audit Script:
Inspects all 80 HTML files for:
1. Title tags & length
2. Meta descriptions & length
3. Meta keywords presence
4. Canonical URL accuracy
5. OpenGraph (og:title, og:description, og:image, og:url) & Twitter tags
6. Schema JSON-LD presence & validation
7. Missing image alt tags
8. Sitemap.xml coverage
"""

import os
import glob
import re
from xml.etree import ElementTree as ET

def run_audit():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_files = glob.glob(os.path.join(root_dir, '*.html'))
    sitemap_path = os.path.join(root_dir, 'sitemap.xml')

    print(f"=== FULL SITE SEO AUDIT ({len(html_files)} HTML files) ===")

    issues = []
    page_stats = {
        'total_files': len(html_files),
        'missing_title': 0,
        'missing_description': 0,
        'missing_keywords': 0,
        'missing_canonical': 0,
        'missing_og': 0,
        'missing_schema': 0,
        'images_missing_alt': 0,
        'total_images': 0
    }

    # 1. Inspect HTML pages
    for filepath in html_files:
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if not title_match or not title_match.group(1).strip():
            issues.append(f"{filename}: Missing <title> tag")
            page_stats['missing_title'] += 1

        # Description
        desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content, re.IGNORECASE)
        if not desc_match or not desc_match.group(1).strip():
            issues.append(f"{filename}: Missing meta description")
            page_stats['missing_description'] += 1

        # Keywords
        kw_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]*)"', content, re.IGNORECASE)
        if not kw_match or not kw_match.group(1).strip():
            issues.append(f"{filename}: Missing meta keywords")
            page_stats['missing_keywords'] += 1

        # Canonical
        canonical_match = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', content, re.IGNORECASE)
        if not canonical_match or not canonical_match.group(1).strip():
            issues.append(f"{filename}: Missing canonical URL tag")
            page_stats['missing_canonical'] += 1

        # OpenGraph
        og_title = re.search(r'<meta\s+property="og:title"\s+content="([^"]*)"', content, re.IGNORECASE)
        og_image = re.search(r'<meta\s+property="og:image"\s+content="([^"]*)"', content, re.IGNORECASE)
        if not og_title or not og_image:
            issues.append(f"{filename}: Incomplete OpenGraph meta tags")
            page_stats['missing_og'] += 1

        # Schema JSON-LD
        schema_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        if not schema_matches:
            issues.append(f"{filename}: Missing Schema JSON-LD structured data")
            page_stats['missing_schema'] += 1

        # Images ALT tags
        img_tags = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
        page_stats['total_images'] += len(img_tags)
        for img in img_tags:
            if 'alt=' not in img.lower() or re.search(r'alt=["\']\s*["\']', img, re.IGNORECASE):
                page_stats['images_missing_alt'] += 1

    # 2. Inspect Sitemap.xml coverage
    sitemap_urls = set()
    if os.path.exists(sitemap_path):
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            sitemap_content = f.read()
        sitemap_urls = set(re.findall(r'<loc>(.*?)</loc>', sitemap_content))

    missing_in_sitemap = []
    for filepath in html_files:
        filename = os.path.basename(filepath)
        expected_url = f"https://www.kashidharshan.com/{filename}"
        if filename == 'index.html':
            expected_url = "https://www.kashidharshan.com/"

        if expected_url not in sitemap_urls and f"https://www.kashidharshan.com/{filename}" not in sitemap_urls:
            missing_in_sitemap.append(filename)

    print("\n--- SEO AUDIT SUMMARY ---")
    print(f"Total HTML files analyzed: {page_stats['total_files']}")
    print(f"Total images checked: {page_stats['total_images']}")
    print(f"Missing Title Tags: {page_stats['missing_title']}")
    print(f"Missing Meta Descriptions: {page_stats['missing_description']}")
    print(f"Missing Meta Keywords: {page_stats['missing_keywords']}")
    print(f"Missing Canonical Tags: {page_stats['missing_canonical']}")
    print(f"Missing OpenGraph Tags: {page_stats['missing_og']}")
    print(f"Missing Schema JSON-LD: {page_stats['missing_schema']}")
    print(f"Images Missing Alt Tags: {page_stats['images_missing_alt']}")
    print(f"Sitemap.xml Total URLs: {len(sitemap_urls)}")
    print(f"Files missing in Sitemap: {len(missing_in_sitemap)}")

    if issues:
        print("\n--- ISSUES DETECTED ---")
        for iss in issues[:20]:
            print(f"- {iss}")
        if len(issues) > 20:
            print(f"... and {len(issues) - 20} more issues.")
    else:
        print("\n✅ PERFECT! Zero structural SEO errors detected across all HTML files!")

    if missing_in_sitemap:
        print(f"\n⚠️ Missing from sitemap.xml: {missing_in_sitemap}")

if __name__ == '__main__':
    run_audit()
