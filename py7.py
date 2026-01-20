from collections import Counter

ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83 
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8* 
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

# ----------------------------------------
# FREQUENCY ANALYSIS
# ----------------------------------------
# Remove spaces/newlines
clean = ciphertext.replace(" ", "").replace("\n", "")

freq = Counter(clean)

print("\n===== FREQUENCY ANALYSIS =====")
for ch, count in freq.most_common():
    print(f"'{ch}': {count}")

# ----------------------------------------
# OPTIONAL: MANUAL SUBSTITUTION
# ----------------------------------------
# After guessing mappings, place them here:
# Example (NOT real key, you must fill):
mapping = {
    # 'cipher_symbol': 'plaintext_letter'
    # e.g. '*': 'E'
}

def substitute(cipher, mapping):
    result = ""
    for ch in cipher:
        if ch in mapping:
            result += mapping[ch]
        else:
            result += ch  # leave as-is
    return result

print("\n===== PARTIAL DECRYPTION (with mapping) =====")
print(substitute(ciphertext, mapping))
