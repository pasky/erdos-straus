// z56 FAMATTACK: exact (★) count R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n} for odd n,
// with a window decomposition of the unordered solutions (u < B) on a 5x5 grid
//   ia = floor(10 * log(u)/log(n))  (clamped to 0..4; u < B forces u <= sqrt(n)/2, so a < 1/2)
//   ic = floor(5 * log(C)/log(n))   (clamped to 0..4)
// R(n) = 2 * #{u < B} (u = B is impossible for odd n).
// Method: for each u <= (sqrt(4n+5)-1)/4, factor N = n + u (segmented sieve), enumerate divisors m of N
// with m = 4uC - 1 (m ≡ -1 mod 4u) and B = N/m > u.  Then 4uBC - u - B = n exactly.
// Usage:  wcount range LO HI      -> all primes n ≡ 1 (mod 4) in [LO, HI]
//         wcount list             -> odd n read from stdin (one per line), any n (prime or not)
// Output: n R g00 g01 ... g44   (g[ia*5+ic], counts of unordered solutions)
// Build: gcc -O2 -o wcount z56_famattack_wcount.c -lm
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

static u64 *primes; static long nprimes;
static void make_primes(u64 lim) {
  char *s = calloc(lim + 1, 1); primes = malloc(sizeof(u64) * (lim / 2 + 10)); nprimes = 0;
  for (u64 i = 2; i <= lim; i++) { if (!s[i]) { primes[nprimes++] = i; for (u64 j = i * i; j <= lim; j += i) s[j] = 1; } }
  free(s);
}

#define MAXF 16
typedef struct { u64 rem; int nf; u64 q[MAXF]; int e[MAXF]; } fac_t;
static fac_t *F; static long Fcap = 0;

static long long grid[25];
static long long cnt_pairs;
static double logn;

static void enum_div(u64 N, u64 u, fac_t *f, u64 n) {
  // enumerate divisors m of N; test m ≡ -1 mod 4u and N/m > u
  u64 divs[1 << 14]; int nd = 1; divs[0] = 1;
  for (int i = 0; i < f->nf; i++) {
    int cur = nd; u64 pw = 1;
    for (int k = 1; k <= f->e[i]; k++) {
      pw *= f->q[i];
      for (int j = 0; j < cur; j++) { if (nd >= (1 << 14)) { fprintf(stderr, "too many divisors\n"); exit(1); } divs[nd++] = divs[j] * pw; }
    }
  }
  u64 mod = 4 * u;
  for (int j = 0; j < nd; j++) {
    u64 m = divs[j];
    if ((m + 1) % mod) continue;
    u64 B = N / m;
    if (B <= u) continue;
    u64 C = (m + 1) / mod;
    // sanity: 4uBC - u - B == n
    if ((u128)4 * u * B * C - u - B != n) { fprintf(stderr, "check fail n=%llu u=%llu B=%llu C=%llu\n", n, u, B, C); exit(2); }
    cnt_pairs++;
    int ia = (int)floor(10.0 * log((double)u) / logn); if (ia < 0) ia = 0; if (ia > 4) ia = 4;
    int ic = (int)floor(5.0 * log((double)C) / logn); if (ic < 0) ic = 0; if (ic > 4) ic = 4;
    grid[ia * 5 + ic]++;
  }
}

static void process(u64 n) {
  u64 U = (u64)((sqrtl(4.0L * n + 5) - 1) / 4) + 1;
  while (U > 1 && 4 * U * U + 2 * U - 1 > n) U--;
  if (U + 1 > (u64)Fcap) { Fcap = U + 1; F = realloc(F, sizeof(fac_t) * Fcap); }
  for (u64 u = 1; u <= U; u++) { F[u].rem = n + u; F[u].nf = 0; }
  u64 lim = (u64)sqrtl((long double)(n + U)) + 1;
  for (long i = 0; i < nprimes && primes[i] <= lim; i++) {
    u64 q = primes[i];
    u64 r = (n + 1) % q; // u=1 corresponds to n+1
    u64 start = (q - r) % q + 1; // smallest u>=1 with q | n+u
    for (u64 u = start; u <= U; u += q) {
      fac_t *f = &F[u]; int e = 0;
      while (f->rem % q == 0) { f->rem /= q; e++; }
      f->q[f->nf] = q; f->e[f->nf] = e; f->nf++;
    }
  }
  memset(grid, 0, sizeof grid); cnt_pairs = 0; logn = log((double)n);
  for (u64 u = 1; u <= U; u++) {
    fac_t *f = &F[u];
    if (f->rem > 1) { f->q[f->nf] = f->rem; f->e[f->nf] = 1; f->nf++; f->rem = 1; }
    enum_div(n + u, u, f, n);
  }
  printf("%llu %lld", n, 2 * cnt_pairs);
  for (int i = 0; i < 25; i++) printf(" %lld", grid[i]);
  printf("\n");
}

int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage\n"); return 1; }
  if (!strcmp(argv[1], "range")) {
    u64 lo = strtoull(argv[2], 0, 10), hi = strtoull(argv[3], 0, 10);
    make_primes((u64)sqrtl((long double)hi * 1.01L) + 100);
    u64 n = lo; while (n % 4 != 1) n++;
    for (; n <= hi; n += 4) if (is_prime(n)) process(n);
  } else {
    u64 lim = argc > 2 ? strtoull(argv[2], 0, 10) : 2000000;
    make_primes(lim);
    u64 n;
    while (scanf("%llu", &n) == 1) { if ((u64)lim * lim < n + n) { fprintf(stderr, "raise lim\n"); return 3; } process(n); }
  }
  return 0;
}
