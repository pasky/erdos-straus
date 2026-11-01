// z52d pass2 NC3: enumerate level-3 words t,u,v>=2 with tuv-u-v=p, i.e. A=tu-1 | p+u, t=(A+1)/u, v=(p+u)/A.
// Usage: words P_LO P_HI [mod8eq1]  -> per prime: p nwords nA nQNR nQR allQR(0/1) (ES5 failure at p iff allQR)
// Uses sieve of smallest prime factor up to 2*P_HI+2 for divisor enumeration of p+u.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static uint32_t *spf;
static int ndiv; static uint64_t divs[4096];
static void gen_divs(uint64_t m) {
    // enumerate all divisors of m via spf
    ndiv = 1; divs[0] = 1;
    while (m > 1) {
        uint32_t q = spf[m]; int e = 0;
        while (m % q == 0) { m /= q; e++; }
        int cur = ndiv; uint64_t pk = 1;
        for (int k = 1; k <= e; k++) {
            pk *= q;
            for (int i = 0; i < cur; i++) divs[ndiv++] = divs[i] * pk;
        }
    }
}
static int legendre(uint64_t a, uint64_t p) {
    // a mod p, p odd prime
    uint64_t r = a % p; if (r == 0) return 0;
    // Euler criterion via modpow
    uint64_t res = 1, b = r, e = (p - 1) / 2;
    while (e) { if (e & 1) res = (unsigned __int128)res * b % p; b = (unsigned __int128)b * b % p; e >>= 1; }
    return res == 1 ? 1 : -1;
}
int main(int argc, char **argv) {
    uint64_t lo = atoll(argv[1]), hi = atoll(argv[2]);
    int only18 = argc > 3 ? atoi(argv[3]) : 0;
    uint64_t N = 2 * hi + 4;
    spf = calloc(N + 1, sizeof(uint32_t));
    for (uint64_t i = 2; i <= N; i++) if (!spf[i]) for (uint64_t j = i; j <= N; j += i) if (!spf[j]) spf[j] = i;
    for (uint64_t p = lo; p <= hi; p++) {
        if (p < 5 || spf[p] != p) continue;
        if (only18 && p % 8 != 1) continue;
        int nw = 0; 
        // collect distinct A values
        uint64_t *As = malloc(sizeof(uint64_t) * 100000); int nA = 0;
        for (uint64_t u = 2; u <= p; u++) {
            uint64_t M = p + u;
            gen_divs(M);
            for (int i = 0; i < ndiv; i++) {
                uint64_t A = divs[i];
                if (A + 1 < 2 * u) continue;           // t >= 2
                if ((A + 1) % u) continue;
                uint64_t t = (A + 1) / u; if (t < 2) continue;
                uint64_t v = M / A; if (v < 2) continue;
                nw++;
                if (nA < 100000) As[nA++] = t * u - 1;
            }
        }
        // distinct A
        int nq = 0, nr = 0;
        // sort+unique
        for (int i = 1; i < nA; i++) { uint64_t x = As[i]; int j = i - 1; while (j >= 0 && As[j] > x) { As[j+1] = As[j]; j--; } As[j+1] = x; }
        int nd = 0; for (int i = 0; i < nA; i++) if (i == 0 || As[i] != As[i-1]) As[nd++] = As[i];
        for (int i = 0; i < nd; i++) { int L = legendre(As[i], p); if (L == 1) nq++; else if (L == -1) nr++; }
        printf("%llu %d %d %d %d %d\n", (unsigned long long)p, nw, nd, nr, nq, nr == 0 ? 1 : 0);
        free(As);
    }
    return 0;
}
