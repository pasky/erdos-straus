// O230 (SYNTHESIS_SPARKS5 §2): square-defect census (variant of s5_sides.c).
// Side category: 0 = clean (no prime r with (r/p) = -1), 1 = square-defect (every such r has even exponent, >= 1 such r),
// 2 = generic.  Word category = min over its three sides.  Output: p N Nm N0 N1 Nm1 lnr
// (N0 = words of category 0 (= Nany of s5_sides), N1/Nm1 = words of category 1 and their chi = -1 count).
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
static int odd_any, odd_oddexp;
static void addp(u64 r, int e, long long p) { if (leg((long long)(r % (u64)p), p) == -1) { odd_any = 1; if (e & 1) odd_oddexp = 1; } }
static void fac_rec(u64 x, long long p, u64 *ps, int *np) { if (x == 1) return;
    if ((long long)x <= M) { while (x > 1) { u64 r = spf[x]; ps[(*np)++] = r; x /= r; } return; }
    if (isprp(x)) { ps[(*np)++] = x; return; }
    u64 d = rho(x); fac_rec(d, p, ps, np); fac_rec(x / d, p, ps, np); }
static int cat(u64 x, long long p) { u64 ps[128]; int np = 0; odd_any = odd_oddexp = 0;
    for (u64 r = 2; r < 100; r++) { if (x % r) continue; int e = 0; while (x % r == 0) { x /= r; e++; } addp(r, e, p); }
    fac_rec(x, p, ps, &np);
    for (int i = 0; i < np; i++) { if (!ps[i]) continue; int e = 0; u64 r = ps[i]; for (int j = i; j < np; j++) if (ps[j] == r) { e++; ps[j] = 0; } addp(r, e, p); }
    return !odd_any ? 0 : (!odd_oddexp ? 1 : 2); }
int main(int argc, char **argv) {
    long long LO = atoll(argv[1]), HI = atoll(argv[2]);
    M = 2 * HI + 2 * (long long)sqrtl((long double)HI) + 100;
    spf = calloc(M + 1, sizeof(int));
    for (long long i = 2; i <= M; i++) if (!spf[i]) for (long long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    static long long divs[1 << 16];
    for (long long p = LO; p < HI; p++) {
        if (p % 4 != 1 || spf[p] != p) continue;
        long long Nw = 0, Nm = 0, N0 = 0, N1 = 0, Nm1 = 0;
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
                if (cu < 0) cu = cat((u64)(p + u), p);
                int ct = cat((u64)t * p + 1, p), cv = cat((u64)(p + v), p);
                int k = ct; if (cu < k) k = cu; if (cv < k) k = cv;
                Nw += mult; if (c == -1) Nm += mult;
                if (k == 0) { N0 += mult; if (c == -1) fprintf(stderr, "VIOLATION p=%lld w=(%lld,%lld,%lld)\n", p, t, u, v); }
                if (k == 1) { N1 += mult; if (c == -1) Nm1 += mult; }
            }
        }
        printf("%lld %lld %lld %lld %lld %lld %lld\n", p, Nw, Nm, N0, N1, Nm1, q);
    }
    return 0;
}
