// z70 LOOSE I6: the single fibre g_1(z) = sum_{a,b>=1} e((4ab-a-b)z) = sum_n r_1(4n+1) e(nz) near rationals r = a0/c.
// Prints g_1(r+iy)/g_1(iy) for three y; a two-term fit (A log(1/y) + B)/y is done in z70_loose_i6fit.py-style below.
// Prediction (Z70_LOOSE §2.3 contrast): A(r)/A(0) = c^{-1} e(-a0 * inv(4d)/c) if gcd(c,4d)=1, else 0 (here d = 1).
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
int main(int argc, char **argv){
  long N = atol(argv[1]); unsigned *r = calloc(N + 1, sizeof(unsigned));
  for (long a = 1; 4 * a - 2 <= N; a++){ long m = 4 * a - 1; for (long b = 1; m * b - a <= N; b++) r[m * b - a]++; }
  double ys[] = {1e-3, 1e-4, 3e-5};
  int rs[][2] = {{0,1},{1,3},{2,3},{1,5},{2,5},{1,7},{1,2},{1,4},{1,9}};
  for (int iy = 0; iy < 3; iy++){ double y = ys[iy];
    double complex G0 = 0; for (long n = 1; n <= N; n++) G0 += r[n] * exp(-2 * M_PI * n * y);
    printf("y=%g G(iy)=%.10g\n", y, creal(G0));
    for (int k = 0; k < 9; k++){ int a0 = rs[k][0], c = rs[k][1]; double complex G = 0;
      for (long n = 1; n <= N; n++) G += r[n] * cexp(2 * M_PI * I * (double)((n * a0) % c) / c - 2 * M_PI * n * y);
      printf("   r=%d/%d G(r+iy)/G(iy) = %+.6f %+.6fi\n", a0, c, creal(G / G0), cimag(G / G0)); }
  }
  return 0;
}
