import re
import os
import xml.etree.ElementTree as ET

BASE_DIR = '/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan'
TODAY_DATE = "2026-11-28"
TODAY_DATETIME = "2026-11-28T14:45:00+05:30"
TODAY_RSS_DATE = "Sat, 28 Nov 2026 14:45:00 +0530"

print(f"🚀 Running Daily SEO Hyper-Boost for {TODAY_DATE}...")

# 1. FIX KASHI-VISHWANATH-TOUR-PACKAGE.HTML CANNIBALIZATION
kv_path = os.path.join(BASE_DIR, 'kashi-vishwanath-tour-package.html')
with open(kv_path, 'r', encoding='utf-8') as f:
    kv_content = f.read()

# Update Title & Meta Description
kv_content = re.sub(
    r'<title>(.*?)</title>',
    '<title>Kashi Vishwanath Tour Package 2026 | VIP Sugam Pass &amp; Cab</title>',
    kv_content,
    flags=re.IGNORECASE
)
kv_content = re.sub(
    r'<meta\s+name="description"\s+content="[^"]*"',
    '<meta name="description" content="Book official Kashi Vishwanath Tour Package 2026. Includes Sugam Darshan VIP pass, Mangla Aarti assistance, Annapurna Mandir &amp; AC cab. 4.9★ rated local agency.">',
    kv_content,
    flags=re.IGNORECASE
)
# Update H1
kv_content = re.sub(
    r'<h1 class="display hero-title-2line">.*?</h1>',
    '<h1 class="display hero-title-2line"><span class="hero-line-1">Kashi Vishwanath Tour Package 2026: </span> <span class="hero-line-2">VIP Sugam Darshan, Mangla Aarti &amp; Mandir Guide</span></h1>',
    kv_content,
    flags=re.DOTALL
)
# Update Breadcrumb
kv_content = re.sub(
    r'<p class="crumb"><a href="/">Home</a> &nbsp;/&nbsp; <a href="services">Services</a> &nbsp;/&nbsp; Varanasi Kashi Darshan Tour</p>',
    '<p class="crumb"><a href="/">Home</a> &nbsp;/&nbsp; <a href="services">Services</a> &nbsp;/&nbsp; Kashi Vishwanath Tour Package</p>',
    kv_content
)
with open(kv_path, 'w', encoding='utf-8') as f:
    f.write(kv_content)
print("✅ Hyper-optimized kashi-vishwanath-tour-package.html (Resolved cannibalization with varanasi-tour-package)")

# 2. INJECT VISUAL BREADCRUMBS IN 9 CITY-TO-AYODHYA PAGES
city_pages = [
    ('delhi-to-ayodhya-tour-package.html', 'Delhi to Ayodhya Tour Package'),
    ('mumbai-to-ayodhya-tour-package.html', 'Mumbai to Ayodhya Tour Package'),
    ('bengaluru-to-ayodhya-tour-package.html', 'Bengaluru to Ayodhya Tour Package'),
    ('hyderabad-to-ayodhya-tour-package.html', 'Hyderabad to Ayodhya Tour Package'),
    ('ahmedabad-to-ayodhya-tour-package.html', 'Ahmedabad to Ayodhya Tour Package'),
    ('kolkata-to-ayodhya-tour-package.html', 'Kolkata to Ayodhya Tour Package'),
    ('chennai-to-ayodhya-tour-package.html', 'Chennai to Ayodhya Tour Package'),
    ('patna-to-ayodhya-tour-package.html', 'Patna to Ayodhya Tour Package'),
    ('lucknow-to-ayodhya-same-day-tour-package.html', 'Lucknow to Ayodhya Same Day Tour')
]

for filename, page_title in city_pages:
    fpath = os.path.join(BASE_DIR, filename)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    crumb_html = f'<p class="crumb" style="font-size:0.85rem; margin-bottom:12px; color:var(--ink-2);"><a href="/" style="color:var(--ink-2); text-decoration:none;">Home</a> &nbsp;/&nbsp; <a href="destinations" style="color:var(--ink-2); text-decoration:none;">Destinations</a> &nbsp;/&nbsp; <span style="color:var(--saffron-deep);">{page_title}</span></p>'
    
    if '<p class="crumb"' not in content:
        # Insert right after <header class="section section--tight center" ...><div class="container" ...>
        target = '<div class="container" style="max-width:800px;">'
        if target in content:
            content = content.replace(target, f'{target}\n    {crumb_html}', 1)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Injected visual breadcrumb in {filename}")

# 3. UPDATE SITEMAP LASTMOD TO TODAY_DATE (2026-11-28)
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
tree = ET.parse(sitemap_path)
root = tree.getroot()
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

sitemap_count = 0
for url in root.findall('sm:url', ns):
    lastmod = url.find('sm:lastmod', ns)
    if lastmod is not None:
        lastmod.text = TODAY_DATE
        sitemap_count += 1

ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
ET.register_namespace('image', 'http://www.google.com/schemas/sitemap-image/1.1')
tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
print(f"✅ Updated {sitemap_count} URLs in sitemap.xml to {TODAY_DATE}")

# 4. UPDATE RSS FEED BUILD DATE
rss_path = os.path.join(BASE_DIR, "rss.xml")
with open(rss_path, "r", encoding="utf-8") as f:
    rss_content = f.read()

rss_content = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', f'<lastBuildDate>{TODAY_RSS_DATE}</lastBuildDate>', rss_content)
with open(rss_path, "w", encoding="utf-8") as f:
    f.write(rss_content)
print(f"✅ Updated rss.xml lastBuildDate to {TODAY_RSS_DATE}")

# 5. UPDATE SCHEMA DATEMODIFIED IN ALL HTML
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

print("✨ Daily SEO Hyper-Boost completed successfully!")
