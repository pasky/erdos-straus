// O230 (SYNTHESIS_SPARKS5 §1): three-side cleanliness census.
// Words (t,u,v), tuv-u-v=p (ordered; enumeration as ns_census.c), chi=((tu-1)/p) for p = 1 (4).
// Side numbers N_t = tp+1 = AB, N_u = p+u = Av, N_v = p+v = Bu.  A side is "clean" if every prime factor r
// (2 included) has (r/p) = +1; then chi(w) = +1 (chi = psi(A) = psi(B), A | N_t, N_u; B | N_t, N_v).
// Output per prime p = 1 (4) in [LO,HI): p N Nminus Nt Nuv Nany lnr
//   Nt = words on clean t-side, Nuv = words with clean u- or v-side, Nany = words with some clean side;
//   check: chi=-1 words on a clean side must be 0 (printed to stderr if violated).
// usage: s5_sides LO HI
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulm(u64 a, u64 b, u64 m) { return (u128)a * b % m; }
static u64 powm(u64 a, u64 e, u64 m) { u64 r = 1; a %= m; while (e) { if (e & 1) r = mulm(r, a, m); a = mulm(a, a, m); e >>= 1; } return r; }
static int leg(long long a, long long p) { a %= p; if (a < 0) a += p; if (!a) return 0; return powm(a, (p - 1) / 2, p) == 1 ? 1 : -1; }
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
    if ((long long)x <= M) { while (x > 1) { int r = spf[x]; if (leg(r, p) != 1) return 0; while (x % r == 0) x /= r; } return 1; }
    if (isprp(x)) return leg((long long)(x % (u64)p), p) == 1;
    u64 d = rho(x); return clean_rec(d, p) && clean_rec(x / d, p); }
static int clean(u64 x, long long p) { for (u64 r = 2; r < 100; r++) { if (x % r) continue; if (leg(r, p) != 1) return 0; while (x % r == 0) x /= r; } return clean_rec(x, p); }
int main(int argc, char **argv) {
    long long LO = atoll(argv[1]), HI = atoll(argv[2]);
    M = 2 * HI + 2 * (long long)sqrtl((long double)HI) + 100;
    spf = calloc(M + 1, sizeof(int));
    for (long long i = 2; i <= M; i++) if (!spf[i]) for (long long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    static long long divs[1 << 16];
    for (long long p = LO; p < HI; p++) {
        if (p % 4 != 1 || spf[p] != p) continue;
        long long Nw = 0, Nm = 0, Nt = 0, Nuv = 0, Na = 0;
        long long q = 2; while (leg(q, p) == 1) q++;
        for (long long u = 1; (u - 2) * u <= p; u++) {
            long long mm = p + u; int nd = 1; divs[0] = 1;
            while (mm > 1) { long long r = spf[mm]; int e = 0; while (mm % r == 0) { mm /= r; e++; }
                int cur = nd; long long pk = 1; for (int k = 1; k <= e; k++) { pk *= r; for (int i = 0; i < cur; i++) divs[nd++] = divs[i] * pk; } }
            int cu = -1;
            for (int di = 0; di < nd; di++) { long long v = divs[di];
                if (v < u) continue;
                if ((p + u + v) % (u * v)) continue;
                long long t = (p + u + v) / (u * v);
                int c = leg(t * u - 1, p);
                int mult = (u == v) ? 1 : 2;
                if (cu < 0) cu = clean((u64)(p + u), p);
                int ct = clean((u64)t * p + 1, p), cv = clean((u64)(p + v), p);
                Nw += mult; if (c == -1) Nm += mult;
                if (ct) Nt += mult;
                if (cu || cv) Nuv += mult;
                if (ct || cu || cv) { Na += mult; if (c == -1) fprintf(stderr, "VIOLATION p=%lld w=(%lld,%lld,%lld)\n", p, t, u, v); }
            }
        }
        printf("%lld %lld %lld %lld %lld %lld %lld\n", p, Nw, Nm, Nt, Nuv, Na, q);
    }
    return 0;
}
