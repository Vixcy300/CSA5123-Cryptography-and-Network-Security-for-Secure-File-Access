# Q27: RSA brute-force attack on letter-wise encryption

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# RSA public key
e = 17
n = 3233

# Encrypt letter 'C' → 2
cipher = mod_exp(2, e, n)
print("Ciphertext:", cipher)

print("\nAttacker brute-forcing:")
for m in range(26):
    if mod_exp(m, e, n) == cipher:
        print("Recovered plaintext:", m, "→", chr(m + ord('A')))
