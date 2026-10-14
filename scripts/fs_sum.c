/* fs_sum.c (O216): union-bound mass of Case B tuples on a c-slice of ES_q(T^k), q = 3^r, k = 2,
   pattern by pattern, with the route bounds of FF_STERILE_PUSH.md §2 (Lemmas 1.1-1.6).
   Pattern (s; a, z, y, t), b = y + t >= a >= 1, t >= 2, s = a + z + y + t (Lemma 1.1); a < b patterns are doubled
   (w <-> C symmetry), a = b counted once. Relative mass per tuple q^{1 - ceil(s/2)}.
   usage: fs_sum r SMAX [cop=1] [verbose s-list every]
   Output: per-s term and cumulative sum (long double; see §3 for the rounding margin). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long double LD;
static LD lq; static int COP = 1;
#define NF 40000
static LD lfact[NF];
static LD lC(int n, int k) { if (k < 0 || k > n || n < 0) return 1e30L; return lfact[n] - lfact[k] - lfact[n - k]; }
static LD Ns(int d) { return d <= 0 ? 0.0L : d * lq + log1pl(-expl(-lq)); }       /* log N*(d) */
/* log of sum_{v1 monic deg e} 2^{omega(v1)} = q^e (2 + (e-1)(1-1/q)) for e >= 1, 1 for e = 0 */
static LD Somega(int e) { if (e <= 0) return 0.0L; return e * lq + logl(2.0L + (e - 1) * (1.0L - expl(-lq))); }

/* Coppersmith count (Lemma 1.5) for divisor degree D, poly degree n, modulus degree rho; 0 if none found */
static int cop1(long n, long D, long rho) {
  if (D < rho) return 1;
  long X = D - rho; int best = 0;
  if (!COP) return 0;
  for (long m = 1; m <= 60; m++) {
    /* smallest k >= 0 with Delta(m,k) < (m+k+1) m D ; Delta - RHS is convex quadratic in k */
    for (long k = 0; k <= 200; k++) {
      long det = n * m * (m + 1) / 2 + X * (m * (m + 1) / 2 + k * m + k * (k + 1) / 2);
      long rhs = (m + k + 1) * m * D;
      if (det < rhs) { if (!best || m + k < best) best = (int)(m + k); break; }
      /* if the quadratic is increasing in k already and still failing, stop */
      if (X * (m + k + 1) >= m * D) break;   /* increments det: X(m+k+1), rhs: mD */
    }
  }
  return best;
}
/* class-divisor count bound, log; both = cofactor version allowed (F prime to Q) */
#define HS (1 << 24)
static unsigned long long hkey[HS]; static int hval[HS];
static int clscount(int n, int d, int rho, int both) {
  unsigned long long key = ((unsigned long long)n << 40) | ((unsigned long long)d << 20) | ((unsigned long long)rho << 1) | both | (1ULL << 63);
  unsigned long long h = ((key * 0x9E3779B97F4A7C15ULL) >> 37) & (HS - 1);
  while (hkey[h] && hkey[h] != key) h = (h + 1) & (HS - 1);
  if (hkey[h] == key) return hval[h];
  int best = 0;
  if (d < rho) best = 1;
  else if (both && n - d < rho) best = 1;
  else {
    if (3 * rho > n) best = 2;                          /* Lemma 1.4 */
    int c = cop1(n, d, rho); if (c && (!best || c < best)) best = c;
    if (both) { c = cop1(n, n - d, rho); if (c && (!best || c < best)) best = c; }
  }
  hkey[h] = key; hval[h] = best; return best;
}
static LD divc(int n, int d, int rho, int both) {
  LD b = lC(n, d); int c = clscount(n, d, rho, both);
  if (c && logl((LD)c) < b) b = logl((LD)c);
  return b;
}
#define MIN(x, y) ((x) < (y) ? (x) : (y))
/* log of the count bound for one pattern; also reports the argmin route */
static const char *rname[] = {"T0","R4'","X1","X2","R1","R2","R3","R4","R3C","R4C","R5a","R5b","R6a","R6b","R8a","R8b","R9a","R10a","R10b"};
LD pattern_bound(int s, int a, int z, int y, int t, int *arg) {
  int b = y + t;
  LD W = Ns(a - 1), WB = Ns(b - 1), Z = Ns(z), Y = Ns(y), V = Ns(t - 2), L2 = logl(2.0L);
  LD e[19];
  e[0] = Z + Y + W;                                   /* (m',g',w) */
  e[1] = Z + W + V;                                   /* (m',w,v) */
  e[2] = L2 + Y + V + Z;                              /* (m',g',v), 2 roots */
  e[3] = Y + V + W;                                   /* (g',v,w) */
  e[4] = V + lfact[s - 2] - lfact[z] - lfact[a - 1] - lfact[b - 1];   /* v, then m'w1C1 = T^{s-2}+v1 */
  e[5] = Z + Y + divc(s + 2 * y + z, a + y + z, y + z + 1, 1);        /* (m',g'): E | 1+T^s m'g'^2, mod TL' */
  e[6] = W + Y + divc(s - 1 + y, a + y + z, a + y, 0);                /* (w1,g'): E | g'T^{s-1}+w1, mod Tw1g' */
  e[7] = Z + W + divc(s - 2, a + y + z, z + a, 1);                    /* (m',w1): E | T^{s-2}+m'w1^2, mod Tm'w1 */
  e[8] = WB + Y + divc(s - 1 + y, b + y + z, b + y, 0);               /* (C1,g') */
  e[9] = Z + WB + divc(z + 2 * b - 2, b + y + z, z + b, 1);           /* (m',C1) */
  e[10] = V + W + divc(s - 1 - a, b - 1, t - 1, 1);                   /* (v1,w1): C1 | (T^{s-2}+v1)/w1, mod Tv1 */
  e[11] = V + WB + divc(s - 1 - b, a - 1, t - 1, 1);                  /* (v1,C1) */
  e[12] = V + lC(s - 2, a - 1) + divc(s - 1 - a, b - 1, t - 1, 1);    /* v1, w1 | T^{s-2}+v1, then C1 */
  e[13] = V + lC(s - 2, b - 1) + divc(s - 1 - b, a - 1, t - 1, 1);
  e[14] = Y + V + lC(s - 2, a - 1);                                   /* (g',v1), w1 | T^{s-2}+v1 */
  e[15] = Y + V + lC(s - 2, b - 1);
  e[16] = Z + V + lC(a + b - 2, a - 1);                               /* (m',v1), w1 | (T^{s-2}+v1)/m' */
  e[17] = Z + L2 + Somega(t - 2) + divc(a + b - 2, a - 1, t - 1, 1);  /* (m',v1), w1 in sqrt classes mod Tv1 */
  e[18] = L2 + Somega(t - 2) + lC(s - 2, z) + divc(a + b - 2, a - 1, t - 1, 1);  /* v1, m' | T^{s-2}+v1, classes */
  int am = 0; for (int i = 1; i < 19; i++) if (e[i] < e[am]) am = i;
  if (arg) *arg = am;
  return e[am];
}
#ifndef NO_MAIN
int main(int argc, char **argv) {
  int r = atoi(argv[1]), S = atoi(argv[2]); if (argc > 3) COP = atoi(argv[3]);
  int every = argc > 4 ? atoi(argv[4]) : 10;
  lq = r * logl(3.0L);
  lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  LD tot = 0; long cnt[19] = {0};
  for (int s = 3; s <= S; s++) {
    LD acc = 0, mx = -1e30L; int mxp[4] = {0};
    for (int a = 1; a < s; a++) for (int z = 0; a + z < s; z++) {
      int b = s - a - z; if (b < a) continue;
      for (int y = 0; y <= b - 2; y++) {
        int t = b - y, am;
        LD e = pattern_bound(s, a, z, y, t, &am);
        cnt[am]++;
        if (e > mx) { mx = e; mxp[0] = a; mxp[1] = z; mxp[2] = y; mxp[3] = t; }
        acc += (a == b ? 1 : 2) * expl(e + (1 - (s + 1) / 2) * lq);
      }
    }
    tot += acc;
    if (s <= 12 || s % every == 0) { printf("s=%d term=%.10Le cum=%.10Le  maxpattern(a,z,y,t)=(%d,%d,%d,%d)\n", s, acc, tot, mxp[0], mxp[1], mxp[2], mxp[3]); fflush(stdout); }
  }
  printf("r=%d cop=%d total(3<=s<=%d)=%.6Le\nroute argmin counts:", r, COP, S, tot);
  for (int i = 0; i < 19; i++) printf(" %s:%ld", rname[i], cnt[i]);
  printf("\n");
  return 0;
}
#endif
