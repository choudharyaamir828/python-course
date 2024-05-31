import random
import string

def generate_password(length=12):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    # Ask the user for the length of the password
    length = int(input("Enter the length of the password: "))
    
    # Generate and print the password
    password = generate_password(length)
    print("Generated Password:", password)
