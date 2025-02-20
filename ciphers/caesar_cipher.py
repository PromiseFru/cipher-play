"""Caesar Cipher Module"""

def caesar_cipher(text: str, key: int, encrypt: bool = True):
    """Caesar Cipher Algorithm"""
    
    result = ""
    shift = key if encrypt else -key

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            new_char = chr((((ord(char) - base) + shift) % 26) + base)
            print(new_char, char)
            result += new_char
        else:
            result += char
        print(result)
    return result

def caesar_encrypt(plaintext, shift):
    """Implements encryption logic"""
    
    return caesar_cipher(plaintext, shift)
    
def caesar_decrypt(ciphertext, shift):
    """Implements decryption logic"""

    return caesar_cipher(ciphertext, shift, False)

