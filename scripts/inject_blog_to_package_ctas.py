import os
import re

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mapping blog files to their respective destination package pages, headings, and descriptions
blog_cta_map = {
    # VARANASI BLOGS
    "blog-varanasi-local-sightseeing-tour-package.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Ready to Book Your Varanasi (Kashi) Tour Package?",
        "desc": "Experience Kashi Vishwanath VIP Sugam Darshan, Dashashwamedh Ganga Aarti boat ride, Sarnath, and private AC cabs with handpicked corridor hotels.",
        "btn_text": "View Varanasi Tour Package & Pricing →"
    },
    "blog-kashi-vishwanath-corridor-tourist-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Book Guided Kashi Vishwanath Corridor Pilgrimage Package",
        "desc": "Get guaranteed VIP Sugam Darshan entry, near-gate 3-Star accommodation, Ganga boat ride, and 24x7 local yatra coordinator.",
        "btn_text": "Explore Kashi Vishwanath Tour Packages →"
    },
    "blog-kashi-vishwanath-sawan-vip-darshan-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Book Sawan Kashi Vishwanath VIP Darshan Package",
        "desc": "Avoid long Sawan queues with priority Sugam Darshan passes, private AC transport, and dedicated Pujari coordination.",
        "btn_text": "Book Sawan Kashi Yatra Package →"
    },
    "blog-kashi-vishwanath-vip-darshan-booking-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Ready to Book Your Kashi Vishwanath VIP Yatra?",
        "desc": "Includes priority Sugam Darshan pass assistance, private AC cab transfers, and 3-Star corridor hotel stay.",
        "btn_text": "Explore Kashi VIP Package Details →"
    },
    "blog-kashi-vishwanath-vip-pass-booking-online.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Book Kashi Vishwanath VIP Pass & Yatra Package",
        "desc": "Skip the queues with official Sugam Darshan assistance, private Ganga boat tour, and clean hotel stays.",
        "btn_text": "View Kashi Yatra Package Prices →"
    },
    "blog-varanasi-dev-deepawali-boat-booking-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Book Dev Deepawali 2026 Kashi Boat & Tour Package",
        "desc": "Reserve private boat / bajra for 84 ghat lighting, Ganga Aarti, and Kashi Vishwanath VIP darshan.",
        "btn_text": "Reserve Dev Deepawali Package →"
    },
    "blog-varanasi-dev-deepawali-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Experience Kashi Dev Deepawali 2026 with VIP Comfort",
        "desc": "Book early-bird packages covering boat ride for 84 ghat lighting, hotel stay, and temple VIP darshan.",
        "btn_text": "Explore Dev Deepawali Packages →"
    },
    "blog-varanasi-ganga-aarti-vip-boat-booking.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Book Private Ganga Aarti Boat & Varanasi Tour",
        "desc": "Enjoy reserved front-row Ganga Aarti boat seating, Kashi Vishwanath VIP darshan, and private AC cab.",
        "btn_text": "View Varanasi Tour Packages →"
    },
    "blog-varanasi-ganga-cruise-booking-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Book Luxury Ganga Cruise & Kashi Vishwanath Yatra",
        "desc": "Combine luxury Alaknanda / Ro-Ro Ganga cruise with Kashi Vishwanath VIP entry and AC transport.",
        "btn_text": "View Cruise & Yatra Packages →"
    },
    "blog-varanasi-kashi-vishwanath-vip-darshan-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Ready for Kashi Vishwanath VIP Darshan & Tour?",
        "desc": "Fully-managed yatra package with Sugam Darshan assistance, hotel stay near Godowlia, and AC cab.",
        "btn_text": "Explore Varanasi Tour Packages →"
    },
    "blog-varanasi-same-day-tour-package.html": {
        "pkg_url": "varanasi-same-day-tour-package.html",
        "title": "Book Full-Day Varanasi & Sarnath Sightseeing Cab",
        "desc": "Private AC sedan / SUV cab for Kashi Vishwanath, Sarnath, Kaal Bhairav, BHU, and Ganga Aarti.",
        "btn_text": "Book Same Day Varanasi Cab Package →"
    },

    # AYODHYA BLOGS
    "blog-ayodhya-dharshan-tour-package.html": {
        "pkg_url": "ayodhya-tour-package.html",
        "title": "Ready to Book Your Ayodhya Ram Mandir Tour Package?",
        "desc": "Book complete Ayodhya yatra with Shri Ram Janmabhoomi VIP passes, Hanuman Garhi, Saryu Aarti, and private AC cab.",
        "btn_text": "View Ayodhya Tour Package & Pricing →"
    },
    "blog-ayodhya-diwali-yatra-guide.html": {
        "pkg_url": "ayodhya-tour-package.html",
        "title": "Experience Ayodhya Deepotsav 2026 with VIP Comfort",
        "desc": "Book Deepotsav yatra packages with Ram Mandir VIP passes, 25-lakh diya lighting view, and hotel stay.",
        "btn_text": "Explore Ayodhya Diwali Packages →"
    },
    "blog-ayodhya-food-guide-sattvic-cuisine.html": {
        "pkg_url": "ayodhya-tour-package.html",
        "title": "Plan Your Spiritual Ayodhya Ram Mandir Yatra",
        "desc": "Includes pure veg Sattvic meals, Ram Mandir VIP pass assistance, 3-Star hotel stay, and private AC cab.",
        "btn_text": "Explore Ayodhya Packages →"
    },
    "blog-ayodhya-same-day-tour-itinerary.html": {
        "pkg_url": "ayodhya-same-day-tour.html",
        "title": "Book 1-Day Ayodhya Ram Mandir Sightseeing Cab",
        "desc": "Private AC cab pickup for Ram Janmabhoomi, Hanuman Garhi, Kanak Bhawan, and evening Saryu Aarti.",
        "btn_text": "Book Ayodhya Same Day Tour →"
    },
    "blog-best-time-to-visit-ayodhya.html": {
        "pkg_url": "ayodhya-tour-package.html",
        "title": "Ready to Book Your Ayodhya Pilgrimage Yatra?",
        "desc": "Book hassle-free family yatra with Ram Mandir Sugam Darshan passes, private AC transport, and hotel stays.",
        "btn_text": "View Ayodhya Tour Packages →"
    },
    "blog-ram-mandir-vip-pass-booking-guide.html": {
        "pkg_url": "ayodhya-tour-package.html",
        "title": "Book Ayodhya Ram Mandir VIP Darshan Package",
        "desc": "Priority entry pass assistance for Shri Ram Janmabhoomi, Hanuman Garhi, Saryu Aarti, and AC cab pickup.",
        "btn_text": "Explore Ram Mandir Packages →"
    },
    "blog-vip-darshan-ayodhya-ram-mandir.html": {
        "pkg_url": "ayodhya-tour-package.html",
        "title": "Ready for Ayodhya Ram Lalla VIP Darshan?",
        "desc": "Get guaranteed Sugam Darshan passes, hotel near Ram Path, private AC cab, and dedicated local guide.",
        "btn_text": "View Ayodhya Package Details →"
    },

    # MULTI-CITY / INTER-CITY BLOGS
    "blog-ayodhya-kashi-vip-darshan-complete-guide.html": {
        "pkg_url": "ayodhya-prayagraj-varanasi-tour-package.html",
        "title": "Book Complete Ayodhya + Kashi VIP Darshan Circuit",
        "desc": "Cover Ram Mandir VIP entry, Kashi Vishwanath Sugam Darshan, Triveni Sangam, and private AC cab transport.",
        "btn_text": "Explore 5-Day Sacred Circuit Package →"
    },
    "blog-ayodhya-prayagraj-tour-package.html": {
        "pkg_url": "ayodhya-prayagraj-tour-package.html",
        "title": "Book Ayodhya + Prayagraj 3-Day Yatra Package",
        "desc": "Includes Ram Mandir VIP passes, Triveni Sangam holy dip boat, Bade Hanuman Mandir, and private AC cab.",
        "btn_text": "View Ayodhya Prayagraj Package →"
    },
    "blog-ayodhya-prayagraj-varanasi-tour-package.html": {
        "pkg_url": "ayodhya-prayagraj-varanasi-tour-package.html",
        "title": "Book Complete Ayodhya + Prayagraj + Varanasi Yatra",
        "desc": "5-Day all-inclusive pilgrimage with temple VIP passes, hotel stays, private AC cabs, and Ganga boat rides.",
        "btn_text": "View 5-Day Yatra Package & Prices →"
    },
    "blog-ayodhya-to-prayagraj-distance-travel-guide.html": {
        "pkg_url": "ayodhya-prayagraj-tour-package.html",
        "title": "Book Highway Cab & Ayodhya-Prayagraj Tour",
        "desc": "Direct door-to-door AC cab transfers between Ayodhya Ram Mandir and Prayagraj Triveni Sangam.",
        "btn_text": "View Ayodhya Prayagraj Packages →"
    },
    "blog-ayodhya-to-varanasi-distance-travel-guide.html": {
        "pkg_url": "ayodhya-varanasi-tour-package.html",
        "title": "Book Ayodhya to Varanasi Highway Yatra Package",
        "desc": "Seamless transfers, Ram Mandir VIP passes, Kashi Vishwanath Sugam Darshan, and Ganga Aarti boat ride.",
        "btn_text": "View Ayodhya Varanasi Packages →"
    },
    "blog-ayodhya-to-varanasi-taxi-fare-cab-booking.html": {
        "pkg_url": "ayodhya-varanasi-tour-package.html",
        "title": "Book Ayodhya to Varanasi Private AC Cab & Yatra",
        "desc": "Comfortable AC sedan / SUV cab booking with experienced driver, hotel pickup, and temple darshan support.",
        "btn_text": "Explore Ayodhya Varanasi Tour →"
    },
    "blog-ayodhya-to-varanasi-vande-bharat-train-guide.html": {
        "pkg_url": "ayodhya-varanasi-tour-package.html",
        "title": "Book Ayodhya + Kashi Vande Bharat Express Yatra",
        "desc": "Combine Vande Bharat train travel with station pickup, 3-Star hotel stays, and VIP temple darshan passes.",
        "btn_text": "View Tour Package Details →"
    },
    "blog-ayodhya-varanasi-ganga-aarti-guide.html": {
        "pkg_url": "ayodhya-varanasi-tour-package.html",
        "title": "Experience Saryu & Ganga Aarti with VIP Seating",
        "desc": "Book guided Ayodhya & Varanasi tour package with reserved Aarti boat seating and temple VIP passes.",
        "btn_text": "View Ayodhya Varanasi Packages →"
    },
    "blog-ayodhya-varanasi-tour-package.html": {
        "pkg_url": "ayodhya-varanasi-tour-package.html",
        "title": "Ready to Book Ayodhya + Varanasi Tour Package?",
        "desc": "All-inclusive 4-Day yatra with Ram Mandir VIP passes, Kashi Vishwanath Sugam Darshan, and private AC cabs.",
        "btn_text": "View Ayodhya Varanasi Package Prices →"
    },
    "blog-ayodhya-tour-cost-budget-planner.html": {
        "pkg_url": "ayodhya-tour-package.html",
        "title": "Calculate & Book Your Ayodhya Yatra Package",
        "desc": "Get transparent all-inclusive package pricing with hotel stay, private AC cabs, and VIP darshan passes.",
        "btn_text": "Explore Ayodhya Tour Packages →"
    },
    "blog-ayodhya-tour-package-from-delhi-cost.html": {
        "pkg_url": "delhi-to-ayodhya-tour-package.html",
        "title": "Book Delhi to Ayodhya All-Inclusive Tour Package",
        "desc": "Includes flight / train tickets, Lucknow airport pickup, Ram Mandir VIP passes, and 3-Star hotel stay.",
        "btn_text": "View Delhi to Ayodhya Package →"
    },

    # OTHER REGIONAL & CITY BLOGS
    "blog-prayagraj-sangam-tour-guide.html": {
        "pkg_url": "prayagraj-tour-package.html",
        "title": "Ready to Book Your Prayagraj Triveni Sangam Yatra?",
        "desc": "Includes holy snan boat trip, Bade Hanuman Mandir, Akshayavat, private AC cab, and local guide.",
        "btn_text": "View Prayagraj Tour Package & Pricing →"
    },
    "blog-chitrakoot-ram-vanvas-tour-guide.html": {
        "pkg_url": "chitrakoot-tour-package.html",
        "title": "Book Guided Chitrakoot Ram Vanvas Dham Yatra",
        "desc": "Explore Kamadgiri Parikrama, Ram Ghat Aarti, Sphatik Shila, and Gupt Godavari with private AC cab.",
        "btn_text": "View Chitrakoot Package Details →"
    },
    "blog-naimisharanya-chakra-tirth-guide.html": {
        "pkg_url": "naimisharanya-tour-package.html",
        "title": "Book Naimisharanya Chakra Tirth Yatra Package",
        "desc": "Chakra Tirth bath, Maa Lalita Devi temple, Vyas Gaddi, and Hanuman Garhi with private AC cab pickup.",
        "btn_text": "View Naimisharanya Package Prices →"
    },
    "blog-vindhyachal-trikon-parikrama-guide.html": {
        "pkg_url": "vindhyachal-tour-package.html",
        "title": "Book Maa Vindhyavasini Devi Trikon Parikrama Yatra",
        "desc": "Cover Vindhyavasini Temple, Kali Khoh, and Ashtabhuja Temple with VIP entry and AC cab transport.",
        "btn_text": "View Vindhyachal Package Details →"
    },
    "blog-mathura-vrindavan-vip-darshan-guide.html": {
        "pkg_url": "mathura-vrindavan-tour-package.html",
        "title": "Ready to Book Mathura Vrindavan Tour Package?",
        "desc": "Shri Krishna Janmabhoomi, Bankey Bihari VIP pass, Prem Mandir light show, and private AC transport.",
        "btn_text": "View Mathura Vrindavan Package Prices →"
    },
    "blog-varanasi-to-gaya-pind-daan-tour-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Book Kashi Prayag Gaya Pind Daan Tour Package",
        "desc": "Certified Pujari coordination, Vishnupad Temple Gaya VIP entry, Kashi Vishwanath darshan, and AC cab.",
        "btn_text": "View Pind Daan Package Details →"
    },
    "blog-sawan-yatra-vip-darshan-guide.html": {
        "pkg_url": "varanasi-tour-package.html",
        "title": "Book Sawan Kashi Vishwanath VIP Yatra Package",
        "desc": "Skip the Sawan rush with priority Sugam Darshan passes, private AC cab, and near-corridor hotel stay.",
        "btn_text": "Explore Sawan Yatra Packages →"
    },
    "blog-lucknow-to-ayodhya-travel-guide-taxi.html": {
        "pkg_url": "lucknow-to-ayodhya-same-day-tour-package.html",
        "title": "Book Lucknow to Ayodhya Same Day Taxi & Tour",
        "desc": "Direct pickup from Lucknow Airport (LKO) / Charbagh station for Ram Mandir VIP darshan and Saryu Aarti.",
        "btn_text": "Book Lucknow to Ayodhya Cab Package →"
    }
}

count_updated = 0

for blog_file, data in blog_cta_map.items():
    file_path = os.path.join(root_dir, blog_file)
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate CTA block HTML
    cta_block = f"""
  <!-- HIGH-CONVERTING CITY PACKAGE CTA BANNER -->
  <div class="blog-city-package-cta" style="background: linear-gradient(135deg, #701616 0%, #3d0808 100%); border: 2px solid #d4af37; border-radius: 18px; padding: 38px 24px; margin: 40px 0; text-align: center; box-shadow: 0 12px 35px rgba(61, 8, 8, 0.4);">
    <div style="font-size: 2.2rem; margin-bottom: 6px;">🛕✨</div>
    <h3 style="color: #ffffff; font-family: 'Marcellus', 'Cormorant Garamond', serif; font-size: clamp(1.4rem, 2.5vw, 1.9rem); margin: 0 0 10px 0; line-height: 1.3;">
      {data['title']}
    </h3>
    <p style="color: #fcefd9; font-size: 1.02rem; line-height: 1.6; max-width: 680px; margin: 0 auto 24px; font-weight: 400;">
      {data['desc']}
    </p>
    <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
      <a href="{data['pkg_url']}" class="btn" style="background: linear-gradient(180deg, #d99a26 0%, #b87c14 100%); color: #1a0808; font-weight: 800; font-size: 1.05rem; padding: 14px 32px; border-radius: 30px; text-decoration: none; box-shadow: 0 6px 20px rgba(216, 160, 39, 0.4); display: inline-flex; align-items: center; gap: 8px;">
        <span>{data['btn_text']}</span>
      </a>
      <a href="https://wa.me/917011960307?text=Har%20Har%20Mahadev!%20I%20read%20the%20travel%20guide%20and%20want%20to%20enquire%20about%20tour%20packages." target="_blank" rel="noopener" class="btn" style="background: #25D366; color: #ffffff; font-weight: 700; font-size: 1rem; padding: 14px 26px; border-radius: 30px; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">
        <span>Instant WhatsApp Chat</span>
      </a>
    </div>
  </div>
"""

    # If already has blog-city-package-cta, replace it. Otherwise insert before <h2>Frequently Asked Questions or </main>
    if 'class="blog-city-package-cta"' in content:
        content = re.sub(r'<!-- HIGH-CONVERTING CITY PACKAGE CTA BANNER -->.*?</div>\s*</div>', cta_block.strip(), content, flags=re.DOTALL)
        content = re.sub(r'<div class="blog-city-package-cta".*?</div>\s*</div>', cta_block.strip(), content, flags=re.DOTALL)
    elif '<!-- Secondary CTA -->' in content:
        # Replace the old Secondary CTA block
        content = re.sub(r'<!-- Secondary CTA -->.*?</div>\s*</div>', cta_block.strip(), content, flags=re.DOTALL)
        content = re.sub(r'<div style="background:#0a2647; color:#fff; padding:30px; border-radius:10px; margin:40px 0; text-align:center;">.*?</div>', cta_block.strip(), content, flags=re.DOTALL)
    elif '<h2>Frequently Asked Questions' in content:
        content = content.replace('<h2>Frequently Asked Questions', cta_block + '\n  <h2>Frequently Asked Questions')
    elif '</main>' in content:
        content = content.replace('</main>', cta_block + '\n</main>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    count_updated += 1
    print(f"✅ Injected/Updated Package CTA in {blog_file} -> {data['pkg_url']}")

print(f"\n🎉 Successfully updated package CTAs across {count_updated} blog guide pages!")
