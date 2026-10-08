/* R93: K = 13 variant of review_m17b_k11.c (same argument; A0, X configurable; sieve stores only e with 4 | n+e).
 * Usage: review_m17b_k13 MODE K A0 X  (MODE = A0 | A1 | B).
 * Original header:
 * R93 from-scratch complete enumeration of P-data at K = 11 (n = 17^11), independent of m17b_penum.
 * N-points of Sigma^II_n: 4abd = n+e, ce = a+b, a<=b, all >=1; output those with 17∤cd.
 * Part A (a >= A0): naive scan over (a,d): b in [max(a,ceil((n+1)/(4ad))), floor((n+a)/(4ad-1))],
 *   e = 4abd-n in [1,a+b], check e | a+b.  d <= (n+2a)/(4a^2) (from b>=a).
 * Part B (a < A0): for fixed a, acde <= n (reviewer's derivation) gives e <= X or cd <= n/(aX).
 *   B1: e <= X: segmented-sieve factorisation of M=(n+e)/4 = abd, divisors d of M/a.
 *   B2: cd <= n/(aX): f = 4acd-1 must divide nc+a (bf = nc+a), b = (nc+a)/f.
 * Usage: review_m17b_k11 MODE [K] ; MODE = A0 (part A, parity 0) | A1 | B. Prints "a b c d".
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 A0 = 50;
static u64 n;
static void out(u64 a, u64 b, u64 c, u64 d) {
  if (b < a || c % 17 == 0 || d % 17 == 0) return;
  u128 l = (u128)4 * a * b * c * d, r = (u128)a + b + (u128)n * c;
  if (l != r) { fprintf(stderr, "BUG %llu %llu %llu %llu\n", a, b, c, d); exit(3); }
  printf("%llu %llu %llu %llu\n", a, b, c, d);
}
int main(int argc, char **argv) {
  int K = argc > 2 ? atoi(argv[2]) : 11; if (argc > 3) A0 = atoll(argv[3]); n = 1; for (int i = 0; i < K; i++) n *= 17;
  char *mode = argv[1];
  if (mode[0] == 'A') {
    int par = mode[1] - '0';
    for (u64 a = A0 + par; 4 * a * a <= n + 2 * a; a += 2) {
      u64 dmax = (n + 2 * a) / (4 * a * a);
      for (u64 d = 1; d <= dmax; d++) {
        u64 m = 4 * a * d;
        u64 blo = (n + 1 + m - 1) / m; if (blo < a) blo = a;
        u64 bhi = (n + a) / (m - 1);
        for (u64 b = blo; b <= bhi; b++) {
          u64 e = m * b - n;               /* >= 1 since b >= ceil((n+1)/m) */
          if ((a + b) % e == 0) out(a, b, (a + b) / e, d);
        }
      }
    }
  } else {
    u64 X = argc > 4 ? atoll(argv[4]) : 10000000ULL;
    /* B2 */
    for (u64 a = 1; a < A0; a++) {
      u64 Y = n / (a * X);
      for (u64 c = 1; c <= Y; c++) for (u64 d = 1; c * d <= Y; d++) {
        u128 f = (u128)4 * a * c * d - 1, num = (u128)n * c + a;
        if (num % f == 0) out(a, (u64)(num / f), c, d);
      }
    }
    /* B1: sieve n+e, e=1..X */
    u64 lim = 1; while ((lim + 1) * (lim + 1) <= n + X) lim++;
    char *comp = calloc(lim + 1, 1);
    u64 e0 = (4 - n % 4) % 4; if (e0 == 0) e0 = 4; u64 NI = (X - e0) / 4 + 1;
#define IX(e) (((e) - e0) / 4)
    u64 *res = malloc(NI * sizeof(u64));
    uint32_t (*fp)[24] = calloc(NI, sizeof *fp); unsigned char *nf = calloc(NI, 1);
    unsigned char (*fe)[24] = calloc(NI, sizeof *fe);
    if (!res || !fp || !nf || !fe) { fprintf(stderr, "OOM\n"); exit(5); }
    for (u64 e = e0; e <= X; e += 4) res[IX(e)] = n + e;
    for (u64 p = 2; p <= lim; p++) {
      if (comp[p]) continue;
      for (u64 q = p * p; q <= lim; q += p) comp[q] = 1;
      u64 first = (p - (n + 1) % p) % p + 1;   /* smallest e>=1 with p | n+e */
      for (u64 e = first; e <= X; e += p) {
        if ((n + e) % 4) continue;
        u64 i = IX(e);
        int k = 0; while (res[i] % p == 0) { res[i] /= p; k++; }
        fp[i][nf[i]] = (uint32_t)p; fe[i][nf[i]] = k; nf[i]++;
      }
    }
    for (u64 e = 1; e <= X; e++) {
      if ((n + e) % 4) continue;
      u64 M = (n + e) / 4;
      /* factorisation of M: primes of n+e with 2-exponent reduced by 2, plus residual prime */
      u64 P[26]; int E[26], np = 0;
      u64 ii = IX(e);
      for (int i = 0; i < nf[ii]; i++) { P[np] = fp[ii][i]; E[np] = fe[ii][i] - (fp[ii][i] == 2 ? 2 : 0); if (E[np] > 0) np++; }
      if (res[ii] > 1) { P[np] = res[ii]; E[np] = 1; np++; }
      /* divisors a < A0 of M, generated from the factorisation (pruned) */
      static u64 Ad[400000]; int na = 1; Ad[0] = 1;
      for (int i = 0; i < np; i++) {
        int cur = na; u64 pk = 1;
        for (int k = 1; k <= E[i]; k++) { pk *= P[i]; if (pk >= A0) break;
          for (int j = 0; j < cur; j++) if (Ad[j] * pk < A0) Ad[na++] = Ad[j] * pk; }
      }
      for (int ia = 0; ia < na; ia++) {
        u64 a = Ad[ia];
        if (M % a) { fprintf(stderr, "ADIV BUG\n"); exit(6); }
        u64 R = M / a;
        /* enumerate divisors d of R */
        u64 divs[200000]; int nd = 1; divs[0] = 1;
        for (int i = 0; i < np; i++) {
          if (R % P[i]) continue;
          int cur = nd; u64 pk = 1;
          for (int k = 1; ; k++) { if ((R / pk) % P[i]) break; pk *= P[i];
            for (int j = 0; j < cur; j++) divs[nd++] = divs[j] * pk; }
        }
        { u64 pr = 1; for (int j = 0; j < nd; j++) if (divs[j] > pr) pr = divs[j];
          if (pr != R) { fprintf(stderr, "FACTBUG e=%llu a=%llu\n", e, a); exit(4); } }
        for (int j = 0; j < nd; j++) {
          u64 d = divs[j], b = R / d;
          if (b >= a && (a + b) % e == 0) out(a, b, (a + b) / e, d);
        }
      }
    }
  }
  fprintf(stderr, "mode %s done\n", mode);
  return 0;
}
