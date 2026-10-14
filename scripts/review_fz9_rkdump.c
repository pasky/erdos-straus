/* R221 harness: dump fz_tail.c's linearised-Rankin constants (lambda, c) for q = 3^r, S. Does not modify fz_tail.c. */
#define main fz_tail_main
#include "fz_tail.c"
#undef main
int main(int argc, char **argv) { int r = atoi(argv[1]); long S = atol(argv[2]); SMIN = S; init_rankin((int)lround(pow(3.0, r)), S);
  long n0s[NN0] = {S / 2, S, 2 * S, 4 * S};
  for (int k = 0; k < NRK; k++) for (int u = 0; u < NN0; u++) printf("%d %ld %.17g %.17g %.17g\n", k + 1, n0s[u], RKlr[k], RKl[k][u], RKc[k][u]);
  return 0; }
