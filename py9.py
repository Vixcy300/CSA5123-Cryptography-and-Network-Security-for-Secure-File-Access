import string

# ------------------------------------------------------------
# 1. Generate 5×5 matrix from keyword
# ------------------------------------------------------------
def generate_matrix(keyword):
    keyword = keyword.lower().replace("j", "i")
    matrix = []
    used = set()

    # Add keyword
    for ch in keyword:
        if ch.isalpha() and ch not in used:
            matrix.append(ch)
            used.add(ch)

    # Add remaining letters
    for ch in string.ascii_lowercase:
        if ch == 'j':
            continue
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    # Convert to 5×5
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix


# ------------------------------------------------------------
# 2. Find row, column of a letter in matrix
# ------------------------------------------------------------
def find_position(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    return None


# ------------------------------------------------------------
# 3. Decrypt a pair
# ------------------------------------------------------------
def decrypt_pair(a, b, matrix):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    # Same row → shift left
    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]

    # Same column → shift up
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]

    # Rectangle → swap corners
    else:
        return matrix[r1][c2] + matrix[r2][c1]


# ------------------------------------------------------------
# 4. Full decryption
# ------------------------------------------------------------
def playfair_decrypt(ciphertext, keyword):
    matrix = generate_matrix(keyword)
    ciphertext = ciphertext.lower().replace(" ", "").replace("\n", "")
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i+1]
        plaintext += decrypt_pair(a, b, matrix)

    return plaintext


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------
print("Playfair Cipher Decryption\n")

keyword = input("Enter Playfair key: ")

ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS 
KREHE GOYFI WTTTU OLKSY CAJPO 
BOTEI ZONTX BYBNT GONEY CUZWR 
GDSON SXBOU YWRHE BAAHY USEDQ"""

print("\n--- Ciphertext Loaded ---")
print(ciphertext)

plaintext = playfair_decrypt(ciphertext, keyword)

print("\nDecrypted Text:")
print(plaintext.upper())
