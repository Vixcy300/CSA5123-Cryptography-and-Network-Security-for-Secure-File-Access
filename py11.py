import math
from math import factorial, log2

# 25! = all possible Playfair keys (I/J merged)
total_keys = factorial(25)

# Effectively unique keys = 25! / (5! * 5!)
unique_keys = total_keys // (factorial(5) * factorial(5))

# Convert to powers of 2
power_total = log2(total_keys)
power_unique = log2(unique_keys)

print("===== PLAYFAIR CIPHER KEY SPACE =====")
print(f"Total possible keys (ignoring duplicates): 25! = {total_keys:.5e}")
print(f"Approx as 2^{power_total:.2f}")

print("\nUnique effective keys (after removing equivalences):")
print(f"25! / (5! * 5!) = {unique_keys:.5e}")
print(f"Approx as 2^{power_unique:.2f}")
