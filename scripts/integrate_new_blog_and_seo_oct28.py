"""
Script: integrate_new_blog_and_seo_oct28.py
Purpose:
1. Add new blog to sitemap.xml and update key lastmod dates to 2026-10-28.
2. Add new blog to rss.xml and update lastBuildDate to 2026-10-28.
3. Feature new blog card at the top of blog.html.
4. Feature new blog card in index.html (Section 6: Latest Pilgrimage Insights).
5. Update Dev Deepawali 2026 date alert in blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html.
"""

import re
import os

ROOT = "."

NEW_SLUG = "blog-kashi-vishwanath-all-aarti-timings-ticket-price-booking-guide-2026"
NEW_URL = f"https://www.kashidharshan.com/{NEW_SLUG}"

def update_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update existing key pages lastmod to 2026-10-28
    key_slugs = [
        "https://www.kashidharshan.com/",
        "https://www.kashidharshan.com/varanasi-tour-package",
        "https://www.kashidharshan.com/hotels-in-varanasi-near-kashi-vishwanath-ghats",
        "https://www.kashidharshan.com/blog-varanasi-air-show-2026-wings-over-ganges-guide",
        "https://www.kashidharshan.com/kashi-vishwanath-sugam-darshan-vip-pass",
        "https://www.kashidharshan.com/blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide",
        "https://www.kashidharshan.com/varanasi-guide",
        "https://www.kashidharshan.com/blog",
        "https://www.kashidharshan.com/services"
    ]

    for slug in key_slugs:
        pattern = rf"(<loc>{re.escape(slug)}</loc>\s*<lastmod>)[^<]*(</lastmod>)"
        content = re.sub(pattern, r"\g<1>2026-10-28\g<2>", content)

    # 2. Add new blog entry if not present
    if f"<loc>{NEW_URL}</loc>" not in content:
        new_entry = f"""  <url>
    <loc>{NEW_URL}</loc>
    <lastmod>2026-10-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>"""
        content = content.replace("</urlset>", new_entry)
        print("Added new blog to sitemap.xml.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Sitemap updated successfully.")

def update_rss():
    path = os.path.join(ROOT, "rss.xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update lastBuildDate
    content = re.sub(
        r"<lastBuildDate>[^<]*</lastBuildDate>",
        "<lastBuildDate>Wed, 28 Oct 2026 18:25:00 +0530</lastBuildDate>",
        content
    )

    # Add new item if not present
    if f"<link>{NEW_URL}</link>" not in content:
        new_item = f"""    <item>
      <title>Kashi Vishwanath Aarti Timings 2026: All 5 Aartis Ticket Price, Schedule &amp; Online Booking Guide</title>
      <link>{NEW_URL}</link>
      <guid>{NEW_URL}</guid>
      <description>Complete 2026 schedule for All 5 Kashi Vishwanath Aartis: Mangla (03:00 AM), Bhog (11:15 AM), Sandhya (07:00 PM), Shringar (09:00 PM) &amp; Shayan (10:30 PM). Ticket rates ₹300-₹500, dress code &amp; VIP pass booking.</description>
      <pubDate>Wed, 28 Oct 2026 18:25:00 +0530</pubDate>
    </item>
"""
        channel_needle = "<atom:link href=\"https://www.kashidharshan.com/rss.xml\" rel=\"self\" type=\"application/rss+xml\" />"
        if channel_needle in content:
            content = content.replace(channel_needle, channel_needle + "\n" + new_item)
            print("Added new item to rss.xml.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("RSS feed updated successfully.")

def update_blog_html():
    path = os.path.join(ROOT, "blog.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    blog_card = f"""      <!-- KASHI VISHWANATH ALL 5 AARTIS GUIDE 2026 -->
      <article class="card blog-card reveal" style="border: 2.5px solid var(--maroon); background: #fffcf7;">
        <a href="{NEW_SLUG}" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Kashi Vishwanath Aarti Timings 2026 All 5 Aartis Schedule" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--maroon); font-weight:800;">🔱 NEW · All 5 Aartis Guide · 8 min read</span>
          <h3><a href="{NEW_SLUG}">Kashi Vishwanath Aarti Timings 2026: All 5 Aartis Ticket Price &amp; Booking Guide</a></h3>
          <p>Mangla (03:00 AM), Bhog (11:15 AM), Sandhya (07:00 PM), Shringar &amp; Shayan Aarti complete schedule, ticket fees (₹300-₹500), dress codes &amp; online booking steps.</p>
          <a class="link-arrow bc-foot" href="{NEW_SLUG}" style="color:var(--maroon); font-weight:700;">Read Aarti Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""
    if NEW_SLUG not in content:
        needle = '<div class="blog-grid">'
        if needle in content:
            content = content.replace(needle, needle + "\n" + blog_card)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Added new blog card to blog.html.")

def update_index_html():
    path = os.path.join(ROOT, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    insight_card = f"""      <!-- KASHI VISHWANATH ALL 5 AARTIS GUIDE 2026 -->
      <article class="card blog-card reveal" style="border: 2px solid var(--maroon); background: #fffcf7;">
        <a href="{NEW_SLUG}" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Kashi Vishwanath Aarti Timings 2026 All 5 Aartis Schedule" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--maroon); font-weight:800;">🔱 Essential Yatra Guide · 2026 Updated</span>
          <h3><a href="{NEW_SLUG}">Kashi Vishwanath Aarti Timings 2026: All 5 Aartis Schedule &amp; Price</a></h3>
          <p>Complete guide to Mangla, Bhog, Sandhya, Shringar &amp; Shayan Aarti. Official tickets (₹300-₹500), Garbhagriha entry gates &amp; booking tips.</p>
          <a class="link-arrow bc-foot" href="{NEW_SLUG}" style="color:var(--maroon); font-weight:700;">Read Aarti Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""
    if NEW_SLUG not in content:
        # Find Section 6 grid
        needle = '<section class="section" style="background:var(--bg-panel); border-top:1px solid rgba(212,175,55,0.15); border-bottom:1px solid rgba(212,175,55,0.15);">'
        if needle in content:
            grid_needle = '<div class="grid cols-3">'
            pos_sec = content.find(needle)
            pos_grid = content.find(grid_needle, pos_sec)
            if pos_grid != -1:
                insert_pos = pos_grid + len(grid_needle)
                content = content[:insert_pos] + "\n" + insight_card + content[insert_pos:]
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print("Added Aarti guide to index.html Section 6.")

def update_dev_deepawali_blog():
    path = os.path.join(ROOT, "blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html")
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update dateModified
    content = re.sub(
        r'"dateModified":\s*"[^"]*"',
        '"dateModified": "2026-10-28T18:25:00+05:30"',
        content
    )

    alert_banner = """    <!-- DEV DEEPAWALI 2026 DATE & ADVANCE BOOKING NOTICE -->
    <div style="background: #fffbeb; border: 2px solid #f59e0b; border-radius: 12px; padding: 20px 24px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(245,158,11,0.15);">
      <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
        <span style="font-size: 24px;">🪔</span>
        <h3 style="color: #92400e; margin: 0; font-size: 1.25rem; font-weight: 700; font-family: var(--font-display);">Official Date Notice: Dev Deepawali is on Tuesday, 24 November 2026 (Kartik Purnima)</h3>
      </div>
      <p style="color: #78350f; margin: 0 0 10px 0; font-size: 0.98rem; line-height: 1.6;">
        <strong>Peak Booking Alert:</strong> Dev Deepawali in Varanasi takes place on <strong>Tuesday, November 24, 2026</strong>. All 84 Ghats from Assi to Namo Ghat will be illuminated with 10 Lakh+ diyas alongside the mega Ganga laser and sound show. 
      </p>
      <p style="color: #78350f; margin: 0; font-size: 0.96rem; line-height: 1.6;">
        Private Bajra boats, motorboats, and sharing seats sell out completely 3-4 weeks in advance. To avoid 3x spot surge rates on the ghats, reserve your verified boat seat online early.
      </p>
    </div>
"""
    if "Official Date Notice: Dev Deepawali is on Tuesday, 24 November 2026" not in content:
        needle = '<h1>Varanasi Dev Deepawali 2026: VIP Boat Booking & Ghat Guide</h1>'
        if needle in content:
            content = content.replace(needle, needle + "\n\n" + alert_banner)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Added Dev Deepawali date alert banner.")

if __name__ == "__main__":
    update_sitemap()
    update_rss()
    update_blog_html()
    update_index_html()
    update_dev_deepawali_blog()
    print("All integration tasks complete!")
