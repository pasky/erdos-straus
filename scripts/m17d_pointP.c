/* O139 (POINTWISE_MORDELL17D §3): all P-data of level L whose box contains a given 17-adic point u.
 * By 17D Lemma 2.1(i): u in box(-f mod W) of the N-point (a,b,c,d) of Sigma^II_N (N = 17^(2L-1), W = 17^L,
 * 17 ∤ cd, both orders) iff 17 ∤ b and a ≡ -u*b (mod W). By Lemma 2.2(i), (4a-1)(4b-1) <= 4N+1.
 * Enumeration: part A: a <= ACUT, b ≡ -a/u (mod W); part B: b <= BCUT, a ≡ -u*b (mod W), a > ACUT,
 * with BCUT chosen so that a > ACUT forces b <= BCUT. For each (a,b): e = (-N mod 4ab) must satisfy
 * 1 <= e <= a+b, e | a+b; then c = (a+b)/e, d = (N+e)/(4ab), require 17 ∤ cd, recheck 4abcd = a+b+Nc and
 * (4acd-1) ≡ -u (mod W). Prints "L a b c d" for each covering datum; stderr: candidate counts.
 * Usage: m17d_pointP L U_NUM U_DEN PART   (u = U_NUM/U_DEN as a 17-adic number; PART = A | B | AB)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef __int128 i128;
static u64 W; static u128 N;
static u64 inv_mod(i128 x, u64 m) { /* x^-1 mod m, x coprime to m */
  i128 a = x % (i128)m; if (a < 0) a += m; i128 b = m, s = 1, t = 0;
  while (b) { i128 qq = a / b, r = a - qq * b; a = b; b = r; r = s - qq * t; s = t; t = r; }
  if (a != 1) { fprintf(stderr, "not invertible\n"); exit(2); }
  s %= (i128)m; if (s < 0) s += m; return (u64)s;
}
static u64 mulmod(u64 x, u64 y, u64 m) { return (u64)((u128)x * y % m); }
static long long ncand = 0, nhit = 0; static u64 uW; /* u mod W */
static void pr128(u128 x) { char buf[64]; int i = 63; buf[i] = 0; do { buf[--i] = '0' + (int)(x % 10); x /= 10; } while (x); fputs(buf + i, stdout); }
static int L;
static void check(u128 a, u128 b) {
  ncand++;
  u128 m = 4 * a * b, e = (m - N % m) % m;      /* e ≡ -N (mod m), 0 <= e < m */
  if (e == 0 || e > a + b || (a + b) % e) return;
  u128 c = (a + b) / e, d = (N + e) / m;
  if (c % 17 == 0 || d % 17 == 0 || b % 17 == 0) return;
  if (4 * a * b * c * d != a + b + N * c) { fprintf(stderr, "BUG\n"); exit(3); }
  u128 f = 4 * a * c * d - 1;
  if ((u64)((f + uW) % W) != 0) { fprintf(stderr, "BUG box\n"); exit(4); }
  nhit++; printf("%d ", L); pr128(a); putchar(' '); pr128(b); putchar(' '); pr128(c); putchar(' '); pr128(d); putchar('\n');
}
int main(int argc, char **argv) {
  if (argc < 5) { fprintf(stderr, "usage\n"); return 1; }
  L = atoi(argv[1]); long long un = atoll(argv[2]), ud = atoll(argv[3]); char *part = argv[4];
  W = 1; for (int i = 0; i < L; i++) W *= 17; N = 1; for (int i = 0; i < 2 * L - 1; i++) N *= 17;
  uW = mulmod((u64)(((un % (long long)W) + (long long)W) % (long long)W), inv_mod(ud, W), W);
  if (uW % 17 == 0) { fprintf(stderr, "u not a unit\n"); return 1; }
  u64 negu = (W - uW) % W, neginvu = inv_mod((i128)(W - uW), W);   /* -u, (-u)^-1 = -1/u */
  u128 lim = 4 * N + 1;
  u64 ACUT = 1; while ((u128)(ACUT + 1) * (ACUT + 1) * 68 <= (u128)W * W) ACUT++;   /* ~ W/sqrt(68) */
  /* a > ACUT => 4a-1 >= 4ACUT+3 => 4b-1 <= lim/(4ACUT+3) */
  u64 BCUT = (u64)((lim / (4 * (u128)ACUT + 3) + 1) / 4);
  if (strchr(part, 'A')) for (u64 a = 1; a <= ACUT; a++) {
    if (a % 17 == 0) continue;
    u64 b0 = mulmod(a % W, neginvu, W);          /* b ≡ -a/u */
    if (b0 == 0) continue;
    for (u128 b = b0; (4 * (u128)a - 1) * (4 * b - 1) <= lim; b += W) check(a, b);
  }
  if (strchr(part, 'B')) for (u64 b = 1; b <= BCUT; b++) {
    if (b % 17 == 0) continue;
    u64 a0 = mulmod(b % W, negu, W);             /* a ≡ -u b */
    u128 a = a0; if (a <= ACUT) a += ((ACUT - a) / W + 1) * (u128)W;
    for (; (4 * a - 1) * (4 * (u128)b - 1) <= lim; a += W) check(a, b);
  }
  fprintf(stderr, "L=%d u=%lld/%lld part=%s ACUT=%llu BCUT=%llu candidates=%lld hits=%lld\n", L, un, ud, part, ACUT, BCUT, ncand, nhit);
  return 0;
}
