import re

extra_content = """
      <!-- SACRED GEOGRAPHY & 84 GHATS HERITAGE ENCYCLOPEDIA -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">7. Sacred Geography of Kashi Dham & Exhaustive Guide to 84 Riverfront Ghats</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">Kashi (Varanasi) is recognised as the oldest living city in human civilization, existing for over 5,000 years continuously on the crescent-shaped western bank of the sacred River Ganga. In Skanda Purana's Kashi Khanda, Shiva declares Kashi as His permanent abode — <em>Anandavana</em> (the Forest of Bliss) and <em>Avimuktha Kshetra</em> (the sacred territory that Shiva never forsakes, even during Pralaya or global cosmic dissolution).</p>

        <h4 style="font-size: 1.3rem; color: #78350f; margin: 24px 0 12px;">The Pancha Tirthas (5 Most Sacred Riverfront Ghats of Kashi):</h4>
        <p style="color: #4b5563; line-height: 1.7;">Performing holy dips and offering Pinda Daan ancestral rituals across these 5 key ghats completes the sacred <em>Pancha Tirtha Yatra</em>:</p>
        <ul style="color: #4b5563; line-height: 1.8; margin-top: 10px;">
          <li><strong>1. Assi Ghat (Confluence of River Assi & Ganga):</strong> The southernmost major ghat where Goddess Durga dropped her sword (Asi) after destroying demons Shumbha and Nishumbha. Famous for <em>Subah-e-Banaras</em> sunrise morning Vedic chants, Yogasana sessions, and classical music performances.</li>
          <li><strong>2. Dashashwamedh Ghat (The Heart of Kashi):</strong> Where Lord Brahma performed ten Horse Sacrifices (Dasha Ashwamedha Yajna) to welcome Lord Shiva to Kashi. The venue for the famous grand 7-priest evening Ganga Aarti.</li>
          <li><strong>3. Manikarnika Ghat (The Holy Burning Ghat & Shaktipeeth):</strong> The primary cremation ghat where Lord Shiva grants <em>Taraka Mantra</em> for instant Moksha (liberation from the cycle of rebirth). According to Puranas, Goddess Sati's earring (Manikarnika) fell into the sacred Chakra Pushkarini Kund excavated by Lord Vishnu.</li>
          <li><strong>4. Panchganga Ghat (Confluence of 5 Rivers):</strong> Where 5 sacred rivers — Ganga, Yamuna, Saraswati, Kirana, and Dhutapapa — meet invisibly. The tapasthali of Sant Kabir, Shrimad Vallabhacharya, and Swami Ramananda. Site of the magnificent 17th-century Alamgir Mosque built over the ancient Bindu Madhav Vishnu Temple.</li>
          <li><strong>5. Rajghat (The Northern Gateway):</strong> The northernmost historical ghat where Ancient Kashi began. Connected to Malaviya Bridge and Namo Ghat (featuring the famous 75-feet Namaste hand sculptures and helipad facility).</li>
        </ul>

        <h4 style="font-size: 1.3rem; color: #78350f; margin: 24px 0 12px;">Complete Index of Famous Heritage Ghats from South to North:</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Assi to Chet Singh Ghat:</strong> Assi Ghat, Ganga Mahal Ghat, Rewa Ghat, Tulsi Ghat (where Goswami Tulsidas composed Ramcharitmanas), Bhadaini Ghat, Anandamayi Ghat, Jain Ghat (birthplace of 7th Tirthankara Suparshvanatha), Nishadraj Ghat, and Chet Singh Ghat (fortified palace of Maharaja Chet Singh).
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Shivala to Kedar Ghat:</strong> Shivala Ghat, Mahanirvani Ghat, Dandi Ghat, Hanuman Ghat (established by Lord Hanuman and Swami Ramdas), Lali Ghat, Vijayanagaram Ghat, Kedar Ghat (housing Sri Gauri Kedar Temple, a replica of Kedarnath Jyotirlinga).
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Chowki to Dashashwamedh Ghat:</strong> Chauki Ghat, Kshemeshwar Ghat, Mansarovar Ghat, Pandey Ghat, Digpatia Ghat, Chousatti Ghat (dedicated to 64 Yoginis), Rana Mahal Ghat, Darbhanga Ghat (featuring the luxurious BrijRama Palace), Ahilyabai Ghat, Munshi Ghat, and Dashashwamedh Ghat.
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Man Mandir to Manikarnika Ghat:</strong> Man Mandir Ghat (featuring Raja Man Singh Observatory & Jantar Mantar), Tripura Bhairavi Ghat, Mir Ghat, Phuta Ghat, Nepali Ghat (featuring wooden Pagoda-style Nepali Pashupatinath Temple), Lalita Ghat (entrance to Kashi Corridor), and Manikarnika Ghat.
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Scindia to Namo Ghat:</strong> Scindia Ghat (housing the famous partially submerged Ratneshwar Mahadev Leaning Temple), Sankatha Ghat, Ganga Mahal Ghat, Bhosale Ghat, Panchganga Ghat, Durga Ghat, Brahma Ghat, Gai Ghat, Trilochan Ghat, Rajghat, and Namo Ghat.
          </div>
        </div>
      </div>

      <!-- KASHI VISHWANATH DHAM CORRIDOR ARCHITECTURE & FACILITY GUIDE -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">8. Shri Kashi Vishwanath Dham Corridor Architecture & Facilities</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">Inaugurated by Prime Minister Narendra Modi in December 2021, the grand <strong>Shri Kashi Vishwanath Dham Corridor Project</strong> expanded the temple premises from a cramped 3,000 square feet to over 500,000 square feet (50,000 sq meters), directly connecting the holy waters of the River Ganga at Lalita Ghat to the Golden Temple sanctum.</p>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">24 Key Public Facility Buildings Inside the Corridor:</h4>
        <ul style="color: #4b5563; line-height: 1.8; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px;">
          <li><strong>1. Yatri Suvidha Kendra (Tourist Facilitation Center):</strong> Luggage lockers, enquiry counters, wheelchair issuance, emergency medical care room, and ticket booking windows.</li>
          <li><strong>2. Vedic Library & Research Center:</strong> Storing ancient Sanskrit manuscripts, Puranas, and Vedic literature.</li>
          <li><strong>3. City Museum & Cultural Center:</strong> Displaying 5,000-year history of Banaras, silk weaving heritage, and ancient temple stone carvings.</li>
          <li><strong>4. Annakshetra (Free Community Dining Hall):</strong> Serving satvik Mahaprasadam meals free of cost to over 5,000 pilgrims daily between 12:00 PM and 03:00 PM.</li>
          <li><strong>5. Mumukshu Bhawan:</strong> Specialized stay facilities for elderly devotees seeking spiritual retirement in Kashi.</li>
          <li><strong>6. Ganga View Gallery & Escalator Ramp:</strong> Multi-tiered observation deck offering panoramic views of the river Ganga, equipped with escalators and ramps for senior citizens.</li>
          <li><strong>7. Bharat Mata Mandir & Marble Murals:</strong> Carved marble panels depicting major 12 Jyotirlingas, 51 Shaktipeeths, and Ramayana heritage sites.</li>
        </ul>
      </div>

      <!-- KASHI FOOD, CULTURE & CRAFT SHOPPING ENCYCLOPEDIA -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">9. Banaras Culinary Map & Heritage Handicraft Shopping Guide</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">No visit to Kashi is complete without relishing authentic Banarasi satvik street food delicacies and exploring centuries-old artisanal craft markets in Vishwanath Gali and Thatheri Gali.</p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
          <div>
            <h4 style="font-size: 1.25rem; color: #78350f; margin-bottom: 10px;">Iconic Banarasi Culinary Delicacies:</h4>
            <ul style="color: #4b5563; line-height: 1.8;">
              <li><strong>Kachori Sabzi & Jalebi:</strong> Morning breakfast benchmark served in Kulhad (earthen clay cups) at Ram Bhandar (Thatheri Gali) and Chachi Ki Kachori (Lanka).</li>
              <li><strong>Malaiyyo (Winter Foamed Milk Dessert):</strong> Light, saffron-infused milk foam garnished with pistachios and almonds, available exclusively during winter months (Nov to Feb) at Chaukhamba and Chowk.</li>
              <li><strong>Tamatar Chaat & Palak Chaat:</strong> Tangy, spicy mashed tomato curry served hot in Kulhad with ghee and crispy Sev at Kashi Chat Bhandar (Godowlia).</li>
              <li><strong>Banarasi Rabri Lassi:</strong> Thick churned curd topped with a thick slab of Rabri, Malai, and Rose syrup served at Blue Lassi Shop (Kunj Gali) and Pehalwan Lassi (Lanka).</li>
              <li><strong>Authentic Banarasi Meetha Paan:</strong> Betel leaf filled with Gulkand, Saunf, Menthol, and Tutti Frutti at Keshav Paan Bhandar.</li>
            </ul>
          </div>
          <div>
            <h4 style="font-size: 1.25rem; color: #78350f; margin-bottom: 10px;">Geographical Indication (GI) Handicraft Markets:</h4>
            <ul style="color: #4b5563; line-height: 1.8;">
              <li><strong>Banarasi Silk Sarees (GI Tagged):</strong> Handloom woven Pure Katan Silk, Georgette, Organza, and Zari Brocade sarees. Authentic government-certified shops are located at Chowk, Godowlia, and Madanpura.</li>
              <li><strong>Gulabi Meenakari (Pink Enamel Art):</strong> Unique pink enamel work on silver and gold metal crafts done by master artisans in Gai Ghat and Thatheri Gali.</li>
              <li><strong>Wooden Lacquerware Toys of Khojwa:</strong> Hand-turned eco-friendly wooden toys, spin tops, and idol figurines from Khojwa craft cluster.</li>
              <li><strong>Brassware & Rudraksha Malas:</strong> Authentic Panchdhatu idols, brass lamps, and lab-certified 1 to 14 Mukhi Rudraksha beads available in Vishwanath Gali.</li>
            </ul>
          </div>
        </div>
      </div>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

if "<!-- SACRED GEOGRAPHY & 84 GHATS HERITAGE ENCYCLOPEDIA -->" not in content:
    target = '<!-- EXPANDED PILGRIMAGE FAQS -->'
    if target in content:
        content = content.replace(target, extra_content + "\n" + target)
    else:
        content += extra_content

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

text_only = re.sub('<[^<]+?>', ' ', content)
words = len(text_only.split())
print(f"Updated index.html word count: {words} words")
