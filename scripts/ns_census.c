// O221 (NEAR_SQUARE §4): per-prime census of five-slice words and of words on T1-type levels.
// Words (t,u,v), tuv - u - v = p (ordered, as in review_r224_census.c), chi = ((tu-1)/p).
// Level t is T1-type for p if tp + 1 = c^2 + t m^2 for some m >= 0, c >= 1 with gcd(m, c) = 1
// (THREE_SQUARES Lemma 1.4 with k = p - m^2, tk + 1 = c^2).  Then every odd prime r | tp+1 has (r/p) = +1.
// Output per prime p = 1 (4) in [LO, HI): p N Nminus NT1 NT1minus lnr minK
//   NT1 = words whose level is T1-type, NT1minus = those with chi = -1 (must be 0 when p = 1 mod 8),
//   minK = min over words on T1-type levels of the least K = p - m^2 realising it (-1 if none).
//   (7 extra columns) Ncl Nclm: words on clean levels (every prime r | tp+1 has (r/p) = +1) and their chi=-1 count (must be 0).
// usage: ns_census LO HI
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static long long pw(long long a, long long e, long long m) { __int128 r = 1, b = a % m; if (b < 0) b += m; while (e) { if (e & 1) r = r * b % m; b = b * b % m; e >>= 1; } return (long long)r; }
static int leg(long long a, long long p) { a %= p; if (a < 0) a += p; if (!a) return 0; return pw(a, (p - 1) / 2, p) == 1 ? 1 : -1; }
static long long isq(long long x) { if (x < 0) return -1; long long r = (long long)sqrtl((long double)x); while (r * r > x) r--; while ((r + 1) * (r + 1) <= x) r++; return r * r == x ? r : -1; }
static long long gcdl(long long a, long long b) { while (b) { long long t = a % b; a = b; b = t; } return a < 0 ? -a : a; }
// least K = p - m^2 > 0 with t K + 1 = c^2, gcd(m,c)=1 ; -1 if none
static long long t1K(long long p, long long t) {
    long long m = (long long)sqrtl((long double)p); while (m * m >= p) m--;
    for (; m >= 0; m--) { long long K = p - m * m; long long c = isq(t * K + 1); if (c > 0 && gcdl(m, c) == 1) return K; }
    return -1;
}
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulm(u64 a, u64 b, u64 m) { return (u128)a * b % m; }
static u64 powm(u64 a, u64 e, u64 m) { u64 r = 1; a %= m; while (e) { if (e & 1) r = mulm(r, a, m); a = mulm(a, a, m); e >>= 1; } return r; }
static int isprp(u64 n) { if (n < 2) return 0; static const u64 B[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (int i = 0; i < 12; i++) { if (n % B[i] == 0) return n == B[i]; }
    u64 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
    for (int i = 0; i < 12; i++) { u64 x = powm(B[i], d, n); if (x == 1 || x == n - 1) continue; int ok = 0;
        for (int r = 1; r < s; r++) { x = mulm(x, x, n); if (x == n - 1) { ok = 1; break; } } if (!ok) return 0; } return 1; }
static u64 rho(u64 n) { if (n % 2 == 0) return 2; for (u64 c = 1;; c++) { u64 x = 2, y = 2, d = 1;
    while (d == 1) { x = (mulm(x, x, n) + c) % n; y = (mulm(y, y, n) + c) % n; y = (mulm(y, y, n) + c) % n; d = gcdl(x > y ? x - y : y - x, n); }
    if (d != n) return d; } }
// clean: every prime factor r of x has leg(r, p) = +1 (r = p excluded: cannot divide tp+1)
static int clean_rec(u64 x, long long p) { if (x == 1) return 1;
    if (isprp(x)) return leg((long long)(x % (u64)p), p) == 1;
    u64 d = rho(x); return clean_rec(d, p) && clean_rec(x / d, p); }
static int clean(u64 x, long long p) { for (u64 r = 2; r < 200; r++) { if (x % r) continue; if (leg(r, p) != 1) return 0; while (x % r == 0) x /= r; } return clean_rec(x, p); }
int main(int argc, char **argv) {
    long long LO = atoll(argv[1]), HI = atoll(argv[2]);
    long long M = HI + 2 * (long long)sqrtl((long double)HI) + 100;
    int *spf = calloc(M + 1, sizeof(int));
    for (long long i = 2; i <= M; i++) if (!spf[i]) for (long long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    static long long divs[1 << 16];
    for (long long p = LO + ((5 - LO % 4) % 4 + 4) % 4 - 4; p < HI; p += 4) {
        if (p < LO || p % 4 != 1 || spf[p] != p) continue;
        long long Nw = 0, Nm = 0, NT = 0, NTm = 0, minK = -1, Ncl = 0, Nclm = 0;
        long long q = 2; while (leg(q, p) == 1) q++;
        // cache T1 status per level (levels up to p+2): use small hash via array for t <= 4096, else compute
        static long long cacheK[4097]; static long long cacheP[4097];
        for (long long u = 1; (u - 2) * u <= p; u++) {
            long long mm = p + u; int nd = 1; divs[0] = 1;
            while (mm > 1) { long long r = spf[mm]; int e = 0; while (mm % r == 0) { mm /= r; e++; }
                int cur = nd; long long pk = 1; for (int k = 1; k <= e; k++) { pk *= r; for (int i = 0; i < cur; i++) divs[nd++] = divs[i] * pk; } }
            for (int di = 0; di < nd; di++) { long long v = divs[di];      // v | p+u, v >= u
                if (v < u) continue;
                if ((p + u + v) % (u * v)) continue;
                long long t = (p + u + v) / (u * v);
                int c = leg(t * u - 1, p);
                int mult = (u == v) ? 1 : 2;
                Nw += mult; if (c == -1) Nm += mult;
                long long K;
                if (t <= 4096) { if (cacheP[t] != p) { cacheP[t] = p; cacheK[t] = t1K(p, t); } K = cacheK[t]; }
                else K = t1K(p, t);
                if (clean((u64)t * p + 1, p)) { Ncl += mult; if (c == -1) Nclm += mult; }
                if (K > 0) { NT += mult; if (c == -1) NTm += mult; if (minK < 0 || K < minK) minK = K; }
            }
        }
        printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld\n", p, Nw, Nm, NT, NTm, q, minK, Ncl, Nclm);
    }
    return 0;
}
