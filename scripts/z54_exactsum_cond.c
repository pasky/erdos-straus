// z54 EXACTSUM: conductor profile of the exact class-minus-genus layer R - G on the Thm U family at one odd n.
// Family (as Z53_GENUSX): u squarefree, u = 1 (4), U0 < u <= U1, gcd(u,n)=1; w odd squarefree, gcd(w,u n)=1,
// Y < w <= X, w | n+u (shell). w'' = (n+u)/(2w). Requires 8*U1*X <= n, n = 1 (4).
// Per shell point with w'' = 3 (4), s := -w'' mod u, the identity
//   2*1[s=1 (u)] - (2*2^omega(u)/phi(u))*1[s in squares mod u] = sum_{f | u, f>1} (2/phi(u)) * [prod_{l|f}((l-1)1[s=1 (l)]-1) - (s/f)]
// splits R - G into conductor-f pieces D_f (the primitive non-real characters mod f of -w'').
// Output: R, G, identity check, and the D-mass bucketed
//   (A) by rho = log f / log u  : [0,.25) [.25,.5) [.5,.75) [.75,1) {1}
//   (B) by m_f = #{u in calU : f | u} (number of integers n+u feeding block f): 1, 2-3, 4-15, 16-63, >=64
//   plus sum_f |D_f| (triangle inequality over conductor blocks) and sum_u |t_u| (over u).
// Usage: z54_exactsum_cond n U0 U1 Y X [dumpfile]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll; typedef __int128 i128;

static int jacobi(ll a, ll m) { a %= m; if (a < 0) a += m; int t = 1;
  while (a) { while ((a & 1) == 0) { a >>= 1; ll r = m & 7; if (r == 3 || r == 5) t = -t; }
    ll tmp = a; a = m; m = tmp; if ((a & 3) == 3 && (m & 3) == 3) t = -t; a %= m; }
  return m == 1 ? t : 0; }
#define MAXF 64
typedef struct { int k; ll pr[MAXF]; } fac_t;

int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage: n U0 U1 Y X [dump]\n"); return 1; }
  ll n = atoll(argv[1]), U0 = atoll(argv[2]), U1 = atoll(argv[3]), Y = atoll(argv[4]), X = atoll(argv[5]);
  FILE *dump = argc > 6 ? fopen(argv[6], "w") : NULL;
  if ((i128)8 * U1 * X > n) { fprintf(stderr, "8 U1 X > n\n"); return 1; }
  if (n % 4 != 1) { fprintf(stderr, "need n = 1 mod 4\n"); return 1; }
  ll L = U1 - U0;
  ll lim = (ll)sqrtl((long double)(n + U1)) + 2;
  char *comp = calloc(lim + 1, 1); ll *pr = malloc(sizeof(ll) * (lim / 2 + 10)); ll np = 0;
  for (ll i = 2; i <= lim; i++) { if (!comp[i]) { pr[np++] = i; if (i <= lim / i) for (ll j = i * i; j <= lim; j += i) comp[j] = 1; } }
  free(comp);
  ll *rem = malloc(sizeof(ll) * (L + 1)); fac_t *F = calloc(L + 1, sizeof(fac_t));
  for (ll i = 0; i < L; i++) rem[i] = n + U0 + 1 + i;
  for (ll t = 0; t < np; t++) { ll q = pr[t]; ll s = ((n + U0 + 1 + q - 1) / q) * q;
    for (ll v = s; v <= n + U1; v += q) { ll i = v - (n + U0 + 1); while (rem[i] % q == 0) rem[i] /= q;
      if (F[i].k < MAXF) F[i].pr[F[i].k++] = q; } }
  for (ll i = 0; i < L; i++) if (rem[i] > 1) F[i].pr[F[i].k++] = rem[i];
  // calU and m_f
  int *mf = calloc(U1 + 1, sizeof(int)); char *inU = calloc(U1 + 1, 1);
  for (ll u = U0 + 1; u <= U1; u++) { if (u % 4 != 1) continue; ll t = u; int sqf = 1, ok = 1;
    for (ll q = 3; q * q <= t; q += 2) if (t % q == 0) { t /= q; if (t % q == 0) { sqf = 0; break; } }
    if (!sqf) continue; if (n % u == 0 && u > 1) continue;
    // gcd(u,n)=1 check
    { ll a = u, b = n % u; while (b) { ll c = a % b; a = b; b = c; } if (a != 1) ok = 0; }
    if (!ok) continue; inU[u] = 1; }
  for (ll u = 1; u <= U1; u++) if (inU[u]) for (ll f = 1; f * f <= u; f++) if (u % f == 0) { mf[f]++; if (f * f != u) mf[u / f]++; }
  double *Df = calloc(U1 + 1, sizeof(double));
  double R = 0, G = 0, bA[5] = {0}, bB[5] = {0}, sumAbsTu = 0, maxerr = 0;
  ll nshell = 0, nshell3 = 0, nhit = 0, ngen = 0, nU = 0;
  for (ll u = U0 + 1; u <= U1; u++) {
    if (!inU[u]) continue; nU++;
    ll up[32]; int ku = 0; ll t = u;
    for (ll q = 3; q * q <= t; q += 2) if (t % q == 0) { up[ku++] = q; t /= q; }
    if (t > 1) up[ku++] = t;
    double phiu = 1; for (int i = 0; i < ku; i++) phiu *= (double)(up[i] - 1);
    double lu = log((double)u);
    fac_t *fc = &F[u - U0 - 1]; ll N = n + u;
    ll op[MAXF]; int ko = 0; for (int i = 0; i < fc->k; i++) if (fc->pr[i] != 2) op[ko++] = fc->pr[i];
    // squarefree check of odd part not needed for w (w squarefree by construction: distinct primes)
    double tu = 0;
    for (ll mask = 0; mask < (1LL << ko); mask++) {
      ll w = 1; int over = 0;
      for (int i = 0; i < ko; i++) if (mask >> i & 1) { if ((i128)w * op[i] > X) { over = 1; break; } w *= op[i]; }
      if (over || w <= Y) continue;
      { int ok = 1; for (int i = 0; i < ku; i++) if (w % up[i] == 0) ok = 0; if (!ok) continue; }
      { ll a = w, b = n; while (b) { ll c = a % b; a = b; b = c; } if (a != 1) continue; }
      ll w2 = N / (2 * w); nshell++;
      if (w2 % 4 != 3) continue; nshell3++;
      int a_l[32], leg[32], allone = 1, allsq = 1;
      for (int i = 0; i < ku; i++) { ll l = up[i]; ll s = ((-(w2 % l)) % l + l) % l;
        a_l[i] = (s == 1) ? (int)(l - 2) : -1; leg[i] = jacobi(s, l); if (s != 1) allone = 0; if (leg[i] != 1) allsq = 0; }
      double cls = allone ? 2.0 : 0.0, gen = allsq ? 2.0 * ldexp(1.0, ku) / phiu : 0.0;
      if (allone && !allsq) { fprintf(stderr, "class not in genus\n"); return 2; }
      R += cls; G += gen; if (allone) nhit++; if (allsq) ngen++;
      double tot = 0;
      for (int dm = 1; dm < (1 << ku); dm++) { ll f = 1; double pa = 1; int pl = 1;
        for (int i = 0; i < ku; i++) if (dm >> i & 1) { f *= up[i]; pa *= a_l[i]; pl *= leg[i]; }
        double c = (2.0 / phiu) * (pa - pl); tot += c; Df[f] += c;
        double rho = (f == u) ? 1.0 : log((double)f) / lu;
        int ia = (f == u) ? 4 : (rho < 0.25 ? 0 : rho < 0.5 ? 1 : rho < 0.75 ? 2 : 3); bA[ia] += c;
        int m = mf[f]; int ib = m <= 1 ? 0 : m <= 3 ? 1 : m <= 15 ? 2 : m <= 63 ? 3 : 4; bB[ib] += c; }
      double err = fabs(tot - (cls - gen)); if (err > maxerr) maxerr = err;
      tu += cls - gen;
    }
    sumAbsTu += fabs(tu);
  }
  double sumAbsDf = 0; for (ll f = 2; f <= U1; f++) sumAbsDf += fabs(Df[f]);
  if (dump) { for (ll f = 2; f <= U1; f++) if (Df[f] != 0) fprintf(dump, "%lld\t%d\t%.9g\n", f, mf[f], Df[f]); fclose(dump); }
  printf("n=%lld U0=%lld U1=%lld Y=%lld X=%lld nU=%lld shell=%lld shell3=%lld hits=%lld gen=%lld R=%.0f G=%.6f RG=%.6f "
         "A0=%.6f A1=%.6f A2=%.6f A3=%.6f Atop=%.6f B1=%.6f B2=%.6f B3=%.6f B4=%.6f B5=%.6f sumAbsDf=%.6f sumAbsTu=%.6f maxerr=%.3g\n",
         n, U0, U1, Y, X, nU, nshell, nshell3, nhit, ngen, R, G, R - G, bA[0], bA[1], bA[2], bA[3], bA[4], bB[0], bB[1], bB[2], bB[3], bB[4],
         sumAbsDf, sumAbsTu, maxerr);
  return 0;
}
