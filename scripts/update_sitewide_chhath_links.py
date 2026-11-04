import re

# 1. Update blog.html
blog_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/blog.html"
with open(blog_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

new_blog_card = """      <!-- VARANASI CHHATH PUJA 2026 BLOG -->
      <article class="card blog-card reveal" style="border: 2.5px solid #ea580c; background: #fffcf7;">
        <a href="blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Chhath Puja 2026 Ghat Arghya Timings Sunset Sunrise Boat Booking" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#c2410c; font-weight:800;">🌅 CHHATH MAHAPARV · 13–16 Nov · 7 min read</span>
          <h3><a href="blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide">Varanasi Chhath Puja 2026: Ghat Arghya Timings (15–16 Nov) &amp; Boat Guide</a></h3>
          <p>Sandhya Arghya sunset (15 Nov 5:12 PM), Usha Arghya sunrise (16 Nov 6:18 AM). 84 ghats rituals, private boat hiring rates &amp; Vrati tips.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" style="color:#c2410c; font-weight:700;">Read Chhath Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""

if "blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" not in blog_content:
    target = '<!-- MAA ANNAPURNA SWARNA DARSHAN 2026 BLOG -->'
    if target in blog_content:
        blog_content = blog_content.replace(target, new_blog_card + "      " + target)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(blog_content)
        print("Updated blog.html with Chhath Puja card.")
    else:
        print("Target not found in blog.html")
else:
    print("Chhath Puja card already in blog.html")

# 2. Update index.html
index_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

index_blog_card = """      <!-- VARANASI CHHATH PUJA CARD -->
      <article class="card blog-card reveal" style="border: 2px solid #ea580c; background: #fffcf7;">
        <a href="blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" class="bc-img"><img width="600" height="400" src="assets/destinations/ganga-aarti.webp" alt="Varanasi Chhath Puja Arghya Timings Boat Booking" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#c2410c; font-weight:800;">🌅 13–16 Nov · Chhath Mahaparv</span>
          <h3><a href="blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide">Chhath Puja 2026: Ghat Arghya Timings</a></h3>
          <p>Sandhya Arghya (15 Nov 5:12 PM), Usha Arghya (16 Nov 6:18 AM). Private boat booking &amp; ghat guide.</p>
          <a class="link-arrow bc-foot" href="blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" style="color:#c2410c; font-weight:700;">View Chhath Schedule <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""

if "blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" not in index_content:
    target_idx = '<!-- MAA ANNAPURNA SWARNA DARSHAN CARD -->'
    if target_idx in index_content:
        index_content = index_content.replace(target_idx, index_blog_card + "      " + target_idx)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("Updated index.html with Chhath Puja insight card.")
    else:
        print("Target not found in index.html")
else:
    print("Chhath Puja card already in index.html")

# 3. Update sitemap.xml
sitemap_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

# Update lastmod for primary pages to 2026-11-04
sitemap_content = sitemap_content.replace("<lastmod>2026-11-02</lastmod>", "<lastmod>2026-11-04</lastmod>")

chhath_url_tag = """  <url>
    <loc>https://www.kashidharshan.com/blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide</loc>
    <lastmod>2026-11-04</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

if "blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" not in sitemap_content:
    sitemap_content = sitemap_content.replace("</urlset>", chhath_url_tag + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Updated sitemap.xml with Chhath Puja guide URL.")
else:
    print("URL already in sitemap.xml")

# 4. Update rss.xml
rss_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/rss.xml"
with open(rss_path, "r", encoding="utf-8") as f:
    rss_content = f.read()

# Update lastBuildDate
rss_content = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', '<lastBuildDate>Wed, 04 Nov 2026 10:30:00 +0530</lastBuildDate>', rss_content)

rss_item = """    <item>
      <title>Varanasi Chhath Puja 2026: Ghat Arghya Timings (15-16 Nov), Boat Rates &amp; Schedule</title>
      <link>https://www.kashidharshan.com/blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide</link>
      <guid>https://www.kashidharshan.com/blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide</guid>
      <description>Complete guide to Chhath Puja in Varanasi: Sandhya Arghya sunset (15 Nov 5:12 PM), Usha Arghya sunrise (16 Nov 6:18 AM), private boat booking rates, and best ghats.</description>
      <pubDate>Wed, 04 Nov 2026 10:30:00 +0530</pubDate>
    </item>
"""

if "blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" not in rss_content:
    rss_content = rss_content.replace("<item>", rss_item + "    <item>", 1)
    with open(rss_path, "w", encoding="utf-8") as f:
        f.write(rss_content)
    print("Updated rss.xml with Chhath Puja RSS item.")
else:
    print("Item already in rss.xml")

# 5. Update llms.txt
llms_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/llms.txt"
with open(llms_path, "r", encoding="utf-8") as f:
    llms_content = f.read()

llms_item = "- [Varanasi Chhath Puja 2026 Guide](https://www.kashidharshan.com/blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide): Complete guide to celebrating Chhath Mahaparv on Varanasi ghats (13-16 November 2026), Sandhya Arghya (15 Nov 5:12 PM) and Usha Arghya (16 Nov 6:18 AM) timings, and private boat booking for Vratis.\n"

if "blog-varanasi-chhath-puja-2026-ghat-arghya-timings-boat-booking-guide" not in llms_content:
    target_llms = "- [Maa Annapurna Swarna Darshan 2026]"
    if target_llms in llms_content:
        llms_content = llms_content.replace(target_llms, llms_item + target_llms)
        with open(llms_path, "w", encoding="utf-8") as f:
            f.write(llms_content)
        print("Updated llms.txt with Chhath Puja guide.")
    else:
        print("Target not found in llms.txt")
else:
    print("Chhath Puja already in llms.txt")

