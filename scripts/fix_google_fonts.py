import os

ROOT_DIR = "/Users/rishabhjaiswal/ayodhya-darshan"

target_search = 'family=Marcellus&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Mukta:wght@300;400;500;600;700&display=swap'
target_replace = 'family=Marcellus&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Mukta:wght@300;400;500;600;700&display=swap'

for root, dirs, files in os.walk(ROOT_DIR):
    if ".git" in root or "node_modules" in root or "ayodhya-landing-main" in root:
        continue
        
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            if target_search in content:
                content = content.replace(target_search, target_replace)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Fixed fonts in {file}")

print("Font update complete.")
