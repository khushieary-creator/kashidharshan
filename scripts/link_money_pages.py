import re

print("Updating services.html and blog.html with the 4 high-intent money pages...")

# 1. UPDATE SERVICES.HTML
with open("services.html", "r", encoding="utf-8") as f:
    services_content = f.read()

# Fix link on Kashi 3D/2N card
services_content = services_content.replace(
    '<a href="ayodhya-tour-package" class="btn btn-saffron" style="margin-top:8px;">Book Kashi 3D/2N Tour</a>',
    '<a href="kashi-vishwanath-tour-package" class="btn btn-saffron" style="margin-top:8px;">Book Kashi 3D/2N Tour</a>'
)

# Add a dedicated High-Intent Kashi VIP Services Section in services.html
vip_services_html = """
<!-- High-Intent Kashi VIP Booking Services -->
<section class="section" style="background: #fffcf7; border-top: 1px solid rgba(212,175,55,0.2); border-bottom: 1px solid rgba(212,175,55,0.2);">
  <div class="container">
    <div class="center" style="max-width:700px;margin:0 auto 46px;">
      <p class="eyebrow center">Instant Kashi Bookings</p>
      <h2 style="color:var(--maroon); font-family:var(--font-display); font-size:clamp(1.8rem,3.2vw,2.4rem);">Specialized Kashi Vishwanath VIP Services</h2>
      <p class="lead">Pre-book your temple passes, river aarti boats, and airport cab transfers with transparent official pricing.</p>
    </div>
    <div class="grid cols-4">
      <div class="card svc-lg reveal" style="border: 2px solid var(--gold-soft); background:#fff;">
        <div class="ic">🎫</div>
        <h3 style="font-size:1.2rem;"><a href="kashi-vishwanath-sugam-darshan-vip-pass" style="color:var(--maroon);">Sugam Darshan VIP Pass</a></h3>
        <p style="font-size:0.92rem;">Skip 3-hour general queues with fast-track entry via Gate 2 &amp; Gate 4. Includes digital locker support.</p>
        <div style="font-weight:700; color:#b45309; margin:10px 0;">Official Fee: ₹300</div>
        <a href="kashi-vishwanath-sugam-darshan-vip-pass" class="link-arrow" style="font-weight:700; color:var(--saffron-deep);">Book VIP Pass →</a>
      </div>

      <div class="card svc-lg reveal" style="border: 2px solid var(--gold-soft); background:#fff;">
        <div class="ic">⛵</div>
        <h3 style="font-size:1.2rem;"><a href="varanasi-ganga-aarti-boat-booking-cost" style="color:var(--maroon);">Ganga Aarti Boat Booking</a></h3>
        <p style="font-size:0.92rem;">Private wooden boats, motorboats and luxury double-decker Bajra rentals for Dashashwamedh evening Aarti.</p>
        <div style="font-weight:700; color:#b45309; margin:10px 0;">Starting from ₹1,500</div>
        <a href="varanasi-ganga-aarti-boat-booking-cost" class="link-arrow" style="font-weight:700; color:var(--saffron-deep);">View Boat Rates →</a>
      </div>

      <div class="card svc-lg reveal" style="border: 2px solid var(--gold-soft); background:#fff;">
        <div class="ic">🔱</div>
        <h3 style="font-size:1.2rem;"><a href="mangla-aarti-kashi-vishwanath-booking-guide" style="color:var(--maroon);">03:00 AM Mangla Aarti</a></h3>
        <p style="font-size:0.92rem;">Sit directly inside Garbhagriha for the supreme awakening ritual of Lord Shiva. Complete quota &amp; dress guidance.</p>
        <div style="font-weight:700; color:#b45309; margin:10px 0;">Official Pass: ₹500</div>
        <a href="mangla-aarti-kashi-vishwanath-booking-guide" class="link-arrow" style="font-weight:700; color:var(--saffron-deep);">Mangla Aarti Guide →</a>
      </div>

      <div class="card svc-lg reveal" style="border: 2px solid var(--gold-soft); background:#fff;">
        <div class="ic">🚕</div>
        <h3 style="font-size:1.2rem;"><a href="varanasi-airport-to-kashi-vishwanath-taxi-fare" style="color:var(--maroon);">Airport Taxi Transfer</a></h3>
        <p style="font-size:0.92rem;">Fixed pre-paid cab fare from Varanasi Airport (VNS) to Kashi Vishwanath, Godowlia and Ghats (26 km / 45 mins).</p>
        <div style="font-weight:700; color:#b45309; margin:10px 0;">Fixed Rate: ₹999 (Sedan)</div>
        <a href="varanasi-airport-to-kashi-vishwanath-taxi-fare" class="link-arrow" style="font-weight:700; color:var(--saffron-deep);">Book Airport Cab →</a>
      </div>
    </div>
  </div>
</section>
"""

if "<!-- High-Intent Kashi VIP Booking Services -->" not in services_content:
    services_content = services_content.replace('<!-- Packages -->', vip_services_html + '\n<!-- Packages -->')
    with open("services.html", "w", encoding="utf-8") as f:
        f.write(services_content)
    print("Added High-Intent Kashi VIP Booking Services to services.html!")
else:
    print("Services already present in services.html")

# 2. UPDATE BLOG.HTML TO FEATURE ALL 4 NEW MONEY PAGES
with open("blog.html", "r", encoding="utf-8") as f:
    blog_content = f.read()

new_money_cards = """
      <!-- KASHI SUGAM DARSHAN VIP PASS -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="kashi-vishwanath-sugam-darshan-vip-pass" class="bc-img"><img width="600" height="400" src="assets/reviews/kashi-temple.jpg" alt="Kashi Vishwanath Sugam Darshan VIP Pass Booking 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">🎫 VIP Pass · 5 min read</span>
          <h3><a href="kashi-vishwanath-sugam-darshan-vip-pass">Kashi Vishwanath Sugam Darshan VIP Pass Booking 2026</a></h3>
          <p>Official guidelines, ₹300 ticket fee, Gate 2 &amp; Gate 4 entry protocol, locker rules &amp; wheelchair support.</p>
          <a class="link-arrow bc-foot" href="kashi-vishwanath-sugam-darshan-vip-pass" style="color:var(--saffron-deep);">Read Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- GANGA AARTI BOAT BOOKING COST -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="varanasi-ganga-aarti-boat-booking-cost" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Ganga Aarti Boat Booking Cost & Rates 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">⛵ Boat Booking · 5 min read</span>
          <h3><a href="varanasi-ganga-aarti-boat-booking-cost">Varanasi Ganga Aarti Boat Booking Cost &amp; Private Bajra Rates 2026</a></h3>
          <p>Wooden boat ₹1,500, motorboat ₹3,500, VIP double-decker Bajra ₹8,000 &amp; sharing rates at Dashashwamedh Ghat.</p>
          <a class="link-arrow bc-foot" href="varanasi-ganga-aarti-boat-booking-cost" style="color:var(--saffron-deep);">Read Rates <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- MANGLA AARTI BOOKING GUIDE -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="mangla-aarti-kashi-vishwanath-booking-guide" class="bc-img"><img width="600" height="400" src="assets/reviews/kashi-temple.jpg" alt="Mangla Aarti Kashi Vishwanath Booking Guide 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">🔱 Temple Ritual · 5 min read</span>
          <h3><a href="mangla-aarti-kashi-vishwanath-booking-guide">Mangla Aarti Kashi Vishwanath Booking Guide 2026 (3:00 AM Pass)</a></h3>
          <p>Sit inside Garbhagriha for the divine awakening ceremony. Official ₹500 ticket price, quota release &amp; dress code.</p>
          <a class="link-arrow bc-foot" href="mangla-aarti-kashi-vishwanath-booking-guide" style="color:var(--saffron-deep);">Read Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

      <!-- VARANASI AIRPORT TO KASHI TAXI FARE -->
      <article class="card blog-card reveal" style="border: 2px solid var(--saffron);">
        <a href="varanasi-airport-to-kashi-vishwanath-taxi-fare" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Varanasi Airport to Kashi Vishwanath Taxi Fare 2026" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:var(--saffron-deep); font-weight:700;">🚕 Cab Rates · 4 min read</span>
          <h3><a href="varanasi-airport-to-kashi-vishwanath-taxi-fare">Varanasi Airport to Kashi Vishwanath Taxi Fare (Fixed Rates 2026)</a></h3>
          <p>Fixed rate ₹999 (Sedan) / ₹1,499 (Ertiga SUV). Distance 26 km, travel time 45 mins &amp; direct drops near temple.</p>
          <a class="link-arrow bc-foot" href="varanasi-airport-to-kashi-vishwanath-taxi-fare" style="color:var(--saffron-deep);">Read Fare Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>
"""

if "kashi-vishwanath-sugam-darshan-vip-pass" not in blog_content:
    target = '<div class="blog-grid">'
    blog_content = blog_content.replace(target, target + new_money_cards)
    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(blog_content)
    print("Added 4 money pages to blog.html blog-grid!")
else:
    print("Money pages already present in blog.html")

print("Services and Blog integration completed!")
