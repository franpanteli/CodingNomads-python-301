# auto_git_push_scheduler.py
import subprocess
import time
import os

# Path to your auto_git_push.py script
script_path = "/Users/francescapanteli/Desktop/CodingNomads-python-301/course_automation_scripts/auto_git_push_scheduler.py"

def run_git_push():
    print("Running auto_git_push.py...")
    try:
        subprocess.run(["python3", script_path], check=True)
        print("auto_git_push.py completed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running auto_git_push.py: {e}\n")

def main():
    print("Starting auto_git_push scheduler (runs every 1 minute)...")
    while True:
        run_git_push()
        # Sleep for 1 minute (60 seconds)
        time.sleep(60)

if __name__ == "__main__":
    main()