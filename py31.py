# Q31: CMAC Subkey generation (128-bit example)

BLOCK_SIZE = 16  # bytes (128-bit)
Rb_128 = 0x87

def left_shift(block):
    out = bytearray(BLOCK_SIZE)
    carry = 0
    for i in reversed(range(BLOCK_SIZE)):
        out[i] = ((block[i] << 1) & 0xFF) | carry
        carry = 1 if (block[i] & 0x80) else 0
    return out

def xor_rb(block):
    block[-1] ^= Rb_128
    return block

# Dummy block cipher output on 0^128
L = bytearray(range(1, BLOCK_SIZE + 1))

K1 = left_shift(L)
if L[0] & 0x80:
    K1 = xor_rb(K1)

K2 = left_shift(K1)
if K1[0] & 0x80:
    K2 = xor_rb(K2)

print("L :", list(L))
print("K1:", list(K1))
print("K2:", list(K2))
