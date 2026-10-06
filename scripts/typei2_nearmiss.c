/* O69 (POINTWISE_TYPEI2.md §5): near-miss statistics at the sign points x = (w; -1 at r; 1 elsewhere).
   A near miss is (c,k,F) with v_r(c) odd, F | 1+4ck^2, F = -1 (mod odd r-free part of ck), F = 1 (mod r^v)
   -- every condition of a certificate except the 2-adic one.  It is a certificate at x exactly when
   w = -F (mod 2^t), t = v_2(4ck).  For each dyadic height bin we print the number of near misses with
   -F = 9 (mod 16), t >= 4, and the sum of 2^(4-t) over them (= expected number of certificates in the bin
   at a Haar-random w in 9+16Z_2, i.e. the measure the bin removes, counted with multiplicity).
   Usage: typei2_nearmiss r X */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
typedef __int128 i128;
typedef unsigned __int128 u128;

static ll inv(ll a, ll m) {
  ll g = m, x = 0, x1 = 1, b = ((a % m) + m) % m;
  while (b) { ll q = g / b, t = g - q * b; g = b; b = t; t = x - q * x1; x = x1; x1 = t; }
  x %= m; if (x < 0) x += m; return x;
}
static u128 isqrt128(u128 n) {
  u128 x = (u128)sqrtl((long double)n);
  while (x * x > n) x--;
  while ((x + 1) * (x + 1) <= n) x++;
  return x;
}

int main(int argc, char **argv) {
  ll r = atoll(argv[1]), X = atoll(argv[2]);
  double sum[64] = {0}; ll cnt[64] = {0}, all[64] = {0};
  for (ll c = r; c <= X; c += r) {
    ll cc = c; int a = 0; while (cc % r == 0) { cc /= r; a++; }
    if (a % 2 == 0) continue;
    for (ll k = 1; k <= X / c; k++) {
      ll P = c * k, h = 4 * P;
      ll o = h; int t = 0; while (o % 2 == 0) { o /= 2; t++; }
      ll rv = 1, o2 = o; while (o2 % r == 0) { o2 /= r; rv *= r; }
      /* xi_o = -1 mod o2, +1 mod rv, modulus o = o2*rv */
      ll xo;
      if (o2 == 1) xo = 1 % o;
      else { ll tt = (ll)(((i128)((o2 - 1 - 1 % o2 + o2) % o2)) * inv(rv % o2, o2) % o2); xo = (ll)((1 + (i128)rv * tt) % o); }
      /* check: xo = 1 mod rv, xo = -1 mod o2 */
      u128 N = (u128)1 + (u128)4 * c * (u128)k * k;
      u128 s = isqrt128(N);
      int bin = 0; { ll q = P; while (q > 1) { q >>= 1; bin++; } }
      for (u128 D = xo; D <= s; D += o) {
        if (D == 0) continue;
        if (N % D) continue;
        u128 Fs[2] = {D, N / D};
        for (int i = 0; i < (Fs[0] == Fs[1] ? 1 : 2); i++) {
          u128 F = Fs[i];
          all[bin]++;
          if (t < 4) continue;
          ll m2 = 1LL << t;
          ll r2 = (ll)((m2 - (ll)(F % (u128)m2)) % m2);
          if (r2 % 16 == 9) { cnt[bin]++; sum[bin] += ldexp(1.0, 4 - t); }
        }
      }
    }
  }
  double tot = 0;
  for (int b = 0; b < 64; b++) if (all[b]) {
    tot += sum[b];
    printf("ck in [2^%d,2^%d): nearmiss %lld, in 9+16Z_2: %lld, sum 2^(4-t) = %.5f, cumulative %.5f\n",
           b, b + 1, all[b], cnt[b], sum[b], tot);
  }
  return 0;
}
