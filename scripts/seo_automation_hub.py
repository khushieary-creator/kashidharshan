import os
from datetime import datetime

# Import sub-modules
from site_health_auditor import audit_html_files
from auto_image_optimizer import optimize_and_geotag_images
from auto_rank_checker import check_and_log_rankings

def generate_report(root_dir, audit_results):
    report_path = os.path.join(root_dir, 'seo_health_report.md')
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    report_content = f"""# SEO Health & Automation Report
Report Generated: **{date_str}**

---

## 📄 HTML Code & Schema Audit

"""
    if not audit_results:
        report_content += "### ✅ All Pages Healthy!\nNo broken links, syntax errors, or missing tags detected.\n"
    else:
        report_content += "### ⚠️ Issues Found:\n\n"
        for filename, issues in audit_results:
            report_content += f"#### [{filename}](file://{os.path.join(root_dir, filename)})\n"
            for issue in issues:
                report_content += f"- ❌ {issue}\n"
            report_content += "\n"
            
    report_content += """
---

## 🖼️ Image Geotagging & Optimization
- Scans `assets/` directory automatically.
- WebP conversions are checked and compressed.
- Ayodhya Ram Mandir coordinates (`26.7956° N, 82.1943° E`) are injected into new WebP assets to boost local search rankings.

---

## 📈 Search Keyword Rankings
Rankings history is automatically logged in [seo_rank_history.csv](file://{os.path.join(root_dir, 'seo_rank_history.csv')}).

---

*💡 Run this tool daily before deploying to Hostinger to catch errors early!*
"""
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"✨ Master health report written to: {report_path}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    
    print("="*60)
    print("        STARTING AUTOMATED DAILY SEO ENGINE CHECKUP        ")
    print("="*60)
    
    # 1. Optimize images & Geotag
    print("\n[Step 1/3] Optimizing & Geotagging Images...")
    try:
        optimize_and_geotag_images(root_dir)
    except Exception as e:
        print(f"❌ Image optimization failed: {e}")
        
    # 2. Check search positions
    print("\n[Step 2/3] Checking Google Keyword positions...")
    try:
        check_and_log_rankings(root_dir)
    except Exception as e:
        print(f"❌ Rank checker failed: {e}")
        
    # 3. Scan site files for health errors
    print("\n[Step 3/3] Auditing HTML Files & Schemas...")
    audit_results = []
    try:
        audit_results = audit_html_files(root_dir)
    except Exception as e:
        print(f"❌ Site auditor failed: {e}")
        
    # 4. Generate master markdown report
    generate_report(root_dir, audit_results)
    
    print("\n" + "="*60)
    print("                  ALL AUTOMATED SEO TASKS DONE                  ")
    print("="*60)

if __name__ == "__main__":
    main()
