import string

# ------------------------------------------------------------
# GIVEN PLAYFAIR MATRIX
# ------------------------------------------------------------
matrix = [
    ['M','F','H','I','K'],
    ['U','N','O','P','Q'],
    ['Z','V','W','X','Y'],
    ['E','L','A','R','G'],
    ['D','S','T','B','C']
]

# ------------------------------------------------------------
# FIND ROW & COLUMN OF A LETTER
# ------------------------------------------------------------
def find_position(ch):
    if ch == 'J':
        ch = 'I'
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    return None

# ------------------------------------------------------------
# PREPARE PLAINTEXT INTO DIGRAPHS
# ------------------------------------------------------------
def prepare_text(text):
    # Remove non-alpha, convert to uppercase, replace J with I
    cleaned = ""
    for ch in text:
        if ch.isalpha():
            ch = ch.upper()
            if ch == 'J':
                ch = 'I'
            cleaned += ch

    # Insert X between duplicate letters in a pair
    result = ""
    i = 0
    while i < len(cleaned):
        a = cleaned[i]
        if i + 1 < len(cleaned):
            b = cleaned[i+1]
            if a == b:
                result += a + 'X'
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + 'X'
            i += 1

    return result

# ------------------------------------------------------------
# ENCRYPT DIGRAPH
# ------------------------------------------------------------
def encrypt_pair(a, b):
    r1, c1 = find_position(a)
    r2, c2 = find_position(b)

    # RULE 1: Same row → shift right
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]

    # RULE 2: Same column → shift down
    if c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]

    # RULE 3: Rectangle → swap columns
    return matrix[r1][c2] + matrix[r2][c1]

# ------------------------------------------------------------
# FULL ENCRYPT FUNCTION
# ------------------------------------------------------------
def playfair_encrypt(text):
    prepared = prepare_text(text)
    ciphertext = ""

    for i in range(0, len(prepared), 2):
        a = prepared[i]
        b = prepared[i+1]
        ciphertext += encrypt_pair(a, b)

    return ciphertext

# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------
message = "Must see you over Cadogan West. Coming at once."

ciphertext = playfair_encrypt(message)

print("Playfair Ciphertext:")
print(ciphertext)
