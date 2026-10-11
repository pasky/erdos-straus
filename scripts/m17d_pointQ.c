/* O139 (POINTWISE_MORDELL17D §3): all Q-data of level k whose box contains a given 17-adic point u.
 * By 17D Lemma 2.1(ii) and the reflection, u is in a Q-box of level k iff some N-point (a,b,c,d) of Sigma^I_F
 * (F = 17^k, 17 ∤ e) with a <= b has 4a^2 d ≡ w (mod F), w ∈ {-u, -1/u}. Lemma 2.2(ii): ad <= (F+1)/2, so
 * min(a,d) <= sqrt((F+1)/2). Loop A: a small, d = w/(4a^2) mod F. Loop D: d small, a = ±sqrt(w/(4d)) mod F.
 * For each pair (a,d) at most 2 data (M17C Lemma 2.1(iv)): f | t = 4a^2 d + 1, f ≡ -F (mod s = 4ad), s^2 > t;
 * f = least residue r1 of -F mod s, or f = t/r2 with r2 = least residue of t*(-F)^-1 mod s.
 * Prints "k a b c d" with the orientation whose first box -4a^2 d contains u. k <= 15 (128-bit).
 * Usage: m17d_pointQ k U_NUM U_DEN
 */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef __int128 i128;
static u64 F;
static u64 inv_mod(u64 x, u64 m) {
  i128 a = x % m, b = m, s = 1, t = 0;
  while (b) { i128 q = a / b, r = a - q * b; a = b; b = r; r = s - q * t; s = t; t = r; }
  if (a != 1) { fprintf(stderr, "not invertible\n"); exit(2); }
  s %= (i128)m; if (s < 0) s += m; return (u64)s;
}
static u64 mm(u64 x, u64 y) { return (u64)((u128)x * y % F); }
static int k; static long long npairs = 0, nhit = 0; static u64 wv[2];
static void pr(u128 x) { char buf[64]; int i = 63; buf[i] = 0; do { buf[--i] = '0' + (int)(x % 10); x /= 10; } while (x); fputs(buf + i, stdout); }
static u64 sqrt_mod(u64 y) { /* a root of r^2 ≡ y mod F, or 0 if none (y unit) */
  u64 r = 0; for (u64 x = 1; x < 17; x++) if ((x * x) % 17 == y % 17) { r = x; break; }
  if (!r) return 0;
  u64 i2r = inv_mod((2 * r) % F, F);
  for (int j = 1; j < k; j++) { u64 s2 = mm(r, r); u64 df = (s2 + F - y) % F; r = (r + F - mm(df, i2r)) % F; }
  /* linear Hensel: each step gains one 17-adic digit; k-1 steps suffice */
  if (mm(r, r) != y % F) { fprintf(stderr, "sqrt BUG\n"); exit(5); }
  return r;
}
static void pair(u64 a, u64 d, int wi) {
  npairs++;
  u128 t = (u128)4 * a * a * d + 1, s = (u128)4 * a * d;
  u128 fs[2]; int nf = 0;
  fs[nf++] = s - (u128)F % s;
  u128 negF = s - (u128)F % s;  /* -F mod s, coprime to s */
  /* r2 = t * negF^-1 mod s ; s < 2^64 since ad <= (F+1)/2 */
  u64 s64 = (u64)s; u64 ni = inv_mod((u64)(negF % s), s64);
  u64 r2 = (u64)((t % s) * ni % s);
  if (r2 && t % r2 == 0) fs[nf++] = t / r2;
  for (int i = 0; i < nf; i++) {
    u128 f = fs[i];
    if (f == 0 || t % f || (f + F) % s) continue;
    u128 c = (f + F) / s; u128 num = (u128)F * a + c;
    if (num % f) continue;
    u128 b = num / f;
    if (b < a || (a + b) % c) continue;
    if (4 * (u128)a * b * c * d != (u128)F * (a + b) + c) { fprintf(stderr, "BUG\n"); exit(3); }
    if (((a + b) / c) % 17 == 0) continue;
    if (i == 1 && fs[0] == fs[1]) continue;
    nhit++; printf("%d ", k);
    if (wi == 0) { pr(a); putchar(' '); pr(b); } else { pr(b); putchar(' '); pr(a); }
    putchar(' '); pr(c); putchar(' '); pr(d); putchar('\n');
  }
}
int main(int argc, char **argv) {
  if (argc < 4) return 1;
  k = atoi(argv[1]); long long un = atoll(argv[2]), ud = atoll(argv[3]);
  if (k > 15) { fprintf(stderr, "k <= 15\n"); return 1; }
  F = 1; for (int i = 0; i < k; i++) F *= 17;
  u64 u = mm((u64)(((un % (long long)F) + (long long)F) % (long long)F), inv_mod((u64)ud, F));
  if (u % 17 == 0) return 1;
  wv[0] = (F - u) % F; wv[1] = inv_mod(wv[0], F);   /* -u, -1/u */
  u64 H = 1; while ((u128)(H + 1) * (H + 1) <= (F + 1) / 2) H++;
  u64 lim = (F + 1) / 2;
  for (int wi = 0; wi < 2; wi++) {
    if (wi == 1 && wv[1] == wv[0]) break;
    u64 w = wv[wi];
    for (u64 a = 1; a <= H; a++) {          /* loop A */
      if (a % 17 == 0) continue;
      u64 d = mm(w, inv_mod(mm(4 % F, mm(a, a)), F));
      if (d && (u128)a * d <= lim) pair(a, d, wi);
    }
    for (u64 d = 1; d <= H; d++) {          /* loop D: a > H */
      if (d % 17 == 0) continue;
      u64 y = mm(w, inv_mod((4 * d) % F, F)); u64 r = sqrt_mod(y);
      if (!r) continue;
      u64 rs[2] = { r, F - r };
      for (int j = 0; j < 2; j++) if (rs[j] > H && (u128)rs[j] * d <= lim) pair(rs[j], d, wi);
    }
  }
  fprintf(stderr, "k=%d u=%lld/%lld pairs=%lld hits=%lld\n", k, un, ud, npairs, nhit);
  return 0;
}
