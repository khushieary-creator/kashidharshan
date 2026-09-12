import os
import re

# Root directory
ROOT_DIR = "/Users/rishabhjaiswal/ayodhya-darshan"

# Replacement mappings
replacements = {
    # Ram Mandir
    r"https?://(?:commons\.wikimedia\.org/wiki/Special:FilePath/|upload\.wikimedia\.org/wikipedia/commons/[a-f0-9/]+/)?Ram_Mandir(?:%2C|,)?_Ayodhya\.(?:png|jpg|webp)(?:\?[a-zA-Z0-9=&_-]*)?": "assets/destinations/ram-mandir.webp",
    
    # Ganga Aarti
    r"https?://(?:commons\.wikimedia\.org/wiki/Special:FilePath/|upload\.wikimedia\.org/wikipedia/commons/[a-f0-9/]+/)?Evening_Ganga_Aarti_at_Dashashwamedh_Ghat\.(?:JPG|jpg|jpeg)(?:\?[a-zA-Z0-9=&_-]*)?": "assets/destinations/ganga-aarti.webp",
    
    # Triveni Sangam
    r"https?://(?:commons\.wikimedia\.org/wiki/Special:FilePath/|upload\.wikimedia\.org/wikipedia/commons/[a-f0-9/]+/)?Triveni_Sangam\.(?:JPG|jpg|jpeg)(?:\?[a-zA-Z0-9=&_-]*)?": "assets/destinations/triveni-sangam.webp",
    
    # Mandakini River
    r"https?://(?:commons\.wikimedia\.org/wiki/Special:FilePath/|upload\.wikimedia\.org/wikipedia/commons/[a-f0-9/]+/)?Mandakini_River\.(?:jpg|jpeg)(?:\?[a-zA-Z0-9=&_-]*)?": "assets/destinations/mandakini-river.webp",
    
    # Kashi Temple
    r"https?://(?:commons\.wikimedia\.org/wiki/Special:FilePath/|upload\.wikimedia\.org/wikipedia/commons/[a-f0-9/]+/)?Kashi_Vishwanath_temple\.(?:jpg|jpeg)(?:\?[a-zA-Z0-9=&_-]*)?": "assets/destinations/kashi-temple.webp",
    
    # Prem Mandir
    r"https?://(?:commons\.wikimedia\.org/wiki/Special:FilePath/|upload\.wikimedia\.org/wikipedia/commons/[a-f0-9/]+/)?Prem_Mandir(?:%2C|,)?_Vrindavan\.(?:jpg|jpeg)(?:\?[a-zA-Z0-9=&_-]*)?": "assets/destinations/prem-mandir.webp",
    
    # Vishram Ghat
    r"https?://(?:commons\.wikimedia\.org/wiki/Special:FilePath/|upload\.wikimedia\.org/wikipedia/commons/[a-f0-9/]+/)?Vishram_Ghat\.(?:jpg|jpeg)(?:\?[a-zA-Z0-9=&_-]*)?": "assets/destinations/vishram-ghat.webp"
}

# Compile regex patterns
compiled_replacements = {re.compile(pattern, re.IGNORECASE): replacement for pattern, replacement in replacements.items()}

# Traverse all HTML files
for root, dirs, files in os.walk(ROOT_DIR):
    # Exclude directories
    if ".git" in root or "node_modules" in root or "ayodhya-landing-main" in root:
        continue
        
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            original_content = content
            replacements_made = 0
            
            # Apply replacements
            for pattern, replacement in compiled_replacements.items():
                content, count = pattern.subn(replacement, content)
                replacements_made += count
                
            if replacements_made > 0:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated {file}: Made {replacements_made} replacements.")

print("Replacement complete.")
