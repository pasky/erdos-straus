// z54 EXACTSUM: sizes of the frequency sums W(a,q) of the exact class count on the Thm U family at one odd n.
//   R/2 = sum_{q odd sqfree} sum_{a mod* q} W(a,q),
//   W(a,q) = e(a/q) sum_{u in calU, q | u} u^{-1} sum_{w in shell(u), k = ceil(n/w) = 6 (8)} e(a k/(2q))   (k = 2 w'').
// For q <= Qmax (q | some u) prints: q, #u with q|u, #terms, Wtriv = sum of |coefficients| = sum u^{-1},
//   rms2 = sqrt(sum u^{-2}) (random-phase scale), max_a |W(a,q)|, rms_a |W(a,q)|, P_q = sum_a W(a,q) (real),
//   and the "density" value of P_q: mu(q)^2-weighted (not computed; P_q itself is reported).
// Usage: z54_exactsum_wsum n U0 U1 Y X Qmax
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
typedef long long ll; typedef __int128 i128;
#define MAXF 64
typedef struct { int k; ll pr[MAXF]; } fac_t;
static ll gcdl(ll a, ll b){ while(b){ ll c=a%b; a=b; b=c;} return a; }
int main(int argc, char **argv) {
  if (argc < 7) { fprintf(stderr, "usage: n U0 U1 Y X Qmax\n"); return 1; }
  ll n = atoll(argv[1]), U0 = atoll(argv[2]), U1 = atoll(argv[3]), Y = atoll(argv[4]), X = atoll(argv[5]); int Q = atoi(argv[6]);
  if ((i128)8 * U1 * X > n || n % 4 != 1) { fprintf(stderr, "bad window\n"); return 1; }
  ll L = U1 - U0; ll lim = (ll)sqrtl((long double)(n + U1)) + 2;
  char *comp = calloc(lim + 1, 1); ll *pr = malloc(sizeof(ll) * (lim / 2 + 10)); ll np = 0;
  for (ll i = 2; i <= lim; i++) { if (!comp[i]) { pr[np++] = i; if (i <= lim / i) for (ll j = i * i; j <= lim; j += i) comp[j] = 1; } }
  free(comp);
  ll *rem = malloc(sizeof(ll) * (L + 1)); fac_t *F = calloc(L + 1, sizeof(fac_t));
  for (ll i = 0; i < L; i++) rem[i] = n + U0 + 1 + i;
  for (ll t = 0; t < np; t++) { ll q = pr[t]; ll s = ((n + U0 + 1 + q - 1) / q) * q;
    for (ll v = s; v <= n + U1; v += q) { ll i = v - (n + U0 + 1); while (rem[i] % q == 0) rem[i] /= q; if (F[i].k < MAXF) F[i].pr[F[i].k++] = q; } }
  for (ll i = 0; i < L; i++) if (rem[i] > 1) F[i].pr[F[i].k++] = rem[i];
  double complex **W = calloc(Q + 1, sizeof(double complex *));
  for (int q = 1; q <= Q; q += 2) W[q] = calloc(q, sizeof(double complex));
  double *triv = calloc(Q + 1, sizeof(double)), *sq2 = calloc(Q + 1, sizeof(double)); ll *nt = calloc(Q + 1, sizeof(ll)), *nu = calloc(Q + 1, sizeof(ll));
  for (ll u = U0 + 1; u <= U1; u++) {
    if (u % 4 != 1) continue; ll t = u; int sqf = 1; ll up[32]; int ku = 0;
    for (ll q = 3; q * q <= t; q += 2) if (t % q == 0) { up[ku++] = q; t /= q; if (t % q == 0) { sqf = 0; break; } }
    if (!sqf) continue; if (t > 1) up[ku++] = t; if (gcdl(u, n) != 1) continue;
    for (int q = 1; q <= Q && q <= u; q += 2) if (u % q == 0) nu[q]++;
    fac_t *fc = &F[u - U0 - 1]; ll N = n + u; ll op[MAXF]; int ko = 0;
    for (int i = 0; i < fc->k; i++) if (fc->pr[i] != 2) op[ko++] = fc->pr[i];
    for (ll mask = 0; mask < (1LL << ko); mask++) {
      ll w = 1; int over = 0;
      for (int i = 0; i < ko; i++) if (mask >> i & 1) { if ((i128)w * op[i] > X) { over = 1; break; } w *= op[i]; }
      if (over || w <= Y) continue;
      { int ok = 1; for (int i = 0; i < ku; i++) if (w % up[i] == 0) ok = 0; if (!ok) continue; }
      if (gcdl(w, n) != 1) continue;
      ll w2 = N / (2 * w); if (w2 % 4 != 3) continue;
      double cu = 1.0 / (double)u;
      for (int q = 1; q <= Q && q <= u; q += 2) { if (u % q) continue; nt[q]++; triv[q] += cu; sq2[q] += cu * cu;
        ll r = (w2 + 1) % q; for (int a = 0; a < q; a++) { if (gcdl(a, q) != 1 && q > 1) continue; if (q == 1 && a) continue;
          W[q][a] += cu * cexp(2 * M_PI * I * (double)((a * r) % q) / (double)q); } }
    }
  }
  for (int q = 1; q <= Q; q += 2) { if (!nu[q]) continue; double mx = 0, s2 = 0, P = 0; int na = 0;
    for (int a = 0; a < q; a++) { if ((q > 1 && gcdl(a, q) != 1) || (q == 1 && a)) continue; double ab = cabs(W[q][a]); if (ab > mx) mx = ab; s2 += ab * ab; P += creal(W[q][a]); na++; }
    printf("%lld\t%d\t%lld\t%lld\t%.6g\t%.6g\t%.6g\t%.6g\t%.6g\n", n, q, nu[q], nt[q], triv[q], sqrt(sq2[q]), mx, sqrt(s2 / na), P); }
  return 0;
}
