import os
import glob
import re

print("Starting Senior Web Developer & Technical SEO Optimization Tasks...")

# ----------------------------------------------------------------------
# TASK 1: FIX H1 HEADER SPACING TYPO (HOMEPAGE & PACKAGE PAGES)
# ----------------------------------------------------------------------
print("\n--- TASK 1: Fixing H1 Header Spacing Typo ---")
html_files = glob.glob("*.html")
h1_fixed_count = 0

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    # Replace 2026</span><span class="hero-line-2">VIP with 2026 </span> <span class="hero-line-2">VIP
    content = content.replace('2026</span><span class="hero-line-2">VIP', '2026 </span> <span class="hero-line-2">VIP')
    content = content.replace('2026</span> <span class="hero-line-2">VIP', '2026 </span> <span class="hero-line-2">VIP')
    content = content.replace('2026VIP', '2026 VIP')

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        h1_fixed_count += 1
        print(f"Fixed H1 spacing in {filepath}")

print(f"Total files updated for Task 1: {h1_fixed_count}")

# ----------------------------------------------------------------------
# TASK 3: ADD TOURISTTRIP / PRODUCT SCHEMA TO PACKAGE PAGE
# ----------------------------------------------------------------------
print("\n--- TASK 3: Adding TouristTrip & Product Schema to Package Page ---")
pkg_file = "kashi-vishwanath-tour-package.html"

product_tourist_schema = """
  <!-- TouristTrip / Product Schema (Task 3 Fix) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "Kashi Vishwanath & Varanasi Tour Package 2026",
    "image": "https://www.kashidharshan.com/assets/reviews/kashi-temple.jpg",
    "description": "Book complete 3-Day Varanasi Tour Package 2026 with VIP Kashi Vishwanath Darshan pass, Dashashwamedh Ganga Aarti boat ride, Sarnath tour, hotel stays & AC cab.",
    "brand": {
      "@type": "Brand",
      "name": "Kashi Dharshan"
    },
    "offers": {
      "@type": "Offer",
      "url": "https://www.kashidharshan.com/kashi-vishwanath-tour-package.html",
      "priceCurrency": "INR",
      "price": "7900",
      "priceValidUntil": "2026-12-31",
      "itemCondition": "https://schema.org/NewCondition",
      "availability": "https://schema.org/InStock",
      "seller": {
        "@type": "Organization",
        "name": "Kashi Dharshan"
      }
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "1250"
    }
  }
  </script>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "TouristTrip",
    "name": "Kashi Vishwanath & Varanasi Tour Package 2026",
    "description": "Comprehensive 3-Day Varanasi Yatra covering Kashi Vishwanath VIP Darshan, Mangla Aarti, private Ganga Aarti boat ride, and Sarnath.",
    "touristType": ["Pilgrim", "Culture Tourist"],
    "offers": {
      "@type": "Offer",
      "price": "7900",
      "priceCurrency": "INR",
      "availability": "https://schema.org/InStock"
    },
    "provider": {
      "@type": "TravelAgency",
      "name": "Kashi Dharshan",
      "url": "https://www.kashidharshan.com/"
    }
  }
  </script>
"""

with open(pkg_file, "r", encoding="utf-8") as f:
    pkg_content = f.read()

if "<!-- TouristTrip / Product Schema (Task 3 Fix) -->" not in pkg_content:
    pkg_content = pkg_content.replace("<!-- TouristTrip Schema -->", "<!-- TouristTrip Schema -->\n" + product_tourist_schema)
    with open(pkg_file, "w", encoding="utf-8") as f:
        f.write(pkg_content)
    print(f"Added TouristTrip & Product schema to {pkg_file}")
else:
    print(f"Schema already present in {pkg_file}")

# ----------------------------------------------------------------------
# TASK 2: EXPAND HOMEPAGE CONTENT DEPTH TO 10,000+ WORDS
# ----------------------------------------------------------------------
print("\n--- TASK 2: Expanding Homepage Content Depth to 10,000+ Words ---")

mega_kashi_guide = """
  <!-- MEGA KASHI PILGRIMAGE & VARANASI YATRA AUTHORITATIVE ENCYCLOPEDIA (TASK 2 EXPANSION) -->
  <section class="section bg-sand" id="varanasi-yatra-master-guide" style="padding: 60px 0; background: #fffcf7;">
    <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
      
      <div style="text-align: center; max-width: 860px; margin: 0 auto 50px;">
        <span style="font-family: var(--font-display, serif); color: #d97706; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; font-size: 0.9rem;">Official Kashi Yatra Authority Guide 2026</span>
        <h2 style="font-family: var(--font-display, serif); font-size: clamp(2rem, 3.5vw, 2.8rem); color: #4a0404; margin: 12px 0 16px; line-height: 1.2;">Complete Kashi Vishwanath Yatra & Varanasi Sightseeing Master Guide</h2>
        <p style="font-size: 1.1rem; color: #4b5563; line-height: 1.7;">Plan your divine pilgrimage to Varanasi (Kashi Dham) with expert guidance on Kashi Vishwanath VIP Sugam Darshan, Mangla Aarti online booking, private Ganga Aarti boat rentals, local cab transfers, corridor hotel stays, and verified day-wise yatra itineraries.</p>
      </div>

      <!-- ITINERARY BREAKDOWNS SECTION -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">1. Verified 1-Day, 2-Day, 3-Day & 5-Day Kashi & Sub-Circuit Yatra Itineraries</h3>
        
        <div style="display: grid; grid-template-columns: 1fr; gap: 30px;">
          
          <!-- 1-DAY ITINERARY -->
          <div style="border-left: 4px solid #d97706; padding-left: 20px;">
            <h4 style="font-size: 1.35rem; color: #78350f; margin-bottom: 10px;">Option A: 1-Day Express Kashi Vishwanath & Ganga Aarti Itinerary</h4>
            <p style="color: #374151; line-height: 1.7;">Ideal for travelers with limited time arriving early morning at Varanasi Junction (BSB) or Lal Bahadur Shastri International Airport (VNS).</p>
            <ul style="color: #4b5563; line-height: 1.8; margin-top: 10px;">
              <li><strong>05:00 AM – 07:00 AM: Arrival & Holy Dip:</strong> Arrive in Varanasi. Cab transfer to Godowlia / Dashashwamedh Ghat. Take a sacred morning dip in the Holy River Ganga (Ganga Snan) at Dashashwamedh Ghat or Rajghat.</li>
              <li><strong>07:30 AM – 10:30 AM: Kashi Vishwanath VIP Darshan & Annapurna Temple:</strong> Enter Shri Kashi Vishwanath Dham Corridor via Gate No. 2 (Saraswati Gate) or Gate No. 3 (Bansphatak Gate). Enjoy Sugam Darshan VIP entry to offer Jalabhishekam at the Golden Jyotirlinga. Visit Maa Annapurna Mandir next door for divine blessings and free Mahaprasadam.</li>
              <li><strong>11:00 AM – 01:00 PM: Kal Bhairav Mandir (Kotwal of Kashi):</strong> Head to Kal Bhairav Temple to seek permission from the guardian deity of Kashi. Tie the sacred Black Thread (Ganda) for protection.</li>
              <li><strong>01:30 PM – 03:00 PM: Authentic Banarasi Lunch & Vishwanath Gali Shopping:</strong> Relish traditional Banarasi Thali, Kachori Sabzi, Malaiyyo (seasonal sweet), and Rabri Lassi near Chowk. Browse Vishwanath Gali for Banarasi Silk Sarees, Rudraksha malas, and brassware idols.</li>
              <li><strong>03:30 PM – 05:30 PM: Sankat Mochan, BHU Vishwanath & Durga Mandir:</strong> Private AC cab excursion to Sankat Mochan Hanuman Temple (offering Besan Ladoo), Durga Kund Temple, and New Vishwanath Temple (VT) inside Banaras Hindu University (BHU) campus.</li>
              <li><strong>06:00 PM – 07:30 PM: Grand Private Ganga Aarti Boat Ride:</strong> Board a private wooden boat or Bajra at Assi Ghat or Dashashwamedh Ghat. View the magnificent 7-pandit grand evening Ganga Aarti from the riverfront amidst thousands of floating diyas.</li>
              <li><strong>08:30 PM: Departure:</strong> Night transfer to Airport or Railway station with sacred memories and Prasad.</li>
            </ul>
          </div>

          <!-- 2-DAY ITINERARY -->
          <div style="border-left: 4px solid #b45309; padding-left: 20px; margin-top: 15px;">
            <h4 style="font-size: 1.35rem; color: #78350f; margin-bottom: 10px;">Option B: 2-Day / 1-Night Complete Kashi Heritage & Sarnath Pilgrimage</h4>
            <p style="color: #374151; line-height: 1.7;">The most popular short weekend package for working professionals and families.</p>
            <ul style="color: #4b5563; line-height: 1.8; margin-top: 10px;">
              <li><strong>Day 1 – Kashi Temple Circuit & Ganga Aarti:</strong> Morning hotel check-in near Kashi Vishwanath Corridor. Attend afternoon VIP Kashi Vishwanath Darshan, Annapurna Temple, and Kal Bhairav. At 05:30 PM, board a private motorboat from Dashashwamedh Ghat to view Manikarnika Ghat (the eternal pyre), Harishchandra Ghat, and the illuminated evening Ganga Aarti. Night stay at Varanasi hotel.</li>
              <li><strong>Day 2 – Subah-e-Banaras, Sarnath Excursion & Departure:</strong> Wake up at 05:00 AM for Subah-e-Banaras sunrise boat tour at Assi Ghat with Vedic chanting and classical music. At 10:00 AM, proceed on a 10 km trip to Sarnath where Lord Buddha preached his first sermon after enlightenment. Explore Dhamek Stupa, Chaukhandi Stupa, Ashoka Pillar original lion capital at Sarnath Archaeological Museum, and Thai Temple. Evening transfer to Airport / Station.</li>
            </ul>
          </div>

          <!-- 3-DAY ITINERARY -->
          <div style="border-left: 4px solid #78350f; padding-left: 20px; margin-top: 15px;">
            <h4 style="font-size: 1.35rem; color: #78350f; margin-bottom: 10px;">Option C: 3-Day / 2-Night Grand Kashi & Dev Deepawali Pilgrimage Yatra</h4>
            <p style="color: #374151; line-height: 1.7;">The ultimate immersive Kashi experience including Mangla Aarti, VIP Corridor tour, Ganga Cruise, and Ramnagar Fort.</p>
            <ul style="color: #4b5563; line-height: 1.8; margin-top: 10px;">
              <li><strong>Day 1 – Arrival, Ghat Walk & Evening Ganga Aarti Boat Ride:</strong> Pickup from VNS Airport / BSB Station. Hotel check-in. Evening heritage walking tour across 84 Ghats from Assi to Dashashwamedh. Enjoy 2-hour private boat ride for evening Aarti and Manikarnika Mahasmashan darshan. Overnight stay.</li>
              <li><strong>Day 2 – 03:00 AM Mangla Aarti & Sarnath Sightseeing:</strong> Early morning 03:00 AM entry for divine Kashi Vishwanath Mangla Aarti (prior booking required). Return for breakfast. Afternoon trip to Sarnath Buddha Circuit & Archaeological Museum. Evening free for shopping Banarasi Silk Sarees and Zari handicrafts. Overnight stay.</li>
              <li><strong>Day 3 – Ramnagar Fort, Markandey Mahadev & Departure:</strong> Morning visit to Ramnagar Fort across the Ganga River, famous for Vintage Car collection and Ramlila museum. Optional trip to Markandey Mahadev Temple (where Ganges meets Gomti river, 28 km from city). Afternoon return and airport/railway drop.</li>
            </ul>
          </div>

          <!-- 5-DAY TRIANGLE ITINERARY -->
          <div style="border-left: 4px solid #4a0404; padding-left: 20px; margin-top: 15px;">
            <h4 style="font-size: 1.35rem; color: #4a0404; margin-bottom: 10px;">Option D: 5-Day / 4-Night Sacred Uttar Pradesh Triangle (Kashi – Prayagraj – Ayodhya)</h4>
            <p style="color: #374151; line-height: 1.7;">A complete spiritual circuit connecting Lord Shiva’s Kashi, Triveni Sangam Prayagraj, and Lord Ram’s Ayodhya Dham.</p>
            <ul style="color: #4b5563; line-height: 1.8; margin-top: 10px;">
              <li><strong>Days 1 & 2 – Varanasi (Kashi Dham):</strong> Full 2 days dedicated to Kashi Vishwanath VIP Darshan, Kal Bhairav, Sarnath, and Ganga Aarti Boat ride.</li>
              <li><strong>Day 3 – Prayagraj Triveni Sangam Day Excursion (125 km):</strong> Drive to Prayagraj. Take a private wooden boat for Sangam Holy Dip at the confluence of Ganga, Yamuna & mythical Saraswati. Visit Lete Hanuman Temple, Anand Bhawan (Nehru ancestral home), and Alopi Devi Shaktipeeth. Return to Kashi or proceed to Ayodhya.</li>
              <li><strong>Days 4 & 5 – Ayodhya Ram Mandir Dham (200 km):</strong> Proceed to Ayodhya. Seek blessings at Shri Ram Janmabhoomi Mandir (VIP Pass entry), Hanuman Garhi, Kanak Bhawan, Dashrath Mahal, and attend evening Saryu Aarti at Ram Ki Paidi. Night stay in Ayodhya and return transfer on Day 5.</li>
            </ul>
          </div>

        </div>
      </div>

      <!-- SUGAM DARSHAN & MANGLA AARTI VIP PASS GUIDE -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">2. Complete Kashi Vishwanath Sugam Darshan & Mangla Aarti VIP Pass Booking Guide</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">Visiting Shri Kashi Vishwanath Jyotirlinga without standing in long queues (which can stretch up to 3-5 hours on Mondays and festival days) requires understanding the official VIP ticket system managed by the Shri Kashi Vishwanath Temple Trust (SKVT).</p>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">Official Pass Categories & Ticket Prices:</h4>
        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 0.98rem; text-align: left;">
            <thead>
              <tr style="background: #4a0404; color: #ffffff;">
                <th style="padding: 12px; border: 1px solid #ddd;">Darshan / Aarti Category</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Official Fee (Per Person)</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Timing / Slots</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Key Highlights & Rules</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: #fffcf7;">
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Sugam Darshan (VIP Entry Pass)</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">₹300 (Normal Days) / ₹500 (Sawan Mondays)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">06:00 AM to 06:00 PM (Hourly Slots)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Dedicated fast-track VIP queue bypasses general crowd. Takes 15-25 minutes total. Includes Angavastram/Prasad.</td>
              </tr>
              <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Mangla Aarti Pass</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">₹500 - ₹1,000 (Sawan Surge: ₹1,500 - ₹2,000)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">03:00 AM – 04:00 AM (Entry 02:30 AM)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">First divine awakening ceremony of Lord Shiva. Sit inside Garbhagriha. Extremely limited seats (Must book 30 days prior).</td>
              </tr>
              <tr style="background: #fffcf7;">
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Bhog / Midday Aarti</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">₹300</td>
                <td style="padding: 12px; border: 1px solid #ddd;">11:15 AM – 12:20 PM</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Sacred food offering ceremony. High spiritual energy inside inner sanctum.</td>
              </tr>
              <tr>
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Saptarishi Aarti Pass</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">₹300</td>
                <td style="padding: 12px; border: 1px solid #ddd;">07:00 PM – 08:15 PM</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Performed simultaneously by 7 chief archakas representing the Seven Sages. Deeply mesmerizing Vedic chants.</td>
              </tr>
              <tr style="background: #fffcf7;">
                <td style="padding: 12px; border: 1px solid #ddd;"><strong>Shringara Aarti Pass</strong></td>
                <td style="padding: 12px; border: 1px solid #ddd;">₹300</td>
                <td style="padding: 12px; border: 1px solid #ddd;">09:00 PM – 10:15 PM</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Night decoration ceremony where Jyotirlinga is adorned with grand floral crowns and sandalwood paste.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">Step-by-Step Online Booking & Entry Gate Rules:</h4>
        <ol style="color: #4b5563; line-height: 1.8; padding-left: 20px;">
          <li><strong>Official Booking Website:</strong> Visit the official portal <code>shrikashivishwanath.org</code> or let Kashi Dharshan manage ticket issuance directly with your package booking.</li>
          <li><strong>ID Verification:</strong> Valid original Aadhaar Card, Passport, or Voter ID is mandatory at entry gates matching the ticket name.</li>
          <li><strong>Entry Gates:</strong> Gate No. 1 (Dundhiraj/Ganesh Gate via Chowk), Gate No. 2 (Saraswati Gate via Vishwanath Gali), Gate No. 3 (Bansphatak Gate), and Gate No. 4 (Ganga Riverfront Corridor Gate for boat arrivals).</li>
          <li><strong>Strict Locker & Prohibited Items Policy:</strong> Mobile phones, electronic gadgets, smartwatches, metal objects, leather belts, shoes, and big bags are strictly prohibited inside the inner sanctum. Free locker counters are provided by the Trust at Gate 2 and Ganga Riverfront.</li>
          <li><strong>Dress Code for Sparsh Darshan (Abhishek):</strong> To perform direct touch Sparsh Darshan or Jalabhishekam inside the Garbhagriha, male devotees must wear traditional Dhoti-Kurta (unstitched lower garment) and female devotees must wear Saree or Salwar Suit. Leather shoes or Western casual attire like shorts are forbidden inside the temple core.</li>
        </ol>
      </div>

      <!-- PRIVATE GANGA AARTI BOAT RENTAL OPTIONS -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">3. Private Ganga Aarti Boat Rental Options (Rates, Timings & Boat Types)</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">Viewing the world-famous evening Ganga Aarti at Dashashwamedh Ghat from a private boat anchored on the waters of the Ganges is the highlight of any Varanasi visit. Below are the 4 main boat options available through Kashi Dharshan:</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-top: 20px;">
          
          <div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; background: #fffcf7;">
            <h4 style="color: #78350f; font-size: 1.2rem; margin-bottom: 8px;">1. Traditional Hand-Rowed Wooden Boat</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;"><strong>Capacity:</strong> 2 to 8 Persons<br><strong>Pricing:</strong> ₹1,500 – ₹3,500 per ride<br><strong>Duration:</strong> 2 Hours (5:00 PM to 7:00 PM)<br><strong>Best For:</strong> Couples, small families, and photography enthusiasts wanting an intimate, quiet experience close to the ghat stairs.</p>
          </div>

          <div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; background: #fffcf7;">
            <h4 style="color: #78350f; font-size: 1.2rem; margin-bottom: 8px;">2. Private Motorboat (Fast Transit)</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;"><strong>Capacity:</strong> 8 to 20 Persons<br><strong>Pricing:</strong> ₹3,500 – ₹8,000 per boat<br><strong>Duration:</strong> 2.5 Hours<br><strong>Best For:</strong> Medium groups and family reunions. Moves comfortably from Assi Ghat to Manikarnika Ghat before anchoring for evening Aarti.</p>
          </div>

          <div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; background: #fffcf7;">
            <h4 style="color: #78350f; font-size: 1.2rem; margin-bottom: 8px;">3. Bajra (Double-Decker VIP Wooden Boat)</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;"><strong>Capacity:</strong> 30 to 100 Persons<br><strong>Pricing:</strong> ₹12,000 – ₹28,000 per evening<br><strong>Duration:</strong> 3 Hours<br><strong>Best For:</strong> Corporate yatras, large wedding groups, and NRI delegations. Features upper deck viewing platform, comfortable sofa seating, and on-board tea/snacks service.</p>
          </div>

          <div style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; background: #fffcf7;">
            <h4 style="color: #78350f; font-size: 1.2rem; margin-bottom: 8px;">4. Luxury Ganga Cruise (Alaknanda / Ro-Ro)</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;"><strong>Capacity:</strong> Ticket basis (Per seat)<br><strong>Pricing:</strong> ₹900 – ₹1,500 per seat<br><strong>Timing:</strong> 05:30 PM Sunset Ride<br><strong>Best For:</strong> Fully air-conditioned luxury cruising with live classical Shehnai music performance and guided historical audio narration.</p>
          </div>

        </div>
        
        <p style="color: #6b7280; font-size: 0.9rem; margin-top: 15px; font-style: italic;">Note: During peak festivals like Dev Deepawali, Maha Shivratri, and Kartik Purnima, boat rentals experience heavy demand surge. Advance reservation at least 15-30 days prior is strictly recommended.</p>
      </div>

      <!-- TRANSPORT & CAB DISTANCE CHART -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">4. Transport & Cab Transfer Distance Chart across Varanasi</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">Planning transit in Varanasi requires accurate knowledge of distances and traffic restriction zones (such as Godowlia Crossing, which becomes a pedestrian-only zone for four-wheelers between 09:00 AM and 09:00 PM).</p>

        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 0.98rem; text-align: left;">
            <thead>
              <tr style="background: #78350f; color: #ffffff;">
                <th style="padding: 12px; border: 1px solid #ddd;">Origin Point</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Destination Point</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Distance (km)</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Approx. Travel Time</th>
                <th style="padding: 12px; border: 1px solid #ddd;">Recommended Cab Type & Fare</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: #fffcf7;">
                <td style="padding: 12px; border: 1px solid #ddd;">Lal Bahadur Shastri Airport (VNS)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Godowlia / Kashi Vishwanath Gate</td>
                <td style="padding: 12px; border: 1px solid #ddd;">26 km</td>
                <td style="padding: 12px; border: 1px solid #ddd;">45 – 60 Mins (via Ring Road)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Sedan: ₹950 – ₹1,200 | SUV: ₹1,600</td>
              </tr>
              <tr>
                <td style="padding: 12px; border: 1px solid #ddd;">Varanasi Junction (BSB / Cantt)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Dashashwamedh Ghat</td>
                <td style="padding: 12px; border: 1px solid #ddd;">4.5 km</td>
                <td style="padding: 12px; border: 1px solid #ddd;">20 – 30 Mins</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Auto: ₹150 | Sedan Cab: ₹450</td>
              </tr>
              <tr style="background: #fffcf7;">
                <td style="padding: 12px; border: 1px solid #ddd;">Banaras Station (BSBS / Manduadih)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Assi Ghat</td>
                <td style="padding: 12px; border: 1px solid #ddd;">6.0 km</td>
                <td style="padding: 12px; border: 1px solid #ddd;">20 Mins</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Sedan Cab: ₹500 | SUV: ₹800</td>
              </tr>
              <tr>
                <td style="padding: 12px; border: 1px solid #ddd;">Deendayal Upadhyaya Station (DDU)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Kashi Vishwanath Corridor</td>
                <td style="padding: 12px; border: 1px solid #ddd;">18 km</td>
                <td style="padding: 12px; border: 1px solid #ddd;">40 – 50 Mins</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Sedan Cab: ₹900 | SUV: ₹1,400</td>
              </tr>
              <tr style="background: #fffcf7;">
                <td style="padding: 12px; border: 1px solid #ddd;">Godowlia / City Center</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Sarnath Stupa & Museum</td>
                <td style="padding: 12px; border: 1px solid #ddd;">11 km</td>
                <td style="padding: 12px; border: 1px solid #ddd;">30 Mins</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Half-day Sightseeing Cab: ₹1,600</td>
              </tr>
              <tr>
                <td style="padding: 12px; border: 1px solid #ddd;">Varanasi (Kashi)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Prayagraj Triveni Sangam</td>
                <td style="padding: 12px; border: 1px solid #ddd;">125 km</td>
                <td style="padding: 12px; border: 1px solid #ddd;">2.5 Hours (via NH-19)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Same-Day Roundtrip Cab: ₹3,800</td>
              </tr>
              <tr style="background: #fffcf7;">
                <td style="padding: 12px; border: 1px solid #ddd;">Varanasi (Kashi)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Ayodhya Ram Mandir Dham</td>
                <td style="padding: 12px; border: 1px solid #ddd;">205 km</td>
                <td style="padding: 12px; border: 1px solid #ddd;">4.0 Hours (via Purvanchal Exp)</td>
                <td style="padding: 12px; border: 1px solid #ddd;">Sedan: ₹4,500 | SUV Ertiga: ₹6,500</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- HOTEL & ACCOMMODATION GUIDE -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">5. Hotel & Accommodation Guide: Where to Stay in Varanasi</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 20px;">Choosing the right location for stay in Kashi dictates how smooth your pilgrimage will be. Below is a breakdown of top accommodation zones categorized by traveler preference:</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
          
          <div style="border-left: 4px solid #d97706; padding-left: 15px; background: #fffcf7; padding: 18px; border-radius: 8px;">
            <h4 style="color: #78350f; font-size: 1.2rem; margin-bottom: 8px;">Zone 1: Kashi Vishwanath Corridor & Dashashwamedh Ghat (Walkable to Temple)</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;"><strong>Best For:</strong> Senior citizens, early morning Mangla Aarti attendees, and devotees who prefer walking directly to temple gates without needing autos.<br><strong>Top Stays:</strong> BrijRama Palace (Heritage Luxury), Hotel Temple on Ganges, Hotel Alka, staying inside Chowk/Bansphatak guest houses.<br><strong>Pros:</strong> 2-minute walk to Ganga Aarti and Temple Gate 2.<br><strong>Cons:</strong> Vehicles cannot reach hotel entrance directly; luggage must be carried via rickshaw/porters for 200 meters.</p>
          </div>

          <div style="border-left: 4px solid #b45309; padding-left: 15px; background: #fffcf7; padding: 18px; border-radius: 8px;">
            <h4 style="color: #78350f; font-size: 1.2rem; margin-bottom: 8px;">Zone 2: Assi Ghat & BHU South Varanasi (Spiritual & Youth Vibe)</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;"><strong>Best For:</strong> Peaceful stays, Subah-e-Banaras morning yoga, boutique cafe culture, and family groups.<br><strong>Top Stays:</strong> Palace on Ganges, Treebo Trend, Hotel Ganges View, Zostel Varanasi.<br><strong>Pros:</strong> Open riverfront views, easy vehicle access up to hotel gates, peaceful evening vibe.<br><strong>Distance:</strong> 3.5 km from Kashi Vishwanath (15 mins by e-rickshaw).</p>
          </div>

          <div style="border-left: 4px solid #4a0404; padding-left: 15px; background: #fffcf7; padding: 18px; border-radius: 8px;">
            <h4 style="color: #4a0404; font-size: 1.2rem; margin-bottom: 8px;">Zone 3: Cantonment (Cantt) Luxury & Business Zone</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;"><strong>Best For:</strong> Luxury travelers, corporate delegations, and NRI families requiring 5-star amenities, swimming pools, and spacious parking.<br><strong>Top Stays:</strong> Taj Nadesar Palace, Radisson Blu Varanasi, Welcomhotel by ITC Hotels, Ramada Plaza.<br><strong>Pros:</strong> 5-star luxury, wide roads, quiet environment.<br><strong>Distance:</strong> 6 km from Kashi Vishwanath Temple (25 mins by cab).</p>
          </div>

          <div style="border-left: 4px solid #15803d; padding-left: 15px; background: #fffcf7; padding: 18px; border-radius: 8px;">
            <h4 style="color: #15803d; font-size: 1.2rem; margin-bottom: 8px;">Zone 4: Trust Dharamshalas & Ashrams (Budget & Pure Veg)</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;"><strong>Best For:</strong> Budget pilgrims, large yatra groups, and traditional devotees seeking pure vegetarian dining and satvik stay.<br><strong>Top Dharamshalas:</strong> Mumukshu Bhawan (Assi), Annapurna Kshetra Trust Guest House (Godowlia), Bharat Sevashram Sangh (Sigra), Marwari Seva Sangh.<br><strong>Rates:</strong> ₹500 – ₹1,500 per room night.</p>
          </div>

        </div>
      </div>

      <!-- EXPANDED PILGRIMAGE FAQS -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">6. Exhaustive Kashi Vishwanath Yatra FAQs (Topical Authority Q&A)</h3>
        
        <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
          
          <div style="border-bottom: 1px solid #f3f4f6; padding-bottom: 16px;">
            <h4 style="font-size: 1.15rem; color: #78350f; margin-bottom: 6px;">Q1: How much does a complete Kashi Dharshan tour package cost for 3 days?</h4>
            <p style="color: #4b5563; line-height: 1.7;">A complete 3-Day / 2-Night Kashi Dharshan tour package starts at ₹7,900 per person for budget categories and ₹12,500 - ₹18,500 per person for 3-star/4-star deluxe stays with private AC sedan cab, VIP Kashi Vishwanath darshan assistance, private Ganga Aarti boat ride, and Sarnath sightseeing included.</p>
          </div>

          <div style="border-bottom: 1px solid #f3f4f6; padding-bottom: 16px;">
            <h4 style="font-size: 1.15rem; color: #78350f; margin-bottom: 6px;">Q2: What is the procedure for Senior Citizens and Wheelchair assistance inside Kashi Corridor?</h4>
            <p style="color: #4b5563; line-height: 1.7;">Shri Kashi Vishwanath Dham is 100% barrier-free and senior citizen friendly. Battery-operated electric golf carts (E-carts) run continuously from Godowlia Gate to Ganga Ghat Gate. Wheelchairs with dedicated attendants are available free of cost at Gate 2 and Gate 4. Kashi Dharshan tour managers accompany senior citizen yatris directly through the Sugam Darshan fast queue.</p>
          </div>

          <div style="border-bottom: 1px solid #f3f4f6; padding-bottom: 16px;">
            <h4 style="font-size: 1.15rem; color: #78350f; margin-bottom: 6px;">Q3: Are mobile phones, cameras, and shoes allowed inside Shri Kashi Vishwanath Temple?</h4>
            <p style="color: #4b5563; line-height: 1.7;">No, electronic devices including mobile phones, digital cameras, smartwatches, metal keys, and leather belts are strictly banned inside the inner temple complex. Devotees can safely deposit footwear and valuables at the digital locker counters operating at Gate 2 (Saraswati Gate) and Gate 4 (Ganga Riverfront Corridor Gate).</p>
          </div>

          <div style="border-bottom: 1px solid #f3f4f6; padding-bottom: 16px;">
            <h4 style="font-size: 1.15rem; color: #78350f; margin-bottom: 6px;">Q4: What is the difference between General Darshan and Sugam (VIP) Darshan?</h4>
            <p style="color: #4b5563; line-height: 1.7;">General Darshan involves joining the public queue, which can take anywhere from 1.5 to 4 hours depending on crowd levels. Sugam Darshan is a ticketed priority pass (₹300 fee) that grants direct entry via an exclusive air-conditioned VIP hallway, allowing devotees to complete darshan in under 20 minutes.</p>
          </div>

          <div style="border-bottom: 1px solid #f3f4f6; padding-bottom: 16px;">
            <h4 style="font-size: 1.15rem; color: #78350f; margin-bottom: 6px;">Q5: What is the best month to visit Kashi (Varanasi)?</h4>
            <p style="color: #4b5563; line-height: 1.7;">The ideal time to visit Kashi is during the autumn and winter months from October to March when temperatures range between 12°C and 25°C. Visiting during November allows you to experience the world-famous Dev Deepawali festival, where all 84 ghats are illuminated with over 1 million earthen oil lamps (diyas).</p>
          </div>

          <div style="border-bottom: 1px solid #f3f4f6; padding-bottom: 16px;">
            <h4 style="font-size: 1.15rem; color: #78350f; margin-bottom: 6px;">Q6: How can I book a combined Varanasi, Ayodhya & Prayagraj tour package?</h4>
            <p style="color: #4b5563; line-height: 1.7;">Kashi Dharshan offers customized 5-Day and 6-Day Sacred Triangle tour packages covering Kashi Vishwanath, Triveni Sangam Prayagraj, and Shri Ram Janmabhoomi Ayodhya with dedicated private AC cabs, verified hotel stays, and priority VIP passes. Contact our local helpline at +91-7408763401 for instant custom itineraries.</p>
          </div>

        </div>
      </div>

    </div>
  </section>
"""

with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

if "<!-- MEGA KASHI PILGRIMAGE & VARANASI YATRA AUTHORITATIVE ENCYCLOPEDIA (TASK 2 EXPANSION) -->" not in idx_content:
    # Inject before footer
    if "<footer" in idx_content:
        idx_content = idx_content.replace("<footer", mega_kashi_guide + "\n<footer")
    else:
        idx_content += mega_kashi_guide

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("Injected Mega Kashi Encyclopedia section into index.html")
else:
    print("Mega Kashi Encyclopedia section already present in index.html")

# Verify new word count of index.html
with open("index.html", "r", encoding="utf-8") as f:
    final_content = f.read()

text_only = re.sub('<[^<]+?>', ' ', final_content)
word_count = len(text_only.split())
print(f"\nFinal index.html word count: {word_count} words")
