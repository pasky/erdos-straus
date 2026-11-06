// z60 MS105: primitive vs inherited solutions.  For all n <= N: R(n) = #solutions, Rp(n) = #solutions with gcd(u,B) = 1.
// By Lemma 2, solutions with g = gcd(u,B) > 1 are exactly those inherited from n/g (solutions of R(n/g) with g | C).
// Prints a summary over n = 1 (4), gcd(n,105) = 1, non-square, split prime / composite:
//   count, #(R = 0), #(Rp = 0 < R) [rescued only by inheritance], mean R, mean (R - Rp).
// Usage: z60_ms105_prim N
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static long gcd(long a, long b) { while (b) { long t = a % b; a = b; b = t; } return a; }
int main(int argc, char **argv) {
  long N = atol(argv[1]);
  int *R = calloc(N + 1, sizeof(int)), *Rp = calloc(N + 1, sizeof(int));
  char *comp = calloc(N + 1, 1);
  for (long i = 2; i * i <= N; i++) if (!comp[i]) for (long j = i * i; j <= N; j += i) comp[j] = 1;
  for (long u = 1; 3 * u - 1 <= N; u++)   // B = C = 1 gives n = 3u - 1
    for (long B = 1; 4 * u * B - u - B <= N; B++) {
      int prim = gcd(u, B) == 1;
      for (long n = 4 * u * B - u - B; n <= N; n += 4 * u * B) { R[n]++; if (prim) Rp[n]++; }
    }
  long cnt[2] = {0}, z[2] = {0}, inh[2] = {0}; double sR[2] = {0}, sI[2] = {0};
  for (long n = 5; n <= N; n += 4) {
    if (n % 3 == 0 || n % 5 == 0 || n % 7 == 0) continue;
    long r = (long)sqrt((double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++;
    if (r * r == n) continue;
    int c = comp[n] ? 1 : 0;
    cnt[c]++; sR[c] += R[n]; sI[c] += R[n] - Rp[n];
    if (R[n] == 0) z[c]++;
    else if (Rp[n] == 0) { inh[c]++; printf("INHERIT_ONLY %ld R=%d\n", n, R[n]); }
  }
  for (int c = 0; c < 2; c++)
    printf("%s count %ld zeros %ld inherit_only %ld meanR %.3f mean_imprimitive %.4f\n", c ? "composite" : "prime",
           cnt[c], z[c], inh[c], sR[c] / cnt[c], sI[c] / cnt[c]);
  return 0;
}
