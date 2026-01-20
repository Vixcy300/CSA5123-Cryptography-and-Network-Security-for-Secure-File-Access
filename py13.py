import numpy as np
from math import gcd

def mod_inverse_matrix(A, mod=26):
    det = int(round(np.linalg.det(A)))
    det_mod = det % mod

    if gcd(det_mod, mod) != 1:
        raise ValueError(f"Matrix is NOT invertible mod {mod}! det={det_mod}")

    det_inv = pow(det_mod, -1, mod)

    adj = np.array([
        [ A[1][1], -A[0][1]],
        [-A[1][0],  A[0][0]]
    ])

    return (det_inv * adj) % mod

# Example invertible plaintext matrix
P = np.array([[7, 4],   # H E
              [11, 15]])  # L P

# Example ciphertext matrix (random example)
C = np.array([[3, 10],
              [20, 5]])

try:
    P_inv = mod_inverse_matrix(P)
    print("P inverse:\n", P_inv)

    K = (C @ P_inv) % 26
    print("\nRecovered Key K:\n", K)

except ValueError as e:
    print(e)
