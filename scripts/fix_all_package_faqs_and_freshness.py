import os
import re

ROOT_DIR = '/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan'

# Target FAQ blocks for each package
FAQ_DATA = {
    'kashi-vishwanath-tour-package.html': {
        'title': 'FAQ — Kashi Vishwanath VIP Darshan & Varanasi Tour',
        'faqs': [
            ("How to book Kashi Vishwanath VIP Sugam Darshan pass?",
             "Official Sugam Darshan passes (₹300) can be booked online via the temple trust portal or directly through our all-inclusive Kashi Dharshan packages. Our local guides escort senior citizens and families through Gate 4 or Gate 2 for fast-track entry in 15–20 minutes without queue hassle."),
            ("What is included in the Varanasi & Kashi Vishwanath tour package?",
             "Our packages include verified 3-star/4-star hotel accommodation near Vishwanath Corridor or Dashashwamedh Ghat, private sanitized AC cab transfers (Sedan/Ertiga/Innova), dedicated local pandit guide, VIP Sugam Darshan assistance, and private evening Ganga Aarti boat ride."),
            ("Can we attend Mangla Aarti and perform Sparsh Darshan?",
             "Yes, we provide full advance booking assistance for the sacred 03:00 AM Mangla Aarti and daytime Sparsh Darshan slots. Yatris must follow the traditional dress code (dhoti-kurta for men, saree for women)."),
            ("What are the boat rental rates for Dashashwamedh Ghat Ganga Aarti?",
             "A private wooden rowboat costs approximately ₹1,500–₹2,000, motorboats range from ₹3,000–₹4,000, and VIP double-decker Bajras cost ₹8,000–₹12,000 for family groups. All boat arrangements are pre-reserved with verified boatmen."),
            ("How many days are recommended for a complete Varanasi yatra?",
             "A 3-day / 2-night trip is ideal to comfortably experience Kashi Vishwanath Dham, Kaal Bhairav, Annapurna Mandir, Sankat Mochan, BHU New Vishwanath, Subah-e-Banaras sunrise boat ride, and Sarnath Buddhist circuit.")
        ]
    },
    'varanasi-tour-package.html': {
        'title': 'FAQ — Varanasi Tour Package & Kashi Vishwanath Darshan',
        'faqs': [
            ("How to book VIP Darshan or Sugam Darshan at Kashi Vishwanath Temple?",
             "Official Sugam Darshan passes (₹300) can be booked online via the official portal or through our packages. Our local guide assists families and senior citizens through priority corridor gates with zero waiting time."),
            ("How much does a Varanasi & Kashi Dharshan tour package cost?",
             "Packages start from ₹7,900 per person for a 3-day / 2-night yatra, which includes verified hotel accommodation, private AC vehicle, VIP darshan passes, local guide, and private Ganga Aarti boat ride."),
            ("What is the dress code for Kashi Vishwanath Temple and Sparsh Darshan?",
             "For regular Sugam Darshan, clean modest traditional attire is recommended. For Garbhagriha Sparsh Darshan and Mangla Aarti, men must wear a traditional unstitched Dhoti-Kurta, and women must wear a Saree."),
            ("Can you arrange private Ganga Aarti boat rides and Sarnath sightseeing?",
             "Yes, every Varanasi tour package includes a reserved private boat for the world-famous Dashashwamedh Ghat Ganga Aarti, as well as a full day excursion to Sarnath (Dhamek Stupa, Ashoka Pillar, and Archaeological Museum)."),
            ("How far is Ayodhya from Varanasi, and can we combine both in one trip?",
             "Varanasi is approximately 220 km from Ayodhya (about 4 hours by road or Vande Bharat Express). We arrange customized 4-Day and 5-Day Sacred Twin City packages covering both holy shrines seamlessly.")
        ]
    },
    'prayagraj-tour-package.html': {
        'title': 'FAQ — Prayagraj Triveni Sangam & Kumbh Yatra',
        'faqs': [
            ("How to book a private boat for Triveni Sangam holy bath (snan)?",
             "Private motorboats and traditional rowboats for Triveni Sangam snan are pre-arranged with registered boatmen in our Prayagraj packages. Boats depart from Qila Ghat or VIP Ghat, taking you to the exact holy confluence of Ganga, Yamuna, and Saraswati with life jackets and changing facilities."),
            ("What sacred places are covered in the Prayagraj tour?",
             "The package covers Triveni Sangam Snan, the miraculous Bade Hanuman Ji (Lete Hanuman Temple), Alopi Devi Shaktipeeth, Anand Bhawan, Allahabad Fort outer viewpoint, Akshayavat (immortal banyan tree), and Patalpuri Temple."),
            ("Can we combine Prayagraj with Varanasi and Ayodhya?",
             "Yes! Our most popular pilgrimage circuit is the Sacred Triangle (5-Day / 4-Night or 6-Day / 5-Night) covering Kashi Vishwanath, Triveni Sangam Prayagraj, and Ram Mandir Ayodhya with continuous private AC cab transfers."),
            ("How far is Prayagraj from Varanasi, and what is the best travel mode?",
             "Prayagraj is approximately 120 km from Varanasi (about 2.5 hours via the smooth 6-lane NH-19 highway). We provide seamless private AC cab pickups from Varanasi hotels, airport, or railway station.")
        ]
    },
    'chitrakoot-tour-package.html': {
        'title': 'FAQ — Chitrakoot Ram Vanvas Pilgrimage Tour',
        'faqs': [
            ("What are the key sacred attractions covered in Chitrakoot?",
             "Our Chitrakoot tour package covers Ramghat on Mandakini River, Kamadgiri 5-km holy Parikrama, Bharat Milap Temple, Hanuman Dhara, Gupt Godavari caves, Sati Anusuya Ashram, and Sphatik Shila where Lord Ram and Maa Sita spent over 11 years of their exile."),
            ("How far is Chitrakoot from Prayagraj and Ayodhya?",
             "Chitrakoot is 135 km from Prayagraj (3.5 hours drive) and 260 km from Ayodhya (6 hours drive). We arrange dedicated private AC cab pickups from Prayagraj, Varanasi, or Lucknow."),
            ("Can senior citizens comfortably complete the Kamadgiri Parikrama?",
             "Yes, the 5-km Kamadgiri parikrama path is fully paved with shaded pathways. Battery-operated e-rickshaws and palanquins (doli) are readily available for elderly pilgrims.")
        ]
    },
    'vindhyachal-tour-package.html': {
        'title': 'FAQ — Vindhyachal Dham & Trikon Parikrama Yatra',
        'faqs': [
            ("What is the Trikon Parikrama of Vindhyachal?",
             "The sacred Trikon Parikrama connects the three divine Shakti forms: Maa Vindhyavasini (Lakshmi), Maa Ashtabhuja (Saraswati), and Maa Kali Khoh (Kali). Completing this triangular yatra is believed to fulfill all spiritual and worldly wishes."),
            ("Is the Vindhyachal ropeway operational for elderly devotees?",
             "Yes, a modern passenger ropeway is operational at both Ashtabhuja Hill and Kali Khoh, allowing yatris to reach the hilltop temples in under 5 minutes without climbing stairs."),
            ("How far is Vindhyachal from Varanasi?",
             "Vindhyachal is located just 65 km from Varanasi (about 1.5 to 2 hours drive via Mirzapur road). It can easily be completed as a same-day excursion from Varanasi or combined with Prayagraj.")
        ]
    },
    'naimisharanya-tour-package.html': {
        'title': 'FAQ — Naimisharanya Teerth Yatra',
        'faqs': [
            ("What is the spiritual significance of Naimisharanya?",
             "Naimisharanya (Neemsar) is the sacred Tapobhumi where Maharishi Ved Vyas composed the 18 Puranas and 88,000 sages performed grand yagnas. Taking a holy dip in the circular Chakra Tirth washes away all sins."),
            ("Which temples are included in the Naimisharanya package?",
             "The tour covers Chakra Tirth, Maa Lalita Devi Shaktipeeth, Vyas Gaddi, Soot Gaddi, Hanuman Garhi (Dakshinamukhi Hanuman), Pandav Kila, and Dadhichi Kund."),
            ("How can we reach Naimisharanya from Lucknow?",
             "Naimisharanya is 90 km from Lucknow (approximately 2 hours by private AC cab via Sitapur road). We provide direct hotel or airport pickup from Lucknow.")
        ]
    },
    'mathura-tour-package.html': {
        'title': 'FAQ — Mathura Krishna Janmabhoomi Tour Package',
        'faqs': [
            ("Which major temples are covered in Mathura and Vrindavan?",
             "The package covers Shri Krishna Janmabhoomi, Dwarkadhish Temple, Vishram Ghat on Yamuna in Mathura; and Banke Bihari Temple, Prem Mandir (light show), ISKCON, Radha Raman, and Nidhivan in Vrindavan."),
            ("Can you arrange VIP darshan at Banke Bihari and Krishna Janmabhoomi?",
             "Yes, our local Braj guides assist senior citizens and families with fast-track entry routes and authorized pandit sevas to avoid peak rush hours."),
            ("What is the distance between Delhi/Agra and Mathura?",
             "Mathura is 150 km from Delhi (2.5 hours via Yamuna Expressway) and 55 km from Agra (1 hour drive). We provide doorstep AC cab pickups from Delhi NCR and Agra.")
        ]
    },
    'vrindavan-tour-package.html': {
        'title': 'FAQ — Vrindavan Banke Bihari & Prem Mandir Tour',
        'faqs': [
            ("What are the darshan timings for Banke Bihari Temple in Vrindavan?",
             "In summer, morning darshan is from 07:45 AM to 12:00 PM and evening from 05:30 PM to 09:30 PM. In winter, morning darshan is from 08:45 AM to 01:00 PM and evening from 04:30 PM to 08:30 PM."),
            ("What is the best time to see Prem Mandir musical fountain & light show?",
             "The mesmerizing light and musical water fountain show at Prem Mandir takes place every evening between 07:00 PM and 07:45 PM. It is included in all our evening Vrindavan tour itineraries."),
            ("How many days are needed to explore Mathura, Vrindavan, and Govardhan?",
             "A 2-day / 1-night or 3-day / 2-night trip allows you to comfortably visit Mathura, Vrindavan, Govardhan Parikrama, Barsana (Radha Rani Temple), and Nandgaon.")
        ]
    }
}

def generate_faq_html(title, faqs):
    details_html = []
    for i, (q, a) in enumerate(faqs):
        open_attr = " open" if i == 0 else ""
        details_html.append(f'''    <details class="faq"{open_attr}><summary>{q}<span class="pm">+</span></summary>
      <div class="ans">{a}</div></details>''')
    
    return f'''<!-- Frequently Asked Questions -->
<section class="section">
  <div class="container" style="max-width:820px;">
    <div class="center" style="margin-bottom:36px;">
      <p class="eyebrow center">Good to know</p>
      <h2>{title}</h2>
    </div>
{chr(10).join(details_html)}
  </div>
</section>'''

def generate_faq_schema(faqs):
    entities = []
    for q, a in faqs:
        q_esc = q.replace('"', '\\"')
        a_esc = a.replace('"', '\\"')
        entities.append(f'''        {{ "@type": "Question", "name": "{q_esc}", "acceptedAnswer": {{ "@type": "Answer", "text": "{a_esc}" }} }}''')
    
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{',\n'.join(entities)}
  ]
}}
</script>'''

def update_package_faqs():
    for fname, data in FAQ_DATA.items():
        fpath = os.path.join(ROOT_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as fp:
            content = fp.read()
        
        # Replace the FAQ HTML section
        # Look for <!-- Frequently Asked Questions --> ... </section>
        pat = r'<!-- Frequently Asked Questions -->\s*<section class="section">.*?<h2>FAQ — Ayodhya Dharshan Yatra</h2>.*?</section>'
        new_faq_sec = generate_faq_html(data['title'], data['faqs'])
        
        m = re.search(pat, content, re.DOTALL)
        if m:
            content = content[:m.start()] + new_faq_sec + content[m.end():]
            print(f"Replaced visible FAQ HTML in {fname}")
        else:
            print(f"Pattern not found in {fname}")

        # Inject or update FAQ schema
        # If FAQPage already exists, replace mainEntity
        new_schema = generate_faq_schema(data['faqs'])
        if '"@type": "FAQPage"' in content:
            # Replace old FAQPage script block
            content = re.sub(r'<script\s+type=[\"\']application/ld\+json[\"\']>\s*\{\s*\"@context\":\s*\"https://schema\.org\",\s*\"@type\":\s*\"FAQPage\".*?</script>', new_schema, content, flags=re.DOTALL)
            print(f"Updated FAQPage schema in {fname}")
        else:
            # Insert before </head>
            content = content.replace('</head>', new_schema + '\n</head>')
            print(f"Injected new FAQPage schema into {fname}")

        with open(fpath, 'w', encoding='utf-8') as fp:
            fp.write(content)

def update_freshness_dates():
    # 1. Update sitemap.xml
    sitemap_path = os.path.join(ROOT_DIR, 'sitemap.xml')
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sm = f.read()
    sm = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>2026-10-16</lastmod>', sm)
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sm)
    print("Updated sitemap.xml to 2026-10-16")

    # 2. Update rss.xml
    rss_path = os.path.join(ROOT_DIR, 'rss.xml')
    with open(rss_path, 'r', encoding='utf-8') as f:
        rss = f.read()
    rss = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', '<lastBuildDate>Fri, 16 Oct 2026 23:10:00 +0530</lastBuildDate>', rss)
    rss = re.sub(r'<pubDate>.*?</pubDate>', '<pubDate>Fri, 16 Oct 2026 23:10:00 +0530</pubDate>', rss)
    with open(rss_path, 'w', encoding='utf-8') as f:
        f.write(rss)
    print("Updated rss.xml to 2026-10-16")

    # 3. Update dateModified in all HTML
    html_files = [f for f in os.listdir(ROOT_DIR) if f.endswith('.html') and not f.startswith('google')]
    count = 0
    for hf in html_files:
        fpath = os.path.join(ROOT_DIR, hf)
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'dateModified' in c:
            c_new = re.sub(r'\"dateModified\":\s*\"[^\"]+\"', '\"dateModified\": \"2026-10-16T23:10:00+05:30\"', c)
            if c_new != c:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(c_new)
                count += 1
    print(f"Updated dateModified in {count} HTML files to 2026-10-16")

def main():
    print("Starting SEO optimization and FAQ overhaul...")
    update_package_faqs()
    update_freshness_dates()
    print("Done!")

if __name__ == '__main__':
    main()
