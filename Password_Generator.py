# Import the 'random' module as 'r' and the 'string' module as 's' for generating random passwords.
import random as r
import string as s

# Define a function to generate a password based on the given password level.
def generate_password(password_level):
    # Check the provided password level and set password length and character set accordingly.

    if password_level == "s":
        password_length = 8
        password_characters = s.ascii_letters  
    elif password_level == "m":
        password_length = 12
        password_characters = s.ascii_letters + s.digits  

    elif password_level == "h":
        password_length = 16
        password_characters = s.ascii_letters + s.digits + s.punctuation 

    elif password_level == "c":
        password_length = 20
        password_characters = s.ascii_letters + s.digits + s.punctuation + s.whitespace  

    else:
        raise ValueError("Invalid password level: {}".format(password_level))  # Raise an error for an invalid password level.

    password = ""
    # Generate the password by randomly selecting characters from the specified character set.
    for i in range(password_length):
        password += r.choice(password_characters)

    return password

# Define a function for interacting with the user.
def main():
    # Ask the user to choose a password level (s, m, h, c).
    password_level = input("Choose a password level type (s for simple, m for medium, h for hard, c for complex): ")

    # Generate a password based on the user's choice.
    password = generate_password(password_level)

    # Display the generated password.
    print("Generated password:", password)

if __name__ == "__main__":
    # Call the main function when the script is executed.
    main()
