/* R139 from-scratch pointwise Q-engine for 17D Comp 3.4 (independent of m17d_pointQ.c).
   Q-datum of level k: 4abcd = F(a+b)+c, F = 17^k, a <= b, e = (a+b)/c, 17∤e; boxes -4a^2d, -4b^2d (mod F).
   u in a box <=> 4a^2d ≡ w (mod F), w ∈ {-u, -1/u} (4abd = eF+1 => 4b^2d ≡ 1/(4a^2d)).
   Re-derived bounds: a <= b and c <= a+b <= 2b give acd <= (F+1)/2, so ad <= (F+1)/2 and min(a,d) <= A0 = isqrt((F+1)/2).
   loop 1: a <= A0, d = least residue of w/(4a^2);  loop 2: d <= A0, a ∈ {roots of w/(4d)}, a > A0 (no double count).
   Per pair (a,d), s = 4ad, t = 4a^2d+1: from f*b = Fa+c (f = 4acd-F) one gets f(sb-1) = F t ... we instead use
   f | t, f ≡ -F (mod s), s^2 > t (17-D/M17C Lemma 2.1, re-derived in the review): candidates f = least residue
   of -F mod s, and f = t/g, g = least residue of t*(-F)^{-1} mod s. Then c=(f+F)/s, b=(Fa+c)/f, exact checks.
   As a guard against a wrong reduction, every candidate f with integral c is tested by the full equation.
   Usage: qengine k s t   (u = s/t). */
#include <stdio.h>
#include <stdlib.h>
typedef __int128 i128; typedef unsigned __int128 u128; typedef unsigned long long u64;
static i128 md(i128 x, i128 m) { x %= m; return x < 0 ? x + m : x; }
static i128 inv(i128 a, i128 m) {
  i128 g = m, x = 0, x1 = 1, a1 = md(a, m);
  while (a1) { i128 q = g / a1, t = g - q * a1; g = a1; a1 = t; t = x - q * x1; x = x1; x1 = t; }
  if (g != 1) return -1;
  return md(x, m);
}
static i128 F; static int k; static u64 pairs = 0, hits = 0, divtests = 0;
static i128 U;
static void pair(i128 a, i128 d) {
  pairs++;
  i128 s = 4 * a * d, t = 4 * a * a * d + 1;
  i128 cand[2]; int nc = 0;
  i128 r = md(-F, s); if (r > 0 && t % r == 0) cand[nc++] = r;
  i128 iF = inv(md(-F, s), s);
  if (iF >= 0) { i128 g = md(md(t, s) * iF, s); if (g > 0 && t % g == 0 && t / g != r) cand[nc++] = t / g; }
  for (int i = 0; i < nc; i++) {
    i128 f = cand[i]; divtests++;
    if ((f + F) % s) continue;
    i128 c = (f + F) / s;
    if ((F * a + c) % f) continue;
    i128 b = (F * a + c) / f;
    if (b < a || (a + b) % c) continue;
    i128 e = (a + b) / c;
    if (e % 17 == 0) continue;
    if (4 * a * b * c * d != F * (a + b) + c) { fprintf(stderr, "equation fail\n"); exit(3); }
    int in1 = md(-4 * a % F * a % F * d - U, F) == 0, in2 = md(-4 * b % F * b % F * d - U, F) == 0;
    printf("HIT k=%d a=%lld b=%lld c=%lld d=%lld e=%lld in1=%d in2=%d\n", k, (long long)a, (long long)b,
           (long long)c, (long long)d, (long long)e, in1, in2);
    if (!(in1 || in2)) { fprintf(stderr, "box mismatch\n"); exit(4); }
    hits++;
  }
}
static int sqrtmod(i128 y, i128 *x1) { /* root of x^2 = y mod 17^k by Hensel; returns 0 if none */
  i128 x = -1; for (int z = 1; z < 17; z++) if ((z * z - y) % 17 == 0 && md(z * z - y, 17) == 0) { x = z; break; }
  if (x < 0) return 0;
  i128 m = 17;
  for (int j = 1; j < k; j++) { m *= 17; x = md(x - md(x * x - y, m) * inv(2 * x, m), m); }
  if (md(x * x - y, F) != 0) { fprintf(stderr, "hensel fail\n"); exit(5); }
  *x1 = x; return 1;
}
int main(int argc, char **argv) {
  k = atoi(argv[1]); F = 1; for (int i = 0; i < k; i++) F *= 17;
  i128 s0 = atoll(argv[2]), t0 = atoll(argv[3]);
  U = md(s0 * inv(t0, F), F);
  i128 ws[2] = { md(-U, F), md(-inv(U, F), F) };
  i128 H = (F + 1) / 2, A0 = 0; while ((A0 + 1) * (A0 + 1) <= H) A0++;
  for (int wi = 0; wi < 2; wi++) {
    i128 w = ws[wi];
    for (i128 a = 1; a <= A0; a++) {
      if (a % 17 == 0) continue;
      i128 d = md(w * inv(4 * a % F * a % F, F), F);
      if (d > 0 && a * d <= H) pair(a, d);
    }
    for (i128 d = 1; d <= A0; d++) {
      if (d % 17 == 0) continue;
      i128 x; if (!sqrtmod(md(w * inv(4 * d, F), F), &x)) continue;
      i128 roots[2] = { x, F - x };
      for (int i = 0; i < 2; i++) if (roots[i] > A0 && roots[i] * d <= H) pair(roots[i], d);
    }
  }
  printf("k=%d pairs=%llu divtests=%llu hits=%llu\n", k, pairs, divtests, hits);
  return 0;
}
