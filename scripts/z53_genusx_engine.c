// z53 GENUSX engine: exact sums over the Thm U family F(n) = {(u,w)} at one odd n (prime p, or a control).
// Family: u squarefree, u = 1 (4), U0 < u <= U1; w odd squarefree, gcd(w,u n) = 1, Y < w <= X; requires 8*U1*X <= n.
// Exact quantities (both orders counted, factor 2):
//   R  = 2 #{(u,w): w | n+u, w'' = (n+u)/(2w) = -1 (mod 4u)}                     [the (*) events of F]
//   G  = 2 sum_u (2^{omega(u)}/phi(u)) #{w | n+u in window : w'' in -(Z/4u)^{x2}}  [exact divisors, genus class]
//   components of G = sum_u phi(u)^{-1} sum_{w|n+u} sum_eta eps_eta eta(w):
//     E1 (eta=1), C4 (eta=chi_{-4}), CU0 (eta=(./u)), CBM (eta=chi_{-4}(./u)), REST (1<d<u)
//   Lemma 2 check: eps*eta for d in {1,u} computed from the definition vs the closed forms 1, -chi4(w''),
//   chi4(w'')(w''/n), -(w''/n); and the full sum over all (d,j) vs 2^{omega(u)+1} 1[genus] (for omega(u) <= 8).
// Mode 'D' additionally computes the density sums by direct summation over w (small n only):
//   M    = 2 sum_u (2^{omega(u)}/phi(u)) sum_{w in window, (i),(ii),(iii)} 2^{omega(w)}/phi(w)
//   Mcls = 2 sum_u sum_{w in window, w = r_u (4u)} 2^{omega(w)} 1[(i)] / phi(w)
// Usage: z53_genusx_engine E|D n U0 U1 Y X
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128;

static int jacobi(ll a, ll m) { // m odd positive
  a %= m; if (a < 0) a += m; int t = 1;
  while (a) { while ((a & 1) == 0) { a >>= 1; ll r = m & 7; if (r == 3 || r == 5) t = -t; }
    ll tmp = a; a = m; m = tmp; if ((a & 3) == 3 && (m & 3) == 3) t = -t; a %= m; }
  return m == 1 ? t : 0;
}
static ll mpow(ll b, ll e, ll m){ ll r=1%m; b%=m; if(b<0)b+=m; while(e){ if(e&1) r=(ll)((i128)r*b%m); b=(ll)((i128)b*b%m); e>>=1;} return r; }
static ll gcdl(ll a, ll b){ while(b){ ll c=a%b; a=b; b=c;} return a; }
static int chi4(ll x) { x %= 4; if (x < 0) x += 4; return x == 1 ? 1 : (x == 3 ? -1 : 0); }

#define MAXF 64
typedef struct { int k; ll pr[MAXF]; int ex[MAXF]; } fac_t;

int main(int argc, char **argv) {
  if (argc < 7) { fprintf(stderr, "usage\n"); return 1; }
  char mode = argv[1][0];
  ll n = atoll(argv[2]), U0 = atoll(argv[3]), U1 = atoll(argv[4]), Y = atoll(argv[5]), X = atoll(argv[6]);
  if ((i128)8 * U1 * X > n) { fprintf(stderr, "8 U1 X > n\n"); return 1; }
  if (n % 4 != 1) { fprintf(stderr, "need n = 1 mod 4\n"); return 1; }
  ll L = U1 - U0;
  // primes up to sqrt(n+U1)
  ll lim = (ll)sqrtl((long double)(n + U1)) + 2;
  char *comp = calloc(lim + 1, 1); ll *pr = malloc(sizeof(ll) * (lim / 2 + 10)); ll np = 0;
  for (ll i = 2; i <= lim; i++) { if (!comp[i]) { pr[np++] = i; for (ll j = i * i; j <= lim; j += i) comp[j] = 1; } }
  // segmented factorisation of n+u, u in (U0, U1]
  ll *rem = malloc(sizeof(ll) * (L + 1)); fac_t *F = calloc(L + 1, sizeof(fac_t));
  for (ll i = 0; i < L; i++) rem[i] = n + U0 + 1 + i;
  for (ll t = 0; t < np; t++) { ll q = pr[t]; ll s = ((n + U0 + 1 + q - 1) / q) * q;
    for (ll v = s; v <= n + U1; v += q) { ll i = v - (n + U0 + 1); int e = 0; while (rem[i] % q == 0) { rem[i] /= q; e++; }
      if (F[i].k < MAXF) { F[i].pr[F[i].k] = q; F[i].ex[F[i].k] = e; F[i].k++; } } }
  for (ll i = 0; i < L; i++) if (rem[i] > 1) { F[i].pr[F[i].k] = rem[i]; F[i].ex[F[i].k] = 1; F[i].k++; }
  static const int KS[4] = {4, 6, 12, 120}; double GK[4] = {0, 0, 0, 0};
  double R = 0, G = 0, E1 = 0, C4 = 0, CU0 = 0, CBM = 0, REST = 0, M = 0, Mcls = 0;
  ll nU = 0, nshell = 0, nhit = 0, ngen = 0, bad2 = 0, badfull = 0, nfullchk = 0;
  // small-prime factorisation of u by trial division (u <= U1 small)
  // for mode D: smallest prime factor sieve up to X
  int *spf = NULL;
  if (mode == 'D') { spf = calloc(X + 1, sizeof(int)); for (ll i = 2; i <= X; i++) if (!spf[i]) for (ll j = i; j <= X; j += i) if (!spf[j]) spf[j] = (int)i; }
  for (ll u = U0 + 1; u <= U1; u++) {
    if (u % 4 != 1) continue;
    ll up[32]; int ku = 0; ll t = u; int sqf = 1;
    for (ll q = 3; q * q <= t; q += 2) if (t % q == 0) { up[ku++] = q; t /= q; if (t % q == 0) { sqf = 0; break; } }
    if (!sqf) continue; if (t > 1) up[ku++] = t;
    { int ok = 1; for (int i = 0; i < ku; i++) if (n % up[i] == 0) ok = 0; if (!ok) continue; }
    nU++;
    double phiu = 1; for (int i = 0; i < ku; i++) phiu *= (double)(up[i] - 1);
    double wg = ldexp(1.0, ku) / phiu; // 2^omega(u)/phi(u)
    fac_t *f = &F[u - U0 - 1]; ll N = n + u; // N = 2 mod 4
    // odd prime factors of N (squarefree divisor choices); w must be coprime to u and n
    ll op[MAXF]; int ko = 0; for (int i = 0; i < f->k; i++) if (f->pr[i] != 2) op[ko++] = f->pr[i];
    for (ll mask = 0; mask < (1LL << ko); mask++) {
      ll w = 1; int over = 0;
      for (int i = 0; i < ko; i++) if (mask >> i & 1) { if ((i128)w * op[i] > X) { over = 1; break; } w *= op[i]; }
      if (over || w <= Y) continue;
      { int ok = 1; for (int i = 0; i < ku; i++) if (w % up[i] == 0) ok = 0; if (!ok) continue; }
      { ll a = w, b = n; while (b) { ll c = a % b; a = b; b = c; } if (a != 1) continue; }
      ll w2 = N / (2 * w); // w''
      nshell++;
      int cls = (w2 % (4 * u)) == 4 * u - 1;
      int gen = (w2 % 4 == 3); for (int i = 0; i < ku && gen; i++) if (jacobi(-w2, up[i]) != 1) gen = 0;
      if (cls && !gen) { fprintf(stderr, "class not in genus! u=%lld w=%lld\n", u, w); return 2; }
      if (cls) { R += 2; nhit++; }
      if (gen) { G += 2 * wg; ngen++; }
      if (gen) for (int k = 0; k < 4; k++) { // K-th power layer on the u-side (exact divisors): -w'' in (Z/u)^{xK}, w''=3 (4)
        double wt = 1.0 / phiu; int in = 1;
        for (int i = 0; i < ku; i++) { ll l = up[i]; ll g = gcdl(KS[k], l - 1); wt *= (double)g;
          ll x = ((-(w2 % l)) % l + l) % l; if (mpow(x, (l - 1) / g, l) != 1) in = 0; }
        if (in) GK[k] += 2 * wt; }
      int jw2 = jacobi(w2, n), c4 = chi4(w2);
      // definition-based eps*eta for d in {1,u}
      ll w0 = ((-(n + u) / 2) % 4 + 4) % 4; int c4w0 = chi4(w0), c4w = chi4(w);
      int e10 = 1, e11 = c4w0 * c4w, e_u0, e_u1;
      { ll a = ((-2 * (n % u)) % u + u) % u; e_u0 = jacobi(a, u) * jacobi(w, u); e_u1 = e_u0 * c4w0 * c4w; }
      if (u == 1) { e_u0 = e10; e_u1 = e11; }
      if (e11 != -c4 || (u > 1 && (e_u0 != c4 * jw2 || e_u1 != -jw2))) bad2++;
      double iu = 1.0 / phiu;
      E1 += iu; C4 += iu * e11;
      if (u > 1) { CU0 += iu * e_u0; CBM += iu * e_u1; }
      // full expansion check over all d | u, j in {0,1}
      if (ku <= 8) { int tot = 0; ll a2 = ((-2 * (n % u)) % u + u) % u;
        for (int dm = 0; dm < (1 << ku); dm++) { ll d = 1; for (int i = 0; i < ku; i++) if (dm >> i & 1) d *= up[i];
          int ed = (d == 1) ? 1 : jacobi(a2 % d, d) * jacobi(w, d);
          tot += ed + ed * c4w0 * c4w; }
        nfullchk++; if (tot != (gen ? (1 << (ku + 1)) : 0)) badfull++; }
    }
    if (mode == 'D') { // direct density sums
      ll r4u = 4 * u; double sM = 0, sC = 0; ll a2 = ((-2 * (n % u)) % u + u) % u;
      ll w0 = ((-(n + u) / 2) % 4 + 4) % 4;
      for (ll w = Y + 1; w <= X; w++) {
        if (!(w & 1)) continue;
        ll x = w; int om = 0, ok = 1; double phw = 1;
        while (x > 1) { ll q = spf[x]; x /= q; if (x % q == 0) { ok = 0; break; } if (u % q == 0 || n % q == 0) { ok = 0; break; }
          if (jacobi(-((u % q) * (n % q) % q), q) != 1) { ok = 0; break; } om++; phw *= (double)(q - 1); }
        if (!ok) continue;
        double rho = ldexp(1.0, om) / phw;
        // genus (ii),(iii)
        int g = (w % 4 == w0); for (int i = 0; i < ku && g; i++) { ll l = up[i]; ll m2 = ((-2 * (n % l)) % l + l) % l; if (jacobi((m2 * (w % l)) % l, l) != 1) g = 0; }
        if (g) sM += rho;
        // exact class mod 8u: w = w0 (4) and 2w = -n (u)
        if (w % 4 == w0 && ((2 * w + n) % u) == 0) sC += rho;
      }
      M += 2 * wg * sM; Mcls += 2 * sC; (void)r4u;
    }
  }
  REST = G / 1.0 - (E1 + C4 + CU0 + CBM);
  printf("n=%lld U0=%lld U1=%lld Y=%lld X=%lld nU=%lld shell=%lld hits=%lld gen=%lld R=%.0f G=%.6f E1=%.6f C4=%.6f CU0=%.6f CBM=%.6f REST=%.6f lemma2_bad=%lld fullchk=%lld fullbad=%lld G4=%.6f G6=%.6f G12=%.6f G120=%.6f",
         n, U0, U1, Y, X, nU, nshell, nhit, ngen, R, G, E1, C4, CU0, CBM, REST, bad2, nfullchk, badfull, GK[0], GK[1], GK[2], GK[3]);
  if (mode == 'D') printf(" M=%.6f Mcls=%.6f", M, Mcls);
  printf("\n");
  return 0;
}
