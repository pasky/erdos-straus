// z59 MSPLUS: exact R(n) for all odd n = 1 (mod 4), n <= N, binned by the local model mean m(n).
//   m(n) = lead(a) * K(n) * L^2 + c1(a) * L + c0(a),  a = n mod 840, L = log(n/4),
//   lead, c1, c0 from data/z59/msplus/coef840.txt (scripts/z59_msplus_coef.py; 840-level local model),
//   K(n) = prod_{11 <= q <= QMAX, q prime} (q | n ? (q^2 - q + 1)/(q^2 + 1) : 1)   (dead-moduli factor at q >= 11,
//          relative to q not dividing n; the common factor prod (1 + 1/q^2) over q >= 11 is ~1.02 and omitted).
// Output (stdout): "H cat grp b mb kb count zeros r2 sumR summ"  with cat P/C/S (prime / non-square composite / square),
//   grp = gcd(n,105) or 0 for a in M (Mordell classes), b = floor(4 log10 n), mb = floor(m),
//   kb = bucket of k(n) = least odd prime l with (n/l) = -1, l !| n: 0:k=3 1:5 2:7 3:11 4:13 5:17..23 6:29..47 7:>47/none
// Usage: z59_msplus_strat2 N COEFFILE
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef long long ll;
#define QMAX 2000
#define NB 40
#define NM 160
#define NK 8
static double H[3][9][NB][NM][NK][5];
static const int GV[9] = {0, 1, 3, 5, 7, 15, 21, 35, 105};
int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "usage: N COEFFILE\n"); return 1; }
  ll N = atoll(argv[1]);
  if (N < 5 || N > 1200000000LL) { fprintf(stderr, "N range\n"); return 1; }
  static double lead[840], c1[840], c0[840];
  FILE *f = fopen(argv[2], "r"); int a; double x, y, z;
  while (fscanf(f, "%d %lf %lf %lf", &a, &x, &y, &z) == 4) { lead[a] = x; c1[a] = y; c0[a] = z; }
  fclose(f);
  ll I = (N - 1) / 4;
  uint16_t *R = calloc(I + 1, 2);
  uint8_t *comp = calloc(N / 2 + 1, 1);
  float *K = malloc((I + 1) * sizeof(float));
  if (!R || !comp || !K) { fprintf(stderr, "alloc\n"); return 2; }
  for (ll i = 0; i <= I; i++) K[i] = 1.0f;
  for (ll u = 1; 3 * u - 1 <= N; u++)
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 3) != 3) continue;
      ll step = 4 * u * B, n = step - u - B, s = step / 4;
      for (ll i = (n - 1) / 4; i <= I; i += s) { if (R[i] == 65535) { fprintf(stderr, "sat\n"); return 3; } R[i]++; }
    }
  for (ll p = 3; p * p <= N; p += 2)
    if (!comp[p / 2]) for (ll m = p * p; m <= N; m += 2 * p) comp[m / 2] = 1;
  for (ll q = 11; q <= QMAX; q += 2) {
    if (comp[q / 2]) continue;
    float fac = (float)((double)(q * q - q + 1) / (double)(q * q + 1));
    // n = 1 (4) and n = 0 (q): n = n0 (mod 4q)
    ll n0 = q; while (n0 % 4 != 1) n0 += q;     // q odd: one of q, 2q, 3q, 4q... with n0 = 1 (4); 2q even skipped
    for (ll n = n0; n <= N; n += 4 * q) K[(n - 1) / 4] *= fac;
  }
  static const int KP[14] = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
  const int NKP = 14;
  static signed char QRt[14][48];
  for (int j = 0; j < NKP; j++) {
    for (int x = 0; x < KP[j]; x++) QRt[j][x] = -1;
    QRt[j][0] = 0;
    for (int x = 1; x < KP[j]; x++) QRt[j][x * x % KP[j]] = 1;
  }
  static const int Mset[6] = {1, 121, 169, 289, 361, 529};
  static int isM[840]; for (int j = 0; j < 6; j++) isM[Mset[j]] = 1;
  for (ll i = 1; i <= I; i++) {
    ll n = 4 * i + 1;
    ll r = (ll)sqrtl((long double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++;
    int cat = (r * r == n) ? 2 : (comp[n / 2] ? 1 : 0);
    int a = n % 840;
    int g = 1; if (n % 3 == 0) g *= 3; if (n % 5 == 0) g *= 5; if (n % 7 == 0) g *= 7;
    int grp = isM[a] ? 0 : g;
    double L = log((double)n / 4.0);
    double m = lead[a] * K[i] * L * L + c1[a] * L + c0[a];
    int b = (int)floor(4 * log10((double)n)); if (b >= NB) b = NB - 1;
    int mb = (int)floor(m); if (mb < 0) mb = 0; if (mb >= NM) mb = NM - 1;
    int k = 0;
    for (int j = 0; j < NKP; j++) if (QRt[j][n % KP[j]] == -1) { k = KP[j]; break; }
    int kb = k == 3 ? 0 : k == 5 ? 1 : k == 7 ? 2 : k == 11 ? 3 : k == 13 ? 4 : (k >= 17 && k <= 23) ? 5 : (k >= 29 && k <= 47) ? 6 : 7;
    int gi = 0; while (GV[gi] != grp) gi++;
    double *h = H[cat][gi][b][mb][kb];
    h[0]++; if (R[i] == 0) h[1]++; if (R[i] == 2) h[2]++; h[3] += R[i]; h[4] += m;
  }
  for (int c = 0; c < 3; c++) for (int g = 0; g < 9; g++) for (int b = 0; b < NB; b++) for (int mb = 0; mb < NM; mb++)
    for (int kb = 0; kb < NK; kb++) {
      double *h = H[c][g][b][mb][kb];
      if (h[0] > 0) printf("H %c %d %d %d %d %.0f %.0f %.0f %.0f %.3f\n", "PCS"[c], GV[g], b, mb, kb, h[0], h[1], h[2], h[3], h[4]);
    }
  return 0;
}
