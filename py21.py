#include <stdio.h>
#include <string.h>

#define BLOCK_SIZE 8   // 64-bit block
#define MAX_LEN 256    // max plaintext length

/* Simple XOR block cipher for demonstration */
void encrypt_block(unsigned char *pt, unsigned char *key, unsigned char *ct)
{
    for(int i = 0; i < BLOCK_SIZE; i++)
        ct[i] = pt[i] ^ key[i];
}

void decrypt_block(unsigned char *ct, unsigned char *key, unsigned char *pt)
{
    for(int i = 0; i < BLOCK_SIZE; i++)
        pt[i] = ct[i] ^ key[i];
}

/* XOR helper */
void XOR(unsigned char *a, unsigned char *b, unsigned char *out)
{
    for(int i = 0; i < BLOCK_SIZE; i++)
        out[i] = a[i] ^ b[i];
}

/* Padding: 1-bit followed by zeros */
int pad(unsigned char *data, int len)
{
    int padLen = BLOCK_SIZE - (len % BLOCK_SIZE);
    data[len] = 0x80; // 10000000 in binary
    for(int i = 1; i < padLen; i++)
        data[len + i] = 0x00;
    return len + padLen; // new length after padding
}

/* ECB Mode */
void ECB(unsigned char *pt, unsigned char *key, unsigned char *ct, int len)
{
    for(int i = 0; i < len; i += BLOCK_SIZE)
        encrypt_block(pt + i, key, ct + i);
}

/* CBC Mode */
void CBC(unsigned char *pt, unsigned char *key, unsigned char *iv,
         unsigned char *ct, int len)
{
    unsigned char prev[BLOCK_SIZE];
    memcpy(prev, iv, BLOCK_SIZE);

    for(int i = 0; i < len; i += BLOCK_SIZE)
    {
        unsigned char tmp[BLOCK_SIZE];
        XOR(pt + i, prev, tmp);
        encrypt_block(tmp, key, ct + i);
        memcpy(prev, ct + i, BLOCK_SIZE);
    }
}

/* CFB Mode (1 block feedback) */
void CFB(unsigned char *pt, unsigned char *key, unsigned char *iv,
         unsigned char *ct, int len)
{
    unsigned char feedback[BLOCK_SIZE];
    memcpy(feedback, iv, BLOCK_SIZE);

    for(int i = 0; i < len; i += BLOCK_SIZE)
    {
        unsigned char tmp[BLOCK_SIZE];
        encrypt_block(feedback, key, tmp);
        XOR(tmp, pt + i, ct + i);
        memcpy(feedback, ct + i, BLOCK_SIZE);
    }
}

/* Demo main program */
int main()
{
    unsigned char plaintext[MAX_LEN] = "HELLO WORLD THIS IS CBC ECB CFB DEMO";
    unsigned char key[BLOCK_SIZE]   = "SECUREKY";
    unsigned char iv[BLOCK_SIZE]    = "INITVEC1";

    int len = strlen((char*)plaintext);

    // Pad plaintext to multiple of block size
    int paddedLen = pad(plaintext, len);

    unsigned char ecb_ct[MAX_LEN], cbc_ct[MAX_LEN], cfb_ct[MAX_LEN];

    // Encrypt in each mode
    ECB(plaintext, key, ecb_ct, paddedLen);
    CBC(plaintext, key, iv, cbc_ct, paddedLen);
    CFB(plaintext, key, iv, cfb_ct, paddedLen);

    // Display ciphertexts in hex
    printf("ECB Ciphertext:\n");
    for(int i = 0; i < paddedLen; i++)
        printf("%02X ", ecb_ct[i]);
    printf("\n\nCBC Ciphertext:\n");
    for(int i = 0; i < paddedLen; i++)
        printf("%02X ", cbc_ct[i]);
    printf("\n\nCFB Ciphertext:\n");
    for(int i = 0; i < paddedLen; i++)
        printf("%02X ", cfb_ct[i]);
    printf("\n");

    return 0;
}
