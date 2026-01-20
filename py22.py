#include <stdio.h>
#include <stdint.h>

#define BLOCK_SIZE 8  // 8-bit blocks
#define NUM_BLOCKS 3  // Test data has 3 blocks

/* Simplified S-DES encrypt (for exam/demo purposes) */
uint8_t SDES_encrypt(uint8_t plaintext, uint16_t key)
{
    // For exam/demo, simple XOR with key truncated to 8 bits
    return plaintext ^ (key & 0xFF);
}

/* Counter Mode encryption/decryption */
void CTR_mode(uint8_t *data, uint8_t *output, uint16_t key, uint8_t counter_start, int num_blocks)
{
    uint8_t counter = counter_start;

    for(int i = 0; i < num_blocks; i++)
    {
        uint8_t keystream = SDES_encrypt(counter, key);
        output[i] = data[i] ^ keystream;
        counter++;  // increment counter
    }
}

int main()
{
    // Binary plaintext: 00000001 00000010 00000100
    uint8_t plaintext[NUM_BLOCKS] = {0x01, 0x02, 0x04};
    uint8_t ciphertext[NUM_BLOCKS];
    uint8_t decrypted[NUM_BLOCKS];

    uint16_t key = 0b0111111101;  // 10-bit key
    uint8_t counter_start = 0x00; // 00000000

    // Encrypt
    CTR_mode(plaintext, ciphertext, key, counter_start, NUM_BLOCKS);

    // Decrypt (same function, CTR is symmetric)
    CTR_mode(ciphertext, decrypted, key, counter_start, NUM_BLOCKS);

    // Print results
    printf("Plaintext : ");
    for(int i = 0; i < NUM_BLOCKS; i++)
        printf("%08b ", plaintext[i]);
    printf("\n");

    printf("Ciphertext: ");
    for(int i = 0; i < NUM_BLOCKS; i++)
        printf("%08b ", ciphertext[i]);
    printf("\n");

    printf("Decrypted : ");
    for(int i = 0; i < NUM_BLOCKS; i++)
        printf("%08b ", decrypted[i]);
    printf("\n");

    return 0;
}
