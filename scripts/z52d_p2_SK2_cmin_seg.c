/* Pass-2 SK2 (Z1790): segmented C-form census over primes p = 1 (mod 4) in (LO, HI].
   Output per prime: "p Cmin u B" (Cmin = least C <= CAP with d = 4Cu-1 | 4Cp+1, cofactor 4CB-1; 0 0 0 if none <= CAP).
   Usage: z52d_p2_SK2_cmin_seg LO HI CAP NPROC K     (processes primes with running index % NPROC == K)
   Memory: segment bytes (2^26) + base sieve up to sqrt(HI) + trial-division primes up to sqrt(4*CAP*HI). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static u64 *sp; static long nsp = 0;
static u64 divs_check(u64 N, u64 m) {
  u64 ps[64]; int es[64]; int k = 0; u64 M = N;
  for (long i = 0; i < nsp && (u64)sp[i] * sp[i] <= M; i++)
    if (M % sp[i] == 0) { int e = 0; while (M % sp[i] == 0) { M /= sp[i]; e++; } ps[k] = sp[i]; es[k] = e; k++; }
  if (M > 1) { ps[k] = M; es[k] = 1; k++; }
  int ex[64]; memset(ex, 0, sizeof(ex));
  while (1) {
    u64 r = 1 % m, dd = 1;
    for (int i = 0; i < k; i++) for (int e = 0; e < ex[i]; e++) { r = (r * (ps[i] % m)) % m; dd *= ps[i]; }
    if (r == m - 1) return dd;
    int i = 0; while (i < k) { ex[i]++; if (ex[i] <= es[i]) break; ex[i] = 0; i++; }
    if (i == k) break;
  }
  return 0;
}
int main(int argc, char **argv) {
  u64 LO = strtoull(argv[1], 0, 10), HI = strtoull(argv[2], 0, 10);
  u64 CAP = strtoull(argv[3], 0, 10); long NP = atol(argv[4]), K = atol(argv[5]);
  u64 SQH = (u64)sqrt((double)HI) + 2;
  u64 SQT = (u64)sqrt(4.0 * (double)CAP * (double)HI + 1.0) + 2;
  char *isc = calloc(SQT + 1, 1); sp = malloc(sizeof(u64) * (SQT / 2 + 10));
  for (u64 i = 2; i <= SQT; i++) if (!isc[i]) { sp[nsp++] = i; for (u64 j = i * i; j <= SQT; j += i) isc[j] = 1; }
  /* base primes for segmented sieve: sp[] up to SQH */
  const u64 SEG = 1ULL << 26;
  char *seg = malloc(SEG);
  long idx = 0;
  for (u64 lo = LO + 1; lo <= HI; lo += SEG) {
    u64 hi = lo + SEG - 1; if (hi > HI) hi = HI;
    u64 len = hi - lo + 1;
    memset(seg, 1, len);
    for (long i = 0; i < nsp && sp[i] <= SQH; i++) {
      u64 q = sp[i];
      u64 start = ((lo + q - 1) / q) * q; if (start < q * q) start = q * q;
      for (u64 j = start; j <= hi; j += q) seg[j - lo] = 0;
    }
    for (u64 x = lo; x <= hi; x++) {
      if (!seg[x - lo] || x < 5 || x % 4 != 1) continue;
      idx++; if (idx % NP != K) continue;
      u64 found = 0, fu = 0, fB = 0;
      for (u64 C = 1; C <= CAP && !found; C++) {
        u64 N = 4 * C * x + 1, m = 4 * C;
        u64 d = divs_check(N, m);
        if (d) { found = C; fu = (d + 1) / m; fB = (N / d + 1) / m; }
      }
      printf("%llu %llu %llu %llu\n", x, found, fu, fB);
    }
    fflush(stdout);
  }
  return 0;
}
