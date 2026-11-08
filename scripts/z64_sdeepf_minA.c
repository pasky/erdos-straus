// For each n <= N (n = 1 mod 4, nonsquare, with a word) compute minA(n) = smallest denominator A of a GOOD word
// (criterion 8 | (n+t)(n+u+v)).  Report per residue class r mod 840 the max of minA over n = r (840), n in [N/2, N]
// and over all n <= N, to detect classes that are not finitely covered.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
int main(int argc, char **argv) {
  long N = atol(argv[1]);
  uint32_t *minA = malloc((N + 1) * sizeof(uint32_t)); unsigned char *any = calloc(N + 1, 1);
  for (long i = 0; i <= N; i++) minA[i] = UINT32_MAX;
  for (long t = 2; 4 * t - 4 <= N; t++)
    for (long u = 2;; u++) {
      long A = t * u - 1; if (2 * A - u > N) break;
      long vmax = (N + u) / A;
      for (long v = 2; v <= vmax; v++) {
        long n = v * A - u; if ((n & 3) != 1) continue;
        any[n] = 1;
        if ((((n + t) * (n + u + v)) & 7) == 0) { long a = A < t * v - 1 ? A : A; if ((uint32_t)a < minA[n]) minA[n] = a; }
      }
    }
  long mx_all[840], mx_hi[840], cnt[840]; long arg_all[840];
  for (int r = 0; r < 840; r++) { mx_all[r] = mx_hi[r] = cnt[r] = 0; arg_all[r] = 0; }
  for (long n = 1; n <= N; n += 4) {
    long s = (long)llround(sqrt((double)n)); if (s * s == n || !any[n]) continue;
    int r = n % 840; cnt[r]++;
    long a = minA[n];
    if (a > mx_all[r]) { mx_all[r] = a; arg_all[r] = n; }
    if (n >= N / 2 && a > mx_hi[r]) mx_hi[r] = a;
  }
  printf("# r mod 840 | count | max minA (n<=N) | argmax n | max minA (n in [N/2,N]) | r mod 8, r mod 3, r mod 5, r mod 7\n");
  for (int r = 1; r < 840; r += 4) {
    if (!cnt[r]) continue;
    printf("%3d %7ld %7ld %9ld %7ld   %d %d %d %d\n", r, cnt[r], mx_all[r], arg_all[r], mx_hi[r], r % 8, r % 3, r % 5, r % 7);
  }
  return 0;
}
