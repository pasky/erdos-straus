/* Z0077 part 3: cubic polynomials X^3 - aX^2 + m c X - c (roots x_i > 0 with sum 1/x_i = m), irreducible over Q,
 * D = disc > 0 (totally real).  Count by m mod 8, separately for D a perfect square (cyclic cubic field) and not.
 * Question: is m = Tr(1/z) == 0 (mod 4) ever attained by a totally positive algebraic integer z of a CYCLIC cubic field?
 * usage: poly AMAX MMAX */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef __int128 i128;
static int issq(i128 D) { if (D < 0) return 0; long double r = sqrtl((long double)D); i128 s = (i128)llroundl(r);
  for (i128 t = s - 2; t <= s + 2; t++) if (t >= 0 && t * t == D) return 1; return 0; }
int main(int argc, char **argv) {
  long AMAX = atol(argv[1]); int MMAX = atoi(argv[2]);
  long cyc[64] = {0}, ncyc[64] = {0};
  for (int m = 1; m <= MMAX; m++) {
    for (long a = 1; a <= AMAX; a++) {
      long cmax = (long)((double)a * a * a / 27.0) + 1;
      for (long c = 1; c <= cmax; c++) {
        i128 b = (i128)m * c;
        i128 D = (i128)a*a*b*b - 4*b*b*b - 4*(i128)a*a*a*c + 18*(i128)a*b*c - 27*(i128)c*c;
        if (D <= 0) continue;
        /* rational root must be a positive divisor r of c (monic, all roots positive): f(r) = 0 ? */
        int red = 0;
        for (long r = 1; r * r <= c && !red; r++) if (c % r == 0) {
          long rr[2] = {r, c / r};
          for (int k = 0; k < 2; k++) { i128 x = rr[k]; if (x*x*x - a*x*x + b*x - c == 0) red = 1; } }
        if (red) continue;
        if (issq(D)) { cyc[m]++; if (m % 4 == 0) printf("CYCLIC m=%d a=%ld c=%ld\n", m, a, c); }
        else ncyc[m]++;
      }
    }
    printf("m=%d  cyclic(square disc)=%ld  non-cyclic totally real=%ld\n", m, cyc[m], ncyc[m]); fflush(stdout);
  }
  return 0;
}
