/* O273 item (4): zeros of the c = 1 line of m/n (4 | m) by AP-marking, and the exact BM main term.  EVIDENCE tool.
 *
 * Line: m*u*B*C = n + u + B, C >= 1, gcd(u,B) = 1, u + B odd (n odd).  R*_m(n) = #{(u,B) ordered : m u B | n + u + B,
 * m u B - u - B <= n}  (cutoff repair (a): m u B - u - B <= N, not m u B <= N).
 * BM main term (BM_CORRECTED Prop 4.1(c): Brauer character chi_{-4uB}; chi_{-4uB}(-(u+B)) = -1):
 *   M_m(n) = sum_{(u,B) in P_m(n), gcd(n, m u B) = 1, -(u+B) a unit mod m u B} (1 - (-uB/n)) / phi(m u B).
 * Exact phi(m u B) (repair (b)): m = 8, 16: phi = m*phi(uB)/... computed exactly below via phi(m*m') with m' = uB even;
 * m = 12: phi(12 m') = 8 phi(m') if 3 !| m', 12 phi(m') if 3 | m'; and for 3 !| m' the target -(u+B) is a unit mod 3
 * iff m' = 1 (mod 3) (then for every splitting), never if m' = 2 (mod 3).  For m = 12 only n with gcd(n,6) = 1 are used.
 *
 * usage:  z42_zero_law mark m N lo            -> prints "Z n" for every zero in [lo,N] (n odd non-square, gcd rule),
 *                                                and "# total ..." summary; uses a bitset over odd n <= N.
 *         z42_zero_law exact m Nmax < list      -> for each n on stdin prints "n M M0" (exact BM main term, principal part)
 *         z42_zero_law sample m N lo k seed     -> marks, then draws k uniform admissible n in [lo,N]; prints "S n R0 M M0"
 *                                                (R0 = 1 iff zero) ; computes M exactly for each.
 *         z42_zero_law check m Nmax             -> brute-force self-test of R* and M for small n
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static int jac(long a, long n) { a %= n; if (a < 0) a += n; int t = 1;
    while (a) { while (!(a & 1)) { a >>= 1; long r = n & 7; if (r == 3 || r == 5) t = -t; }
        long x = a; a = n; n = x; if ((a & 3) == 3 && (n & 3) == 3) t = -t; a %= n; }
    return n == 1 ? t : 0; }
static long gcdl(long a, long b) { while (b) { long t = a % b; a = b; b = t; } return a; }
static int issq(long n) { long r = (long)llround(sqrt((double)n)); while (r*r > n) r--; while ((r+1)*(r+1) <= n) r++; return r*r == n; }
static long phil(long x) { long r = x; for (long p = 2; p*p <= x; p++) if (x % p == 0) { while (x % p == 0) x /= p; r -= r / p; } if (x > 1) r -= r / x; return r; }

static int M_NUM;
static int admissible(long n) { if (!(n & 1) || n < 5) return 0; if (M_NUM % 3 == 0 && n % 3 == 0) return 0; return !issq(n); }
/* pair-level unit condition and phi(m u B) */
static int pair_ok(long u, long B) { if (((u + B) & 1) == 0 || gcdl(u, B) != 1) return 0;
    if (M_NUM % 3 == 0 && (u*B) % 3 != 0 && (u + B) % 3 == 0) return 0;
    return 1; }

/* ---------- marking ---------- */
static uint8_t *bits; static long NB;
static void mark(long N) {
    NB = N / 2 + 1; bits = calloc(NB / 8 + 1, 1);
    long m = M_NUM;
    for (long u = 1; (m - 1) * u - 1 <= N; u++)
        for (long B = 1; m * u * B - u - B <= N; B++) {
            if (((u + B) & 1) == 0 || gcdl(u, B) != 1) continue;
            long q = m * u * B; long n0 = q - u - B;
            for (long n = n0; n <= N; n += q) { long i = n >> 1; bits[i >> 3] |= (uint8_t)(1u << (i & 7)); }
        }
}
static int hit(long n) { long i = n >> 1; return (bits[i >> 3] >> (i & 7)) & 1; }

/* ---------- exact main term ---------- */
static int *spf; static float *wt; static signed char *chi; static long XMAX, XW;
static long phi_spf(long x) { long r = 1; while (x > 1) { long l = spf[x], e = 1; x /= l; while (x % l == 0) { x /= l; e *= l; } r *= e * (l - 1); } return r; }
static void tables(long Nmax) {
    XMAX = Nmax / (M_NUM - 1) + 3;   /* chi/spf range: every u*B at the boundary is <= (n+1)/(m-1) */
    XW = Nmax / M_NUM + 2;           /* bulk range */
    spf = calloc(XMAX + 1, sizeof(int));
    for (long i = 2; i <= XMAX; i++) if (!spf[i]) { spf[i] = (int)i; if (i <= XMAX / i) for (long j = i * i; j <= XMAX; j += i) if (!spf[j]) spf[j] = (int)i; }
    wt = calloc(XW / 2 + 2, sizeof(float)); /* weight of even m' (index m'/2): (#admissible splittings)/phi(m m') */
    for (long mp = 2; mp <= XW; mp += 2) {
        long x = mp, ph = 1; int om = 0; while (x > 1) { long l = spf[x], e = 1; x /= l; while (x % l == 0) { x /= l; e *= l; } ph *= e * (l - 1); om++; }
        double phm;  /* phi(M_NUM * mp) for mp even */
        if (M_NUM == 12) { if (mp % 3 == 0) phm = 12.0 * ph; else if (mp % 3 == 1) phm = 8.0 * ph; else phm = 0; }
        else phm = (double)M_NUM * ph;   /* m = 2^a, a >= 2: phi(2^a mp) = 2^a phi(mp) for mp even */
        wt[mp / 2] = phm > 0 ? (float)((double)(1L << om) / phm) : 0.0f;
    }
    chi = malloc(XMAX + 2);
}
static double phi_mUB(long u, long B) { /* phi(m u B), u+B odd, gcd(u,B)=1 */
    double ph = (double)phi_spf(u) * (double)phi_spf(B);
    if (M_NUM == 12) return ((u * B) % 3 == 0) ? 12.0 * ph : 8.0 * ph;
    return (double)M_NUM * ph; }
static void exactM(long n, double *Mout, double *M0out) {
    long X = n / M_NUM;                  /* bulk: m' = uB <= n/m  (then m uB - u - B <= n) */
    long XB = (n + 1) / (M_NUM - 1) + 1; /* chi needed up to here for boundary pairs */
    chi[1] = 1;
    for (long k = 2; k <= XB; k++) { long l = spf[k]; chi[k] = (l == k) ? (signed char)jac(k, n) : (signed char)(chi[l] * chi[k / l]); }
    int cm1 = jac(-1, n);
    double M = 0, M0 = 0;
    for (long mp = 2; mp <= X; mp += 2) { if (!chi[mp]) continue; double w = wt[mp / 2]; M0 += w; M += w * (1 - cm1 * chi[mp]); }
    /* boundary pairs: uB > n/m, m u B - u - B <= n */
    for (long u = 1; (M_NUM - 1) * u - 1 <= n; u++) {
        long Bl = X / u + 1; long Bh = (n + u) / (M_NUM * u - 1);
        for (long B = Bl; B <= Bh; B++) {
            if (u * B <= X) continue;
            if (!pair_ok(u, B)) continue;
            int c = chi[u] * chi[B]; if (!c) continue;
            double w = 1.0 / phi_mUB(u, B); M0 += w; M += w * (1 - cm1 * c);
        }
    }
    *Mout = M; *M0out = M0;
}

/* cheap proxy for stratification only (never used as M): exact sum over m' <= Y, principal tail
   (S(X) - S(Y)) * prod_{odd l | n} (l-1)^2/(l^2+1)  [coprime-weight fraction], character tail ignored. */
static double *Spre; static long YP = 50000;
/* coarse prefix sums of wt: Spre[j] = sum_{i <= 256 j} wt[i] */
static void prefix(void) { long K = XW / 2 + 1, G = K / 256 + 2; Spre = calloc(G + 1, sizeof(double)); double acc = 0;
    for (long i = 1; i <= K; i++) { acc += wt[i]; if (i % 256 == 0) Spre[i / 256] = acc; } }
static double Sat(long i) { long j = i / 256; double a = Spre[j]; for (long t = 256 * j + 1; t <= i; t++) a += wt[t]; return a; }
static double proxyM(long n) {
    long X = n / M_NUM; long Y = YP < X ? YP : X;
    chi[1] = 1;
    for (long k = 2; k <= Y; k++) { long l = spf[k]; chi[k] = (l == k) ? (signed char)jac(k, n) : (signed char)(chi[l] * chi[k / l]); }
    int cm1 = jac(-1, n); double P = 0;
    for (long mp = 2; mp <= Y; mp += 2) if (chi[mp]) P += wt[mp / 2] * (1 - cm1 * chi[mp]);
    double f = 1; long r = n; for (long l = 3; l * l <= r; l += 2) if (r % l == 0) { while (r % l == 0) r /= l; f *= (double)(l-1)*(l-1)/((double)l*l+1); }
    if (r > 1) f *= (double)(r-1)*(r-1)/((double)r*r+1);
    /* principal tail from prefix sums of wt over even m' (computed lazily) */
    return P + (Sat(X / 2) - Sat(Y / 2)) * f;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    M_NUM = atoi(argv[2]);
    if (!strcmp(argv[1], "mark")) {
        long N = atol(argv[3]), lo = atol(argv[4]); mark(N);
        long z = 0, adm = 0;
        for (long n = lo | 1; n <= N; n += 2) { if (!admissible(n)) continue; adm++; if (!hit(n)) { z++; printf("Z %ld\n", n); } }
        printf("# m=%d N=%ld lo=%ld admissible=%ld zeros=%ld\n", M_NUM, N, lo, adm, z);
    } else if (!strcmp(argv[1], "exact")) {
        long Nmax = atol(argv[3]); tables(Nmax); long n;
        while (scanf("%ld", &n) == 1) { double M, M0; exactM(n, &M, &M0); printf("%ld %.5f %.5f\n", n, M, M0); fflush(stdout); }
    } else if (!strcmp(argv[1], "proxy")) {
        long Nmax = atol(argv[3]); tables(Nmax); prefix(); long n;
        while (scanf("%ld", &n) == 1) printf("%ld %.4f\n", n, proxyM(n));
    } else if (!strcmp(argv[1], "sample")) {
        long N = atol(argv[3]), lo = atol(argv[4]), k = atol(argv[5]); unsigned long seed = strtoul(argv[6], 0, 10);
        mark(N); tables(N); srand48((long)seed);
        for (long i = 0; i < k; ) { long n = lo + (long)(drand48() * (double)(N - lo + 1)); if (!admissible(n)) continue; i++;
            double M, M0; exactM(n, &M, &M0); printf("S %ld %d %.5f %.5f\n", n, !hit(n), M, M0); fflush(stdout); }
    } else if (!strcmp(argv[1], "check")) {
        long Nmax = atol(argv[3]); mark(Nmax); tables(Nmax); long bad = 0, tested = 0;
        for (long n = 5; n <= Nmax; n += 2) { if (!admissible(n) && !(issq(n) && !(M_NUM % 3 == 0 && n % 3 == 0))) continue;
            /* brute force R* and M over all pairs */
            long R = 0; double M = 0, M0 = 0; int cm1 = jac(-1, n);
            for (long u = 1; (M_NUM - 1) * u - 1 <= n; u++) for (long B = 1; (long)M_NUM * u * B - u - B <= n; B++) {
                if (((u + B) & 1) == 0 || gcdl(u, B) != 1) continue;
                if ((n + u + B) % ((long)M_NUM * u * B) == 0) R++;
                if (!pair_ok(u, B)) continue;
                if (gcdl(n, (long)M_NUM * u * B) != 1) continue;
                double w = 1.0 / (double)phil((long)M_NUM * u * B); M0 += w; M += w * (1 - cm1 * jac(u * B, n)); }
            double Me, M0e; exactM(n, &Me, &M0e); tested++;
            if ((R == 0) != !hit(n) || fabs(M - Me) > 1e-4 || fabs(M0 - M0e) > 1e-4 || (issq(n) && (R != 0 || fabs(Me) > 1e-9))) {
                bad++; if (bad < 10) printf("BAD n=%ld R=%ld hit=%d M=%.5f Me=%.5f M0=%.5f M0e=%.5f\n", n, R, hit(n), M, Me, M0, M0e); }
        }
        printf("# check m=%d n<=%ld tested=%ld bad=%ld\n", M_NUM, Nmax, tested, bad);
    }
    return 0;
}
