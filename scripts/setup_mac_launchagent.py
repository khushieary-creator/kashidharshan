import os
import subprocess

def setup_launchagent():
    # 1. Clean up old crontab to avoid double execution
    try:
        current_cron = subprocess.check_output('crontab -l', shell=True, stderr=subprocess.DEVNULL).decode('utf-8')
        lines = [line for line in current_cron.splitlines() if 'run_seo_automation.command' not in line]
        new_cron = "\n".join(lines).strip()
        
        if new_cron:
            temp_cron = "/tmp/clean_cron"
            with open(temp_cron, 'w') as f:
                f.write(new_cron + "\n")
            subprocess.run(f'crontab "{temp_cron}"', shell=True)
            if os.path.exists(temp_cron):
                os.remove(temp_cron)
        else:
            subprocess.run('crontab -r', shell=True, stderr=subprocess.DEVNULL)
        print("🧹 Cleaned up old crontab configuration.")
    except Exception as e:
        pass

    # 2. Configure macOS LaunchAgent plist
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    launcher_path = os.path.join(root_dir, 'run_seo_automation.command')
    os.chmod(launcher_path, 0o755)
    
    plist_label = "com.ayodhyadharshan.seo"
    user_home = os.path.expanduser('~')
    plist_dir = os.path.join(user_home, 'Library', 'LaunchAgents')
    os.makedirs(plist_dir, exist_ok=True)
    
    plist_path = os.path.join(plist_dir, f"{plist_label}.plist")
    
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//B3C//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{plist_label}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>{launcher_path}</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>10</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>{root_dir}/scripts/launchagent.log</string>
    <key>StandardErrorPath</key>
    <string>{root_dir}/scripts/launchagent.err</string>
</dict>
</plist>
"""
    
    with open(plist_path, 'w', encoding='utf-8') as f:
        f.write(plist_content)
    os.chmod(plist_path, 0o644)
    
    # 3. Register and load the LaunchAgent
    # Unload first in case it is already registered
    subprocess.run(f'launchctl unload "{plist_path}"', shell=True, stderr=subprocess.DEVNULL)
    try:
        subprocess.run(f'launchctl load "{plist_path}"', shell=True, check=True)
        print("✅ macOS LaunchAgent registered successfully!")
        print("📅 The SEO Engine will run automatically every day at 10:00 AM.")
        print("💡 (Note: If your Mac is sleeping at 10:00 AM, macOS will execute the checks immediately when it wakes up!)")
    except Exception as e:
        print(f"❌ Failed to load LaunchAgent: {e}")

if __name__ == "__main__":
    setup_launchagent()
