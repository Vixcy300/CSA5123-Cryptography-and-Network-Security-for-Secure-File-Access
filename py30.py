# Q30: CBC-MAC vulnerability

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def block_cipher(block, key):
    return xor_bytes(block, key)

def cbc_mac(key, message):
    prev = bytes([0]*16)
    for i in range(0, len(message), 16):
        block = xor_bytes(message[i:i+16], prev)
        prev = block_cipher(block, key)
    return prev

key = bytes([0x0F]*16)
X = bytes(range(16))

T = cbc_mac(key, X)
print("MAC(X):", T.hex())

X2 = xor_bytes(X, T)
msg = X + X2

T2 = cbc_mac(key, msg)
print("MAC(X || (X⊕T)):", T2.hex())

if T == T2:
    print("⚠️ Vulnerability demonstrated")
