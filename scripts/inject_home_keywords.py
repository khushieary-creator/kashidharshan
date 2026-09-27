#!/usr/bin/env python3
"""
Inject target user keywords into index.html:
- Updates <meta name="keywords">
- Updates #searchIndexContainer pills
- Enriches Schema JSON-LD knowsAbout array
"""

import os
import re

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(root_dir, 'index.html')
    raw_file = os.path.join(root_dir, 'user_keywords_raw.txt')

    if not os.path.exists(raw_file):
        print(f"Error: {raw_file} not found!")
        return

    with open(raw_file, 'r', encoding='utf-8') as f:
        raw_lines = f.readlines()

    new_keywords = []
    ignore_patterns = ['<USER_REQUEST>', '</USER_REQUEST>', '<ADDITIONAL_METADATA>', '</ADDITIONAL_METADATA>', 'home page', 'The current local time']
    
    for line in raw_lines:
        line_str = line.strip()
        if not line_str:
            continue
        if any(p in line_str for p in ignore_patterns):
            continue
        new_keywords.append(line_str)

    print(f"Extracted {len(new_keywords)} unique raw keywords from prompt.")

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update <meta name="keywords">
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
    print(f"Added {added_to_meta} keywords to <meta name=\"keywords\">. Total keywords: {len(combined_meta_kw)}")

    # 2. Update #searchIndexContainer pills
    pill_style = 'background: rgba(255,107,0,0.06); border: 1px solid rgba(212,175,55,0.25); border-radius: 20px; padding: 4px 12px; font-size: 0.82rem; color: var(--maroon); display: inline-block; white-space: nowrap;'
    
    # Extract existing pills inside searchIndexContainer
    search_container_match = re.search(r'(<div id="searchIndexContainer"[^>]*>.*?<div style="display: flex; flex-wrap: wrap; gap: 6px;">)(.*?)(</div>\s*</div>)', content, re.DOTALL)
    if search_container_match:
        header_part = search_container_match.group(1)
        pills_part = search_container_match.group(2)
        footer_part = search_container_match.group(3)

        existing_pills = re.findall(r'<span[^>]*>(.*?)</span>', pills_part, re.DOTALL)
        existing_pill_texts = [p.strip() for p in existing_pills if p.strip()]
        existing_pill_lower = {p.lower() for p in existing_pill_texts}

        added_pills = 0
        all_pills_texts = list(existing_pill_texts)
        for kw in new_keywords:
            if kw.lower() not in existing_pill_lower:
                existing_pill_lower.add(kw.lower())
                all_pills_texts.append(kw)
                added_pills += 1

        all_pills_texts.sort()
        new_pills_html = '\n        '.join(
            [f'<span style="{pill_style}">{kw}</span>' for kw in all_pills_texts]
        )

        new_container_html = f'{header_part}\n        {new_pills_html}\n      {footer_part}'
        content = re.sub(r'<div id="searchIndexContainer"[^>]*>.*?</div>\s*</div>', new_container_html, content, count=1, flags=re.DOTALL)
        print(f"Added {added_pills} pill tags to #searchIndexContainer. Total pills: {len(all_pills_texts)}")
    else:
        print("Warning: #searchIndexContainer not found in index.html!")

    # 3. Add knowsAbout to TravelAgency schema if missing
    knows_about_items = [
        "India Pilgrimage Tour", "Uttar Pradesh Dharmik Yatra", "Ayodhya Varanasi Prayagraj Tour",
        "Kashi Vishwanath VIP Sugam Darshan", "Dev Deepawali Boat Booking", "NRI Pilgrimage Tour Packages"
    ]
    knows_str = ', '.join([f'"{item}"' for item in knows_about_items])

    if '"@type": "TravelAgency"' in content and '"knowsAbout"' not in content:
        content = content.replace(
            '"@type": "TravelAgency",',
            f'"@type": "TravelAgency",\n      "knowsAbout": [{knows_str}],',
            1
        )
        print("Added knowsAbout array to TravelAgency schema.")

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully updated index.html!")

    # Remove temporary raw file if exists
    if os.path.exists(raw_file):
        os.remove(raw_file)

if __name__ == '__main__':
    main()
