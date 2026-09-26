import os
import re

banner_template = """  <!-- DEDICATED CITY EXPLORE BLOG CTA BANNER -->
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
        <a href="{blog_url}" class="btn" style="background: linear-gradient(180deg, #d99a26 0%, #b87c14 100%); color: #3b0909; font-weight: 700; font-size: 1.02rem; padding: 14px 32px; border-radius: 30px; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 8px 24px rgba(216, 160, 39, 0.45); transition: transform 0.2s, box-shadow 0.2s;">
          <span>{btn_text}</span>
          <span style="font-size: 1.2rem; line-height: 1;">→</span>
        </a>
      </div>
    </div>
  </section>"""

mappings = {
    # Varanasi
    "varanasi-tour-package.html": {
        "title": "Want to Read Complete Kashi Varanasi Travel Guide?",
        "desc": "Get complete details on Kashi Vishwanath temple VIP darshan, Dashashwamedh Ganga Aarti, boat rides, Sarnath excursion, and 1-day sightseeing travel guides in our dedicated Varanasi guide.",
        "blog_url": "varanasi-guide.html",
        "btn_text": "Read Complete Varanasi Sightseeing Guide"
    },
    "varanasi-same-day-tour-package.html": {
        "title": "Want to Read Complete Kashi Varanasi Travel Guide?",
        "desc": "Get complete details on Kashi Vishwanath temple VIP darshan, Dashashwamedh Ganga Aarti, boat rides, Sarnath excursion, and cab fares in our dedicated Varanasi guide.",
        "blog_url": "varanasi-guide.html",
        "btn_text": "Read Complete Varanasi Sightseeing Guide"
    },
    # Ayodhya
    "ayodhya-tour-package.html": {
        "title": "Want to Read Complete Ayodhya Dham Travel Guide?",
        "desc": "Get complete details on Shri Ram Janmabhoomi Mandir VIP passes, Hanuman Garhi, Kanak Bhawan, Saryu Aarti, and 1-day itinerary in our dedicated Ayodhya guide.",
        "blog_url": "ayodhya-guide.html",
        "btn_text": "Read Complete Ayodhya Dham Guide"
    },
    "ayodhya-dharshan-tour-package.html": {
        "title": "Want to Read Complete Ayodhya Dham Travel Guide?",
        "desc": "Get complete details on Shri Ram Janmabhoomi Mandir VIP passes, Hanuman Garhi, Kanak Bhawan, Saryu Aarti, and 1-day itinerary in our dedicated Ayodhya guide.",
        "blog_url": "ayodhya-guide.html",
        "btn_text": "Read Complete Ayodhya Dham Guide"
    },
    "ayodhya-same-day-tour.html": {
        "title": "Want to Read Complete Ayodhya Dham Travel Guide?",
        "desc": "Get complete details on Shri Ram Janmabhoomi Mandir VIP passes, Hanuman Garhi, Kanak Bhawan, Saryu Aarti, and 1-day itinerary in our dedicated Ayodhya guide.",
        "blog_url": "ayodhya-guide.html",
        "btn_text": "Read Complete Ayodhya Dham Guide"
    },
    # Prayagraj
    "prayagraj-tour-package.html": {
        "title": "Want to Read Complete Prayagraj Sangam Travel Guide?",
        "desc": "Get complete details on Triveni Sangam holy snan procedure, VIP boat booking, Bade Hanuman Mandir, and Magh/Kumbh Mela guide in our dedicated Prayagraj guide.",
        "blog_url": "prayagraj-guide.html",
        "btn_text": "Read Complete Prayagraj Sangam Guide"
    },
    # Vindhyachal
    "vindhyachal-tour-package.html": {
        "title": "Want to Read Complete Vindhyachal Dham Travel Guide?",
        "desc": "Get complete details on Maa Vindhyavasini Devi VIP darshan, Kali Khoh & Ashtabhuja Trikon Parikrama in our dedicated Vindhyachal guide.",
        "blog_url": "vindhyachal-guide.html",
        "btn_text": "Read Complete Vindhyachal Parikrama Guide"
    },
    # Chitrakoot
    "chitrakoot-tour-package.html": {
        "title": "Want to Read Complete Chitrakoot Dham Travel Guide?",
        "desc": "Get complete details on Kamadgiri 5km parikrama rules, Ram Ghat Aarti, Sphatik Shila, and Gupt Godavari in our dedicated Chitrakoot guide.",
        "blog_url": "chitrakoot-guide.html",
        "btn_text": "Read Complete Chitrakoot Ram Vanvas Guide"
    },
    # Naimisharanya
    "naimisharanya-tour-package.html": {
        "title": "Want to Read Complete Naimisharanya Dham Travel Guide?",
        "desc": "Get complete details on Chakra Tirth holy bath, Maa Lalita Devi temple timings, Vyas Gaddi, and Hanuman Garhi in our dedicated Naimisharanya guide.",
        "blog_url": "naimisharanya-guide.html",
        "btn_text": "Read Complete Naimisharanya Guide"
    },
    # Mathura
    "mathura-tour-package.html": {
        "title": "Want to Read Complete Mathura Vrindavan Travel Guide?",
        "desc": "Get complete details on Shri Krishna Janmabhoomi Garbha Griha VIP pass, Dwarkadhish temple, Vishram Ghat Yamuna Aarti, and 1-day sightseeing travel guides in our dedicated Mathura guide.",
        "blog_url": "mathura-guide.html",
        "btn_text": "Read Complete Mathura Vrindavan Guide"
    },
    # Vrindavan
    "vrindavan-tour-package.html": {
        "title": "Want to Read Complete Vrindavan Dham Travel Guide?",
        "desc": "Get complete details on Shri Bankey Bihari VIP pass, Prem Mandir 3D illuminated light show, ISKCON kirtan, and Nidhivan in our dedicated Vrindavan guide.",
        "blog_url": "vrindavan-guide.html",
        "btn_text": "Read Complete Vrindavan Dham Guide"
    },
    "mathura-vrindavan-tour-package.html": {
        "title": "Want to Read Complete Mathura & Vrindavan Travel Guide?",
        "desc": "Get complete details on Shri Krishna Janmabhoomi, Bankey Bihari VIP pass, Prem Mandir lighting show, and Yamuna Aarti in our dedicated Mathura Vrindavan guide.",
        "blog_url": "mathura-guide.html",
        "btn_text": "Read Complete Mathura Vrindavan Guide"
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
        "title": "Want to Read Complete Ayodhya Dham Travel Guide?",
        "desc": "Get complete details on Shri Ram Janmabhoomi Mandir VIP passes, Hanuman Garhi, Kanak Bhawan, Saryu Aarti, and 1-day itinerary in our dedicated Ayodhya blog post.",
        "blog_url": "blog-ayodhya-dharshan-tour-package.html",
        "btn_text": "Read Complete Ayodhya Dham Blog Guide"
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
        "title": "Want to Read Complete Sacred Circuit Travel Guide?",
        "desc": "Explore detailed travel blogs on temple timings, VIP darshan passes, local sightseeing routes, cab fares, and pilgrimage guides across all holy cities.",
        "blog_url": "blog-ayodhya-kashi-vip-darshan-complete-guide.html",
        "btn_text": "Read Complete Multi-City Yatra Blog Guide"
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
        content = re.sub(r"<!-- DEDICATED CITY EXPLORE BLOG CTA BANNER -->.*?</section>", banner_html, content, flags=re.DOTALL)
        content = re.sub(r"<section class=\"dedicated-city-explore-banner\".*?</section>", banner_html, content, flags=re.DOTALL)
    else:
        if "<footer class=\"site-foot\">" in content:
            content = content.replace("<footer class=\"site-foot\">", f"{banner_html}\n\n<footer class=\"site-foot\">")
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1

print(f"Successfully configured CTA banners across {count} city package pages to link directly to their specific published blog post.")
