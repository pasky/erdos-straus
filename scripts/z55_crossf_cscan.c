// z55 CROSSF: factorisation-free scan of hits(p) = R_F(p)/2 via the C-form  p = 8uwC - u - 2w  (Z55_CROSSF.md Lemma 1.1):
//   hits(p) = #{(u,C): u sqfree, u = 1 (4), U0 < u <= U1, (8uC - 2) | (p + u), w := (p+u)/(8uC-2) in (Y,X] odd sqfree}.
// Cost ~ sum_u p/(8uY) = O(p^{1/3} log p) per prime (standard window), so usable to p ~ 1e18.
// Mode 1: all primes p = 1 (4) in [A, B]:            z55cscan A B
// Mode 2: first K primes p = 1 (4) at/after A, step S: z55cscan A K S   (S > 0 means: scan A, A+S, A+2S,... taking the next prime = 1 (4))
// Output: "p hits" per line to stdout; summary to stderr.  Build: gcc -O2 -o /tmp/z55cscan scripts/z55_crossf_cscan.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128;

static int *primes, nprimes;
static void sieve(int lim) {
  char *c = calloc(lim + 1, 1); primes = malloc(sizeof(int) * (lim / 2 + 10)); nprimes = 0;
  for (int i = 2; i <= lim; i++) { if (!c[i]) { primes[nprimes++] = i; for (ll j = (ll)i * i; j <= lim; j += i) c[j] = 1; } }
  free(c);
}
static ull mulmod(ull a, ull b, ull m) { return (ull)((i128)a * b % m); }
static ull powmod(ull a, ull e, ull m) { ull r = 1; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int isprime(ull n) { // deterministic Miller-Rabin for n < 3.3e24 (bases up to 41)
  if (n < 2) return 0; static const ull bs[] = {2,3,5,7,11,13,17,19,23,29,31,37,41};
  for (int i = 0; i < 13; i++) { if (n % bs[i] == 0) return n == bs[i]; }
  ull d = n - 1; int s = 0; while ((d & 1) == 0) { d >>= 1; s++; }
  for (int i = 0; i < 13; i++) { ull x = powmod(bs[i], d, n); if (x == 1 || x == n - 1) continue; int ok = 0;
    for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } } if (!ok) return 0; }
  return 1;
}
static int sqfree(ll n) { // trial division; n <= ~1e12 here (w <= X <= p^{2/3}/4)
  for (int i = 0; i < nprimes; i++) { ll q = primes[i]; if (q * q > n) break; if (n % q == 0) { n /= q; if (n % q == 0) return 0; } }
  return 1;
}
static ll gcdl(ll a, ll b) { while (b) { ll c = a % b; a = b; b = c; } return a; }

static int hits(ll p, ll *pU0, ll *pU1, ll *pY, ll *pX) {
  ll U0; { double t = pow((double)p, 1.0 / 12) - 0.5; U0 = (ll)floor(t + 0.5); }
  ll U1 = (ll)(pow((double)p, 1.0 / 3) / 2), Y = (ll)pow((double)p, 1.0 / 3), X = (ll)(pow((double)p, 2.0 / 3) / 4);
  while ((i128)8 * U1 * X > p) X--;
  if (U0 < 1) U0 = 1;
  *pU0 = U0; *pU1 = U1; *pY = Y; *pX = X;
  int h = 0;
  for (ll u = U0 + 1; u <= U1; u++) {
    if (u % 4 != 1 || !sqfree(u) || p % u == 0) continue;
    ll n = p + u; // need m = 8uC - 2 | n with Y < n/m <= X  =>  n/X <= m < n/Y
    ll mlo = n / X, mhi = n / Y;  // m in [mlo, mhi]
    ll Clo = (mlo + 2 + 8 * u - 1) / (8 * u); if (Clo < 1) Clo = 1;
    ll Chi = (mhi + 2) / (8 * u);
    for (ll C = Clo; C <= Chi; C++) {
      ll m = 8 * u * C - 2;
      if (n % m) continue;
      ll w = n / m;
      if (w <= Y || w > X || (w & 1) == 0) continue;
      if (gcdl(w, u) != 1 || !sqfree(w)) continue;
      h++;
    }
  }
  return h;
}

int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "usage: A B | A K S\n"); return 1; }
  ll A = atoll(argv[1]), B = atoll(argv[2]); ll S = argc > 3 ? atoll(argv[3]) : 0;
  sieve(2000000);
  long N = 0, zeros = 0; long hist[64] = {0}; double sh = 0;
  if (S == 0) {
    for (ll p = A | 1; p <= B; p += 2) {
      if (p % 4 != 1 || !isprime(p)) continue;
      ll U0, U1, Y, X; int h = hits(p, &U0, &U1, &Y, &X);
      printf("%lld %d\n", p, h); N++; sh += h; if (h == 0) zeros++; if (h < 64) hist[h]++;
    }
  } else {
    ll K = B;
    for (ll k = 0; k < K; k++) {
      ll p = (A + k * S) | 1; while (p % 4 != 1 || !isprime(p)) p += 2;
      ll U0, U1, Y, X; int h = hits(p, &U0, &U1, &Y, &X);
      printf("%lld %d\n", p, h); fflush(stdout); N++; sh += h; if (h == 0) zeros++; if (h < 64) hist[h]++;
    }
  }
  fprintf(stderr, "# A=%lld N=%ld zeros=%ld meanhits=%.4f", A, N, zeros, sh / N);
  for (int i = 0; i < 16; i++) fprintf(stderr, " h%d=%ld", i, hist[i]);
  fprintf(stderr, "\n");
  return 0;
}
