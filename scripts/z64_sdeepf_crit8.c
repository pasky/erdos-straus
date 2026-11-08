// Direct check of Theorem 1: for every word (t,u,v) of n = tuv-u-v <= N, n = 1 mod 4,
// Jacobi(A/n) == -1  <=>  8 | (n+t)(n+u+v).   Jacobi computed directly (no rule).
// Also: squares never have (A/n) = -1 (automatic) and every nonsquare with a word has a good one (S).
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int jacobi(long a, long n) { // n odd positive
  a %= n; if (a < 0) a += n; int r = 1;
  while (a) {
    while (!(a & 1)) { a >>= 1; long m = n & 7; if (m == 3 || m == 5) r = -r; }
    long tmp = a; a = n; n = tmp;
    if ((a & 3) == 3 && (n & 3) == 3) r = -r;
    a %= n;
  }
  return n == 1 ? r : 0;
}
int main(int argc, char **argv) {
  long N = atol(argv[1]);
  unsigned char *good = calloc(N + 1, 1), *any = calloc(N + 1, 1);
  long words = 0, mism = 0;
  for (long t = 2; 4 * t - 4 <= N; t++)
    for (long u = 2;; u++) {
      long A = t * u - 1; if (2 * A - u > N) break;
      long vmax = (N + u) / A;
      for (long v = 2; v <= vmax; v++) {
        long n = v * A - u; if ((n & 3) != 1) continue;
        int j = jacobi(A, n);
        int pred = (((n + t) * (n + u + v)) & 7) == 0 ? -1 : 1;
        words++;
        if (j != pred) { mism++; if (mism < 10) printf("MISMATCH n=%ld t=%ld u=%ld v=%ld A=%ld jac=%d pred=%d\n", n, t, u, v, A, j, pred); }
        any[n] = 1; if (j == -1) good[n] = 1;
      }
    }
  long sqgood = 0, nonsq_bad = 0, nonsq_words = 0;
  for (long n = 1; n <= N; n += 4) {
    long r = (long)llround(sqrt((double)n)); int sq = (r * r == n);
    if (!any[n]) continue;
    if (sq) sqgood += good[n]; else { nonsq_words++; if (!good[n]) { nonsq_bad++; printf("S FAILS at n=%ld\n", n); } }
  }
  printf("N=%ld words=%ld mismatches=%ld | nonsquares with words=%ld, of which without good word=%ld | squares with good word=%ld\n",
         N, words, mism, nonsq_words, nonsq_bad, sqgood);
  return 0;
}
