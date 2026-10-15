// O231 (UNFORCED_WORDS.md): type census of unforced words at n = 1 (mod 8) (primes by default; ALL=1 env -> all odd non-squares n = 1 (8)).
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
    long long LO = atoll(argv[1]), HI = atoll(argv[2]); int ALL = getenv("ALL") != NULL; long long bad = 0, cnt = 0, u0 = 0;
    M = 2 * HI + 2 * (long long)sqrtl((long double)HI) + 100;
    spf = calloc(M + 1, sizeof(int));
    for (long long i = 2; i <= M; i++) if (!spf[i]) for (long long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    static long long divs[1 << 16];
    for (long long p = LO; p < HI; p++) {
        if (p % 8 != 1) continue;
        { long long r0 = (long long)sqrtl((long double)p); while (r0 * r0 > p) r0--; while ((r0 + 1) * (r0 + 1) <= p) r0++; if (r0 * r0 == p) continue; }
        if (!ALL && spf[p] != p) continue;
        cnt++;
        long long Nw = 0, Nm = 0, U = 0, U2 = 0, mm0 = 0;
        for (long long u = 1; (u - 2) * u <= p; u++) {
            long long mm = p + u; int nd = 1; divs[0] = 1;
            while (mm > 1) { long long r = spf[mm]; int e = 0; while (mm % r == 0) { mm /= r; e++; }
                int cur = nd; long long pk = 1; for (int k = 1; k <= e; k++) { pk *= r; for (int i = 0; i < cur; i++) divs[nd++] = divs[i] * pk; } }
            int cu = -1;
            for (int di = 0; di < nd; di++) { long long v = divs[di];
                if (v < u) continue;
                if ((p + u + v) % (u * v)) continue;
                long long t = (p + u + v) / (u * v);
                long long A = t * u - 1, B = t * v - 1;
                int c = jac(A, p);
                int mult = (u == v) ? 1 : 2;
                if (cu < 0) cu = clean((u64)(p + u), p);
                int ct = clean((u64)t * p + 1, p), cv = clean((u64)(p + v), p);
                Nw += mult; if (c == -1) Nm += mult;
                if (!ct && !cu && !cv) { U += mult; long long mn = t < u ? t : u; if (mm0 == 0 || mn < mm0) mm0 = mn;
                    if (!clean(A, p) && !clean(B, p)) U2 += mult; }
                if ((ct || cu || cv) && c == -1) bad++;
            }
        }
        if (U == 0) u0++;
        printf("%lld %lld %lld %lld %lld %lld %d %d %d\n", p, Nw, Nm, U2, U, mm0, clean(p + 1, p), clean(p + 2, p), clean(2 * p + 1, p));
    }
    fprintf(stderr, "n count %lld, U=0 %lld, LemmaS violations %lld\n", cnt, u0, bad);
    return 0;
}
