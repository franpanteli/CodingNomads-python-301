# delete_file.py

import os

def main():
    file_path = input("Enter the full path of the file you want to delete: ").strip()

    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' does not exist or is not a file.")
        return

    confirm = input(f"Are you sure you want to delete this file'? (y/n): ").strip().lower()
    if confirm == 'y':
        try:
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()