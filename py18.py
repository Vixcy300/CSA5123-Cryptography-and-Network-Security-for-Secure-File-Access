# DES PC-1 table (maps 64->56 bits)
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# PC-2 table (from 56 bits to 48-bit subkey)
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

# Shift schedule for C and D
shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


# -------------------------------------------------------
# Helper: track bit positions instead of actual bits
# -------------------------------------------------------
def left_shift_list(L, n):
    return L[n:] + L[:n]


# -------------------------------------------------------
# MAIN CHECKER
# -------------------------------------------------------
def analyze_des_key_origin():

    # Step 1 → Apply PC-1, but instead of real bits,
    # we store ORIGINAL BIT POSITIONS 1–64.
    mapped = PC1[:]       # these are original positions
    C = mapped[:28]
    D = mapped[28:]

    # For 16 subkeys
    print("\n===== DES BIT ORIGIN ANALYSIS =====")
    for round in range(16):

        # Step 2: apply shifts
        C = left_shift_list(C, shifts[round])
        D = left_shift_list(D, shifts[round])

        CD = C + D   # join 56 bits

        # Step 3: apply PC-2 to produce subkey positions
        subkey_positions = [CD[i-1] for i in PC2]

        left24  = subkey_positions[:24]
        right24 = subkey_positions[24:]

        print(f"\nRound {round+1} subkey:")
        print("Left 24 bits come from original positions:", left24)
        print("Right 24 bits come from original positions:", right24)

        # Check disjointness
        left_from_C = all(pos in range(1, 29*3) for pos in left24)
        right_from_D = all(pos in range(29, 65) for pos in right24)

        print("Left half from C-set only?  →", left_from_C)
        print("Right half from D-set only? →", right_from_D)


# Run analysis
analyze_des_key_origin()
