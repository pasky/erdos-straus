/* y5_ocensus: for primes p = 1 (mod 8), p <= X, the smallest "opposite vertex" o of a five-slice certificate
 * word (c,m,s) at N = p (memo y5_five_positions, TRANSPORT_LAW.md).  At N = 1 (8) a word is a certificate iff
 * o = 7 (mod 8), o the odd cluster variable opposite the even edge.  Positions (mirror-reduced):
 *   Pc : o = c (edge {s,h}):  s*h = p + o, h = -1 (mod o), h, s even       [mirror Ps]
 *   Pm : o = m (edge {h,h'}): h*h' = 1 + o*p, h = h' = -1 (mod o), both even
 *   Ph : o = h (edge {c,m}):  c*m = o + 1, c, m even, o | p + c            [mirror Ph']
 * mode I = interior words (letters >= 2), mode F = formal words (letters >= 1).
 * Output: histogram of o*(p) by position, and the hardest primes; per-position minima stats.
 * usage: y5_ocensus X OMAX mode(I|F) [S]   (S: run over odd squares N <= X instead of primes = T1 control) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll; typedef unsigned long long ull;
static int *pr; static int npr;
static int nfac(ull n, ull *P, int *E) { int k = 0;
  for (int i = 0; i < npr; i++) { ull q = pr[i]; if (q * q > n) break;
    if (n % q == 0) { int e = 0; while (n % q == 0) { n /= q; e++; } P[k] = q; E[k++] = e; } }
  if (n > 1) { P[k] = n; E[k++] = 1; } return k; }
static int ndiv(ull n, ull *D) { ull P[64]; int E[64]; int k = nfac(n, P, E); int nd = 1; D[0] = 1;
  for (int i = 0; i < k; i++) { int cur = nd; ull pw = 1;
    for (int e = 1; e <= E[i]; e++) { pw *= P[i]; for (int j = 0; j < cur; j++) D[nd++] = D[j] * pw; } }
  return nd; }
static ull D[200000];
static int interior;
static int Pc(ull p, ull o) { ull n = p + o; int nd = ndiv(n, D);
  for (int i = 0; i < nd; i++) { ull h = D[i], s = n / h; if (h % 2 || s % 2) continue; if ((h + 1) % o) continue;
    ull m = (h + 1) / o; if (interior && (m < 2 || s < 2)) continue; return 1; } return 0; }
static int Pm(ull p, ull o) { ull n = 1 + o * p; int nd = ndiv(n, D);
  for (int i = 0; i < nd; i++) { ull h = D[i], h2 = n / h; if (h % 2 || h2 % 2) continue; if ((h + 1) % o || (h2 + 1) % o) continue;
    ull c = (h + 1) / o, s = (h2 + 1) / o; if (interior && (c < 2 || s < 2)) continue; return 1; } return 0; }
static int Ph(ull p, ull o) { for (ull c = 2; c <= o + 1; c += 2) { if ((o + 1) % c) continue; ull m = (o + 1) / c; if (m % 2) continue;
    if ((p + c) % o) continue; ull s = (p + c) / o; if (interior && s < 2) continue; return 1; } return 0; }
int main(int argc, char **argv) {
  ll X = atoll(argv[1]); ll OMAX = atoll(argv[2]); interior = argv[3][0] == 'I';
  int L = 200000; char *sv = calloc(L, 1); pr = malloc(sizeof(int) * L); npr = 0;
  for (int i = 2; i < L; i++) if (!sv[i]) { pr[npr++] = i; for (ll j = (ll)i * i; j < L; j += i) sv[j] = 1; }
  char *cmp = calloc(X + 1, 1); for (ll i = 2; i * i <= X; i++) if (!cmp[i]) for (ll j = i * i; j <= X; j += i) cmp[j] = 1;
  static ll hist[4][4096]; ll cnt = 0, fail = 0; ll worst[20]; ll worsto[20]; int nw = 0;
  ll firstpos[3] = {0, 0, 0};
  int sq = argc > 4 && argv[4][0] == 'S'; ll r = 3;
  for (ll p = 17; p <= X; p += 8) { if (sq) { p = r * r; r += 2; if (p > X) break; } else if (cmp[p]) continue; cnt++;
    ll best = -1; int pos = -1;
    for (ll o = 7; o <= OMAX; o += 8) {
      int a = Ph(p, o), b = Pc(p, o), c = Pm(p, o);
      if (a || b || c) { best = o; pos = a ? 0 : (b ? 1 : 2); hist[0][(o - 7) / 8 < 4095 ? (o - 7) / 8 : 4095]++;
        if (a) hist[1][(o - 7) / 8 < 4095 ? (o - 7) / 8 : 4095]++; if (b) hist[2][(o - 7) / 8 < 4095 ? (o - 7) / 8 : 4095]++;
        if (c) hist[3][(o - 7) / 8 < 4095 ? (o - 7) / 8 : 4095]++; firstpos[pos]++; break; } }
    if (best < 0) { fail++; printf("NO o<=%lld at p=%lld\n", OMAX, p); continue; }
    /* keep top 20 hardest */
    if (nw < 20) { worst[nw] = p; worsto[nw++] = best; }
    else { int mi = 0; for (int i = 1; i < 20; i++) if (worsto[i] < worsto[mi]) mi = i; if (best > worsto[mi]) { worst[mi] = p; worsto[mi] = best; } }
  }
  printf("%s <= %lld: %lld  failures(o>%lld): %lld  mode %s\n", sq ? "odd squares" : "primes p=1(8)", X, cnt, OMAX, fail, interior ? "interior" : "formal");
  printf("first-success position counts (ties -> Ph>Pc>Pm): Ph %lld Pc %lld Pm %lld\n", firstpos[0], firstpos[1], firstpos[2]);
  printf("o*: count | #with Ph-witness #Pc #Pm at that o\n");
  for (int i = 0; i < 4096; i++) if (hist[0][i]) printf("o=%d: %lld | %lld %lld %lld\n", 8 * i + 7, hist[0][i], hist[1][i], hist[2][i], hist[3][i]);
  printf("hardest:"); for (int i = 0; i < nw; i++) printf(" %lld:%lld", worst[i], worsto[i]); printf("\n");
  return 0; }
