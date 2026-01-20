# Q29: SHA-3 capacity lane filling simulation (ignoring permutation)

import random

TOTAL_LANES = 25
RATE_LANES = 16
CAPACITY_LANES = 9

state = [0] * TOTAL_LANES

# First message block: rate lanes non-zero
for i in range(RATE_LANES):
    state[i] = random.randint(1, 100)

rounds = 0

while any(state[i] == 0 for i in range(RATE_LANES, TOTAL_LANES)):
    idx = random.randint(RATE_LANES, TOTAL_LANES - 1)
    state[idx] = random.randint(1, 100)
    rounds += 1

print("All capacity lanes became non-zero after", rounds, "rounds")
