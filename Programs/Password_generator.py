import random
import string

def show_menu():

    # Display the menu of options for the user.

    print("\nPassword Generator")
    print("1. Generate Password")
    print("2. Exit")

def generate_password(length, use_digits, use_special_chars, use_uppercase):

    # Generate a random password with the specified options.

    characters = string.ascii_lowercase
    
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():

    # Main function to run the password generator. Displays the menu and handles user input.

    while True:
        show_menu()
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                length = int(input("Enter the password length: "))
                use_digits = input("Include digits? (y/n): ").lower() == 'y'
                use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
                use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
                
                # Ask user for the website or application associated with the password
                website = input("Enter the website or application name: ")
                
                password = generate_password(length, use_digits, use_special_chars, use_uppercase)
                print(f"Generated Password: {password}")
                
                # Save the generated password and website to a file
                save_password(password, website)
                
            except ValueError:
                print("Invalid input. Please enter valid choices.")
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def save_password(password, website):

    # Save the generated password and associated website to a file.
    
    with open("passwords.txt", "a") as file:
        file.write(f"Website/App: {website} - Password: {password}\n")
    print("Password saved to file.")

# Entry point of the program
if __name__ == "__main__":
    main()

