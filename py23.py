#include <stdio.h>
#include <string.h>

/* --- Simplified S-DES Encryption/Decryption --- */

/* Example S-DES permutation functions (simplified for exam) */
unsigned char permute(unsigned char b, unsigned char p[], int n)
{
    unsigned char res = 0;
    for(int i = 0; i < n; i++)
        res |= ((b >> (8 - p[i])) & 1) << (7 - i);
    return res;
}

/* Simplified S-DES encrypt/decrypt as XOR with key for demonstration */
unsigned char SDES_encrypt(unsigned char plaintext, unsigned char key)
{
    return plaintext ^ key;  // placeholder for actual S-DES
}

unsigned char SDES_decrypt(unsigned char ciphertext, unsigned char key)
{
    return ciphertext ^ key;  // placeholder for actual S-DES
}

/* CBC Encryption */
void CBC_encrypt(unsigned char *pt, unsigned char *ct, int len,
                 unsigned char key, unsigned char IV)
{
    unsigned char prev = IV;
    for(int i = 0; i < len; i++)
    {
        unsigned char x = pt[i] ^ prev;
        ct[i] = SDES_encrypt(x, key);
        prev = ct[i];
    }
}

/* CBC Decryption */
void CBC_decrypt(unsigned char *ct, unsigned char *pt, int len,
                 unsigned char key, unsigned char IV)
{
    unsigned char prev = IV;
    for(int i = 0; i < len; i++)
    {
        unsigned char x = SDES_decrypt(ct[i], key);
        pt[i] = x ^ prev;
        prev = ct[i];
    }
}

int main()
{
    unsigned char plaintext[] = "HELLO S-DES CBC"; // 14 bytes
    int len = strlen((char*)plaintext);

    unsigned char ciphertext[256], decrypted[256];

    unsigned char key = 0b1010011010;   // example 10-bit key
    unsigned char IV  = 0b10101010;     // provided binary IV

    // Encrypt
    CBC_encrypt(plaintext, ciphertext, len, key, IV);

    // Decrypt
    CBC_decrypt(ciphertext, decrypted, len, key, IV);
    decrypted[len] = '\0';

    // Display results
    printf("Plaintext: %s\n", plaintext);

    printf("Ciphertext (hex): ");
    for(int i = 0; i < len; i++)
        printf("%02X ", ciphertext[i]);
    printf("\n");

    printf("Decrypted text: %s\n", decrypted);

    return 0;
}
