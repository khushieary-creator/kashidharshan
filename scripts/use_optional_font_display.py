import os

ROOT_DIR = "/Users/rishabhjaiswal/ayodhya-darshan"

target_search = 'display=swap'
target_replace = 'display=optional'

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
                print(f"Changed display=swap to display=optional in {file}")

print("Font display update complete.")
