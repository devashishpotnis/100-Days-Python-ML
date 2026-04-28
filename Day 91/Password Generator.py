import random
import string

def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_symbols)

    print(f"\n Generated Password: {password}")


    save = input("Do you want to save password to file? (y/n): ").lower()
    if save == 'y':
        with open("passwords.txt", "a") as f:
            f.write(password + "\n")
        print("Password saved to passwords.txt")


if __name__ == "__main__":
    main()