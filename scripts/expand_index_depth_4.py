import re

extra_content_4 = """
      <!-- KASHI YATRA TRAVEL CHECKLIST, PACKING & WEATHER ENCYCLOPEDIA -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">14. Kashi Yatra Weather Chart, Packing Checklist & Visitor Guidelines</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">Preparing for your pilgrimage to Varanasi requires understanding the seasonal climate variations and carrying suitable attire for sacred temple visits and boat rides on the River Ganga.</p>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">Month-by-Month Weather & Tourism Season Guide:</h4>
        <div style="overflow-x: auto;">
          <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 0.95rem; text-align: left;">
            <thead>
              <tr style="background: #78350f; color: #ffffff;">
                <th style="padding: 10px; border: 1px solid #ddd;">Season & Months</th>
                <th style="padding: 10px; border: 1px solid #ddd;">Temperature Range</th>
                <th style="padding: 10px; border: 1px solid #ddd;">Weather Characteristics</th>
                <th style="padding: 10px; border: 1px solid #ddd;">Pilgrimage Suitability</th>
              </tr>
            </thead>
            <tbody>
              <tr style="background: #fffcf7;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Winter (Oct – Mar)</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">8°C to 25°C</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Pleasant, crisp mornings with early fog over the Ganges. Cool breeze during evening Aarti.</td>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Peak Season (10/10):</strong> Best time for Dev Deepawali, ghat walking, and boat rides. Heavy bookings required.</td>
              </tr>
              <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Summer (Apr – Jun)</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">28°C to 44°C</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Hot afternoons with strong Loo winds. Warm evenings.</td>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Off-Peak Season (7/10):</strong> Budget stays available. Early morning 05:00 AM darshan recommended.</td>
              </tr>
              <tr style="background: #fffcf7;">
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Monsoon (Jul – Sep)</strong></td>
                <td style="padding: 10px; border: 1px solid #ddd;">24°C to 34°C</td>
                <td style="padding: 10px; border: 1px solid #ddd;">Heavy rain showers. Water level in River Ganga rises, partially submerging lower ghat stairs.</td>
                <td style="padding: 10px; border: 1px solid #ddd;"><strong>Sawan Season (9/10):</strong> Sacred Sawan Yatra month. Boat rides operate with restricted motor limits during flood alert.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">Essential Packing Checklist for Kashi Pilgrims:</h4>
        <ul style="color: #4b5563; line-height: 1.8; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px;">
          <li><strong>Traditional Clothing:</strong> Cotton Dhoti-Kurta or Kurta-Pyjama for men; Sarees or Salwar Suits for women for temple Jalabhishekam.</li>
          <li><strong>Footwear:</strong> Easy slip-on sandals or cloth shoes (shoes must be removed frequently at ghats and temple locker gates).</li>
          <li><strong>Identity Proof:</strong> Original Aadhaar Card, Passport, or Voter ID for Kashi Vishwanath VIP ticket validation at Gate 2.</li>
          <li><strong>Winter Wear:</strong> Light woolens or jackets for morning sunrise boat rides between November and February.</li>
          <li><strong>Temple Travel Pouch:</strong> Small cloth pouch for carrying cash, Prasad, and locker key (as leather wallets are prohibited in inner sanctum).</li>
        </ul>
      </div>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

if "<!-- KASHI YATRA TRAVEL CHECKLIST, PACKING & WEATHER ENCYCLOPEDIA -->" not in content:
    target = '<!-- EXHAUSTIVE KASHI VISHWANATH YATRA FAQS -->'
    if target in content:
        content = content.replace(target, extra_content_4 + "\n" + target)
    else:
        content += extra_content_4

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

text_only = re.sub('<[^<]+?>', ' ', content)
words = len(text_only.split())
print(f"Final index.html word count after expansion 4: {words} words")
