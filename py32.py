# Q32: DSA vs RSA signature difference

import random

def hash_msg(msg):
    return sum(ord(c) for c in msg) % 101

def rsa_sign(msg, d, n):
    h = hash_msg(msg)
    return pow(h, d, n)

def dsa_sign(msg, x, q):
    h = hash_msg(msg)
    k = random.randint(1, q-1)
    return (h * k + x) % q

msg = "HELLO"

print("RSA signatures:")
print(rsa_sign(msg, 17, 3233))
print(rsa_sign(msg, 17, 3233))

print("\nDSA signatures:")
print(dsa_sign(msg, 23, 101))
print(dsa_sign(msg, 23, 101))
