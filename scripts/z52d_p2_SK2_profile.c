/* Pass-2 SK2: exact per-prime (star)-count profile, all C (no cap).
   For prime p = 1 (mod 4): R_C(p) = #{(u,B) >= 1 : 4CuB - u - B = p} = #{d | 4Cp+1 : d = -1 mod 4C}
   (ordered pairs; see z52d_p2_SK2_starcmin.c for the enumeration proof: all solutions have min(u,B) <= sqrt p + 2).
   Enumeration: for u <= U=floor(sqrt p)+2: divisors D of n=p+u with D = -1 mod 4u give C=(D+1)/(4u), B=n/D.
   Ordered count: each solution with u<=U counted once; solutions with u>U have B<=U and are the swaps of
   solutions with B>U found in the same loop.  So R = #{found, u<=U} + #{found, B>U}.
   Output per prime: p R Cmin R_le2 R_le20 R_le500 Z(1.01) Z(1.1) Z(1.5) Z(2)   [Z(s)=sum_C R_C(p) C^-s]
   Argv: PMAX NPROC K  (primes with index%NPROC==K).  Pairs file (optional, argv[4]=PSTAT):
   for p <= PSTAT and winning C <= 500 writes "p C phi(4C) omega(4Cp+1) ratio" to stdout after the summary? -> separate file via argv[5].
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
typedef unsigned long long u64;
static u64 *sp; static long nsp;
static int fact(u64 m, u64 *ps, int *es) {
  int k = 0;
  for (long i = 0; i < nsp && (u64)sp[i] * sp[i] <= m; i++)
    if (m % sp[i] == 0) { int e = 0; while (m % sp[i] == 0) { m /= sp[i]; e++; } ps[k] = sp[i]; es[k] = e; k++; }
  if (m > 1) { ps[k] = m; es[k] = 1; k++; }
  return k;
}
int main(int argc, char **argv) {
  long PMAX = atol(argv[1]), NP = atol(argv[2]), K = atol(argv[3]);
  long PSTAT = argc > 4 ? atol(argv[4]) : 0;
  FILE *pf = argc > 5 ? fopen(argv[5], "w") : NULL;
  long SQ = 1 + (long)sqrt((double)PMAX + 2e6) + 10;
  char *isc = calloc(SQ + 1, 1); sp = malloc(sizeof(u64) * (SQ / 2 + 10));
  for (long i = 2; i <= SQ; i++) if (!isc[i]) { sp[nsp++] = i; for (long j = i * i; j <= SQ; j += i) isc[j] = 1; }
  char *cs = calloc(PMAX + 1, 1);
  for (long i = 2; i <= PMAX; i++) if (!cs[i]) for (long j = i * i; j <= PMAX; j += i) cs[j] = 1;
  long idx = 0;
  static double RC[1000]; /* R_C for C < 1000 is needed for stats up to 500 */
  for (long p = 5; p <= PMAX; p++) {
    if (cs[p] || p % 4 != 1) continue;
    idx++; if (idx % NP != K) continue;
    memset(RC, 0, sizeof(RC));
    double Z[4] = {0, 0, 0, 0}; double ss[4] = {1.01, 1.1, 1.5, 2.0};
    u64 R = 0, Cmin = 0; u64 Rle2 = 0, Rle20 = 0, Rle500 = 0; u64 Rm[4] = {0,0,0,0}; /* ordered pairs with min(u,B)<=1,2,5,20 */
    u64 U = (u64)sqrt((double)p) + 2;
    for (u64 u = 1; u <= U; u++) {
      u64 n = p + u; u64 ps[64]; int es[64];
      int k = fact(n, ps, es);
      u64 mod = 4 * u; int ex[64]; memset(ex, 0, sizeof(ex));
      while (1) {
        u64 D = 1;
        for (int i = 0; i < k; i++) for (int e = 0; e < ex[i]; e++) D *= ps[i];
        if ((D + 1) % mod == 0) {
          u64 C = (D + 1) / mod; u64 B = n / D;
          int cnt = 0;
          if (u <= U) cnt++;               /* counted as (u,B) with u<=U */
          if (B > U) cnt++;                /* swap (B,u): second coordinate u > ... counted once more */
          /* ordered solution (u,B): counted once here; plus its swap (B,u) if B>U is a solution with first coord B>U
             which we must count explicitly: total contributes 1 + [B>U] */
          R += 1 + (B > U ? 1 : 0);
          { u64 mn = u < B ? u : B; int kk2[4] = {1,2,5,20}; for (int j = 0; j < 4; j++) if (mn <= (u64)kk2[j]) Rm[j] += 1 + (B > U ? 1 : 0); }
          RC[C < 1000 ? C : 999] += 1 + (B > U ? 1 : 0);
          if (Cmin == 0 || C < Cmin) Cmin = C;
          (void)cnt;
        }
        int i = 0; while (i < k) { ex[i]++; if (ex[i] <= es[i]) break; ex[i] = 0; i++; }
        if (i == k) break;
      }
    }
    for (int C = 1; C < 1000; C++) {
      if (RC[C] == 0) continue;
      if (C <= 2) Rle2 += (u64)RC[C];
      if (C <= 20) Rle20 += (u64)RC[C];
      if (C <= 500) Rle500 += (u64)RC[C];
      for (int j = 0; j < 4; j++) Z[j] += RC[C] * pow((double)C, -ss[j]);
    }
    printf("%ld %llu %llu %llu %llu %llu %.9g %.9g %.9g %.9g %llu %llu %llu %llu\n", p, R, Cmin, Rle2, Rle20, Rle500, Z[0], Z[1], Z[2], Z[3], Rm[0], Rm[1], Rm[2], Rm[3]);
    if (pf && p <= PSTAT) {
      for (int C = 1; C <= 500; C++) {
        if (RC[C] == 0) continue;
        /* phi(4C), omega(4Cp+1) */
        u64 m = 4ULL * C; u64 phi = 1; u64 t = m; u64 ps2[64]; int es2[64];
        int kk = fact(m, ps2, es2);
        for (int i = 0; i < kk; i++) { phi *= (ps2[i] - 1); for (int e = 1; e < es2[i]; e++) phi *= ps2[i]; }
        u64 N = 4ULL * C * (u64)p + 1; u64 ps3[64]; int es3[64];
        int k3 = fact(N, ps3, es3);
        (void)t;
        fprintf(pf, "%ld %d %llu %d %.6f %.0f\n", p, C, phi, k3, (double)phi / pow(2.0, k3), RC[C]);
      }
    }
    fflush(stdout);
  }
  if (pf) fclose(pf);
  return 0;
}
