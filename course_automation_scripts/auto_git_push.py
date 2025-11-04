import os
import subprocess
from datetime import datetime

# Path to your local repository
repo_path = "/Users/francescapanteli/Desktop/CodingNomads-python-301"

# Commit message with timestamp
commit_message = f"Automated commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def run_command(command, cwd=None):
    """Run a shell command and print output."""
    result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error running command: {command}\n{result.stderr}")
    return result.returncode

def git_push():
    # Step 1: Navigate to repo
    if not os.path.exists(repo_path):
        print(f"Error: Path '{repo_path}' does not exist.")
        return

    # Step 2: Add all changes
    if run_command("git add .", cwd=repo_path) != 0:
        return

    # Step 3: Commit changes
    if run_command(f"git commit -m \"{commit_message}\"", cwd=repo_path) != 0:
        print("No changes to commit.")
        return

    # Step 4: Push to remote
    run_command("git push", cwd=repo_path)

if __name__ == "__main__":
    git_push()