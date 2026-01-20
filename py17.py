# DES Key schedule implementation for ENCRYPTION and DECRYPTION

# PC-1 permutation table (removes parity bits)
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# PC-2 permutation table (selects 48 bits)
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

# Left shift schedule
shifts = [1, 1, 2, 2, 2, 2, 2, 2,
          1, 2, 2, 2, 2, 2, 2, 1]


# -------------------------------------------------
# Helper: Apply permutation table to a bitstring
# -------------------------------------------------
def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

# -------------------------------------------------
# Left shift rotation
# -------------------------------------------------
def left_shift(bits, n):
    return bits[n:] + bits[:n]


# -------------------------------------------------
# Key generation
# -------------------------------------------------
def generate_keys(key_64bit):
    # Step 1: apply PC-1
    key_56bit = permute(key_64bit, PC1)

    C = key_56bit[:28]
    D = key_56bit[28:]

    encryption_keys = []

    # Step 2: generate 16 subkeys
    for i in range(16):
        C = left_shift(C, shifts[i])
        D = left_shift(D, shifts[i])

        CD = C + D

        # Step 3: apply PC-2 to get Ki
        Ki = permute(CD, PC2)
        encryption_keys.append(Ki)

    # For decryption: reverse key order
    decryption_keys = encryption_keys[::-1]

    return encryption_keys, decryption_keys


# -------------------------------------------------
# MAIN
# -------------------------------------------------
key_64bit = input("Enter 64-bit key (as binary 0/1 string): ")

enc_keys, dec_keys = generate_keys(key_64bit)

print("\n===== DES Encryption Subkeys (K1 to K16) =====")
for i, k in enumerate(enc_keys):
    print(f"K{i+1}: {k}")

print("\n===== DES Decryption Subkeys (K16 to K1 reversed) =====")
for i, k in enumerate(dec_keys):
    print(f"K{i+1}: {k}")
