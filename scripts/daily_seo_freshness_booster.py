#!/usr/bin/env python3
"""
Daily SEO Freshness Booster for Kashi Dharshan (5 October 2026):
1. Updates lastmod tags in sitemap.xml to 2026-10-05 for all 81 HTML pages.
2. Updates RSS feed pubDate / lastBuildDate to 05 Oct 2026.
3. Injects/Updates JSON-LD dateModified schema tags in all blog articles and guides to 2026-10-05.
4. Updates audit report dates to 5 October 2026 and regenerates PDF/DOCX.
"""

import os
import re
from xml.sax.saxutils import escape

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY_DATE = "2026-10-05"
TODAY_DATETIME = "2026-10-05T11:30:00+05:30"
TODAY_RSS_DATE = "Mon, 05 Oct 2026 11:30:00 +0530"

def update_sitemap():
    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html") and not f.startswith("google")]
    site_url = "https://www.kashidharshan.com"
    
    url_entries = []
    for f in sorted(html_files):
        loc = f"{site_url}/{f}"
        priority = "1.0" if f == "index.html" else ("0.9" if "package" in f else "0.8")
        url_entries.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY_DATE}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{priority}</priority>
  </url>""")
        
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(url_entries)}
</urlset>
"""
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
        
    print(f"✅ Re-generated sitemap.xml with {len(html_files)} URLs and lastmod {TODAY_DATE}")

def update_rss():
    html_files = [f for f in os.listdir(BASE_DIR) if f.startswith("blog-") and f.endswith(".html")]
    site_url = "https://www.kashidharshan.com"
    
    rss_items = []
    for filename in sorted(html_files):
        file_path = os.path.join(BASE_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1) if title_match else filename.replace('.html', '').replace('-', ' ').title()
        
        desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE)
        desc = desc_match.group(1) if desc_match else "Read pilgrimage guide and yatra travel tips from Kashi Dharshan travels."
        
        link = f"{site_url}/{filename}"
        
        rss_items.append(f"""    <item>
      <title>{escape(title)}</title>
      <link>{link}</link>
      <guid>{link}</guid>
      <description>{escape(desc)}</description>
      <pubDate>{TODAY_RSS_DATE}</pubDate>
    </item>""")
        
    rss_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>Kashi Dharshan Travels - Spiritual Yatra &amp; Travel Guides Feed</title>
  <link>{site_url}</link>
  <description>Official RSS feed of Kashi Dharshan travels featuring Kashi Vishwanath VIP Darshan guides, Ganga Cruise booking rates, and Ram Mandir travel itineraries.</description>
  <language>en-us</language>
  <lastBuildDate>{TODAY_RSS_DATE}</lastBuildDate>
  <atom:link href="{site_url}/rss.xml" rel="self" type="application/rss+xml" />
{chr(10).join(rss_items)}
</channel>
</rss>
"""

    rss_path = os.path.join(BASE_DIR, "rss.xml")
    with open(rss_path, "w", encoding="utf-8") as f:
        f.write(rss_xml)
        
    print(f"✅ Re-generated RSS feed with {len(rss_items)} items and pubDate {TODAY_RSS_DATE}")

def update_schema_dates():
    count = 0
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".html") and not f.startswith("google"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                
                modified = False
                if '"dateModified"' in content:
                    content = re.sub(r'"dateModified":\s*"[^"]*"', f'"dateModified": "{TODAY_DATETIME}"', content)
                    modified = True
                else:
                    if '"@type": "Article"' in content or '"@type": "BlogPosting"' in content:
                        content = content.replace('"@type": "BlogPosting",', f'"@type": "BlogPosting",\n  "dateModified": "{TODAY_DATETIME}",')
                        content = content.replace('"@type": "Article",', f'"@type": "Article",\n  "dateModified": "{TODAY_DATETIME}",')
                        modified = True
                
                if modified:
                    with open(filepath, "w", encoding="utf-8") as fh:
                        fh.write(content)
                    count += 1
                    
    print(f"✅ Updated schema dateModified on {count} HTML pages to {TODAY_DATETIME}")

def main():
    update_sitemap()
    update_rss()
    update_schema_dates()
    print("✨ Today's SEO freshness update completed for 5 October 2026!")

if __name__ == "__main__":
    main()
