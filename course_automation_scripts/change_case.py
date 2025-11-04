# change_case.py

def main():
    # Take input from the user
    text = input("Enter the text: ").strip()

    # Ask the user for the desired case
    print("Choose the text transformation:")
    print("1. UPPERCASE")
    print("2. lowercase")
    choice = input("Enter 1 or 2: ").strip()

    # Transform the text based on the choice
    if choice == "1":
        transformed_text = text.upper()
    elif choice == "2":
        transformed_text = text.lower()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    # Display the result
    print(transformed_text)

if __name__ == "__main__":
    main()