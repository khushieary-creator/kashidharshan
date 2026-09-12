import os
import re
from xml.sax.saxutils import escape

def generate_rss():
    base_dir = "/Users/rishabhjaiswal/ayodhya-darshan"
    site_url = "https://www.ayodhyadharshan.com"
    
    html_files = [f for f in os.listdir(base_dir) if f.startswith("blog-") and f.endswith(".html")]
    
    rss_items = []
    
    for filename in sorted(html_files):
        file_path = os.path.join(base_dir, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1) if title_match else filename.replace('.html', '').replace('-', ' ').title()
        
        desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE)
        desc = desc_match.group(1) if desc_match else "Read pilgrimage guide and yatra travel tips from Ayodhya Dharshan travels."
        
        link = f"{site_url}/{filename}"
        
        rss_items.append(f"""    <item>
      <title>{escape(title)}</title>
      <link>{link}</link>
      <guid>{link}</guid>
      <description>{escape(desc)}</description>
      <pubDate>Tue, 01 Sep 2026 00:00:00 +0530</pubDate>
    </item>""")
        
    rss_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>Ayodhya Dharshan Travels - Spiritual Yatra &amp; Travel Guides Feed</title>
  <link>{site_url}</link>
  <description>Official RSS feed of Ayodhya Dharshan travels featuring Ram Mandir VIP Darshan guides, Kashi Ganga Cruise booking rates, and travel itineraries.</description>
  <language>en-us</language>
  <atom:link href="{site_url}/rss.xml" rel="self" type="application/rss+xml" />
{chr(10).join(rss_items)}
</channel>
</rss>
"""

    rss_path = os.path.join(base_dir, "rss.xml")
    with open(rss_path, "w", encoding="utf-8") as f:
        f.write(rss_xml)
        
    print(f"✅ Generated RSS 2.0 feed with {len(rss_items)} articles at: {rss_path}")

if __name__ == "__main__":
    generate_rss()
