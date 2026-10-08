/* R93 from-scratch naive enumerator of P-data at level K (independent of ET Lemma 2.8 cover).
 * N-points (a,b,c,d) of Sigma^II_n, n = 17^K: 4abcd = a+b+nc, a<=b, 17∤cd.
 * Divide by c: 4abd = n+e with e=(a+b)/c, 1<=e<=a+b<4ab, so e = (-n mod 4ab) is forced (must be >0),
 * and d>=1 forces 4ab <= n+e <= n+a+b; we scan all a<=b with 4ab <= n+a+b (weaker than 2ab<=n).
 * Usage: review_m17b_brute K NPARTS PART   (a ≡ PART mod NPARTS). Output "a b c d" lines.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char **argv) {
  int K = atoi(argv[1]); uint64_t np = atoll(argv[2]), part = atoll(argv[3]);
  uint64_t n = 1; for (int i = 0; i < K; i++) n *= 17;
  double nd = (double)n;
  long cnt = 0;
  for (uint64_t a = 1 + part; ; a += np) {
    if (4 * a * a > n + 2 * a) break;
    for (uint64_t b = a; 4 * a * b <= n + a + b; b++) {
      uint64_t m = 4 * a * b;
      uint64_t q = (uint64_t)(nd / (double)m);
      /* fix q so that q*m <= n < (q+1)*m */
      while (q * m > n) q--;
      while ((q + 1) * m <= n) q++;
      uint64_t r = n - q * m;
      if (r == 0) continue;
      uint64_t e = m - r;
      if ((a + b) % e) continue;
      uint64_t c = (a + b) / e, d = (n + e) / m;
      if (c % 17 == 0 || d % 17 == 0) continue;
      /* verify in 128-bit */
      unsigned __int128 lhs = (unsigned __int128)4 * a * b * c * d;
      unsigned __int128 rhs = (unsigned __int128)a + b + (unsigned __int128)n * c;
      if (lhs != rhs) { fprintf(stderr, "BUG %lu %lu\n", a, b); return 1; }
      printf("%lu %lu %lu %lu\n", a, b, c, d); cnt++;
    }
  }
  fprintf(stderr, "K=%d part %lu/%lu: %ld\n", K, part, np, cnt);
  return 0;
}
