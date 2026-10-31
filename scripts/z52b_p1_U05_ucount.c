/* U(n) = #{(x,y,z): 1<=x<=y<=z, 4/n = 1/x+1/y+1/z}  (unordered, = OEIS A192787).
   Method: for each x in [ceil(n/4), floor(3n/4)], A=4x-n, B=n*x; y,z solve (Ay-B)(Az-B)=B^2,
   so d=Ay-B runs over divisors of B^2 with d≡-B (mod A), y=(B+d)/A >= x, z=(B+B^2/d)/A >= y.
   Usage: echo "n1 n2 ..." | ./ucount   (n <= NMAX). Needs factor sieve up to 3*NMAX/4 and NMAX.
   Memory: spf array of 3e5 ints. ulimit -v 4000000 recommended. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LIM 3300000
static int spf[LIM+1];
static int pf[64], pe[64], np;
static void addfac(int m, int mult) {
  while (m > 1) { int q = spf[m], e = 0; while (m % q == 0) { m /= q; e++; }
    int i; for (i = 0; i < np && pf[i] != q; i++); if (i == np) { pf[np] = q; pe[np] = 0; np++; }
    pe[i] += e * mult; }
}
int main() {
  for (int i = 2; i <= LIM; i++) if (!spf[i]) for (int j = i; j <= LIM; j += i) if (!spf[j]) spf[j] = i;
  long n; int dump = (getenv("UDUMP") != NULL);
  while (scanf("%ld", &n) == 1) {
    long cnt = 0; long nx = 0;
    long xlo = (n + 3) / 4, xhi = (3 * n) / 4;
    for (long x = xlo; x <= xhi; x++) {
      long A = 4 * x - n; if (A <= 0) continue;
      long cnt_before = cnt;
      /* factor B^2 = n^2 x^2 */
      np = 0; addfac((int)n, 2); addfac((int)x, 2);
      /* enumerate divisors d of B^2 */
      static long divs[1 << 22]; long nd = 1; divs[0] = 1;
      for (int i = 0; i < np; i++) {
        long cur = nd;
        for (int e = 1; e <= pe[i]; e++) {
          long pw = 1; for (int k = 0; k < e; k++) pw *= pf[i];
          for (long j = 0; j < cur; j++) divs[nd++] = divs[j] * pw;
        }
      }
      long B = n * x;
      /* B^2 as double-safe: use 128-bit via __int128 for comparisons */
      __int128 B2 = (__int128)B * B;
      for (long t = 0; t < nd; t++) {
        long d = divs[t];
        /* need d ≡ -B (mod A) and y=(B+d)/A >= x */
        if (((d + B) % A) != 0) continue;
        __int128 y = ((__int128)B + d) / A;
        if (y < x) continue;
        __int128 z = ((__int128)B + B2 / d) / A;
        if (z < y) continue;
        if (((__int128)B + B2 / d) % A != 0) continue;
        cnt++;
        if (dump) { /* solution triple (x, y, z) on its own line, prefixed by n */
          printf("S %ld %ld %ld %ld\n", n, x, (long)y, (long)z); }
      }
      if (cnt > cnt_before) nx++;
    }
    printf("%ld %ld %ld\n", n, cnt, nx);
  }
  return 0;
}
