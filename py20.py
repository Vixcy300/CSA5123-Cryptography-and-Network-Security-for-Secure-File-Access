from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

BLOCK = 8  # DES block size

def flip_bit(data, byte_index, bit_index):
    data = bytearray(data)
    data[byte_index] ^= (1 << bit_index)
    return bytes(data)

def ecb_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, BLOCK))

def ecb_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), BLOCK)

def cbc_encrypt(key, plaintext, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    return cipher.encrypt(pad(plaintext, BLOCK))

def cbc_decrypt(key, ciphertext, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), BLOCK)


# --------------------------
# MAIN DEMO
# --------------------------
key = os.urandom(8)
iv = os.urandom(8)
plaintext = b"ABCDEFGHIJKLMNOP"  # 2 blocks

print("\nOriginal Plaintext:", plaintext)

# Encrypt both modes
ecb_ct = ecb_encrypt(key, plaintext)
cbc_ct = cbc_encrypt(key, plaintext, iv)

# Flip 1 bit in C1
cbc_ct_corrupt = flip_bit(cbc_ct, 0, 0)

print("\nCBC: Corrupting one bit in C1...")

try:
    new_pt = cbc_decrypt(key, cbc_ct_corrupt, iv)
    print("Recovered plaintext:", new_pt)
except:
    print("Decryption failed due to padding error")

