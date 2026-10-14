/* review_fs2_sum.c (R218, from scratch; written from the text of FF_STERILE_PUSH Lemma 1.6, not from fs_sum.c).
   Finite Case B part of (Σ): sum_{3<=s<=S} q^{1-ceil(s/2)} sum_{patterns a<=b} mult * min_route bound,
   q = 3^r, mult = 2 (a<b), 1 (a=b).
   Arithmetic: logs in long double (64-bit mantissa). Error budget: every log-bound is a sum of <= 6 terms, each with
   absolute error <= 1e-15 (log-factorials are cumulative sums of <= 2000 logl values, error <= 2000*2^-64*1e4 < 1e-12),
   so each exponentiated term has relative error < 1e-11; the sum of <= 1e8 positive terms adds < 1e-10 relative.
   We output total*(1+1e-8) as the certified upper bound.
   Class counts are exact integers (minimal m+k over m+k <= KMAX, Lemma 1.5; 2 by Lemma 1.4; 1 trivial).
   usage: review_fs2_sum r S [print_every]  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long double LD;
static int q_r; static LD LQ; static LD lfac[4096];
#define KMAX 200
/* exact Coppersmith search: least K=m+k<=KMAX, m>=1, with n*A + X*(A + k*m + k(k+1)/2) < (m+k+1)*m*d */
static int cop(long n, long d, long rho) {
  long X = d - rho; if (X < 0) return 1;
  for (long K = 1; K <= KMAX; K++) for (long m = 1; m <= K; m++) {
    long k = K - m, A = m * (m + 1) / 2;
    long lhs = n * A + X * (A + k * m + k * (k + 1) / 2), rhs = (m + k + 1) * m * d;
    if (lhs < rhs) return (int)K;
  }
  return 0;
}
/* memo for cop over (n,d,rho) with n<=NMAX */
#define NMAX 700
static short *memo;  /* index n*(NMAX+1)*... too big; use (n, d, X) with X<=d<=n: map via hash */
#define HB 25
static unsigned long long *hk; static int *hv;
static int copm(long n, long d, long rho) {
  if (d < rho) return 1;
  unsigned long long key = ((unsigned long long)n << 42) | ((unsigned long long)d << 21) | (unsigned long long)rho | (1ULL << 63);
  unsigned long long h = (key * 11400714819323198485ULL) >> (64 - HB);
  for (;;) { if (hk[h] == key) return hv[h]; if (!hk[h]) break; h = (h + 1) & ((1ULL << HB) - 1); }
  int c = cop(n, d, rho); hk[h] = key; hv[h] = c; return c;
}
static LD lbin(long n, long d) { return lfac[n] - lfac[d] - lfac[n - d]; }
/* log of class-divisor bound: min(C(n,d), 1 trivial, 2 Lenstra, m+k Coppersmith, cofactor versions if both) */
static LD lcls(long n, long d, long rho, int both) {
  LD best = lbin(n, d);
  if (d < rho || (both && n - d < rho)) return best < 0 ? best : 0.0L;
  long c = 0;
  if (3 * rho > n) c = 2;
  long c1 = copm(n, d, rho); if (c1 && (!c || c1 < c)) c = c1;
  if (both) { long c2 = copm(n, n - d, rho); if (c2 && (!c || c2 < c)) c = c2; }
  if (c && logl((LD)c) < best) best = logl((LD)c);
  return best;
}
static LD lN(long d) { return d <= 0 ? 0.0L : d * LQ + log1pl(-expl(-LQ)); }
static LD lSom(long e) { /* 2 q^e + (e-1)(q^e - q^{e-1}) */
  if (e <= 0) return 0.0L; return e * LQ + logl(2.0L + (e - 1) * (1.0L - expl(-LQ))); }
static const char *RN[19] = {"T0","R4'","X1","X2","R1","R2","R3","R4","R3C","R4C","R5a","R5b","R6a","R6b","R8a","R8b","R9a","R10a","R10b"};
static LD minroute(long s, long a, long z, long y, long t, int *arg) {
  long b = y + t; LD W = lN(a - 1), WB = lN(b - 1), Z = lN(z), Y = lN(y), V = lN(t - 2), l2 = logl(2.0L);
  LD e[19];
  e[0] = Z + Y + W; e[1] = Z + W + V; e[2] = l2 + Y + V + Z; e[3] = Y + V + W;
  e[4] = V + lfac[s - 2] - lfac[z] - lfac[a - 1] - lfac[b - 1];
  e[5] = Z + Y + lcls(s + 2 * y + z, a + y + z, y + z + 1, 1);
  e[6] = W + Y + lcls(s - 1 + y, a + y + z, a + y, 0);
  e[7] = Z + W + lcls(s - 2, a + y + z, a + z, 1);
  e[8] = WB + Y + lcls(s - 1 + y, b + y + z, b + y, 0);
  e[9] = Z + WB + lcls(z + 2 * b - 2, b + y + z, b + z, 1);
  LD c5a = lcls(s - 1 - a, b - 1, t - 1, 1), c5b = lcls(s - 1 - b, a - 1, t - 1, 1), c10 = lcls(a + b - 2, a - 1, t - 1, 1);
  e[10] = V + W + c5a; e[11] = V + WB + c5b;
  e[12] = V + lbin(s - 2, a - 1) + c5a; e[13] = V + lbin(s - 2, b - 1) + c5b;
  e[14] = Y + V + lbin(s - 2, a - 1); e[15] = Y + V + lbin(s - 2, b - 1);
  e[16] = Z + V + lbin(a + b - 2, a - 1);
  e[17] = Z + l2 + lSom(t - 2) + c10;
  e[18] = l2 + lSom(t - 2) + lbin(s - 2, z) + c10;
  int am = 0; for (int i = 1; i < 19; i++) if (e[i] < e[am]) am = i;
  if (arg) *arg = am; return e[am];
}
int main(int argc, char **argv) {
  q_r = atoi(argv[1]); long S = atol(argv[2]); long every = argc > 3 ? atol(argv[3]) : 10;
  LQ = q_r * logl(3.0L);
  lfac[0] = 0; for (int i = 1; i < 4096; i++) lfac[i] = lfac[i - 1] + logl((LD)i);
  hk = calloc(1ULL << HB, sizeof *hk); hv = calloc(1ULL << HB, sizeof *hv);
  LD tot = 0; long rc[19] = {0};
  for (long s = 3; s <= S; s++) {
    LD acc = 0, comp = 0;
    for (long a = 1; a < s; a++) for (long z = 0; a + z < s; z++) {
      long b = s - a - z; if (b < a) continue;
      for (long y = 0; y + 2 <= b; y++) {
        int am; LD e = minroute(s, a, z, y, b - y, &am); rc[am]++;
        LD term = (a < b ? 2.0L : 1.0L) * expl(e - ((s + 1) / 2 - 1) * LQ);
        LD yk = term - comp, tk = acc + yk; comp = (tk - acc) - yk; acc = tk;   /* Kahan */
      }
    }
    tot += acc;
    if (s <= 12 || s % every == 0 || s == S) printf("s=%ld term=%.12Le cum=%.12Le\n", s, acc, tot);
  }
  printf("r=%d S=%ld finite_total=%.15Le certified_upper(x(1+1e-8))=%.15Le\nargmin:", q_r, S, tot, tot * (1 + 1e-8L));
  for (int i = 0; i < 19; i++) printf(" %s:%ld", RN[i], rc[i]); printf("\n");
  return 0;
}
