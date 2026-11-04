// z56 FAMDESIGN: exact region-1 slice S1(o; Y, X) = sum_{Y < e <= X, e even, gcd(e,o)=1} W(o,e) (all k) and exact
// region-2 slice S2(e; Y, X) = sum_{Y < o <= X, o odd, gcd(o,e)=1} W(o,e), W from Lemma 3.2. Input lines: "1 p o Y X" or
// "2 p e Y X". Output: the input line + the exact sum.  Build: gcc -O2 -o /tmp/z56slice scripts/z56_famdesign_slicecheck.c -lm
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int *spf; static ll lim = 0;
static void build(ll n) { if (n <= lim) return; free(spf); lim = n; spf = calloc(n + 1, sizeof(int));
  for (ll i = 2; i <= n; i++) if (!spf[i]) for (ll j = i; j <= n; j += i) if (!spf[j]) spf[j] = (int)i; }
static int jacobi(ll a, ll n) { a %= n; if (a < 0) a += n; int t = 1;
  while (a) { while ((a & 1) == 0) { a >>= 1; ll r = n & 7; if (r == 3 || r == 5) t = -t; }
    ll tmp = a; a = n; n = tmp; if ((a & 3) == 3 && (n & 3) == 3) t = -t; a %= n; } return n == 1 ? t : 0; }
typedef struct { int np; ll pr[16]; ll phi; } fac;
static void factor(ll m, fac *f) { f->np = 0; f->phi = 1; while (m > 1) { ll q = spf[m], pk = 1; while (m % q == 0) { m /= q; pk *= q; } f->pr[f->np++] = q; f->phi *= pk / q * (q - 1); } }
static double W(ll p, ll o, ll e) {
  if (((o + e + p) & 7) != 0) return 0;
  int k = 0; ll ep = e; while ((ep & 1) == 0) { ep >>= 1; k++; }
  fac fo, fe; factor(o, &fo); factor(ep, &fe);
  for (int i = 0; i < fo.np; i++) if (ep % fo.pr[i] == 0) return 0;
  for (int i = 0; i < fe.np; i++) { ll l = fe.pr[i]; if (jacobi(-(p % l) * (o % l), l) != 1) return 0; }
  for (int i = 0; i < fo.np; i++) { ll l = fo.pr[i]; if (jacobi(-(p % l) * (e % l), l) != 1) return 0; }
  return (double)(1 << (fo.np + fe.np)) * 4.0 / ((double)(1LL << k) * fo.phi * fe.phi);
}
int main(void) { int t; ll p, v, Y, X;
  while (scanf("%d %lld %lld %lld %lld", &t, &p, &v, &Y, &X) == 5) {
    build(X > v ? X + 2 : v + 2); double s = 0;
    if (t == 1) { for (ll e = Y + 1 + ((Y + 1) & 1); e <= X; e += 2) s += W(p, v, e); }
    else { for (ll o = Y + 1 + !((Y + 1) & 1); o <= X; o += 2) s += W(p, o, v); }
    printf("%d %lld %lld %lld %lld %.6f\n", t, p, v, Y, X, s); fflush(stdout); }
  return 0; }
