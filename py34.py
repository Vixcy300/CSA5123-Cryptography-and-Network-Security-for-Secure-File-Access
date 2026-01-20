# Q34: ECB, CBC, CFB with padding (Python)

BLOCK_SIZE = 8  # bytes

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def add_padding(data):
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    if pad_len == 0:
        pad_len = BLOCK_SIZE
    return data + bytes([0x80]) + bytes([0x00] * (pad_len - 1))

def ecb_encrypt(data, key):
    out = b""
    for i in range(0, len(data), BLOCK_SIZE):
        out += xor_bytes(data[i:i+BLOCK_SIZE], key)
    return out

def cbc_encrypt(data, key, iv):
    out = b""
    prev = iv
    for i in range(0, len(data), BLOCK_SIZE):
        block = xor_bytes(data[i:i+BLOCK_SIZE], prev)
        enc = xor_bytes(block, key)
        out += enc
        prev = enc
    return out

def cfb_encrypt(data, key, iv):
    out = b""
    prev = iv
    for i in range(0, len(data), BLOCK_SIZE):
        temp = xor_bytes(prev, key)
        enc = xor_bytes(temp, data[i:i+BLOCK_SIZE])
        out += enc
        prev = enc
    return out

def print_hex(label, data):
    print(label, ":", data.hex().upper())

# ===== INPUT =====
plaintext = b"HELLO BLOCK WORLD!"
key = bytes([0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x70, 0x81])
iv = bytes([0x00] * BLOCK_SIZE)

# Padding
padded = add_padding(plaintext)

# Encryption
ecb = ecb_encrypt(padded, key)
cbc = cbc_encrypt(padded, key, iv)
cfb = cfb_encrypt(padded, key, iv)

# Output
print_hex("Plaintext (padded)", padded)
print_hex("ECB Cipher", ecb)
print_hex("CBC Cipher", cbc)
print_hex("CFB Cipher", cfb)
