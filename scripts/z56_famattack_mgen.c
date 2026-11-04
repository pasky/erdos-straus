// z56 FAMATTACK: genus main term M_gen(n) for odd n (prime or composite), exact, by enumeration.
//   M_gen(n) = Σ_{(u,B): gcd(u,B)=1, u+B odd, 4uB-u-B <= n, gcd(n,4uB)=1} (s(q)/φ(q)) · 1[n·a is a square unit mod q],
//   q = 4uB, a = -(u+B).  (FRONTIER §2.1 genus split; pairs with gcd(n,q)>1 can never hit and carry no density.)
// Also prints R*(n) = #{such pairs with n ≡ a (mod q)} (= R(n) for primes) for cross-checking.
// Usage: mgen < list_of_n   -> "n Mgen Rstar Mgen/log^2 n"
// Build: gcc -O2 -o mgen z56_famattack_mgen.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int *spf; static ll SPFN;
static void build_spf(ll N) {
  spf = calloc(N + 1, sizeof(int)); SPFN = N;
  for (ll i = 2; i <= N; i++) if (!spf[i]) for (ll j = i; j <= N; j += i) if (!spf[j]) spf[j] = (int)i;
}
static ll pw(ll b, ll e, ll m) { ll r = 1; b %= m; if (b < 0) b += m; while (e) { if (e & 1) r = (__int128)r * b % m; b = (__int128)b * b % m; e >>= 1; } return r; }
static ll gcdl(ll a, ll b) { while (b) { ll t = a % b; a = b; b = t; } return a < 0 ? -a : a; }
// returns 1 if x (unit mod odd prime l) is a QR
static int qr(ll x, ll l) { x %= l; if (x < 0) x += l; return pw(x, (l - 1) / 2, l) == 1; }
// accumulate over odd prime factors of v: product of (2/φ(ℓ^k)) weights and QR test of x
static int oddpart(ll v, ll x, double *w) {
  while (v > 1) {
    ll l = spf[v]; ll lk = 1; while (v % l == 0) { v /= l; lk *= l; }
    if (l == 2) continue;
    if (!qr(x, l)) return 0;
    *w *= 2.0 / (double)(lk - lk / l);
  }
  return 1;
}
int main(void) {
  ll n;
  ll *ns = malloc(sizeof(ll) * 100000); int cnt = 0; ll maxn = 0;
  while (scanf("%lld", &n) == 1) { ns[cnt++] = n; if (n > maxn) maxn = n; }
  build_spf(maxn / 4 + 10);
  for (int t = 0; t < cnt; t++) {
    n = ns[t];
    double M = 0; ll Rs = 0;
    for (ll u = 1; 4 * u * 1 - u - 1 <= n; u++) {
      for (ll B = 1; 4 * u * B - u - B <= n; B++) {
        if (((u + B) & 1) == 0) continue;
        if (gcdl(u, B) != 1) continue;
        ll q = 4 * u * B;
        if (gcdl(n, q) != 1) continue;
        ll a = -(u + B);
        if (((n - a) % q) == 0) Rs++;
        // square test of x = n*a mod q: 2-part: q has 2-adic valuation >= 3 (one of u,B even) -> x ≡ 1 mod 8
        ll x8 = ((n % 8) * (((a % 8) + 8) % 8)) % 8;
        if (x8 != 1) continue;
        double w = 4.0 / (double)(q & -q) * 2.0; // s_2/φ(2^e) = 4 / 2^{e-1}
        // odd parts of u and B
        ll x = (ll)((__int128)(n % q) * (((a % q) + q) % q) % q);
        ll ou = u, oB = B; while (!(ou & 1)) ou >>= 1; while (!(oB & 1)) oB >>= 1;
        if (!oddpart(ou, x, &w)) continue;
        if (!oddpart(oB, x, &w)) continue;
        M += w;
      }
    }
    double L = log((double)n);
    printf("%lld %.4f %lld %.5f\n", n, M, Rs, M / (L * L));
    fflush(stdout);
  }
  return 0;
}
