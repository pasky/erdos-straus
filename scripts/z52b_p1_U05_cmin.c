/* Early-exit C-form census: for prime p (stdin) output p and Cmin = least C<=CMAX with a win (0 if none).
   Usage: awk primes | ./cmin CMAX.  Trial division up to sqrt(4*CMAX*pmax+1) with pmax=1.5e7 (sieve bound). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int sp[2000000]; static int nsp = 0;
int main(int argc, char **argv) {
  int CMAX = atoi(argv[1]); long p;
  long SQ = 1 + (long)sqrt(4.0 * CMAX * 1.5e7 + 1.0);
  char *isc = calloc(SQ + 1, 1);
  for (long i = 2; i <= SQ; i++) if (!isc[i]) { sp[nsp++] = (int)i; for (long j = i * i; j <= SQ; j += i) isc[j] = 1; }
  while (scanf("%ld", &p) == 1) {
    long found = 0;
    for (int C = 1; C <= CMAX && !found; C++) {
      long m = 4L * C, M = m * p + 1; long ps[64]; int es[64], k = 0;
      for (int i = 0; i < nsp && (long)sp[i] * sp[i] <= M; i++)
        if (M % sp[i] == 0) { int e = 0; while (M % sp[i] == 0) { M /= sp[i]; e++; } ps[k] = sp[i]; es[k] = e; k++; }
      if (M > 1) { ps[k] = M; es[k] = 1; k++; }
      /* divisor check via DP over residues mod m: reachable set of divisor residues */
      char *reach = calloc(m, 1); reach[1 % m] = 1;  /* residue of product so far (mod m) */
      for (int i = 0; i < k; i++) {
        char *nr = calloc(m, 1);
        long qm = ps[i] % m;
        for (long r = 0; r < m; r++) if (reach[r]) {
          long v = r;
          for (int e = 0; e <= es[i]; e++) { nr[v] = 1; v = (v * qm) % m; }
        }
        free(reach); reach = nr;
      }
      if (reach[m - 1]) found = C;
      free(reach);
    }
    printf("%ld %ld\n", p, found);
  }
  return 0;
}
