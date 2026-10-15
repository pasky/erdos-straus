// (helpers copied from z7_types.c) O231 type census of unforced words at n = 1 (mod 8) (primes by default; ALL=1 env -> all odd non-squares n = 1 (8)).
// Words (t,u,v) positive, tuv-u-v=n; A=tu-1, B=tv-1; sides N_t=tn+1=AB, N_u=n+u=Av, N_v=n+v=Bu; psi=Jacobi(./n).
// clean(x): no prime factor r with psi(r)=-1.  U = #words with all sides unclean; U2 = #words with A and B both unclean
// (A|N_t,N_u ; B|N_t,N_v so U2 <= U); Nm = #chi=-1 (chi=psi(A)); Nm <= U2 <= U.
// Output per n: n N Nm U2 U minmin_unforced c1 c2 c2p1   (c1,c2,c2p1 = clean flags of n+1, n+2, 2n+1; minmin = min(t,u,v) min over unforced words, 0 if none)
// usage: z7_types LO HI   (env ALL=1 for composites too)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulm(u64 a, u64 b, u64 m) { return (u128)a * b % m; }
static u64 powm(u64 a, u64 e, u64 m) { u64 r = 1; a %= m; while (e) { if (e & 1) r = mulm(r, a, m); a = mulm(a, a, m); e >>= 1; } return r; }
static int jac(long long a, long long n) { a %= n; if (a < 0) a += n; int r = 1; while (a) { while (!(a & 1)) { a >>= 1; long long m = n & 7; if (m == 3 || m == 5) r = -r; } long long t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) r = -r; a %= n; } return n == 1 ? r : 0; }
static u64 gcdu(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static int isprp(u64 n) { if (n < 2) return 0; static const u64 B[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (int i = 0; i < 12; i++) { if (n % B[i] == 0) return n == B[i]; }
    u64 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
    for (int i = 0; i < 12; i++) { u64 x = powm(B[i], d, n); if (x == 1 || x == n - 1) continue; int ok = 0;
        for (int r = 1; r < s; r++) { x = mulm(x, x, n); if (x == n - 1) { ok = 1; break; } } if (!ok) return 0; } return 1; }
static u64 rho(u64 n) { if (n % 2 == 0) return 2; for (u64 c = 1;; c++) { u64 x = 2, y = 2, d = 1;
    while (d == 1) { x = (mulm(x, x, n) + c) % n; y = (mulm(y, y, n) + c) % n; y = (mulm(y, y, n) + c) % n; d = gcdu(x > y ? x - y : y - x, n); }
    if (d != n) return d; } }
static int *spf; static long long M;
static int clean_rec(u64 x, long long p) { if (x == 1) return 1;
    if ((long long)x <= M) { while (x > 1) { int r = spf[x]; if (jac(r, p) == -1) return 0; while (x % r == 0) x /= r; } return 1; }
    if (isprp(x)) return jac((long long)(x % (u64)p), p) != -1;
    u64 d = rho(x); return clean_rec(d, p) && clean_rec(x / d, p); }
static int clean(u64 x, long long p) { for (u64 r = 2; r < 100; r++) { if (x % r) continue; if (jac(r, p) == -1) return 0; while (x % r == 0) x /= r; } return clean_rec(x, p); }
int main(int argc, char **argv) {
    // O231 §3: Landau depth K(p) = max K such that p+s and s p+1 are clean for all 1 <= s <= K (primes p = 1 (8)).
    // Output: p K(p)  for every prime p = 1 (8) in [LO,HI) with K(p) >= KMIN; histogram on stderr.  usage: z7_depth LO HI KMIN
    long long LO = atoll(argv[1]), HI = atoll(argv[2]), KMIN = atoll(argv[3]); long long hist[64] = {0};
    M = 2 * HI + 100; spf = calloc(M + 1, sizeof(int));
    for (long long i = 2; i <= M; i++) if (!spf[i]) for (long long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    for (long long p = LO; p < HI; p++) { if (p % 8 != 1 || spf[p] != p) continue;
        int K = 0; while (K < 60 && clean((u64)(p + K + 1), p) && clean((u64)(K + 1) * p + 1, p)) K++;
        hist[K]++; if (K >= KMIN) printf("%lld %d\n", p, K); }
    for (int k = 0; k < 64; k++) if (hist[k]) fprintf(stderr, "K=%d: %lld\n", k, hist[k]);
    return 0; }
