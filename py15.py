from collections import Counter

def decrypt_shift(ct, k):
    pt = ""
    for ch in ct:
        if ch.isalpha():
            pt += chr((ord(ch)-97-k)%26 + 97)
        else:
            pt += ch
    return pt

def freq_attack(ct, top_n=10):
    freq = Counter([ch for ch in ct if ch.isalpha()])
    sorted_freq = freq.most_common()

    # assume most common = 'e'
    probable_plains = []
    for ch, _ in sorted_freq[:top_n]:
        k = (ord(ch) - ord('e')) % 26
        plain = decrypt_shift(ct, k)
        probable_plains.append((k, plain))
    return probable_plains


ciphertext = input("Enter additive cipher text: ")
results = freq_attack(ciphertext, 10)

for k, pt in results:
    print(f"\nKey {k}: {pt}")
