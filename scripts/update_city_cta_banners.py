import os
import re

banner_template = """  <!-- DEDICATED CITY EXPLORE CTA BANNER -->
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
      <a href="{blog_url}" class="btn" style="background: linear-gradient(180deg, #d99a26 0%, #b87c14 100%); color: #3b0909; font-weight: 700; font-size: 1.02rem; padding: 14px 32px; border-radius: 30px; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 8px 24px rgba(216, 160, 39, 0.45); transition: transform 0.2s, box-shadow 0.2s;">
        <span>{btn_text}</span>
        <span style="font-size: 1.2rem; line-height: 1;">→</span>
      </a>
    </div>
  </section>"""

mappings = {
    # Varanasi
    "varanasi-tour-package.html": {
        "title": "Want to Explore Everything About Kashi Varanasi?",
        "desc": "Get complete details on Kashi Vishwanath temple VIP darshan, Dashashwamedh Ganga Aarti, boat rides, Sarnath excursion, and 1-day sightseeing travel guides on our dedicated Varanasi blog.",
        "blog_url": "blog-varanasi-local-sightseeing-tour-package.html",
        "btn_text": "Explore Complete Varanasi Kashi Sightseeing Guide"
    },
    "varanasi-same-day-tour-package.html": {
        "title": "Want to Explore Everything About Kashi Varanasi?",
        "desc": "Get complete details on Kashi Vishwanath temple VIP darshan, Dashashwamedh Ganga Aarti, boat rides, Sarnath excursion, and 1-day sightseeing travel guides on our dedicated Varanasi blog.",
        "blog_url": "blog-varanasi-local-sightseeing-tour-package.html",
        "btn_text": "Explore Complete Varanasi Kashi Sightseeing Guide"
    },
    # Ayodhya
    "ayodhya-tour-package.html": {
        "title": "Want to Explore Everything About Ayodhya Dham?",
        "desc": "Get complete details on Shri Ram Janmabhoomi Mandir timings, Hanuman Garhi, Kanak Bhawan, Saryu Aarti ghats, local food, and 1-day sightseeing travel guides on our dedicated Ayodhya blog.",
        "blog_url": "blog-ayodhya-dharshan-tour-package.html",
        "btn_text": "Explore Complete Ayodhya Dham Sightseeing Guide"
    },
    "ayodhya-dharshan-tour-package.html": {
        "title": "Want to Explore Everything About Ayodhya Dham?",
        "desc": "Get complete details on Shri Ram Janmabhoomi Mandir timings, Hanuman Garhi, Kanak Bhawan, Saryu Aarti ghats, local food, and 1-day sightseeing travel guides on our dedicated Ayodhya blog.",
        "blog_url": "blog-ayodhya-dharshan-tour-package.html",
        "btn_text": "Explore Complete Ayodhya Dham Sightseeing Guide"
    },
    "ayodhya-same-day-tour.html": {
        "title": "Want to Explore Everything About Ayodhya Dham?",
        "desc": "Get complete details on Shri Ram Janmabhoomi Mandir timings, Hanuman Garhi, Kanak Bhawan, Saryu Aarti ghats, local food, and 1-day sightseeing travel guides on our dedicated Ayodhya blog.",
        "blog_url": "blog-ayodhya-dharshan-tour-package.html",
        "btn_text": "Explore Complete Ayodhya Dham Sightseeing Guide"
    },
    # Prayagraj
    "prayagraj-tour-package.html": {
        "title": "Want to Explore Everything About Prayagraj Triveni Sangam?",
        "desc": "Get complete details on Triveni Sangam holy dip procedure, VIP boat booking, Bade Hanuman Mandir, Anand Bhawan, and 1-day sightseeing travel guides on our dedicated Prayagraj blog.",
        "blog_url": "blog-prayagraj-sangam-tour-guide.html",
        "btn_text": "Explore Complete Prayagraj Sangam Sightseeing Guide"
    },
    # Vindhyachal
    "vindhyachal-tour-package.html": {
        "title": "Want to Explore Everything About Vindhyachal Dham?",
        "desc": "Get complete details on Maa Vindhyavasini temple VIP darshan, Kali Khoh, Ashtabhuja temple Trikon Parikrama, and 1-day sightseeing travel guides on our dedicated Vindhyachal blog.",
        "blog_url": "blog-vindhyachal-trikon-parikrama-guide.html",
        "btn_text": "Explore Complete Vindhyachal Dham Sightseeing Guide"
    },
    # Chitrakoot
    "chitrakoot-tour-package.html": {
        "title": "Want to Explore Everything About Chitrakoot Dham?",
        "desc": "Get complete details on Kamadgiri 5km parikrama rules, Ram Ghat evening Aarti, Sphatik Shila, Gupt Godavari caves, and 1-day sightseeing travel guides on our dedicated Chitrakoot blog.",
        "blog_url": "blog-chitrakoot-ram-vanvas-tour-guide.html",
        "btn_text": "Explore Complete Chitrakoot Dham Sightseeing Guide"
    },
    # Naimisharanya
    "naimisharanya-tour-package.html": {
        "title": "Want to Explore Everything About Naimisharanya Dham?",
        "desc": "Get complete details on Chakra Tirth holy dip procedure, Maa Lalita Devi temple timings, Vyas Gaddi, Hanuman Garhi, and 1-day sightseeing travel guides on our dedicated Naimisharanya blog.",
        "blog_url": "blog-naimisharanya-chakra-tirth-guide.html",
        "btn_text": "Explore Complete Naimisharanya Dham Sightseeing Guide"
    },
    # Mathura
    "mathura-tour-package.html": {
        "title": "Want to Explore Everything About Mathura Vrindavan?",
        "desc": "Get complete details on Shri Krishna Janmabhoomi Garbha Griha VIP pass, Dwarkadhish temple, Vishram Ghat Yamuna Aarti, and 1-day sightseeing travel guides on our dedicated Mathura blog.",
        "blog_url": "blog-mathura-vrindavan-vip-darshan-guide.html",
        "btn_text": "Explore Complete Mathura Vrindavan Sightseeing Guide"
    },
    # Vrindavan
    "vrindavan-tour-package.html": {
        "title": "Want to Explore Everything About Vrindavan Dham?",
        "desc": "Get complete details on Shri Bankey Bihari temple VIP pass, Prem Mandir 3D illuminated light show, ISKCON kirtan, Nidhivan grove, and 1-day sightseeing travel guides on our dedicated Vrindavan blog.",
        "blog_url": "blog-mathura-vrindavan-vip-darshan-guide.html",
        "btn_text": "Explore Complete Vrindavan Dham Sightseeing Guide"
    },
    "mathura-vrindavan-tour-package.html": {
        "title": "Want to Explore Everything About Mathura & Vrindavan Dham?",
        "desc": "Get complete details on Shri Krishna Janmabhoomi, Shri Bankey Bihari VIP pass, Prem Mandir lighting show, and 1-day sightseeing travel guides on our dedicated Mathura-Vrindavan blog.",
        "blog_url": "blog-mathura-vrindavan-vip-darshan-guide.html",
        "btn_text": "Explore Complete Mathura Vrindavan Sightseeing Guide"
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
        "title": "Want to Explore Everything About Ayodhya Dham?",
        "desc": "Get complete details on Shri Ram Janmabhoomi Mandir timings, Hanuman Garhi, Kanak Bhawan, Saryu Aarti ghats, local food, and 1-day sightseeing travel guides on our dedicated Ayodhya blog.",
        "blog_url": "blog-ayodhya-dharshan-tour-package.html",
        "btn_text": "Explore Complete Ayodhya Dham Sightseeing Guide"
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
        "title": "Want to Read Comprehensive Travel Guides for Kashi, Ayodhya & Prayagraj?",
        "desc": "Explore detailed travel blogs on temple timings, VIP darshan passes, local sightseeing routes, cab fares, and pilgrimage guides across all holy cities.",
        "blog_url": "blog-ayodhya-kashi-vip-darshan-complete-guide.html",
        "btn_text": "Explore Complete Sacred City Travel Guide"
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
        content = re.sub(r"<section class=\"dedicated-city-explore-banner\".*?</section>", banner_html, content, flags=re.DOTALL)
    else:
        if "<footer class=\"site-foot\">" in content:
            content = content.replace("<footer class=\"site-foot\">", f"{banner_html}\n\n<footer class=\"site-foot\">")
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1

print(f"Successfully processed {count} package/city files with dedicated city CTA banners.")
