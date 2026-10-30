/* z52_bank_types.c — coprime (Elsholtz–Tao) Type I / Type II census for odd n (z52 bank §1(d)).
 * ET: a solution (x,y,z) of 4/n = 1/x+1/y+1/z is Type I if n | x and gcd(n, yz) = 1, Type II if n | y, n | z, gcd(n, x) = 1
 * (up to permutation).  All solutions are enumerated by the divisor method: every solution has a coordinate x with
 * n/4 < x <= 3n/4 (its least one); m = 4x - n; (m y - n x)(m z - n x) = (n x)^2 (both factors positive), so (y, z) come
 * from divisor pairs D D' = (nx)^2 with D, D' = -nx (mod m).
 * usage: z52_bank_types scan NMAX      -> odd non-squares n <= NMAX with no coprime Type I/II solution (early exit otherwise)
 *        z52_bank_types list n         -> all solutions with x <= y <= z and their classification
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static uint32_t *spf;
static u64 gcd(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static int cls(u64 n, u128 a, u128 b, u128 c) { /* bit0: coprime Type I, bit1: coprime Type II */
  u64 v[3] = { (u64)(a % n), (u64)(b % n), (u64)(c % n) }; int r = 0;
  for (int i = 0; i < 3; i++) {
    u64 x = v[i], y = v[(i + 1) % 3], z = v[(i + 2) % 3];
    if (x == 0 && gcd(n, y) == 1 && gcd(n, z) == 1) r |= 1;
    if (gcd(n, x) == 1 && y == 0 && z == 0) r |= 2;
  }
  return r;
}
#define DCAP 4000000
static u128 divs[DCAP];
static int factor_into(u64 v, u64 *pr, int *ex, int k) {
  while (v > 1) { u64 q = spf[v]; int e = 0; while (v % q == 0) { v /= q; e++; }
    int j; for (j = 0; j < k; j++) if (pr[j] == q) { ex[j] += e; break; }
    if (j == k) { pr[k] = q; ex[k] = e; k++; } }
  return k;
}
/* enumerate solutions for n; mode 0: return 1 at first coprime I/II; mode 1: print all (x<=y<=z) */
static int run(u64 n, int mode, long *cnt) {
  u64 pr[64]; int ex[64];
  for (u64 x = n / 4 + 1; 4 * x <= 3 * n; x++) {
    u64 m = 4 * x - n, nx = n * x;
    int k = factor_into(n, pr, ex, 0); k = factor_into(x, pr, ex, k);
    int nd = 1; divs[0] = 1;
    for (int i = 0; i < k; i++) { int cur = nd; u128 vv = 1;
      for (int e = 1; e <= 2 * ex[i]; e++) { vv *= pr[i]; for (int j = 0; j < cur; j++) { if (nd >= DCAP) { fprintf(stderr, "DCAP\n"); exit(2); } divs[nd++] = divs[j] * vv; } } }
    u128 N = (u128)nx * nx; u64 r = (m - nx % m) % m; (void)0;
    for (int i = 0; i < nd; i++) {
      u128 D = divs[i]; if (D > N / D) continue;   /* D <= D' */
      u128 Dp = N / D;
      if ((u64)(D % m) != r || (u64)(Dp % m) != r) continue;
      u128 y = (D + nx) / m, z = (Dp + nx) / m;
      if (y < x) continue;                               /* keep x least: each solution once */
      { const u128 P = 2305843009213693951ULL; u128 X = x % P, Y = y % P, Z = z % P;   /* check mod 2^61-1 */
        u128 L = 4 * X % P * Y % P * Z % P, R = n % P * ((X * Y + Y * Z + Z * X) % P) % P;
        if (L != R) { fprintf(stderr, "BUG\n"); exit(1); } }
      int c = cls(n, x, y, z);
      if (mode == 0 && c) return 1;
      if (mode == 1) printf("%llu %llu %llu  typeI=%d typeII=%d\n", x, (u64)y, (u64)z, c & 1, (c >> 1) & 1);
      cnt[c]++;
    }
  }
  return 0;
}
int main(int argc, char **argv) {
  u64 N = strtoull(argv[2], 0, 10), M = (argv[1][0] == 's' ? N : N) + 10;
  spf = calloc(M + 1, 4);
  for (u64 i = 2; i <= M; i++) if (!spf[i]) for (u64 j = i; j <= M; j += i) if (!spf[j]) spf[j] = (uint32_t)i;
  long cnt[4] = { 0, 0, 0, 0 };
  if (argv[1][0] == 'l') { run(N, 1, cnt); printf("n=%llu: solutions %ld (neither %ld, typeI-only %ld, typeII-only %ld, both %ld)\n", N, cnt[0]+cnt[1]+cnt[2]+cnt[3], cnt[0], cnt[1], cnt[2], cnt[3]); return 0; }
  for (u64 n = 3; n <= N; n += 2) {
    u64 s = (u64)sqrt((double)n); while (s * s > n) s--; while ((s + 1) * (s + 1) <= n) s++;
    int sq = (s * s == n);
    if (sq && getenv("SKIPSQ")) continue;  /* T1 (ET Prop 1.6) proves squares are zeros */
    if (!run(n, 0, cnt)) printf("%llu %s\n", n, sq ? "square" : "NONSQUARE-ZERO");
    else if (sq) printf("%llu SQUARE-WITH-COPRIME-SOLUTION\n", n);
    fflush(stdout);
  }
  return 0;
}
