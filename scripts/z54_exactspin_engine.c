// z54 EXACTSPIN engine: spin layers of the class-within-genus layer R - G on the Thm U family at one odd n.
// Family/window exactly as scripts/z53_genusx_engine.c (u squarefree = 1 (4) in (U0,U1], w odd squarefree in (Y,X],
// gcd(w, u n) = 1, shell w | n+u, w'' = (n+u)/(2w)).  On a shell point put x := -w'' mod u, G := (Z/u)^x = A2 x Aodd.
// Per shell point with w'' = 3 (4) (weight 2 = both orders):
//   R    : 1[x = 1]
//   G    : 1[x in G^2]/|G^2|
//   S2   : (1[x_2 = 1] - 1[x in G^2]/|A2^2|) * 1[x_odd = 1]            (2-power spin layer: quartic, octic, ...)
//   Sodd : (1[x in G^2]/|A2^2|) * (1[x_odd = 1] - 1/|Aodd|)             (odd spin layer: cubic, quintic, ...)
//   (R - G = S2 + Sodd identically; both vanish pointwise off the genus, hence at odd squares.)
//   D_k  : (1/phi(u)) sum_{psi mod u, ord psi = k} psi(x)                 (exact-order-k layer, k in KL)
// Model variances (x uniform; shell points independent):
//   VG2, VGo: x uniform in its actual G^2-coset (genus-conditioned) for S2, Sodd;  VRG = VG2 + VGo;
//   VK[k]   : x uniform on G for D_k  (= N_k/phi^2).
// Optional dump (argv[7]): one line per shell point with w''=3(4): u w w2 genus hit.
// Usage: z54_exactspin_engine n U0 U1 Y X [dumpfile]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef long long ll; typedef __int128 i128;
static ll mpow(ll b, ll e, ll m){ ll r=1%m; b%=m; if(b<0)b+=m; while(e){ if(e&1) r=(ll)((i128)r*b%m); b=(ll)((i128)b*b%m); e>>=1;} return r; }
static ll gcdl(ll a, ll b){ if(a<0)a=-a; if(b<0)b=-b; while(b){ ll c=a%b; a=b; b=c;} return a; }
static int mu(ll n){ int s=1; for(ll q=2;q*q<=n;q++) if(n%q==0){ n/=q; if(n%q==0) return 0; s=-s; } if(n>1) s=-s; return s; }
#define MAXF 64
typedef struct { int k; ll pr[MAXF]; int ex[MAXF]; } fac_t;
static const int KL[] = {3,4,5,6,7,8,9,10,11,12,13,16,20,24};
#define NK (int)(sizeof(KL)/sizeof(KL[0]))

int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage\n"); return 1; }
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
  double R = 0, G = 0, S2 = 0, So = 0, VG2 = 0, VGo = 0, VRu = 0;
  double DK[NK], VK[NK]; for (int k = 0; k < NK; k++) DK[k] = VK[k] = 0;
  double R_pr = 0, G_pr = 0, S2_pr = 0, So_pr = 0; // prime-u sub-piece
  ll nshell = 0, nsh3 = 0, ngen = 0, nhit = 0, badsplit = 0;
  for (ll u = U0 + 1; u <= U1; u++) {
    if (u % 4 != 1) continue;
    ll up[32]; int ku = 0; ll t = u; int sqf = 1;
    for (ll q = 3; q * q <= t; q += 2) if (t % q == 0) { up[ku++] = q; t /= q; if (t % q == 0) { sqf = 0; break; } }
    if (!sqf) continue; if (t > 1) up[ku++] = t;
    { int ok = 1; for (int i = 0; i < ku; i++) if (n % up[i] == 0) ok = 0; if (!ok) continue; }
    double phiu = 1; ll a2 = 1, ao = 1; // |A2|, |Aodd|
    ll o_l[32], t_l[32];
    for (int i = 0; i < ku; i++) { ll l1 = up[i] - 1; phiu *= (double)l1; ll tw = 1; while (l1 % 2 == 0) { l1 /= 2; tw *= 2; } o_l[i] = l1; t_l[i] = tw; a2 *= tw; ao *= l1; }
    ll a22 = a2 >> ku; // |A2^2| (each factor 2^{v}-> 2^{v-1})
    double g2 = phiu / (double)(1LL << ku); // |G^2|
    // N_k(u) for model variance
    double Nk[NK];
    for (int k = 0; k < NK; k++) { double s = 0; for (ll d = 1; d <= KL[k]; d++) if (KL[k] % d == 0) { int m = mu(KL[k] / d); if (!m) continue;
        double pg = 1; for (int i = 0; i < ku; i++) pg *= (double)gcdl(d, up[i] - 1); s += m * pg; } Nk[k] = s; }
    fac_t *f = &F[u - U0 - 1]; ll N = n + u;
    ll op[MAXF]; int ko = 0; for (int i = 0; i < f->k; i++) if (f->pr[i] != 2) op[ko++] = f->pr[i];
    for (ll mask = 0; mask < (1LL << ko); mask++) {
      ll w = 1; int over = 0;
      for (int i = 0; i < ko; i++) if (mask >> i & 1) { if ((i128)w * op[i] > X) { over = 1; break; } w *= op[i]; }
      if (over || w <= Y) continue;
      { int ok = 1; for (int i = 0; i < ku; i++) if (w % up[i] == 0) ok = 0; if (!ok) continue; }
      if (gcdl(w, n) != 1) continue;
      ll w2 = N / (2 * w);
      nshell++;
      if (w2 % 4 != 3) continue;
      nsh3++;
      // x = -w2 mod u, per prime
      int isq = 1, x2one = 1, xoone = 1, xone = 1;
      ll xl[32];
      for (int i = 0; i < ku; i++) { ll l = up[i]; ll x = ((-(w2 % l)) % l + l) % l; xl[i] = x;
        if (mpow(x, (l - 1) / 2, l) != 1) isq = 0;
        if (mpow(x, o_l[i], l) != 1) x2one = 0;      // 2-component trivial <=> x^{odd part} = 1
        if (mpow(x, t_l[i], l) != 1) xoone = 0;      // odd component trivial <=> x^{2-part} = 1
        if (x != 1) xone = 0; }
      if (xone != (x2one && xoone)) badsplit++;
      double r = xone, g = isq / g2;
      double s2 = (x2one - (double)isq / (double)a22) * xoone;
      double so = ((double)isq / (double)a22) * (xoone - 1.0 / (double)ao);
      if (fabs(r - g - s2 - so) > 1e-9) badsplit++;
      R += 2 * r; G += 2 * g; S2 += 2 * s2; So += 2 * so;
      if (ku == 1) { R_pr += 2 * r; G_pr += 2 * g; S2_pr += 2 * s2; So_pr += 2 * so; }
      if (isq) { ngen++; VG2 += 4 * (1.0 / ao) * (1.0 / a22) * (1 - 1.0 / a22); VGo += 4 * (1.0 / ((double)a22 * a22)) * (1.0 / ao) * (1 - 1.0 / ao); }
      VRu += 4 * (1.0 / phiu) * (1 - 1.0 / g2);
      if (xone) nhit++;
      for (int k = 0; k < NK; k++) { double s = 0; for (ll d = 1; d <= KL[k]; d++) if (KL[k] % d == 0) { int m = mu(KL[k] / d); if (!m) continue;
          double pg = 1; int in = 1; for (int i = 0; i < ku; i++) { ll l = up[i]; ll gg = gcdl(d, l - 1); pg *= (double)gg; if (mpow(xl[i], (l - 1) / gg, l) != 1) in = 0; }
          if (in) s += m * pg; }
        DK[k] += 2 * s / phiu; VK[k] += 4 * Nk[k] / (phiu * phiu); }
      if (dump) fprintf(dump, "%lld %lld %lld %d %d\n", u, w, w2, isq, xone);
    }
  }
  printf("n=%lld U0=%lld U1=%lld Y=%lld X=%lld shell=%lld sh3=%lld gen=%lld hits=%lld badsplit=%lld R=%.0f G=%.6f S2=%.6f Sodd=%.6f VG2=%.6f VGo=%.6f VRu=%.6f Rpr=%.0f Gpr=%.6f S2pr=%.6f Soddpr=%.6f",
         n, U0, U1, Y, X, nshell, nsh3, ngen, nhit, badsplit, R, G, S2, So, VG2, VGo, VRu, R_pr, G_pr, S2_pr, So_pr);
  for (int k = 0; k < NK; k++) printf(" D%d=%.6f V%d=%.6f", KL[k], DK[k], KL[k], VK[k]);
  printf("\n");
  if (dump) fclose(dump);
  return 0;
}
