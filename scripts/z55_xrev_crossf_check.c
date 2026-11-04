/* Independent z55 CROSSF review: exact-integer windows, direct w-residue
 * enumeration, trial-division primality, and direct genus square-class tests.
 * No code imported from the lane's factorisation/C-form scanners.
 * Input: p expected_hits, restricted to p <= 10010000000.
 * Optional --witness-only (p <= 1001000000000): do NOT recompute hits/primality;
 * only exhibit M > 0, suitable after the independent prime-coverage audit.
 * Output includes a positive genus witness for every sample, and M at 10000169.
 * Build/run under timeout and ulimit; see REVIEW_CROSSF.md. */
#include <assert.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef uint64_t U;
typedef __uint128_t W;
#define LIMIT 1200000
static int spf[LIMIT + 1];
static unsigned char squarefree[LIMIT + 1];

static U root(W n, unsigned k) {
    U lo = 0, hi = 1ULL << 30;
    while (lo + 1 < hi) {
        U m = (lo + hi) / 2;
        W v = 1;
        for (unsigned j = 0; j < k && v <= n; j++) v *= m;
        if (v <= n) lo = m; else hi = m;
    }
    return lo;
}
static U power(U a, U k, U q) {
    U r = 1;
    while (k) {
        if (k & 1) r = (W)r * a % q;
        a = (W)a * a % q; k >>= 1;
    }
    return r;
}
static int prime(U p) {
    for (U d = 2; d * d <= p; d++) if (p % d == 0) return 0;
    return p >= 2;
}
/* Square-class test of p*(-u-2w) modulo 8uw; weight for BOTH orders.
 * u,w odd squarefree, coprime and below p. */
static double weight(U p, U u, U w) {
    if (((p % 8) * ((8 - (u + 2*w) % 8) % 8)) % 8 != 1) return 0;
    U phi = 1, s = 2;
    U args[2] = {u, w};
    for (int j = 0; j < 2; j++) {
        U n = args[j];
        while (n > 1) {
            U q = spf[n];
            if (j == 0 && w % q == 0) return 0;
            U a = (q - (u + 2*w) % q) % q;
            if (power((p % q) * a % q, (q - 1)/2, q) != 1) return 0;
            phi *= q - 1; s *= 2; n /= q;
        }
    }
    return (double)s / phi;
}
int main(int argc, char **argv) {
    int witness_only = argc == 2 && strcmp(argv[1], "--witness-only") == 0;
    assert(argc == 1 || witness_only);
    squarefree[1] = 1;
    for (int n = 2; n <= LIMIT; n++) {
        if (!spf[n]) for (int m = n; m <= LIMIT; m += n) if (!spf[m]) spf[m] = n;
        int q = spf[n], m = n/q;
        squarefree[n] = squarefree[m] && m % q != 0;
    }
    U p; int expected, N = 0, zeros = 0;
    while (scanf("%" SCNu64 " %d", &p, &expected) == 2) {
        assert(p <= (witness_only ? 1001000000000ULL : 10010000000ULL) && p % 4 == 1);
        if (!witness_only) assert(prime(p));
        U u0 = root(p, 12), u1 = root(p/8, 3), y = root(p, 3);
        U x = root((W)p*p/64, 3);
        while ((W)8*u1*x > p) --x;
        assert(u1 < y);
        if (!witness_only) assert(x <= LIMIT);
        int hits = witness_only ? expected : 0;
        for (U w = y + 1; !witness_only && w <= x; w++) {
            if (!(w & 1) || !squarefree[w]) continue;
            U u = (w - p % w) % w;
            if (u <= u0 || u > u1 || u % 4 != 1 || !squarefree[u]) continue;
            if ((p + u + 2*w) % (8*u*w) == 0) hits++;
        }
        if (hits != expected) {
            fprintf(stderr, "MISMATCH p=%" PRIu64 " got=%d expected=%d\n", p, hits, expected);
            return 1;
        }
        U witness_u = 0, witness_w = 0;
        double mass = 0;
        for (U u = u0 + 1; u <= u1; u++) {
            if (u % 4 != 1 || !squarefree[u]) continue;
            for (U w = y + 1; w <= x && w <= LIMIT; w++) {
                if (!(w & 1) || !squarefree[w]) continue;
                double term = weight(p, u, w);
                mass += term;
                if (term > 0) { witness_u = u; witness_w = w; }
                if (witness_u && p != 10000169) break;
            }
            if (witness_u && p != 10000169) break;
        }
        assert(witness_u); /* exact modular tests establish M > 0 */
        printf("%" PRIu64 " %s=%d witness=(%" PRIu64 ",%" PRIu64 ")", p,
               witness_only ? "input_hits" : "hits", hits, witness_u, witness_w);
        if (p == 10000169) printf(" M=%.12f", mass);
        putchar('\n');
        N++; zeros += hits == 0;
    }
    fprintf(stderr, "mode=%s checked=%d zeros=%d mismatches=0 positive-M=%d\n",
            witness_only ? "witness-only" : "independent-hits", N, zeros, N);
    return 0;
}
