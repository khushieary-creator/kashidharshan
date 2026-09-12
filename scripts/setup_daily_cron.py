import os
import subprocess

def setup_cron():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    
    # Ensure launcher has executable permissions
    launcher_path = os.path.join(root_dir, 'run_seo_automation.command')
    os.chmod(launcher_path, 0o755)
    
    # Read current crontab
    try:
        current_cron = subprocess.check_output('crontab -l', shell=True, stderr=subprocess.DEVNULL).decode('utf-8')
    except Exception:
        current_cron = ""
        
    # Check if this launcher is already in crontab
    if launcher_path in current_cron:
        print("✅ Daily automation cron job is already configured on this Mac.")
        return
        
    # Add new cron entry to run every day at 10:00 AM
    cron_entry = f'0 10 * * * "{launcher_path}" > /dev/null 2>&1\n'
    new_cron = current_cron.strip() + "\n" + cron_entry
    
    # Write to a temporary file
    temp_cron_file = os.path.join(root_dir, 'scripts', 'temp_cron_setup')
    with open(temp_cron_file, 'w', encoding='utf-8') as f:
        f.write(new_cron)
        
    # Apply crontab
    try:
        subprocess.run(f'crontab "{temp_cron_file}"', shell=True, check=True)
        print("✅ Daily cron job set up successfully!")
        print("📅 The SEO Engine will run automatically every day at 10:00 AM.")
    except Exception as e:
        print(f"❌ Error setting up cron job: {e}")
    finally:
        if os.path.exists(temp_cron_file):
            os.remove(temp_cron_file)

if __name__ == "__main__":
    setup_cron()
