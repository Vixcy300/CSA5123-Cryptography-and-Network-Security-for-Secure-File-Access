#include <stdio.h>
#include <stdint.h>

// Compute GCD
long long gcd(long long a, long long b)
{
    while(b != 0)
    {
        long long t = b;
        b = a % b;
        a = t;
    }
    return a;
}

// Extended Euclidean Algorithm
long long modinv(long long e, long long phi)
{
    long long t = 0, newt = 1;
    long long r = phi, newr = e;

    while(newr != 0)
    {
        long long q = r / newr;
        long long temp = newt; newt = t - q*newt; t = temp;
        temp = newr; newr = r - q*newr; r = temp;
    }

    if(r > 1) return -1; // no inverse
    if(t < 0) t += phi;
    return t;
}

// Fast modular exponentiation
long long modexp(long long base, long long exp, long long mod)
{
    long long result = 1;
    base %= mod;
    while(exp > 0)
    {
        if(exp % 2 == 1) result = (result * base) % mod;
        exp /= 2;
        base = (base * base) % mod;
    }
    return result;
}

int main()
{
    // Example RSA public key
    long long n = 77; // n = 7*11 for demo
    long long e = 13;

    // Ciphertext block
    long long c = 34;

    // Suppose we know a plaintext block that shares a factor with n
    long long known_plain = 11;

    // Step 1: Compute gcd
    long long factor = gcd(known_plain, n);
    printf("GCD of known plaintext and n = %lld\n", factor);

    if(factor != 1 && factor != n)
    {
        long long p = factor;
        long long q = n / p;
        printf("Factors found: p = %lld, q = %lld\n", p, q);

        // Step 2: Compute private key
        long long phi = (p-1)*(q-1);
        long long d = modinv(e, phi);
        printf("Private key d = %lld\n", d);

        // Step 3: Decrypt ciphertext
        long long decrypted = modexp(c, d, n);
        printf("Decrypted plaintext = %lld\n", decrypted);
    }
    else
    {
        printf("No useful factor found.\n");
    }

    return 0;
}

