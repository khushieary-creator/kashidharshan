import re

# 1. Update blog.html
blog_path = "blog.html"
with open(blog_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

new_blog_card = """      <!-- KASHI DARSHAN 2026 COMPLETE GUIDE BLOG -->
      <article class="card blog-card reveal" style="border: 2.5px solid var(--maroon); background: #fffcf7;">
        <a href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Kashi Darshan 2026 Places to Visit 1 Day 2 Day Sightseeing Itinerary" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--maroon); font-weight:800;">🔱 PILLAR GUIDE · 1-Day &amp; 2-Day Yatra · 8 min read</span>
          <h3><a href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026">Kashi Darshan 2026: Top 10 Places, 1-Day &amp; 2-Day Itinerary, Timings &amp; Cost</a></h3>
          <p>Complete yatra guide to Kashi Darshan: Top 10 temples, hour-by-hour 1-day &amp; 2-day schedules, taxi rates, VIP Sugam pass tips &amp; food trails.</p>
          <a class="link-arrow bc-foot" href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" style="color:var(--maroon); font-weight:700;">Read Kashi Darshan Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""

if "blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" not in blog_content:
    # insert before SUBAH-E-BANARAS
    target = '<!-- SUBAH-E-BANARAS ASSI GHAT GUIDE -->'
    if target in blog_content:
        blog_content = blog_content.replace(target, new_blog_card + "      " + target)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(blog_content)
        print("Updated blog.html with Kashi Darshan card.")
    else:
        print("Target not found in blog.html")
else:
    print("Kashi Darshan card already in blog.html")

# 2. Update index.html
index_path = "index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

index_blog_card = """      <!-- KASHI DARSHAN PILLAR GUIDE CARD -->
      <article class="card blog-card reveal" style="border: 2px solid var(--maroon); background: #fffcf7;">
        <a href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Kashi Darshan Places to Visit Itinerary Guide" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--maroon); font-weight:800;">🔱 Complete Yatra Guide · 2026</span>
          <h3><a href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026">Kashi Darshan 2026: 1-Day &amp; 2-Day Sightseeing Guide</a></h3>
          <p>Top 10 sacred places to visit in Kashi, temple timings, private cab fares &amp; VIP Sugam pass assistance.</p>
          <a class="link-arrow bc-foot" href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" style="color:var(--maroon); font-weight:700;">Read Kashi Darshan Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""

if "blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" not in index_content:
    target_idx = '<!-- SUBAH-E-BANARAS CARD -->'
    if target_idx in index_content:
        index_content = index_content.replace(target_idx, index_blog_card + "      " + target_idx)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("Updated index.html with Kashi Darshan insight card.")
    else:
        print("Target not found in index.html")
else:
    print("Kashi Darshan card already in index.html")

# 3. Update sitemap.xml
sitemap_path = "sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

kashi_darshan_url_tag = """  <url>
    <loc>https://www.kashidharshan.com/blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026</loc>
    <lastmod>2026-10-29</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

if "blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" not in sitemap_content:
    sitemap_content = sitemap_content.replace("</urlset>", kashi_darshan_url_tag + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Updated sitemap.xml with Kashi Darshan guide URL.")
else:
    print("URL already in sitemap.xml")

# 4. Update rss.xml
rss_path = "rss.xml"
with open(rss_path, "r", encoding="utf-8") as f:
    rss_content = f.read()

rss_item = """    <item>
      <title>Kashi Darshan 2026: Top 10 Places to Visit, 1-Day &amp; 2-Day Sightseeing Itinerary, Temple Timings</title>
      <link>https://www.kashidharshan.com/blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026</link>
      <guid>https://www.kashidharshan.com/blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026</guid>
      <description>Exhaustive guide to Kashi Darshan in Varanasi covering top 10 sacred temples, hour-by-hour 1-day &amp; 2-day itineraries, temple opening timings, taxi rates, and VIP Sugam Darshan tips.</description>
      <pubDate>Thu, 29 Oct 2026 14:45:00 +0530</pubDate>
    </item>
"""

if "blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" not in rss_content:
    rss_content = rss_content.replace("<item>", rss_item + "    <item>", 1)
    with open(rss_path, "w", encoding="utf-8") as f:
        f.write(rss_content)
    print("Updated rss.xml with Kashi Darshan RSS item.")
else:
    print("Item already in rss.xml")
