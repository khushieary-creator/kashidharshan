#!/usr/bin/env python3
import os
import re

ROOT = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan"

# ==========================================
# 1. Update index.html
# ==========================================
index_path = os.path.join(ROOT, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_c = f.read()

# 1a. Add AEO Direct Answer Box right above Section id="destinations"
aeo_box = """    <!-- AEO DIRECT ANSWER CALLOUT BOX FOR KASHI DARSHAN -->
    <div class="aeo-direct-answer container" style="background: #fffcf7; border: 2px solid #b45309; border-radius: 14px; padding: 26px 24px; margin: 36px auto 20px; max-width: 1100px; box-shadow: 0 4px 18px rgba(180, 83, 9, 0.1);">
      <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
        <span style="font-size: 26px;">🛕</span>
        <h2 style="color: #78350f; margin: 0; font-size: 1.4rem; font-family: var(--font-display);">What is Kashi Darshan &amp; How to Plan Your 2026 Pilgrimage?</h2>
      </div>
      <p style="color: #44403c; line-height: 1.75; font-size: 1rem; margin-bottom: 16px;">
        <strong>Kashi Darshan</strong> is the sacred Hindu pilgrimage to Varanasi (the eternal city of Moksha), centered around seeking the blessings of Lord Shiva at <strong>Shri Kashi Vishwanath Dham</strong> (one of the 12 Jyotirlingas). A traditional complete Kashi Darshan covers taking a holy snan at Manikarnika or Dashashwamedh Ghat, worship at <strong>Maa Annapurna Mandir</strong>, obtaining formal pilgrimage sanction from <strong>Kaal Bhairav (Kotwal of Kashi)</strong>, attending the world-famous evening <strong>Ganga Aarti</strong> by private boat, experiencing sunrise <strong>Subah-e-Banaras</strong> at Assi Ghat, and visiting Sankat Mochan, Durga Kund, and <strong>Sarnath</strong>.
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px; background: #fff8f0; padding: 16px; border-radius: 10px; border: 1px dashed #d97706;">
        <div><strong style="color:#92400e;">⏱️ Ideal Duration:</strong> 1 Day (Same Day Darshan) to 3 Days (Full Circuit)</div>
        <div><strong style="color:#92400e;">🎫 VIP Sugam Darshan:</strong> ₹300/person (Direct entry via Gate 4B, zero queue)</div>
        <div><strong style="color:#92400e;">💰 Package Starting Price:</strong> ₹1,499/person (Day Tour) to ₹4,999/person (with Hotel)</div>
        <div><strong style="color:#92400e;">📞 24×7 Local Helpline:</strong> <a href="tel:+917011960307" style="color:#b45309; font-weight:700;">+91 70119 60307</a></div>
      </div>
    </div>
"""

if "aeo-direct-answer" not in idx_c:
    target_dest = '<section class="section" id="destinations">'
    if target_dest in idx_c:
        idx_c = idx_c.replace(target_dest, aeo_box + "\n" + target_dest)
        print("✅ Added AEO Direct Answer Box to index.html")
    else:
        print("❌ Could not find target destination section in index.html")
else:
    print("ℹ️ AEO box already in index.html")

# 1b. Add SpeakableSpecification to TravelAgency schema in index.html
if "SpeakableSpecification" not in idx_c:
    target_schema = '"legalName": "Kashi Dharshan Teerth Yatra",'
    speakable_json = """"legalName": "Kashi Dharshan Teerth Yatra",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".aeo-direct-answer", ".hero-title-2line", ".lead"]
  },"""
    if target_schema in idx_c:
        idx_c = idx_c.replace(target_schema, speakable_json)
        print("✅ Added SpeakableSpecification schema to index.html")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_c)


# ==========================================
# 2. Update blog.html
# ==========================================
blog_path = os.path.join(ROOT, "blog.html")
with open(blog_path, "r", encoding="utf-8") as f:
    blog_c = f.read()

traffic_blog_card = """      <!-- VARANASI DEV DEEPAWALI 2026 TRAFFIC ADVISORY -->
      <article class="card blog-card reveal" style="border: 2.5px solid #dc2626; background: #fffcf7;">
        <a href="blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Dev Deepawali Traffic Advisory Parking Route Diversion 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b91c1c; font-weight:800;">🚨 TRAVEL ADVISORY · 24 Nov 2026 · 7 min read</span>
          <h3><a href="blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules">Dev Deepawali 2026: Traffic Advisory, Parking &amp; Boat Rules</a></h3>
          <p>Official police advisory (24 Nov): Godowlia no-entry timings (12–11 PM), 12 designated car parking lots, boat life jacket mandates &amp; ghat routes.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules" style="color:#b91c1c; font-weight:700;">Read Police Advisory <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""

if "blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules" not in blog_c:
    target_grid = '<div class="blog-grid">'
    if target_grid in blog_c:
        blog_c = blog_c.replace(target_grid, target_grid + "\n" + traffic_blog_card)
        print("✅ Added Dev Deepawali Traffic Advisory card to blog.html")

with open(blog_path, "w", encoding="utf-8") as f:
    f.write(blog_c)


# ==========================================
# 3. Update sitemap.xml
# ==========================================
sitemap_path = os.path.join(ROOT, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sm_c = f.read()

# Update lastmod to 2026-11-18 for core pages
sm_c = re.sub(
    r"(<loc>https://www.kashidharshan.com/?</loc>\s*<lastmod>)[^<]+(</lastmod>)",
    r"\g<1>2026-11-18\g<2>",
    sm_c
)
sm_c = re.sub(
    r"(<loc>https://www.kashidharshan.com/kashi-tour-package</loc>\s*<lastmod>)[^<]+(</lastmod>)",
    r"\g<1>2026-11-18\g<2>",
    sm_c
)
sm_c = re.sub(
    r"(<loc>https://www.kashidharshan.com/blog</loc>\s*<lastmod>)[^<]+(</lastmod>)",
    r"\g<1>2026-11-18\g<2>",
    sm_c
)

new_sitemap_entry = """  <url>
    <loc>https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules</loc>
    <lastmod>2026-11-18</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

if "blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules" not in sm_c:
    sm_c = sm_c.replace("</urlset>", new_sitemap_entry + "</urlset>")
    print("✅ Added new URL to sitemap.xml (Total URLs: 103)")

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sm_c)


# ==========================================
# 4. Update rss.xml
# ==========================================
rss_path = os.path.join(ROOT, "rss.xml")
with open(rss_path, "r", encoding="utf-8") as f:
    rss_c = f.read()

rss_c = re.sub(
    r"<lastBuildDate>.*?</lastBuildDate>",
    "<lastBuildDate>Wed, 18 Nov 2026 15:30:00 +0530</lastBuildDate>",
    rss_c
)

new_rss_item = """    <item>
      <title>Dev Deepawali 2026 Varanasi Traffic Advisory: Parking Lots &amp; Boat Safety Guidelines</title>
      <link>https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules</link>
      <guid>https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules</guid>
      <pubDate>Wed, 18 Nov 2026 15:30:00 +0530</pubDate>
      <description>Official police advisory for Dev Deepawali in Varanasi on 24 November 2026. Route diversions, Godowlia no-entry timings (12:00 PM to 11:00 PM), 12 designated vehicle parking grounds, boat life jacket enforcement, and river safety rules.</description>
    </item>
"""

if "blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules" not in rss_c:
    idx_desc = rss_c.find("</description>")
    if idx_desc != -1:
        end_desc = rss_c.find("\n", idx_desc) + 1
        rss_c = rss_c[:end_desc] + new_rss_item + rss_c[end_desc:]
        print("✅ Added Traffic Advisory item to rss.xml (Total items: 51)")

with open(rss_path, "w", encoding="utf-8") as f:
    f.write(rss_c)


# ==========================================
# 5. Update llms.txt
# ==========================================
llms_path = os.path.join(ROOT, "llms.txt")
with open(llms_path, "r", encoding="utf-8") as f:
    llms_c = f.read()

llms_entry = "- [Varanasi Dev Deepawali 2026 Traffic Advisory](https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules): Official Varanasi Police Commissionerate traffic advisory for 24 November 2026, no-vehicle zone timings (12:00 PM - 11:00 PM) for Godowlia and Assi, designated car parking locations, NDRF boat safety regulations, and life jacket mandates.\n"

if "blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules" not in llms_c:
    target_llms = "## Logistical Travel Guides, Aarti Timings & Festival Insights\n\n"
    if target_llms in llms_c:
        llms_c = llms_c.replace(target_llms, target_llms + llms_entry)
        print("✅ Added Traffic Advisory entry to llms.txt")

with open(llms_path, "w", encoding="utf-8") as f:
    f.write(llms_c)

# ==========================================
# 6. Interlink in Dev Deepawali Master Guide
# ==========================================
dd_master_path = os.path.join(ROOT, "blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide.html")
if os.path.exists(dd_master_path):
    with open(dd_master_path, "r", encoding="utf-8") as f:
        dd_c = f.read()
    if "blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules" not in dd_c:
        target_traffic = "3. No-Vehicle Zones &amp; Tourist Traffic Rules (24 Nov)"
        replacement_traffic = """3. No-Vehicle Zones &amp; Tourist Traffic Rules (24 Nov)<br><br>
        👉 <strong>Driving your own vehicle or hiring a cab?</strong> Read our detailed <a href="blog-varanasi-dev-deepawali-2026-traffic-advisory-parking-boat-safety-rules" style="color:#b45309; font-weight:700; text-decoration:underline;">Dev Deepawali 2026 Varanasi Traffic Advisory: Parking Lots, Route Diversions &amp; Boat Safety</a>.<br>"""
        if target_traffic in dd_c:
            dd_c = dd_c.replace(target_traffic, replacement_traffic)
            with open(dd_master_path, "w", encoding="utf-8") as f:
                f.write(dd_c)
            print("✅ Interlinked Traffic Advisory from Dev Deepawali Master Guide")

print("🎉 Completed sitewide update script successfully!")
