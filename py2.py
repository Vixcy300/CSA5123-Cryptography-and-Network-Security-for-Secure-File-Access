import string

# Encrypt using monoalphabetic substitution
def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    ciphertext = ""

    alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"

    for ch in plaintext:
        if ch in alphabet:
            index = alphabet.index(ch)
            ciphertext += key[index]
        else:
            ciphertext += ch  # keep spaces, digits, punctuation
    return ciphertext


# Decrypt using monoalphabetic substitution
def decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    plaintext = ""

    alphabet = string.ascii_lowercase

    for ch in ciphertext:
        if ch in key:
            index = key.index(ch)
            plaintext += alphabet[index]
        else:
            plaintext += ch
    return plaintext


# ---- MAIN PROGRAM ----
print("Monoalphabetic Substitution Cipher\n")

# Example key (must contain 26 unique letters)
key = input("Enter a 26-letter key (unique letters only): ").lower()

if len(key) != 26 or len(set(key)) != 26:
    print("Invalid! Key must contain 26 UNIQUE letters.")
    exit()

text = input("Enter text: ")

print("\n1. Encrypt")
print("2. Decrypt")
choice = int(input("Choose option: "))

if choice == 1:
    print("Ciphertext:", encrypt(text, key))
elif choice == 2:
    print("Plaintext:", decrypt(text, key))
else:
    print("Invalid choice!")
