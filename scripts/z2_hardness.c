// z2_hardness.c (O225, NEAR_SQUARE_EXIST §2/§3): per prime p = 1 (4) in [LO,HI), all words (u <= v, counted with
// multiplicity 2 for u < v), flags:
//   t-clean (THREE_SQUARES/ns_census definition: every prime r | tp+1 has (r/p) = +1),
//   u-genus-clean: some imaginary quadratic F = Q(sqrt(-K0)) inside Sigma_u = Q(zeta_u, sqrt(-u)) (NEAR_SQUARE_EXIST
//   Cor 2.3 (a),(b)) splits every odd prime of p+u; the word is "u-flagged" if (A odd and level u is u-genus-clean) or
//   (A* odd and level v is v-genus-clean).  Pointwise Thm 2.1(b) predicts chi = +1 on every flagged word.
// Output per prime: p N Nminus Ncl Nclm Nfl_beyond_clean Nflm_all K0 lnr
// usage: z2_hardness LO HI
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
static int *spf;
static int jac(long long a, long long n) { int s = 1; a %= n; if (a < 0) a += n; while (a) { while (!(a & 1)) { a >>= 1; long long r = n & 7; if (r == 3 || r == 5) s = -s; } long long t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) s = -s; a %= n; } return n == 1 ? s : 0; }
static int cond_b(long long K0, long long u) {           // Cor 2.3 (b)
    if (K0 % 4 == 3) return 1;
    if (K0 % 2 == 1) return (u % 4 == 1) || (u % 4 == 0);
    long long K1 = K0 / 2, u2 = u % 8;
    if (u % 8 == 0) return 1;
    if (u % 4 != 2) return 0;
    long long up = u / 2;
    return (K1 % 4 == 1) ? (up % 4 == 1) : (up % 4 == 3);
}
static int genus_clean(long long p, long long u) {
    long long q[16]; int nq = 0; long long x = u; while (x % 2 == 0) x /= 2;
    while (x > 1) { long long r = spf[x]; q[nq++] = r; while (x % r == 0) x /= r; }
    long long pr[40]; int npr = 0; x = p + u; while (x % 2 == 0) x /= 2;
    while (x > 1) { long long r = spf[x]; pr[npr++] = r; while (x % r == 0) x /= r; }
    for (int mask = 0; mask < (1 << nq); mask++) for (int two = 1; two <= 2; two++) {
        long long K0 = two; for (int i = 0; i < nq; i++) if (mask >> i & 1) K0 *= q[i];
        if (!cond_b(K0, u)) continue;
        int ok = 1; for (int i = 0; i < npr && ok; i++) if (jac(-K0, pr[i]) != 1) ok = 0;
        if (ok) return 1;
    }
    return 0;
}
int main(int argc, char **argv) {
    long long LO = atoll(argv[1]), HI = atoll(argv[2]);
    long long M = 2 * HI + 4 * (long long)sqrtl((long double)HI) + 100;
    spf = calloc(M + 1, sizeof(int));
    for (long long i = 2; i <= M; i++) if (!spf[i]) for (long long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    static long long divs[1 << 16];
    for (long long p = LO; p < HI; p++) {
        if (p % 4 != 1 || spf[p] != p) continue;
        long long Nw = 0, Nm = 0, Ncl = 0, Nclm = 0, Nfl = 0, Nflm = 0;
        long long q = 2; while (leg(q, p) == 1) q++;
        long long m = (long long)sqrtl((long double)p); while (m * m > p) m--; long long K0 = p - m * m;
        for (long long u = 1; (u - 2) * u <= p; u++) {
            long long mm = p + u; int nd = 1; divs[0] = 1;
            while (mm > 1) { long long r = spf[mm]; int e = 0; while (mm % r == 0) { mm /= r; e++; }
                int cur = nd; long long pk = 1; for (int k = 1; k <= e; k++) { pk *= r; for (int i = 0; i < cur; i++) divs[nd++] = divs[i] * pk; } }
            int gu = -1;
            for (int di = 0; di < nd; di++) { long long v = divs[di];
                if (v < u || (p + u + v) % (u * v)) continue;
                long long t = (p + u + v) / (u * v), A = t * u - 1, As = t * v - 1;
                int c = leg(A, p); int mult = (u == v) ? 1 : 2;
                Nw += mult; if (c == -1) Nm += mult;
                int iscl = clean((u64)t * p + 1, p);
                if (iscl) { Ncl += mult; if (c == -1) Nclm += mult; }
                int fl = 0;
                if (A % 2) { if (gu < 0) gu = genus_clean(p, u); fl = gu; }
                if (!fl && (As % 2)) fl = genus_clean(p, v);
                if (fl) { if (!iscl) Nfl += mult; if (c == -1) Nflm += mult; }
            }
        }
        printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld\n", p, Nw, Nm, Ncl, Nclm, Nfl, Nflm, K0, q);
    }
    return 0;
}
