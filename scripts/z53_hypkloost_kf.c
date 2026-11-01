// z53 HYPKLOOST falsifier F3: Kloosterman-fraction sums of the one-sided relation at fixed p.
// For the block (U,2U] x (V,2V] and prime p:
//   K(b) = sum_{u,B coprime} e(b p ubar / B),   ubar = u^{-1} mod B,  b = 1..bmax
// (the bilinear Kloosterman-fraction sum of DFI type that detects B | p+u), together with
//   N1  = #{(u,B): B | p+u},  N1' = #{(u,B): u | p+B},  N = #{(u,B): 4uB | p+u+B},
//   main1 = sum 1/B over all pairs (zero frequency of 1[B | p+u]),  ncop = #coprime pairs.
// Usage: ./kf U V bmax < primes ; output: p N N1 N1' main1 ncop |K(1)| ... |K(bmax)|
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
typedef unsigned long long u64;
static ll inv(ll a, ll m) {  // a^{-1} mod m, gcd(a,m)=1, m>=1
  ll g = m, x = 0, x1 = 1, a1 = a % m; if (m == 1) return 0;
  ll b = a1;
  while (b) { ll qq = g / b, t = g - qq * b; g = b; b = t; t = x - qq * x1; x = x1; x1 = t; }
  x %= m; if (x < 0) x += m; return x;
}
static ll gcdll(ll a, ll b) { while (b) { ll t = a % b; a = b; b = t; } return a; }
int main(int argc, char **argv) {
  ll U = atoll(argv[1]), V = atoll(argv[2]); int bmax = atoi(argv[3]);
  size_t cap = 1024, cnt = 0; u64 *ps = malloc(cap * 8); unsigned long long t;
  while (scanf("%llu", &t) == 1) { if (cnt == cap) { cap *= 2; ps = realloc(ps, cap * 8); } ps[cnt++] = t; }
  double *res = malloc(sizeof(double) * cnt * (bmax + 6));
#pragma omp parallel for schedule(dynamic, 1)
  for (size_t i = 0; i < cnt; i++) {
    u64 p = ps[i];
    double *re = calloc(bmax + 1, sizeof(double)), *im = calloc(bmax + 1, sizeof(double));
    ll N = 0, N1 = 0, N1b = 0, ncop = 0; double main1 = 0;
    for (ll u = U + 1; u <= 2 * U; u++)
      for (ll B = V + 1; B <= 2 * V; B++) {
        main1 += 1.0 / B;
        if ((p + u) % B == 0) N1++;
        if ((p + B) % u == 0) N1b++;
        if ((p + u + B) % (4 * u * B) == 0) N++;
        if (gcdll(u, B) != 1) continue;
        ncop++;
        ll ub = inv(u, B);
        ll pm = (ll)(p % (u64)B);
        ll r = (ll)(((__int128)pm * ub) % B);  // p*ubar mod B
        for (int b = 1; b <= bmax; b++) {
          ll x = (ll)(((__int128)b * r) % B);
          double ang = 2 * M_PI * (double)x / (double)B;
          re[b] += cos(ang); im[b] += sin(ang);
        }
      }
    double *o = res + i * (bmax + 6);
    o[0] = N; o[1] = N1; o[2] = N1b; o[3] = main1; o[4] = ncop;
    for (int b = 1; b <= bmax; b++) o[4 + b] = sqrt(re[b] * re[b] + im[b] * im[b]);
    free(re); free(im);
  }
  for (size_t i = 0; i < cnt; i++) {
    double *o = res + i * (bmax + 6);
    printf("%llu\t%.0f\t%.0f\t%.0f\t%.4f\t%.0f", ps[i], o[0], o[1], o[2], o[3], o[4]);
    for (int b = 1; b <= bmax; b++) printf("\t%.3f", o[4 + b]);
    printf("\n");
  }
  return 0;
}
