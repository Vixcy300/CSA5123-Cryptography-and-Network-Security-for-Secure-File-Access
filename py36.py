# Q36: Affine Caesar Cipher

import math

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(pt, a, b):
    return ''.join(
        chr((a*(ord(c)-65) + b) % 26 + 65)
        for c in pt
    )

def decrypt(ct, a, b):
    a_inv = modinv(a, 26)
    return ''.join(
        chr((a_inv*(ord(c)-65 - b)) % 26 + 65)
        for c in ct
    )

a, b = 5, 8
plaintext = "HELLO"

cipher = encrypt(plaintext, a, b)
print("Cipher:", cipher)
print("Plain :", decrypt(cipher, a, b))
