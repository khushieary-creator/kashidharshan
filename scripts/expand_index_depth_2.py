import re

extra_content_2 = """
      <!-- PANCHKROSHI PARIKRAMA, BHAIRAVAS & SARNATH DEEP HERITAGE ENCYCLOPEDIA -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">10. Sacred Panchkroshi Yatra, Ashta Bhairava & Nav Durga Temples of Kashi</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">Beyond the main Kashi Vishwanath temple, classical Hindu scriptures describe the sacred 55-mile <strong>Panchkroshi Parikrama</strong> — a 5-day walking pilgrimage encircling 108 holy shrines around the outer perimeter of Kashi Dham.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 20px;">
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 18px; border-radius: 10px;">
            <h4 style="color: #78350f; font-size: 1.15rem; margin-bottom: 8px;">The 5 Stops (Halts) of Panchkroshi Yatra:</h4>
            <ol style="color: #4b5563; line-height: 1.7; padding-left: 18px;">
              <li><strong>Kardameshwar Mahadev (Kandwa):</strong> The first halt housing a 12th-century stone temple built by the Gahadavala dynasty.</li>
              <li><strong>Bhimchandi Devi (Bhimchandi):</strong> The second halt dedicated to Goddess Durga defeating demon Durgamasura.</li>
              <li><strong>Rameshwar Mahadev (Rameshwar):</strong> Located on the banks of Varuna River, housing Shivalingas installed by Lord Ram.</li>
              <li><strong>Shivpur (5 Shiv Shrines):</strong> The fourth halt featuring Sri Pancha Pandava Mandir.</li>
              <li><strong>Kapildhara (Rajghat):</strong> The final halt where pilgrims complete ritual offerings before concluding at Manikarnika.</li>
            </ol>
          </div>

          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 18px; border-radius: 10px;">
            <h4 style="color: #78350f; font-size: 1.15rem; margin-bottom: 8px;">Ashta Bhairava (8 Guardian Deities of Kashi):</h4>
            <p style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;">According to Kashi Khanda, 8 forms of Lord Bhairava protect the 8 cardinal directions of Kashi. Seeking their blessings removes all fears and obstacles:</p>
            <ul style="font-size: 0.95rem; color: #4b5563; line-height: 1.6;">
              <li><strong>Ruru Bhairava:</strong> Hanuman Ghat</li>
              <li><strong>Chanda Bhairava:</strong> Durga Kund</li>
              <li><strong>Asitanga Bhairava:</strong> Vriddhakaleshwar</li>
              <li><strong>Kroda Bhairava:</strong> Kamachha</li>
              <li><strong>Unmatta Bhairava:</strong> Deora Village</li>
              <li><strong>Kapala Bhairava:</strong> Lati Bhairav</li>
              <li><strong>Bhishana Bhairava:</strong> Bhoot Bhairav</li>
              <li><strong>Samhara Bhairava:</strong> Gaibi Ghat</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- SARNATH COMPLETE BUDDHIST & ARCHAEOLOGICAL ENCYCLOPEDIA -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">11. Sarnath Buddhist Heritage Circuit & Archaeological Monuments</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">Located just 10 km northeast of Kashi Vishwanath Temple, <strong>Sarnath (Isipatana)</strong> is one of the four most sacred Buddhist pilgrimage destinations in the world. It is here in the Deer Park (Rishipatana) that Lord Buddha preached his first sermon after attaining enlightenment at Bodhgaya, turning the Wheel of Law (Dharmachakra Pravartana).</p>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">Major Monuments & Attractions in Sarnath:</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Dhamek Stupa:</strong> Massive 43.6-meter tall cylindrical stone stupa built by Emperor Ashoka in 249 BCE to mark the exact spot of Buddha's first sermon. Features exquisite Gupta-era stone carvings.
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Sarnath Archaeological Museum:</strong> Housing India's National Emblem — the original 3rd century BCE polished sandstone Ashoka Lion Capital, along with 5th century preaching Buddha statues.
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Chaukhandi Stupa:</strong> An imposing 5th-century Gupta-period terraced brick monument topped with an octagonal Mughal tower constructed by Todar Mal's son Govardhan to commemorate Emperor Humayun's visit.
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 15px; border-radius: 8px;">
            <strong style="color: #78350f;">Mulagandha Kuti Vihar & Thai Temple:</strong> Modern Buddhist temple featuring colorful frescoes painted by Japanese artist Kosetsu Nosu, housing sacred Buddha relics, surrounded by international monasteries from Thailand, Japan, Tibet, and Sri Lanka.
          </div>
        </div>
      </div>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

if "<!-- PANCHKROSHI PARIKRAMA, BHAIRAVAS & SARNATH DEEP HERITAGE ENCYCLOPEDIA -->" not in content:
    target = '<!-- BANARAS CULINARY MAP & HERITAGE HANDICRAFT SHOPPING GUIDE -->'
    if target in content:
        content = content.replace(target, extra_content_2 + "\n" + target)
    else:
        content += extra_content_2

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

text_only = re.sub('<[^<]+?>', ' ', content)
words = len(text_only.split())
print(f"Final expanded index.html word count: {words} words")
