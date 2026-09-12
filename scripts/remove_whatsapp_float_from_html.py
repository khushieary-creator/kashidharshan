import os
import re

ROOT_DIR = "/Users/rishabhjaiswal/ayodhya-darshan"

# Regex to match floating whatsapp button a-tags, with optional preceding comment, matching across multiple lines
pattern = re.compile(r'(<!--\s*Floating WhatsApp Button\s*-->\s*)?<a\s+[^>]*class="whatsapp-float"[^>]*>.*?</a>', re.DOTALL)

for root, dirs, files in os.walk(ROOT_DIR):
    if ".git" in root or "node_modules" in root or "ayodhya-landing-main" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "whatsapp-float" in content:
                new_content = pattern.sub("", content)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Removed floating WhatsApp button from {file}")

print("Cleanup complete.")
