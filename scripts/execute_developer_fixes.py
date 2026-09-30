#!/usr/bin/env python3
"""
Developer Requested Lead Conversion & SEO Title Fixes:
1. Replaces form submission script with requested WhatsApp listener for phone: 917408763401.
2. Connects Homepage Hero Form on index.html.
3. Sets exact requested SEO Titles:
   - Homepage: "Kashi Vishwanath & Ayodhya Ram Mandir Tour Packages 2026" (57 chars)
   - Varanasi Page: "Varanasi Tour Package: Kashi Vishwanath VIP Darshan" (52 chars)
   - Ayodhya Page: "Ayodhya Ram Mandir VIP Pass & Tour Package 2026" (48 chars)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_WA_NUMBER = "917408763401"

UNIVERSAL_FORM_JS = """
<script>
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('form').forEach(function(form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var nameInput = this.querySelector('[name="name"]') || this.querySelector('[name="fullname"]') || this.querySelector('#name') || {};
      var phoneInput = this.querySelector('[name="phone"]') || this.querySelector('[name="mobile"]') || this.querySelector('#phone') || {};
      var dateInput = this.querySelector('[name="date"]') || this.querySelector('[name="travel_date"]') || this.querySelector('#date') || {};
      
      var name = nameInput.value || 'Guest';
      var phone = phoneInput.value || '';
      var date = dateInput.value || 'Upcoming';
      var pkg = (document.title.split('|')[0] || 'Tour Package').trim();
      
      if (!phone || phone.length < 8) {
        alert('Please enter a valid mobile number so we can send your itinerary & quote!');
        return false;
      }
      
      var waText = "Hi Kashi Dharshan! New Inquiry:\\nPackage: " + pkg + "\\nName: " + name + "\\nPhone: " + phone + "\\nTravel Date: " + date;
      var waUrl = "https://wa.me/917408763401?text=" + encodeURIComponent(waText);
      
      window.open(waUrl, '_blank');
      window.location.href = "thankyou.html";
      return false;
    });
  });
});
</script>
"""

EXACT_TITLES = {
    "index.html": "Kashi Vishwanath & Ayodhya Ram Mandir Tour Packages 2026",
    "varanasi-tour-package.html": "Varanasi Tour Package: Kashi Vishwanath VIP Darshan",
    "ayodhya-tour-package.html": "Ayodhya Ram Mandir VIP Pass & Tour Package 2026"
}

def apply_fixes():
    fixed_count = 0
    
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".html") and not f.startswith("google"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8") as fh:
                    content = fh.read()
                    
                orig_content = content
                
                # 1. Update Titles if in EXACT_TITLES
                if f in EXACT_TITLES:
                    content = re.sub(r'<title>(.*?)</title>', f'<title>{EXACT_TITLES[f]}</title>', content, flags=re.IGNORECASE)
                    
                # 2. Inject or Update Universal Form JS
                # Remove any existing submitYatraFormToWhatsApp or older handlers
                if "submitYatraFormToWhatsApp" in content:
                    content = re.sub(r'<script>\s*function submitYatraFormToWhatsApp.*?</script>', '', content, flags=re.DOTALL)
                    
                if "917408763401" not in content:
                    if '</head>' in content:
                        content = content.replace('</head>', UNIVERSAL_FORM_JS + '\n</head>')
                    elif '</body>' in content:
                        content = content.replace('</body>', UNIVERSAL_FORM_JS + '\n</body>')
                        
                # 3. Update all forms to have action="thankyou.html"
                def fix_form_tag(m):
                    tag = m.group(0)
                    if 'action=' not in tag or 'action=""' in tag or "action=''" in tag:
                        tag = re.sub(r'action=["\']?["\']?', '', tag)
                        tag = tag[:-1] + ' action="thankyou.html" method="GET">'
                    return tag
                    
                content = re.sub(r'<form[^>]*>', fix_form_tag, content, flags=re.IGNORECASE)
                
                # 4. Update any standalone WhatsApp links to 917408763401 if requested
                content = content.replace('wa.me/917011960307', 'wa.me/917408763401')
                content = content.replace('phone=917011960307', 'phone=917408763401')
                
                if content != orig_content:
                    with open(filepath, "w", encoding="utf-8") as fh:
                        fh.write(content)
                    fixed_count += 1
                    
    print(f"✅ Developer requested fixes applied across {fixed_count} HTML pages!")

if __name__ == "__main__":
    apply_fixes()
