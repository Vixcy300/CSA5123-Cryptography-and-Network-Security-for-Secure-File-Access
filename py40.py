# Q40: Monoalphabetic attack (top guesses)

from collections import Counter

ciphertext = "WKH TXLFN EURZQ IRA MXPSV"

freq = Counter(c for c in ciphertext if c.isalpha())
order = [x[0] for x in freq.most_common()]

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

for i in range(5):
    mapping = dict(zip(order, english[i:]))
    guess = ""
    for c in ciphertext:
        guess += mapping.get(c, c)
    print(f"Option {i+1}:", guess)
