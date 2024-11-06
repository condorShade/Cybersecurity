import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """
    Generates a secure password based on the provided parameters.
    
    Parameters:
    - length (int): Length of the password.
    - use_upper (bool): Include uppercase letters.
    - use_digits (bool): Include digits.
    - use_symbols (bool): Include special symbols.
    
    Returns:
    - str: Generated password.
    """
    
    # Basic characters (lowercase letters)
    characters = list(string.ascii_lowercase)
    
    # Add character types based on parameters
    if use_upper:
        characters.extend(string.ascii_uppercase)
    if use_digits:
        characters.extend(string.digits)
    if use_symbols:
        characters.extend(string.punctuation)
    
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
print(generate_password(16))
