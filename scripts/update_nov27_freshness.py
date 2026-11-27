import os
import re
import xml.etree.ElementTree as ET

BASE_DIR = '/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan'
TODAY_DATE = "2026-11-27"
TODAY_DATETIME = "2026-11-27T15:15:00+05:30"
TODAY_RSS_DATE = "Fri, 27 Nov 2026 15:15:00 +0530"

# 1. Update Sitemap lastmod
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
tree = ET.parse(sitemap_path)
root = tree.getroot()
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

count = 0
for url in root.findall('sm:url', ns):
    lastmod = url.find('sm:lastmod', ns)
    if lastmod is not None:
        lastmod.text = TODAY_DATE
        count += 1

ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
ET.register_namespace('image', 'http://www.google.com/schemas/sitemap-image/1.1')
tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
print(f"✅ Updated {count} URLs in sitemap.xml to {TODAY_DATE}")

# 2. Update RSS Feed
rss_path = os.path.join(BASE_DIR, "rss.xml")
with open(rss_path, "r", encoding="utf-8") as f:
    rss_content = f.read()

rss_content = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{TODAY_RSS_DATE}</lastBuildDate>', rss_content)
with open(rss_path, "w", encoding="utf-8") as f:
    f.write(rss_content)
print(f"✅ Updated rss.xml lastBuildDate to {TODAY_RSS_DATE}")

# 3. Update dateModified in all HTML
schema_count = 0
for root_dir, _, files in os.walk(BASE_DIR):
    for f in files:
        if f.endswith('.html') and not f.startswith('google'):
            fpath = os.path.join(root_dir, f)
            with open(fpath, 'r', encoding='utf-8') as fh:
                cnt = fh.read()
            if '"dateModified"' in cnt:
                cnt = re.sub(r'"dateModified":\s*"[^"]*"', f'"dateModified": "{TODAY_DATETIME}"', cnt)
                with open(fpath, 'w', encoding='utf-8') as fh:
                    fh.write(cnt)
                schema_count += 1
print(f"✅ Updated schema dateModified to {TODAY_DATETIME} in {schema_count} files")

