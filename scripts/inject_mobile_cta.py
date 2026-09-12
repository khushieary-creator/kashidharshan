import os

def inject_mobile_cta():
    root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"
    
    mobile_cta_markup = """
<!-- Mobile Sticky Bottom CTA Bar -->
<div class="mobile-sticky-cta">
  <a href="tel:+919235222399" class="cta-call">
    <svg viewBox="0 0 24 24"><path d="M6.62,10.79C8.06,13.62 10.38,15.94 13.21,17.38L15.41,15.18C15.69,14.9 16.08,14.82 16.43,14.93C17.55,15.3 18.75,15.5 20,15.5A1,1 0 0,1 21,16.5V20A1,1 0 0,1 20,21A17,17 0 0,1 3,4A1,1 0 0,1 4,3H7.5A1,1 0 0,1 8.5,4C8.7,5.25 8.9,6.45 9.27,7.57C9.38,7.92 9.3,8.31 9.03,8.59L6.62,10.79Z"/></svg>
    <span>Call Now</span>
  </a>
  <a href="https://wa.me/919235222399?text=Jai%20Shree%20Ram!%20I%20want%20to%20enquire%20about%20Ayodhya%20Dharshan%20tour%20packages." class="cta-whatsapp" target="_blank" rel="noopener noreferrer">
    <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2zm5.83 14.12c-.24.68-1.22 1.25-1.7 1.29-.48.04-.97.19-3.07-.63-2.67-1.05-4.4-3.76-4.53-3.94-.13-.18-1.07-1.42-1.07-2.72 0-1.29.67-1.93.91-2.19.24-.26.54-.33.72-.33.18 0 .36.01.52.02.17.01.39-.06.61.47.24.58.82 2.01.89 2.16.07.15.12.33.02.52-.1.19-.21.31-.36.48-.15.17-.32.39-.46.52-.16.15-.33.31-.14.63.19.32.85 1.4 1.82 2.26.97.86 1.79 1.13 2.11 1.26.32.13.51.1.7-.12.19-.22.82-.96 1.04-1.29.22-.33.45-.28.76-.16.31.12 1.99.94 2.33 1.11.34.17.57.26.65.41.08.15.08.88-.16 1.56z"/></svg>
    <span>WhatsApp Chat</span>
  </a>
</div>
"""
    
    count = 0
    for file in os.listdir(root_dir):
        if file.endswith(".html") and file not in ["google0dc20d35f8fb3bcd.html"]:
            file_path = os.path.join(root_dir, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if mobile-sticky-cta is already in the page
            if "class=\"mobile-sticky-cta\"" in content:
                continue
                
            # Find the floating WhatsApp button block or </body> and place our CTA before it
            target = 'class="whatsapp-float"'
            if target in content:
                print(f"Injecting mobile CTA into: {file}")
                # We want to find the end of the <a> tag that contains class="whatsapp-float"
                idx = content.find(target)
                end_a_idx = content.find("</a>", idx)
                if end_a_idx != -1:
                    insert_pos = end_a_idx + len("</a>")
                    new_content = content[:insert_pos] + "\n" + mobile_cta_markup + content[insert_pos:]
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
            else:
                # Fallback: insert right before </body>
                if "</body>" in content:
                    print(f"Injecting mobile CTA (fallback </body>) into: {file}")
                    new_content = content.replace("</body>", f"\n{mobile_cta_markup}\n</body>")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
                    
    print(f"✨ Successfully injected mobile sticky CTA bar in {count} HTML pages!")

if __name__ == "__main__":
    inject_mobile_cta()
