import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired password length: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)

        print("\nGenerated Password:", password)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
