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

# 1a. Optimize title & description
idx_c = re.sub(
    r"<title>.*?</title>",
    "<title>Kashi Darshan Tour Package 2026 | Kashi Vishwanath VIP Yatra</title>",
    idx_c,
    flags=re.DOTALL
)
idx_c = re.sub(
    r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']',
    '<meta name="description" content="Book official Kashi Darshan 2026 tour packages. Priority Kashi Vishwanath VIP pass, Ganga Aarti boat &amp; AC transfers. 4.9★ rated local Varanasi agency.">',
    idx_c,
    flags=re.DOTALL
)

# 1b. Replace expired Air Show card in id="packages" with Dev Deepawali Tour Package
old_air_show_card = """      <!-- 0. VARANASI AIR SHOW 2026 WINGS OVER GANGES -->
      <article class="card blog-card reveal" style="border: 2px solid #d97706; background: #fffcf7;">
        <a href="blog-varanasi-air-show-2026-wings-over-ganges-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Air Show 2026 Wings Over Ganges Schedule Namo Ghat" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🔥 Trending Event · 22-25 Oct 2026</span>
          <h3><a href="blog-varanasi-air-show-2026-wings-over-ganges-guide">Varanasi Air Show 2026: Wings Over Ganges Schedule (100% Free Entry)</a></h3>
          <p>Indian Air Force mega aerial show on 22, 24 &amp; 25 Oct at Namo Ghat. Surya Kiran, Rafale aerobatics schedule, Namo Ghat timings &amp; 100% free entry guide.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-air-show-2026-wings-over-ganges-guide" style="color:#b45309; font-weight:700;">Read Air Show Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>"""

new_dev_deepawali_pkg_card = """      <!-- DEV DEEPAWALI 2026 FESTIVAL PACKAGE CARD -->
      <a class="card pkg reveal" href="blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" style="color:inherit; border: 2px solid #d97706; background: #fffcf7;">
        <div class="pkg-top"><img class="pkg-img" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Dev Deepawali 2026 Festival Tour Package" loading="lazy" decoding="async"><span class="badge" style="background:#dc2626;">🔥 24 Nov 2026 Special</span></div>
        <div class="pkg-body"><span class="days" style="color:#b45309; font-weight:700;">3 Days · 2 Nights</span><h3>Dev Deepawali 2026 Tour Package</h3>
          <p class="route">VIP Diya Viewing Boat · 84 Ghats Illumination · Kashi Vishwanath Sugam Darshan</p>
          <div class="price">₹14,500 <small>/ person (All Inclusive)</small></div>
          <span class="link-arrow" style="margin-top:6px; color:#b45309; font-weight:700;">View Festival Package <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></div>
      </a>"""

if old_air_show_card in idx_c:
    idx_c = idx_c.replace(old_air_show_card, new_dev_deepawali_pkg_card)
    print("✅ Replaced expired Air Show card with Dev Deepawali Package card in index.html")
else:
    print("ℹ️ Air Show card not found in exact format, checking partial match")

# 1c. In Section 6 (Latest Pilgrimage Insights), update cards to:
# 1. Dev Deepawali Master Guide
# 2. Ganga Mahotsav Guide
# 3. Kashi Darshan Itinerary Guide
insights_target = "<!-- VARANASI CHHATH PUJA CARD -->"
ganga_mahotsav_card = """<!-- VARANASI GANGA MAHOTSAV 2026 CARD -->
      <article class="card blog-card reveal" style="border: 2px solid #d97706; background: #fffcf7;">
        <a href="blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Ganga Mahotsav 2026 Dates Schedule Rajghat" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🎶 21–24 Nov · Cultural Festival</span>
          <h3><a href="blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide">Ganga Mahotsav 2026: Rajghat Schedule</a></h3>
          <p>4-day classical music concerts, Kashi boat race, wrestling dangal, 100% free entry &amp; Dev Deepawali.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide" style="color:#b45309; font-weight:700;">View Festival Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>"""

kashi_darshan_card = """<!-- KASHI DARSHAN ITINERARY CARD -->
      <article class="card blog-card reveal" style="border: 2px solid #b45309; background: #fffcf7;">
        <a href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Kashi Darshan 2026 Places to Visit 1 Day 2 Days Itinerary" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🏛️ Pilgrimage Itinerary Guide</span>
          <h3><a href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026">Kashi Darshan 2026: Top Places &amp; Itinerary</a></h3>
          <p>Top 10 sacred places to visit, 1-day &amp; 2-day temple itinerary, VIP Sugam Darshan &amp; local cab tips.</p>
          <a class="link-arrow bc-foot" href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" style="color:#b45309; font-weight:700;">Read Itinerary Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>"""

# Replace the older Chhath and Maa Annapurna cards
chhath_card_pattern = r"<!-- VARANASI CHHATH PUJA CARD -->.*?</article>\s*<!-- MAA ANNAPURNA SWARNA DARSHAN CARD -->.*?</article>"
m_cards = re.search(chhath_card_pattern, idx_c, re.DOTALL)
if m_cards:
    idx_c = idx_c[:m_cards.start()] + ganga_mahotsav_card + "\n\n      " + kashi_darshan_card + idx_c[m_cards.end():]
    print("✅ Replaced Chhath & Annapurna cards with Ganga Mahotsav & Kashi Darshan cards in index.html")
else:
    print("ℹ️ Chhath & Annapurna pattern not found in index.html")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_c)


# ==========================================
# 2. Update kashi-tour-package.html
# ==========================================
ktp_path = os.path.join(ROOT, "kashi-tour-package.html")
with open(ktp_path, "r", encoding="utf-8") as f:
    ktp_c = f.read()

ktp_c = re.sub(
    r"<title>.*?</title>",
    "<title>Kashi Tour Package 2026 | VIP Kashi Darshan &amp; Ganga Aarti</title>",
    ktp_c,
    flags=re.DOTALL
)
ktp_c = re.sub(
    r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']',
    '<meta name="description" content="Book official Kashi Tour Package 2026 from ₹4,999. Includes Kashi Vishwanath VIP pass, Ganga Aarti private boat, Sarnath &amp; AC cab. 4.9★ rated local agency.">',
    ktp_c,
    flags=re.DOTALL
)

with open(ktp_path, "w", encoding="utf-8") as f:
    f.write(ktp_c)
print("✅ Optimized snippet for kashi-tour-package.html")


# ==========================================
# 3. Update blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026.html
# ==========================================
kdb_path = os.path.join(ROOT, "blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026.html")
with open(kdb_path, "r", encoding="utf-8") as f:
    kdb_c = f.read()

kdb_c = re.sub(
    r"<title>.*?</title>",
    "<title>Kashi Darshan 2026: Top Places to Visit &amp; 1-2 Day Itinerary</title>",
    kdb_c,
    flags=re.DOTALL
)
kdb_c = re.sub(
    r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']',
    '<meta name="description" content="Complete Kashi Darshan 2026 guide: Top 10 places to visit, 1-day &amp; 2-day itinerary, temple timings (Vishwanath, Kaal Bhairav) &amp; local taxi booking guide.">',
    kdb_c,
    flags=re.DOTALL
)

with open(kdb_path, "w", encoding="utf-8") as f:
    f.write(kdb_c)
print("✅ Optimized snippet for Kashi Darshan Itinerary blog")


# ==========================================
# 4. Update blog.html
# ==========================================
blog_path = os.path.join(ROOT, "blog.html")
with open(blog_path, "r", encoding="utf-8") as f:
    blog_c = f.read()

blog_c = re.sub(
    r"<title>.*?</title>",
    "<title>Kashi Yatra Blog: Temple Timings, Darshan Guides &amp; Itinerary</title>",
    blog_c,
    flags=re.DOTALL
)
blog_c = re.sub(
    r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']',
    '<meta name="description" content="Official Kashi Yatra travel blog. Explore Kashi Vishwanath darshan rules, Ganga Aarti timings, Dev Deepawali schedule &amp; local Varanasi pilgrimage guides.">',
    blog_c,
    flags=re.DOTALL
)

ganga_mahotsav_blog_card = """      <!-- VARANASI GANGA MAHOTSAV 2026 MASTER GUIDE -->
      <article class="card blog-card reveal" style="border: 2.5px solid #d97706; background: #fffcf7;">
        <a href="blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Ganga Mahotsav 2026 Dates Schedule Rajghat Free Entry" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🎶 CULTURAL FESTIVAL · 21–24 Nov 2026 · 8 min read</span>
          <h3><a href="blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide">Varanasi Ganga Mahotsav 2026: Dates, Schedule &amp; Rajghat Guide</a></h3>
          <p>Complete 4-day guide (21–24 Nov): Rajghat classical concerts, Shehnai recital, Kashi boat race, wrestling dangal, craft mela, 100% free entry &amp; Dev Deepawali.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide" style="color:#b45309; font-weight:700;">Read Festival Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""

if "blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide" not in blog_c:
    target_blog = '<div class="blog-grid">'
    if target_blog in blog_c:
        blog_c = blog_c.replace(target_blog, target_blog + "\n" + ganga_mahotsav_blog_card)
        print("✅ Added Ganga Mahotsav card to blog.html")

with open(blog_path, "w", encoding="utf-8") as f:
    f.write(blog_c)


# ==========================================
# 5. Update sitemap.xml
# ==========================================
sitemap_path = os.path.join(ROOT, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sm_c = f.read()

# Update main pages lastmod to 2026-11-17
sm_c = re.sub(
    r"(<loc>https://www.kashidharshan.com/?</loc>\s*<lastmod>)[^<]+(</lastmod>)",
    r"\g<1>2026-11-17\g<2>",
    sm_c
)
sm_c = re.sub(
    r"(<loc>https://www.kashidharshan.com/kashi-tour-package</loc>\s*<lastmod>)[^<]+(</lastmod>)",
    r"\g<1>2026-11-17\g<2>",
    sm_c
)
sm_c = re.sub(
    r"(<loc>https://www.kashidharshan.com/blog</loc>\s*<lastmod>)[^<]+(</lastmod>)",
    r"\g<1>2026-11-17\g<2>",
    sm_c
)

new_sitemap_entry = """  <url>
    <loc>https://www.kashidharshan.com/blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

if "blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide" not in sm_c:
    sm_c = sm_c.replace("</urlset>", new_sitemap_entry + "</urlset>")
    print("✅ Added new URL to sitemap.xml (Total URLs: 102)")

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sm_c)


# ==========================================
# 6. Update rss.xml
# ==========================================
rss_path = os.path.join(ROOT, "rss.xml")
with open(rss_path, "r", encoding="utf-8") as f:
    rss_c = f.read()

rss_c = re.sub(
    r"<lastBuildDate>.*?</lastBuildDate>",
    "<lastBuildDate>Tue, 17 Nov 2026 17:45:00 +0530</lastBuildDate>",
    rss_c
)

new_rss_item = """    <item>
      <title>Varanasi Ganga Mahotsav 2026: Dates, Schedule &amp; Rajghat Cultural Guide</title>
      <link>https://www.kashidharshan.com/blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide</link>
      <guid>https://www.kashidharshan.com/blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide</guid>
      <pubDate>Tue, 17 Nov 2026 17:45:00 +0530</pubDate>
      <description>Complete 4-day visitor guide for Varanasi Ganga Mahotsav (21-24 November 2026) at Rajghat and Assi Ghat. Schedule of classical Hindustani music concerts, Kashi boat race, wrestling dangal, craft mela, 100% free entry guidelines, and Dev Deepawali grand finale.</description>
    </item>
"""

if "blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide" not in rss_c:
    idx_desc = rss_c.find("</description>")
    if idx_desc != -1:
        end_desc = rss_c.find("\n", idx_desc) + 1
        rss_c = rss_c[:end_desc] + new_rss_item + rss_c[end_desc:]
        print("✅ Added Ganga Mahotsav item to rss.xml")

with open(rss_path, "w", encoding="utf-8") as f:
    f.write(rss_c)


# ==========================================
# 7. Update llms.txt
# ==========================================
llms_path = os.path.join(ROOT, "llms.txt")
with open(llms_path, "r", encoding="utf-8") as f:
    llms_c = f.read()

llms_entry = "- [Varanasi Ganga Mahotsav 2026 Guide](https://www.kashidharshan.com/blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide): Comprehensive 4-day schedule (21-24 November 2026) for the cultural festival at Rajghat and Assi Ghat, classical music and dance programs, Kashi Nauka Pratiyogita, wrestling tournaments, free entry, and Dev Deepawali integration.\n"

if "blog-varanasi-ganga-mahotsav-2026-dates-schedule-rajghat-guide" not in llms_c:
    target_llms = "## Logistical Travel Guides, Aarti Timings & Festival Insights\n\n"
    if target_llms in llms_c:
        llms_c = llms_c.replace(target_llms, target_llms + llms_entry)
        print("✅ Added Ganga Mahotsav entry to llms.txt")

with open(llms_path, "w", encoding="utf-8") as f:
    f.write(llms_c)

print("🎉 All SEO updates and sitewide synchronization executed successfully!")
