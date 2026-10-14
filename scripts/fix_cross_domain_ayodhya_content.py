import os
import re
import glob

print("Fixing Cross-Domain Duplicate Penalty & Differentiating All Package Content...")

# ----------------------------------------------------------------------
# 1. FIX AYODHYA-TOUR-PACKAGE.HTML (VARANASI TO AYODHYA DEPARTURE)
# ----------------------------------------------------------------------
with open("ayodhya-tour-package.html", "r", encoding="utf-8") as f:
    ayodhya_html = f.read()

# Update Title
ayodhya_html = re.sub(
    r'<title>.*?</title>',
    '<title>Varanasi to Ayodhya Tour Package (Same Day AC Cab) | Kashi Dharshan</title>',
    ayodhya_html,
    flags=re.I
)

# Update Meta Description
ayodhya_html = re.sub(
    r'<meta[^>]*name=[\"\']description[\"\'][^>]*content=[\"\'].*?[\"\']',
    '<meta name="description" content="Book Varanasi to Ayodhya Same Day Tour Package 2026 by private AC cab via Purvanchal Expressway. Includes doorstep hotel pickup in Varanasi, Ram Mandir Sugam Darshan VIP pass assistance, Hanuman Garhi, Saryu River Aarti, Kanak Bhawan & evening return drop in Varanasi.">',
    ayodhya_html,
    flags=re.I
)

# Update H1
ayodhya_html = re.sub(
    r'<h1[^>]*>.*?</h1>',
    '<h1 class="display hero-title-2line"><span class="hero-line-1">Varanasi to Ayodhya Tour Package: </span> <span class="hero-line-2">Same Day Ram Mandir VIP Darshan by AC Cab</span></h1>',
    ayodhya_html,
    flags=re.I | re.DOTALL
)

# Update Lead Paragraph
ayodhya_html = re.sub(
    r'<p class="lead">.*?</p>',
    '<p class="lead">Depart from your Varanasi hotel or railway station in a private sanitized AC cab via the high-speed Purvanchal Expressway. Experience hassle-free Ram Mandir Sugam Darshan VIP entry, visit Hanuman Garhi & Kanak Bhawan, attend the sunset Saryu River Aarti, and return back to Kashi the same evening.</p>',
    ayodhya_html,
    count=1,
    flags=re.I | re.DOTALL
)

# Update Breadcrumb
ayodhya_html = re.sub(
    r'<p class="crumb">.*?</p>',
    '<p class="crumb"><a href="/">Home</a> &nbsp;/&nbsp; <a href="services">Services</a> &nbsp;/&nbsp; Varanasi to Ayodhya Tour</p>',
    ayodhya_html,
    count=1,
    flags=re.I | re.DOTALL
)

# Update Itinerary in ayodhya-tour-package.html to be Varanasi Departure
ayodhya_itinerary = """        <h2 style="color:var(--maroon); margin-bottom: 20px;">Varanasi to Ayodhya Same-Day Itinerary</h2>
        
        <div class="timeline">
          <div class="timeline-item reveal">
            <div class="timeline-time">06:00 AM — Varanasi Hotel Pickup &amp; Express Drive</div>
            <h3>Departure from Kashi via Purvanchal Expressway</h3>
            <p>Our sanitized AC Sedan/SUV picks you up directly from your Varanasi hotel, Godowlia, or Cantt Railway Station. Enjoy a smooth 3.5-hour drive via NH-19 and Purvanchal Expressway with a stop for breakfast.</p>
          </div>
          <div class="timeline-item reveal">
            <div class="timeline-time">10:00 AM – 02:00 PM — Sacred Core Darshan in Ayodhya Dham</div>
            <h3>Hanuman Garhi &amp; Shri Ram Janmabhoomi VIP Darshan</h3>
            <p>Arrive in Ayodhya Dham. Meet our local dedicated pandit guide. Begin by seeking blessings at Hanuman Garhi, followed by priority fast-track entry into the magnificent Shri Ram Janmabhoomi Mandir. Visit Kanak Bhawan and Dashrath Mahal.</p>
          </div>
          <div class="timeline-item reveal">
            <div class="timeline-time">05:30 PM – 09:30 PM — Saryu Aarti &amp; Return to Varanasi</div>
            <h3>Ram Ki Paidi Sunset Aarti &amp; Kashi Drop</h3>
            <p>Witness the divine evening Saryu River Aarti at Ram Ki Paidi amidst hundreds of floating diyas. At 06:30 PM, board your private AC cab for the comfortable return drive back to Varanasi, dropping you at your hotel by 09:30 PM.</p>
          </div>
        </div>"""

ayodhya_html = re.sub(
    r'<h2 style="color:var\(--maroon\); margin-bottom: 20px;\">.*?</div>\s*</div>\s*</div>',
    ayodhya_itinerary + "\n      </div>",
    ayodhya_html,
    flags=re.DOTALL
)

with open("ayodhya-tour-package.html", "w", encoding="utf-8") as f:
    f.write(ayodhya_html)
print("Updated ayodhya-tour-package.html to Varanasi departure!")

# ----------------------------------------------------------------------
# 2. FIX AYODHYA-PRAYAGRAJ-VARANASI-TOUR-PACKAGE.HTML (KASHI 3-DHAM TOUR)
# ----------------------------------------------------------------------
with open("ayodhya-prayagraj-varanasi-tour-package.html", "r", encoding="utf-8") as f:
    three_dham_html = f.read()

# Update Title
three_dham_html = re.sub(
    r'<title>.*?</title>',
    '<title>Kashi Prayagraj Ayodhya Tour Package 4 Days | Kashi Dharshan</title>',
    three_dham_html,
    flags=re.I
)

# Update Meta Description
three_dham_html = re.sub(
    r'<meta[^>]*name=[\"\']description[\"\'][^>]*content=[\"\'].*?[\"\']',
    '<meta name="description" content="Book 4-Day Kashi Prayagraj Ayodhya 3-Dham Tour Package 2026 starting & concluding in Varanasi. Includes Kashi Vishwanath VIP Darshan, Dashashwamedh Ganga Aarti boat ride, Triveni Sangam Holy Dip in Prayagraj, and Ayodhya Ram Mandir VIP entry by private AC cab.">',
    three_dham_html,
    flags=re.I
)

# Update H1
three_dham_html = re.sub(
    r'<h1[^>]*>.*?</h1>',
    '<h1 class="display hero-title-2line"><span class="hero-line-1">Kashi Prayagraj Ayodhya </span> <span class="hero-line-2">3-Dham Tour Package (4 Days / 3 Nights)</span></h1>',
    three_dham_html,
    flags=re.I | re.DOTALL
)

# Update Lead Paragraph
three_dham_html = re.sub(
    r'<p class="lead">.*?</p>',
    '<p class="lead">The ultimate Uttar Pradesh sacred triangle yatra connecting Lord Shiva’s eternal Kashi, the sacred Triveni Sangam confluence at Prayagraj, and Maryada Purushottam Lord Ram’s Janmabhoomi in Ayodhya. Starts and concludes seamlessly in Varanasi with private AC cab, hotel stays, and VIP entry passes.</p>',
    three_dham_html,
    count=1,
    flags=re.I | re.DOTALL
)

# Update Breadcrumb
three_dham_html = re.sub(
    r'<p class="crumb">.*?</p>',
    '<p class="crumb"><a href="/">Home</a> &nbsp;/&nbsp; <a href="services">Services</a> &nbsp;/&nbsp; Kashi Prayagraj Ayodhya 4-Day Tour</p>',
    three_dham_html,
    count=1,
    flags=re.I | re.DOTALL
)

with open("ayodhya-prayagraj-varanasi-tour-package.html", "w", encoding="utf-8") as f:
    f.write(three_dham_html)
print("Updated ayodhya-prayagraj-varanasi-tour-package.html to Kashi 3-Dham package!")

# ----------------------------------------------------------------------
# 3. FIX AUTHENTIC VARANASI ITINERARY IN VARANASI-TOUR-PACKAGE & KASHI-VISHWANATH-TOUR-PACKAGE
# ----------------------------------------------------------------------
varanasi_pure_itinerary = """        <h2 style="color:var(--maroon); margin-bottom: 20px;">3-Day Varanasi &amp; Kashi Itinerary</h2>
        
        <div class="timeline">
          <div class="timeline-item reveal">
            <div class="timeline-time">Day 1 — Arrival &amp; Grand Evening Ganga Aarti</div>
            <h3>Ghat Check-in &amp; Private Boat Aarti Ride</h3>
            <p>Arrive in Varanasi (Airport / Station). Meet our representative and transfer to your hotel near Godowlia or the Ghats. At 05:00 PM, board your private wooden boat to witness the majestic 7-priest evening Ganga Aarti at Dashashwamedh Ghat from the river.</p>
          </div>
          <div class="timeline-item reveal">
            <div class="timeline-time">Day 2 — Sacred Darshan &amp; Sarnath Excursion</div>
            <h3>Kashi Vishwanath VIP Darshan, Kal Bhairav &amp; Sarnath</h3>
            <p>Morning priority Sugam Darshan at Shri Kashi Vishwanath Dham Golden Temple, Maa Annapurna Mandir, and Kal Bhairav (Kotwal of Kashi). In the afternoon, explore Sarnath Buddhist Stupas and the original Ashoka Lion Capital museum.</p>
          </div>
          <div class="timeline-item reveal">
            <div class="timeline-time">Day 3 — Subah-e-Banaras &amp; Departure Transfer</div>
            <h3>Assi Sunrise Boat, Sankat Mochan &amp; Farewell</h3>
            <p>Experience early morning Subah-e-Banaras at Assi Ghat with Vedic chanting and classical music. Visit Sankat Mochan Hanuman Temple and New Vishwanath Temple inside BHU before your departure airport/station drop.</p>
          </div>
        </div>"""

for v_file in ["varanasi-tour-package.html", "kashi-vishwanath-tour-package.html"]:
    with open(v_file, "r", encoding="utf-8") as f:
        v_content = f.read()
    
    # Replace the copied Ayodhya timeline
    v_content = re.sub(
        r'<div class="timeline">.*?</div>\s*</div>\s*<!-- Senior Citizen',
        varanasi_pure_itinerary + "\n      <!-- Senior Citizen",
        v_content,
        flags=re.DOTALL
    )
    # Fix crumb if it mentions Ayodhya Dharshan Tour
    v_content = v_content.replace("Ayodhya Dharshan Tour", "Varanasi Kashi Darshan Tour")
    # Fix lead paragraph if it mentions Lord Ram's holy birthplace
    v_content = re.sub(
        r'<p class="lead">An unhurried, spiritual yatra exploring the ancient temples of Lord Ram.*?</p>',
        '<p class="lead">An unhurried, deeply spiritual yatra exploring the eternal city of Lord Shiva. Includes priority Kashi Vishwanath Sugam Darshan VIP entry, private sunset boat ride for Dashashwamedh Ganga Aarti, Sarnath excursion, comfortable AC vehicle and verified hotel stays.</p>',
        v_content,
        flags=re.I | re.DOTALL
    )
    with open(v_file, "w", encoding="utf-8") as f:
        f.write(v_content)
    print(f"Fixed authentic Varanasi itinerary in {v_file}!")

# ----------------------------------------------------------------------
# 4. FIX DESTINATION-SPECIFIC ITINERARIES IN OTHER TOUR PACKAGES
# ----------------------------------------------------------------------
def replace_timeline_in_file(filepath, new_timeline_html):
    with open(filepath, "r", encoding="utf-8") as f:
        c = f.read()
    if 'Ram ki Paidi' in c:
        c = re.sub(
            r'<div class="timeline">.*?</div>\s*</div>\s*<!-- Senior Citizen',
            new_timeline_html + "\n      <!-- Senior Citizen",
            c,
            flags=re.DOTALL
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Fixed specific destination timeline in {filepath}!")

# Prayagraj
prayagraj_itinerary = """        <h2 style="color:var(--maroon); margin-bottom: 20px;">3-Day Prayagraj Sangam Itinerary</h2>
        <div class="timeline">
          <div class="timeline-item reveal"><div class="timeline-time">Day 1 — Welcome &amp; Sangam Aarti</div><h3>Arrival &amp; Triveni Sunset</h3><p>Arrive in Prayagraj. Transfer to hotel. Evening visit to Sangam bank for sunset Ganga Aarti and view of the historic Allahabad Fort.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 2 — Sacred Sangam Snan &amp; Shrines</div><h3>Holy Dip, Lete Hanuman &amp; Alopi Devi</h3><p>Early morning private boat ride for holy snan at the confluence of Ganga, Yamuna &amp; Saraswati. Darshan at Bade Hanuman Ji (Lete Hanuman) and Maa Alopi Devi Shaktipeeth.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 3 — Heritage &amp; Departure</div><h3>Anand Bhawan &amp; Departure</h3><p>Visit historic Anand Bhawan (Nehru heritage museum), Chandrashekhar Azad Park, and drop at Prayagraj Junction or airport.</p></div>
        </div>"""
replace_timeline_in_file("prayagraj-tour-package.html", prayagraj_itinerary)

# Mathura & Vrindavan
mathura_itinerary = """        <h2 style="color:var(--maroon); margin-bottom: 20px;">3-Day Mathura &amp; Vrindavan Itinerary</h2>
        <div class="timeline">
          <div class="timeline-item reveal"><div class="timeline-time">Day 1 — Mathura Janmabhoomi &amp; Yamuna Aarti</div><h3>Shri Krishna Janmabhoomi &amp; Vishram Ghat</h3><p>Arrive in Mathura. VIP darshan at Shri Krishna Janmasthan Temple, Dwarkadhish Mandir, and evening Yamuna Aarti at historic Vishram Ghat.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 2 — Divine Vrindavan Darshan</div><h3>Bankey Bihari, ISKCON &amp; Prem Mandir</h3><p>Morning VIP entry at Bankey Bihari Mandir, Nidhivan, ISKCON Krishna Balaram Mandir, and mesmerizing evening musical laser light show at Prem Mandir.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 3 — Govardhan Parikrama &amp; Departure</div><h3>Govardhan Hill, Radha Kund &amp; Farewell</h3><p>Visit Govardhan Hill, Mansi Ganga, and Radha Kund before departure transfer to Mathura Station or Delhi.</p></div>
        </div>"""
replace_timeline_in_file("mathura-tour-package.html", mathura_itinerary)
replace_timeline_in_file("vrindavan-tour-package.html", mathura_itinerary)
replace_timeline_in_file("mathura-vrindavan-tour-package.html", mathura_itinerary)

# Chitrakoot
chitrakoot_itinerary = """        <h2 style="color:var(--maroon); margin-bottom: 20px;">3-Day Chitrakoot Pilgrimage Itinerary</h2>
        <div class="timeline">
          <div class="timeline-item reveal"><div class="timeline-time">Day 1 — Ram Ghat &amp; Mandakini Aarti</div><h3>Arrival &amp; Holy River Aarti</h3><p>Arrive in Chitrakoot. Check in to hotel. Evening boat ride at Ram Ghat and witness the soulful evening Mandakini River Aarti.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 2 — Sacred Ram Vanvas Shrines</div><h3>Kamadgiri Parikrama, Hanuman Dhara &amp; Gupt Godavari</h3><p>Perform sacred Kamadgiri Parikrama, climb Hanuman Dhara for spring water darshan, and explore the ancient subterranean streams of Gupt Godavari caves.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 3 — Sati Anusuya &amp; Departure</div><h3>Sati Anusuya Ashram, Sphatik Shila &amp; Drop</h3><p>Visit peaceful Sati Anusuya Ashram in the dense forest and Sphatik Shila (footprints of Lord Ram &amp; Sita) before departure transfer.</p></div>
        </div>"""
replace_timeline_in_file("chitrakoot-tour-package.html", chitrakoot_itinerary)

# Vindhyachal
vindhyachal_itinerary = """        <h2 style="color:var(--maroon); margin-bottom: 20px;">3-Day Vindhyachal Shaktipeeth Itinerary</h2>
        <div class="timeline">
          <div class="timeline-item reveal"><div class="timeline-time">Day 1 — Arrival &amp; Maa Vindhyavasini Darshan</div><h3>Ganga Snan &amp; Main Temple VIP Entry</h3><p>Arrive at Vindhyachal Dham. Holy dip in the Ganges and fast-track VIP darshan of Maa Vindhyavasini (Kajal Devi).</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 2 — Complete Trikon Parikrama</div><h3>Kali Khoh, Ashtabhuja &amp; Ropeway Ride</h3><p>Perform the auspicious Trikon Parikrama visiting Maa Kali Khoh (Goddess Chamunda) and Maa Ashtabhuja Devi atop Vindhya hill with scenic ropeway views.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 3 — Sita Kund &amp; Departure</div><h3>Sita Kund, Rameshwar Temple &amp; Return</h3><p>Visit serene Sita Kund and ancient Rameshwar Mahadev Temple before transfer back to Mirzapur / Varanasi.</p></div>
        </div>"""
replace_timeline_in_file("vindhyachal-tour-package.html", vindhyachal_itinerary)

# Naimisharanya
naimisharanya_itinerary = """        <h2 style="color:var(--maroon); margin-bottom: 20px;">3-Day Naimisharanya Tapasthali Itinerary</h2>
        <div class="timeline">
          <div class="timeline-item reveal"><div class="timeline-time">Day 1 — Chakra Tirth &amp; Holy Snan</div><h3>Arrival &amp; Chakra Kund Pujan</h3><p>Arrive in Naimisharanya (Sitapur). Holy dip at the miraculous circular Chakra Tirth and attend evening Gomti Aarti.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 2 — 88,000 Rishi Tapasthali Darshan</div><h3>Vyas Gaddi, Lalita Devi Shaktipeeth &amp; Soot Gaddi</h3><p>Visit sacred Vyas Gaddi where Maharishi Ved Vyas divided the Vedas and composed Puranas, Maa Lalita Devi temple, and Soot Gaddi.</p></div>
          <div class="timeline-item reveal"><div class="timeline-time">Day 3 — Dadhichi Kund &amp; Departure</div><h3>Dadhichi Kund, Hanuman Garhi &amp; Return</h3><p>Visit Dadhichi Kund where Sage Dadhichi donated his bones for the divine Vajra, followed by departure transfer to Lucknow.</p></div>
        </div>"""
replace_timeline_in_file("naimisharanya-tour-package.html", naimisharanya_itinerary)

# ----------------------------------------------------------------------
# 5. FIX BRAND NAME AND OG:SITE_NAME ACROSS ALL HTML FILES
# ----------------------------------------------------------------------
all_html_files = glob.glob("*.html")
brand_fixed = 0
site_name_fixed = 0

for filepath in all_html_files:
    if filepath == "google0dc20d35f8fb3bcd.html":
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        c = f.read()
    orig = c
    
    # Replace brand name in navbar
    c = c.replace('<span class="brand-name">Ayodhya Dharshan<small>Teerth Yatra</small></span>', '<span class="brand-name">Kashi Dharshan<small>Teerth Yatra</small></span>')
    c = c.replace('<span class="brand-name">Ayodhya Dharshan<small>Ayodhya · Kashi · Vrindavan Yatras</small></span>', '<span class="brand-name">Kashi Dharshan<small>Kashi · Ayodhya · Vrindavan Yatras</small></span>')
    c = c.replace('aria-label="Ayodhya Dharshan home"', 'aria-label="Kashi Dharshan home"')
    c = c.replace('alt="Ayodhya Dharshan Logo"', 'alt="Kashi Dharshan Logo"')
    
    # Replace og:site_name
    c = re.sub(r'<meta[^>]*property=[\"\']og:site_name[\"\'][^>]*content=[\"\']Ayodhya Dharshan[\"\']', '<meta property="og:site_name" content="Kashi Dharshan"', c)

    if c != orig:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(c)
        brand_fixed += 1

print(f"Fixed brand name and og:site_name in {brand_fixed} files!")
print("\nAll Cross-Domain Duplicate Penalty Fixes Applied Successfully!")
