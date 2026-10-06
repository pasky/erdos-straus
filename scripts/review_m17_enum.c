/* R83 from-scratch complete enumerator of 17-generic boxes at level k (F = 17^k).
 * Derivations (reviewer's own, see reviews/pointwise-mordell17-review.md):
 *
 *  S-mode  (II2 / I2 / I3 with 17 | modulus-f, II3 with 17 | e):
 *     all (a,m,d,j) >= 1 with j(4adm-1) = F(a+m), a <= m  [symmetric in a,m].
 *     Bound: j>=1, m>=a  =>  j(4a^2 d - 1) <= 2Fa.  f = 4adm-1 must have v17(f) = k,
 *     g = f/F | 4a^2 d+1 (then also | 4m^2 d+1).  Prints "S a m d" (Python post-processes:
 *     II2 boxes -4a^2d, -4m^2d; I2 boxes -m/a, -a/m; I3 boxes sqrt(-4a^2 d), sqrt(-4m^2 d)).
 *  U-mode  (II1 / I4 / I2 with 17 | ac):  4iabc = F(a+b+c), sorted u<=v<=w, 4iuv <= 3F;
 *     for each choice of c: e=(a+b)/c integer, gcd(e,4ab)=1, v17(ab)=k.  Prints "U e".
 *  P-mode  (I1 / I3 with 17|cd / II3 with 17|ad), K given:  4a'd'ij = i+j+17^K a',
 *     17 !| a'd', i<=j; loop d', i with 4d'i^2 <= N+2i, then a' with
 *     (4a'd'i-1) | 4d'i^2+N.  Prints "P f fstar" with f=4a'd'i-1, f*=4a'd'j-1 (full ints).
 */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
typedef __int128 i128;
static u64 p17(int k) { u64 r = 1; while (k--) r *= 17; return r; }
static u64 g(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static int v17(u64 x) { int v = 0; while (x % 17 == 0) { x /= 17; v++; } return v; }

int main(int argc, char **argv) {
    char mode = argv[1][0];
    int k = atoi(argv[2]);
    u64 F = p17(k), cnt = 0;
    if (mode == 'S') {
        for (u64 a = 1; 4 * a * a - 1 <= 2 * F * a; a++)
            for (u64 d = 1; 4 * a * a * d - 1 <= 2 * F * a; d++) {
                u64 jmax = 2 * F * a / (4 * a * a * d - 1);
                for (u64 j = 1; j <= jmax; j++) {
                    /* m (4adj - F) = Fa + j */
                    i128 D = (i128)4 * a * d * j - F;
                    if (D <= 0) continue;
                    i128 num = (i128)F * a + j;
                    if (num % D) continue;
                    u64 m = (u64)(num / D);
                    if (m < a) continue;
                    i128 f = (i128)4 * a * d * m - 1;
                    if (f % F) continue;
                    i128 gg = f / F;
                    if (gg % 17 == 0) continue;
                    if (((i128)4 * a * a * d + 1) % gg) continue;
                    if (((i128)4 * m * m * d + 1) % gg) { fprintf(stderr, "ASYM\n"); exit(2); }
                    cnt++;
                    printf("S %llu %llu %llu\n", a, m, d);
                }
            }
    } else if (mode == 'U') {
        for (u64 i = 1; 4 * i <= 3 * F; i++)
            for (u64 u = 1; 4 * i * u * u <= 3 * F; u++)
                for (u64 v = u; 4 * i * u * v <= 3 * F; v++) {
                    i128 D = (i128)4 * i * u * v - F;
                    if (D <= 0) continue;
                    i128 W = (i128)F * (u + v);
                    if (W % D) continue;
                    u64 w = (u64)(W / D);
                    if (w < v) continue;
                    u64 t[3] = {u, v, w};
                    for (int r = 0; r < 3; r++) {
                        u64 c = t[r], a = t[(r + 1) % 3], b = t[(r + 2) % 3];
                        if ((a + b) % c) continue;
                        u64 e = (a + b) / c;
                        if (v17(a) + v17(b) != k) continue;
                        if (g(e, 4 * a) != 1 || g(e, b) != 1) continue;
                        cnt++;
                        printf("U %llu %llu %llu %llu\n", e, a, b, i);
                    }
                }
    } else if (mode == 'P') {
        u64 N = F;
        for (u64 i = 1; 4 * i * i <= N + 2 * i; i++)
            for (u64 dp = 1; 4 * dp * i * i <= N + 2 * i; dp++) {
                if (dp % 17 == 0) continue;
                u64 s = 4 * dp * i;
                u64 R = 4 * dp * i * i + N;
                for (u64 ap = 1; s * ap - 1 <= R; ap++) {
                    if (ap % 17 == 0) continue;
                    if (R % (s * ap - 1)) continue;
                    i128 num = (i128)i + (i128)N * ap;
                    i128 den = (i128)s * ap - 1;
                    if (num % den) { fprintf(stderr, "DIVBUG\n"); exit(2); }
                    u64 j = (u64)(num / den);
                    if (j < i) continue;
                    cnt++;
                    printf("P %llu %llu %llu %llu\n", 4 * ap * dp * i - 1, 4 * ap * dp * j - 1, ap, dp);
                }
            }
    }
    fprintf(stderr, "%c %d count=%llu\n", mode, k, cnt);
    return 0;
}
