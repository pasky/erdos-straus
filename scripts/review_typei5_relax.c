/* R92 from-scratch relaxed brute force (TYPEI4 Cor 3.2 with 7^b replaced by an arbitrary odd u).
   Solutions of: y = c' g delta < T u (y odd), a odd, W = 7^a,
     P1 = c' g^2 + W u (2y - T u) >= 1, P1 | z = T u - y, 7 !| P1, 7 !| c',
     X = (1 + W u z / P1) / (4 c' g) an odd integer, 7 !| X.
   Output: L u a c' g delta P1 X     (classification in review_typei5_classify.py)
   Usage: review_typei5_relax L Umax */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef __int128 i128;
int main(int argc, char **argv) {
  int L = atoi(argv[1]); ll U = atoll(argv[2]); ll T = 1LL << (L - 4); long n = 0;
  for (ll u = 1; u <= U; u += 2)
    for (ll W = 7; W < T * T * u; W *= 49) /* a odd; crude bound W < T^2 u (TYPEI4 L3.1(iv) relaxed) */
      for (ll cp = 1; cp < T * u; cp += 2) { if (cp % 7 == 0) continue;
        for (ll g = 1; cp * g < T * u; g += 2) { ll G = cp * g;
          for (ll dl = 1; G * dl < T * u; dl += 2) {
            ll y = G * dl;
            i128 P1 = (i128)cp * g * g + (i128)W * u * (2 * y - T * u);
            if (P1 < 1) continue;
            ll z = T * u - y;
            if ((i128)z % P1) continue;
            ll p1 = (ll)P1; if (p1 % 7 == 0) continue;
            i128 num = 1 + (i128)W * u * (z / p1);
            if (num % (4 * (i128)G)) continue;
            i128 X = num / (4 * (i128)G);
            if (X % 2 == 0 || X % 7 == 0) continue;
            printf("%d %lld %lld %lld %lld %lld %lld %lld\n", L, u, W, cp, g, dl, p1, (ll)X); n++;
          }
        } }
  fprintf(stderr, "L=%d U=%lld: %ld relaxed solutions\n", L, U, n);
  return 0;
}
