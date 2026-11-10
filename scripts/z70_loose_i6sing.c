// z70 LOOSE I6: numerical illustration of Lemma K: G(r+iy)/G(iy) -> mu(c)/c^2 [c odd], 0 [c even], r = a0/c.
// R(n) = #{(a,b,d) >= 1 : 4abd - a - b = n} for n <= N, then G(r+iy) = sum_n R(n) e(n r) e^{-2 pi n y}.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
int main(int argc, char **argv){
  long N = atol(argv[1]); unsigned *R = calloc(N + 1, sizeof(unsigned));
  for (long d = 1; 4 * d - 2 <= N; d++) for (long a = 1; 4 * a * d - a - 1 <= N; a++){
    long m = 4 * a * d - 1; for (long b = 1; m * b - a <= N; b++) R[m * b - a]++; }
  double ys[] = {1e-3, 1e-4, 3e-5};
  int rs[][2] = {{0,1},{1,3},{1,5},{1,7},{1,15},{2,15},{1,2},{1,4},{1,9},{4,9},{1,25},{1,45}};
  for (int iy = 0; iy < 3; iy++){ double y = ys[iy]; if (2 * M_PI * y * N < 40) { printf("y=%g: N too small\n", y); continue; }
    double complex G0 = 0; for (long n = 1; n <= N; n++) G0 += R[n] * exp(-2 * M_PI * n * y);
    printf("y=%g  G(iy)=%.6g  log^2(1/y)/(16 pi y)=%.6g\n", y, creal(G0), log(1/y)*log(1/y)/(16*M_PI*y));
    for (int k = 0; k < 12; k++){ int a0 = rs[k][0], c = rs[k][1]; double complex G = 0;
      for (long n = 1; n <= N; n++) G += R[n] * cexp(2 * M_PI * I * (double)((n * a0) % c) / c - 2 * M_PI * n * y);
      printf("   r=%d/%d  G(r+iy)/G(iy) = %+.5f %+.5fi\n", a0, c, creal(G / G0), cimag(G / G0)); }
  }
  return 0;
}
