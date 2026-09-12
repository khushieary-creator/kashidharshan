import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

international_nri_keywords = [
    # NRI & Overseas Indian Pilgrims
    "NRI Kashi Vishwanath VIP Sugam Darshan booking",
    "Varanasi tour package for NRIs from USA UK Canada Australia",
    "Kashi Yatra package for overseas Indians",
    "NRI Pind Daan ceremony booking in Kashi Varanasi",
    "Singapore to Varanasi Kashi tour package",
    "Dubai UAE to Kashi Vishwanath tour package",
    "Mauritius to Varanasi pilgrimage tour",
    "Malaysia to Kashi Yatra package",
    "London UK to Varanasi Kashi tour package",
    "New York USA to Varanasi Kashi trip package",
    "Toronto Canada to Kashi Vishwanath tour package",
    "Sydney Melbourne Australia to Varanasi tour package",
    
    # Foreign Tourists & International Travelers
    "Varanasi private tour guide for foreign tourists",
    "English speaking local guide in Varanasi Kashi",
    "Private Ganga Aarti luxury boat tour for international travelers",
    "Varanasi 3 days luxury heritage tour package",
    "Subah e Banaras sunrise boat ride private booking",
    "Sarnath Buddhist heritage tour package for international visitors",
    "Safe travel agency in Varanasi for foreign nationals",
    "Varanasi airport luxury cab pickup Lal Bahadur Shastri VNS",
    "Custom Varanasi photography and spiritual walking tour",
    "Varanasi ghats boat tour for international visitors",
    "Varanasi cultural and heritage day tour for foreigners",
    "Varanasi airport transfer to ghat hotels for overseas travelers"
]

def inject_international_seo():
    index_path = os.path.join(BASE_DIR, 'index.html')
    services_path = os.path.join(BASE_DIR, 'services.html')
    contact_path = os.path.join(BASE_DIR, 'contact.html')
    
    # 1. Update index.html meta keywords & add NRI / International section
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    meta_pattern = re.compile(r'<meta\s+name="keywords"\s+content="([^"]*)"', re.IGNORECASE)
    match = meta_pattern.search(content)
    if match:
        existing = match.group(1)
        new_kws = list(dict.fromkeys(international_nri_keywords + existing.split(', ')))
        content = meta_pattern.sub(f'<meta name="keywords" content="{", ".join(new_kws[:150])}"', content)
        
    # Check if international section exists
    if 'id="nri-international-yatra"' not in content:
        nri_html_section = """
<!-- ===== NRI & INTERNATIONAL DELEGATE YATRA SEVA ===== -->
<section class="section" id="nri-international-yatra" style="background:linear-gradient(160deg,#FBF5EA,#F4E6CE); border-top:1px solid var(--line); border-bottom:1px solid var(--line);">
  <div class="container">
    <div class="grid cols-2" style="align-items:center; gap:clamp(36px,5vw,72px);">
      <div class="reveal">
        <p class="eyebrow">🌐 Special Seva for Overseas Devotees &amp; Foreign Travelers</p>
        <h2>NRI &amp; International Pilgrimage Assistance</h2>
        <p class="lead">Visiting Kashi from USA, UK, Canada, Australia, Singapore, Malaysia or Dubai? We offer seamless end-to-end arrangements for NRIs, PIOs, and international tourists — from airport transfers to VIP Kashi Vishwanath Darshan and private Ganga Aarti boat cruises.</p>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:24px;">
          <div style="background:#fff; padding:16px; border-radius:12px; border:1px solid var(--line-soft);">
            <h4 style="color:var(--maroon); margin-bottom:6px; font-size:1.05rem;">✈️ Overseas Pickups</h4>
            <p style="font-size:0.88rem; color:var(--ink-2); margin:0;">Direct VNS Airport transfers in premium luxury AC Innova/SUVs with courteous drivers.</p>
          </div>
          <div style="background:#fff; padding:16px; border-radius:12px; border:1px solid var(--line-soft);">
            <h4 style="color:var(--maroon); margin-bottom:6px; font-size:1.05rem;">🗣️ Fluent English Guides</h4>
            <p style="font-size:0.88rem; color:var(--ink-2); margin:0;">Government approved, English-speaking local scholar guides for ghat walks &amp; Sarnath.</p>
          </div>
          <div style="background:#fff; padding:16px; border-radius:12px; border:1px solid var(--line-soft);">
            <h4 style="color:var(--maroon); margin-bottom:6px; font-size:1.05rem;">🪔 Priority VIP Passes</h4>
            <p style="font-size:0.88rem; color:var(--ink-2); margin:0;">Pre-booked Kashi Vishwanath Sugam Darshan &amp; Mangala Aarti passes for elderly family members.</p>
          </div>
          <div style="background:#fff; padding:16px; border-radius:12px; border:1px solid var(--line-soft);">
            <h4 style="color:var(--maroon); margin-bottom:6px; font-size:1.05rem;">⛵ Private Ganga Cruise</h4>
            <p style="font-size:0.88rem; color:var(--ink-2); margin:0;">Reserved private bajra/motorboat for Dashashwamedh Ganga Aarti &amp; Subah-e-Banaras.</p>
          </div>
        </div>
        <div style="margin-top:28px;">
          <a href="contact.html" class="btn btn-saffron">Book NRI / International Yatra
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </div>
      <div class="reveal">
        <div class="frame arch" style="height:440px;"><img src="assets/reviews/group-varanasi.jpg" alt="International pilgrims and NRIs enjoying Kashi Ganga Aarti boat tour" loading="lazy" style="width:100%; height:100%; object-fit:cover;"></div>
      </div>
    </div>
  </div>
</section>
"""
        content = content.replace('<!-- ===== SERVICES ===== -->', nri_html_section + '\n<!-- ===== SERVICES ===== -->')
        
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Injected NRI & International section and keywords into index.html")

if __name__ == '__main__':
    inject_international_seo()
