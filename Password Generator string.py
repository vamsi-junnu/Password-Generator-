import random
import string

def generate_password_from_input(input_string):
    """
    Generate a password based on user preferences from a single string input.

    Args:
        input_string (str): User input string in the format "length:uppercase:numbers:special".

    Returns:
        str: A randomly generated password.
    """
    # Parse the input string
    try:
        parts = input_string.split(":")
        if len(parts) != 4:
            raise ValueError("Input must be in the format 'length:uppercase:numbers:special'")

        length = int(parts[0])
        use_uppercase = parts[1].strip().lower() == 'y'
        use_numbers = parts[2].strip().lower() == 'y'
        use_special = parts[3].strip().lower() == 'y'

        if length < 4:
            raise ValueError("Password length must be at least 4.")
    except Exception as e:
        raise ValueError("Invalid input format or data: " + str(e))

    # Character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''

    all_characters = lowercase + uppercase + numbers + special
    if not all_characters:
        raise ValueError("At least one character type must be selected!")

    # Ensure at least one character from each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special:
        password.append(random.choice(special))
    password.append(random.choice(lowercase))  # Always include a lowercase letter

    # Fill the remaining password length
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator with Single String Input")
    print("Input format: 'length:uppercase:numbers:special'")
    print("Example: '12:y:y:y' (12 characters, include uppercase, numbers, special)")
    try:
        user_input = input("Enter your preferences: ").strip()
        password = generate_password_from_input(user_input)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
