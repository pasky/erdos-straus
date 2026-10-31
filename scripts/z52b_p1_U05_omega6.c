/* z52b pass1 U05 Z1596: list C-form failures (no divisor d of N=4Cp+1 with d ≡ -1 mod 4C) with omega(N) >= 6.
   Input primes (stdin), CMAX argv[1]. Output: p C N omega and the prime factors.  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int sp[400000]; static int nsp = 0;
int main(int argc, char **argv) {
  int CMAX = atoi(argv[1]); long p;
  long SQ = 1 + (long)sqrt(4.0 * CMAX * 1e5 + 1.0) + 10;
  char *isc = calloc(SQ + 1, 1);
  for (long i = 2; i <= SQ; i++) if (!isc[i]) { sp[nsp++] = (int)i; for (long j = i * i; j <= SQ; j += i) isc[j] = 1; }
  while (scanf("%ld", &p) == 1) {
    for (int C = 1; C <= CMAX; C++) {
      long m = 4L * C, N = m * p + 1, M = N; long ps[64]; int es[64], k = 0;
      for (int i = 0; i < nsp && (long)sp[i] * sp[i] <= M; i++)
        if (M % sp[i] == 0) { int e = 0; while (M % sp[i] == 0) { M /= sp[i]; e++; } ps[k] = sp[i]; es[k] = e; k++; }
      if (M > 1) { ps[k] = M; es[k] = 1; k++; }
      if (k < 6) continue;
      char *reach = calloc(m, 1); reach[1 % m] = 1;
      for (int i = 0; i < k; i++) {
        char *nr = calloc(m, 1); long qm = ps[i] % m;
        for (long r = 0; r < m; r++) if (reach[r]) { long v = r; for (int e = 0; e <= es[i]; e++) { nr[v] = 1; v = (v * qm) % m; } }
        free(reach); reach = nr;
      }
      int win = reach[m - 1]; free(reach);
      if (!win) {
        printf("%ld %d %ld %d", p, C, N, k);
        for (int i = 0; i < k; i++) printf(" %ld^%d", ps[i], es[i]);
        printf("\n");
      }
    }
  }
  return 0;
}
