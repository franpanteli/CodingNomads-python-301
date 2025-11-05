import subprocess
import time
import os
import sys

# Correct path to your auto_git_push.py script
script_path = os.path.join(
    os.path.dirname(__file__), "auto_git_push.py"
)

def run_git_push():
    print("\nRunning auto_git_push.py...")
    try:
        subprocess.run(["python3", script_path], check=True)
        print("auto_git_push.py completed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running auto_git_push.py: {e}\n")
    except FileNotFoundError:
        print(f"Could not find script at {script_path}\n")

def progress_bar(duration=60):
    """Display a progress bar for 'duration' seconds."""
    for i in range(duration):
        percent = int((i + 1) / duration * 100)
        bar = "█" * (percent // 2) + "-" * (50 - percent // 2)
        sys.stdout.write(f"\rWaiting for next run: |{bar}| {percent}%")
        sys.stdout.flush()
        time.sleep(1)
    print()  # Move to a new line after the bar finishes

def main():
    print("Starting auto_git_push scheduler (runs every 1 minute)...\n")
    while True:
        run_git_push()
        progress_bar(60)  # 60 seconds

if __name__ == "__main__":
    main()