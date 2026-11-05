// z59 MSPLUS: exact R(n) for all n = 1 (mod 4), n <= N, with stratified statistics.
// R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n}; for fixed (u,B) the n form the progression n = -(u+B) mod 4uB,
// n >= 4uB - u - B (C >= 1); n = 1 (4) forces u + B = 3 (4).  Counts in uint16 (saturation checked).
// Output (stdout):
//  "A cat a bin count sumR sumR2 zeros le2"   per (cat P/C/S, a = n mod 840, bin = floor(4*log10 n))
//  "K cat g105 k bin count sumR zeros le2"    per (cat, gcd(n,105), k = least odd prime l<=199 with (n/l) = -1, l !| n
//                                              (k = 0 if none), bin)
//  "Z n cat R"  for every n with R(n) <= 2 and n >= ZMIN (cat P prime, C non-square composite, S square)
// Usage: z59_msplus_strat N ZMIN
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef long long ll;
#define NB 64
#define NPR 46
static const int PR[NPR] = {3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,
  127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211};
static signed char QR[NPR][212];  // Legendre symbol table
// aggregated tables
static double A_cnt[3][840][NB], A_s[3][840][NB], A_s2[3][840][NB], A_z[3][840][NB], A_l2[3][840][NB];
static double K_cnt[3][106][213][NB], K_s[3][106][213][NB], K_z[3][106][213][NB], K_l2[3][106][213][NB];
int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "usage: N ZMIN\n"); return 1; }
  ll N = atoll(argv[1]), ZMIN = atoll(argv[2]);
  if (N < 5 || N > 1200000000LL) { fprintf(stderr, "N range\n"); return 1; }
  ll I = (N - 1) / 4;  // index i = (n-1)/4
  uint16_t *R = calloc(I + 1, 2);
  uint8_t *comp = calloc(N / 2 + 1, 1);  // odd composite flag, index n/2
  if (!R || !comp) { fprintf(stderr, "alloc\n"); return 2; }
  for (ll u = 1; 3 * u - 1 <= N; u++)
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 3) != 3) continue;
      ll step = 4 * u * B, n = step - u - B, s = step / 4;
      for (ll i = (n - 1) / 4; i <= I; i += s) { if (R[i] == 65535) { fprintf(stderr, "sat\n"); return 3; } R[i]++; }
    }
  for (ll p = 3; p * p <= N; p += 2)
    if (!comp[p / 2]) for (ll m = p * p; m <= N; m += 2 * p) comp[m / 2] = 1;
  for (int j = 0; j < NPR; j++) {
    int l = PR[j];
    for (int x = 0; x < l; x++) QR[j][x] = -1;
    QR[j][0] = 0;
    for (int x = 1; x < l; x++) QR[j][(ll)x * x % l] = 1;
  }
  for (ll i = 1; i <= I; i++) {
    ll n = 4 * i + 1;
    ll r = (ll)sqrtl((long double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++;
    int cat = (r * r == n) ? 2 : (comp[n / 2] ? 1 : 0);
    int a = n % 840, bin = (int)floor(4 * log10((double)n));
    double Rv = R[i];
    A_cnt[cat][a][bin]++; A_s[cat][a][bin] += Rv; A_s2[cat][a][bin] += Rv * Rv;
    if (Rv == 0) A_z[cat][a][bin]++;
    if (Rv <= 2) A_l2[cat][a][bin]++;
    int g = 1; if (n % 3 == 0) g *= 3; if (n % 5 == 0) g *= 5; if (n % 7 == 0) g *= 7;
    int k = 0;
    for (int j = 0; j < NPR - 1; j++) if (QR[j][n % PR[j]] == -1) { k = PR[j]; break; }
    K_cnt[cat][g][k][bin]++; K_s[cat][g][k][bin] += Rv;
    if (Rv == 0) K_z[cat][g][k][bin]++;
    if (Rv <= 2) K_l2[cat][g][k][bin]++;
    if (Rv <= 2 && n >= ZMIN) printf("Z %lld %c %d\n", n, "PCS"[cat], (int)Rv);
  }
  for (int c = 0; c < 3; c++) for (int a = 0; a < 840; a++) for (int b = 0; b < NB; b++)
    if (A_cnt[c][a][b] > 0)
      printf("A %c %d %d %.0f %.0f %.0f %.0f %.0f\n", "PCS"[c], a, b, A_cnt[c][a][b], A_s[c][a][b], A_s2[c][a][b],
             A_z[c][a][b], A_l2[c][a][b]);
  for (int c = 0; c < 3; c++) for (int g = 0; g < 106; g++) for (int k = 0; k < 213; k++) for (int b = 0; b < NB; b++)
    if (K_cnt[c][g][k][b] > 0)
      printf("K %c %d %d %d %.0f %.0f %.0f %.0f\n", "PCS"[c], g, k, b, K_cnt[c][g][k][b], K_s[c][g][k][b],
             K_z[c][g][k][b], K_l2[c][g][k][b]);
  return 0;
}
