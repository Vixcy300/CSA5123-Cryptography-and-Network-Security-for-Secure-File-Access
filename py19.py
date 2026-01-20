from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# ------------------------------------------------------------
# CBC Encryption using 3DES
# ------------------------------------------------------------
def cbc_encrypt(key, plaintext):
    iv = get_random_bytes(8)        # 64-bit IV for 3DES
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, 8))
    return iv, ciphertext

# ------------------------------------------------------------
# CBC Decryption using 3DES
# ------------------------------------------------------------
def cbc_decrypt(key, iv, ciphertext):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), 8)
    return plaintext


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
print("=== CBC Encryption using 3DES ===")

# 24-byte 3DES key (168-bit)
key = DES3.adjust_key_parity(get_random_bytes(24))
plaintext = b"Cryptography CBC Mode Example"

print("Plaintext:", plaintext)

# Encrypt
iv, ciphertext = cbc_encrypt(key, plaintext)
print("\nIV:", iv.hex())
print("Ciphertext:", ciphertext.hex())

# Decrypt
recovered = cbc_decrypt(key, iv, ciphertext)
print("\nRecovered Plaintext:", recovered)
