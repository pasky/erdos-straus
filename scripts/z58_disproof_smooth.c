// z58 DISPROOF §4: for each prime p (stdin), enumerate ALL (★) solutions (u,B,C) (same three loops as
// z58_disproof_eng.c / FAMDESIGN) and, for each y in a list, count the solutions none of whose three moduli
// m1 = 4uB, m2 = 4uC-1, m3 = 4BC-1 is y-smooth (largest prime factor <= y).  By Lemma 2.2 a prime p with p = 1 (8) and
// (l/p) = +1 for all odd l <= y (a "y-square-mimicking" prime) has exactly such solutions only; the share
// surv_y(p) := #{no y-smooth modulus}/R(p) over generic p is the "surviving mass" prediction for the design depression.
// Output: p R surv_y1 surv_y2 ...   Build: gcc -O2 -o /tmp/z58smooth scripts/z58_disproof_smooth.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll; typedef __int128 i128;
static inline int divides(ll m, ll n) { ll q = (ll)((double)n / (double)m + 0.5); return q * m == n; }
static int YS[] = {3, 7, 13, 31, 61, 97, 199, 499}; enum { NY = 8 };
static int primes[200]; static int np = 0;
// largest prime factor <= y?  returns the smallest y-index k such that m is YS[k]-smooth, or NY if none
static int smooth_idx(ll m) {
  while (!(m & 1)) m >>= 1;
  int lp = 1;
  for (int i = 0; i < np && m > 1; i++) { int q = primes[i]; if ((ll)q * q > m) break; if (m % q == 0) { lp = q; while (m % q == 0) m /= q; } }
  if (m > 1) { if (m > 499) return NY; if (m > lp) lp = (int)m; }
  for (int k = 0; k < NY; k++) if (lp <= YS[k]) return k;
  return NY;
}
static long R, surv[NY];
static void rec(ll u, ll B, ll C) {
  ll m1 = 4 * u * B, m2 = 4 * u * C - 1, m3 = 4 * B * C - 1;
  int k = smooth_idx(m1), k2 = smooth_idx(m2), k3 = smooth_idx(m3); if (k2 < k) k = k2; if (k3 < k) k = k3;
  R += 2; for (int j = 0; j < NY; j++) if (j < k) surv[j] += 2;   // survives at y_j iff no modulus is y_j-smooth (k > j)
}
int main(void) {
  for (int q = 3; q < 500; q += 2) { int pr = 1; for (int t = 3; t * t <= q; t += 2) if (q % t == 0) pr = 0; if (pr) primes[np++] = q; }
  printf("# p R"); for (int k = 0; k < NY; k++) printf(" surv_%d", YS[k]); printf("\n");
  ll n;
  while (scanf("%lld", &n) == 1) {
    R = 0; for (int k = 0; k < NY; k++) surv[k] = 0;
    // (P,Q,C) with P = min(u,B) < Q = max(u,B); moduli symmetric in u,B so P,Q order irrelevant
    for (ll P = 1; 4 * P * P * P - 2 * P <= n; P++)
      for (ll Q = P; ; Q++) { i128 lhs = (i128)4 * P * Q * Q - P - Q; if (lhs > n) break; ll m = 4 * P * Q, N = n + P + Q;
        if (divides(m, N)) { ll C = N / m; if (C >= Q) rec(P, Q, C); } }
    for (ll P = 1; 4 * P * P * P - P <= n + P; P++)
      for (ll C = P; ; C++) { ll m = 4 * P * C - 1; if ((i128)C * m >= n + P) break; ll N = n + P;
        if (divides(m, N)) { ll Q = N / m; if (Q > C) rec(P, Q, C); } }
    for (ll C = 1; ; C++) { ll P0 = C + 1; if ((i128)P0 * (4 * P0 * C - 1) > n + P0) break;
      for (ll P = P0; ; P++) { ll m = 4 * P * C - 1; if ((i128)P * m > n + P) break; ll N = n + P;
        if (divides(m, N)) { ll Q = N / m; if (Q >= P) rec(P, Q, C); } } }
    printf("%lld %ld", n, R); for (int k = 0; k < NY; k++) printf(" %ld", surv[k]); printf("\n"); fflush(stdout);
  }
  return 0;
}
