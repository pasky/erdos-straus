// z57 COMPLEMENT: per-prime census of the length-3 word set and its certificate slices.
//
// W(n) = {(t,u,v) in N^3, t,u,v >= 1 : t*u*v - u - v = n}   (ordered: (t,u,v) and (t,v,u) are distinct words)
// Every word with u <= v is found from the integer N = n + u:  m := t*u - 1 divides N, m ≡ -1 (mod u),
// t = (m+1)/u, v = N/m, and u <= v  <=>  m <= N/u; u <= 1 + sqrt(n+1).  (v*(tu-1) = n + u.)
//
// Slices (DEDEKIND_ES Thm 4.5; n ≡ 1 mod 4, t,u,v >= 2): the Jacobi symbol (A/n), A = tu - 1, is -1 iff
//   STAR: 4 | t           ((★) = ET Type II c = 1 line; (u,B,C) = (u,v,t/4))
//   B1  : 4 | u or 4 | v  (López Type A / b = 1 line; 4xy | p + 4x + y with (u,v) = (4x,y))
//   I1  : 4 | tu-1 or 4 | tv-1   (ET Type I, slice a = 1)
//   QR  : none of the above (Jacobi +1; not a certificate; placebo family)
// Boundary words (some of t,u,v equal to 1) are reported separately (BND) and also counted in STAR/B1/I1 if they
// satisfy the congruence (they are certificates there: CONDITIONAL_ES Lemma 1.1, FRONTIER (★) allows u = 1).
//
// For each family the words are binned by z = log t / log n into 10 bands [k/10,(k+1)/10).
// STAR extra splits (Z56_FAMDESIGN): G = {Q^4 > P*n} (P = min(u,v), Q = max(u,v)), K = STAR \ G,
//   H3 = {64 C^3 <= n}, HC = {C <= floor(log^2 n)}  (C = t/4).
// c-lines (ET Type II, c >= 2): words of W(c*n) with 4c | t  (4abcd - a - b = c n, (t,u,v) = (4cd, a, b)).
//
// Usage: z57_complement_words range LO HI [C2]   -> all primes n ≡ 1 (mod 4) in [LO,HI]
//        z57_complement_words list [C2]          -> odd n from stdin (any n ≡ 1 mod 4: primes, squares, composites)
//   C2 = max c for the c-lines (default 3; 1 = none).  Optional env JAC=1: verify Thm 4.5 by computing (A/n).
// Output line: n  W  STAR B1 I1 QR BND  G K H3 HC  c2 .. cC2   then band counts: STAR[10] B1[10] I1[10] QR[10] c2[10] ...
// Build: gcc -O2 -o z57w scripts/z57_complement_words.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef unsigned long long u64;
typedef __uint128_t u128;

static u64 mulmod(u64 a, u64 b, u64 m) { return (u64)((u128)a * b % m); }
static u64 powmod(u64 a, u64 e, u64 m) { u64 r = 1; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int is_prime(u64 n) {
  if (n < 2) return 0;
  static const u64 sp[] = {2,3,5,7,11,13,17,19,23,29,31,37};
  for (int i = 0; i < 12; i++) { if (n % sp[i] == 0) return n == sp[i]; }
  u64 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
  for (int i = 0; i < 12; i++) {
    u64 x = powmod(sp[i], d, n);
    if (x == 1 || x == n - 1) continue;
    int ok = 0;
    for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } }
    if (!ok) return 0;
  }
  return 1;
}
static int jacobi(u64 a, u64 n) { // n odd
  int t = 1; a %= n;
  while (a) { while (!(a & 1)) { a >>= 1; u64 r = n & 7; if (r == 3 || r == 5) t = -t; }
    u64 x = a; a = n; n = x; if ((a & 3) == 3 && (n & 3) == 3) t = -t; a %= n; }
  return n == 1 ? t : 0;
}

static u64 *primes; static long nprimes;
static void make_primes(u64 lim) {
  char *s = calloc(lim + 1, 1); primes = malloc(sizeof(u64) * (lim / 2 + 10)); nprimes = 0;
  for (u64 i = 2; i <= lim; i++) { if (!s[i]) { primes[nprimes++] = i; for (u64 j = i * i; j <= lim; j += i) s[j] = 1; } }
  free(s);
}

#define MAXF 16
typedef struct { u64 rem; int nf; u64 q[MAXF]; int e[MAXF]; } fac_t;
#define BLK 65536
static fac_t F[BLK];

#define NB 10
#define MAXC 8
static int C2 = 3, JAC = 0;
// per-prime accumulators
static long long Wtot, cS, cB, cI, cQ, cBND, cG, cK, cH3, cHC, cc[MAXC + 1];
static long long bS[NB], bB[NB], bI[NB], bQ[NB], bc[MAXC + 1][NB];
static double logn0; static u64 n0, hc_cut; static long long jacfail;

static int band(u64 t, double logn) { if (t <= 1) return 0; int b = (int)floor(NB * log((double)t) / logn); if (b < 0) b = 0; if (b >= NB) b = NB - 1; return b; }

// record word (t,u,v) for base n (c = 1) with multiplicity w (1 or 2 for the mirror)
static void word1(u64 t, u64 u, u64 v, int w) {
  Wtot += w;
  int bnd = (t == 1 || u == 1 || v == 1);
  int s = (t % 4 == 0), b1 = (u % 4 == 0) || (v % 4 == 0);
  // I1 per orientation: 4 | tu-1 or 4 | tv-1 (symmetric under u<->v, so mirror has the same flag)
  int i1 = ((t * u) % 4 == 1) || ((t * v) % 4 == 1);  // t*u may overflow only mod 2^64, and 2^64 ≡ 0 mod 4: ok
  int bd = band(t, logn0);
  if (bnd) cBND += w;
  if (s) { cS += w; bS[bd] += w;
    u64 P = u < v ? u : v, Q = u < v ? v : u, C = t / 4;
    int inG;
    if (Q >= (1ULL << 32)) inG = 1; else { u128 q4 = (u128)Q * Q; q4 = q4 * Q * Q; inG = q4 > (u128)P * n0; }
    if (inG) cG += w; else cK += w;
    if (C <= (n0 / 64) / C / C) cH3 += w;     // 64 C^3 <= n  (floor-chain is exact for integers)
    if (C <= hc_cut) cHC += w; }
  if (b1) { cB += w; bB[bd] += w; }
  if (i1) { cI += w; bI[bd] += w; }
  if (!bnd && !s && !b1 && !i1) { cQ += w; bQ[bd] += w; }
  if (JAC && !bnd) { u64 A = t * u - 1; int j = jacobi(A, n0); int pred = (s || b1 || i1) ? -1 : 1;
    if (j != pred) jacfail++; }
}

static void enum_words(u64 N, u64 u, fac_t *f, u64 n, int c) {
  // divisors m of N with m ≡ -1 (mod u), m <= N/u, m >= 1
  static u64 divs[1 << 15]; int nd = 1; divs[0] = 1;
  u64 lim = N / u;
  for (int i = 0; i < f->nf; i++) {
    int cur = nd; u64 pw = 1;
    for (int k = 1; k <= f->e[i]; k++) {
      pw *= f->q[i];
      for (int j = 0; j < cur; j++) { u64 d = divs[j] * pw; if (d > lim) continue;
        if (nd >= (1 << 15)) { fprintf(stderr, "too many divisors\n"); exit(1); } divs[nd++] = d; }
    }
  }
  for (int j = 0; j < nd; j++) {
    u64 m = divs[j];
    if ((m + 1) % u) continue;
    u64 t = (m + 1) / u, v = N / m;
    if (v < u) continue;
    int w = (v == u) ? 1 : 2;
    if (c == 1) word1(t, u, v, w);
    else if (t % (4 * (u64)c) == 0) { cc[c] += w; bc[c][band(t, log((double)n))] += w; }
  }
}

static void run_base(u64 n, int c) {
  // all words of W(n) with u <= v: factor N = n + u, u = 1 .. U
  u64 U = 2 + (u64)sqrtl((long double)n + 1);
  // u <= v forces (u-1)^2 <= (u-1)(v-1) <= n+1 (t >= 1), so U is a safe upper bound (extra u give no words with u <= v)
  for (u64 base = 1; base <= U; base += BLK) {
    u64 len = (U - base + 1 < BLK) ? (U - base + 1) : BLK;
    u64 lo = n + base;
    for (u64 i = 0; i < len; i++) { F[i].rem = lo + i; F[i].nf = 0; }
    u64 hi = lo + len - 1;
    for (long k = 0; k < nprimes; k++) {
      u64 q = primes[k]; if (q * q > hi) break;
      u64 st = (lo % q) ? (q - lo % q) : 0;
      for (u64 i = st; i < len; i += q) {
        fac_t *f = &F[i]; int e = 0; while (f->rem % q == 0) { f->rem /= q; e++; }
        f->q[f->nf] = q; f->e[f->nf] = e; f->nf++;
      }
    }
    for (u64 i = 0; i < len; i++) {
      fac_t *f = &F[i]; if (f->rem > 1) { f->q[f->nf] = f->rem; f->e[f->nf] = 1; f->nf++; f->rem = 1; }
      enum_words(lo + i, base + i, f, n, c);
    }
  }
}

static void do_n(u64 n) {
  Wtot = cS = cB = cI = cQ = cBND = cG = cK = cH3 = cHC = 0; jacfail = 0;
  memset(cc, 0, sizeof cc); memset(bS, 0, sizeof bS); memset(bB, 0, sizeof bB); memset(bI, 0, sizeof bI);
  memset(bQ, 0, sizeof bQ); memset(bc, 0, sizeof bc);
  n0 = n; logn0 = log((double)n);
  long double L2 = logl((long double)n); L2 *= L2; hc_cut = (u64)floorl(L2);
  run_base(n, 1);
  for (int c = 2; c <= C2; c++) run_base((u64)c * n, c);
  printf("%llu %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld", n, Wtot, cS, cB, cI, cQ, cBND, cG, cK, cH3, cHC);
  for (int c = 2; c <= C2; c++) printf(" %lld", cc[c]);
  for (int b = 0; b < NB; b++) printf(" %lld", bS[b]);
  for (int b = 0; b < NB; b++) printf(" %lld", bB[b]);
  for (int b = 0; b < NB; b++) printf(" %lld", bI[b]);
  for (int b = 0; b < NB; b++) printf(" %lld", bQ[b]);
  for (int c = 2; c <= C2; c++) for (int b = 0; b < NB; b++) printf(" %lld", bc[c][b]);
  if (JAC) printf(" jacfail=%lld", jacfail);
  printf("\n"); fflush(stdout);
}

int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage\n"); return 1; }
  if (getenv("JAC")) JAC = atoi(getenv("JAC"));
  if (!strcmp(argv[1], "range")) {
    u64 LO = strtoull(argv[2], 0, 10), HI = strtoull(argv[3], 0, 10);
    if (argc > 4) C2 = atoi(argv[4]);
    if (C2 > MAXC) C2 = MAXC;
    make_primes((u64)sqrtl((long double)(C2 * HI) * 1.01L) + 1000);
    for (u64 n = LO | 1; n <= HI; n += 2) { if ((n & 3) != 1) continue; if (!is_prime(n)) continue; do_n(n); }
  } else {
    if (argc > 2) C2 = atoi(argv[2]);
    if (C2 > MAXC) C2 = MAXC;
    u64 n, mx = 0; u64 *buf = malloc(sizeof(u64) * 10000000); long cnt = 0;
    while (scanf("%llu", &n) == 1) { buf[cnt++] = n; if (n > mx) mx = n; }
    make_primes((u64)sqrtl((long double)(C2 * mx) * 1.01L) + 1000);
    for (long i = 0; i < cnt; i++) do_n(buf[i]);
  }
  return 0;
}
