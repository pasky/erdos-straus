/* fz_sum.c (O220): fs_sum.c (O216) + division/class routes of FF_STERILE_SMALL Lemmas 1.2-1.4.
   Original header: fs_sum.c (O216): union-bound mass of Case B tuples on a c-slice of ES_q(T^k), q = 3^r, k = 2,
   pattern by pattern, with the route bounds of FF_STERILE_PUSH.md §2 (Lemmas 1.1-1.6).
   Pattern (s; a, z, y, t), b = y + t >= a >= 1, t >= 2, s = a + z + y + t (Lemma 1.1); a < b patterns are doubled
   (w <-> C symmetry), a = b counted once. Relative mass per tuple q^{1 - ceil(s/2)}.
   usage: fz_sum r SMAX [cop=1] [every] [new=1] [rankin=1]
   Output: per-s term and cumulative sum (long double; see §3 for the rounding margin). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long double LD;
static LD lq; static int COP = 1, NEWR = 1;
#define NF 40000
static LD lfact[NF];
static LD lC(int n, int k) { if (k < 0 || k > n || n < 0) return 1e30L; return lfact[n] - lfact[k] - lfact[n - k]; }
static LD lD(int n, int d);
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
static int REF = 1;
/* FF_STERILE_SMALL Lemma 1.4: min over j >= 0 of q^j * cls(n, d, rho + j); also min with C(n, d) (Lemma 1.3) */
static LD divc(int n, int d, int rho, int both) {
  LD b = lD(n, d); int jmax = REF ? (d - rho + 1 > 0 ? d - rho + 1 : 0) : 0;
  for (int j = 0; j <= jmax; j++) {
    if (j * lq >= b) break;
    int c = clscount(n, d, rho + j, both);
    if (c && j * lq + logl((LD)c) < b) b = j * lq + logl((LD)c);
  }
  return b;
}
/* FF_STERILE_SMALL Lemma 1.3: log of the number of v1 (deg e = t-2, fixed lc) in a fixed class mod D, deg D = d */
static LD logV(int e, int d) { return d <= e ? (e - d) * lq : 0.0L; }
/* FF_STERILE_SMALL Lemma 4.1 (fixed-q divisor bound): for F of exact degree n, T not dividing F, the number of monic
   divisors of degree d is <= rho^{-d'} exp(V_rho(n)), d' = min(d, n-d), 0 < rho <= 1, where V_rho(n) is the fractional-
   knapsack maximum of sum of gains log(S_e(rho^j)/S_{e-1}(rho^j)) (S_e(y) = 1 + y + ... + y^e) over items
   (irreducible P of degree j, e-th power), at most Ip(j) irreducibles of degree j (Ip(1) = q - 1), capacity n. */
#define NRHO 64
#define NMAXRK 2048
static int RANK = 1;
static double Vr[NRHO][NMAXRK + 1]; static double lrho[NRHO];
static LD rkcache[NMAXRK + 1][NMAXRK / 2 + 2]; static char rkdone[NMAXRK + 1][NMAXRK / 2 + 2];
typedef struct { double ratio, gain; int j; double cnt; } RKI;
static int rkcmp(const void *x, const void *y) { double a = ((RKI *)x)->ratio, b = ((RKI *)y)->ratio; return a < b ? 1 : a > b ? -1 : 0; }
static void init_rankin(long double q) {   /* O220: q as long double (was int; overflowed for q > 2^31) */
  static double Ip[NMAXRK + 1];
  for (int j = 1; j <= NMAXRK; j++) {
    long double sum = 0;
    for (int i = 1; i <= j; i++) if (j % i == 0) {
      int m = i, mu = 1, p; for (p = 2; p * p <= m; p++) if (m % p == 0) { m /= p; if (m % p == 0) { mu = 0; break; } mu = -mu; }
      if (mu && m > 1) mu = -mu;
      long double term = (j / i) * logl((LD)q) > 11000 ? 1e4000L : powl((LD)q, (LD)(j / i)); sum += mu * term;
    }
    Ip[j] = (double)fminl(sum / j, 1e300L); if (j == 1) Ip[j] -= 1;
  }
  RKI *it = malloc(sizeof(RKI) * 400000);
  for (int k = 0; k < NRHO; k++) {
    double rho = (k + 1.0) / NRHO; lrho[k] = log(rho);
    int ni = 0;
    for (int j = 1; j <= NMAXRK; j++) {
      double y = pow(rho, j); if (y < 1e-300) break;
      double Sprev = 1, Se = 1;
      for (int e = 1; e * j <= NMAXRK; e++) {
        Se = Sprev + pow(y, e); double g = log(Se / Sprev); Sprev = Se;
        if (g < 1e-18) break;
        it[ni].gain = g; it[ni].ratio = g / j; it[ni].j = j; it[ni].cnt = Ip[j]; ni++;
        if (ni >= 400000) { fprintf(stderr, "rankin overflow\n"); exit(2); }
      }
    }
    qsort(it, ni, sizeof(RKI), rkcmp);
    /* V(n) = fractional fill of capacity n: piecewise linear; evaluate at integers */
    int idx = 0; double val = 0, leftcnt = ni ? it[0].cnt : 0;
    Vr[k][0] = 0;
    for (int n = 1; n <= NMAXRK; n++) {
      double need = 1.0;             /* fill one more unit of degree */
      while (need > 1e-15 && idx < ni) {
        double cap = leftcnt * it[idx].j;       /* degree available in this class */
        double take = cap < need ? cap : need;
        val += take * it[idx].ratio; need -= take; leftcnt -= take / it[idx].j;
        if (leftcnt <= 1e-12) { idx++; if (idx < ni) leftcnt = it[idx].cnt; }
      }
      Vr[k][n] = val * (1 + 1e-12) + 1e-12;    /* outward rounding */
    }
  }
  free(it);
}
static LD lRk(int n, int d) {
  if (!RANK || n > NMAXRK || n < 0 || d < 0 || d > n) return 1e30L;
  int dp = d < n - d ? d : n - d;
  if (rkdone[n][dp]) return rkcache[n][dp];
  double best = 1e300;
  for (int k = 0; k < NRHO; k++) { double v = -dp * lrho[k] + Vr[k][n]; if (v < best) best = v; }
  rkdone[n][dp] = 1; rkcache[n][dp] = best; return best;
}
static LD lD(int n, int d) { LD a = lC(n, d), b = lRk(n, d); return a < b ? a : b; }
/* omega*(e): max number of distinct monic irreducibles != T with total degree <= e (greedy by degree) */
static int omstar[NF];
static void init_omstar(long double q) {   /* O220: q as long double */
  /* number of monic irreducibles of degree j: (1/j) sum_{i | j} mu(i) q^{j/i}; computed in long double, capped */
  LD cntj[64]; int J = 63;
  for (int j = 1; j <= J; j++) {
    LD sum = 0; for (int i = 1; i <= j; i++) if (j % i == 0) {
      int m = i, mu = 1, p; for (p = 2; p * p <= m; p++) if (m % p == 0) { m /= p; if (m % p == 0) { mu = 0; break; } mu = -mu; }
      if (mu && m > 1) mu = -mu;
      sum += mu * powl((LD)q, (LD)(j / i));
    }
    cntj[j] = sum / j; if (j == 1) cntj[j] -= 1;      /* exclude T */
  }
  for (int e = 0; e < NF; e++) {
    int left = e, om = 0;
    for (int j = 1; j <= J && left >= j; j++) {
      LD take = floorl((LD)left / j); if (take > cntj[j]) take = cntj[j];
      om += (int)take; left -= (int)take * j;
    }
    omstar[e] = om;     /* greedy is optimal: smaller degrees first maximise the count (exchange argument) */
  }
}
/* log bound for sum over v1 (deg e, fixed lc, in a fixed unit class mod D, deg D = d) of 2^{omega(v1)} */
static LD logSomClass(int e, int d) {
  LD a = logV(e, d) + omstar[e > 0 ? e : 0] * logl(2.0L);
  if (d <= e) {      /* tau-bound: 2 sum_{j <= e/2} q^j max(1, q^{e-d-j}) */
    LD s = 0; for (int j = 0; j <= e / 2; j++) s += expl(j * lq + (e - d - j > 0 ? (e - d - j) * lq : 0.0L) - (e - d) * lq);
    LD b = logl(2.0L * s) + (e - d) * lq; if (b < a) a = b;
  }
  return a;
}
#define MIN(x, y) ((x) < (y) ? (x) : (y))
/* log of the count bound for one pattern; also reports the argmin route */
static const char *rname[] = {"T0","R4'","X1","X2","R1","R2","R3","R4","R3C","R4C","R5a","R5b","R6a","R6b","R8a","R8b","R9a","R10a","R10b","R9a3","R10a3","R5a3","R5b3","X1_3","X2_3","R4p3"};
#define NR 26
LD pattern_bound(int s, int a, int z, int y, int t, int *arg) {
  int b = y + t;
  LD W = Ns(a - 1), WB = Ns(b - 1), Z = Ns(z), Y = Ns(y), V = Ns(t - 2), L2 = logl(2.0L);
  LD e[NR];
  e[0] = Z + Y + W;                                   /* (m',g',w) */
  e[1] = Z + W + V;                                   /* (m',w,v) */
  e[2] = L2 + Y + V + Z;                              /* (m',g',v), 2 roots */
  e[3] = Y + V + W;                                   /* (g',v,w) */
  e[4] = V + lfact[s - 2] - lfact[z] - lfact[a - 1] - lfact[b - 1];   /* v, then m'w1C1 = T^{s-2}+v1 */
  { LD r1 = V + lD(s - 2, z) + lD(s - 2 - z, a - 1), r2 = V + lD(s - 2, a - 1) + lD(s - 1 - a, z),
       r3 = V + lD(s - 2, b - 1) + lD(s - 1 - b, z);   /* Lemma 4.1: m' | F then w1 | F/m', etc. */
    if (r1 < e[4]) e[4] = r1; if (r2 < e[4]) e[4] = r2; if (r3 < e[4]) e[4] = r3; }
  e[5] = Z + Y + divc(s + 2 * y + z, a + y + z, y + z + 1, 1);        /* (m',g'): E | 1+T^s m'g'^2, mod TL' */
  e[6] = W + Y + divc(s - 1 + y, a + y + z, a + y, 0);                /* (w1,g'): E | g'T^{s-1}+w1, mod Tw1g' */
  e[7] = Z + W + divc(s - 2, a + y + z, z + a, 1);                    /* (m',w1): E | T^{s-2}+m'w1^2, mod Tm'w1 */
  e[8] = WB + Y + divc(s - 1 + y, b + y + z, b + y, 0);               /* (C1,g') */
  e[9] = Z + WB + divc(z + 2 * b - 2, b + y + z, z + b, 1);           /* (m',C1) */
  e[10] = V + W + divc(s - 1 - a, b - 1, t - 1, 1);                   /* (v1,w1): C1 | (T^{s-2}+v1)/w1, mod Tv1 */
  e[11] = V + WB + divc(s - 1 - b, a - 1, t - 1, 1);                  /* (v1,C1) */
  e[12] = V + lD(s - 2, a - 1) + divc(s - 1 - a, b - 1, t - 1, 1);    /* v1, w1 | T^{s-2}+v1, then C1 */
  e[13] = V + lD(s - 2, b - 1) + divc(s - 1 - b, a - 1, t - 1, 1);
  e[14] = Y + V + lD(s - 2, a - 1);                                   /* (g',v1), w1 | T^{s-2}+v1 */
  e[15] = Y + V + lD(s - 2, b - 1);
  e[16] = Z + V + lD(a + b - 2, a - 1);                               /* (m',v1), w1 | (T^{s-2}+v1)/m' */
  e[17] = Z + L2 + Somega(t - 2) + divc(a + b - 2, a - 1, t - 1, 1);  /* (m',v1), w1 in sqrt classes mod Tv1 */
  e[18] = L2 + Somega(t - 2) + lD(s - 2, z) + divc(a + b - 2, a - 1, t - 1, 1);  /* v1, m' | T^{s-2}+v1, classes */
  int nr = 19;
  if (NEWR) {   /* FF_STERILE_SMALL Lemmas 1.2-1.3: v1 in a class mod the fixed factors */
    int ev = t - 2;
    e[19] = Z + logV(ev, z) + lD(a + b - 2, a - 1);                                   /* (m', v1) -> w1 | G */
    e[20] = Z + L2 + logSomClass(ev, z) + divc(a + b - 2, a - 1, t - 1, 1);           /* (m', v1), sqrt classes */
    e[21] = W + logV(ev, a - 1) + divc(s - 1 - a, b - 1, t - 1, 1);                   /* (w1, v1) -> C1 */
    e[22] = WB + logV(ev, b - 1) + divc(s - 1 - b, a - 1, t - 1, 1);                  /* (C1, v1) -> w1 */
    e[23] = L2 + Y + Z + logV(ev, z);                                                 /* (m', g', v1), 2 roots */
    e[24] = Y + W + logV(ev, a - 1);                                                  /* (g', v1, w1) */
    e[25] = Z + W + logV(ev, z + a - 1);                                              /* (m', w1, v1) */
    nr = 26;
  }
  int am = 0; for (int i = 1; i < nr; i++) if (e[i] < e[am]) am = i;
  if (arg) *arg = am;
  return e[am];
}
#ifndef NO_MAIN
int main(int argc, char **argv) {
  int r = atoi(argv[1]), S = atoi(argv[2]); if (argc > 3) COP = atoi(argv[3]);
  int every = argc > 4 ? atoi(argv[4]) : 10;
  if (argc > 5) NEWR = REF = atoi(argv[5]);
  init_omstar(powl(3.0L, r));
  if (argc > 6) RANK = atoi(argv[6]);
  if (RANK) init_rankin(powl(3.0L, r));
  lq = r * logl(3.0L);
  lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  LD tot = 0; long cnt[NR] = {0};
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
  printf("r=%d cop=%d total(3<=s<=%d)=%.12Le\nroute argmin counts:", r, COP, S, tot);
  for (int i = 0; i < NR; i++) printf(" %s:%ld", rname[i], cnt[i]);
  printf("\n");
  return 0;
}
#endif
