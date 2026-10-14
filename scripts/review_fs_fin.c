/* review_fs_fin.c (R217, from scratch): finite part of the left side of (Sigma) of FF_STERILE_PUSH, Case B,
   q = 3^r, k = 2, levels 3 <= s <= S:
     sum_s q^{1 - ceil(s/2)} sum_{patterns (a,z,y,t)} mult * min_routes bound
   Patterns: a >= 1, z >= 0, y >= 0, t >= 2, b = y + t >= a, s = a + z + y + t; mult = 2 if a < b else 1.
   Route bounds re-derived by R217 (see reviews/ff-sterile-push-review.md, Lemma 1.6 section); written independently of
   scripts/fs_sum.c. The class-divisor count uses: 1 if d < rho (or n-d < rho), 2 if 3 rho > n (Lemma 1.4), and
   the least j = m + k with n m(m+1) + (d - rho) j(j+1) < 2 (j+1) m d   (Lemma 1.5 (C), rewritten: the
   k-dependence of Delta(m,k) collapses to j(j+1)/2), m <= j <= JMAX; and C(n,d) (Lemma 1.3).
   Arithmetic: long double logs of exact integers; all terms are exp(sum of < 100 logs), relative error < 1e-14;
   the printed total is multiplied by (1 + 1e-9) and rounded up in the last printed digit.
   usage: review_fs_fin r S [JMAX=200] */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long double LD;
static int JMAX = 3000;
static LD L;            /* log q */
static LD lf[4000];     /* log factorial */
static LD lbin(long n, long d) { return lf[n] - lf[d] - lf[n - d]; }
static LD lNs(long d) { return d == 0 ? 0.0L : (d - 1) * L + logl(expl(L) - 1.0L); }  /* log(q^d - q^{d-1}) */
static LD lSom(long e) {   /* log sum_{v monic deg e} 2^omega(v) = log( q^e (2 + (e-1)(1 - 1/q)) ), e>=1; 0 for e=0 */
  if (e == 0) return 0.0L;
  return e * L + logl(2.0L + (LD)(e - 1) * (1.0L - expl(-L)));
}
/* class bound for divisors of degree d of F (deg n) in a unit class mod Q (deg rho); cof: cofactor version allowed */
static long jcop(long n, long d, long rho) {          /* least j = m + k with (C), or 0 */
  long X = d - rho; if (X < 0) return 1;
  /* necessary: by AM-GM, n m(m+1) + X j(j+1) >= 2 sqrt(nX) sqrt(m(m+1)j(j+1)) >= 2 sqrt(nX) m (j+1) for m <= j,
     so (C) needs n X < d^2 */
  if (n * X >= d * d) return 0;
  /* for fixed j the left side minus right side is convex in m: n m^2 + m (n - 2(j+1)d) + X j(j+1); its integer
     minimum over 1 <= m <= j is at floor/ceil of m* = (2(j+1)d - n)/(2n), clamped */
  for (long j = 1; j <= JMAX; j++) {
    long m0 = (2 * (j + 1) * d - n) / (2 * n);
    for (long m = m0 - 1; m <= m0 + 2; m++) {
      if (m < 1 || m > j) continue;
      if (n * m * (m + 1) + X * j * (j + 1) < 2 * (j + 1) * m * d) return j;
    }
    if (m0 > j) { long m = j; if (n * m * (m + 1) + X * j * (j + 1) < 2 * (j + 1) * m * d) return j; }
    if (m0 < 1) { long m = 1; if (n * m * (m + 1) + X * j * (j + 1) < 2 * (j + 1) * m * d) return j; }
  }
  return 0;
}
static LD lcls(long n, long d, long rho, int cof) {
  LD best = lbin(n, d);
  if (d < rho || (cof && n - d < rho)) return 0.0L;     /* at most one */
  long c = 0;
  if (3 * rho > n) c = 2;
  long j = jcop(n, d, rho); if (j && (!c || j < c)) c = j;
  if (cof) { j = jcop(n, n - d, rho); if (j && (!c || j < c)) c = j; }
  if (c && logl((LD)c) < best) best = logl((LD)c);
  return best;
}
static LD mn(LD x, LD y) { return x < y ? x : y; }
LD lbound(long s, long a, long z, long y, long t) {
  long b = y + t;
  LD m_ = lNs(z), g_ = lNs(y), w_ = lNs(a - 1), c_ = lNs(b - 1), v_ = lNs(t - 2), l2 = logl(2.0L);
  LD r = m_ + g_ + w_;                                           /* T0: (m',g',w) */
  r = mn(r, m_ + w_ + v_);                                       /* R4': (m',w,v) */
  r = mn(r, l2 + m_ + g_ + v_);                                  /* X1: (m',g',v), quadratic */
  r = mn(r, g_ + v_ + w_);                                       /* X2: (g',v,w) */
  r = mn(r, v_ + lf[s - 2] - lf[z] - lf[a - 1] - lf[b - 1]);     /* R1 */
  r = mn(r, m_ + g_ + lcls(s + 2 * y + z, a + y + z, 1 + y + z, 1));       /* R2 */
  r = mn(r, w_ + g_ + lcls(s - 1 + y, a + y + z, a + y, 0));               /* R3 */
  r = mn(r, m_ + w_ + lcls(s - 2, a + y + z, a + z, 1));                   /* R4 */
  r = mn(r, c_ + g_ + lcls(s - 1 + y, b + y + z, b + y, 0));               /* R3C */
  r = mn(r, m_ + c_ + lcls(z + 2 * b - 2, b + y + z, b + z, 1));           /* R4C */
  r = mn(r, v_ + w_ + lcls(s - 1 - a, b - 1, t - 1, 1));                   /* R5a */
  r = mn(r, v_ + c_ + lcls(s - 1 - b, a - 1, t - 1, 1));                   /* R5b */
  r = mn(r, v_ + lbin(s - 2, a - 1) + lcls(s - 1 - a, b - 1, t - 1, 1));   /* R6a */
  r = mn(r, v_ + lbin(s - 2, b - 1) + lcls(s - 1 - b, a - 1, t - 1, 1));   /* R6b */
  r = mn(r, g_ + v_ + lbin(s - 2, a - 1));                                 /* R8a */
  r = mn(r, g_ + v_ + lbin(s - 2, b - 1));                                 /* R8b */
  r = mn(r, m_ + v_ + lbin(a + b - 2, a - 1));                             /* R9a */
  r = mn(r, m_ + l2 + lSom(t - 2) + lcls(a + b - 2, a - 1, t - 1, 1));     /* R10a */
  r = mn(r, l2 + lSom(t - 2) + lbin(s - 2, z) + lcls(a + b - 2, a - 1, t - 1, 1));  /* R10b */
  return r;
}
#ifndef NOMAIN
int main(int argc, char **argv) {
  int r = atoi(argv[1]); long S = atol(argv[2]); if (argc > 3) JMAX = atoi(argv[3]);
  L = r * logl(3.0L);
  lf[0] = 0; for (int i = 1; i < 4000; i++) lf[i] = lf[i - 1] + logl((LD)i);
  LD tot = 0;
  for (long s = 3; s <= S; s++) {
    LD term = 0;
    for (long a = 1; a <= s; a++) for (long z = 0; a + z <= s; z++) for (long y = 0; a + z + y <= s; y++) {
      long t = s - a - z - y, b = y + t;
      if (t < 2 || b < a) continue;
      term += (a < b ? 2 : 1) * expl(lbound(s, a, z, y, t) + (1 - (s + 1) / 2) * L);
    }
    tot += term;
    if (s <= 15 || s % 10 == 0) printf("s=%ld term=%.12Le cum=%.12Le\n", s, term, tot);
    fflush(stdout);
  }
  printf("FINAL r=%d S=%ld finite_upper=%.12Le\n", r, S, tot * (1.0L + 1e-9L));
  return 0;
}
#endif
