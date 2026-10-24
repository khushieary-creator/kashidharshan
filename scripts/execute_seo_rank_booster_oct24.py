"""
Script: execute_seo_rank_booster_oct24.py
Purpose:
1. Inject global internal links in foot-quick-services across all 92 HTML pages for:
   - hotels-in-varanasi-near-kashi-vishwanath-ghats
   - blog-varanasi-air-show-2026-wings-over-ganges-guide
2. Add Hotels & Packages to main header navigation in key landing pages.
3. Add Hotel guide card to index.html packages section and insights section.
4. Add live rehearsal & finale status banner to Air Show blog with updated dateModified.
5. Add contextual in-content links in varanasi-tour-package.html and varanasi-guide.html.
6. Update sitemap.xml lastmod dates to 2026-10-24.
7. Update rss.xml lastBuildDate to 2026-10-24.
"""

import os
import re

ROOT = "."

def update_foot_quick_services():
    target_needle = '<a href="varanasi-guide" style="color:#FCEFD9; text-decoration:none;">Varanasi Complete Travel Guide</a>'
    replacement = (
        '<a href="varanasi-guide" style="color:#FCEFD9; text-decoration:none;">Varanasi Complete Travel Guide</a>\n'
        '      <span style="color:rgba(255,255,255,0.25);">•</span>\n'
        '      <a href="hotels-in-varanasi-near-kashi-vishwanath-ghats" style="color:#FCEFD9; text-decoration:none;">Hotels in Varanasi (3★, 4★, 5★)</a>\n'
        '      <span style="color:rgba(255,255,255,0.25);">•</span>\n'
        '      <a href="blog-varanasi-air-show-2026-wings-over-ganges-guide" style="color:#FCEFD9; text-decoration:none;">Varanasi Air Show 2026 Schedule</a>'
    )

    count = 0
    for f in os.listdir(ROOT):
        if f.endswith(".html"):
            path = os.path.join(ROOT, f)
            with open(path, "r", encoding="utf-8") as fp:
                content = fp.read()
            
            if target_needle in content and "hotels-in-varanasi-near-kashi-vishwanath-ghats" not in content.split("foot-quick-services")[-1]:
                new_content = content.replace(target_needle, replacement, 1)
                with open(path, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                count += 1

    print(f"Updated foot-quick-services in {count} HTML files.")

def update_air_show_live_banner():
    path = os.path.join(ROOT, "blog-varanasi-air-show-2026-wings-over-ganges-guide.html")
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    # Update dateModified in schema
    content = re.sub(
        r'"dateModified":\s*"[^"]*"',
        '"dateModified": "2026-10-24T14:30:00+05:30"',
        content
    )

    # Check if live banner already exists
    live_banner = """    <!-- LIVE 24 & 25 OCT SCHEDULE ALERT BANNER -->
    <div style="background: #fffbeb; border: 2px solid #f59e0b; border-radius: 12px; padding: 20px 24px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(245,158,11,0.15);">
      <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
        <span style="display: inline-block; width: 12px; height: 12px; border-radius: 50%; background: #ef4444;"></span>
        <h3 style="color: #92400e; margin: 0; font-size: 1.25rem; font-weight: 700; font-family: var(--font-display);">🔴 LIVE TIMINGS UPDATE: 24 Oct Rehearsal &amp; 25 Oct Grand Finale</h3>
      </div>
      <p style="color: #78350f; margin: 0 0 8px 0; font-size: 0.98rem; line-height: 1.6;">
        <strong>Today (24 Oct 2026):</strong> Full Dress Rehearsal successfully completed with Surya Kiran 9-Hawk formations, Rafale vertical Charlie climbs, and Akash Ganga paratroopers over Namo Ghat and River Ganga.
      </p>
      <p style="color: #78350f; margin: 0 0 10px 0; font-size: 0.98rem; line-height: 1.6;">
        <strong>Tomorrow (25 Oct 2026 - Sharad Purnima):</strong> Grand Public Finale scheduled between <strong>10:00 AM – 01:30 PM</strong>. Entry is 100% FREE at Namo Ghat (Khidkiya Ghat), Rajghat, and Malviya Bridge. Reach by 09:00 AM for prime riverfront viewing!
      </p>
      <div style="margin-top: 10px; padding-top: 10px; border-top: 1px dashed #fcd34d; font-size: 0.92rem; color: #92400e;">
        💡 <em>Planning to stay overnight in Varanasi? Read our verified guide on <a href="hotels-in-varanasi-near-kashi-vishwanath-ghats" style="color: #b45309; font-weight: 700; text-decoration: underline;">Best Hotels in Varanasi Near Kashi Vishwanath &amp; Ghats (3★, 4★, 5★)</a>.</em>
      </div>
    </div>
"""
    if "LIVE TIMINGS UPDATE" not in content:
        needle = '<!-- 100% FREE ENTRY ANNOUNCEMENT BANNER -->'
        if needle in content:
            content = content.replace(needle, live_banner + "\n    " + needle)
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(content)
            print("Added live banner to Air Show blog.")

def update_index_cards_and_faq():
    path = os.path.join(ROOT, "index.html")
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    # 1. Add Hotel card to Section 5 (Popular tour packages) if not present
    hotel_pkg_card = """      <!-- HOTELS IN VARANASI CARD -->
      <a class="card pkg reveal" href="hotels-in-varanasi-near-kashi-vishwanath-ghats" style="color:inherit;">
        <div class="pkg-top"><img class="pkg-img" src="assets/destinations/kashi-temple.webp" alt="Best Hotels in Varanasi near Kashi Vishwanath" loading="lazy" decoding="async"><span class="badge" style="background:#0284c7;">3★, 4★ &amp; 5★ Stays</span></div>
        <div class="pkg-body"><span class="days">Godowlia, Cantt &amp; Ghats</span><h3>Hotels in Varanasi Near Kashi Vishwanath</h3>
          <p class="route">Verified 3-Star, 4-Star &amp; 5-Star Hotel Guide · Senior Citizen Elevator Access · Walking Distance to Temple</p>
          <div class="price">From ₹2,200 <small>/ night (Verified Stays)</small></div>
          <span class="link-arrow" style="margin-top:6px;">Explore Hotel Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></div>
      </a>
"""
    if 'href="hotels-in-varanasi-near-kashi-vishwanath-ghats"' not in content:
        # Insert in Section 5 after 1-Day package or 3-Day package
        target = 'href="varanasi-same-day-tour-package"'
        if target in content:
            # find start of that card
            card_start = content.rfind('<a class="card pkg reveal"', 0, content.find(target))
            if card_start != -1:
                content = content[:card_start] + hotel_pkg_card + "\n      " + content[card_start:]
                print("Added Hotel Package card into index.html Section 5.")

    # 2. Add Hotel guide card to Section 6 (Latest Pilgrimage Insights) if not present in Section 6
    hotel_insight_card = """      <!-- BEST HOTELS IN VARANASI 2026 INSIGHT CARD -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="hotels-in-varanasi-near-kashi-vishwanath-ghats" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Best Hotels in Varanasi near Kashi Vishwanath Temple and Ghats" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">🏨 Hotels &amp; Stays · 7 min read</span>
          <h3><a href="hotels-in-varanasi-near-kashi-vishwanath-ghats">Best Hotels in Varanasi 2026: 3-Star, 4-Star &amp; 5-Star Stays near Kashi Vishwanath</a></h3>
          <p>Verified 2026 guide to 3-star, 4-star, and 5-star hotels in Godowlia, Cantt &amp; Ghats. Tariffs, elevator access for senior citizens &amp; VIP booking.</p>
          <a class="link-arrow bc-foot" href="hotels-in-varanasi-near-kashi-vishwanath-ghats" style="color:var(--saffron-deep);">Read Hotel Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""
    if "<!-- BEST HOTELS IN VARANASI 2026 INSIGHT CARD -->" not in content:
        target_insight = "<!-- 0. VARANASI AIR SHOW 2026 WINGS OVER GANGES -->"
        # find the second occurrence (which is inside section 6)
        pos1 = content.find(target_insight)
        if pos1 != -1:
            pos2 = content.find(target_insight, pos1 + 1)
            if pos2 != -1:
                content = content[:pos2] + hotel_insight_card + "\n      " + content[pos2:]
                print("Added Hotel insight card into index.html Section 6.")

    # 3. Add FAQ on Hotels and Kashi Darshan package in index.html FAQ section
    faq_hotel = """    <details class="faq-item" style="border-bottom:1px solid var(--line-soft); padding:16px 0;">
      <summary style="font-weight:700; font-size:1.08rem; color:var(--maroon); cursor:pointer; list-style:none; display:flex; justify-content:space-between; align-items:center;">
        Which are the best hotels to stay in Varanasi near Kashi Vishwanath Temple?
        <span style="font-size:1.2rem; color:var(--saffron-deep);">+</span>
      </summary>
      <div style="padding-top:10px; color:#4b5563; line-height:1.7;">
        For quick walking access to Kashi Vishwanath Gate 4, staying in Godowlia or near Dashashwamedh Ghat at verified 3-star hotels (₹2,200–₹3,800/night) is most convenient. For senior citizens who need elevator access and quiet surroundings, 4-star and 5-star hotels in Varanasi Cantt (like Taj Ganges, Radisson, or Brijrama Palace) provide luxury rooms and dedicated AC cab transfers. Read our complete <a href="hotels-in-varanasi-near-kashi-vishwanath-ghats" style="color:var(--saffron-deep); font-weight:700;">Varanasi Hotels Guide (3★, 4★, 5★)</a>.
      </div>
    </details>
"""
    if "Which are the best hotels to stay in Varanasi" not in content:
        faq_target = '<div class="faq-list"'
        if faq_target in content:
            pos = content.find(faq_target)
            end_div = content.find('>', pos) + 1
            content = content[:end_div] + "\n" + faq_hotel + content[end_div:]
            print("Added Hotel FAQ into index.html.")

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(content)

def update_varanasi_tour_package():
    path = os.path.join(ROOT, "varanasi-tour-package.html")
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    # Link hotel guide in package inclusion section
    target1 = 'transfer to your hotel near Godowlia or the Ghats.'
    replacement1 = 'transfer to your <a href="hotels-in-varanasi-near-kashi-vishwanath-ghats" style="color:var(--saffron-deep); font-weight:600; text-decoration:underline;">verified 3-star or 4-star hotel near Godowlia or the Ghats</a>.'
    if target1 in content:
        content = content.replace(target1, replacement1, 1)

    # Link Air Show in event calendar
    if "blog-varanasi-air-show-2026-wings-over-ganges-guide" not in content:
        target2 = '<h3>Important Yatra Tips</h3>'
        air_show_callout = """<div style="background:#fffcf7; border:1px solid #fed7aa; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:10px; margin:24px 0;">
        <h4 style="margin:0 0 6px 0; color:#92400e; font-size:1.1rem;">✈️ Special Event Alert: Varanasi Air Show 2026</h4>
        <p style="margin:0; font-size:0.95rem; color:#78350f; line-height:1.6;">
          Witness the Indian Air Force mega aerial show over River Ganga at Namo Ghat. Read our complete guide to <a href="blog-varanasi-air-show-2026-wings-over-ganges-guide" style="color:#b45309; font-weight:700; text-decoration:underline;">Varanasi Air Show 2026 (Wings Over Ganges) Schedule &amp; Free Entry</a>.
        </p>
      </div>\n      """
        if target2 in content:
            content = content.replace(target2, air_show_callout + target2, 1)
            print("Added Air Show callout to varanasi-tour-package.html.")

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(content)

def update_sitemap_lastmod():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    # Update lastmod for homepage, air show, hotels, varanasi-tour-package to 2026-10-24
    key_slugs = [
        "https://www.kashidharshan.com/",
        "https://www.kashidharshan.com/varanasi-tour-package",
        "https://www.kashidharshan.com/hotels-in-varanasi-near-kashi-vishwanath-ghats",
        "https://www.kashidharshan.com/blog-varanasi-air-show-2026-wings-over-ganges-guide",
        "https://www.kashidharshan.com/kashi-vishwanath-sugam-darshan-vip-pass",
        "https://www.kashidharshan.com/varanasi-guide",
        "https://www.kashidharshan.com/blog"
    ]

    for slug in key_slugs:
        pattern = rf"(<loc>{re.escape(slug)}</loc>\s*<lastmod>)[^<]*(</lastmod>)"
        content = re.sub(pattern, r"\g<1>2026-10-24\g<2>", content)

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(content)
    print("Updated sitemap.xml key lastmod dates to 2026-10-24.")

def update_rss_date():
    path = os.path.join(ROOT, "rss.xml")
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    content = re.sub(
        r"<lastBuildDate>[^<]*</lastBuildDate>",
        "<lastBuildDate>Sat, 24 Oct 2026 14:30:00 +0530</lastBuildDate>",
        content
    )

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(content)
    print("Updated rss.xml lastBuildDate.")

if __name__ == "__main__":
    update_foot_quick_services()
    update_air_show_live_banner()
    update_index_cards_and_faq()
    update_varanasi_tour_package()
    update_sitemap_lastmod()
    update_rss_date()
    print("All SEO booster tasks completed!")
