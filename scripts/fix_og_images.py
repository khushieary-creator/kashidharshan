import os

def fix_og_images():
    root_dir = "/Users/rishabhjaiswal/ayodhya-darshan"
    wikimedia_prefix = "https://commons.wikimedia.org"
    local_og_image = "https://www.ayodhyadharshan.com/assets/reviews/ayodhya-night.jpg"
    
    count = 0
    for file in os.listdir(root_dir):
        if file.endswith(".html"):
            file_path = os.path.join(root_dir, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Replace og:image and twitter:image if they contain wikimedia links
            if wikimedia_prefix in content:
                print(f"Fixing hotlinked image in: {file}")
                # Simple replacement for typical tags
                import re
                content = re.sub(
                    r'<meta property="og:image" content="https://commons.wikimedia.org/[^"]+">',
                    f'<meta property="og:image" content="{local_og_image}">',
                    content
                )
                content = re.sub(
                    r'<meta name="twitter:image" content="https://commons.wikimedia.org/[^"]+">',
                    f'<meta name="twitter:image" content="{local_og_image}">',
                    content
                )
                # Fallback generic string replacement
                content = re.sub(
                    r'content="https://commons.wikimedia.org/wiki/Special:FilePath/[^"]+"',
                    f'content="{local_og_image}"',
                    content
                )
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                
    print(f"✨ Successfully fixed hotlinked og:image in {count} HTML pages!")

if __name__ == "__main__":
    fix_og_images()
