# Q33: Simplified DES demo

def des_encrypt(block, key):
    return block ^ key

def des_decrypt(block, key):
    return block ^ key

key = 0xAABBCCDDEEFF0011
plaintext = 0x1234567890ABCDEF

cipher = des_encrypt(plaintext, key)
decrypted = des_decrypt(cipher, key)

print("Plaintext :", hex(plaintext))
print("Ciphertext:", hex(cipher))
print("Decrypted :", hex(decrypted))
