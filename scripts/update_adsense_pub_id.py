import os

def update_pub_id():
    old_id = "ca-pub-7972876869997430"
    new_id = "ca-pub-7513283731802791"
    
    root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"
    
    # 1. Update HTML files in root directory
    for file in os.listdir(root_dir):
        if file.endswith(".html"):
            file_path = os.path.join(root_dir, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if old_id in content:
                print(f"Updating AdSense ID in: {file}")
                content = content.replace(old_id, new_id)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
    # 2. Update Next.js layout.tsx
    layout_path = os.path.join(root_dir, "ayodhya-landing-main", "app", "layout.tsx")
    if os.path.exists(layout_path):
        with open(layout_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if old_id in content:
            print("Updating AdSense ID in: layout.tsx")
            content = content.replace(old_id, new_id)
            with open(layout_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
    print("✨ AdSense Publisher ID update complete!")

if __name__ == "__main__":
    update_pub_id()
