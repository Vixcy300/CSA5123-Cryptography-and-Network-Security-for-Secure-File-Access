import string

# ---------------------------------------------------------
# Generate cipher alphabet using the keyword
# ---------------------------------------------------------
def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
    cipher = ""

    # Step 1: Add keyword letters (no duplicates)
    for ch in keyword:
        if ch not in cipher and ch.isalpha():
            cipher += ch

    # Step 2: Add remaining unused alphabet letters
    for ch in string.ascii_uppercase:
        if ch not in cipher:
            cipher += ch

    return cipher


# ---------------------------------------------------------
# Encrypt plaintext using the cipher alphabet
# ---------------------------------------------------------
def encrypt(plaintext, cipher_alpha):
    plaintext = plaintext.upper()
    normal_alpha = string.ascii_uppercase
    result = ""

    for ch in plaintext:
        if ch.isalpha():
            index = normal_alpha.index(ch)
            result += cipher_alpha[index]
        else:
            result += ch
    return result


# ---------------------------------------------------------
# Decrypt ciphertext using the cipher alphabet
# ---------------------------------------------------------
def decrypt(ciphertext, cipher_alpha):
    ciphertext = ciphertext.upper()
    normal_alpha = string.ascii_uppercase
    result = ""

    for ch in ciphertext:
        if ch.isalpha():
            index = cipher_alpha.index(ch)
            result += normal_alpha[index]
        else:
            result += ch
    return result


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------
keyword = input("Enter keyword: ")
cipher_alphabet = generate_cipher_alphabet(keyword)

print("\nGenerated Cipher Alphabet:")
print(cipher_alphabet)

text = input("\nEnter text: ")

print("\n1. Encrypt")
print("2. Decrypt")
choice = int(input("Choose option: "))

if choice == 1:
    print("\nEncrypted Text:", encrypt(text, cipher_alphabet))
elif choice == 2:
    print("\nDecrypted Text:", decrypt(text, cipher_alphabet))
else:
    print("Invalid choice!")
