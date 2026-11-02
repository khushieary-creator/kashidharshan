import re

# 1. Update blog.html
blog_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/blog.html"
with open(blog_path, "r", encoding="utf-8") as f:
    blog_content = f.read()

new_blog_card = """      <!-- MAA ANNAPURNA SWARNA DARSHAN 2026 BLOG -->
      <article class="card blog-card reveal" style="border: 2.5px solid #d97706; background: #fffcf7;">
        <a href="blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Maa Annapurna Swarna Darshan Golden Idol Dates Annakoot Varanasi" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">✨ ONLY 5 DAYS A YEAR · 6-10 Nov · 7 min read</span>
          <h3><a href="blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026">Maa Annapurna Swarna Darshan 2026: Golden Idol Dates &amp; Khazana Coins</a></h3>
          <p>Rare annual golden idol opening from Dhanteras to Bhai Dooj. 56 Bhog Annakoot schedule, Mahant coin distribution &amp; VIP yatra tips.</p>
          <a class="link-arrow bc-foot" href="blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" style="color:#b45309; font-weight:700;">Read Swarna Darshan Guide <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""

if "blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" not in blog_content:
    target = '<!-- VARANASI GANGA AARTI WINTER TIMINGS 2026-2027 BLOG -->'
    if target in blog_content:
        blog_content = blog_content.replace(target, new_blog_card + "      " + target)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(blog_content)
        print("Updated blog.html with Maa Annapurna Swarna Darshan card.")
    else:
        print("Target not found in blog.html")
else:
    print("Maa Annapurna card already in blog.html")

# 2. Update index.html
index_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

index_blog_card = """      <!-- MAA ANNAPURNA SWARNA DARSHAN CARD -->
      <article class="card blog-card reveal" style="border: 2px solid #d97706; background: #fffcf7;">
        <a href="blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" class="bc-img"><img width="600" height="400" src="assets/destinations/kashi-temple.webp" alt="Maa Annapurna Swarna Darshan Golden Idol Dates" loading="lazy" decoding="async"></a>
        <div class="bc-body">
          <span class="bc-meta" style="color:#b45309; font-weight:800;">✨ 6–10 Nov · Swarna Darshan</span>
          <h3><a href="blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026">Maa Annapurna Swarna Darshan 2026: Golden Idol Dates</a></h3>
          <p>Annual 5-day golden idol opening from Dhanteras to Bhai Dooj. Khazana coin prasad &amp; Annakoot 56 Bhog.</p>
          <a class="link-arrow bc-foot" href="blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" style="color:#b45309; font-weight:700;">View Festival Dates <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        </div>
      </article>

"""

if "blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" not in index_content:
    target_idx = '<!-- VARANASI GANGA AARTI WINTER TIMING CARD -->'
    if target_idx in index_content:
        index_content = index_content.replace(target_idx, index_blog_card + "      " + target_idx)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("Updated index.html with Maa Annapurna Swarna Darshan insight card.")
    else:
        print("Target not found in index.html")
else:
    print("Maa Annapurna card already in index.html")

# 3. Update sitemap.xml
sitemap_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

# Update lastmod for primary pages to 2026-11-02
sitemap_content = sitemap_content.replace("<lastmod>2026-10-30</lastmod>", "<lastmod>2026-11-02</lastmod>")

annapurna_url_tag = """  <url>
    <loc>https://www.kashidharshan.com/blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026</loc>
    <lastmod>2026-11-02</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

if "blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" not in sitemap_content:
    sitemap_content = sitemap_content.replace("</urlset>", annapurna_url_tag + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Updated sitemap.xml with Maa Annapurna guide URL.")
else:
    print("URL already in sitemap.xml")

# 4. Update rss.xml
rss_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/rss.xml"
with open(rss_path, "r", encoding="utf-8") as f:
    rss_content = f.read()

# Update lastBuildDate
rss_content = re.sub(r'<lastBuildDate>.*?</lastBuildDate>', '<lastBuildDate>Mon, 02 Nov 2026 10:00:00 +0530</lastBuildDate>', rss_content)

rss_item = """    <item>
      <title>Maa Annapurna Swarna Darshan 2026: Golden Idol Dates, Annakoot &amp; Khazana Coin Guide</title>
      <link>https://www.kashidharshan.com/blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026</link>
      <guid>https://www.kashidharshan.com/blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026</guid>
      <description>Rare annual 5-day golden idol opening of Maa Annapurna from Dhanteras to Bhai Dooj (6 to 10 November 2026). Timings, 56 Bhog Annakoot, and blessed coin distribution.</description>
      <pubDate>Mon, 02 Nov 2026 10:00:00 +0530</pubDate>
    </item>
"""

if "blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" not in rss_content:
    rss_content = rss_content.replace("<item>", rss_item + "    <item>", 1)
    with open(rss_path, "w", encoding="utf-8") as f:
        f.write(rss_content)
    print("Updated rss.xml with Maa Annapurna Swarna Darshan RSS item.")
else:
    print("Item already in rss.xml")

# 5. Update llms.txt
llms_path = "/Users/rishabhjaiswal/.gemini/antigravity/scratch/kashidharshan/llms.txt"
with open(llms_path, "r", encoding="utf-8") as f:
    llms_content = f.read()

llms_item = "- [Maa Annapurna Swarna Darshan 2026](https://www.kashidharshan.com/blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026): Annual 5-day opening of the solid pure-gold idol of Maa Annapurna from Dhanteras to Bhai Dooj (6-10 November 2026), Annakoot 56 Bhog schedule, and Khazana coin prasad.\n"

if "blog-maa-annapurna-swarna-darshan-golden-idol-annakoot-dates-timings-2026" not in llms_content:
    target_llms = "- [Varanasi Ganga Aarti Winter Timings 2026-2027]"
    if target_llms in llms_content:
        llms_content = llms_content.replace(target_llms, llms_item + target_llms)
        with open(llms_path, "w", encoding="utf-8") as f:
            f.write(llms_content)
        print("Updated llms.txt with Maa Annapurna guide.")
    else:
        print("Target not found in llms.txt")
else:
    print("Maa Annapurna already in llms.txt")

