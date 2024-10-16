from collections import Counter

# Sample frequency mapping for encryption (can be customized)
ENCRYPTION_MAP = {
    'E': 'X', 'T': 'Y', 'A': 'Z', 'O': 'W', 'I': 'V',
    'N': 'U', 'S': 'T', 'H': 'S', 'R': 'R', 'D': 'Q',
    'L': 'P', 'C': 'O', 'U': 'N', 'M': 'M', 'W': 'L',
    'F': 'K', 'G': 'J', 'Y': 'I', 'P': 'H', 'B': 'G',
    'V': 'F', 'K': 'E', 'J': 'D', 'X': 'C', 'Q': 'B', 'Z': 'A'
}

# Reverse mapping for decryption
DECRYPTION_MAP = {v: k for k, v in ENCRYPTION_MAP.items()}

def encrypt(plaintext):
    ciphertext = ''
    plaintext = plaintext.upper()
    for letter in plaintext:
        if letter.isalpha():
            ciphertext += ENCRYPTION_MAP.get(letter, letter)
        else:
            ciphertext += letter  # Non-alphabetic characters remain unchanged
    return ciphertext

def decrypt(ciphertext):
    plaintext = ''
    ciphertext = ciphertext.upper()
    for letter in ciphertext:
        if letter.isalpha():
            plaintext += DECRYPTION_MAP.get(letter, letter)
        else:
            plaintext += letter  # Non-alphabetic characters remain unchanged
    return plaintext

# Example usage
if __name__ == "__main__":
    message = "I AM A RWANDAN"
    encrypted_message = encrypt(message)
    decrypted_message = decrypt(encrypted_message)

    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")
