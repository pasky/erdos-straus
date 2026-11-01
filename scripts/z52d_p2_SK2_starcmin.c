/* Pass-2 SK2: EXACT least C with a (star) certificate, no cap.
   (star) triple (u,B,C): 4uBC - u - B = p  <=>  d = 4Cu-1 divides 4Cp+1 with d = -1 mod 4C
   (C-form of the census, same set).  Enumeration: any solution has min(u,B) <= sqrt(p)+2
   (proof: if u<=B then 4uB<=p+2B; if B>=sqrt p this gives u<=sqrt(p)/4+1, else u<=B<sqrt p).
   For each u<=U, let n = p+u; then B*D = n with D = 4uC-1, i.e. D | n, D = -1 (mod 4u), C=(D+1)/(4u).
   Reads primes (p = 1 mod 4) from stdin, prints "p Cmin_exact (0 = none)  and (u,B) of minimiser".
   Memory: O(1) per prime. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
static u64 *sp; static long nsp;
int main(void) {
  long SQ = 200000; /* covers trial division of p+u for p <= 4e10 */
  char *isc = calloc(SQ + 1, 1); sp = malloc(sizeof(u64) * 30000);
  for (long i = 2; i <= SQ; i++) if (!isc[i]) { sp[nsp++] = i; for (long j = i * i; j <= SQ; j += i) isc[j] = 1; }
  u64 p;
  while (scanf("%llu", &p) == 1) {
    u64 best = 0, bu = 0, bB = 0;
    u64 U = (u64)sqrt((double)p) + 2;
    for (u64 u = 1; u <= U; u++) {
      u64 n = p + u;
      /* factor n */
      u64 ps[64]; int es[64]; int k = 0, M = 0; u64 m = n;
      for (long i = 0; i < nsp && (u64)sp[i] * sp[i] <= m; i++)
        if (m % sp[i] == 0) { int e = 0; while (m % sp[i] == 0) { m /= sp[i]; e++; } ps[k] = sp[i]; es[k] = e; k++; }
      if (m > 1) { ps[k] = m; es[k] = 1; k++; }
      (void)M;
      /* enumerate all divisors D of n, test D = -1 mod 4u */
      u64 mod = 4 * u; int ex[64] = {0};
      while (1) {
        u64 D = 1;
        for (int i = 0; i < k; i++) for (int e = 0; e < ex[i]; e++) D *= ps[i];
        if ((D + 1) % mod == 0) {
          u64 C = (D + 1) / mod; u64 B = n / D;
          if (B >= 1 && C >= 1 && (best == 0 || C < best)) { best = C; bu = u; bB = B; }
        }
        int i = 0; while (i < k) { ex[i]++; if (ex[i] <= es[i]) break; ex[i] = 0; i++; }
        if (i == k) break;
      }
    }
    printf("%llu %llu %llu %llu\n", p, best, bu, bB);
  }
  return 0;
}
