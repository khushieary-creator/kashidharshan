#!/bin/bash
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
cd "$(dirname "$0")"
echo "============================================================"
echo "          AYODHYA DHARSHAN AUTOMATED SEO LAUNCHER          "
echo "============================================================"


# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 is not installed on this system."
    echo "💡 Please install Python 3 on your Mac to run these automated checks."
    if [ -t 0 ]; then
        read -p "Press Enter to exit..."
    fi
    exit 1
fi

# Check if PIL is installed
python3 -c "import PIL" &> /dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing Pillow library (needed for image compression and geotagging)..."
    python3 -m pip install Pillow
fi

# Run the master automation script
python3 scripts/seo_automation_hub.py

echo "🚀 Starting Auto-Push to GitHub..."
git add seo_rank_history.csv seo_health_report.md assets/* 2>/dev/null
git commit -m "Auto-update: Daily SEO rankings, health report, and optimized assets"
git push origin main

echo ""
echo "📄 Your master SEO report has been generated and pushed to GitHub!"
if [ -t 0 ]; then
    read -p "Press Enter to close this window..."
fi

