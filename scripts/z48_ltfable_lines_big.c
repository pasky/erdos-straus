/* z48_ltfable_lines_big.c — lean version of z48_ltfable_lines.c for N up to ~2e9:
 * keeps only three saturating uint8 arrays: ST (= R(n), words with 4 | t), I3 (words with t,u,v >= 3),
 * W2 (words with t,u,v >= 2).  Reports: all n with I3 = 0 or W2 = 0; primes p = 1 (mod 4) with ST = 0.
 * Usage: z48_ltfable_lines_big N outprefix.   Memory: 3N bytes of counters + N/2 bytes of prime sieve.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static inline void inc(uint8_t *a, uint64_t i) { if (a[i] < 255) a[i]++; }
int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s N outprefix\n", argv[0]); return 1; }
    uint64_t N = strtoull(argv[1], 0, 10);
    uint8_t *ST = calloc(N + 1, 1), *I3 = calloc(N + 1, 1), *W2 = calloc(N + 1, 1);
    if (!ST || !I3 || !W2) { fprintf(stderr, "alloc failed\n"); return 2; }
    for (int64_t u = 1; ; u++) {
        if (u * u - 2 * u > (int64_t)N) break;
        for (int64_t v = u; ; v++) {
            int64_t uv = u * v;
            int64_t tmin = (u + v + uv - 1) / uv;
            if (tmin < 1) tmin = 1;
            if (tmin * uv - u - v > (int64_t)N) break;
            int mult = (u == v) ? 1 : 2;
            int mp = (u >= 3) && (v >= 3);
            int ge2 = (u >= 2) && (v >= 2);
            for (int64_t t = tmin; ; t++) {
                int64_t n = t * uv - u - v;
                if (n > (int64_t)N) break;
                for (int k = 0; k < mult; k++) {
                    if (t % 4 == 0) inc(ST, n);
                    if (mp && t >= 3) inc(I3, n);
                    if (ge2 && t >= 2) inc(W2, n);
                }
            }
        }
    }
    uint8_t *comp = calloc(N / 2 + 1, 1);
    for (uint64_t i = 1; (2 * i + 1) * (2 * i + 1) <= N; i++) {
        if (comp[i]) continue;
        uint64_t p = 2 * i + 1;
        for (uint64_t j = (p * p - 1) / 2; j <= N / 2; j += p) comp[j] = 1;
    }
    char fn[512]; snprintf(fn, sizeof fn, "%s.txt", argv[2]);
    FILE *g = fopen(fn, "w");
    fprintf(g, "# N = %llu\n", (unsigned long long)N);
    uint64_t ni3 = 0, nw2 = 0, nst = 0, np = 0;
    for (uint64_t n = 3; n <= N; n++) {
        if (I3[n] == 0) { ni3++; if (ni3 <= 5000) { uint64_t m = (uint64_t)sqrt((double)n); while (m*m > n) m--; while ((m+1)*(m+1) <= n) m++; fprintf(g, "I30 %llu sq=%d W2=%u\n", (unsigned long long)n, m*m == n, W2[n]); } }
        if (W2[n] == 0) { nw2++; if (nw2 <= 5000) fprintf(g, "W20 %llu\n", (unsigned long long)n); }
    }
    for (uint64_t p = 5; p <= N; p += 4) { if (comp[p / 2]) continue; np++; if (ST[p] == 0) { nst++; fprintf(g, "ST0 %llu I3=%u W2=%u\n", (unsigned long long)p, I3[p], W2[p]); } }
    fprintf(g, "# I3 failures %llu, W2 failures %llu, primes=1(4) %llu, (*) failures %llu\n",
            (unsigned long long)ni3, (unsigned long long)nw2, (unsigned long long)np, (unsigned long long)nst);
    fclose(g);
    printf("done N=%llu I3fail=%llu W2fail=%llu primes=%llu STfail=%llu\n", (unsigned long long)N,
           (unsigned long long)ni3, (unsigned long long)nw2, (unsigned long long)np, (unsigned long long)nst);
    return 0;
}
