// z55 CROSSU engine: class-index statistics of the exact layer R - G on the Thm U family at one odd n.
// Family/window exactly as scripts/z53_genusx_engine.c: u squarefree = 1 (4) in (U0,U1], gcd(u,n)=1; w odd squarefree
// in (Y,X], gcd(w, u n) = 1; shell: w | n+u; level divisor d = (n+u)/(2w).  Only shell points with d = 3 (4) count.
// Class index j := -d^{-1} mod u in [1,u)  (Lemma A of Z55_CROSSU.md: u*(u^{-1} mod d) = 1 + j d).
//   hit  <=> j = 1 ;  genus <=> j in (Z/u)^{x2} (i.e. (j/l) = 1 for all primes l | u).
// Twisted counts, for c in CL (c = -1, -2 mean u-1, u-2):
//   N_c := 2 #{points: j = c mod u}                     (so N_1 = R)
//   G_c := 2 sum_points 1[j in c * squares] / |G^2|      (genus-coset prediction for N_c; G_1 = G)
//   E_c := 2 sum_points 1/phi(u)  (gcd(c,u)=1)         (uniform prediction)
// Also: histogram of j/u in NB bins (all points, and genus points only), and per-u dump (optional).
// Usage: z55_crossu_engine n U0 U1 Y X [dumpfile]   -> key=value lines
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef long long ll; typedef __int128 i128;
static ll mpow(ll b, ll e, ll m){ ll r=1%m; b%=m; if(b<0)b+=m; while(e){ if(e&1) r=(ll)((i128)r*b%m); b=(ll)((i128)b*b%m); e>>=1;} return r; }
static ll gcdl(ll a, ll b){ if(a<0)a=-a; if(b<0)b=-b; while(b){ ll c=a%b; a=b; b=c;} return a; }
static ll egcd_inv(ll a, ll m){ // inverse of a mod m, m>1, gcd=1
  ll r0=m, r1=((a%m)+m)%m, s0=0, s1=1; while(r1){ ll q=r0/r1; ll t=r0-q*r1; r0=r1; r1=t; t=s0-q*s1; s0=s1; s1=t; }
  if(r0!=1) return -1; return ((s0%m)+m)%m; }
#define MAXF 64
typedef struct { int k; ll pr[MAXF]; int ex[MAXF]; } fac_t;
static const ll CL[] = {1,2,3,4,5,6,7,8,9,10,11,12,16,25,-1,-2,-3,-4};
#define NC (int)(sizeof(CL)/sizeof(CL[0]))
#define NB 10

int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage: n U0 U1 Y X [dump]\n"); return 1; }
  ll n = atoll(argv[1]), U0 = atoll(argv[2]), U1 = atoll(argv[3]), Y = atoll(argv[4]), X = atoll(argv[5]);
  FILE *dump = (argc > 6) ? fopen(argv[6], "w") : NULL;
  if ((i128)8 * U1 * X > n) { fprintf(stderr, "8 U1 X > n\n"); return 1; }
  if (n % 4 != 1) { fprintf(stderr, "need n = 1 mod 4\n"); return 1; }
  ll L = U1 - U0;
  ll lim = (ll)sqrtl((long double)(n + U1)) + 2;
  char *comp = calloc(lim + 1, 1); ll *pr = malloc(sizeof(ll) * (lim / 2 + 10)); ll np = 0;
  for (ll i = 2; i <= lim; i++) { if (!comp[i]) { pr[np++] = i; for (ll j = i * i; j <= lim; j += i) comp[j] = 1; } }
  ll *rem = malloc(sizeof(ll) * (L + 1)); fac_t *F = calloc(L + 1, sizeof(fac_t));
  for (ll i = 0; i < L; i++) rem[i] = n + U0 + 1 + i;
  for (ll t = 0; t < np; t++) { ll q = pr[t]; ll s = ((n + U0 + 1 + q - 1) / q) * q;
    for (ll v = s; v <= n + U1; v += q) { ll i = v - (n + U0 + 1); int e = 0; while (rem[i] % q == 0) { rem[i] /= q; e++; }
      if (F[i].k < MAXF) { F[i].pr[F[i].k] = q; F[i].ex[F[i].k] = e; F[i].k++; } } }
  for (ll i = 0; i < L; i++) if (rem[i] > 1) { F[i].pr[F[i].k] = rem[i]; F[i].ex[F[i].k] = 1; F[i].k++; }
  double Nc[NC], Gc[NC], Ec[NC]; for (int c = 0; c < NC; c++) Nc[c] = Gc[c] = Ec[c] = 0;
  double HB[NB], HBg[NB]; for (int b = 0; b < NB; b++) HB[b] = HBg[b] = 0;
  double VRG = 0, sumphi = 0; // model variance of R - G (genus-conditioned): sum 1/|G^2| (1 - 1/|G^2|) over genus pts
  ll nshell = 0, nsh3 = 0, ngen = 0, nhit = 0, nanti = 0, badj = 0; ll nu = 0;
  for (ll u = U0 + 1; u <= U1; u++) {
    if (u % 4 != 1) continue;
    ll up[32]; int ku = 0; ll t = u; int sqf = 1;
    for (ll q = 3; q * q <= t; q += 2) if (t % q == 0) { up[ku++] = q; t /= q; if (t % q == 0) { sqf = 0; break; } }
    if (!sqf) continue; if (t > 1) up[ku++] = t;
    { int ok = 1; for (int i = 0; i < ku; i++) if (n % up[i] == 0) ok = 0; if (!ok) continue; }
    nu++;
    double phiu = 1; for (int i = 0; i < ku; i++) phiu *= (double)(up[i] - 1);
    double g2 = phiu / (double)(1LL << ku); // |G^2|
    fac_t *f = &F[u - U0 - 1]; ll N = n + u;
    ll op[MAXF]; int ko = 0; for (int i = 0; i < f->k; i++) if (f->pr[i] != 2) op[ko++] = f->pr[i];
    for (ll mask = 0; mask < (1LL << ko); mask++) {
      ll w = 1; int over = 0;
      for (int i = 0; i < ko; i++) if (mask >> i & 1) { if ((i128)w * op[i] > X) { over = 1; break; } w *= op[i]; }
      if (over || w <= Y) continue;
      { int ok = 1; for (int i = 0; i < ku; i++) if (w % up[i] == 0) ok = 0; if (!ok) continue; }
      if (gcdl(w, n) != 1) continue;
      ll d = N / (2 * w);
      nshell++;
      if (d % 4 != 3) continue;
      nsh3++;
      // class index j = -d^{-1} mod u ; check Lemma A: u * (u^{-1} mod d) = 1 + j d
      ll dinv = egcd_inv(d % u, u); if (dinv < 0) { badj++; continue; }
      ll j = (u - dinv) % u; if (j == 0) j = u; // j in [1,u) (u>1); j==u impossible
      { ll uinv = egcd_inv(u % d, d); i128 lhs = (i128)u * uinv; i128 rhs = (i128)1 + (i128)j * d; if (lhs != rhs) badj++; }
      // genus: j in squares mod u (per prime)
      int isq = 1; for (int i = 0; i < ku; i++) { ll l = up[i]; if (mpow(j % l, (l - 1) / 2, l) != 1) { isq = 0; break; } }
      if (isq) { ngen++; VRG += (1.0 / g2) * (1.0 - 1.0 / g2); }
      if (j == 1) nhit++; if (j == u - 1) nanti++;
      sumphi += 1.0 / phiu;
      int b = (int)((long double)j / (long double)u * NB); if (b >= NB) b = NB - 1; HB[b] += 1; if (isq) HBg[b] += 1;
      for (int c = 0; c < NC; c++) {
        ll cc = CL[c] > 0 ? CL[c] % u : ((u + CL[c]) % u);
        if (gcdl(cc, u) != 1) continue;
        Ec[c] += 2.0 / phiu;
        if (j == cc) Nc[c] += 2;
        // j in c * squares <=> j * c^{-1} square <=> (j c / l) = 1 for all l | u
        int ok = 1; for (int i = 0; i < ku; i++) { ll l = up[i]; ll v = (ll)((i128)(j % l) * (cc % l) % l); if (mpow(v, (l - 1) / 2, l) != 1) { ok = 0; break; } }
        if (ok) Gc[c] += 2.0 / g2;
      }
      if (dump) fprintf(dump, "%lld %lld %lld %lld %d\n", u, w, d, j, isq);
    }
  }
  printf("n=%lld U0=%lld U1=%lld Y=%lld X=%lld nu=%lld nshell=%lld nsh3=%lld ngen=%lld nhit=%lld nanti=%lld badj=%lld\n",
         n, U0, U1, Y, X, nu, nshell, nsh3, ngen, nhit, nanti, badj);
  printf("R=%.6f G=%.6f VRG=%.6f sumphi=%.6f\n", Nc[0], Gc[0], 4 * VRG, 2 * sumphi);
  for (int c = 0; c < NC; c++) printf("N%lld=%.6f G%lld=%.6f E%lld=%.6f\n", CL[c], Nc[c], CL[c], Gc[c], CL[c], Ec[c]);
  for (int b = 0; b < NB; b++) printf("HB%d=%.0f HBg%d=%.0f\n", b, HB[b], b, HBg[b]);
  if (dump) fclose(dump);
  return 0;
}
