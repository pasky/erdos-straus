/* z66 UCOVER: exact enumeration of the ET Prop 1.9 family classes that contain the profile e_g
 * (e_g = 1 at every prime p != ell, g at ell), level by level.  See Z66_UCOVER.md, Lemma 2 (reduction to the
 * three event equations A, E(=D), F) for the derivation and the completeness bounds used here.
 *
 * For a level k >= 1 (N = ell^k) it prints every caught residue  rho mod ell^k  as a line
 *    <fam> <rho> <params...>
 * fam F : 4acd - 1 = N f', ell !| f', f' | a + c           rho = -a/c  (and the twin -c/a, printed as F too)
 * fam E : c(4a'b'D - 1) = ell^k1 a' + ell^k2 b'            rho = -e     (e = 4a'b'D - 1)
 * fam D : same events as E                                   rho = -1/e
 * fam A : a'(4d'Cw - ell^K') = C + w, K' = k + k1           rho = -f     (f = 4a'd'C - 1)
 * Usage: z66_ucover_levels ELL K
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef unsigned long long u64;
typedef __int128 i128;

static u64 ipow(u64 b, int e) { u64 r = 1; while (e-- > 0) r *= b; return r; }
static long long modinv(long long a, long long m) {
    long long g = m, x = 0, x1 = 1, a1 = a % m; if (a1 < 0) a1 += m;
    long long b = a1;
    /* extended Euclid on (b, m) */
    long long r0 = m, r1 = b, s0 = 0, s1 = 1;
    while (r1) { long long q = r0 / r1, t = r0 - q * r1; r0 = r1; r1 = t; t = s0 - q * s1; s0 = s1; s1 = t; }
    (void)g; (void)x; (void)x1;
    if (r0 != 1) return -1;
    s0 %= m; if (s0 < 0) s0 += m; return s0;
}
static long long modN(i128 x, long long N) { long long r = (long long)(x % N); if (r < 0) r += N; return r; }

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s ELL K\n", argv[0]); return 1; }
    u64 ell = strtoull(argv[1], 0, 10); int k = atoi(argv[2]);
    u64 N = ipow(ell, k);
    long long cntF = 0, cntE = 0, cntA = 0;
    /* ---- F: w(4acd-1) = N(a+c), a <= c  =>  N/4 < adw <= 2N/3 ; c = (Na + w)/(4adw - N) ---- */
    for (u64 a = 1; 4 * a < 4 * N; a++) {
        if (a % ell == 0) continue;
        for (u64 d = 1; a * d <= 2 * N / 3 + 1; d++) {
            if (d % ell == 0) continue;
            u64 ad = a * d;
            u64 wlo = N / (4 * ad) + 1, whi = (2 * N) / (3 * ad) + 1;
            for (u64 w = wlo; w <= whi; w++) {
                i128 X = (i128)4 * ad * w - (i128)N;
                if (X <= 0) continue;
                i128 num = (i128)N * a + w;
                if (num % X) continue;
                i128 c = num / X;
                if (c < (i128)a) continue;
                if (c % ell == 0) continue;
                i128 F = (i128)4 * a * c * d - 1;
                if (F % N) continue;
                i128 fp = F / N;
                if (fp % ell == 0) continue;
                if ((i128)(a + c) % fp) continue; /* sanity: f' | a + c */
                long long ci = modinv(modN(c, N), N), ai = modinv((long long)(a % N), N);
                long long r1 = modN(-(i128)a * ci, N), r2 = modN(-(i128)c * ai, N);
                printf("F %lld a=%llu c=%lld d=%llu w=%llu\n", r1, a, (long long)c, d, w);
                if (r2 != r1) printf("F %lld a=%lld c=%llu d=%llu w=%llu (twin)\n", r2, (long long)c, a, d, w);
                cntF++;
            }
        }
    }
    /* ---- E/D: c(4a'b'D - 1) = ell^k1 a' + ell^k2 b', a <= b  =>  a'cD <= (2/3) ell^k2 ---- */
    for (int k1 = 0; k1 <= k; k1++) {
        int k2 = k - k1; u64 L1 = ipow(ell, k1), L2 = ipow(ell, k2);
        for (u64 ap = 1; 3 * ap <= 2 * L2; ap++) {
            if (ap % ell == 0) continue;
            for (u64 c = 1; 3 * ap * c <= 2 * L2; c++) {
                for (u64 D = 1; 3 * ap * c * D <= 2 * L2; D++) {
                    i128 X = (i128)4 * ap * c * D - (i128)L2;
                    if (X <= 0) continue;
                    i128 num = (i128)L1 * ap + c;
                    if (num % X) continue;
                    i128 bp = num / X;
                    if (bp % ell == 0) continue;
                    i128 A = (i128)L1 * ap, B = (i128)L2 * bp;
                    if (A > B) continue;
                    i128 e = (i128)4 * ap * bp * D - 1;
                    if (e % ell == 0) continue;
                    if ((i128)c * e != A + B) { fprintf(stderr, "E sanity fail\n"); return 2; }
                    long long er = modN(e, N), ei = modinv(er, N);
                    printf("E %lld k1=%d a'=%llu b'=%lld c=%llu D=%llu e=%lld\n", modN(-e, N), k1, ap, (long long)bp, c, D, (long long)e);
                    printf("D %lld k1=%d a'=%llu b'=%lld c=%llu D=%llu e=%lld\n", modN(-(i128)ei, N), k1, ap, (long long)bp, c, D, (long long)e);
                    cntE++;
                }
            }
        }
    }
    /* ---- A: a'(4d'Cw - M) = C + w, M = ell^(k+k1); d'Cw <= M/2; w in (M/(4d'C), (M+C)/(4d'C-1)] ---- */
    for (int k1 = 0; k1 <= k - 1; k1++) {        /* k2 = k - k1 >= 1 (k2 = 0 impossible: chi_{-4d}) */
        int k2 = k - k1; u64 M = ipow(ell, k + k1);
        (void)k2;
        for (u64 dp = 1; 4 * dp <= M + 1; dp++) {
            if (dp % ell == 0) continue;
            for (u64 C = 1; 4 * dp * C - 1 <= M + C; C++) {
                u64 q = 4 * dp * C;
                u64 wlo = M / q + 1;
                u64 whi = (M + C) / (q - 1);
                for (u64 w = wlo; w <= whi; w++) {
                    i128 X = (i128)q * w - (i128)M;
                    if (X <= 0) continue;
                    if ((i128)(C + w) % X) continue;
                    i128 ap = (i128)(C + w) / X;
                    if (ap % ell == 0) continue;
                    i128 f = (i128)4 * ap * dp * C - 1;
                    /* sanity: f | 4 ell^(2k1+k2) a'^2 d' + 1 */
                    i128 big = (i128)4 * (i128)M * ap * ap * dp + 1;
                    if (big % f) { fprintf(stderr, "A sanity fail\n"); return 3; }
                    printf("A %lld k1=%d a'=%lld d'=%llu C=%llu w=%llu f=%lld\n", modN(-f, N), k1, (long long)ap, dp, C, w, (long long)f);
                    cntA++;
                }
            }
        }
    }
    fprintf(stderr, "# ell=%llu k=%d N=%llu events F=%lld E=%lld A=%lld\n", ell, k, N, cntF, cntE, cntA);
    return 0;
}
