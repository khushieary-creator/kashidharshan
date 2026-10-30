import re

# 1. Update blog.html
blog_path = "blog.html"
with open(blog_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

new_blog_card = """      <!-- VARANASI GANGA AARTI WINTER TIMINGS 2026-2027 BLOG -->
      <article class="card blog-card reveal" style="border: 2.5px solid #b45309; background: #fffcf7;">
        <a href="blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Ganga Aarti Winter Timings 2026 2027 Dashashwamedh Assi Namo Ghat" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">⚡ WINTER TIMING UPDATE · 06:00 PM Aarti · 7 min read</span>
          <h3><a href="blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide">Varanasi Ganga Aarti Winter Timings 2026-2027: Dashashwamedh, Assi &amp; Namo Ghat</a></h3>
          <p>Critical seasonal update: Dashashwamedh Aarti shifts to 06:00 PM due to early sunset. Ghat schedule, boat boarding cut-off &amp; pilgrim tips.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide" style="color:#b45309; font-weight:700;">Read Winter Schedule <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""

if "blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide" not in blog_content:
    target = '<!-- KASHI DARSHAN 2026 COMPLETE GUIDE BLOG -->'
    if target in blog_content:
        blog_content = blog_content.replace(target, new_blog_card + "      " + target)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(blog_content)
        print("Updated blog.html with Winter Ganga Aarti card.")
    else:
        print("Target not found in blog.html")
else:
    print("Winter Ganga Aarti card already in blog.html")

# 2. Update index.html
index_path = "index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

index_blog_card = """      <!-- VARANASI GANGA AARTI WINTER TIMING CARD -->
      <article class="card blog-card reveal" style="border: 2px solid #b45309; background: #fffcf7;">
        <a href="blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Ganga Aarti Winter Timings Dashashwamedh Ghat" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">⚡ Winter Schedule · 06:00 PM</span>
          <h3><a href="blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide">Ganga Aarti Winter Timings 2026-2027: Ghat Schedule</a></h3>
          <p>Aarti shifts from 7 PM to 6 PM. Complete schedule for Dashashwamedh, Assi &amp; Namo Ghats plus boat rates.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide" style="color:#b45309; font-weight:700;">View Winter Timings <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""

if "blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide" not in index_content:
    target_idx = '<!-- KASHI DARSHAN PILLAR GUIDE CARD -->'
    if target_idx in index_content:
        index_content = index_content.replace(target_idx, index_blog_card + "      " + target_idx)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("Updated index.html with Winter Ganga Aarti insight card.")
    else:
        print("Target not found in index.html")
else:
    print("Winter Ganga Aarti card already in index.html")

# 3. Update sitemap.xml
sitemap_path = "sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

# Update lastmod for primary pages to 2026-10-30
sitemap_content = sitemap_content.replace("<lastmod>2026-10-29</lastmod>", "<lastmod>2026-10-30</lastmod>")

winter_aarti_url_tag = """  <url>
    <loc>https://www.kashidharshan.com/blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

if "blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide" not in sitemap_content:
    sitemap_content = sitemap_content.replace("</urlset>", winter_aarti_url_tag + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Updated sitemap.xml with Winter Ganga Aarti guide URL.")
else:
    print("URL already in sitemap.xml")

# 4. Update rss.xml
rss_path = "rss.xml"
with open(rss_path, "r", encoding="utf-8") as f:
    rss_content = f.read()

# Update lastBuildDate
rss_content = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', '<lastBuildDate>Fri, 30 Oct 2026 23:45:00 +0530</lastBuildDate>', rss_content)

rss_item = """    <item>
      <title>Varanasi Ganga Aarti Winter Timings 2026-2027: Dashashwamedh, Assi &amp; Namo Ghat Schedule</title>
      <link>https://www.kashidharshan.com/blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide</link>
      <guid>https://www.kashidharshan.com/blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide</guid>
      <description>Critical seasonal timing update: Dashashwamedh evening Ganga Aarti shifts to 06:00 PM in winter due to early sunset. Ghat schedule, boat boarding times &amp; rates.</description>
      <pubDate>Fri, 30 Oct 2026 23:45:00 +0530</pubDate>
    </item>
"""

if "blog-varanasi-ganga-aarti-winter-timings-2026-2027-schedule-guide" not in rss_content:
    rss_content = rss_content.replace("<item>", rss_item + "    <item>", 1)
    with open(rss_path, "w", encoding="utf-8") as f:
        f.write(rss_content)
    print("Updated rss.xml with Winter Ganga Aarti RSS item.")
else:
    print("Item already in rss.xml")
