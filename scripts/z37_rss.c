/* O267 §3: reciprocity singular series for the five-slice count, levels t <= T.
   For each odd n = 1 (4) read from stdin, and each level 2 <= t <= T:
     N_t = t n + 1; range divisors d of N_t with 2t-1 <= d <= N_t/(2t-1).
     actual  W-_t = #{d : d = -1 (t), (d/n) = -1}       (five-slice words of level t, Thm 4.5)
     words   W_t  = #{d : d = -1 (t)}
     model R (reciprocity):  sum_{d : (d/n) = -1} rho_R(t, e(d))
     model 0 (naive):        sum_{d} rho_0(t, e(d))
   where, writing d = 2^e d_o and s = -(2/n)^e, rho_R = #{a odd mod 4t : a = -2^{-e} (t), J(-t,a) = s} / #{a odd mod 4t: J(-t,a) = s},
   rho_0 = same numerator / #{a odd mod 4t : gcd(a,t)=1}.  (chi(d) = (2/n)^e J(-t,d_o), QUESTION_R Prop 1.2.)
   Output per n: n actual words modelR model0 cleanwords(=words on levels with no chi=-1 range divisor)
   Build: gcc -O2 -o /tmp/z37/rss scripts/z37_rss.c ; usage: rss T < list_of_n */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef unsigned long long ull;
static int jac(ll a, ll n) { /* n odd positive */
  int r = 1; a %= n; if (a < 0) a += n;
  while (a) { while (!(a & 1)) { a >>= 1; ll m = n & 7; if (m == 3 || m == 5) r = -r; }
    ll t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) r = -r; a %= n; }
  return n == 1 ? r : 0; }
static ll gcdl(ll a, ll b) { while (b) { ll t = a % b; a = b; b = t; } return a; }
static int *pr; static int np;
static ll modinv(ll a, ll m) { ll g = m, x = 0, x1 = 1, a1 = a % m; if (a1 < 0) a1 += m;
  ll b = a1; while (b) { ll q = g / b, t = g - q * b; g = b; b = t; t = x - q * x1; x = x1; x1 = t; }
  x %= m; if (x < 0) x += m; return x; }
int main(int argc, char **argv) {
  int T = atoi(argv[1]); int LIM = 200000; char *s = calloc(LIM + 1, 1); pr = malloc(sizeof(int) * LIM); np = 0;
  for (int i = 2; i <= LIM; i++) if (!s[i]) { pr[np++] = i; for (ll j = (ll)i * i; j <= LIM; j += i) s[j] = 1; }
  /* precompute per t: cntJ[s] over odd a mod 4t coprime to t; and for e=0..40 numerator counts for s=+-1 */
  int *den_p = malloc(sizeof(int) * (T + 1)), *den_m = malloc(sizeof(int) * (T + 1));
  int (*num)[41][2] = malloc(sizeof(int[41][2]) * (T + 1));
  for (int t = 2; t <= T; t++) {
    den_p[t] = den_m[t] = 0; for (int e = 0; e <= 40; e++) num[t][e][0] = num[t][e][1] = 0;
    for (ll a = 1; a < 4LL * t; a += 2) { if (gcdl(a, t) != 1) continue; int J = jac(-(ll)t, a);
      if (J == 1) den_p[t]++; else if (J == -1) den_m[t]++; else continue;
      for (int e = 0; e <= 40; e++) { if (e > 0 && t % 2 == 0) break;
        ll c = (t % 2) ? (t - modinv(((ull)1 << (e % 60)) % t, t)) % t : t - 1; /* -2^{-e} mod t */
        if (t == 1) c = 0; if (a % t == c % t) num[t][e][J == 1 ? 1 : 0]++; } } }
  ll n; ll divs[200000];
  while (scanf("%lld", &n) == 1) {
    int two_n = (n % 8 == 1 || n % 8 == 7) ? 1 : -1;
    ll act = 0, words = 0, cleanw = 0; double mR = 0, m0 = 0;
    for (int t = 2; t <= T; t++) {
      ll N = (ll)t * n + 1; if ((ll)(2 * t - 1) * (2 * t - 1) > N) break;
      /* factor */
      ll m = N; ll ps[64]; int es[64], k = 0;
      for (int i = 0; i < np && (ll)pr[i] * pr[i] <= m; i++) if (m % pr[i] == 0) { ps[k] = pr[i]; es[k] = 0; while (m % pr[i] == 0) { m /= pr[i]; es[k]++; } k++; }
      if (m > 1) { if (m > (ll)LIM * LIM) { fprintf(stderr, "factor fail\n"); return 1; } ps[k] = m; es[k] = 1; k++; }
      int nd = 1; divs[0] = 1;
      for (int i = 0; i < k; i++) { int cur = nd; ll pp = 1; for (int j = 1; j <= es[i]; j++) { pp *= ps[i]; for (int q = 0; q < cur; q++) divs[nd++] = divs[q] * pp; } }
      ll lo = 2 * t - 1, hi = N / (2 * t - 1); ll aw = 0, ww = 0, negd = 0;
      for (int q = 0; q < nd; q++) { ll d = divs[q]; if (d < lo || d > hi) continue;
        int e = 0; ll dd = d; while (!(dd & 1)) { dd >>= 1; e++; }
        int chi = jac(d, n); int sv = -((e & 1) ? two_n : 1); /* needed J(-t,d_o) for chi=-1 */
        double nm = (e <= 40) ? num[t][e][sv == 1 ? 1 : 0] : 0;
        double denS = (sv == 1) ? den_p[t] : den_m[t];
        if (chi == -1) { negd++; if (denS > 0) mR += nm / denS; }
        m0 += nm / (double)(den_p[t] + den_m[t]);
        if (d % t == t - 1) { ww++; if (chi == -1) aw++; } }
      act += aw; words += ww; if (negd == 0) cleanw += ww; }
    printf("%lld %lld %lld %.4f %.4f %lld\n", n, act, words, mR, m0, cleanw); }
  return 0; }
