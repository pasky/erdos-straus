// z56 FAMDESIGN: exact genus layer M_gen(p) split into G and the Burgess corner K, plus the density M0 split likewise.
// For each odd n = p (prime, p = 1 mod 4) given on stdin: enumerate all pairs (o, e), o odd, e = 2^k e' even, gcd(o,e) = 1,
// 4oe - o - e <= p; weight W(o,e) = 2^{2-k} 2^{w(o)+w(e')} / (phi(o) phi(e')) if (i) (-po/l) = 1 for l | e', (ii) (-pe/l) = 1
// for l | o, (iii) o + e = -p (mod 8)   (Z56_FAMDESIGN Lemma 3.2; = 2 s(q)/phi(q) 1[pa square mod q]);
// density weight 2/phi(4oe) (both orders).  G: max^4 > min * p.  Output:
//   p  L^2  M0  M0_G  Mgen  M_G  M_K  M_{A∩G_{1/15}}  M0_{G_{1/15}}
// Build: gcc -O2 -o /tmp/z56mgen scripts/z56_famdesign_mgen.c -lm      (memory ~ 4 p/4 bytes for the spf table)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int *spf; static ll lim;
static void build(ll n) { lim = n; spf = calloc(n + 1, sizeof(int));
  for (ll i = 2; i <= n; i++) if (!spf[i]) { for (ll j = i; j <= n; j += i) if (!spf[j]) spf[j] = (int)i; } }

// exact integer membership tests (no floating point): Q^4 > P*n, P^15 > n
static int gtest(long long P, long long Q, long long n) { if (Q > 3000000000LL) return 1; __int128 q2 = (__int128)Q * Q; return q2 * q2 > (__int128)P * n; }
static int lamtest(long long P, long long n) { __int128 a = 1; for (int i = 0; i < 15; i++) { a *= P; if (a > n) return 1; } return a > n; }
static long long hccut(long long n) { long double L = logl((long double)n), s = L * L; if (fabsl(s - roundl(s)) < 1e-12L) { fprintf(stderr, "HC cutoff tie at %lld\n", n); exit(3); } return (long long)floorl(s); }
static int jacobi(ll a, ll n) { // n odd positive
  a %= n; if (a < 0) a += n; int t = 1;
  while (a) { while ((a & 1) == 0) { a >>= 1; ll r = n & 7; if (r == 3 || r == 5) t = -t; }
    ll tmp = a; a = n; n = tmp; if ((a & 3) == 3 && (n & 3) == 3) t = -t; a %= n; }
  return n == 1 ? t : 0;
}
typedef struct { int np; ll pr[16]; ll phi; } fac;
static void factor(ll m, fac *f) { f->np = 0; f->phi = 1; while (m > 1) { ll q = spf[m], pk = 1; while (m % q == 0) { m /= q; pk *= q; } f->pr[f->np++] = q; f->phi *= pk / q * (q - 1); } }
int main(void) {
  ll p;
  while (scanf("%lld", &p) == 1) {
    if (p % 4 != 1) continue;
    ll N = p / 4 + 2; if (N > lim) { free(spf); build(N); }
    long double L = logl((long double)p);
    long double M0 = 0, M0G = 0, Mg = 0, MG = 0, MK = 0, MGl = 0, M0Gl = 0;
    for (ll o = 1; 4 * o * 2 - o - 2 <= p; o += 2) {
      fac fo; factor(o, &fo);
      for (ll e = 2; 4 * o * e - o - e <= p; e += 2) {
        int k = 0; ll ep = e; while ((ep & 1) == 0) { ep >>= 1; k++; }
        fac fe; factor(ep, &fe);
        int cop = 1; for (int i = 0; i < fo.np && cop; i++) if (ep % fo.pr[i] == 0) cop = 0;
        if (!cop) continue;
        ll P = o < e ? o : e, Q = o < e ? e : o;
        int G = gtest(P, Q, p), lam = lamtest(P, p);
        long double dens = 2.0L / ((long double)(1LL << (k + 1)) * fo.phi * fe.phi); // 2/phi(4oe)
        M0 += dens; if (G) M0G += dens; if (G && lam) M0Gl += dens;
        if (((o + e + p) & 7) != 0) continue;                       // (iii)
        int ok = 1;
        for (int i = 0; i < fe.np && ok; i++) { ll l = fe.pr[i]; if (jacobi(-(p % l) * (o % l), l) != 1) ok = 0; }   // (i)
        for (int i = 0; i < fo.np && ok; i++) { ll l = fo.pr[i]; if (jacobi(-(p % l) * (e % l), l) != 1) ok = 0; }   // (ii)
        if (!ok) continue;
        long double W = (long double)(1 << (fo.np + fe.np)) * 4.0L / ((long double)(1LL << k) * fo.phi * fe.phi);
        Mg += W; if (G) MG += W; else MK += W; if (G && lam) MGl += W;
      }
    }
    printf("%lld %.4Lf %.5Lf %.5Lf %.5Lf %.5Lf %.5Lf %.5Lf %.5Lf\n", p, L * L, M0, M0G, Mg, MG, MK, MGl, M0Gl); fflush(stdout);
  }
  return 0;
}
