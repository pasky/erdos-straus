// z58 DISPROOF §6: local cells for the zero law.  Sieve-enumerate all (★) triples 4uBC - u - B = n <= N (as
// scripts/z57_synth_tri.c) recording R(n) and R8(n) (C even) for odd n; then for every prime p = 1 (4), 1000 <= p <= N,
// aggregate by cell = (p mod 840, Legendre signs (l/p) for l = 11,13,17,19,23 [5 bits], floor(2*log2 p) [half-octave]):
// n, sum R, sum R^2, sum R8, sum R8^2, #(R=0), #(R8=0), #(R<=2), #(R8<=2).
// Output: one line per non-empty cell.  Build: gcc -O2 -o /tmp/z58cells scripts/z58_disproof_cells.c -lm
// Memory: 2 uint16 arrays of N/2 + a char sieve of N/2 (N = 2e8 -> 500 MB).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll;
static int leg(ll a, int l) { ll r = 1, b = a % l, e = (l - 1) / 2; while (e) { if (e & 1) r = r * b % l; b = b * b % l; e >>= 1; } return r == 1; }
int main(int argc, char **argv) {
  ll N = atoll(argv[1]); ll H = N / 2 + 1;
  uint16_t *R = calloc(H, 2), *R8 = calloc(H, 2); char *comp = calloc(H, 1);
  if (!R || !R8 || !comp) { fprintf(stderr, "alloc\n"); return 2; }
  for (ll u = 1; 4 * u - u - 1 <= N; u++)
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 1) == 0) continue;
      ll step = 4 * u * B, n = step - u - B;
      for (ll C = 1; n <= N; C++, n += step) { ll i = (n - 1) / 2; if (R[i] < 65535) R[i]++; if (!(C & 1) && R8[i] < 65535) R8[i]++; }
    }
  for (ll q = 3; q * q <= N; q += 2) if (!comp[(q - 1) / 2]) for (ll j = q * q; j <= N; j += 2 * q) comp[(j - 1) / 2] = 1;
  enum { NB = 64 }; static double s[840][32][NB][9];
  static const int LS[5] = {11, 13, 17, 19, 23};
  for (ll p = 1001; p <= N; p += 4) {
    ll i = (p - 1) / 2; if (comp[i]) continue;
    int bits = 0; for (int k = 0; k < 5; k++) bits |= leg(p, LS[k]) << k;
    int b = (int)floor(2 * log2((double)p)); double r = R[i], r8 = R8[i];
    double *c = s[p % 840][bits][b];
    c[0]++; c[1] += r; c[2] += r * r; c[3] += r8; c[4] += r8 * r8; c[5] += r == 0; c[6] += r8 == 0; c[7] += r <= 2; c[8] += r8 <= 2;
  }
  printf("# N=%lld cells: mod840 bits(11,13,17,19,23) halfoctave n sumR sumR2 sumR8 sumR82 zR zR8 le2R le2R8\n", N);
  for (int a = 0; a < 840; a++) for (int bt = 0; bt < 32; bt++) for (int b = 0; b < NB; b++) { double *c = s[a][bt][b]; if (c[0] == 0) continue;
    printf("%d %d %d %.0f %.0f %.0f %.0f %.0f %.0f %.0f %.0f %.0f\n", a, bt, b, c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8]); }
  return 0;
}
