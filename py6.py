# Solve system of equations:
# a*E + b = B (mod 26)
# a*T + b = U (mod 26)

# Letter to number
def L(c):
    return ord(c) - ord('A')

# We know:
# plaintext:  E -> most frequent (4)
# plaintext:  T -> second      (19)
p1 = L('E')     # 4
p2 = L('T')     # 19

# ciphertext letters:
c1 = L('B')     # 1
c2 = L('U')     # 20

# Equation:
# (a*p1 + b) mod 26 = c1
# (a*p2 + b) mod 26 = c2

# Subtract equations:
# a(p2 - p1) = (c2 - c1) mod 26
A = (p2 - p1) % 26       # 19 - 4 = 15
C = (c2 - c1) % 26       # 20 - 1 = 19

# Now: a * A = C (mod 26)
# Find modular inverse of A
def mod_inverse(x, m=26):
    for i in range(1, m):
        if (x * i) % m == 1:
            return i
    return None

invA = mod_inverse(A)
a = (invA * C) % 26

# Solve for b:
b = (c1 - a * p1) % 26

print("Solved values:")
print("a =", a)
print("b =", b)


# -------------------------------
# Affine decryption
# -------------------------------
def decrypt_affine(ciphertext, a, b):
    # find inverse of a
    a_inv = mod_inverse(a)
    if a_inv is None:
        return "No multiplicative inverse for a!"

    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            C = ord(ch.upper()) - ord('A')
            P = (a_inv * (C - b + 26)) % 26
            plaintext += chr(P + ord('A'))
        else:
            plaintext += ch
    return plaintext


# ---- Example (user enters ciphertext) ----
ciphertext = input("\nEnter ciphertext to decrypt: ")
plaintext = decrypt_affine(ciphertext, a, b)

print("\nDecrypted Plaintext:")
print(plaintext)
