"""
Script: execute_oct29_seo_freshness_push.py
Purpose:
1. Add subah-e-banaras to sitemap.xml and refresh key pages to lastmod 2026-10-29.
2. Add subah-e-banaras to rss.xml.
3. Feature subah-e-banaras on blog.html and index.html.
4. Update index.html hero primary CTA to link directly to kashi-tour-package.
5. Enrich kashi-tour-package.html with long-tail keywords and cross-links.
"""

import os
import re

ROOT = "."
NEW_SLUG = "blog-subah-e-banaras-assi-ghat-morning-aarti-timings-guide"
NEW_URL = f"https://www.kashidharshan.com/{NEW_SLUG}"

def update_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update lastmod of key pages to 2026-10-29
    key_slugs = [
        "https://www.kashidharshan.com/",
        "https://www.kashidharshan.com/kashi-tour-package",
        "https://www.kashidharshan.com/varanasi-tour-package",
        "https://www.kashidharshan.com/hotels-in-varanasi-near-kashi-vishwanath-ghats",
        "https://www.kashidharshan.com/kashi-vishwanath-sugam-darshan-vip-pass",
        "https://www.kashidharshan.com/blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost",
        "https://www.kashidharshan.com/blog-kashi-vishwanath-all-aarti-timings-ticket-price-booking-guide-2026",
        "https://www.kashidharshan.com/blog",
        "https://www.kashidharshan.com/services"
    ]

    for slug in key_slugs:
        pattern = rf"(<loc>{re.escape(slug)}</loc>\s*<lastmod>)[^<]*(</lastmod>)"
        content = re.sub(pattern, r"\g<1>2026-10-29\g<2>", content)

    # 2. Add new blog if not present
    if f"<loc>{NEW_URL}</loc>" not in content:
        new_entry = f"""  <url>
    <loc>{NEW_URL}</loc>
    <lastmod>2026-10-29</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>"""
        content = content.replace("</urlset>", new_entry)
        print("Added Subah-e-Banaras guide to sitemap.xml.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Sitemap updated to 2026-10-29 successfully.")

def update_rss():
    path = os.path.join(ROOT, "rss.xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update lastBuildDate
    content = re.sub(
        r"<lastBuildDate>[^<]*</lastBuildDate>",
        "<lastBuildDate>Thu, 29 Oct 2026 14:30:00 +0530</lastBuildDate>",
        content
    )

    if f"<link>{NEW_URL}</link>" not in content:
        new_item = f"""    <item>
      <title>Subah-e-Banaras Assi Ghat Timings 2026: Morning Ganga Aarti &amp; Sunrise Boat Tour</title>
      <link>{NEW_URL}</link>
      <guid>{NEW_URL}</guid>
      <description>Complete 2026 guide to Subah-e-Banaras at Assi Ghat: Morning Ganga Aarti timings (05:00 AM - 07:00 AM), Vedic Hawan, sunrise boat tour price, yoga, classical music &amp; yatra guide.</description>
      <pubDate>Thu, 29 Oct 2026 14:30:00 +0530</pubDate>
    </item>
"""
        channel_needle = '<atom:link href="https://www.kashidharshan.com/rss.xml" rel="self" type="application/rss+xml" />'
        if channel_needle in content:
            content = content.replace(channel_needle, channel_needle + "\n" + new_item)
            print("Added Subah-e-Banaras guide to rss.xml.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("RSS feed updated to 2026-10-29.")

def update_blog_listing():
    path = os.path.join(ROOT, "blog.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    blog_card = f"""      <!-- SUBAH-E-BANARAS ASSI GHAT GUIDE -->
      <article class="card blog-card reveal" style="border: 2.5px solid #d97706; background: #fffcf7;">
        <a href="{NEW_SLUG}" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Subah e Banaras Assi Ghat Morning Ganga Aarti Sunrise" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🌅 MORNING YATRA · Assi Ghat Timings · 7 min read</span>
          <h3><a href="{NEW_SLUG}">Subah-e-Banaras Assi Ghat Timings 2026: Morning Aarti &amp; Sunrise Boat Tour</a></h3>
          <p>Dawn rituals at Assi Ghat (05:00 AM to 07:00 AM), Vedic Hawan, sunrise boat ride rates, Banarasi morning breakfast &amp; yatra itinerary.</p>
          <a class="link-arrow bc-foot" href="{NEW_SLUG}" style="color:#b45309; font-weight:700;">Read Morning Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""
    if NEW_SLUG not in content:
        needle = '<div class="blog-grid">'
        if needle in content:
            content = content.replace(needle, needle + "\n" + blog_card)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Added Subah-e-Banaras card to blog.html.")

def update_index_page():
    path = os.path.join(ROOT, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Hero primary CTA button to link directly to kashi-tour-package
    content = content.replace(
        '<a href="services" class="btn btn-saffron">Explore Kashi Darshan Packages',
        '<a href="kashi-tour-package" class="btn btn-saffron">Explore Kashi Tour Packages'
    )

    # 2. Add Subah-e-Banaras guide card to Section 6
    insight_card = f"""      <!-- SUBAH-E-BANARAS CARD -->
      <article class="card blog-card reveal" style="border: 2px solid #d97706; background: #fffcf7;">
        <a href="{NEW_SLUG}" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Subah e Banaras Assi Ghat Morning Ganga Aarti Sunrise" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">🌅 Assi Ghat Dawn · Morning Yatra</span>
          <h3><a href="{NEW_SLUG}">Subah-e-Banaras Assi Ghat Timings 2026: Morning Aarti &amp; Boat Tour</a></h3>
          <p>Sunrise rituals at Assi Ghat (05:00 AM), Vedic Hawan, morning Ganga Aarti &amp; private sunrise boat tour fares.</p>
          <a class="link-arrow bc-foot" href="{NEW_SLUG}" style="color:#b45309; font-weight:700;">Read Morning Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""
    if NEW_SLUG not in content:
        pos_sec = content.find("Latest Pilgrimage Insights")
        if pos_sec != -1:
            grid_needle = '<div class="grid cols-3">'
            pos_grid = content.find(grid_needle, pos_sec)
            if pos_grid != -1:
                insert_pos = pos_grid + len(grid_needle)
                content = content[:insert_pos] + "\n" + insight_card + content[insert_pos:]
                print("Added Subah-e-Banaras card to index.html Section 6.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def enrich_kashi_tour_package():
    path = os.path.join(ROOT, "kashi-tour-package.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Cross-link Subah-e-Banaras guide in day 3 itinerary
    needle = "Subah-e-Banaras at Assi Ghat with Vedic chanting and classical music."
    replacement = 'Subah-e-Banaras at Assi Ghat with Vedic chanting and classical music (read our complete <a href="blog-subah-e-banaras-assi-ghat-morning-aarti-timings-guide" style="color:var(--saffron-deep); font-weight:600; text-decoration:underline;">Subah-e-Banaras Assi Ghat Morning Aarti &amp; Timings Guide</a>).'
    if needle in content:
        content = content.replace(needle, replacement, 1)

    # Add long-tail keyword paragraph
    needle_kw = "<!-- Package Pricing Cards Grid -->"
    kw_section = """<!-- Long-tail Keyword Rich Quick Comparison -->
      <div style="background:#fff; border:1px solid #e5e7eb; border-radius:12px; padding:20px 24px; margin:24px 0;">
        <h3 style="color:var(--maroon); margin-top:0; font-size:1.25rem;">Compare Kashi Darshan Tour Package Durations &amp; Prices</h3>
        <p style="color:#4b5563; font-size:0.95rem; line-height:1.7; margin-bottom:12px;">
          Whether you are looking for a quick <strong>kashi tour package 2 days 1 night price</strong> or an all-inclusive <strong>kashi darshan tour package with hotel and cab</strong> for senior citizen family members, we offer fully transparent tariffs:
        </p>
        <ul style="color:#4b5563; font-size:0.93rem; line-height:1.8; margin:0; padding-left:20px;">
          <li><strong>Kashi Tour Package 2 Days 1 Night:</strong> ₹4,999/person — Includes 3-star AC hotel, breakfast, private cab, and Kashi Vishwanath VIP Darshan.</li>
          <li><strong>Kashi Tour Package 3 Days 2 Nights (Recommended):</strong> ₹7,900/person — Complete yatra including VIP Sugam Darshan, private Ganga Aarti boat, Subah-e-Banaras sunrise tour, Sarnath, and AC vehicle.</li>
          <li><strong>Kashi Yatra Package with Ayodhya &amp; Prayagraj (5 Days):</strong> ₹14,900/person — Complete sacred triangle covering Ram Janmabhoomi &amp; Triveni Sangam.</li>
        </ul>
      </div>
"""
    if "Compare Kashi Darshan Tour Package Durations" not in content:
        if needle_kw in content:
            content = content.replace(needle_kw, kw_section + "\n      " + needle_kw, 1)
            print("Enriched kashi-tour-package.html with long-tail keyword section.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_listing()
    update_index_page()
    enrich_kashi_tour_package()
    print("All October 29 SEO freshness tasks executed successfully!")
