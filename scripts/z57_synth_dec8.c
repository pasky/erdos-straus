// z57 SYNTH: exhaustive decision of R8(p) >= 1 (a (★) solution 4uBC - u - B = p with C EVEN, i.e. a solution of the
// numerator-8 line 8uBC' - u - B = p) for every prime p = 1 (4) in [A, B]; prints every prime with R8(p) = 0 together
// with its full (★) count R(p).  Method: (1) level scan C = 2, 4, ... with 64 C^3 <= p (all (u,B), u <= B, at level C via
// (4uC - 1) | p + u, u(4uC - 1) <= p + u), early exit at the first hit; (2) if undecided, the exact full enumeration of all
// (★) solutions (the three loops of scripts/z56_famdesign_scan.c / z56_famdesign_decide.c, by which of P = min(u,B),
// Q = max(u,B), C is smallest; cost ~ 3 p^{2/3}) and R8 = #{C even}.  OpenMP over segment primes.
// Build: gcc -O2 -fopenmp -o /tmp/z57dec8 scripts/z57_synth_dec8.c -lm ; run: /tmp/z57dec8 A B > out (summary on stderr)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll; typedef __int128 i128;
static inline int divides(ll m, ll n) { ll q = (ll)((double)n / (double)m + 0.5); return q * m == n; }
// full enumeration: returns R (all solutions, both orders counted as 2 per unordered {P,Q}, P != Q always) and *r8
static long full(ll n, long *r8) {
  long R = 0; *r8 = 0;
  #define REC(C_) do { R += 2; if (((C_) & 1) == 0) *r8 += 2; } while (0)
  for (ll P = 1; 4 * P * P * P - 2 * P <= n; P++)
    for (ll Q = P; ; Q++) { i128 lhs = (i128)4 * P * Q * Q - P - Q; if (lhs > n) break; ll m = 4 * P * Q, N = n + P + Q;
      if (divides(m, N)) { ll C = N / m; if (C >= Q) REC(C); } }
  for (ll P = 1; 4 * P * P * P - P <= n + P; P++)
    for (ll C = P; ; C++) { ll m = 4 * P * C - 1; if ((i128)C * m >= n + P) break; ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q > C) REC(C); } }
  for (ll C = 1; ; C++) { ll P0 = C + 1; if ((i128)P0 * (4 * P0 * C - 1) > n + P0) break;
    for (ll P = P0; ; P++) { ll m = 4 * P * C - 1; if ((i128)P * m > n + P) break; ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q >= P) REC(C); } } }
  return R;
}
static int levelscan_even(ll n) {
  for (ll C = 2; C <= n / 64 / C / C; C += 2)
    for (ll P = 1; ; P++) { ll m = 4 * P * C - 1; if ((i128)P * m > n + P) break;
      if (divides(m, n + P)) { ll Q = (n + P) / m; if (Q >= P) return 1; } }
  return 0;
}
int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "usage: A B\n"); return 1; }
  ll A = atoll(argv[1]), B = atoll(argv[2]); if (A < 1000) A = 1000;
  ll sq = (ll)sqrtl((long double)B) + 2; char *small = calloc(sq + 1, 1); int *pr = malloc(sizeof(int) * (sq + 1)); int np = 0;
  for (ll i = 2; i <= sq; i++) if (!small[i]) { pr[np++] = (int)i; for (ll j = i * i; j <= sq; j += i) small[j] = 1; }
  const ll SEG = 1 << 22; char *seg = malloc(SEG); ll *cand = malloc(sizeof(ll) * SEG);
  long N = 0, Z = 0, nfull = 0;
  for (ll lo = A; lo <= B; lo += SEG) {
    ll hi = lo + SEG - 1; if (hi > B) hi = B;
    for (ll i = 0; i <= hi - lo; i++) seg[i] = 1;
    for (int k = 0; k < np; k++) { ll q = pr[k]; if (q * q > hi) break; ll s = ((lo + q - 1) / q) * q; if (s < q * q) s = q * q;
      for (ll j = s; j <= hi; j += q) seg[j - lo] = 0; }
    long nc = 0; for (ll p = lo; p <= hi; p++) if (seg[p - lo] && (p & 3) == 1) cand[nc++] = p;
    #pragma omp parallel for schedule(dynamic, 64) reduction(+:N, Z, nfull)
    for (long i = 0; i < nc; i++) {
      ll p = cand[i]; N++;
      if (levelscan_even(p)) continue;
      nfull++; long r8; long R = full(p, &r8);
      if (r8 == 0) { Z++;
        #pragma omp critical
        { printf("%lld %ld %ld\n", p, R, r8); fflush(stdout); } }
    }
  }
  fprintf(stderr, "range [%lld, %lld]: primes(1 mod 4)=%ld full-enumerations=%ld R8-zeros=%ld\n", A, B, N, nfull, Z);
  return 0;
}
