def shift_encrypt(text, offset):
    result = ""

    for char in text:
        # Encrypt all characters, wrapping within the ASCII range
        result += chr((ord(char) + offset) % 256)

    return result


def shift_decrypt(text, offset):
    result = ""

    for char in text:
        # Encrypt all characters, wrapping within the ASCII range
        result += chr((ord(char) + -offset) % 256)

    return result


# Example usage
original_text = "Hello, World! 1234."
offset = 5641

encrypted_text = shift_encrypt(original_text, offset)
print(f"Encrypted: {encrypted_text}")

decrypted_text = shift_decrypt(encrypted_text, offset)
print(f"Decrypted: {decrypted_text}")
