/* O69 (POINTWISE_TYPEI2.md §3, Computation 3.2): factorisation-free checker for certificates at the sign
   point  x = (w at 2; -1 at r; 1 at every other prime),  r = 3 (mod 4).
   For every slice (c,k) with ck <= X and v_r(c) odd (exactly the unforced slices, Lemma 2.1) a
   certificate is a divisor F of N = 1+4ck^2 with F = xi (mod 4ck), where
     xi = -1 (mod odd r-free part of ck),  xi = +1 (mod r^{v_r(ck)}),  xi = -w (mod 2^{v_2(4ck)}).
   Since N = 1 (mod 4ck), the cofactor N/F is = xi^{-1}.  Every divisor pair has a member <= sqrt(N), so
   it suffices to test D <= sqrt(N) with D = xi or D = xi^{-1} (mod 4ck): about sqrt(N)/(4ck) < 1 candidates
   per class.  Prints every certificate found (up to a cap) and the number of slices.
   Usage: typei2_signcheck r w X [maxprint]  (w = 1 mod 8; uses __int128) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
typedef __int128 i128;
typedef unsigned __int128 u128;

static ll mulmod(ll a, ll b, ll m) { return (ll)((i128)a * b % m); }
static ll egcd_inv(ll a, ll m) { /* inverse of a mod m, gcd=1 */
  ll g = m, x = 0, x1 = 1, a1 = a % m; if (a1 < 0) a1 += m;
  ll b = a1;
  while (b) { ll q = g / b, t = g - q * b; g = b; b = t; t = x - q * x1; x = x1; x1 = t; }
  if (g != 1) return -1;
  x %= m; if (x < 0) x += m; return x;
}
/* combine x = a1 (m1), x = a2 (m2), coprime */
static void crt(ll *a, ll *m, ll a2, ll m2) {
  ll inv = egcd_inv(*m % m2, m2);
  ll t = mulmod(((a2 - *a) % m2 + m2) % m2, inv, m2);
  *m *= m2; *a = (ll)(((i128)*a + (i128)(*m / m2) * t) % *m);
}
static u128 isqrt128(u128 n) {
  u128 x = (u128)sqrtl((long double)n);
  while (x * x > n) x--;
  while ((x + 1) * (x + 1) <= n) x++;
  return x;
}

int main(int argc, char **argv) {
  ll r = atoll(argv[1]), w = atoll(argv[2]), X = atoll(argv[3]);
  ll maxprint = argc > 4 ? atoll(argv[4]) : 20;
  ll nslices = 0, nfound = 0, ncand = 0;
  for (ll c = r; c <= X; c += r) {
    ll cc = c; int a = 0; while (cc % r == 0) { cc /= r; a++; }
    if (a % 2 == 0) continue;
    for (ll k = 1; k <= X / c; k++) {
      ll P = c * k;
      nslices++;
      ll h = 4 * c * k;
      /* split h = 2^t * r^v * o */
      ll o = h; int t = 0; while (o % 2 == 0) { o /= 2; t++; }
      ll rv = 1; while (o % r == 0) { o /= r; rv *= r; }
      ll m2 = 1LL << t;
      ll xa = ((o - 1) % o + o) % o, xm = o;          /* -1 mod o */
      if (o == 1) xa = 0;
      crt(&xa, &xm, 1 % rv, rv);                       /* +1 mod r^v */
      crt(&xa, &xm, ((-w) % m2 + m2) % m2, m2);        /* -w mod 2^t */
      ll xi = xa;
      ll xinv = egcd_inv(xi, h);
      u128 N = (u128)1 + (u128)4 * (u128)c * (u128)k * (u128)k;
      u128 s = isqrt128(N);
      for (int pass = 0; pass < 2; pass++) {
        ll cls = pass ? xinv : xi;
        for (u128 D = cls; D <= s; D += h) {
          ncand++;
          if (D == 0) continue;
          if (N % D == 0) {
            u128 F = pass ? N / D : D;
            nfound++;
            if (nfound <= maxprint)
              printf("CERT ck=%lld c=%lld k=%lld F=%llu\n", P, c, k, (unsigned long long)F);
          }
        }
      }
    }
  }
  printf("r=%lld w=%lld X=%lld: unforced slices %lld, candidates %lld, certificates %lld\n",
         r, w, X, nslices, ncand, nfound);
  return 0;
}
