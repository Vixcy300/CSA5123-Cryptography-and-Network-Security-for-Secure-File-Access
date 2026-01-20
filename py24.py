#include <stdio.h>
#include <math.h>

// Fast modular exponentiation
long long modexp(long long base, long long exp, long long mod)
{
    long long result = 1;
    base = base % mod;
    while(exp > 0)
    {
        if(exp % 2 == 1)
            result = (result * base) % mod;
        exp = exp / 2;
        base = (base * base) % mod;
    }
    return result;
}

int main()
{
    long long n = 3599;
    long long e = 31;
    long long d = 3031; // private key

    long long plaintext, ciphertext, decrypted;

    // Example: Encrypt 123
    plaintext = 123;
    ciphertext = modexp(plaintext, e, n);
    decrypted = modexp(ciphertext, d, n);

    printf("RSA Encryption/Decryption Demo\n");
    printf("Public Key (e,n): (%lld, %lld)\n", e, n);
    printf("Private Key (d,n): (%lld, %lld)\n", d, n);
    printf("Plaintext: %lld\n", plaintext);
    printf("Ciphertext: %lld\n", ciphertext);
    printf("Decrypted: %lld\n", decrypted);

    return 0;
}
