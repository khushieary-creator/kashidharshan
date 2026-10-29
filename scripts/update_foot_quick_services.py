import os
import glob

old_snippet = '<a href="blog-varanasi-air-show-2026-wings-over-ganges-guide" style="color:#FCEFD9; text-decoration:none;">Varanasi Air Show 2026 Schedule</a>'
new_snippet = '<a href="blog-kashi-darshan-places-to-visit-1-day-2-days-itinerary-guide-2026" style="color:#FCEFD9; text-decoration:none;">Kashi Darshan Guide</a>\n      <span style="color:rgba(255,255,255,0.25);">•</span>\n      <a href="blog-varanasi-dev-deepawali-tour-package-2026-complete-itinerary-cost" style="color:#FCEFD9; text-decoration:none;">Dev Deepawali 2026 Package</a>'

count = 0
for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_snippet in content:
        content = content.replace(old_snippet, new_snippet)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Updated {count} HTML files with fresh Kashi Darshan and Dev Deepawali foot links.")
