/* z48_ltfable_minlevels.c — for every n <= N record the least level t and least endpoint min(u,v)
 * among (a) (*) words (4 | t) and (b) five-slice certificate words (any slot), and the least level among
 * interior words (t,u,v >= 3).  Endpoints: uint16 saturating (65535 = none); levels: uint32 (0xFFFFFFFF = none).
 * Then print, for primes p = 1 (mod 4): max of each statistic per dyadic range, normalised by log p and log^2 p,
 * and the full list of primes where the (*) least endpoint exceeds (log p)^2 or the least level exceeds 8 log^2 p.
 * Usage: z48_ltfable_minlevels N outprefix
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static inline void mn(uint16_t *a, uint64_t i, int64_t x) { uint16_t y = x > 65535 ? 65535 : (uint16_t)x; if (y < a[i]) a[i] = y; }
static inline void mn32(uint32_t *a, uint64_t i, int64_t x) { uint32_t y = x > 0xFFFFFFFEll ? 0xFFFFFFFEu : (uint32_t)x; if (y < a[i]) a[i] = y; }
int main(int argc, char **argv) {
    uint64_t N = strtoull(argv[1], 0, 10);
    uint32_t *STt = malloc(4 * (N + 1)), *ANt = malloc(4 * (N + 1)), *I3t = malloc(4 * (N + 1));
    uint16_t *STu = malloc(2 * (N + 1)), *ANu = malloc(2 * (N + 1));
    for (uint64_t i = 0; i <= N; i++) { STt[i] = ANt[i] = I3t[i] = 0xFFFFFFFFu; STu[i] = ANu[i] = 65535; }
    for (int64_t u = 1; ; u++) {
        if (u * u - 2 * u > (int64_t)N) break;
        for (int64_t v = u; ; v++) {
            int64_t uv = u * v;
            int64_t tmin = (u + v + uv - 1) / uv; if (tmin < 1) tmin = 1;
            if (tmin * uv - u - v > (int64_t)N) break;
            for (int64_t t = tmin; ; t++) {
                int64_t n = t * uv - u - v;
                if (n > (int64_t)N) break;
                int st = (t % 4 == 0);
                int any = st || (u % 4 == 0) || (v % 4 == 0) || ((t * u - 1) % 4 == 0) || ((t * v - 1) % 4 == 0);
                if (st) { mn32(STt, n, t); mn(STu, n, u); }
                if (any) { mn32(ANt, n, t); mn(ANu, n, u); }
                if (u >= 3 && t >= 3) mn32(I3t, n, t);
            }
        }
    }
    uint8_t *comp = calloc(N / 2 + 1, 1);
    for (uint64_t i = 1; (2 * i + 1) * (2 * i + 1) <= N; i++) { if (comp[i]) continue; uint64_t p = 2 * i + 1; for (uint64_t j = (p * p - 1) / 2; j <= N / 2; j += p) comp[j] = 1; }
    char fn[512]; snprintf(fn, sizeof fn, "%s.txt", argv[2]);
    FILE *g = fopen(fn, "w");
    fprintf(g, "# N=%llu; per dyadic range [2^k,2^(k+1)) over primes p=1(4): count, max STu, max STu/log^2p, max STt/4 (=C_min), max C_min/log^2 p, max ANu, max ANt, max I3t; (*)-failures excluded from STu/STt maxima\n", (unsigned long long)N);
    for (int k = 2; (1ULL << k) <= N; k++) {
        uint64_t lo = 1ULL << k, hi = (1ULL << (k + 1)) - 1; if (hi > N) hi = N;
        uint64_t cnt = 0; double mSTu = 0, mSTur = 0, mC = 0, mCr = 0, mANu = 0, mANt = 0, mI3 = 0; uint64_t aSTu = 0, aC = 0, aANu = 0, aANt = 0, aI3 = 0;
        for (uint64_t p = lo + ((lo % 4 == 1) ? 0 : (4 - (lo % 4) + 1) % 4); p <= hi; p += 4) {
            if (p % 4 != 1 || p < 5 || comp[p / 2]) continue; cnt++;
            double L = log((double)p);
            if (STu[p] != 65535) { if (STu[p] > mSTu) { mSTu = STu[p]; aSTu = p; } if (STu[p] / (L * L) > mSTur) mSTur = STu[p] / (L * L);
                                   double C = STt[p] / 4.0; if (C > mC) { mC = C; aC = p; } if (C / (L * L) > mCr) mCr = C / (L * L); }
            if (ANu[p] > mANu) { mANu = ANu[p]; aANu = p; } if (ANt[p] > mANt) { mANt = ANt[p]; aANt = p; }
            if (I3t[p] != 0xFFFFFFFFu && I3t[p] > mI3) { mI3 = I3t[p]; aI3 = p; }
        }
        fprintf(g, "k=%2d [%llu,%llu] n=%llu maxSTu=%g(@%llu) maxSTu/L2=%.3f maxCmin=%g(@%llu) maxCmin/L2=%.3f maxANu=%g(@%llu) maxANt=%g(@%llu) maxI3t=%g(@%llu)\n",
                k, (unsigned long long)lo, (unsigned long long)hi, (unsigned long long)cnt, mSTu, (unsigned long long)aSTu, mSTur, mC, (unsigned long long)aC, mCr, mANu, (unsigned long long)aANu, mANt, (unsigned long long)aANt, mI3, (unsigned long long)aI3);
    }
    fprintf(g, "# primes p=1(4) with STu > (log p)^2 or C_min > (log p)^2, or ANu > log p + 5 (five-slice least endpoint):\n");
    for (uint64_t p = 5; p <= N; p += 4) {
        if (comp[p / 2]) continue; double L = log((double)p);
        if (STu[p] != 65535 && (STu[p] > L * L || STt[p] / 4.0 > L * L)) fprintf(g, "BIG %llu STu=%u Cmin=%u ANu=%u ANt=%u\n", (unsigned long long)p, STu[p], STt[p] / 4, ANu[p], ANt[p]);
        if (ANu[p] > L + 5) fprintf(g, "ANUBIG %llu ANu=%u ANt=%u STu=%u\n", (unsigned long long)p, ANu[p], ANt[p], STu[p]);
    }
    fclose(g); printf("done\n"); return 0;
}
