import re
import os

BASE_DIR = '/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan'

# 1. FIX AYODHYA-TOUR-PACKAGE.HTML
ayodhya_path = os.path.join(BASE_DIR, 'ayodhya-tour-package.html')
with open(ayodhya_path, 'r', encoding='utf-8') as f:
    ayodhya_content = f.read()

# Replace Breadcrumb
ayodhya_content = re.sub(
    r'<p class="crumb"><a href="/">Home</a> &nbsp;/&nbsp; <a href="services">Services</a> &nbsp;/&nbsp; Varanasi to Ayodhya Tour</p>',
    '<p class="crumb"><a href="/">Home</a> &nbsp;/&nbsp; <a href="services">Services</a> &nbsp;/&nbsp; Ayodhya Tour Package</p>',
    ayodhya_content
)

# Replace H1
ayodhya_content = re.sub(
    r'<h1 class="display hero-title-2line"><span class="hero-line-1">Varanasi to Ayodhya Tour Package: </span>\s*<span class="hero-line-2">Same Day Ram Mandir VIP Darshan by AC Cab</span></h1>',
    '<h1 class="display hero-title-2line"><span class="hero-line-1">Ayodhya Tour Package 2026: </span> <span class="hero-line-2">Ram Mandir VIP Darshan, Hotels &amp; Sightseeing Guide</span></h1>',
    ayodhya_content
)

# Replace Lead
old_lead = r'<p class="lead">Depart from your Varanasi hotel or railway station in a private sanitized AC cab via the high-speed Purvanchal Expressway. Experience hassle-free Ram Mandir Sugam Darshan VIP entry, visit Hanuman Garhi & Kanak Bhawan, attend the sunset Saryu River Aarti, and return back to Kashi the same evening.</p>'
new_lead = '<p class="lead">Book the official all-inclusive <strong>Ayodhya Tour Package 2026</strong> from ₹2,999. Experience priority Shri Ram Janmabhoomi VIP Sugam Darshan passes, visit Hanuman Garhi, Kanak Bhawan, Dashrath Mahal, and attend the divine sunset Saryu River Aarti. Options for Same Day Ayodhya Tour (from ₹2,900/cab), 2-Day Divine Yatra (from ₹5,500/person with 3★ hotel), and 3-Day Complete Ramayana Circuit. Doorstep pickup from Ayodhya Airport, Railway Station, Lucknow, or Varanasi.</p>'
ayodhya_content = ayodhya_content.replace(old_lead, new_lead)

# Replace Itinerary Title and Content
old_itin_heading = '<h2 style="color:var(--maroon); margin-bottom: 20px;">Varanasi to Ayodhya Same-Day Itinerary</h2>'
new_itin_heading = '<h2 style="color:var(--maroon); margin-bottom: 20px;">Complete Ayodhya Tour Package Itineraries (1-Day, 2-Day &amp; 3-Day Yatra)</h2>'
ayodhya_content = ayodhya_content.replace(old_itin_heading, new_itin_heading)

# Replace Itinerary Timeline
old_timeline_pattern = r'<div class="timeline">.*?</div>\s*</div>\s*<!-- Right column'
new_timeline = """<div class="timeline">
          <div class="timeline-item reveal">
            <div class="timeline-time">Option A: 1-Day Same Day Ayodhya Darshan (From ₹2,900 / Cab)</div>
            <h3>Express Ram Janmabhoomi VIP Darshan &amp; Saryu Aarti</h3>
            <p>• Morning doorstep pickup from Ayodhya Airport, Ayodhya Dham Railway Station, Lucknow, or Varanasi.<br>
            • Dedicated local pandit guide escorts you to Hanuman Garhi for traditional blessings first.<br>
            • Priority fast-track entry to Shri Ram Janmabhoomi Mandir for divine darshan of Ram Lalla.<br>
            • Visit Kanak Bhawan, Dashrath Mahal, and Sita Ki Rasoi.<br>
            • Evening grand Saryu River Aarti at Ram Ki Paidi amidst floating diyas, followed by return drop.</p>
          </div>
          <div class="timeline-item reveal">
            <div class="timeline-time">Option B: 2-Day / 1-Night Divine Ayodhya Stay (From ₹5,500 / Person)</div>
            <h3>Complete Ayodhya Pilgrimage with 3★ Hotel &amp; Aarti</h3>
            <p>• <strong>Day 1:</strong> Pickup, check-in at verified 3-star hotel on Ram Path. Visit Hanuman Garhi, Ram Mandir VIP Darshan, sunset boat ride on holy River Saryu &amp; evening Aarti.<br>
            • <strong>Day 2:</strong> Attend early morning Mangla Aarti, visit Guptar Ghat (where Lord Ram took Jal Samadhi), Surya Kund, Bharat Kund, and local shopping for Ayodhya peda &amp; souvenirs before departure.</p>
          </div>
          <div class="timeline-item reveal">
            <div class="timeline-time">Option C: 3-Day / 2-Night Ayodhya &amp; Sacred Circuit (From ₹8,900 / Person)</div>
            <h3>Extended Yatra: Ayodhya, Chhapaiya &amp; Naimisharanya</h3>
            <p>• Complete 3-day spiritual circuit covering all Ayodhya sacred sites, plus excursion to Chhapaiya (birthplace of Bhagwan Swaminarayan) or holy Naimisharanya Chakra Tirth, with sanitized AC vehicle throughout.</p>
          </div>
        </div>
      </div>

      <!-- Right column"""
ayodhya_content = re.sub(old_timeline_pattern, new_timeline, ayodhya_content, flags=re.DOTALL)

# Replace Schema ItemList and FAQPage
old_itemlist_pattern = r'\{\s*"@type":\s*"ItemList",\s*"name":\s*"Kashi Yatra Tour Packages".*?\}\s*\}\s*\]\s*\}'
new_itemlist = """{
      "@type": "ItemList",
      "name": "Ayodhya Tour Packages 2026",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "item": { "@type": "TouristTrip", "name": "1-Day Ayodhya Same Day Tour Package", "description": "Express same-day tour covering Ram Mandir VIP Darshan, Hanuman Garhi, Kanak Bhawan, and Saryu Aarti.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "2900", "priceCurrency": "INR" } } },
        { "@type": "ListItem", "position": 2, "item": { "@type": "TouristTrip", "name": "2-Day 1-Night Divine Ayodhya Stay Package", "description": "2 days / 1 night Ayodhya pilgrimage covering Ram Janmabhoomi, 3-star hotel stay, Saryu boat ride, Guptar Ghat and Surya Kund.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "5500", "priceCurrency": "INR" } } },
        { "@type": "ListItem", "position": 3, "item": { "@type": "TouristTrip", "name": "3-Day 2-Night Ayodhya & Sacred Circuit Yatra", "description": "3 days all-inclusive yatra covering Ayodhya Dham, Chhapaiya, and Naimisharanya with dedicated AC cab and guide.", "touristType": "Pilgrimage", "offers": { "@type": "Offer", "price": "8900", "priceCurrency": "INR" } } }
      ]
    }"""
ayodhya_content = re.sub(r'\{\s*"@type":\s*"ItemList",\s*"name":\s*"Kashi Yatra Tour Packages".*?\}\s*\]\s*\}', new_itemlist, ayodhya_content, flags=re.DOTALL)

# Replace FAQPage in Schema
new_faq_schema = """{
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How to book Ram Mandir VIP Sugam Darshan pass in Ayodhya?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ram Mandir Sugam Darshan passes can be arranged through the official trust portal or via our registered Ayodhya yatra coordinator. Our packages include priority darshan assistance with direct entry, allowing devotees to complete darshan comfortably within 20 to 30 minutes without waiting in 3-hour general queues."
          }
        },
        {
          "@type": "Question",
          "name": "What is the cost of an Ayodhya tour package in 2026?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ayodhya tour packages start at ₹2,900 per vehicle for a Same-Day private AC cab tour (covering Ram Mandir, Hanuman Garhi, and Saryu Aarti). A 2-Day/1-Night package with 3-star hotel stay, breakfast, and VIP darshan escort starts at ₹5,500 per person."
          }
        },
        {
          "@type": "Question",
          "name": "How to reach Ayodhya by flight or train?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Ayodhya is directly connected by air via Maharishi Valmiki International Airport (AYJ) with non-stop flights from Delhi, Mumbai, Bengaluru, Ahmedabad, and Kolkata. By rail, Ayodhya Dham Junction (AY) and Ayodhya Cantt (AYC) receive trains from all major Indian cities. Lucknow Airport (135 km) is also just 2.5 hours away via Purvanchal Expressway."
          }
        },
        {
          "@type": "Question",
          "name": "Which temples are included in the Ayodhya tour package?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our Ayodhya tour packages cover Shri Ram Janmabhoomi Mandir, Hanuman Garhi Mandir, Kanak Bhawan, Dashrath Mahal, Saryu River Ghats (Ram Ki Paidi), Guptar Ghat, Surya Kund, and Bharat Kund."
          }
        },
        {
          "@type": "Question",
          "name": "Is wheelchair or battery-cart assistance available for senior citizens in Ayodhya?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, we provide dedicated wheelchair escorts and electric golf-cart assistance along Ram Path and temple security corridors for elderly parents and differently-abled pilgrims."
          }
        }
      ]
    }"""
ayodhya_content = re.sub(r'\{\s*"@type":\s*"FAQPage".*?\}\s*\]\s*\}', new_faq_schema, ayodhya_content, flags=re.DOTALL)

# Replace on-page FAQ HTML
old_faq_html_pattern = r'<h2>FAQ — Ayodhya Dharshan Yatra</h2>.*?</div>\s*</section>'
new_faq_html = """<h2>Frequently Asked Questions — Ayodhya Tour Package 2026</h2>
    </div>
    <details class="faq" open><summary>How to book Ram Mandir VIP Sugam Darshan pass in Ayodhya?<span class="pm">+</span></summary>
      <div class="ans">Ram Mandir Sugam Darshan passes can be arranged through the official trust portal or via our registered Ayodhya yatra coordinator. Our packages include priority darshan assistance with direct entry, allowing devotees to complete darshan comfortably within 20 to 30 minutes without waiting in 3-hour general queues.</div></details>
    <details class="faq"><summary>What is the cost of an Ayodhya tour package in 2026?<span class="pm">+</span></summary>
      <div class="ans">Ayodhya tour packages start at ₹2,900 per vehicle for a Same-Day private AC cab tour (covering Ram Mandir, Hanuman Garhi, and Saryu Aarti). A 2-Day/1-Night package with 3-star hotel stay, breakfast, and VIP darshan escort starts at ₹5,500 per person.</div></details>
    <details class="faq"><summary>How to reach Ayodhya by flight or train?<span class="pm">+</span></summary>
      <div class="ans">Ayodhya is directly connected by air via Maharishi Valmiki International Airport (AYJ) with non-stop flights from Delhi, Mumbai, Bengaluru, Ahmedabad, and Kolkata. By rail, Ayodhya Dham Junction (AY) and Ayodhya Cantt (AYC) receive trains from all major Indian cities. We provide doorstep cab pickup from all airports and stations.</div></details>
    <details class="faq"><summary>Which sacred temples are included in the Ayodhya tour package?<span class="pm">+</span></summary>
      <div class="ans">Our Ayodhya tour packages cover Shri Ram Janmabhoomi Mandir, Hanuman Garhi Mandir, Kanak Bhawan, Dashrath Mahal, Saryu River Ghats (Ram Ki Paidi), Guptar Ghat, Surya Kund, and Bharat Kund.</div></details>
    <details class="faq"><summary>Is wheelchair or golf-cart assistance available for senior citizens in Ayodhya?<span class="pm">+</span></summary>
      <div class="ans">Yes, we provide dedicated wheelchair escorts and electric golf-cart assistance along Ram Path and temple security corridors for elderly parents and differently-abled pilgrims.</div></details>
  </div>
</section>"""
ayodhya_content = re.sub(old_faq_html_pattern, new_faq_html, ayodhya_content, flags=re.DOTALL)

with open(ayodhya_path, 'w', encoding='utf-8') as f:
    f.write(ayodhya_content)
print("✅ Rebuilt ayodhya-tour-package.html with 100% matched Ayodhya H1, Itineraries, Schema & FAQs!")

# 2. FIX BREADCRUMBS & SCHEMA IN OTHER MONEY PAGES
page_fixes = [
    ('chitrakoot-tour-package.html', 'Chitrakoot Tour Package', 'Chitrakoot Tour Package 2026'),
    ('mathura-tour-package.html', 'Mathura Tour Package', 'Mathura Tour Package 2026'),
    ('vrindavan-tour-package.html', 'Vrindavan Tour Package', 'Vrindavan Tour Package 2026'),
    ('naimisharanya-tour-package.html', 'Naimisharanya Tour Package', 'Naimisharanya Tour Package 2026'),
    ('prayagraj-tour-package.html', 'Prayagraj Tour Package', 'Prayagraj Tour Package 2026'),
    ('vindhyachal-tour-package.html', 'Vindhyachal Tour Package', 'Vindhyachal Tour Package 2026'),
    ('ayodhya-dharshan-tour-package.html', 'Ayodhya Tour Package', 'Ayodhya 3-Day Tour Package 2026')
]

for filename, breadcrumb_name, schema_trip_name in page_fixes:
    p_path = os.path.join(BASE_DIR, filename)
    with open(p_path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace breadcrumb
    c = re.sub(
        r'<p class="crumb"><a href="/">Home</a> &nbsp;/&nbsp; <a href="services">Services</a> &nbsp;/&nbsp; Ayodhya Dharshan Tour</p>',
        f'<p class="crumb"><a href="/">Home</a> &nbsp;/&nbsp; <a href="services">Services</a> &nbsp;/&nbsp; {breadcrumb_name}</p>',
        c
    )
    # Replace schema trip name
    c = c.replace('"name": "Ayodhya Dharshan Package"', f'"name": "{schema_trip_name}"')

    # Replace lingering Ayodhya Dharshan brand
    c = c.replace('Ayodhya Dharshan', 'Kashi Dharshan Travels')

    with open(p_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"✅ Fixed breadcrumb & schema in {filename}")

