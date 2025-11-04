import os
import platform


def main():
    system_name = platform.system()

    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")  # macOS and Linux


if __name__ == "__main__":
    main()