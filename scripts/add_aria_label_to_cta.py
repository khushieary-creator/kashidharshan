import os

# Root directory
ROOT_DIR = "/Users/rishabhjaiswal/ayodhya-darshan"

target_search = 'class="btn btn-primary"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 2C7 9 7 13 12 22 17 13 17 9 12 2Z"/></svg><span class="btn-text">Plan Your Yatra</span></a>'
target_replace = 'class="btn btn-primary" aria-label="Plan Your Yatra"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 2C7 9 7 13 12 22 17 13 17 9 12 2Z"/></svg><span class="btn-text">Plan Your Yatra</span></a>'

# Traverse all HTML files
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
                print(f"Added aria-label to {file}")

print("Aria label update complete.")
