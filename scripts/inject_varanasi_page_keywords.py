#!/usr/bin/env python3
"""
Inject target Varanasi keywords into varanasi-tour-package.html:
- Updates <meta name="keywords">
- Fixes any accidental leftover Ayodhya schema strings
- Adds searchIndexSection before <footer> with expandable keyword pills
- Enriches Schema JSON-LD knowsAbout array
"""

import os
import re

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_path = os.path.join(root_dir, 'varanasi-tour-package.html')
    raw_file = os.path.join(root_dir, 'varanasi_keywords_raw_full.txt')

    if not os.path.exists(raw_file):
        raw_file = os.path.join(root_dir, 'varanasi_keywords_raw.txt')

    if not os.path.exists(raw_file):
        print(f"Error: {raw_file} not found!")
        return

    with open(raw_file, 'r', encoding='utf-8') as f:
        raw_lines = f.readlines()

    ignore_patterns = ['<USER_REQUEST>', '</USER_REQUEST>', '<ADDITIONAL_METADATA>', '</ADDITIONAL_METADATA>', 'https://', 'ya ispar lago', 'The current local time']
    
    new_keywords = []
    seen_raw = set()
    for line in raw_lines:
        kw = line.strip()
        if not kw:
            continue
        if any(p in kw for p in ignore_patterns):
            continue
        if kw.lower() not in seen_raw:
            seen_raw.add(kw.lower())
            new_keywords.append(kw)

    print(f"Extracted {len(new_keywords)} unique keywords from raw file.")

    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix leftover Ayodhya mentions in varanasi-tour-package.html schema
    content = content.replace("guided Ram Mandir darshan, stays, and Saryu Aarti.", "guided Kashi Vishwanath VIP Darshan, stays, Ganga Aarti boat ride & Sarnath sightseeing.")
    content = content.replace("Plan a perfect 3-Day family trip to Ayodhya. Package includes premium hotel stays, private AC cab, guided Ram Mandir darshan, Kanak Bhawan, and Saryu Aarti.", "Plan a perfect 3-Day family trip to Varanasi & Kashi. Package includes premium hotel stays, private AC cab, guided Kashi Vishwanath VIP Darshan, Dashashwamedh Ganga Aarti boat ride, and Sarnath tour.")
    content = content.replace("How many days are recommended for Ayodhya Darshan?", "How many days are recommended for Varanasi Kashi Darshan?")
    content = content.replace("A 3-Day / 2-Night tour is highly recommended to explore Ram Janmabhoomi", "A 3-Day / 2-Night tour is highly recommended to explore Kashi Vishwanath Dham, Ganga Ghats, Sarnath, and local heritage")

    # 2. Update <meta name="keywords">
    meta_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]*)"', content, re.IGNORECASE)
    existing_meta_kw = []
    if meta_match:
        existing_meta_kw = [k.strip() for k in meta_match.group(1).split(',') if k.strip()]

    combined_meta_kw = list(existing_meta_kw)
    seen_lower = {k.lower() for k in existing_meta_kw}

    added_to_meta = 0
    for kw in new_keywords:
        if kw.lower() not in seen_lower:
            seen_lower.add(kw.lower())
            combined_meta_kw.append(kw)
            added_to_meta += 1

    new_meta_str = ', '.join(combined_meta_kw)
    content = re.sub(
        r'<meta\s+name="keywords"\s+content="[^"]*"',
        f'<meta name="keywords" content="{new_meta_str}"',
        content,
        flags=re.IGNORECASE
    )
    print(f"Added {added_to_meta} keywords to <meta name=\"keywords\">. Total keywords in meta tag: {len(combined_meta_kw)}")

    # 3. Build or update searchIndexSection
    pill_style = 'background: rgba(255,107,0,0.06); border: 1px solid rgba(212,175,55,0.25); border-radius: 20px; padding: 4px 12px; font-size: 0.82rem; color: var(--maroon); display: inline-block; white-space: nowrap;'
    
    sorted_pills = sorted(new_keywords)
    pills_html = '\n        '.join([f'<span style="{pill_style}">{kw}</span>' for kw in sorted_pills])

    search_section_html = f'''
<section class="section search-index-section" style="background: var(--paper-2); padding: 32px 0; border-top: 1px solid rgba(212,175,55,0.25);">
  <div class="container" style="max-width: 1100px; margin: 0 auto; padding: 0 16px;">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; flex-wrap: wrap; gap: 10px;">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--saffron-deep);"></span>
        <h3 style="color: var(--maroon); font-size: 1.1rem; margin: 0; font-family: var(--font-display); font-weight: 600; letter-spacing: 0.3px;">Varanasi, Banaras &amp; Kashi Tour, Temple &amp; Travel Index ({len(sorted_pills)} Topics)</h3>
      </div>
      <button id="toggleSearchIndexBtn" onclick="toggleSearchIndex()" style="background: transparent; border: 1px solid rgba(212,175,55,0.4); border-radius: 20px; padding: 6px 16px; font-size: 0.85rem; color: var(--maroon); cursor: pointer; display: flex; align-items: center; gap: 6px; font-weight: 500;">
        <span>Expand Search Index</span>
        <svg id="toggleSearchIndexIcon" style="width: 14px; height: 14px; fill: currentColor; transition: transform 0.3s ease;" viewBox="0 0 24 24"><path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6z"/></svg>
      </button>
    </div>
    
    <div id="searchIndexContainer" style="max-height: 82px; overflow: hidden; transition: max-height 0.4s ease; position: relative;">
      <div style="display: flex; flex-wrap: wrap; gap: 6px;">
        {pills_html}
      </div>
    </div>
  </div>
</section>

<script>
function toggleSearchIndex() {{
  const container = document.getElementById('searchIndexContainer');
  const btnText = document.querySelector('#toggleSearchIndexBtn span');
  const icon = document.getElementById('toggleSearchIndexIcon');
  
  if (!container.style.maxHeight || container.style.maxHeight === '82px') {{
    container.style.maxHeight = '5000px';
    btnText.textContent = 'Collapse Search Index';
    icon.style.transform = 'rotate(180deg)';
  }} else {{
    container.style.maxHeight = '82px';
    btnText.textContent = 'Expand Search Index';
    icon.style.transform = 'rotate(0deg)';
  }}
}}
</script>
'''

    # Insert section before <footer> if not already present, or update existing searchIndexContainer
    if 'id="searchIndexContainer"' in content:
        content = re.sub(
            r'<section class="section search-index-section".*?</script>',
            search_section_html.strip(),
            content,
            flags=re.DOTALL
        )
        print("Updated existing searchIndexSection on varanasi-tour-package.html")
    else:
        footer_pos = content.find('<footer')
        if footer_pos != -1:
            content = content[:footer_pos] + search_section_html + '\n' + content[footer_pos:]
            print("Inserted searchIndexSection before <footer> on varanasi-tour-package.html")
        else:
            print("Warning: <footer> tag not found!")

    # 4. Enrich Schema JSON-LD with knowsAbout / keywords
    knows_about_items = [
        "Varanasi Tour Package", "Kashi Vishwanath VIP Sugam Darshan", "Dashashwamedh Ganga Aarti Boat Tour",
        "Sarnath Buddhist Tour", "Assi Ghat Subah-e-Banaras", "Varanasi Local Sightseeing Taxi",
        "Banarasi Saree Shopping", "Varanasi Food Tour", "Kaal Bhairav Mandir Darshan"
    ]
    knows_str = ', '.join([f'"{item}"' for item in knows_about_items])

    if '"@type": "TouristTrip"' in content and '"knowsAbout"' not in content:
        content = content.replace(
            '"@type": "TouristTrip",',
            f'"@type": "TouristTrip",\n  "knowsAbout": [{knows_str}],',
            1
        )
        print("Added knowsAbout array to TouristTrip schema.")

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated varanasi-tour-package.html!")

    # Cleanup temporary raw files
    for rf in [os.path.join(root_dir, 'varanasi_keywords_raw.txt'), os.path.join(root_dir, 'varanasi_keywords_raw_full.txt')]:
        if os.path.exists(rf):
            os.remove(rf)

if __name__ == '__main__':
    main()
