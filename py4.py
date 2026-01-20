def generate_key(text, key):
    key = key.lower()
    new_key = ""
    key_index = 0

    for ch in text:
        if ch.isalpha():
            new_key += key[key_index % len(key)]
            key_index += 1
        else:
            new_key += ch  # keep symbols same
    return new_key


def encrypt(text, key):
    text = text.lower()
    key = generate_key(text, key)
    result = ""

    for t, k in zip(text, key):
        if t.isalpha():
            shift = ord(k) - ord('a')
            result += chr((ord(t) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += t
    return result


def decrypt(cipher, key):
    cipher = cipher.lower()
    key = generate_key(cipher, key)
    result = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            shift = ord(k) - ord('a')
            result += chr((ord(c) - ord('a') - shift + 26) % 26 + ord('a'))
        else:
            result += c
    return result


# --------------------
# MAIN PROGRAM
# --------------------
print("Polyalphabetic Substitution Cipher (Vigenère)\n")

text = input("Enter text: ")
key = input("Enter key: ")

print("\n1. Encrypt")
print("2. Decrypt")
choice = int(input("Choose option: "))

if choice == 1:
    print("Encrypted text:", encrypt(text, key))
elif choice == 2:
    print("Decrypted text:", decrypt(text, key))
else:
    print("Invalid choice!")
