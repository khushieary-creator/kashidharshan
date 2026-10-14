import os
import re
import glob

# Paths
ROOT_DIR = '/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan'

def extract_pills_from_file(filename):
    filepath = os.path.join(ROOT_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'id="searchIndexContainer"[^>]*>(.*?)</div>\s*</div>', content, re.DOTALL)
    if not m:
        raise ValueError(f"Could not find searchIndexContainer in {filename}")
    inner = m.group(1)
    spans = re.findall(r'<span[^>]*>(.*?)</span>', inner)
    return spans

def build_search_section(topic_title, keywords):
    count = len(keywords)
    pills_html = ' '.join([
        f'<span style="background:#fff8f0; border:1px solid #fed7aa; border-radius:14px; padding:3px 9px; font-size:11.5px; font-weight:500; color:#78350f; display:inline-block;">{kw}</span>'
        for kw in keywords
    ])
    
    return f'''
<!-- Search Index Cloud ({count} Topics) -->
<section class="section search-index-section" style="background: var(--paper-2); padding: 32px 0; border-top: 1px solid rgba(212,175,55,0.25);">
  <div class="container" style="max-width: 1100px; margin: 0 auto; padding: 0 16px;">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; flex-wrap: wrap; gap: 10px;">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--saffron-deep);"></span>
        <h3 style="color: var(--maroon); font-size: 1.1rem; margin: 0; font-family: var(--font-display); font-weight: 600; letter-spacing: 0.3px;">Index - {topic_title} ({count} Topics)</h3>
      </div>
      <button id="toggleSearchIndexBtn" onclick="toggleSearchIndex()" style="background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 20px; padding: 6px 16px; font-size: 0.85rem; color: #78350f; cursor: pointer; display: flex; align-items: center; gap: 6px; font-weight: 600; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <span>Expand Search Index ({count} Topics)</span>
        <svg id="toggleSearchIndexIcon" style="width: 14px; height: 14px; fill: currentColor; transition: transform 0.3s ease;" viewBox="0 0 24 24"><path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6z"/></svg>
      </button>
    </div>
    
    <div id="searchIndexContainer" style="max-height: 84px; overflow: hidden; transition: max-height 0.4s ease; position: relative;">
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px;">
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
  
  if (!container.style.maxHeight || container.style.maxHeight === '84px') {{
    container.style.maxHeight = '30000px';
    btnText.textContent = 'Collapse Search Index';
    icon.style.transform = 'rotate(180deg)';
  }} else {{
    container.style.maxHeight = '84px';
    btnText.textContent = 'Expand Search Index ({count} Topics)';
    icon.style.transform = 'rotate(0deg)';
  }}
}}
</script>
'''

def main():
    print("Extracting canonical keyword pools...")
    vns_kw = extract_pills_from_file('index.html')
    ayodhya_kw = extract_pills_from_file('ayodhya-tour-package.html')
    prayagraj_kw = extract_pills_from_file('prayagraj-tour-package.html')
    chitrakoot_kw = extract_pills_from_file('chitrakoot-tour-package.html')
    naimish_kw = extract_pills_from_file('naimisharanya-tour-package.html')
    vindhya_kw = extract_pills_from_file('vindhyachal-tour-package.html')
    mathura_kw = extract_pills_from_file('mathura-tour-package.html')
    vrindavan_kw = extract_pills_from_file('vrindavan-tour-package.html')
    general_kw = extract_pills_from_file('services.html')

    print(f"Varanasi: {len(vns_kw)}")
    print(f"Ayodhya: {len(ayodhya_kw)}")
    print(f"Prayagraj: {len(prayagraj_kw)}")
    print(f"Chitrakoot: {len(chitrakoot_kw)}")
    print(f"Naimisharanya: {len(naimish_kw)}")
    print(f"Vindhyachal: {len(vindhya_kw)}")
    print(f"Mathura: {len(mathura_kw)}")
    print(f"Vrindavan: {len(vrindavan_kw)}")
    print(f"General UP: {len(general_kw)}")

    # Step 1: Fix index.html placement
    # In index.html, remove the current search index cloud section and script, and place it right before <footer class="site-foot">
    index_file = os.path.join(ROOT_DIR, 'index.html')
    with open(index_file, 'r', encoding='utf-8') as f:
        idx_content = f.read()

    # Remove existing search-index-section and its script from index.html
    pattern_idx = r'<!-- Search Index Cloud \(\d+ Topics\) -->\s*<section class="section search-index-section".*?</script>'
    idx_content_cleaned = re.sub(pattern_idx, '', idx_content, flags=re.DOTALL)
    
    # Also clean up any loose comments
    idx_content_cleaned = re.sub(r'<!-- January 2026 High-Converting Google Ads Search Index Cloud -->\s*', '', idx_content_cleaned)

    # Insert right above <footer class="site-foot">
    vns_section = build_search_section("Varanasi, Kashi & Banaras Topics", vns_kw)
    if '<footer class="site-foot">' in idx_content_cleaned:
        idx_content_cleaned = idx_content_cleaned.replace('<footer class="site-foot">', vns_section + '\n<footer class="site-foot">')
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(idx_content_cleaned)
        print("Updated index.html: moved search index cloud right above footer.")
    else:
        print("Warning: could not find <footer class=\"site-foot\"> in index.html")

    # Step 2: Replace or inject into targeted blog and package pages
    # Mapping for files with 20 keywords:
    blog_fixes = [
        ('blog-prayagraj-sangam-tour-guide.html', "Prayagraj Sangam & Kumbh Topics", prayagraj_kw),
        ('blog-chitrakoot-ram-vanvas-tour-guide.html', "Chitrakoot Ram Vanvas Topics", chitrakoot_kw),
        ('blog-mathura-vrindavan-vip-darshan-guide.html', "Mathura & Vrindavan Topics", vrindavan_kw),
        ('blog-naimisharanya-chakra-tirth-guide.html', "Naimisharanya Chakra Tirth Topics", naimish_kw),
        ('blog-vindhyachal-trikon-parikrama-guide.html', "Vindhyachal Shaktipeeth Topics", vindhya_kw),
        ('blog-vip-darshan-ayodhya-ram-mandir.html', "Ayodhya Ram Mandir VIP Pass Topics", ayodhya_kw),
    ]

    for fname, title, kw_list in blog_fixes:
        fpath = os.path.join(ROOT_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()

        # Remove old section and toggleSearchIndex script
        # Match from search index start to </script>
        c = re.sub(r'(?:<!-- Search Index Cloud.*?-->\s*)?<section[^>]*search-index-section.*?<\/script>', '', c, flags=re.DOTALL)
        # Also match if section doesn't have search-index-section class but has id="searchIndexContainer"
        c = re.sub(r'<section[^>]*>.*?id="searchIndexContainer".*?<\/section>\s*(?:<script>function toggleSearchIndex.*?<\/script>)?', '', c, flags=re.DOTALL)
        
        # New section
        sec = build_search_section(title, kw_list)
        if '<footer class="site-foot">' in c:
            c = c.replace('<footer class="site-foot">', sec + '\n<footer class="site-foot">')
        else:
            c = c.replace('</body>', sec + '\n</body>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Replaced search index in {fname} with {len(kw_list)} keywords.")

    # Step 3: Inject into package pages that don't have it yet
    outbound_ayodhya_packages = [
        ('delhi-to-ayodhya-tour-package.html', "Delhi to Ayodhya Tour Package Topics", ayodhya_kw),
        ('mumbai-to-ayodhya-tour-package.html', "Mumbai to Ayodhya Tour Package Topics", ayodhya_kw),
        ('ahmedabad-to-ayodhya-tour-package.html', "Ahmedabad to Ayodhya Tour Package Topics", ayodhya_kw),
        ('bengaluru-to-ayodhya-tour-package.html', "Bengaluru to Ayodhya Tour Package Topics", ayodhya_kw),
        ('chennai-to-ayodhya-tour-package.html', "Chennai to Ayodhya Tour Package Topics", ayodhya_kw),
        ('hyderabad-to-ayodhya-tour-package.html', "Hyderabad to Ayodhya Tour Package Topics", ayodhya_kw),
        ('kolkata-to-ayodhya-tour-package.html', "Kolkata to Ayodhya Tour Package Topics", ayodhya_kw),
        ('patna-to-ayodhya-tour-package.html', "Patna to Ayodhya Tour Package Topics", ayodhya_kw),
        ('lucknow-to-ayodhya-same-day-tour-package.html', "Lucknow to Ayodhya Same Day Tour Topics", ayodhya_kw),
    ]

    circuit_packages = [
        ('ayodhya-prayagraj-tour-package.html', "Ayodhya & Prayagraj Tour Package Topics", general_kw),
        ('ayodhya-prayagraj-chitrakoot-varanasi-tour-package.html', "Ayodhya Prayagraj Chitrakoot Varanasi Topics", general_kw),
        ('full-ramayana-circuit-tour-package.html', "Ramayana Circuit Tour Package Topics", general_kw),
    ]

    for fname, title, kw_list in outbound_ayodhya_packages + circuit_packages:
        fpath = os.path.join(ROOT_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'searchIndexContainer' in c:
            continue
        
        sec = build_search_section(title, kw_list)
        if '<footer class="site-foot">' in c:
            c = c.replace('<footer class="site-foot">', sec + '\n<footer class="site-foot">')
        else:
            c = c.replace('</body>', sec + '\n</body>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Injected search index into {fname} with {len(kw_list)} keywords.")

    # Step 4: Inject into remaining blog posts
    vns_blogs = [
        'blog-varanasi-local-sightseeing-tour-package.html',
        'blog-varanasi-ganga-aarti-vip-boat-booking.html',
        'blog-varanasi-dev-deepawali-guide.html',
        'blog-varanasi-dev-deepawali-2026-vip-boat-booking-guide.html',
        'blog-kashi-vishwanath-corridor-tourist-guide.html',
        'blog-kashi-vishwanath-mangla-aarti-online-booking-guide-2026.html',
        'blog-kashi-vishwanath-sawan-vip-darshan-guide.html',
        'blog-kashi-vishwanath-sparsh-darshan-booking-rules-2026.html',
        'blog-kashi-vishwanath-vip-darshan-booking-guide.html',
        'blog-kashi-vishwanath-vip-pass-booking-online.html',
        'blog-kashi-vishwanath-vip-pass-online-booking-price-guide.html'
    ]

    for fname in vns_blogs:
        fpath = os.path.join(ROOT_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'searchIndexContainer' in c:
            continue
        
        title = fname.replace('blog-', '').replace('.html', '').replace('-', ' ').title() + " Topics"
        sec = build_search_section(title, vns_kw)
        if '<footer class="site-foot">' in c:
            c = c.replace('<footer class="site-foot">', sec + '\n<footer class="site-foot">')
        else:
            c = c.replace('</body>', sec + '\n</body>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Injected search index into Varanasi blog {fname} with {len(vns_kw)} keywords.")

    ayodhya_blogs = [
        'blog-ayodhya-deepotsav-kashi-dev-deepawali-tour-package-2026.html',
        'blog-ayodhya-dharshan-tour-package.html',
        'blog-ayodhya-diwali-yatra-guide.html',
        'blog-ayodhya-food-guide-sattvic-cuisine.html',
        'blog-ayodhya-kashi-vip-darshan-complete-guide.html',
        'blog-ayodhya-prayagraj-tour-package.html',
        'blog-ayodhya-prayagraj-varanasi-tour-package.html',
        'blog-ayodhya-same-day-tour-itinerary.html',
        'blog-ayodhya-to-prayagraj-distance-travel-guide.html',
        'blog-ayodhya-to-varanasi-distance-travel-guide.html',
        'blog-ayodhya-to-varanasi-taxi-fare-cab-booking.html',
        'blog-ayodhya-to-varanasi-vande-bharat-train-guide.html',
        'blog-ayodhya-tour-cost-budget-planner.html',
        'blog-ayodhya-tour-package-from-delhi-cost.html',
        'blog-ayodhya-varanasi-ganga-aarti-guide.html',
        'blog-ayodhya-varanasi-tour-package.html',
        'blog-best-time-to-visit-ayodhya.html',
        'blog-lucknow-to-ayodhya-travel-guide-taxi.html',
        'blog-ram-mandir-vip-pass-booking-guide.html',
        'blog-sawan-yatra-vip-darshan-guide.html'
    ]

    for fname in ayodhya_blogs:
        fpath = os.path.join(ROOT_DIR, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'searchIndexContainer' in c:
            continue
        
        title = fname.replace('blog-', '').replace('.html', '').replace('-', ' ').title() + " Topics"
        sec = build_search_section(title, ayodhya_kw)
        if '<footer class="site-foot">' in c:
            c = c.replace('<footer class="site-foot">', sec + '\n<footer class="site-foot">')
        else:
            c = c.replace('</body>', sec + '\n</body>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Injected search index into Ayodhya blog {fname} with {len(ayodhya_kw)} keywords.")

    print("Reconciliation complete!")

if __name__ == '__main__':
    main()
