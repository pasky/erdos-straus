// z58 DISPROOF: targeted (★)-zero search engine.  For each prime p = 1 (4) produced by a design generator, compute
//   S_K   := #(★) solutions (u,B,C) (ordered) with C <= K (complete levels; exact)
//   S_Ke  := the C-even part of S_K
//   flags: R>0, R8>0 (C even), Rodd>0 (C odd), H3>0 (some level C with 64C^3 <= p) decided by level scans with early exit;
//   if any of the four is undecided after the level scan up to cmax = floor(cbrt(p/64)), the exact full enumeration
//   (three loops of scripts/z56_famdesign_decide.c, by which of P=min(u,B), Q=max(u,B), C is smallest) gives exact
//   R, R8, R_G* (G* = {(o,e): max(o,e)^4 > min(o,e) p}, o/e = odd/even member of {u,B}).
//   dmin  := least d = 3 (4) with (-p mod d) | (d+1)/4  (raw (MS) witness; searched to DMAX, else -1)
// Output line: p S_K S_Ke dmin zR z8 zodd zH3 [R R8 RG] (z* = 1 if that count is ZERO; exact counts only if full ran,
// else "-").  Summary to stderr.
// Generators (argv[1]):
// Env: K (default 16), EXACT=1 (always run the full enumeration: exact R, R8, R_G* for every prime).
//   ap   A COUNT Q a z  : primes p >= A, p = a (mod Q) (p = 1 mod 4 required of a,Q), with (l/p) = +1 for every odd
//                         prime l <= z, l not dividing Q (z = 0: no filter); first COUNT of them.
//   nsq  A COUNT Q J z  : p = m^2 + Q*j, m >= sqrt(A) ascending, gcd(m,2Q)=1, J0 < j <= J0 + J (env J0, default 0: "near-squares"), same filter.
//   list               : primes read from stdin (one per line; primality re-checked).
// Build: gcc -O2 -o /tmp/z58eng scripts/z58_disproof_eng.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128; typedef unsigned __int128 u128;
static int K = 16; static ll DMAX = 20000000; static int EXACT = 0;
static inline int divides(ll m, ll n) { ll q = (ll)((double)n / (double)m + 0.5); return q * m == n; }
static ull mulmod(ull a, ull b, ull m) { return (u128)a * b % m; }
static ull powmod(ull a, ull e, ull m) { ull r = 1; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int isprime(ull n) {
  if (n < 2) return 0; static const ull sp[] = {2,3,5,7,11,13,17,19,23,29,31,37};
  for (int i = 0; i < 12; i++) { if (n == sp[i]) return 1; if (n % sp[i] == 0) return 0; }
  ull d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
  for (int i = 0; i < 12; i++) { ull x = powmod(sp[i], d, n); if (x == 1 || x == n - 1) continue; int ok = 0;
    for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } } if (!ok) return 0; }
  return 1;   // deterministic for n < 3.3e24 with these 12 bases
}
static int legendre(ll a, ll l) { ll r = (ll)powmod((ull)((a % l + l) % l), (ull)(l - 1) / 2, (ull)l); return r == 1 ? 1 : (r == 0 ? 0 : -1); }
static int gtest(ll P, ll Q, ll n) { if (Q > 3000000000LL) return 1; i128 q2 = (i128)Q * Q; return q2 * q2 > (i128)P * n; }
static void full(ll n, long *R, long *R8, long *RG) {
  *R = *R8 = *RG = 0;
  #define REC(P_, Q_, C_) do { (*R) += 2; if (((C_) & 1) == 0) (*R8) += 2; if (gtest((P_), (Q_), n)) (*RG) += 2; } while (0)
  for (ll P = 1; 4 * P * P * P - 2 * P <= n; P++)
    for (ll Q = P; ; Q++) { i128 lhs = (i128)4 * P * Q * Q - P - Q; if (lhs > n) break; ll m = 4 * P * Q, N = n + P + Q;
      if (divides(m, N)) { ll C = N / m; if (C >= Q) REC(P, Q, C); } }
  for (ll P = 1; 4 * P * P * P - P <= n + P; P++)
    for (ll C = P; ; C++) { ll m = 4 * P * C - 1; if ((i128)C * m >= n + P) break; ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q > C) REC(P, Q, C); } }
  for (ll C = 1; ; C++) { ll P0 = C + 1; if ((i128)P0 * (4 * P0 * C - 1) > n + P0) break;
    for (ll P = P0; ; P++) { ll m = 4 * P * C - 1; if ((i128)P * m > n + P) break; ll N = n + P;
      if (divides(m, N)) { ll Q = N / m; if (Q >= P) REC(P, Q, C); } } }
}
// number of ordered solutions at level C (all u <= B pairs, x2; u != B always for odd n)
static long level(ll n, ll C) { long c = 0;
  for (ll P = 1; ; P++) { ll m = 4 * P * C - 1; if ((i128)P * m > n + P) break;
    if (divides(m, n + P)) { ll Q = (n + P) / m; if (Q >= P) c += 2; } }
  return c; }
static ll dmin(ll p) { for (ll d = 3; d <= DMAX; d += 4) { ll r = (d - p % d) % d; if (r && ((d + 1) / 4) % r == 0) return d; } return -1; }
static long N = 0, nz[4] = {0}, nfull = 0; static double sumS = 0;
static void process(ll p) {
  ll cmax = (ll)cbrtl((long double)p / 64.0L); while ((i128)64 * (cmax + 1) * (cmax + 1) * (cmax + 1) <= p) cmax++;
  while (cmax > 0 && (i128)64 * cmax * cmax * cmax > p) cmax--;
  long S = 0, Se = 0; int hR = 0, h8 = 0, ho = 0, hH = 0;
  for (ll C = 1; C <= K; C++) { long c = level(p, C); S += c; if (!(C & 1)) Se += c;
    if (c) { hR = 1; if (C <= cmax) hH = 1; if (C & 1) ho = 1; else h8 = 1; } }
  for (ll C = K + 1; C <= cmax && !(hR && h8 && ho && hH); C++) {
    if ((C & 1) ? ho : h8) continue;      // only need the missing parity (H3 is decided by any hit at C <= cmax)
    long c = level(p, C); if (c) { hR = hH = 1; if (C & 1) ho = 1; else h8 = 1; } }
  if (!hH && (hR)) {}                    // H3 undecided only if no hit at all in levels <= min(K,cmax): handled by full
  long R = -1, R8 = -1, RG = -1;
  if (EXACT || !(hR && h8 && ho && hH)) { full(p, &R, &R8, &RG); nfull++; hR = R > 0; h8 = R8 > 0; ho = R - R8 > 0; }
  ll dm = dmin(p);
  N++; sumS += S; if (!hR) nz[0]++; if (!h8) nz[1]++; if (!ho) nz[2]++; if (!hH) nz[3]++;
  if (R >= 0) printf("%lld %ld %ld %lld %d %d %d %d %ld %ld %ld\n", p, S, Se, dm, !hR, !h8, !ho, !hH, R, R8, RG);
  else printf("%lld %ld %ld %lld %d %d %d %d - - -\n", p, S, Se, dm, !hR, !h8, !ho, !hH);
  fflush(stdout);
}
static int oddprimes[200], nop = 0;
static int filt(ll p, ll Q, int z) { for (int i = 0; i < nop && oddprimes[i] <= z; i++) { int l = oddprimes[i]; if (Q % l == 0) continue; if (legendre(p, l) != 1) return 0; } return 1; }
int main(int argc, char **argv) {
  for (int q = 3; q < 1000 && nop < 200; q += 2) { int pr = 1; for (int t = 3; t * t <= q; t += 2) if (q % t == 0) pr = 0; if (pr) oddprimes[nop++] = q; }
  if (getenv("K")) K = atoi(getenv("K")); if (getenv("EXACT")) EXACT = atoi(getenv("EXACT"));
  if (argc < 2) { fprintf(stderr, "usage: see header\n"); return 1; }
  printf("# z58eng %s", argv[1]); for (int i = 2; i < argc; i++) printf(" %s", argv[i]); printf(" K=%d EXACT=%d\n# p S_K S_Ke dmin zR z8 zodd zH3 R R8 RG\n", K, EXACT);
  if (!strcmp(argv[1], "ap")) {
    ll A = atoll(argv[2]); long cnt = atol(argv[3]); ll Q = atoll(argv[4]), a = atoll(argv[5]); int z = atoi(argv[6]);
    ll p = A + (((a - A) % Q) + Q) % Q; long got = 0;
    for (; got < cnt; p += Q) { if ((p & 3) != 1) { fprintf(stderr, "class not 1 mod 4\n"); return 2; }
      if (!filt(p, Q, z) || !isprime((ull)p)) continue; process(p); got++; }
  } else if (!strcmp(argv[1], "nsq")) {
    ll A = atoll(argv[2]); long cnt = atol(argv[3]); ll Q = atoll(argv[4]); ll J = atoll(argv[5]); int z = atoi(argv[6]);
    ll m = (ll)sqrtl((long double)A); long got = 0;
    for (; got < cnt; m++) { ll g = m, h = 2 * Q; while (h) { ll t = g % h; g = h; h = t; } if (g != 1) continue;
      ll J0 = getenv("J0") ? atoll(getenv("J0")) : 0;
      for (ll j = J0 + 1; j <= J0 + J && got < cnt; j++) { ll p = m * m + Q * j; if ((p & 3) != 1) continue;
        if (!filt(p, Q, z) || !isprime((ull)p)) continue; process(p); got++; } }
  } else if (!strcmp(argv[1], "list")) {
    ll p; while (scanf("%lld", &p) == 1) { if (!isprime((ull)p) || (p & 3) != 1) { fprintf(stderr, "skip %lld\n", p); continue; } process(p); }
  }
  fprintf(stderr, "# N=%ld meanS=%.3f zeros R=%ld R8=%ld Rodd=%ld H3=%ld full=%ld\n", N, N ? sumS / N : 0, nz[0], nz[1], nz[2], nz[3], nfull);
  return 0;
}
