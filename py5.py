import math

# Find multiplicative inverse of a mod 26
def mod_inverse(a):
    a = a % 26
    for x in range(1, 26):
        if (a * x) % 26 == 1:
            return x
    return None


def encrypt(text, a, b):
    result = ""
    for ch in text.lower():
        if ch.isalpha():
            p = ord(ch) - ord('a')
            C = (a * p + b) % 26
            result += chr(C + ord('a'))
        else:
            result += ch
    return result


def decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a)
    if a_inv is None:
        return "Error: 'a' has no multiplicative inverse (gcd(a,26) != 1)."

    for ch in cipher.lower():
        if ch.isalpha():
            C = ord(ch) - ord('a')
            p = (a_inv * (C - b + 26)) % 26
            result += chr(p + ord('a'))
        else:
            result += ch
    return result


# ----------------------
# MAIN PROGRAM
# ----------------------
print("Affine Caesar Cipher\n")

text = input("Enter text: ")
a = int(input("Enter value for a (must satisfy gcd(a,26)=1): "))
b = int(input("Enter value for b (0-25): "))

print("\n1. Encrypt")
print("2. Decrypt")
choice = int(input("Choose option: "))

if choice == 1:
    print("Encrypted text:", encrypt(text, a, b))
elif choice == 2:
    print("Decrypted text:", decrypt(text, a, b))
else:
    print("Invalid choice!")
