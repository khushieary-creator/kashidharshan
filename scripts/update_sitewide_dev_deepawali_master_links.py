#!/usr/bin/env python3
import os
import re

ROOT = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan"

# 1. Update blog.html
blog_path = os.path.join(ROOT, "blog.html")
with open(blog_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

dev_deepawali_blog_card = """      <!-- VARANASI DEV DEEPAWALI 2026 MASTER SCHEDULE BLOG -->
      <article class="card blog-card reveal" style="border: 2.5px solid #d97706; background: #fffcf7;">
        <a href="blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Dev Deepawali 2026 Schedule Timings Laser Show Boat Fare Guide" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🪔 KARTIK PURNIMA · 24 Nov 2026 · 10 min read</span>
          <h3><a href="blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide">Varanasi Dev Deepawali 2026: Official Timings, Laser Show &amp; Boat Guide</a></h3>
          <p>Complete 24 Nov 2026 schedule: 05:15 PM 84 ghats 12L+ diya lighting, Chet Singh Ghat 3D laser show (7 &amp; 8:30 PM), Ganga Mahotsav, administration boat fare caps &amp; no-vehicle zone guide.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" style="color:#b45309; font-weight:700;">Read Master Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""

if "blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" not in blog_content:
    target = '<div class="blog-grid">'
    if target in blog_content:
        blog_content = blog_content.replace(target, target + "\n" + dev_deepawali_blog_card)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(blog_content)
        print("✅ Added Dev Deepawali master card to blog.html")
    else:
        print("❌ Could not find .blog-grid in blog.html")
else:
    print("ℹ️ Card already present in blog.html")

# 2. Update index.html
index_path = os.path.join(ROOT, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

index_blog_card = """      <!-- VARANASI DEV DEEPAWALI 2026 MASTER SCHEDULE CARD -->
      <article class="card blog-card reveal" style="border: 2px solid #d97706; background: #fffcf7;">
        <a href="blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Dev Deepawali 2026 Schedule Timings Laser Show Boat Guide" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🪔 24 Nov · Kartik Purnima Master Guide</span>
          <h3><a href="blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide">Dev Deepawali 2026: Timings, Laser Show &amp; Boat Guide</a></h3>
          <p>05:15 PM 84 ghats 12L+ diya lighting, Chet Singh Ghat 3D laser show (7 &amp; 8:30 PM), official boat rate caps &amp; boarding rules.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" style="color:#b45309; font-weight:700;">View Master Schedule <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""

if "blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" not in index_content:
    target_idx = "<!-- VARANASI CHHATH PUJA CARD -->"
    if target_idx in index_content:
        index_content = index_content.replace(target_idx, index_blog_card + "\n                              " + target_idx)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("✅ Added Dev Deepawali master card to index.html")
    else:
        print("❌ Could not find target in index.html")
else:
    print("ℹ️ Card already present in index.html")

# 3. Update sitemap.xml
sitemap_path = os.path.join(ROOT, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

new_sitemap_url = """  <url>
    <loc>https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide</loc>
    <lastmod>2026-11-16</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

# Update main pages lastmod to 2026-11-16
sitemap_content = re.sub(
    r"(<loc>https://www.kashidharshan.com/?</loc>\s*<lastmod>)[^<]+(</lastmod>)",
    r"\g<1>2026-11-16\g<2>",
    sitemap_content
)
sitemap_content = re.sub(
    r"(<loc>https://www.kashidharshan.com/blog</loc>\s*<lastmod>)[^<]+(</lastmod>)",
    r"\g<1>2026-11-16\g<2>",
    sitemap_content
)

if "blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" not in sitemap_content:
    sitemap_content = sitemap_content.replace("</urlset>", new_sitemap_url + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("✅ Added new URL to sitemap.xml")
else:
    print("ℹ️ URL already in sitemap.xml")

# 4. Update rss.xml
rss_path = os.path.join(ROOT, "rss.xml")
with open(rss_path, "r", encoding="utf-8") as f:
    rss_content = f.read()

rss_item = """    <item>
      <title>Varanasi Dev Deepawali 2026: Official Timings, Laser Show Schedule &amp; Boat Booking Guide</title>
      <link>https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide</link>
      <guid>https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide</guid>
      <pubDate>Mon, 16 Nov 2026 21:45:00 +0530</pubDate>
      <description>Complete 24 November 2026 schedule for Dev Deepawali in Varanasi. Hour-by-hour timeline: 05:15 PM 12 Lakh+ diya lighting across 84 ghats, Chet Singh Ghat 3D laser show (07:00 PM &amp; 08:30 PM), Ganga Mahotsav 2026 dates (21–24 Nov), district administration official boat fare caps, traffic rules, and VIP boat boarding tips.</description>
    </item>
"""

# update lastBuildDate
rss_content = re.sub(
    r"<lastBuildDate>.*?</lastBuildDate>",
    "<lastBuildDate>Mon, 16 Nov 2026 21:45:00 +0530</lastBuildDate>",
    rss_content
)

if "blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" not in rss_content:
    target_rss = "<channel>"
    idx_rss = rss_content.find("</description>") # channel description
    if idx_rss != -1:
        end_desc = rss_content.find("\n", idx_rss) + 1
        rss_content = rss_content[:end_desc] + rss_item + rss_content[end_desc:]
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(rss_content)
        print("✅ Added item to rss.xml")
    else:
        print("❌ Could not find insert spot in rss.xml")
else:
    print("ℹ️ Item already in rss.xml")

# 5. Update llms.txt
llms_path = os.path.join(ROOT, "llms.txt")
with open(llms_path, "r", encoding="utf-8") as f:
    llms_content = f.read()

llms_entry = "- [Varanasi Dev Deepawali 2026 Master Guide](https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide): Complete hour-by-hour schedule for Kartik Purnima Dev Deepawali (24 November 2026) across 84 ghats, Chet Singh Ghat 3D laser projection timings (7:00 PM & 8:30 PM), Ganga Mahotsav (21-24 Nov), official boat fare caps, boarding cutoff times, and vehicular traffic survival guide.\n"

if "blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" not in llms_content:
    target_llms = "## Logistical Travel Guides, Aarti Timings & Festival Insights\n\n"
    if target_llms in llms_content:
        llms_content = llms_content.replace(target_llms, target_llms + llms_entry)
        with open(llms_path, "w", encoding="utf-8") as f:
            f.write(llms_content)
        print("✅ Added entry to llms.txt")
    else:
        print("❌ Could not find target in llms.txt")
else:
    print("ℹ️ Entry already in llms.txt")

# 6. Interlinking from tour package blog
itinerary_path = os.path.join(ROOT, "blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost.html")
if os.path.exists(itinerary_path):
    with open(itinerary_path, "r", encoding="utf-8") as f:
        itinerary_c = f.read()
    if "blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" not in itinerary_c:
        target_itinerary = '⚠️ <strong>Booking Warning:</strong>'
        replacement_itinerary = """👉 <strong>Looking for the minute-by-minute festival timeline?</strong> Read our comprehensive <a href="blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" style="color:#b45309; font-weight:700; text-decoration:underline;">Varanasi Dev Deepawali 2026 Master Schedule (Ghat Lighting, Laser Show &amp; Boat Fare Caps)</a>.<br><br>
        ⚠️ <strong>Booking Warning:</strong>"""
        if target_itinerary in itinerary_c:
            itinerary_c = itinerary_c.replace(target_itinerary, replacement_itinerary)
            with open(itinerary_path, "w", encoding="utf-8") as f:
                f.write(itinerary_c)
            print("✅ Interlinked from Dev Deepawali tour package blog")

# 7. Interlinking from Ganga Aarti winter timings blog
aarti_path = os.path.join(ROOT, "blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide.html")
if os.path.exists(aarti_path):
    with open(aarti_path, "r", encoding="utf-8") as f:
        aarti_c = f.read()
    if "blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" not in aarti_c:
        target_aarti = '<td style="padding: 13px 14px; font-weight: 700; color: var(--maroon);">Dev Deepawali (24 Nov 2026 Special)</td>'
        replacement_aarti = '<td style="padding: 13px 14px; font-weight: 700; color: var(--maroon);"><a href="blog-varanasi-dev-deepawali-2026-schedule-timings-laser-show-boat-guide" style="color:var(--maroon); text-decoration:underline;">Dev Deepawali (24 Nov 2026 Special)</a></td>'
        if target_aarti in aarti_c:
            aarti_c = aarti_c.replace(target_aarti, replacement_aarti)
            with open(aarti_path, "w", encoding="utf-8") as f:
                f.write(aarti_c)
            print("✅ Interlinked from Ganga Aarti winter timings blog")

print("🎉 Sitewide updates complete!")
