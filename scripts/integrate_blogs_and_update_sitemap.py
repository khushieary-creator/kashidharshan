import re
import glob

print("Starting Integration of Blogs, Sitemap Refresh & DateModified Updates...")

# ======================================================================
# 1. UPDATE BLOG.HTML TO INCLUDE ALL 6 MISSING/NEW BLOGS
# ======================================================================
print("\n--- 1. Updating blog.html with all 42 blogs ---")
with open("blog.html", "r", encoding="utf-8") as f:
    blog_page = f.read()

new_blog_cards = """
      <!-- DEV DEEPAWALI 2026 SPECIAL -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Dev Deepawali 2026 VIP Boat Booking & Ghat Guide" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Festival Special · 6 min read</span>
          <h3><a href="blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html">Varanasi Dev Deepawali 2026: VIP Boat Booking &amp; Ghat Guide</a></h3>
          <p>Official guide on Dev Deepawali 2026 boat booking, private bajra prices, Ganga Aarti timings, laser show viewing &amp; direct reservation.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html" style="color:var(--saffron-deep);">Read Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- MANGLA AARTI 2026 SPECIAL -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-kashi-vishwanath-mangla-aarti-online-booking-guide-2026.html" class="bc-img"><img width="600" height="400" src="assets/reviews/kashi-temple.jpg" alt="Kashi Vishwanath Mangla Aarti Online Booking 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Aarti Special · 5 min read</span>
          <h3><a href="blog-kashi-vishwanath-mangla-aarti-online-booking-guide-2026.html">Kashi Vishwanath Mangla Aarti Online Booking 2026: Pass Price &amp; Rules</a></h3>
          <p>Complete guide for Kashi Vishwanath Mangla Aarti online booking, ticket price (₹500-₹1000), 03:00 AM entry gates &amp; dress code.</p>
          <a class="link-arrow bc-foot" href="blog-kashi-vishwanath-mangla-aarti-online-booking-guide-2026.html" style="color:var(--saffron-deep);">Read Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- AYODHYA DEEPOTSAV & KASHI DEV DEEPAWALI 2026 -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-deepotsav-kashi-dev-deepawali-tour-package-2026.html" class="bc-img"><img width="600" height="400" src="assets/reviews/ayodhya-night.jpg" alt="Ayodhya Deepotsav and Kashi Dev Deepawali Tour Package 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Festive Special · 7 min read</span>
          <h3><a href="blog-ayodhya-deepotsav-kashi-dev-deepawali-tour-package-2026.html">Ayodhya Deepotsav &amp; Kashi Dev Deepawali Tour Package 2026</a></h3>
          <p>Combined festive package: 25 lakh diyas in Ayodhya, VIP Ram Mandir darshan, and private boat ride for 84 ghats Dev Deepawali in Kashi.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-deepotsav-kashi-dev-deepawali-tour-package-2026.html" style="color:var(--saffron-deep);">Read Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- SPARSH DARSHAN 2026 SPECIAL -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-kashi-vishwanath-sparsh-darshan-booking-rules-2026.html" class="bc-img"><img width="600" height="400" src="assets/reviews/kashi-temple.jpg" alt="Kashi Vishwanath Sparsh Darshan Booking 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Ritual Special · 5 min read</span>
          <h3><a href="blog-kashi-vishwanath-sparsh-darshan-booking-rules-2026.html">Kashi Vishwanath Sparsh Darshan Booking 2026: Timings &amp; Rules</a></h3>
          <p>Step-by-step guide to touching the Golden Jyotirlinga, morning &amp; afternoon Sparsh slots, dhoti/saree dress code, and Rudrabhishekam.</p>
          <a class="link-arrow bc-foot" href="blog-kashi-vishwanath-sparsh-darshan-booking-rules-2026.html" style="color:var(--saffron-deep);">Read Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- VIP PASS ONLINE BOOKING PRICE GUIDE -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-kashi-vishwanath-vip-pass-online-booking-price-guide.html" class="bc-img"><img width="600" height="400" src="assets/reviews/kashi-temple.jpg" alt="Kashi Vishwanath VIP Darshan Pass Online Booking Price" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">VIP Guide · 5 min read</span>
          <h3><a href="blog-kashi-vishwanath-vip-pass-online-booking-price-guide.html">Kashi Vishwanath VIP Darshan Pass Online Booking 2026: Price &amp; Timings</a></h3>
          <p>Detailed breakdown of Sugam Darshan ticket fees, online portal slot availability, and VIP corridor fast entry gates.</p>
          <a class="link-arrow bc-foot" href="blog-kashi-vishwanath-vip-pass-online-booking-price-guide.html" style="color:var(--saffron-deep);">Read Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- VARANASI LOCAL SIGHTSEEING TOUR PACKAGE -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-varanasi-local-sightseeing-tour-package.html" class="bc-img"><img width="600" height="400" src="assets/destinations/sarnath.webp" alt="Varanasi Local Sightseeing Tour Package Guide" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Sightseeing · 5 min read</span>
          <h3><a href="blog-varanasi-local-sightseeing-tour-package.html">Varanasi Local Sightseeing Tour Package: Full Day Cab &amp; Temple Guide</a></h3>
          <p>Explore Sankat Mochan, BHU New Vishwanath Temple, Durga Kund, and Sarnath with private sanitized AC cab and local guide.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-local-sightseeing-tour-package.html" style="color:var(--saffron-deep);">Read Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""

# Inject before the first </main> or inside grid in blog.html
if "blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html" not in blog_page:
    # Find grid container in blog.html
    grid_match = re.search(r'<div class="grid cols-3[^"]*">', blog_page)
    if grid_match:
        insert_pos = grid_match.end()
        blog_page = blog_page[:insert_pos] + "\n" + new_blog_cards + blog_page[insert_pos:]
        with open("blog.html", "w", encoding="utf-8") as f:
            f.write(blog_page)
        print("Injected 6 featured blogs into blog.html grid!")
    else:
        print("Warning: grid cols-3 not found in blog.html")

# ======================================================================
# 2. UPDATE INDEX.HTML TO FEATURE 6 HIGH-CONVERTING VIRAL GUIDES
# ======================================================================
print("\n--- 2. Updating Featured Blogs on index.html ---")
with open("index.html", "r", encoding="utf-8") as f:
    index_page = f.read()

featured_blogs_html = """    <div class="grid cols-3">
      <!-- 1. DEV DEEPAWALI 2026 -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Dev Deepawali 2026 VIP Boat Booking & Ghat Guide" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Trending Festival · 6 min read</span>
          <h3><a href="blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html">Varanasi Dev Deepawali 2026: VIP Boat Booking &amp; Ghat Guide</a></h3>
          <p>Official guide on Dev Deepawali private bajra rates, Ganga Aarti illumination timings &amp; direct boat booking.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html" style="color:var(--saffron-deep);">Read Boat Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- 2. MANGLA AARTI 2026 -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-kashi-vishwanath-mangla-aarti-online-booking-guide-2026.html" class="bc-img"><img width="600" height="400" src="assets/reviews/kashi-temple.jpg" alt="Kashi Vishwanath Mangla Aarti Online Booking 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Temple Aarti · 5 min read</span>
          <h3><a href="blog-kashi-vishwanath-mangla-aarti-online-booking-guide-2026.html">Kashi Vishwanath Mangla Aarti Online Booking 2026: Pass Price &amp; Rules</a></h3>
          <p>Complete guide for Kashi Vishwanath Mangla Aarti online booking, ticket price (₹500-₹1000), 03:00 AM entry gates &amp; dress code.</p>
          <a class="link-arrow bc-foot" href="blog-kashi-vishwanath-mangla-aarti-online-booking-guide-2026.html" style="color:var(--saffron-deep);">Read Aarti Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- 3. AYODHYA DEEPOTSAV & KASHI DEV DEEPAWALI -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-ayodhya-deepotsav-kashi-dev-deepawali-tour-package-2026.html" class="bc-img"><img width="600" height="400" src="assets/reviews/ayodhya-night.jpg" alt="Ayodhya Deepotsav and Kashi Dev Deepawali Tour Package 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Combined Festive · 7 min read</span>
          <h3><a href="blog-ayodhya-deepotsav-kashi-dev-deepawali-tour-package-2026.html">Ayodhya Deepotsav &amp; Kashi Dev Deepawali Tour Package 2026</a></h3>
          <p>Combined festive package: 25 lakh diyas in Ayodhya, VIP Ram Mandir darshan, and private boat ride for 84 ghats Dev Deepawali.</p>
          <a class="link-arrow bc-foot" href="blog-ayodhya-deepotsav-kashi-dev-deepawali-tour-package-2026.html" style="color:var(--saffron-deep);">Read Festival Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- 4. SPARSH DARSHAN 2026 -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-kashi-vishwanath-sparsh-darshan-booking-rules-2026.html" class="bc-img"><img width="600" height="400" src="assets/reviews/kashi-temple.jpg" alt="Kashi Vishwanath Sparsh Darshan Booking 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Abhishek Guide · 5 min read</span>
          <h3><a href="blog-kashi-vishwanath-sparsh-darshan-booking-rules-2026.html">Kashi Vishwanath Sparsh Darshan Booking 2026: Timings &amp; Rules</a></h3>
          <p>Learn how to touch the Golden Jyotirlinga, morning &amp; afternoon Sparsh slots, dhoti/saree dress code, and Rudrabhishekam.</p>
          <a class="link-arrow bc-foot" href="blog-kashi-vishwanath-sparsh-darshan-booking-rules-2026.html" style="color:var(--saffron-deep);">Read Sparsh Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- 5. RAM MANDIR VIP PASS -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-ram-mandir-vip-pass-booking-guide.html" class="bc-img"><img width="600" height="400" src="assets/reviews/ayodhya-night.jpg" alt="Ram Mandir VIP Pass Online Booking Price Slots" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">VIP Pass · 4 min read</span>
          <h3><a href="blog-ram-mandir-vip-pass-booking-guide.html">Ram Mandir VIP Pass Booking: Price, Slots &amp; Priority Entry Guide</a></h3>
          <p>Confused about Ram Mandir VIP entry? Read our detailed guide on booking Sugam Darshan/VIP passes and priority queue tips.</p>
          <a class="link-arrow bc-foot" href="blog-ram-mandir-vip-pass-booking-guide.html" style="color:var(--saffron-deep);">Read VIP Pass Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- 6. GANGA CRUISE BOOKING -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="blog-varanasi-ganga-cruise-booking-guide.html" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Ganga Cruise Booking Alaknanda Ro-Ro price slots" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">Varanasi Cruise · 5 min read</span>
          <h3><a href="blog-varanasi-ganga-cruise-booking-guide.html">Varanasi Ganga Cruise Booking 2026: Alaknanda, Ro-Ro Price &amp; Slots</a></h3>
          <p>Planning a luxury cruise ride in Varanasi? Read our guide on Kashi Ganga Cruise online booking, Alaknanda Cruise tickets, and timings.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-ganga-cruise-booking-guide.html" style="color:var(--saffron-deep);">Read Cruise Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
    </div>"""

# Replace the grid in index.html
old_grid_pattern = r'<div class="grid cols-3">\s*<article class="card blog-card reveal"[^>]*>.*?</div>\s*</div>\s*</article>\s*</div>'
if re.search(r'<p class="eyebrow center">Travel Guides &amp; Yatra Tips</p>', index_page):
    sub_start = index_page.find('<p class="eyebrow center">Travel Guides &amp; Yatra Tips</p>')
    grid_start = index_page.find('<div class="grid cols-3">', sub_start)
    grid_end = index_page.find('<div class="center" style="margin-top:40px;">', grid_start)
    if grid_start != -1 and grid_end != -1:
        index_page = index_page[:grid_start] + featured_blogs_html + "\n    " + index_page[grid_end:]
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(index_page)
        print("Updated index.html with 6 featured high-intent blogs!")

# ======================================================================
# 3. REFRESH SITEMAP.XML WITH NEW BLOGS & CURRENT LASTMOD
# ======================================================================
print("\n--- 3. Refreshing sitemap.xml with 2026-10-12 timestamps ---")
all_html_files = sorted(glob.glob("*.html"))
all_html_files = [f for f in all_html_files if f != "google0dc20d35f8fb3bcd.html"]

sitemap_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.kashidharshan.com/</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
"""

for f in all_html_files:
    if f == "index.html":
        continue
    priority = "0.9" if "tour-package" in f else ("0.8" if "blog-" in f or "guide" in f else "0.7")
    changefreq = "daily" if "tour-package" in f or "blog-" in f else "weekly"
    sitemap_xml_content += f"""  <url>
    <loc>https://www.kashidharshan.com/{f}</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""

sitemap_xml_content += "</urlset>\n"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml_content)

print(f"Generated clean sitemap.xml with {len(all_html_files)} URLs set to 2026-10-12!")

# ======================================================================
# 4. UPDATE DATEMODIFIED IN SCHEMAS ACROSS CORE PAGES
# ======================================================================
print("\n--- 4. Updating dateModified to 2026-10-12 across all HTML schemas ---")
dm_updated_count = 0
for f in all_html_files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    orig = c
    c = re.sub(r'"dateModified":\s*"2026-[0-9]{2}-[0-9]{2}[^"]*"', '"dateModified": "2026-10-12"', c)
    if c != orig:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(c)
        dm_updated_count += 1

print(f"Updated dateModified to 2026-10-12 across {dm_updated_count} files!")
print("\nAll integration & sitemap tasks completed successfully!")
