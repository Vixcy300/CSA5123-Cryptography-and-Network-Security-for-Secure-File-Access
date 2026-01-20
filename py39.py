# Q39: Additive cipher frequency attack

def decrypt(ct, k):
    return ''.join(chr((ord(c)-65-k)%26+65) for c in ct)

ciphertext = "KHOORZRUOG"

for k in range(26):
    print(k, decrypt(ciphertext, k))
