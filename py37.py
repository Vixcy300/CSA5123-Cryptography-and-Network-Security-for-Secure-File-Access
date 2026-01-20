# Q37: Frequency attack (monoalphabetic)

import string
from collections import Counter

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

ciphertext = "GSRH RH Z HVXIVG NVHHZTV"

freq = Counter(c for c in ciphertext if c.isalpha())
sorted_letters = [x[0] for x in freq.most_common()]

mapping = dict(zip(sorted_letters, english))

plaintext = ""
for c in ciphertext:
    plaintext += mapping.get(c, c)

print("Guess:", plaintext)
