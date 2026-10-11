/* R139 from-scratch pointwise P-engine for 17D Comp 3.4 (independent of m17d_pointP.c).
   Lists every ordered N-point (a,b,c,d) of 4abcd = a+b+Nc, N = 17^(2L-1), with 17∤b, 17∤cd and
   a ≡ r*b (mod W), W = 17^L, where r = -u mod W (box -f ∋ u  <=>  a/b ≡ -u, 17-D Lemma 2.1(i), re-derived).
   Completeness: (4a-1)(4b-1) <= 4N+1 (Lemma 2.2(i), re-derived). Split by min(a,b):
     case 1: b <= a  -> (4b-1)^2 <= 4N+1, loop b <= B0, a in class r*b mod W, b <= a <= amax(b);
     case 2: a <  b  -> loop a <= B0, b in class a/r mod W, a < b <= bmax(a).
   Class representatives are updated additively (x_{n+1} = x_n + r mod W): no modular multiplication.
   Usage: pengine L rat s t   (u = s/t)   |   pengine L res R   (u ≡ R mod W)
   Prints hits and the candidate count. All arithmetic in unsigned __int128 where it could exceed 2^63. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef __int128 i128; typedef unsigned __int128 u128;
static i128 md(i128 x, i128 m) { x %= m; return x < 0 ? x + m : x; }
static i128 inv(i128 a, i128 m) { /* extended Euclid */
  i128 g = m, x = 0, x1 = 1, a1 = md(a, m);
  while (a1) { i128 q = g / a1, t = g - q * a1; g = a1; a1 = t; t = x - q * x1; x = x1; x1 = t; }
  if (g != 1) { fprintf(stderr, "not invertible\n"); exit(2); }
  return md(x, m);
}
static u64 isqrt128(u128 n) { u64 x = 0; for (int b = 63; b >= 0; b--) { u64 y = x | (1ULL << b); if ((u128)y * y <= n) x = y; } return x; }
static u128 N, W; /* W < 2^64 for L <= 10 */ static i128 U; static unsigned long long cand = 0, hits = 0;
static void pr(u128 x) { char buf[64]; int i = 63; buf[i] = 0; do { buf[--i] = '0' + (int)(x % 10); x /= 10; } while (x); fputs(buf + i, stdout); }
static void test(u128 a, u128 b) {
  cand++;
  u128 m = (u128)4 * a * b, e = (m - N % m) % m;
  if (e == 0 || e > (u128)a + b || ((u128)a + b) % e) return;
  u128 c = ((u128)a + b) / e, d = (N + e) / m;
  if (c % 17 == 0 || d % 17 == 0 || b % 17 == 0) return;
  /* exact equation 4abcd = a+b+Nc, checked as m*d = N+e and c*e = a+b (both < 2^128) */
  if (m * d != N + e || c * e != (u128)a + b) { fprintf(stderr, "equation fail\n"); exit(3); }
  /* box: -(4acd-1) ≡ u (mod W), reduce mod W first */
  i128 f = md((i128)md(4 * (i128)(a % W) % W * (i128)(c % W), W) * (i128)(d % W) - 1, W);
  int inbox = md(-f - U, W) == 0;
  fputs("HIT a=", stdout); pr(a); fputs(" b=", stdout); pr(b); fputs(" c=", stdout); pr(c); fputs(" d=", stdout); pr(d);
  fputs(" e=", stdout); pr(e); printf(" inbox=%d\n", inbox);
  if (!inbox) { fprintf(stderr, "class/box mismatch\n"); exit(4); }
  hits++;
}
int main(int argc, char **argv) {
  if (argc < 4) return 1;
  int L = atoi(argv[1]); if (L < 1 || L > 10) { fprintf(stderr, "L must be 1..10\n"); return 1; } W = 1; for (int i = 0; i < L; i++) W *= 17; N = 1; for (int i = 0; i < 2 * L - 1; i++) N *= 17;
  int nx;
  if (!strcmp(argv[2], "rat")) { i128 s = atoll(argv[3]), t = atoll(argv[4]); U = md(s * inv(t, W), W); nx = 5; }
  else { U = md(atoll(argv[3]), W); nx = 4; }
  /* optional: restrict the outer index (b in case 1, a in case 2) to [lo, hi] (sampling) */
  u64 lo = argc > nx + 1 ? strtoull(argv[nx], 0, 10) : 1, hi = argc > nx + 1 ? strtoull(argv[nx + 1], 0, 10) : ~0ULL;
  i128 r = md(-U, W), ri = inv(r, W);
  u64 B0 = (u64)((isqrt128(4 * N + 1) + 1) / 4);
  /* case 1: b <= a */
  u64 hi1 = hi < B0 ? hi : B0;
  i128 x = md(r * (i128)(lo - 1), W);
  for (u64 b = lo; b <= hi1; b++) {
    x += r; if (x >= (i128)W) x -= W;          /* x = r*b mod W */
    if (b % 17 == 0) continue;
    u128 amax = ((4 * N + 1) / (4 * (u128)b - 1) + 1) / 4;
    u128 a = (u128)x; if (a == 0) a = W;
    if (a < b) a += ((b - a + W - 1) / W) * W;
    for (; a <= amax; a += W) test(a, b);
  }
  /* case 2: a < b */
  x = md(ri * (i128)(lo - 1), W);
  for (u64 a = lo; a <= hi1; a++) {
    x += ri; if (x >= (i128)W) x -= W;         /* x = a/r mod W */
    if (a % 17 == 0) continue;                 /* 17∤a since 17∤b and a ≡ r b */
    u128 bmax = ((4 * N + 1) / (4 * (u128)a - 1) + 1) / 4;
    u128 b = (u128)x; if (b == 0) b = W;
    if (b <= a) b += ((a + 1 - b + W - 1) / W) * W;
    for (; b <= bmax; b += W) test(a, b);
  }
  printf("L=%d outer=[%llu,%llu] B0=%llu candidates=%llu hits=%llu\n", L, lo, hi1, B0, cand, hits);
  return 0;
}
