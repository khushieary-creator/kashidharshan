#!/usr/bin/env python3
"""
SEO Blog Keyword Injector:
Extracts all targeted city keywords from transcript_full.jsonl and updates:
1. blog-varanasi-kashi-vishwanath-vip-darshan-guide.html
2. blog-vip-darshan-ayodhya-ram-mandir.html
3. blog-prayagraj-sangam-tour-guide.html
4. blog-chitrakoot-ram-vanvas-tour-guide.html
5. blog-naimisharanya-chakra-tirth-guide.html
6. blog-vindhyachal-trikon-parikrama-guide.html
7. blog-mathura-vrindavan-vip-darshan-guide.html
8. blog.html
"""

import os
import re
import json

def extract_keywords_from_transcript():
    transcript_path = '/Users/rishabhjaiswal/.gemini/antigravity/brain/ccc2ea79-0ed2-4269-a657-8551ea40bb5d/.system_generated/logs/transcript_full.jsonl'
    
    city_keywords = {
        'varanasi': set(),
        'ayodhya': set(),
        'prayagraj': set(),
        'chitrakoot': set(),
        'naimisharanya': set(),
        'vindhyachal': set(),
        'mathura': set(),
        'vrindavan': set()
    }
    
    ignore_patterns = ['<USER_REQUEST>', '</USER_REQUEST>', '<ADDITIONAL_METADATA>', '</ADDITIONAL_METADATA>', 'https://', 'The current local time', 'isko', 'ya ispar lago', 'home page']

    if not os.path.exists(transcript_path):
        print(f"Error: {transcript_path} not found!")
        return city_keywords

    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('type') == 'USER_INPUT':
                    content = data.get('content', '')
                    lines = [l.strip() for l in content.splitlines() if l.strip()]
                    
                    target_city = None
                    if 'https://www.kashidharshan.com/varanasi-tour-package' in content:
                        target_city = 'varanasi'
                    elif 'https://www.kashidharshan.com/ayodhya-tour-package' in content:
                        target_city = 'ayodhya'
                    elif 'https://www.kashidharshan.com/prayagraj-tour-package' in content:
                        target_city = 'prayagraj'
                    elif 'https://www.kashidharshan.com/chitrakoot-tour-package' in content:
                        target_city = 'chitrakoot'
                    elif 'https://www.kashidharshan.com/naimisharanya-tour-package' in content:
                        target_city = 'naimisharanya'
                    elif 'https://www.kashidharshan.com/vindhyachal-tour-package' in content:
                        target_city = 'vindhyachal'
                    elif 'https://www.kashidharshan.com/mathura-tour-package' in content:
                        target_city = 'mathura'
                    elif 'https://www.kashidharshan.com/vrindavan-tour-package' in content:
                        target_city = 'vrindavan'
                    
                    if target_city:
                        for l in lines:
                            if any(p in l for p in ignore_patterns):
                                continue
                            city_keywords[target_city].add(l)
            except Exception as e:
                continue

    return city_keywords

def update_blog_file(file_path, keywords_list, title_heading, knows_about_list):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update <meta name="keywords">
    meta_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]*)"', content, re.IGNORECASE)
    existing_meta_kw = []
    if meta_match:
        existing_meta_kw = [k.strip() for k in meta_match.group(1).split(',') if k.strip()]

    combined_meta_kw = list(existing_meta_kw)
    seen_lower = {k.lower() for k in existing_meta_kw}

    added_to_meta = 0
    for kw in keywords_list:
        if kw.lower() not in seen_lower:
            seen_lower.add(kw.lower())
            combined_meta_kw.append(kw)
            added_to_meta += 1

    new_meta_str = ', '.join(combined_meta_kw)
    if meta_match:
        content = re.sub(
            r'<meta\s+name="keywords"\s+content="[^"]*"',
            f'<meta name="keywords" content="{new_meta_str}"',
            content,
            flags=re.IGNORECASE
        )
    else:
        # Insert meta keywords in <head>
        content = content.replace('</head>', f'  <meta name="keywords" content="{new_meta_str}">\n</head>', 1)

    print(f"Updated {os.path.basename(file_path)}: Added {added_to_meta} keywords to meta tag. Total meta keywords: {len(combined_meta_kw)}")

    # 2. Build or update searchIndexSection
    pill_style = 'background: rgba(255,107,0,0.06); border: 1px solid rgba(212,175,55,0.25); border-radius: 20px; padding: 4px 12px; font-size: 0.82rem; color: var(--maroon); display: inline-block; white-space: nowrap;'
    
    sorted_pills = sorted(keywords_list)
    pills_html = '\n        '.join([f'<span style="{pill_style}">{kw}</span>' for kw in sorted_pills])

    search_section_html = f'''
<section class="section search-index-section" style="background: var(--paper-2); padding: 32px 0; border-top: 1px solid rgba(212,175,55,0.25);">
  <div class="container" style="max-width: 1100px; margin: 0 auto; padding: 0 16px;">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; flex-wrap: wrap; gap: 10px;">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--saffron-deep);"></span>
        <h3 style="color: var(--maroon); font-size: 1.1rem; margin: 0; font-family: var(--font-display); font-weight: 600; letter-spacing: 0.3px;">{title_heading} ({len(sorted_pills)} Topics)</h3>
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
    container.style.maxHeight = '4000px';
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

    # 3. Enrich Schema JSON-LD with knowsAbout
    knows_str = ', '.join([f'"{item}"' for item in knows_about_list])

    if '"knowsAbout"' not in content:
        if '"@type": "BlogPosting"' in content:
            content = content.replace(
                '"@type": "BlogPosting",',
                f'"@type": "BlogPosting",\n  "knowsAbout": [{knows_str}],',
                1
            )
        elif '"@type": "Article"' in content:
            content = content.replace(
                '"@type": "Article",',
                f'"@type": "Article",\n  "knowsAbout": [{knows_str}],',
                1
            )
        elif '"@type": "WebPage"' in content:
            content = content.replace(
                '"@type": "WebPage",',
                f'"@type": "WebPage",\n  "knowsAbout": [{knows_str}],',
                1
            )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    city_keywords = extract_keywords_from_transcript()
    
    for city, kws in city_keywords.items():
        print(f"Extracted {len(kws)} keywords for {city}")

    # Mapping of city to blog file
    blogs_map = [
        (
            os.path.join(root_dir, 'blog-varanasi-kashi-vishwanath-vip-darshan-guide.html'),
            list(city_keywords['varanasi']),
            "Varanasi & Kashi Vishwanath Yatra Guide Topics",
            ["Varanasi Kashi Vishwanath VIP Darshan", "Dashashwamedh Ganga Aarti Boat Tour", "Sarnath Sightseeing", "Varanasi Local Guide"]
        ),
        (
            os.path.join(root_dir, 'blog-vip-darshan-ayodhya-ram-mandir.html'),
            list(city_keywords['ayodhya']),
            "Ayodhya Ram Mandir VIP Darshan Guide Topics",
            ["Ayodhya Ram Mandir VIP Pass", "Hanuman Garhi Darshan", "Kanak Bhawan Sightseeing", "Saryu River Aarti"]
        ),
        (
            os.path.join(root_dir, 'blog-prayagraj-sangam-tour-guide.html'),
            list(city_keywords['prayagraj']),
            "Prayagraj Triveni Sangam Yatra Guide Topics",
            ["Prayagraj Triveni Sangam Boat Ride", "Lete Hue Hanuman Ji Mandir", "Alopi Devi Shaktipeeth", "Anand Bhawan"]
        ),
        (
            os.path.join(root_dir, 'blog-chitrakoot-ram-vanvas-tour-guide.html'),
            list(city_keywords['chitrakoot']),
            "Chitrakoot Ram Vanvas Guide Topics",
            ["Chitrakoot Kamadgiri Parikrama", "Ramghat Mandakini Aarti", "Gupt Godavari Caves", "Hanuman Dhara Waterfall"]
        ),
        (
            os.path.join(root_dir, 'blog-naimisharanya-chakra-tirth-guide.html'),
            list(city_keywords['naimisharanya']),
            "Naimisharanya Chakra Tirth Guide Topics",
            ["Naimisharanya Chakra Tirth Snan", "Maa Lalita Devi Shaktipeeth", "Maharishi Ved Vyas Gaddi", "Dadhichi Kund"]
        ),
        (
            os.path.join(root_dir, 'blog-vindhyachal-trikon-parikrama-guide.html'),
            list(city_keywords['vindhyachal']),
            "Vindhyachal Trikon Parikrama Guide Topics",
            ["Maa Vindhyavasini Shaktipeeth", "Kali Khoh Devi Temple", "Ashtabhuja Devi Mandir", "Vindhyachal Trikon Parikrama"]
        ),
        (
            os.path.join(root_dir, 'blog-mathura-vrindavan-vip-darshan-guide.html'),
            list(city_keywords['mathura'] | city_keywords['vrindavan']),
            "Mathura & Vrindavan Yatra Guide Topics",
            ["Shri Krishna Janmabhoomi Mathura", "Shri Banke Bihari Mandir Vrindavan", "Prem Mandir Light Show", "Govardhan Parikrama"]
        ),
    ]

    for blog_path, kws, title, knows_about in blogs_map:
        if kws:
            update_blog_file(blog_path, kws, title, knows_about)

    # Now update main blog.html directory with all combined keywords
    all_combined_kws = set()
    for kws in city_keywords.values():
        all_combined_kws.update(kws)

    blog_hub_path = os.path.join(root_dir, 'blog.html')
    if os.path.exists(blog_hub_path) and all_combined_kws:
        update_blog_file(
            blog_hub_path,
            list(all_combined_kws),
            "All Uttar Pradesh Sacred Yatra & Temple Guides Index",
            ["Uttar Pradesh Sacred Yatra", "Varanasi Kashi Vishwanath VIP Darshan", "Ayodhya Ram Mandir VIP Pass", "Prayagraj Triveni Sangam", "Mathura Vrindavan Tour"]
        )
        print(f"Updated main blog.html with {len(all_combined_kws)} combined keywords!")

if __name__ == '__main__':
    main()
