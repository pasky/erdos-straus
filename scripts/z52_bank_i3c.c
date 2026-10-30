/* z52_bank_i3c.c — census of I3_C(p) for primes p = 1 (mod 4) in [lo, hi]  (z52 bank, T1).
 *
 * I3_C(p) = #{(t,u,v) in Z_{>=3}^3 : t u v - u - v = p, some coordinate in C_p},  C_p = 4Z u (8Z - p).
 * Method (independent of the board's code): a word with endpoints u <= v has v (tu - 1) = p + u, A := tu - 1 | p + u,
 * A = -1 (mod u), and (tu-1)u <= p + u, i.e. t u^2 <= p + 2u, so with t >= 3: 3u^2 - 2u <= p.  For every endpoint
 * u >= 3 in that range we factor p + u (smallest-prime-factor table), run over all divisors A = -1 (mod u) with
 * t = (A+1)/u >= 3 and v = (p+u)/A >= 3 (v >= u is NOT imposed, so words may be met twice; harmless for existence),
 * and test the coordinate condition.  Stops at the first certifying interior word.  A prime is reported as a zero
 * only after the complete u-range is exhausted.
 * Output: zeros, and the distribution of the least endpoint u at which a certifying interior word is first met.
 * usage: z52_bank_i3c lo hi
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef uint64_t u64;
static uint32_t *spf;
static int inC(u64 x, u64 p) { return (x % 4 == 0) || ((x + p) % 8 == 0); }

int main(int argc, char **argv) {
  u64 lo = strtoull(argv[1], 0, 10), hi = strtoull(argv[2], 0, 10);
  u64 umaxall = (u64)sqrt((double)hi) + 10, M = hi + umaxall + 10;
  spf = calloc(M + 1, 4);
  for (u64 i = 2; i <= M; i++) if (!spf[i]) { spf[i] = (uint32_t)i; if (i * i <= M) for (u64 j = i * i; j <= M; j += i) if (!spf[j]) spf[j] = (uint32_t)i; }
  u64 nprimes = 0, nzero = 0, hist[64] = {0}, worst_u = 0, worst_p = 0;
  u64 divs[20000];
  for (u64 p = lo; p <= hi; p++) {
    if (p % 4 != 1 || p < 5 || spf[p] != p) continue;
    nprimes++;
    int found = 0; u64 ufound = 0;
    for (u64 u = 3; 3 * u * u - 2 * u <= p && !found; u++) {
      u64 N = p + u, t0 = N; int nd = 1; divs[0] = 1;
      while (t0 > 1) {
        u64 q = spf[t0]; int e = 0; while (t0 % q == 0) { t0 /= q; e++; }
        int cur = nd; u64 v = 1;
        for (int k = 1; k <= e; k++) { v *= q; for (int j = 0; j < cur; j++) divs[nd++] = divs[j] * v; }
      }
      for (int i = 0; i < nd && !found; i++) {
        u64 A = divs[i];
        if ((A + 1) % u) continue;
        u64 t = (A + 1) / u, v = N / A;
        if (t < 3 || v < 3) continue;
        if (t * u * v - u - v != p) { fprintf(stderr, "BUG\n"); return 1; }
        if (inC(t, p) || inC(u, p) || inC(v, p)) { found = 1; ufound = u; }
      }
    }
    if (!found) { nzero++; printf("ZERO %llu\n", (unsigned long long)p); }
    else {
      int b = 0; while ((1ULL << (b + 1)) <= ufound) b++;
      hist[b]++;
      if (ufound > worst_u) { worst_u = ufound; worst_p = p; }
    }
  }
  printf("range [%llu,%llu]: primes p=1(4): %llu, zeros: %llu, max least-u = %llu at p = %llu\n",
         (unsigned long long)lo, (unsigned long long)hi, (unsigned long long)nprimes, (unsigned long long)nzero,
         (unsigned long long)worst_u, (unsigned long long)worst_p);
  for (int b = 0; b < 64; b++) if (hist[b]) printf("least u in [%llu,%llu): %llu\n", 1ULL << b, 1ULL << (b + 1), (unsigned long long)hist[b]);
  return 0;
}
