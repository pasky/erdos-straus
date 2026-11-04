// z56 FAMDESIGN: enumerate ALL (★) solutions (o, e, C) of p = 4·o·e·C − o − e (o odd, e even) at each n, and count them
// in the candidate families of Z56_FAMDESIGN.md (counts are #solutions = R_𝔊/2, i.e. CROSSF's "hits").
// Enumeration (every triple exactly once; P = min(o,e), Q = max(o,e)):
//   1a  P <= Q <= C : loop P, Q (4PQ^2 - P - Q <= n), test 4PQ | n + P + Q, C >= Q
//   1b  P <= C <  Q : loop P, C (C(4PC-1) < n + P),    test (4PC-1) | n + P, Q > C
//   2   C <  P <= Q : loop C, P (P(4PC-1) <= n + P),   test (4PC-1) | n + P, Q >= P
// Cost ~ 3 n^{2/3}. Divisibility by double-quotient test, exact for n < 2^53 (checked: n < 4e15 enforced).
// Families (columns):  all | F0 = CROSSF standard window (U-type) | F1 = U ∩ R1(1/15) | F2U = U ∩ G_{1/15} |
//   F2S = S ∩ G_{1/15} | F3U = U ∩ G | F3S = S ∩ G | F4 = A ∩ G | F4L = A ∩ G_{1/15} | K = A \ G (Burgess corner)
//   U: o = 1 (4) squarefree, e = 2w, w squarefree;  S: o squarefree, odd part of e squarefree;  A: all.
//   G: Q^4 > P·n ;  G_{1/15}: G and P^15 > n ;  R1(1/15): e^4 > o·n and o^15 > n.
// Modes:  z56scan A B          all primes p = 1 (4) in [A, B]
//         z56scan A K S        first K primes p = 1 (4) at/after A, A+S, A+2S, ... (S > 0)
//         z56scan -            read integers n (odd, any) from stdin (controls: squares, test primes)
//   H3 = A ∩ {64 C^3 <= n} (whole C-layers, C <= n^{1/3}/4) | HC = A ∩ {C <= log^2 n}
// Output: "n all F0 F1 F2U F2S F3U F3S F4 F4L K H3 HC" per line.
// Build: gcc -O2 -o /tmp/z56scan scripts/z56_famdesign_scan.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128;

static int *primes, nprimes;
static void sieve(int lim) {
  char *c = calloc(lim + 1, 1); primes = malloc(sizeof(int) * (lim / 2 + 10)); nprimes = 0;
  for (int i = 2; i <= lim; i++) { if (!c[i]) { primes[nprimes++] = i; for (ll j = (ll)i * i; j <= lim; j += i) c[j] = 1; } }
  free(c);
}
static ull mulmod(ull a, ull b, ull m) { return (ull)((i128)a * b % m); }
static ull powmod(ull a, ull e, ull m) { ull r = 1; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int isprime(ull n) {
  if (n < 2) return 0; static const ull bs[] = {2,3,5,7,11,13,17,19,23,29,31,37,41};
  for (int i = 0; i < 13; i++) { if (n % bs[i] == 0) return n == bs[i]; }
  ull d = n - 1; int s = 0; while ((d & 1) == 0) { d >>= 1; s++; }
  for (int i = 0; i < 13; i++) { ull x = powmod(bs[i], d, n); if (x == 1 || x == n - 1) continue; int ok = 0;
    for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } } if (!ok) return 0; }
  return 1;
}
static ll isqrt_ll(ll n) { ll r = (ll)sqrtl((long double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++; return r; }
// squarefree test: trial division by primes <= cbrt(n); the remaining cofactor has <= 2 prime factors (all > cbrt n),
// so it is non-squarefree iff it is a perfect square > 1.
static int sqfree(ll n) {
  for (int i = 0; i < nprimes; i++) { ll q = primes[i]; if (q * q * q > n) break; if (n % q == 0) { n /= q; if (n % q == 0) return 0; } }
  if (n > 1) { ll r = isqrt_ll(n); if (r * r == n) return 0; }
  return 1;
}

// exact integer membership tests (no floating point): Q^4 > P*n, P^15 > n
static int gtest(long long P, long long Q, long long n) { if (Q > 3000000000LL) return 1; __int128 q2 = (__int128)Q * Q; return q2 * q2 > (__int128)P * n; }
static int lamtest(long long P, long long n) { __int128 a = 1; for (int i = 0; i < 15; i++) { a *= P; if (a > n) return 1; } return a > n; }
static long long hccut(long long n) { long double L = logl((long double)n), s = L * L; if (fabsl(s - roundl(s)) < 1e-12L) { fprintf(stderr, "HC cutoff tie at %lld\n", n); exit(3); } return (long long)floorl(s); }
static inline int divides(ll m, ll n) { ll q = (ll)((double)n / (double)m + 0.5); return q * m == n; }

#define NF 12
static ll cU0, cU1, cY, cX, cHC; static long double Ln;
static void classify(ll n, ll o, ll e, ll C, long *cnt) {
  int k = 0; ll ep = e; while ((ep & 1) == 0) { ep >>= 1; k++; }
  int so = sqfree(o), se = sqfree(ep);
  int U = (o % 4 == 1) && so && k == 1 && se;
  int S = so && se;
  ll P = o < e ? o : e, Q = o < e ? e : o;
  int G = gtest(P, Q, n);
  int lam = lamtest(P, n);
  int R1 = gtest(o, e, n) && lamtest(o, n);
  int F0 = U && o > cU0 && o <= cU1 && (e / 2) > cY && (e / 2) <= cX;
  cnt[0]++;
  if (F0) cnt[1]++;
  if (U && R1) cnt[2]++;
  if (U && G && lam) cnt[3]++;
  if (S && G && lam) cnt[4]++;
  if (U && G) cnt[5]++;
  if (S && G) cnt[6]++;
  if (G) cnt[7]++;
  if (G && lam) cnt[8]++;
  if (!G) cnt[9]++;
  if (C <= n / 64 / C / C) cnt[10]++;                 // H3: 64C^3 <= n, overflow-free (all divisors of each layer)
  if (C <= cHC) cnt[11]++;                             // HC: polylog layer C <= floor(log^2 n)
}
static void count(ll n, long *cnt) {
  for (int i = 0; i < NF; i++) cnt[i] = 0;
  Ln = logl((long double)n);
  cHC = hccut(n);
  { double t = pow((double)n, 1.0 / 12) - 0.5; cU0 = (ll)floor(t + 0.5); if (cU0 < 1) cU0 = 1; }
  cU1 = (ll)(pow((double)n, 1.0 / 3) / 2); cY = (ll)pow((double)n, 1.0 / 3); cX = (ll)(pow((double)n, 2.0 / 3) / 4);
  while ((i128)8 * cU1 * cX > n) cX--;
  // 1a: P <= Q <= C
  for (ll P = 1; 4 * P * P * P - 2 * P <= n; P++) {
    for (ll Q = P; ; Q++) {
      i128 lhs = (i128)4 * P * Q * Q - P - Q; if (lhs > n) break;
      ll m = 4 * P * Q, N = n + P + Q;
      if (divides(m, N)) { ll C = N / m; if (C >= Q) { ll o = (P & 1) ? P : Q, e = (P & 1) ? Q : P; classify(n, o, e, C, cnt); } }
    }
  }
  // 1b: P <= C < Q
  for (ll P = 1; 4 * P * P * P - P <= n + P; P++) {
    for (ll C = P; ; C++) {
      ll m = 4 * P * C - 1; if ((i128)C * m >= n + P) break;
      ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q > C) { ll o = (P & 1) ? P : Q, e = (P & 1) ? Q : P; classify(n, o, e, C, cnt); } }
    }
  }
  // 2: C < P <= Q
  for (ll C = 1; ; C++) {
    ll P0 = C + 1; if ((i128)P0 * (4 * P0 * C - 1) > n + P0) break;
    for (ll P = P0; ; P++) {
      ll m = 4 * P * C - 1; if ((i128)P * m > n + P) break;
      ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q >= P) { ll o = (P & 1) ? P : Q, e = (P & 1) ? Q : P; classify(n, o, e, C, cnt); } }
    }
  }
}
static void emit(ll n) {
  long cnt[NF]; count(n, cnt);
  printf("%lld", n); for (int i = 0; i < NF; i++) printf(" %ld", cnt[i]); printf("\n");
}
int main(int argc, char **argv) {
  sieve(300000); // cbrt(4e15) < 1.6e5
  if (argc == 2 && argv[1][0] == '-') { ll n; while (scanf("%lld", &n) == 1) { if (n >= 4e15 || n < 3 || !(n & 1)) { fprintf(stderr, "skip %lld\n", n); continue; } emit(n); fflush(stdout); } return 0; }
  if (argc < 3) { fprintf(stderr, "usage: A B | A K S | -\n"); return 1; }
  ll A = atoll(argv[1]), B = atoll(argv[2]); ll S = argc > 3 ? atoll(argv[3]) : 0;
  if (S == 0) { if (B >= 4e15) return 1; for (ll p = A | 1; p <= B; p += 2) { if (p % 4 != 1 || !isprime(p)) continue; emit(p); } }
  else { for (ll k = 0; k < B; k++) { ll p = (A + k * S) | 1; while (p % 4 != 1 || !isprime(p)) p += 2; if (p >= 4e15) return 1; emit(p); fflush(stdout); } }
  return 0;
}
