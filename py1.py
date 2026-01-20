def encrypt(text, k):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        else:
            result += ch
    return result


def decrypt(text, k):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') - k + 26) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') - k + 26) % 26 + ord('a'))
        else:
            result += ch
    return result


# ---- Main program ----
text = input("Enter text: ")
k = int(input("Enter shift (1-25): "))

print("1. Encrypt")
print("2. Decrypt")
choice = int(input("Choose option: "))

if choice == 1:
    print("Encrypted Text:", encrypt(text, k))
elif choice == 2:
    print("Decrypted Text:", decrypt(text, k))
else:
    print("Invalid choice!")