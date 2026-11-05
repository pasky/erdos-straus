// z58 WITNESS: least witnesses of (MS) in four orderings, per prime p (or any odd n).
//   d_min : least d ≡ 3 (4), d ≥ 3, with r := (−n mod d) ≥ 1 and r | (d+1)/4      (raw d-form; gives u=r, C, B)
//   u_min : least u ≥ 1 such that n+u has a divisor d ≡ −1 (mod 4u)                (u-form; = min over sols of min(u,B))
//   C_min : least C ≥ 1 such that 4Cn+1 has a divisor d ≡ −1 (mod 4C)              (divisor/level form)
//   q_min : least pair modulus q = 4uB, gcd(u,B)=1, with n ≡ −(u+B) (mod 4uB)        (pair form; u+B odd automatically for n odd)
//   n_p   : least prime ℓ with (n/ℓ) = −1 (Jacobi; for prime n ≡ 1 (4) = least QNR mod n by reciprocity)
// Lemma A.1 (Z57_SYNTH): all four exist iff R(n) ≥ 1.  Caps: d-loop to DCAP (then d_min reported as -1 = ">cap"),
// u to UCAP, C to CCAP, q to QCAP (reported -1 if not found below cap).  For n with R(n)=0 all are -1.
// Factoring: trial division to 1000, Miller–Rabin (deterministic bases, n < 3.3e24), Pollard–Brent rho; n+u, 4Cn+1 < 2^63.
// Modes:  z58scan A B [mode]      all primes p ≡ 1 (4) in [A,B]  (A,B ≤ 4e9 for the segmented prime sieve)
//         z58scan -               read integers n from stdin (any odd n; controls)
// Output per n: n  n%840  inM  d_min u_d C_d B_d  u_min d_u  C_min d_C  q_min uq Bq  n_p  [mode=all lines]
// In range mode with mode "S" only a summary (+hard list) is printed (see bottom).
// Build: gcc -O2 -o /tmp/z58scan scripts/z58_witness_scan.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef unsigned long long ull; typedef long long ll; typedef unsigned __int128 u128;

static ull DCAP = 400000000ULL, UCAP = 100000, CCAP = 100000, QCAP = 100000000ULL;
static ull mulmod(ull a, ull b, ull m) { return (ull)((u128)a * b % m); }
static ull powmod(ull a, ull e, ull m) { ull r = 1 % m; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int isprime(ull n) {
  if (n < 2) return 0; static const ull sp[] = {2,3,5,7,11,13,17,19,23,29,31,37};
  for (int i = 0; i < 12; i++) { if (n % sp[i] == 0) return n == sp[i]; }
  ull d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
  for (int i = 0; i < 12; i++) { ull x = powmod(sp[i], d, n); if (x == 1 || x == n - 1) continue; int ok = 0;
    for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } } if (!ok) return 0; }
  return 1;
}
static ull gcdu(ull a, ull b) { while (b) { ull t = a % b; a = b; b = t; } return a; }
static ull rho(ull n) {
  if (!(n & 1)) return 2;
  for (ull c = 1;; c++) { ull y = 2, x, g = 1, q = 1, ys = 2; ull m = 64, r = 1;
    do { x = y; for (ull i = 0; i < r; i++) y = (mulmod(y, y, n) + c) % n; ull k = 0;
      do { ys = y; for (ull i = 0; i < m && i < r - k; i++) { y = (mulmod(y, y, n) + c) % n; q = mulmod(q, x > y ? x - y : y - x, n); }
        g = gcdu(q, n); k += m; } while (k < r && g == 1); r <<= 1; } while (g == 1);
    if (g == n) { do { ys = (mulmod(ys, ys, n) + c) % n; g = gcdu(x > ys ? x - ys : ys - x, n); } while (g == 1); }
    if (g != n) return g; }
}
// factor into distinct primes P[] with exponents E[]
static int nf; static ull P[64]; static int E[64];
static void addp(ull p) { for (int i = 0; i < nf; i++) if (P[i] == p) { E[i]++; return; } P[nf] = p; E[nf] = 1; nf++; }
static void fac_rec(ull n) { if (n == 1) return; if (isprime(n)) { addp(n); return; } ull g = rho(n); fac_rec(g); fac_rec(n / g); }
static void factor(ull n) { nf = 0; for (ull p = 2; p < 1000 && p * p <= n; p += (p == 2 ? 1 : 2)) while (n % p == 0) { addp(p); n /= p; }
  if (n > 1) fac_rec(n); }
// does m (factored in P,E) have a divisor ≡ −1 (mod M)?  divisors coprime to M only.  returns least such divisor or 0.
static ull divcls(ull M) {
  // enumerate divisors (coprime to M) iteratively
  static ull dv[200000]; int nd = 1; dv[0] = 1;
  for (int i = 0; i < nf; i++) { if (gcdu(P[i], M) != 1) continue; int cur = nd; ull pk = 1;
    for (int e = 1; e <= E[i]; e++) { pk *= P[i]; for (int j = 0; j < cur; j++) { if (nd >= 200000) { fprintf(stderr, "too many divisors\n"); exit(1); } dv[nd++] = dv[j] * pk; } } }
  ull best = 0; for (int j = 0; j < nd; j++) if (dv[j] % M == M - 1 && (best == 0 || dv[j] < best)) best = dv[j];
  return best;
}
static int jacobi(ull a, ull n) { // n odd positive
  a %= n; int t = 1; while (a) { while (!(a & 1)) { a >>= 1; ull r = n & 7; if (r == 3 || r == 5) t = -t; }
    ull tmp = a; a = n; n = tmp; if ((a & 3) == 3 && (n & 3) == 3) t = -t; a %= n; } return n == 1 ? t : 0;
}
static const int Mcls[6] = {1, 121, 169, 289, 361, 529};
static int inM(ull n) { int r = n % 840; for (int i = 0; i < 6; i++) if (r == Mcls[i]) return 1; return 0; }

typedef struct { ll dmin, ud, Cd, Bd, umin, du, Cmin, dC, qmin, uq, Bq, np; } W;
static W witness(ull n) {
  W w; memset(&w, 0xff, sizeof w); // all -1
  // d-form
  for (ull d = 3; d <= DCAP && 3 * d <= 4 * n + 1; d += 4) { ull r = (d - n % d) % d; if (r == 0) continue; ull h = (d + 1) / 4;
    if (h % r == 0) { w.dmin = d; w.ud = r; w.Cd = h / r; w.Bd = (n + r) / d; break; } }
  int exhausted = (w.dmin < 0 && 3 * (DCAP + 4) > 4 * n + 1);
  if (exhausted) goto np_only; // R(n) = 0 certified by the exhaustive d-loop
  // u-form
  for (ull u = 1; u <= UCAP && 3 * u <= n + 1; u++) { factor(n + u); ull d = divcls(4 * u); if (d) { w.umin = u; w.du = d; break; } }
  // C-form
  for (ull C = 1; C <= CCAP; C++) { if (4 * C > n + 1) break; factor(4 * C * n + 1); ull d = divcls(4 * C); if (d) { w.Cmin = C; w.dC = d; break; } }
  // pair form: q = 4uB, gcd(u,B)=1, n + u + B ≡ 0 mod 4uB; search q ≤ Q with Q doubling up to QCAP
  for (ull Q = 1024; ; Q *= 4) { if (Q > QCAP) Q = QCAP; ll best = -1, bu = 0, bB = 0;
    for (ull u = 1; 4 * u * u <= Q; u++) for (ull B = u; 4 * u * B <= Q; B++) { if ((n + u + B) % (4 * u * B)) continue;
        if (gcdu(u, B) != 1) continue; if (best < 0 || (ll)(4 * u * B) < best) { best = 4 * u * B; bu = u; bB = B; } }
    if (best > 0) { w.qmin = best; w.uq = bu; w.Bq = bB; break; } if (Q >= QCAP || Q > 4 * n + 8) break; }
  np_only:
  for (ull l = 2;; l++) { if (!isprime(l)) continue; if (l == 2) { if ((n & 7) == 3 || (n & 7) == 5) { w.np = 2; break; } else continue; }
    if (n % l == 0) continue; if (jacobi(n % l, l) == -1) { w.np = l; break; } if (l > 100000) break; }
  return w;
}
static void pr(ull n, W w) {
  printf("%llu %llu %d %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld\n", n, n % 840, inM(n), w.dmin, w.ud, w.Cd, w.Bd,
         w.umin, w.du, w.Cmin, w.dC, w.qmin, w.uq, w.Bq, w.np); }
int main(int argc, char **argv) {
  char *e;
  if ((e = getenv("DCAP"))) DCAP = strtoull(e, 0, 10);
  if ((e = getenv("UCAP"))) UCAP = strtoull(e, 0, 10);
  if ((e = getenv("CCAP"))) CCAP = strtoull(e, 0, 10);
  if ((e = getenv("QCAP"))) QCAP = strtoull(e, 0, 10);
  printf("# n n%%840 inM d_min u_d C_d B_d u_min d_u C_min d_C q_min u_q B_q n_p\n");
  if (argc >= 2 && !strcmp(argv[1], "-")) { ull n; while (scanf("%llu", &n) == 1) { pr(n, witness(n)); fflush(stdout); } return 0; }
  ull A = strtoull(argv[1], 0, 10), Bh = strtoull(argv[2], 0, 10);
  // segmented sieve
  ull lim = (ull)sqrt((double)Bh) + 2; char *sc = calloc(lim + 1, 1); int *sp = malloc(sizeof(int) * (lim / 2 + 10)); int ns = 0;
  for (ull i = 2; i <= lim; i++) if (!sc[i]) { sp[ns++] = i; for (ull j = i * i; j <= lim; j += i) sc[j] = 1; }
  ull S = 1 << 22; char *seg = malloc(S);
  for (ull lo = A; lo <= Bh; lo += S) { ull hi = lo + S - 1; if (hi > Bh) hi = Bh; memset(seg, 0, S);
    for (int i = 0; i < ns; i++) { ull p = sp[i]; if (p * p > hi) break; ull st = (lo + p - 1) / p * p; if (st < p * p) st = p * p;
      for (ull j = st; j <= hi; j += p) seg[j - lo] = 1; }
    for (ull n = lo; n <= hi; n++) { if (seg[n - lo] || n < 5 || (n & 3) != 1) continue; pr(n, witness(n)); } }
  return 0;
}
