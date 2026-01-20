# Q38: Hill cipher key recovery (2x2)

import numpy as np

P = np.array([[7, 4], [11, 15]])   # HELP
C = np.array([[8, 25], [22, 23]])  # IZWX

det = int(round(np.linalg.det(P))) % 26
det_inv = pow(det, -1, 26)

P_inv = det_inv * np.round(np.linalg.inv(P)).astype(int) % 26
K = (C @ P_inv) % 26

print("Recovered key:\n", K)
