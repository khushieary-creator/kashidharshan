import re

extra_content_5 = """
      <!-- EMERGENCY HELPLINES & KASHI DHARSHAN GUARANTEE ENCYCLOPEDIA -->
      <div style="background: #ffffff; border: 1px solid #f3e8ff; border-radius: 16px; padding: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
        <h3 style="font-family: var(--font-display, serif); font-size: 1.8rem; color: #4a0404; margin-bottom: 24px; border-bottom: 2px solid #fde68a; padding-bottom: 10px;">15. Kashi Tourist Police, Emergency Helplines & Local Assistance</h3>
        
        <p style="color: #374151; line-height: 1.7; margin-bottom: 16px;">To ensure a safe, hassle-free, and spiritually enriching experience for pilgrims from all corners of India and overseas, Varanasi Administration operates dedicated Tourist Assistance Booths across major transit hubs.</p>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">Important Emergency Contact Numbers & Tourist Help Desks:</h4>
        <ul style="color: #4b5563; line-height: 1.8; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px;">
          <li><strong>Varanasi Tourist Helpline:</strong> 1800-180-5145 (Toll-Free 24x7)</li>
          <li><strong>Kashi Tourist Police Station (Dashashwamedh):</strong> +91-542-2450001</li>
          <li><strong>Shri Kashi Vishwanath Temple Control Room:</strong> +91-542-2392600</li>
          <li><strong>Lal Bahadur Shastri Airport Tourist Counter:</strong> +91-542-2622155</li>
          <li><strong>Kashi Dharshan Direct Local Yatra Helpline:</strong> +91-7408763401 / WhatsApp Assistance</li>
        </ul>

        <h4 style="font-size: 1.25rem; color: #78350f; margin: 20px 0 10px;">The Kashi Dharshan Yatra Commitment:</h4>
        <p style="color: #4b5563; line-height: 1.7;">When you book your Varanasi yatra with Kashi Dharshan, we guarantee 100% transparent pricing with no hidden charges, verified luxury/deluxe hotel stays with 24-hour hot water and satvik dining, polite and knowledgeable local pandit guides, private sanitized AC cabs with experienced drivers, and dedicated on-ground yatra managers to assist senior citizens at every step of your divine trip.</p>
      </div>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

if "<!-- EMERGENCY HELPLINES & KASHI DHARSHAN GUARANTEE ENCYCLOPEDIA -->" not in content:
    target = '<!-- EXHAUSTIVE KASHI VISHWANATH YATRA FAQS -->'
    if target in content:
        content = content.replace(target, extra_content_5 + "\n" + target)
    else:
        content += extra_content_5

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

text_only = re.sub('<[^<]+?>', ' ', content)
words = len(text_only.split())
print(f"Final index.html word count after expansion 5: {words} words")
