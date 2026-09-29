#!/usr/bin/env python3
"""
Varanasi / Kashi / Banaras SEO Rank Booster Script:
Hyper-optimizes all Varanasi/Kashi/Banaras pages with the complete 2,230+ keyword cluster:
- index.html
- varanasi-tour-package.html
- varanasi-guide.html
- blog-varanasi-kashi-vishwanath-vip-darshan-guide.html
- blog-kashi-vishwanath-corridor-tourist-guide.html
- blog-kashi-vishwanath-vip-darshan-booking-guide.html
- blog-varanasi-dev-deepawali-boat-booking-guide.html
- blog-varanasi-ganga-aarti-vip-boat-booking.html
- blog-varanasi-ganga-cruise-booking-guide.html
- blog-varanasi-to-gaya-pind-daan-tour-guide.html
- blog-varanasi-same-day-tour-package.html
- blog.html
"""

import os
import re
import json

def get_varanasi_keywords():
    transcript_path = '/Users/rishabhjaiswal/.gemini/antigravity/brain/ccc2ea79-0ed2-4269-a657-8551ea40bb5d/.system_generated/logs/transcript_full.jsonl'
    keywords = set()
    ignore_patterns = ['<USER_REQUEST>', '</USER_REQUEST>', '<ADDITIONAL_METADATA>', '</ADDITIONAL_METADATA>', 'https://', 'The current local time', 'isko', 'ya ispar lago', 'home page']

    if os.path.exists(transcript_path):
        with open(transcript_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get('type') == 'USER_INPUT':
                        content = data.get('content', '')
                        if 'https://www.kashidharshan.com/varanasi-tour-package' in content:
                            for l in content.splitlines():
                                l_str = l.strip()
                                if l_str and not any(p in l_str for p in ignore_patterns):
                                    keywords.add(l_str)
                except Exception:
                    continue

    print(f"Extracted {len(keywords)} Varanasi/Kashi/Banaras keywords from transcript.")
    return sorted(list(keywords))

def boost_page(filepath, keywords_list, section_title, knows_about_items):
    if not os.path.exists(filepath):
        print(f"File missing: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update <meta name="keywords">
    meta_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]*)"', content, re.IGNORECASE)
    existing_meta_kw = []
    if meta_match:
        existing_meta_kw = [k.strip() for k in meta_match.group(1).split(',') if k.strip()]

    combined_meta_kw = list(existing_meta_kw)
    seen_lower = {k.lower() for k in existing_meta_kw}

    added = 0
    for kw in keywords_list:
        if kw.lower() not in seen_lower:
            seen_lower.add(kw.lower())
            combined_meta_kw.append(kw)
            added += 1

    new_meta_str = ', '.join(combined_meta_kw)
    if meta_match:
        content = re.sub(
            r'<meta\s+name="keywords"\s+content="[^"]*"',
            f'<meta name="keywords" content="{new_meta_str}"',
            content,
            flags=re.IGNORECASE
        )
    else:
        content = content.replace('</head>', f'  <meta name="keywords" content="{new_meta_str}">\n</head>', 1)

    # 2. Add or update searchIndexSection
    pill_style = 'background: rgba(255,107,0,0.06); border: 1px solid rgba(212,175,55,0.25); border-radius: 20px; padding: 4px 12px; font-size: 0.82rem; color: var(--maroon); display: inline-block; white-space: nowrap;'
    sorted_pills = sorted(keywords_list)
    pills_html = '\n        '.join([f'<span style="{pill_style}">{kw}</span>' for kw in sorted_pills])

    search_section_html = f'''
<section class="section search-index-section" style="background: var(--paper-2); padding: 32px 0; border-top: 1px solid rgba(212,175,55,0.25);">
  <div class="container" style="max-width: 1100px; margin: 0 auto; padding: 0 16px;">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; flex-wrap: wrap; gap: 10px;">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--saffron-deep);"></span>
        <h3 style="color: var(--maroon); font-size: 1.1rem; margin: 0; font-family: var(--font-display); font-weight: 600; letter-spacing: 0.3px;">{section_title} ({len(sorted_pills)} Topics)</h3>
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

    if 'id="searchIndexContainer"' in content:
        content = re.sub(
            r'<section class="section search-index-section".*?</script>',
            search_section_html.strip(),
            content,
            flags=re.DOTALL
        )
    else:
        footer_pos = content.find('<footer')
        if footer_pos != -1:
            content = content[:footer_pos] + search_section_html + '\n' + content[footer_pos:]

    # 3. Enrich JSON-LD Schema
    knows_str = ', '.join([f'"{item}"' for item in knows_about_items])
    if '"knowsAbout"' not in content:
        for stype in ['"TravelAgency"', '"WebPage"', '"TouristTrip"', '"BlogPosting"', '"Article"']:
            if f'"@type": {stype}' in content:
                content = content.replace(
                    f'"@type": {stype},',
                    f'"@type": {stype},\n  "knowsAbout": [{knows_str}],',
                    1
                )
                break

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Rank-boosted {os.path.basename(filepath)} with {len(keywords_list)} Varanasi/Kashi keywords!")

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    kws = get_varanasi_keywords()
    
    if not kws:
        print("No keywords found!")
        return

    varanasi_knows_about = [
        "Varanasi Tour Package", "Kashi Vishwanath VIP Sugam Darshan", "Dashashwamedh Ganga Aarti Boat Tour",
        "Banaras Ghats Heritage Walk", "Sarnath Buddhist Tour", "Varanasi Local Sightseeing Taxi",
        "Banarasi Saree Shopping Market", "Varanasi Street Food Tour", "Kaal Bhairav Mandir Darshan",
        "Assi Ghat Subah-e-Banaras", "Dev Deepawali Boat Booking", "Varanasi Gaya Pind Daan Package"
    ]

    target_files = [
        'index.html',
        'varanasi-tour-package.html',
        'varanasi-guide.html',
        'blog-varanasi-kashi-vishwanath-vip-darshan-guide.html',
        'blog-kashi-vishwanath-corridor-tourist-guide.html',
        'blog-kashi-vishwanath-vip-darshan-booking-guide.html',
        'blog-varanasi-dev-deepawali-boat-booking-guide.html',
        'blog-varanasi-ganga-aarti-vip-boat-booking.html',
        'blog-varanasi-ganga-cruise-booking-guide.html',
        'blog-varanasi-to-gaya-pind-daan-tour-guide.html',
        'blog-varanasi-same-day-tour-package.html'
    ]

    for fname in target_files:
        fpath = os.path.join(root_dir, fname)
        title = f"{fname.replace('.html', '').replace('-', ' ').title()} - Varanasi, Kashi & Banaras Topics"
        boost_page(fpath, kws, title, varanasi_knows_about)

if __name__ == '__main__':
    main()
