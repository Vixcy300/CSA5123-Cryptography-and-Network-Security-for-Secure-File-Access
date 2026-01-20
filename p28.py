# Q28: Diffie-Hellman Key Exchange

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# Public values
q = 23
a = 5

# Secrets
x = 6   # Alice
y = 15  # Bob

A = mod_exp(a, x, q)
B = mod_exp(a, y, q)

KA = mod_exp(B, x, q)
KB = mod_exp(A, y, q)

print("Alice sends:", A)
print("Bob sends:", B)
print("Alice key:", KA)
print("Bob key  :", KB)
