"""
Script: master_kashi_tour_package_booster.py
Purpose:
1. In all HTML files, add kashi-tour-package link into foot-quick-services.
2. In index.html, update nav-links, update primary package card to point to kashi-tour-package, and add dev deepawali package insight card.
3. In blog.html, add dev deepawali package card.
4. In sitemap.xml, add kashi-tour-package and blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost.
5. In rss.xml, add the new package items.
"""

import os
import re

ROOT = "."

def update_footers():
    needle = '<span style="color:var(--gold-soft, #f59e0b); font-weight:700; text-transform:uppercase; letter-spacing:0.8px; font-size:0.78rem;">⚡ Quick VIP Services:</span>'
    replacement = (
        '<span style="color:var(--gold-soft, #f59e0b); font-weight:700; text-transform:uppercase; letter-spacing:0.8px; font-size:0.78rem;">⚡ Quick VIP Services:</span>\n'
        '      <a href="kashi-tour-package" style="color:#FCEFD9; text-decoration:none; font-weight:700;">Kashi Tour Package (Best Rates)</a>\n'
        '      <span style="color:rgba(255,255,255,0.25);">•</span>'
    )

    count = 0
    for f in os.listdir(ROOT):
        if f.endswith(".html"):
            path = os.path.join(ROOT, f)
            with open(path, "r", encoding="utf-8") as fp:
                content = fp.read()

            if needle in content and 'href="kashi-tour-package"' not in content.split("foot-quick-services")[-1]:
                content = content.replace(needle, replacement, 1)
                with open(path, "w", encoding="utf-8") as fp:
                    fp.write(content)
                count += 1

    print(f"Updated foot-quick-services in {count} HTML files to include kashi-tour-package.")

def update_index_and_nav():
    # Update index.html
    path = os.path.join(ROOT, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update nav-links in index.html to have Kashi Tour Packages
    content = content.replace(
        '<a href="varanasi-tour-package">Packages</a>',
        '<a href="kashi-tour-package">Kashi Tour Packages</a>'
    )
    content = content.replace(
        '<a href="varanasi-tour-package">Varanasi Tour Packages</a>',
        '<a href="kashi-tour-package">Kashi Tour Packages</a>'
    )

    # In section 5, update the main 3D/2N package link to point to kashi-tour-package
    content = content.replace(
        '<a class="card pkg reveal" href="varanasi-tour-package" style="color:inherit;">\n        <div class="pkg-top"><img class="pkg-img" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Tour Package Kashi Vishwanath Ganga Aarti" loading="lazy" decoding="async"><span class="badge">Most Popular</span></div>\n        <div class="pkg-body"><span class="days">3 Days · 2 Nights</span><h3>Kashi Darshan Tour Package (3D/2N Complete Yatra)</h3>',
        '<a class="card pkg reveal" href="kashi-tour-package" style="color:inherit;">\n        <div class="pkg-top"><img class="pkg-img" src="assets/destinations/ganga-aarti.webp" alt="Kashi Tour Package Kashi Vishwanath Ganga Aarti" loading="lazy" decoding="async"><span class="badge">⭐ Most Popular</span></div>\n        <div class="pkg-body"><span class="days">3 Days · 2 Nights</span><h3>Kashi Tour Package (3D/2N Complete Yatra)</h3>'
    )

    # In Section 6, add Dev Deepawali Package card
    dd_card = """      <!-- DEV DEEPAWALI TOUR PACKAGE 2026 CARD -->
      <article class="card blog-card reveal" style="border: 2px solid #b45309; background: #fffcf7;">
        <a href="blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Dev Deepawali Varanasi Tour Package 2026 84 Ghats Boat Booking" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🪔 24 Nov 2026 · Kartik Purnima · 7 min read</span>
          <h3><a href="blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost">Dev Deepawali Varanasi Tour Package 2026: Yatra Cost, Boat &amp; Hotel</a></h3>
          <p>Experience 10 Lakh+ diyas across 84 ghats. Complete 3-day package including 3-star hotel stay, reserved boat viewing &amp; Kashi Vishwanath VIP pass.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" style="color:#b45309; font-weight:700;">Explore Festival Package <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""
    if "blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" not in content:
        needle_insight = '<div class="grid cols-3">'
        pos_sec = content.find("Latest Pilgrimage Insights")
        if pos_sec != -1:
            pos_grid = content.find(needle_insight, pos_sec)
            if pos_grid != -1:
                insert_pos = pos_grid + len(needle_insight)
                content = content[:insert_pos] + "\n" + dd_card + content[insert_pos:]
                print("Added Dev Deepawali package card to index.html Section 6.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_blog_listing():
    path = os.path.join(ROOT, "blog.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    dd_blog_card = """      <!-- DEV DEEPAWALI TOUR PACKAGE 2026 BLOG -->
      <article class="card blog-card reveal" style="border: 2.5px solid #b45309; background: #fffcf7;">
        <a href="blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Dev Deepawali Varanasi Tour Package 2026 84 Ghats Boat Booking" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🪔 UPCOMING FESTIVAL · 24 Nov 2026 · 7 min read</span>
          <h3><a href="blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost">Dev Deepawali Varanasi Tour Package 2026: 3-Day Yatra Cost, Boat &amp; Hotel</a></h3>
          <p>Complete 3D/2N Dev Deepawali yatra package. Guaranteed riverfront boat seat for 84 ghats illumination, 3-star hotel &amp; Kashi Vishwanath VIP pass.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" style="color:#b45309; font-weight:700;">View Festival Package <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""
    if "blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" not in content:
        needle = '<div class="blog-grid">'
        if needle in content:
            content = content.replace(needle, needle + "\n" + dd_blog_card)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Added Dev Deepawali blog card to blog.html.")

def update_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_urls = [
        ("https://www.kashidharshan.com/kashi-tour-package", "1.0", "daily"),
        ("https://www.kashidharshan.com/blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost", "0.9", "weekly")
    ]

    for url, prio, freq in new_urls:
        if f"<loc>{url}</loc>" not in content:
            entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-10-28</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>
</urlset>"""
            content = content.replace("</urlset>", entry)
            print(f"Added {url} to sitemap.xml.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_rss():
    path = os.path.join(ROOT, "rss.xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_rss_item = """    <item>
      <title>Dev Deepawali Varanasi Tour Package 2026: 3-Day Yatra Cost, VIP Boat Booking &amp; Itinerary</title>
      <link>https://www.kashidharshan.com/blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost</link>
      <guid>https://www.kashidharshan.com/blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost</guid>
      <description>Official Dev Deepawali Varanasi Tour Package 2026 (24 Nov Kartik Purnima). Includes 3-star hotel stay, VIP Ganga Aarti boat booking, Kashi Vishwanath Sugam Darshan pass &amp; AC cab transfers.</description>
      <pubDate>Wed, 28 Oct 2026 18:35:00 +0530</pubDate>
    </item>
"""
    if "blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" not in content:
        channel_needle = '<atom:link href="https://www.kashidharshan.com/rss.xml" rel="self" type="application/rss+xml" />'
        if channel_needle in content:
            content = content.replace(channel_needle, channel_needle + "\n" + new_rss_item)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Added Dev Deepawali package to rss.xml.")

if __name__ == "__main__":
    update_footers()
    update_index_and_nav()
    update_blog_listing()
    update_sitemap()
    update_rss()
    print("Master Kashi Tour Package Booster finished!")
