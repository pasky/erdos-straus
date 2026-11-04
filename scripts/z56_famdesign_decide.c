// z56 FAMDESIGN: fast exhaustive *decision* of hits_F(p) >= 1 for the families HC = {C <= log^2 p}, H3 = {64C^3 <= p},
// F4 = A ∩ G, F4L = A ∩ G_{1/15} (Z56_FAMDESIGN.md §1), over all primes p = 1 (4) in [A, B] (segmented sieve).
// Method: scan levels C = 1, 2, ... (each level: all (P, Q), P <= Q, 4PQC - P - Q = p, by testing (4PC-1) | p + P for
// P <= sqrt-range); every solution with 64C^3 <= p lies in G (proof in the memo §1), so a hit at such a level decides
// HC/H3/F4 (and F4L if min(o,e)^15 > p). Stop when all four are decided positive. If the level scan up to
// C = floor(cbrt(p/64)) leaves F4 or F4L undecided, fall back to the exact full count (z56scan's enumeration).
// Output: one line per prime where some of {all, HC, H3, F4, F4L} is zero: "p all HC H3 F4 F4L" (exact full counts),
// and to stderr a summary "N=... zeros: all HC H3 F4 F4L".  Build: gcc -O2 -o /tmp/z56dec scripts/z56_famdesign_decide.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll; typedef __int128 i128;
static inline int divides(ll m, ll n) { ll q = (ll)((double)n / (double)m + 0.5); return q * m == n; }
static long double Ln;
// full count (same enumeration as z56_famdesign_scan.c), returning counts all, HC, H3, F4, F4L
static void full(ll n, long *c) {
  for (int i = 0; i < 5; i++) c[i] = 0;
  #define REC(o_, e_, C_) do { ll o = (o_), e = (e_), CC = (C_); ll P = o < e ? o : e, Q = o < e ? e : o; \
    long double lP = logl((long double)P), lQ = logl((long double)Q); int G = 4 * lQ > Ln + lP, lam = 15 * lP > Ln; \
    c[0]++; if ((long double)CC <= Ln * Ln) c[1]++; if ((i128)64 * CC * CC * CC <= n) c[2]++; if (G) c[3]++; if (G && lam) c[4]++; } while (0)
  for (ll P = 1; 4 * P * P * P - 2 * P <= n; P++)
    for (ll Q = P; ; Q++) { i128 lhs = (i128)4 * P * Q * Q - P - Q; if (lhs > n) break; ll m = 4 * P * Q, N = n + P + Q;
      if (divides(m, N)) { ll C = N / m; if (C >= Q) REC((P & 1) ? P : Q, (P & 1) ? Q : P, C); } }
  for (ll P = 1; 4 * P * P * P - P <= n + P; P++)
    for (ll C = P; ; C++) { ll m = 4 * P * C - 1; if ((i128)C * m >= n + P) break; ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q > C) REC((P & 1) ? P : Q, (P & 1) ? Q : P, C); } }
  for (ll C = 1; ; C++) { ll P0 = C + 1; if ((i128)P0 * (4 * P0 * C - 1) > n + P0) break;
    for (ll P = P0; ; P++) { ll m = 4 * P * C - 1; if ((i128)P * m > n + P) break; ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q >= P) REC((P & 1) ? P : Q, (P & 1) ? Q : P, C); } } }
}
// level scan: returns bitmask of decided-positive families (1=HC, 2=H3, 4=F4, 8=F4L) using levels C <= cmax
static int levels(ll n, ll cmax) {
  int got = 0; long double L2 = Ln * Ln;
  for (ll C = 1; C <= cmax; C++) {
    // all P >= 1 with P <= Q: P(4PC - 1) <= n + P
    for (ll P = 1; ; P++) { ll m = 4 * P * C - 1; if ((i128)P * m > n + P) break; ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q >= P) {
        got |= 2 | 4; if ((long double)C <= L2) got |= 1;
        if (15 * logl((long double)P) > Ln) got |= 8;
        if (got == 15) return got; } } }
  }
  return got;
}
int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "usage: A B\n"); return 1; }
  ll A = atoll(argv[1]), B = atoll(argv[2]); if (A < 1000) A = 1000;
  ll sq = (ll)sqrtl((long double)B) + 2; char *small = calloc(sq + 1, 1); int *pr = malloc(sizeof(int) * (sq + 1)); int np = 0;
  for (ll i = 2; i <= sq; i++) if (!small[i]) { pr[np++] = (int)i; for (ll j = i * i; j <= sq; j += i) small[j] = 1; }
  const ll SEG = 1 << 22; char *seg = malloc(SEG);
  long N = 0, z[5] = {0};
  for (ll lo = A; lo <= B; lo += SEG) {
    ll hi = lo + SEG - 1; if (hi > B) hi = B;
    for (ll i = 0; i <= hi - lo; i++) seg[i] = 1;
    for (int k = 0; k < np; k++) { ll q = pr[k]; if (q * q > hi) break; ll s = ((lo + q - 1) / q) * q; if (s < q * q) s = q * q;
      for (ll j = s; j <= hi; j += q) seg[j - lo] = 0; }
    for (ll p = lo; p <= hi; p++) {
      if (!seg[p - lo] || (p & 3) != 1) continue;
      N++; Ln = logl((long double)p);
      ll cmax = (ll)cbrtl((long double)p / 64.0L); while ((i128)64 * (cmax + 1) * (cmax + 1) * (cmax + 1) <= p) cmax++;
      while (cmax > 0 && (i128)64 * cmax * cmax * cmax > p) cmax--;
      int got = levels(p, cmax);
      if (got == 15) continue;
      long c[5]; full(p, c);
      int anyz = 0; for (int i = 0; i < 5; i++) if (c[i] == 0) { z[i]++; anyz = 1; }
      if (anyz) { printf("%lld %ld %ld %ld %ld %ld\n", p, c[0], c[1], c[2], c[3], c[4]); fflush(stdout); }
    }
  }
  fprintf(stderr, "# [%lld,%lld] N=%ld zeros: all=%ld HC=%ld H3=%ld F4=%ld F4L=%ld\n", A, B, N, z[0], z[1], z[2], z[3], z[4]);
  return 0;
}
