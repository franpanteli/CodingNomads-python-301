import subprocess
import time
import os
import sys
from datetime import datetime

# Use a relative path to auto_git_push.py
script_path = os.path.join(os.path.dirname(__file__), "auto_git_push.py")

def run_git_push(run_count):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n" + "=" * 70)
    print(f"AUTO GIT PUSH RUN #{run_count} | {timestamp}")
    print("=" * 70)

    try:
        subprocess.run(["python3", script_path], check=True)
        print("\nauto_git_push.py completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"\nError running auto_git_push.py: {e}")
    except FileNotFoundError:
        print(f"\nCould not find script at {script_path}")
    print("-" * 70 + "\n")

def progress_bar(duration=60):
    """Display a progress bar for 'duration' seconds."""
    for i in range(duration):
        percent = int((i + 1) / duration * 100)
        bar = "█" * (percent // 2) + "-" * (50 - percent // 2)
        sys.stdout.write(f"\rWaiting for next run: |{bar}| {percent}%")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

def main():
    print("Starting auto_git_push scheduler (runs every 1 minute)...\n")
    run_count = 1
    while True:
        run_git_push(run_count)
        progress_bar(60)  # Wait 1 minute
        run_count += 1

if __name__ == "__main__":
    main()