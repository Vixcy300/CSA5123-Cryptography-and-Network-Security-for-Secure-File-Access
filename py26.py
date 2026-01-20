# Q26: RSA key regeneration using same modulus n

def mod_inverse(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1:
            return x

# Original RSA parameters
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)

e1 = 17
d1 = mod_inverse(e1, phi)

# Bob generates new keys using SAME n
e2 = 31
d2 = mod_inverse(e2, phi)

print("Original keys:")
print("Public key (e,n):", e1, n)
print("Private key d:", d1)

print("\nNew keys using SAME n:")
print("Public key (e,n):", e2, n)
print("Private key d:", d2)

print("\n Not safe: attacker can recover φ(n) from leaked d and compute all future keys.")
