# open_file_in_pycharm.py
import os
import subprocess

def main():
    # Ask user for the file path
    file_path = input("Enter the full path of the file you want to open in PyCharm: ").strip()

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' does not exist or is not a file.")
        return

    # Path to PyCharm app (adjust if your version is different)
    pycharm_app_path = "/Applications/PyCharm.app"

    # Open the file in PyCharm
    try:
        subprocess.run(["open", "-a", pycharm_app_path, file_path])
        print(f"Opened '{file_path}' in PyCharm.")
    except Exception as e:
        print(f"Error opening file: {e}")

if __name__ == "__main__":
    main()