/* z66 UCOVER: two-prime version of z66_ucover_levels.c (for the brief's K-question).
 * Profile pi: g at p1, h at p2, 1 at every other prime.  A family class with modulus m = p1^k p2^j m'
 * (gcd(m', p1 p2) = 1) contains pi iff r = 1 mod m', r = g mod p1^k, r = h mod p2^j.
 * Event equations (Z66_UCOVER.md Lemma 1 with ell^k replaced by the S-number N = p1^k p2^j; every prime of S is
 * split between the a- and the d- (resp. b-) parameter; E-events with a prime in both a and b are sub-cylinders of
 * parents with that prime removed from one side, as in §2.1, so only "coprime" E-splits are enumerated):
 *   F : 4acd - 1 = N f', gcd(f'acd, p1p2) = 1, f' | a + c          rho = -a/c mod N
 *   E : c(4a'b'D - 1) = N1 a' + N2 b', N1 N2 = N, gcd(N1,N2) = 1,  rho = -e, -1/e (e = 4a'b'D - 1)
 *   A : a'(4d'Cw - N1^2 N2) = C + w, N1 N2 = N (any split), N2 > 1  rho = -f (f = 4a'd'C - 1)
 * Output: "<fam> <rho mod p1^k> <rho mod p2^j> ...".  A-splits with N1^2 N2 > MCAP are skipped and reported.
 * Usage: z66_ucover_levels2 P1 K P2 J [MCAP]
 */
#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long u64;
typedef __int128 i128;

static u64 ipow(u64 b, int e) { u64 r = 1; while (e-- > 0) r *= b; return r; }
static long long modinv(long long a, long long m) {
    long long r0 = m, r1 = a % m, s0 = 0, s1 = 1;
    if (r1 < 0) r1 += m;
    while (r1) { long long q = r0 / r1, t = r0 - q * r1; r0 = r1; r1 = t; t = s0 - q * s1; s0 = s1; s1 = t; }
    if (r0 != 1) return -1;
    s0 %= m; if (s0 < 0) s0 += m; return s0;
}
static long long modN(i128 x, long long N) { long long r = (long long)(x % N); if (r < 0) r += N; return r; }

static u64 P1, P2, Q1, Q2, N;
static int coprimeS(i128 x) { return (x % (i128)P1) != 0 && (x % (i128)P2) != 0; }
static void out(const char *fam, i128 rho, const char *extra) {
    printf("%s %lld %lld %s\n", fam, modN(rho, (long long)Q1), modN(rho, (long long)Q2), extra);
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage\n"); return 1; }
    P1 = strtoull(argv[1], 0, 10); int K = atoi(argv[2]); P2 = strtoull(argv[3], 0, 10); int J = atoi(argv[4]);
    u64 MCAP = argc > 5 ? strtoull(argv[5], 0, 10) : 300000000ULL;
    Q1 = ipow(P1, K); Q2 = ipow(P2, J); N = Q1 * Q2;
    char buf[256];
    long long cF = 0, cE = 0, cA = 0;
    /* F */
    for (u64 a = 1; a < N; a++) {
        if (!coprimeS(a)) continue;
        for (u64 d = 1; a * d <= 2 * N / 3 + 1; d++) {
            if (!coprimeS(d)) continue;
            u64 ad = a * d;
            for (u64 w = N / (4 * ad) + 1; w <= (2 * N) / (3 * ad) + 1; w++) {
                i128 X = (i128)4 * ad * w - (i128)N; if (X <= 0) continue;
                i128 num = (i128)N * a + w; if (num % X) continue;
                i128 c = num / X; if (c < (i128)a || !coprimeS(c)) continue;
                i128 F = (i128)4 * a * c * d - 1; if (F % N) continue;
                i128 fp = F / N; if (!coprimeS(fp)) continue;
                if ((i128)(a + c) % fp) continue;
                long long ci = modinv(modN(c, N), N), ai = modinv((long long)(a % N), N);
                snprintf(buf, sizeof buf, "a=%llu c=%lld d=%llu", a, (long long)c, d);
                out("F", -(i128)a * ci, buf);
                out("F", -(i128)c * ai, buf);
                cF++;
            }
        }
    }
    /* E: coprime splits N1 in {1, Q1, Q2, N} */
    u64 n1s[4] = {1, Q1, Q2, N};
    for (int si = 0; si < 4; si++) {
        u64 N1 = n1s[si], N2 = N / N1;
        if (N2 == 1) continue; /* a <= b case with b's S-part trivial is impossible (a'cD <= 2/3) */
        for (u64 ap = 1; 3 * ap <= 2 * N2; ap++) {
            if (!coprimeS(ap)) continue;
            for (u64 c = 1; 3 * ap * c <= 2 * N2; c++)
                for (u64 D = 1; 3 * ap * c * D <= 2 * N2; D++) {
                    i128 X = (i128)4 * ap * c * D - (i128)N2; if (X <= 0) continue;
                    i128 num = (i128)N1 * ap + c; if (num % X) continue;
                    i128 bp = num / X; if (!coprimeS(bp)) continue;
                    i128 A = (i128)N1 * ap, B = (i128)N2 * bp; if (A > B) continue;
                    i128 e = (i128)4 * ap * bp * D - 1; if (!coprimeS(e)) continue;
                    if ((i128)c * e != A + B) { fprintf(stderr, "E sanity\n"); return 2; }
                    long long ei = modinv(modN(e, N), N);
                    snprintf(buf, sizeof buf, "N1=%llu a'=%llu b'=%lld c=%llu D=%llu", N1, ap, (long long)bp, c, D);
                    out("E", -e, buf); out("D", -(i128)ei, buf);
                    cE++;
                }
        }
    }
    /* A: a-part N1 = P1^al P2^be, d-part N2 = N/N1 > 1 */
    for (int al = 0; al <= K; al++) for (int be = 0; be <= J; be++) {
        u64 N1 = ipow(P1, al) * ipow(P2, be), N2 = N / N1;
        if (N2 == 1) continue;
        i128 Mb = (i128)N1 * N1 * N2;
        if (Mb > (i128)MCAP) { fprintf(stderr, "# SKIPPED A split al=%d be=%d (M=%.3g)\n", al, be, (double)Mb); continue; }
        u64 M = (u64)Mb;
        for (u64 dp = 1; 4 * dp <= M + 1; dp++) {
            if (!coprimeS(dp)) continue;
            for (u64 C = 1; 4 * dp * C - 1 <= M + C; C++) {
                u64 q = 4 * dp * C;
                for (u64 w = M / q + 1; w <= (M + C) / (q - 1); w++) {
                    i128 X = (i128)q * w - (i128)M; if (X <= 0) continue;
                    if ((i128)(C + w) % X) continue;
                    i128 ap = (i128)(C + w) / X; if (!coprimeS(ap)) continue;
                    i128 f = (i128)4 * ap * dp * C - 1;
                    i128 big = (i128)4 * (i128)M * ap * ap * dp + 1;
                    if (big % f) { fprintf(stderr, "A sanity\n"); return 3; }
                    snprintf(buf, sizeof buf, "al=%d be=%d a'=%lld d'=%llu C=%llu", al, be, (long long)ap, dp, C);
                    out("A", -f, buf);
                    cA++;
                }
            }
        }
    }
    fprintf(stderr, "# p1=%llu^%d p2=%llu^%d events F=%lld E=%lld A=%lld\n", P1, K, P2, J, cF, cE, cA);
    return 0;
}
