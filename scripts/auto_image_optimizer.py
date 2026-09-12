import os
import re

try:
    from PIL import Image, ImageOps
    from PIL.ExifTags import TAGS
except ImportError:
    Image = None
    ImageOps = None


def optimize_and_geotag_images(root_dir):
    if Image is None:
        print("⚠️ Pillow library is not installed. Skipping image conversion and EXIF injection.")
        print("💡 Run: pip install Pillow to enable automated image optimization.")
        return
        
    assets_dir = os.path.join(root_dir, 'assets')
    if not os.path.exists(assets_dir):
        print("❌ assets/ directory not found.")
        return
        
    image_extensions = ('.jpg', '.jpeg', '.png')
    images_optimized = 0
    
    for filename in os.listdir(assets_dir):
        if filename.lower().endswith(image_extensions):
            file_path = os.path.join(assets_dir, filename)
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            webp_path = os.path.join(assets_dir, webp_filename)
            
            # Don't re-optimize if WebP already exists and is newer
            if os.path.exists(webp_path):
                continue
                
            try:
                print(f"Compressing and Geotagging: {filename} -> {webp_filename}")
                img = Image.open(file_path)
                img = ImageOps.exif_transpose(img)
                
                # Setup EXIF with Ayodhya coordinates (26.7956 N, 82.1943 E)
                exif = img.getexif()
                gps_ifd = exif.get_ifd(34853)
                gps_ifd[1] = 'N'
                gps_ifd[2] = 26.7956
                gps_ifd[3] = 'E'
                gps_ifd[4] = 82.1943
                
                # Save as WebP
                img.save(webp_path, 'WEBP', quality=82, exif=exif)
                images_optimized += 1
                
                # Replace image references in all HTML files
                replace_image_refs_in_html(root_dir, filename, webp_filename)
                
            except Exception as e:
                print(f"  ❌ Error optimizing {filename}: {str(e)}")
                
    print(f"✅ Image optimization complete. Optimized {images_optimized} new images.")

def replace_image_refs_in_html(root_dir, old_img, new_img):
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
    for file_name in html_files:
        file_path = os.path.join(root_dir, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_ref = f"assets/{old_img}"
        new_ref = f"assets/{new_img}"
        
        if old_ref in content:
            updated_content = content.replace(old_ref, new_ref)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"  🔄 Updated image reference in {file_name}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    optimize_and_geotag_images(current_dir)
