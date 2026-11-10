// z70 LOOSE item 3: EXACT (untruncated) Type I slice decision at fixed (p, d).
// Lemma (Z70_LOOSE §3): the slice is non-empty iff it has a point with a <= b, and then f <= p + 2 and a <= (p+1)/(2d).
// So: for a = 1..(p+1)/(2d), f = -p mod 4ad, f <= p+2, step 4ad: test f | 4a^2 d + 1.  Input lines: "p d".
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef __uint128_t u128;
int main(int argc, char **argv){
  FILE *F = fopen(argv[1], "r"); u64 p, d;
  while (fscanf(F, "%llu %llu", &p, &d) == 2){
    u64 amax = (p + 1) / (2 * d), found = 0, fa = 0, ff = 0;
    for (u64 a = 1; a <= amax && !found; a++){
      u64 g = 4 * a * d; u128 N = (u128)g * a + 1; u64 f = (g - p % g) % g; if (!f) f = g;
      for (; f <= p + 2; f += g) if (N % f == 0){ found = 1; fa = a; ff = f; break; }
    }
    printf("%llu %llu %s", p, d, found ? "NONEMPTY" : "EMPTY");
    if (found) printf(" a=%llu f=%llu", fa, ff);
    printf(" (amax=%llu)\n", amax); fflush(stdout);
  }
  return 0;
}
