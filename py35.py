# Q35: OTP Vigenere Cipher

import random
import string

def encrypt(pt, key):
    return ''.join(
        chr((ord(p)-65 + k) % 26 + 65)
        for p, k in zip(pt, key)
    )

def decrypt(ct, key):
    return ''.join(
        chr((ord(c)-65 - k) % 26 + 65)
        for c, k in zip(ct, key)
    )

plaintext = "HELLO"
key = [random.randint(0, 25) for _ in plaintext]

cipher = encrypt(plaintext, key)
plain = decrypt(cipher, key)

print("Key :", key)
print("Ciphertext:", cipher)
print("Decrypted :", plain)
