#!/usr/bin/env python3
import glob
import os
import re

INLINE_HEAD_SCRIPT = """<script>
function submitYatraFormToWhatsApp(e,pkg){
  if(window.submitYatraFormToWhatsApp && window.submitYatraFormToWhatsApp !== submitYatraFormToWhatsApp){
    return window.submitYatraFormToWhatsApp(e,pkg);
  }
  if(e && e.preventDefault) e.preventDefault();
  var f = (e && e.target && e.target.tagName==='FORM') ? e.target : (document.getElementById('yatraForm') || document.getElementById('kashiPkgForm') || document.forms[0]);
  if(!f) return false;
  var p = (f.querySelector('[name="mobile"],[name="phone"],#phone,input[type="tel"]')||{}).value||'';
  var n = (f.querySelector('[name="fullname"],[name="name"],#name,input[type="text"]')||{}).value||'Pilgrim Guest';
  var d = (f.querySelector('[name="travel_date"],[name="date"],#date')||{}).value||'Upcoming';
  var k = pkg || (f.querySelector('[name="package"],[name="city"],#city')||{}).value || (document.title ? document.title.split('|')[0].trim() : 'Tour Package');
  var digits = p.replace(/\D/g,'');
  if(!digits || digits.length < 10){
    alert('कृपया सही 10-अंकों का मोबाइल नंबर दर्ज करें!');
    return false;
  }
  var t = "🚩 *NEW YATRA ENQUIRY - KASHI DHARSHAN*\\n\\n👤 Name: "+n+"\\n📞 Phone: "+p+"\\n🛕 Package: "+k+"\\n📅 Date: "+d+"\\n\\n🙏 Please send complete itinerary & lowest price quote!";
  window.location.href = "https://wa.me/917011960307?text=" + encodeURIComponent(t);
  return false;
}
</script>"""

STICKY_CTA_HTML = """<!-- HIGH CONVERSION MOBILE STICKY CTA BAR -->
<div class="mobile-sticky-cta-bar" style="display: none; position: fixed; bottom: 0; left: 0; right: 0; width: 100%; background: #ffffff; border-top: 2px solid #FF6B00; z-index: 999999; box-shadow: 0 -4px 15px rgba(0,0,0,0.18); padding: 8px 12px;">
  <div style="display: flex; gap: 10px; max-width: 500px; margin: 0 auto;">
    <a href="tel:+917011960307" style="flex: 1; background: #800000; color: #ffffff; text-align: center; padding: 11px 5px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 14px; display: flex; align-items: center; justify-content: center; gap: 6px;">
      📞 Call Us Now
    </a>
    <a href="https://wa.me/917011960307?text=Har%20Har%20Mahadev!%20I%20am%20on%20website%20and%20want%20instant%20tour%20package%20details" target="_blank" rel="noopener" style="flex: 1; background: #25D366; color: #ffffff; text-align: center; padding: 11px 5px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 14px; display: flex; align-items: center; justify-content: center; gap: 6px;">
      💬 WhatsApp Inquiry
    </a>
  </div>
</div>
<style>
@media (max-width: 768px) {
  .mobile-sticky-cta-bar { display: block !important; }
  body { padding-bottom: 65px !important; }
}
</style>"""

WHATSAPP_FLOAT_HTML = """<!-- Desktop Floating WhatsApp Button with Live Pulse Badge -->
<div class="whatsapp-float-wrapper" style="position: fixed; bottom: 25px; right: 25px; z-index: 99999;">
  <a href="https://wa.me/917011960307?text=Har%20Har%20Mahadev!%20I%20want%20to%20enquire%20about%20Kashi%20Dharshan%20tour%20packages." class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp" style="display: flex; align-items: center; justify-content: center; width: 56px; height: 56px; background: #25D366; border-radius: 50%; box-shadow: 0 4px 15px rgba(37,211,102,0.4); color: #fff; text-decoration: none; position: relative;">
    <svg viewBox="0 0 24 24" style="width: 32px; height: 32px; fill: currentColor;"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm5.83 14.12c-.24.68-1.22 1.25-1.7 1.29-.48.04-.97.19-3.07-.63-2.67-1.05-4.4-3.76-4.53-3.94-.13-.18-1.07-1.42-1.07-2.72 0-1.29.67-1.93.91-2.19.24-.26.54-.33.72-.33.18 0 .36.01.52.02.17.01.39-.06.61.47.24.58.82 2.01.89 2.16.07.15.12.33.02.52-.1.19-.21.31-.36.48-.15.17-.32.39-.46.52-.16.15-.33.31-.14.63.19.32.85 1.4 1.82 2.26.97.86 1.79 1.13 2.11 1.26.32.13.51.1.7-.12.19-.22.82-.96 1.04-1.29.22-.33.45-.28.76-.16.31.12 1.99.94 2.33 1.11.34.17.57.26.65.41.08.15.08.88-.16 1.56z"/></svg>
  </a>
</div>"""

TRACKER_TAG = '<script src="conversion-tracker.js" defer></script>'

files = glob.glob('/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/*.html')
print(f"Processing {len(files)} files...")

updated_files = 0
for filepath in files:
    filename = os.path.basename(filepath)
    if filename == 'google0dc20d35f8fb3bcd.html':
        continue

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    changed = False

    # 1. Inline head script for submitYatraFormToWhatsApp
    if 'function submitYatraFormToWhatsApp' not in content:
        if '</head>' in content:
            content = content.replace('</head>', f'{INLINE_HEAD_SCRIPT}\n</head>', 1)
            changed = True

    # 2. conversion-tracker.js
    if 'conversion-tracker.js' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{TRACKER_TAG}\n</body>', 1)
            changed = True

    # 3. Mobile Sticky CTA Bar
    if 'mobile-sticky-cta-bar' not in content and 'mobile-sticky-cta' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{STICKY_CTA_HTML}\n</body>', 1)
            changed = True

    # 4. Floating WhatsApp
    if 'whatsapp-float' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{WHATSAPP_FLOAT_HTML}\n</body>', 1)
            changed = True

    # 5. Fix kashiPkgForm on kashi-tour-package.html
    if filename == 'kashi-tour-package.html' and '<form id="kashiPkgForm"' in content:
        if 'onsubmit=' not in content:
            content = content.replace('<form id="kashiPkgForm">', '<form id="kashiPkgForm" onsubmit="return submitYatraFormToWhatsApp(event, \'Kashi Tour Package (3D/2N Complete Yatra)\')">')
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_files += 1

print(f"Successfully updated {updated_files} files with conversion & lead engines!")
