import math
import random
from collections import Counter

# ---------------------------------------------------
# English bigram scoring table (log probabilities)
# ---------------------------------------------------
# Based on wordlists — precomputed frequency log table (short version)
# You can extend it if needed.
bigram_scores = {}
with open("bigrams.txt", "r") as f:
    for line in f:
        bg, score = line.split()
        bigram_scores[bg] = float(score)

def score_text(text):
    """Return English likelihood score using bigrams."""
    score = 0
    for i in range(len(text)-1):
        bg = text[i:i+2]
        if bg in bigram_scores:
            score += bigram_scores[bg]
        else:
            score += -10  # penalize rare bigrams
    return score


# ---------------------------------------------------
# Helper: apply key to decrypt
# ---------------------------------------------------
def decrypt(cipher, key):
    table = {c: p for c, p in zip(key, "abcdefghijklmnopqrstuvwxyz")}
    result = ""
    for ch in cipher:
        if ch.isalpha():
            result += table[ch.lower()]
        else:
            result += ch
    return result


# ---------------------------------------------------
# Generate random key
# ---------------------------------------------------
def random_key():
    letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(letters)
    return "".join(letters)


# ---------------------------------------------------
# Hill-climbing search for best key
# ---------------------------------------------------
def hill_climb(cipher, iterations=2000):
    key = random_key()
    best_score = score_text(decrypt(cipher, key))
    best_key = key

    for _ in range(iterations):
        new_key = list(best_key)
        a, b = random.sample(range(26), 2)
        new_key[a], new_key[b] = new_key[b], new_key[a]
        new_key = "".join(new_key)

        new_score = score_text(decrypt(cipher, new_key))
        if new_score > best_score:
            best_key = new_key
            best_score = new_score

    return best_key, best_score


# ---------------------------------------------------
# Attack engine: produce top N plaintexts
# ---------------------------------------------------
def attack(cipher, top_n=10):
    candidates = []

    print("\n[*] Running automatic monoalphabetic substitution attack...\n")

    # Run multiple hill-climb restarts
    for i in range(40):
        print(f"  Attempt {i+1}/40")
        key, score = hill_climb(cipher)
        plaintext = decrypt(cipher, key)
        candidates.append((score, plaintext, key))

    # Sort by score (higher = more English-like)
    candidates.sort(reverse=True, key=lambda x: x[0])

    print("\n===== TOP CANDIDATES =====\n")
    for i in range(top_n):
        print(f"Rank {i+1}")
        print("Score:", candidates[i][0])
        print("Key:", candidates[i][2])
        print("Plaintext:", candidates[i][1])
        print("-" * 40)


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------
ciphertext = input("Enter monoalphabetic substitution ciphertext:\n")

attack(ciphertext, top_n=10)
