/* C-form census: for prime p (stdin), C=1..CMAX (argv[1]):
   N=4Cp+1; R(p)=sum_C #{d | N : d ≡ -1 mod 4C} (all divisors); win(C) iff that count>0.
   Output per prime:  p  R  nwin  C_1 C_2 ... (winning C, ascending).
   Trial division by primes up to sqrt(N). Usage: echo primes | ./cform 200 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int sp[400000]; static int nsp = 0;
int main(int argc, char **argv) {
  int CMAX = atoi(argv[1]);
  long p;
  /* primes up to sqrt(4*CMAX*pmax+1); pmax supplied by scanning input would need two passes; use 1e7 bound */
  long SQ = 1 + (long)sqrt(4.0 * CMAX * 1e7 + 1.0);
  char *isc = calloc(SQ + 1, 1);
  for (long i = 2; i <= SQ; i++) if (!isc[i]) { sp[nsp++] = (int)i; for (long j = i * i; j <= SQ; j += i) isc[j] = 1; }
  while (scanf("%ld", &p) == 1) {
    long R = 0; int nwin = 0; long *wins = malloc(sizeof(long) * (CMAX + 1)); int nw = 0;
    for (int C = 1; C <= CMAX; C++) {
      long m = 4L * C, N = m * p + 1, M = N; int ps[64], es[64], k = 0;
      for (int i = 0; i < nsp && (long)sp[i] * sp[i] <= M; i++) {
        if (M % sp[i] == 0) { int e = 0; while (M % sp[i] == 0) { M /= sp[i]; e++; } ps[k] = sp[i]; es[k] = e; k++; }
      }
      if (M > 1) { ps[k] = (int)M; es[k] = 1; k++; }
      /* enumerate divisors d and test d mod m == m-1 */
      long nd = 1; long *dv = malloc(sizeof(long) * 1); dv[0] = 1;
      long cap = 1; 
      for (int i = 0; i < k; i++) {
        long newcap = nd * (es[i] + 1);
        long *nv = malloc(sizeof(long) * newcap); long t = 0;
        for (long j = 0; j < nd; j++) { long v = dv[j]; for (int e = 0; e <= es[i]; e++) { nv[t++] = v; v *= ps[i]; } }
        free(dv); dv = nv; nd = newcap; (void)cap;
      }
      long cnt = 0;
      for (long j = 0; j < nd; j++) if (dv[j] % m == m - 1) cnt++;
      free(dv);
      R += cnt;
      if (cnt > 0) { nwin++; wins[nw++] = C; }
    }
    printf("%ld %ld %d", p, R, nwin);
    for (int i = 0; i < nw; i++) printf(" %ld", wins[i]);
    printf("\n"); fflush(stdout);
    free(wins);
  }
  return 0;
}
