def otp_encrypt(pt, key_stream):
    pt = pt.replace(" ", "").lower()
    result = ""
    for i, ch in enumerate(pt):
        p = ord(ch) - 97
        k = key_stream[i]
        c = (p + k) % 26
        result += chr(c + 97)
    return result

plaintext = "send more money"
key_stream = [9,0,1,7,23,15,21,14,11,11,2,8,9]

ciphertext = otp_encrypt(plaintext, key_stream)
print("Ciphertext:", ciphertext)
