/* O143 memo 2: total ES count f(p) = #{x<=y<=z : 4/p = 1/x+1/y+1/z} for primes p in [P0,P1],
   with Type split (Type I: exactly one of x,y,z divisible by p; Type II: two).
   Method: x in (p/4, 3p/4], A = 4x-p, B = p*x, delta | B^2, delta <= B, delta = -B (mod A), y=(delta+B)/A >= x.
   Output: p, p mod 840, fI, fII.   usage: bs_cubic_fclass P0 P1  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128;
static int *spf;
int main(int argc, char **argv){
  ll P0 = atoll(argv[1]), P1 = atoll(argv[2]);
  ll M = P1 + 10; spf = calloc(M, sizeof(int));
  for (ll i = 2; i < M; i++) if (!spf[i]) for (ll j = i; j < M; j += i) if (!spf[j]) spf[j] = i;
  static ull divs[1 << 16];
  for (ll p = P0; p <= P1; p++) {
    if (p < 5 || spf[p] != p) continue;
    ll fI = 0, fII = 0;
    for (ll x = p / 4 + 1; x <= (3 * p) / 4 + 1; x++) {
      ll A = 4 * x - p; if (A <= 0) continue;
      ull B = (ull)p * x;
      /* factor B^2 = p^2 * x^2 */
      int nd = 1; divs[0] = 1;
      ll t = x; ll q[20]; int e[20]; int k = 0; int pe = 2;
      while (t > 1) { ll r = spf[t]; int c = 0; while (t % r == 0) { t /= r; c++; }
        if (r == p) pe += 2 * c; else { q[k] = r; e[k] = 2 * c; k++; } }
      q[k] = p; e[k] = pe; k++;
      for (int i = 0; i < k; i++) { int cur = nd; ull pw = 1;
        for (int j = 1; j <= e[i]; j++) { pw *= q[i]; for (int m = 0; m < cur; m++) { ull d = divs[m] * pw; if (d <= B) divs[nd++] = d; } } }
      ull target = (ull)(( (i128)A - (i128)(B % A)) % A);
      for (int m = 0; m < nd; m++) {
        ull d = divs[m]; if (d % A != target) continue;
        ull y = (d + B) / A; if ((ll)y < x) continue;
        ull z = (B * (B / d) + 0); /* (A z - B) = B^2/d */
        z = ((ull)((i128)B * B / d) + B) / A;
        int cnt = (x % p == 0) + (y % p == 0) + (z % p == 0);
        if (cnt == 1) fI++; else if (cnt == 2) fII++;
      }
    }
    printf("%lld %lld %lld %lld\n", p, p % 840, fI, fII);
  }
  return 0;
}
