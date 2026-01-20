def otp_find_key(ciphertext, new_plaintext):
    ciphertext = ciphertext.replace(" ", "")
    new_plaintext = new_plaintext.replace(" ", "")
    key = []
    for c, p in zip(ciphertext, new_plaintext):
        cnum = ord(c) - 97
        pnum = ord(p) - 97
        k = (cnum - pnum) % 26
        key.append(k)
    return key

cipher = 'ciphertext'
new_pt = "cash not needed"

print("Required Key:", otp_find_key(cipher, new_pt))
