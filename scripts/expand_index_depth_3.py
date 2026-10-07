import re

extra_content_3 = """
      <!-- SAWAN YATRA & MOKSHA RITUAL SERVICES ENCYCLOPEDIA -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">12. Sawan Month Kanwar Yatra & Maha Shivratri Festival Guide</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">The holy month of <strong>Shravan (Sawan)</strong> and the auspicious festival of <strong>Maha Shivratri</strong> witness the highest influx of Shiva devotees (Kanwariyas) visiting Kashi Vishwanath Dham. Over 5 million pilgrims perform Jalabhishekam with holy Ganga water brought on foot from Sultanganj or Gaumukh.</p>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">Sawan Monday Special Darshan Rules & Entry Channels:</h4>
        <ul style="color: #4b5563; line-height: 1.8;">
          <li><strong>24-Hour Continuous Darshan:</strong> On Sawan Mondays, temple doors remain open continuously for 24 hours except during specific Aarti breaks.</li>
          <li><strong>Special Jhanki Darshan:</strong> Due to extreme crowds, Sparsh Darshan (touching the Jyotirlinga) is suspended on Sawan Mondays. Devotees offer Ganga water through external copper pipes (Argha) leading directly to the sanctum.</li>
          <li><strong>Kanwariya Dedicated Corridor:</strong> Gate 4 (Ganga Riverfront Corridor Gate) is designated as the primary entry point for barefoot Kanwar yatris arriving directly after Ganga Snan.</li>
          <li><strong>Advance Sawan VIP Slot Booking:</strong> Special Sawan Sugam Darshan passes (priced at ₹500 - ₹750) can be booked up to 45 days prior through Kashi Dharshan packages.</li>
        </ul>
      </div>

      <!-- KASHI MOKSHA & ANCESTRAL RITUAL SERVICES GUIDE -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">13. Kashi Moksha & Ancestral Ritual Services (Pinda Daan & Asthi Visarjan)</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">In Hindu theology, performing ancestral rites (Shraddh Karma) in Kashi frees ancestors' souls from earthly bondage, granting them eternal peace and salvation. Kashi Dharshan provides certified Teerth Purohit (local Vedic Pandits) for performing sacred rituals at designated ghats.</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 16px; border-radius: 8px;">
            <strong style="color: #78350f;">1. Pinda Daan (Pitru Daan):</strong> Performed at Dashashwamedh Ghat or Manikarnika Ghat using rice balls (Pinda), sesame seeds, and sacred Ganga water under the guidance of authorized Kashi Purohits.
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 16px; border-radius: 8px;">
            <strong style="color: #78350f;">2. Asthi Visarjan (Immersion of Ashes):</strong> Immersing mortal remains in the holy River Ganga with Vedic mantras for supreme liberation of departed family members.
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 16px; border-radius: 8px;">
            <strong style="color: #78350f;">3. Tripindi Shraddh & Narayan Bali:</strong> Special Vedic Yajna performed at Panchganga Ghat or Pishach Mochan Kund to eradicate Pitru Dosh and ancestral karma.
          </div>
          <div style="background: #fffcf7; border: 1px solid #e5e7eb; padding: 16px; border-radius: 8px;">
            <strong style="color: #78350f;">4. Rudrabhishekam Yajna:</strong> Chanting of Sri Rudram by 5 or 11 Vedic Pandits inside Kashi Vishwanath Dham or private ghat mandapam for health, prosperity, and peace.
          </div>
        </div>
      </div>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

if "<!-- SAWAN YATRA & MOKSHA RITUAL SERVICES ENCYCLOPEDIA -->" not in content:
    target = '<!-- EXHAUSTIVE KASHI VISHWANATH YATRA FAQS -->'
    if target in content:
        content = content.replace(target, extra_content_3 + "\n" + target)
    else:
        content += extra_content_3

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

text_only = re.sub('<[^<]+?>', ' ', content)
words = len(text_only.split())
print(f"Final index.html word count after expansion 3: {words} words")
