/* z52_bank_gauss.c — ES_Q1 over Z[i]: 4/n = 1/x + 1/y + 1/z with x, y, z in Q1 = {Re >= 0, Im >= 0} \ {0}
 * (fable-2 / argon-4 of the generators board).  Census over Gaussian primes n = a + b i, 0 < a < b, N = a^2+b^2 prime,
 * Nlo < N <= Nhi (one representative per rational prime p = 1 (4); b + a i = i * conj(a + b i) is equivalent).
 *
 * Search bounds (proof in Z52_BANKED.md T3): u_j := 1/x_j lie in the closed 4th quadrant and sum to w = 4/n, so each
 * u_j lies in the rectangle [0, Re w] x [Im w, 0]; hence N(x_j) >= N/16, Re x_j * N <= 4a N(x_j), Im x_j * N <= 4b N(x_j),
 * and the coordinate with the largest |u_j| (= least norm) has N(x) <= 9N/16.
 * For a candidate x put m = 4x - n, M = n x: 1/y + 1/z = m/M  <=>  (m y - M)(m z - M) = M^2.  We enumerate ALL Gaussian
 * divisors D of M^2 (all four unit multiples), require m | D + M and m | M^2/D + M, set y = (D+M)/m, z = (M^2/D+M)/m and
 * keep y, z in Q1.  Every solution is verified exactly (4xyz = n(xy+yz+zx) in Z[i], 128-bit).
 * usage: z52_bank_gauss MODE Nlo Nhi [stride offset]
 *   MODE first: print "a b N  xr xi yr yi zr zi" for the first solution found, or "a b N FAIL" after the complete search.
 *   MODE count: print "a b N count" with count = #unordered triples (complete).
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef int64_t i64; typedef __int128 i128;
typedef struct { i128 r, i; } G;
static G gmul(G a, G b) { G c = { a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r }; return c; }
static G gadd(G a, G b) { G c = { a.r + b.r, a.i + b.i }; return c; }
static i128 gnorm(G a) { return a.r * a.r + a.i * a.i; }
/* exact division a/b if b | a, returns 1 on success */
static int gdiv(G a, G b, G *q) {
  i128 nb = gnorm(b); G t = gmul(a, (G){ b.r, -b.i });
  if (t.r % nb || t.i % nb) return 0;
  q->r = t.r / nb; q->i = t.i / nb; return 1;
}
static int inQ1(G a) { return a.r >= 0 && a.i >= 0 && (a.r || a.i); }
static int gless(G a, G b) { /* total order: norm, then re, then im */
  i128 na = gnorm(a), nb = gnorm(b);
  if (na != nb) return na < nb; if (a.r != b.r) return a.r < b.r; return a.i < b.i;
}

static uint32_t *spf; static int32_t *ga, *gb; /* ga[p]+gb[p] i: a Gaussian prime over p = 1 (4) */
static long NMAXP;

#define MAXGP 64
typedef struct { int k; G pr[MAXGP]; int e[MAXGP]; } GF;
static void gf_add(GF *F, G p, int e) {
  for (int j = 0; j < F->k; j++) {
    /* same prime up to unit? compare by dividing */
    G q; if (gnorm(F->pr[j]) == gnorm(p) && gdiv(p, F->pr[j], &q) && gnorm(q) == 1) { F->e[j] += e; return; }
  }
  F->pr[F->k] = p; F->e[F->k] = e; F->k++;
}
/* factor x (nonzero) up to a unit */
static void gfactor(G x, GF *F) {
  i128 nx = gnorm(x); long t = (long)nx;
  while (t > 1) {
    long l = spf[t]; int e = 0; while (t % l == 0) { t /= l; e++; }
    if (l == 2) gf_add(F, (G){ 1, 1 }, e);
    else if (l % 4 == 3) gf_add(F, (G){ l, 0 }, e / 2);
    else {
      G p = { ga[l], gb[l] }, pc = { ga[l], -gb[l] }, y = x, q; int f = 0;
      while (gdiv(y, p, &q)) { y = q; f++; }
      if (f) gf_add(F, p, f);
      if (e - f) gf_add(F, pc, e - f);
    }
  }
}

static long nsol_count; static G sol[3]; static int mode_first;
static long checked_D;

/* try candidate x for n; return 1 if a solution was found (first mode) */
static int try_x(G n, G x) {
  G m = gadd(gmul((G){ 4, 0 }, x), (G){ -n.r, -n.i });
  if (m.r == 0 && m.i == 0) return 0;
  G M = gmul(n, x), M2 = gmul(M, M);
  GF F; F.k = 0; gf_add(&F, n, 1);
  gfactor(x, &F);
  /* exponents of M^2 */
  int ex[MAXGP]; for (int j = 0; j < F.k; j++) ex[j] = 2 * F.e[j];
  int cur[MAXGP]; memset(cur, 0, sizeof cur);
  G units[4] = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };
  int found = 0;
  for (;;) {
    G D = { 1, 0 };
    for (int j = 0; j < F.k; j++) for (int c = 0; c < cur[j]; c++) D = gmul(D, F.pr[j]);
    for (int uu = 0; uu < 4; uu++) {
      G Du = gmul(D, units[uu]), Dp, y, z;
      checked_D++;
      if (!gdiv(M2, Du, &Dp)) { fprintf(stderr, "BUG divisor\n"); exit(5); }
      if (!gdiv(gadd(Du, M), m, &y)) continue;
      if (!gdiv(gadd(Dp, M), m, &z)) continue;
      if (!inQ1(y) || !inQ1(z)) continue;
      /* verify 4xyz == n(xy+yz+zx) */
      G lhs = gmul((G){ 4, 0 }, gmul(x, gmul(y, z)));
      G rhs = gmul(n, gadd(gadd(gmul(x, y), gmul(y, z)), gmul(z, x)));
      if (lhs.r != rhs.r || lhs.i != rhs.i) { fprintf(stderr, "VERIFY FAIL\n"); exit(6); }
      if (mode_first) { sol[0] = x; sol[1] = y; sol[2] = z; return 1; }
      /* count each unordered triple once: x least, y <= z in the total order */
      if (!gless(y, x) && !gless(z, y)) nsol_count++;
      found = 1;
    }
    int j = 0; while (j < F.k && cur[j] == ex[j]) { cur[j] = 0; j++; }
    if (j == F.k) break;
    cur[j]++;
  }
  return found && mode_first;
}

int main(int argc, char **argv) {
  if (argc < 4) { fprintf(stderr, "usage\n"); return 1; }
  mode_first = strcmp(argv[1], "first") == 0;
  long Nlo = atol(argv[2]), Nhi = atol(argv[3]);
  long stride = argc > 5 ? atol(argv[4]) : 1, off = argc > 5 ? atol(argv[5]) : 0;
  NMAXP = Nhi + 10;
  spf = calloc(NMAXP + 1, 4); ga = calloc(NMAXP + 1, 4); gb = calloc(NMAXP + 1, 4);
  for (long i = 2; i <= NMAXP; i++) if (!spf[i]) for (long j = i; j <= NMAXP; j += i) if (!spf[j]) spf[j] = (uint32_t)i;
  for (long a = 1; a * a <= NMAXP; a++) for (long b = a + 1; a * a + b * b <= NMAXP; b++) {
    long p = a * a + b * b; if (spf[p] == p && p % 4 == 1) { ga[p] = (int32_t)a; gb[p] = (int32_t)b; }
  }
  long idx = 0;
  for (long p = 5; p <= Nhi; p++) {
    if (p <= Nlo || p % 4 != 1 || spf[p] != p) continue;
    if ((idx++ % stride) != off) continue;
    G n = { ga[p], gb[p] }; /* 0 < a < b */
    long a = ga[p], b = gb[p];
    long R = (long)(0.75 * sqrt((double)p)) + 2;
    nsol_count = 0; int done = 0;
    /* passes by |4x - n|^2 <= p/64, <= p/4, <= infinity (ordering only; the union is the full box) */
    double lim[3] = { p / 64.0, p / 4.0, 1e300 }, prev = -1;
    for (int pass = 0; pass < 3 && !done; pass++) {
      for (long xr = 0; xr <= R && !done; xr++) for (long xi = 0; xi <= R && !done; xi++) {
        if (!xr && !xi) continue;
        long nx = xr * xr + xi * xi;
        if (16 * nx < p || 16 * nx > 9 * p) continue;          /* N/16 <= N(x) <= 9N/16 */
        if (xr * p > 4 * a * nx || xi * p > 4 * b * nx) continue; /* rectangle constraints */
        double key = (double)(4 * xr - a) * (4 * xr - a) + (double)(4 * xi - b) * (4 * xi - b);
        if (key > lim[pass] || key <= prev) continue;
        if (try_x(n, (G){ xr, xi })) done = 1;
      }
      prev = lim[pass];
    }
    if (mode_first) {
      if (done) printf("%ld %ld %ld  %ld %ld %ld %ld %ld %ld\n", a, b, p, (long)sol[0].r, (long)sol[0].i,
                       (long)sol[1].r, (long)sol[1].i, (long)sol[2].r, (long)sol[2].i);
      else printf("%ld %ld %ld FAIL\n", a, b, p);
    } else printf("%ld %ld %ld %ld\n", a, b, p, nsol_count);
    fflush(stdout);
  }
  fprintf(stderr, "checked divisors: %ld\n", checked_D);
  return 0;
}
