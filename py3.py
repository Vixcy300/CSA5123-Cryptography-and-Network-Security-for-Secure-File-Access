import string

# -------------------------
# FUNCTION: Create 5x5 matrix using keyword
# -------------------------
def generate_matrix(keyword):
    keyword = keyword.lower().replace("j", "i")
    matrix = []
    used = set()

    for ch in keyword:
        if ch not in used and ch.isalpha():
            used.add(ch)
            matrix.append(ch)

    for ch in string.ascii_lowercase:
        if ch == 'j':  # I/J merge
            continue
        if ch not in used:
            used.add(ch)
            matrix.append(ch)

    # Convert into 5x5 matrix
    matrix_5x5 = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix_5x5


# -------------------------
# FUNCTION: Prepare plaintext into digraphs (pairs)
# -------------------------
def prepare_plaintext(text):
    text = text.lower().replace(" ", "").replace("j", "i")
    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i+1]
            if a == b:
                result += a + 'x'
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + 'x'
            i += 1

    return result


# -------------------------
# FUNCTION: Find position in matrix
# -------------------------
def find_position(matrix, ch):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == ch:
                return row, col
    return None


# -------------------------
# FUNCTION: Encrypt plaintext pairs
# -------------------------
def encrypt_pair(a, b, matrix):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    # Rule 1: Same row -> shift right
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]

    # Rule 2: Same column -> shift down
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]

    # Rule 3: Rectangle -> swap columns
    else:
        return matrix[r1][c2] + matrix[r2][c1]


# -------------------------
# MAIN ENCRYPT FUNCTION
# -------------------------
def playfair_encrypt(plaintext, keyword):
    matrix = generate_matrix(keyword)
    plaintext = prepare_plaintext(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1]
        ciphertext += encrypt_pair(a, b, matrix)

    return ciphertext


# -------------------------
# MAIN PROGRAM
# -------------------------
print("Playfair Cipher Encryption\n")

keyword = input("Enter keyword: ")
plaintext = input("Enter plaintext: ")

ciphertext = playfair_encrypt(plaintext, keyword)

print("Encrypted Text:", ciphertext)
