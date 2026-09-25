import os
import re

banner_template = """  <!-- DEDICATED CITY TOUR PACKAGE CTA BANNER -->
  <section class="dedicated-city-explore-banner" style="padding: 32px 16px; background: transparent;">
    <div style="background: linear-gradient(135deg, #701616 0%, #4a0d0d 100%); border: 1.5px solid #c59b27; border-radius: 20px; padding: 48px 32px; text-align: center; max-width: 860px; margin: 0 auto; box-shadow: 0 15px 40px rgba(74, 13, 13, 0.35); position: relative; overflow: hidden;">
      <div style="margin-bottom: 12px; display: flex; justify-content: center;">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="#d8a027" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 2L15 8H9L12 2ZM12 6L19 21H5L12 6ZM12 10L8 18H16L12 10Z"/>
        </svg>
      </div>
      <h3 style="font-family: var(--font-display, 'Cormorant Garamond', serif); font-size: clamp(1.6rem, 3.2vw, 2.2rem); font-weight: 600; color: #ffffff; margin: 0 0 14px 0; line-height: 1.25;">
        {title}
      </h3>
      <p style="font-size: 1.02rem; line-height: 1.6; color: #fcefd9; max-width: 720px; margin: 0 auto 28px; font-weight: 400;">
        {desc}
      </p>
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#yatraForm" class="btn" style="background: linear-gradient(180deg, #d99a26 0%, #b87c14 100%); color: #3b0909; font-weight: 700; font-size: 1.02rem; padding: 14px 32px; border-radius: 30px; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 8px 24px rgba(216, 160, 39, 0.45); transition: transform 0.2s, box-shadow 0.2s;">
          <span>{btn_text}</span>
          <span style="font-size: 1.2rem; line-height: 1;">↓</span>
        </a>
      </div>
    </div>
  </section>"""

mappings = {
    # Varanasi
    "varanasi-tour-package.html": {
        "title": "Ready to Book Your Kashi Varanasi Yatra Package?",
        "desc": "Get instant booking confirmation with 3-star hotel stays, private AC cab pickup, VIP Kashi Vishwanath Sugam Darshan passes, and Ganga Aarti boat arrangements.",
        "btn_text": "Book Varanasi Package Now"
    },
    "varanasi-same-day-tour-package.html": {
        "title": "Ready to Book Your Varanasi Same Day Cab Package?",
        "desc": "Book full-day private AC cab for Kashi Vishwanath, Sarnath, Kaal Bhairav, and Ganga Aarti with door-to-door hotel & railway station pickup.",
        "btn_text": "Book Varanasi Same Day Cab Now"
    },
    # Ayodhya
    "ayodhya-tour-package.html": {
        "title": "Ready to Book Your Ayodhya Ram Mandir Yatra Package?",
        "desc": "Book complete Ayodhya tour package with Shri Ram Janmabhoomi VIP darshan escort, Hanuman Garhi, Saryu Aarti, and private AC cab pickup.",
        "btn_text": "Book Ayodhya Tour Package Now"
    },
    "ayodhya-dharshan-tour-package.html": {
        "title": "Ready to Book Your Ayodhya Ram Mandir Yatra Package?",
        "desc": "Book complete Ayodhya tour package with Shri Ram Janmabhoomi VIP darshan escort, Hanuman Garhi, Saryu Aarti, and private AC cab pickup.",
        "btn_text": "Book Ayodhya Tour Package Now"
    },
    "ayodhya-same-day-tour.html": {
        "title": "Ready to Book Your Ayodhya Same Day Sightseeing Tour?",
        "desc": "Full-day AC sedan / SUV cab booking for Ram Mandir, Hanuman Garhi, Kanak Bhawan, and Saryu Aarti with local expert driver.",
        "btn_text": "Book Ayodhya Same Day Tour Now"
    },
    # Prayagraj
    "prayagraj-tour-package.html": {
        "title": "Ready to Book Your Prayagraj Triveni Sangam Yatra Package?",
        "desc": "Book Triveni Sangam holy snan by boat, Bade Hanuman Mandir darshan, Akshayavat, and private AC cab package with instant confirmation.",
        "btn_text": "Book Prayagraj Sangam Package Now"
    },
    # Vindhyachal
    "vindhyachal-tour-package.html": {
        "title": "Ready to Book Your Vindhyachal Devi Trikon Parikrama Yatra?",
        "desc": "Book complete Maa Vindhyavasini Devi darshan, Kali Khoh & Ashtabhuja Trikon Parikrama cab package with local guide support.",
        "btn_text": "Book Vindhyachal Parikrama Package Now"
    },
    # Chitrakoot
    "chitrakoot-tour-package.html": {
        "title": "Ready to Book Your Chitrakoot Ram Vanvas Dham Yatra?",
        "desc": "Book Kamadgiri Parikrama, Ram Ghat Aarti, Sphatik Shila, and Gupt Godavari sightseeing package with private AC cab.",
        "btn_text": "Book Chitrakoot Tour Package Now"
    },
    # Naimisharanya
    "naimisharanya-tour-package.html": {
        "title": "Ready to Book Your Naimisharanya Chakra Tirth Yatra Package?",
        "desc": "Book Chakra Tirth holy dip, Maa Lalita Devi Shakti Peeth, Vyas Gaddi, and Hanuman Garhi package with comfortable private transport.",
        "btn_text": "Book Naimisharanya Package Now"
    },
    # Mathura
    "mathura-tour-package.html": {
        "title": "Ready to Book Your Mathura Vrindavan Yatra Package?",
        "desc": "Book Shri Krishna Janmabhoomi, Bankey Bihari VIP pass, Prem Mandir light show, and Yamuna Aarti package with private AC cab.",
        "btn_text": "Book Mathura Vrindavan Package Now"
    },
    # Vrindavan
    "vrindavan-tour-package.html": {
        "title": "Ready to Book Your Vrindavan Dham Yatra Package?",
        "desc": "Book Shri Bankey Bihari VIP entry, Prem Mandir 3D show, ISKCON kirtan, and Nidhivan package with private AC transport.",
        "btn_text": "Book Vrindavan Tour Package Now"
    },
    "mathura-vrindavan-tour-package.html": {
        "title": "Ready to Book Your Mathura Vrindavan Yatra Package?",
        "desc": "Book Shri Krishna Janmabhoomi, Bankey Bihari VIP pass, Prem Mandir light show, and Yamuna Aarti package with private AC cab.",
        "btn_text": "Book Mathura Vrindavan Package Now"
    }
}

origin_pages = [
    "delhi-to-ayodhya-tour-package.html",
    "mumbai-to-ayodhya-tour-package.html",
    "bengaluru-to-ayodhya-tour-package.html",
    "hyderabad-to-ayodhya-tour-package.html",
    "chennai-to-ayodhya-tour-package.html",
    "kolkata-to-ayodhya-tour-package.html",
    "ahmedabad-to-ayodhya-tour-package.html",
    "patna-to-ayodhya-tour-package.html",
    "lucknow-to-ayodhya-same-day-tour-package.html"
]

for op in origin_pages:
    mappings[op] = {
        "title": "Ready to Book Your Ayodhya Ram Mandir Tour Package?",
        "desc": "Get complete all-inclusive package with hotel stay, pickup, Ram Mandir VIP darshan escort, and Saryu Aarti.",
        "btn_text": "Book Ayodhya Tour Package Now"
    }

circuit_pages = [
    "ayodhya-prayagraj-varanasi-tour-package.html",
    "ayodhya-prayagraj-tour-package.html",
    "ayodhya-varanasi-tour-package.html",
    "ayodhya-prayagraj-chitrakoot-varanasi-tour-package.html",
    "full-ramayana-circuit-tour-package.html"
]

for cp in circuit_pages:
    mappings[cp] = {
        "title": "Ready to Book Your Multi-City Sacred Circuit Yatra?",
        "desc": "Book all-inclusive Kashi, Ayodhya & Prayagraj tour package with hotels, private cabs, and VIP temple darshan.",
        "btn_text": "Book Multi-City Yatra Package Now"
    }

count = 0
for file_name, info in mappings.items():
    if not os.path.exists(file_name):
        continue
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
    
    banner_html = banner_template.format(**info)
    
    if "dedicated-city-explore-banner" in content:
        content = re.sub(r"<!-- DEDICATED CITY EXPLORE CTA BANNER -->.*?</section>", banner_html, content, flags=re.DOTALL)
        content = re.sub(r"<!-- DEDICATED CITY TOUR PACKAGE CTA BANNER -->.*?</section>", banner_html, content, flags=re.DOTALL)
        content = re.sub(r"<section class=\"dedicated-city-explore-banner\".*?</section>", banner_html, content, flags=re.DOTALL)
    else:
        if "<footer class=\"site-foot\">" in content:
            content = content.replace("<footer class=\"site-foot\">", f"{banner_html}\n\n<footer class=\"site-foot\">")
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1

print(f"Successfully updated CTA banners across {count} package/city pages to scroll directly to #yatraForm.")
