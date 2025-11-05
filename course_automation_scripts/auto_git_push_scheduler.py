import subprocess
import time
import os
import sys
from datetime import datetime

# Path to your Git repo (project root)
repo_path = "/Users/francescapanteli/Desktop/CodingNomads-python-301"

def auto_git_push():
    """Stage, commit, and push changes to GitHub."""
    os.chdir(repo_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Automated commit at {timestamp}"

    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit changes; won't fail if nothing to commit
        commit_result = subprocess.run(
            ["git", "commit", "-m", commit_message],
            check=False, capture_output=True, text=True
        )

        if "nothing to commit" in commit_result.stdout.lower():
            print(f"No changes to commit at {timestamp}")
        else:
            print(f"Committed changes at {timestamp}")
            # Push to remote
            subprocess.run(["git", "push"], check=True)
            print(f"Pushed changes successfully at {timestamp}")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

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
        # Show run header
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 70)
        print(f"AUTO GIT PUSH RUN #{run_count} | {timestamp}")
        print("=" * 70)

        # Run the git push routine
        auto_git_push()

        print("-" * 70 + "\n")

        # Wait 1 minute with progress bar
        progress_bar(60)
        run_count += 1

if __name__ == "__main__":
    main()