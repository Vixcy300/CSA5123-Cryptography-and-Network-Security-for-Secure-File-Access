import numpy as np

# Convert letter to number (a=0, b=1, ... z=25)
def char_to_num(c):
    return ord(c) - ord('a')

# Convert number to letter
def num_to_char(n):
    return chr(n + ord('a'))

# Prepare plaintext: remove spaces and make even length
def prepare_plaintext(pt):
    pt = pt.replace(" ", "").lower()
    if len(pt) % 2 != 0:
        pt += 'x'
    return pt

# Hill cipher encryption
def hill_encrypt(pt, K):
    pt = prepare_plaintext(pt)
    ciphertext = ""
    print("\n--- Encryption Calculations ---")

    for i in range(0, len(pt), 2):
        a = char_to_num(pt[i])
        b = char_to_num(pt[i+1])
        vec = np.array([[a], [b]])

        print(f"\nPair: {pt[i]} {pt[i+1]} → vector [{a} {b}]")

        res = np.dot(K, vec) % 26
        c1 = num_to_char(int(res[0][0]))
        c2 = num_to_char(int(res[1][0]))

        print(f"Matrix * vector mod 26 = {res.T} → {c1}{c2}")

        ciphertext += c1 + c2
    return ciphertext

# Hill cipher decryption
def hill_decrypt(ct, K):
    det = int(np.round(np.linalg.det(K)))
    det_inv = pow(det % 26, -1, 26)

    adj = np.array([[K[1][1], -K[0][1]],
                    [-K[1][0], K[0][0]]])

    K_inv = (det_inv * adj) % 26
    K_inv = K_inv.astype(int)

    print("\nInverse Key Matrix:")
    print(K_inv)

    plaintext = ""
    print("\n--- Decryption Calculations ---")

    for i in range(0, len(ct), 2):
        a = char_to_num(ct[i])
        b = char_to_num(ct[i+1])
        vec = np.array([[a], [b]])

        print(f"\nCipher Pair: {ct[i]} {ct[i+1]} → [{a} {b}]")

        res = np.dot(K_inv, vec) % 26
        p1 = num_to_char(int(res[0][0]))
        p2 = num_to_char(int(res[1][0]))

        print(f"K_inv * vector mod 26 = {res.T} → {p1}{p2}")

        plaintext += p1 + p2
    return plaintext


# ---------------- MAIN ----------------
plaintext = "meet me at the usual place at ten rather than eight oclock"
K = np.array([[9, 4], [5, 7]])

ciphertext = hill_encrypt(plaintext, K)
print("\nCiphertext:", ciphertext)

decrypted = hill_decrypt(ciphertext, K)
print("\nRecovered Plaintext:", decrypted)
