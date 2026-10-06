/* m17_enum.c — exact enumeration of 17-generic ET boxes (POINTWISE_MORDELL17 §2-3).
 *
 * usage: m17_enum Q k   -> (Q)-data of level k (Type I N-points of 4/17^k, 17∤e):
 *                          prints "Q r" for boxes r = -4a^2 d and r = -4b^2 d (mod 17^k)
 *        m17_enum U k   -> (U)-data of level k: 4iabc = F(a+b+c), (ab)_17 = F, e=(a+b)/c,
 *                          gcd(e,4ab)=1; prints "U r" for r = -e (mod 17^k)
 *        m17_enum P K   -> Type II N-points of 4/17^K with 17∤cd; prints "P r" for
 *                          r = -f and r = -f* (f=4acd-1, f*=4bcd-1) mod 17^ceil(K/2)
 * Output residues are deduplicated by the caller (sort -u).  Counts of data on stderr.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
typedef __int128 i128;

static u64 pw17(int k) { u64 r = 1; while (k--) r *= 17; return r; }
static u64 gcdu(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static u64 mod(i128 x, u64 m) { i128 r = x % (i128)m; if (r < 0) r += m; return (u64)r; }

int main(int argc, char **argv) {
    if (argc < 3) return 1;
    char mode = argv[1][0];
    int k = atoi(argv[2]);
    u64 cnt = 0;
    if (mode == 'Q') {
        /* Type I, a<=b: n/4 < acd <= 3n/4 (ET Lemma 2.8), f = 4acd - n | 4a^2 d + 1,
           b = (na+c)/f, e = (a+b)/c.  Both orientations recorded via boxes for a and b. */
        u64 n = pw17(k), F = n;
        for (u64 a = 1; 4 * a <= 3 * n; a++)
            for (u64 d = 1; 4 * a * d <= 3 * n; d++) {
                u64 ad = a * d;
                u64 c0 = n / (4 * ad) + 1;
                for (u64 c = c0; 4 * ad * c <= 3 * n; c++) {
                    u64 f = 4 * ad * c - n;
                    i128 E = (i128)4 * a * a * d + 1;
                    if (E % f) continue;
                    i128 B = (i128)n * a + c;
                    if (B % f) continue;
                    u64 b = (u64)(B / f);
                    if (b < a || (a + b) % c) continue;
                    u64 e = (a + b) / c;
                    if (e % 17 == 0) continue;
                    cnt++;
                    printf("Q %llu\n", mod(-(i128)4 * a * a * d, F));
                    printf("Q %llu\n", mod(-(i128)4 * b * b * d, F));
                }
            }
    } else if (mode == 'U') {
        u64 F = pw17(k);
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
                        if (r > 0 && t[r] == t[r - 1]) continue;
                        u64 c = t[r], a = t[(r + 1) % 3], b = t[(r + 2) % 3];
                        i128 ab = (i128)a * b;
                        if (ab % F) continue;
                        i128 nn = ab / F;
                        if (nn % 17 == 0) continue;
                        if ((a + b) % c) continue;
                        u64 e = (a + b) / c;
                        if (4 * i * nn != (i128)e + 1) continue; /* consistency */
                        if (gcdu(e, (u64)(((i128)4 * ab) % e)) != 1) continue;
                        cnt++;
                        printf("U %llu\n", mod(-(i128)e, F));
                    }
                }
    } else if (mode == 'P') {
        /* Type II, a<=b: n/4 < abd <= n/2, so a^2 d <= n/2. ef = n+4a^2 d, f = 4acd-1,
           e = -n mod 4ad.  Scan the smaller of e, f in its residue class. */
        int K = k;
        u64 n = pw17(K), F = pw17((K + 1) / 2);
        for (u64 a = 1; 2 * a * a <= n; a++)
            for (u64 d = 1; 2 * a * a * d <= n; d++) {
                u64 m4 = 4 * a * d;
                i128 m = (i128)n + (i128)4 * a * a * d;
                /* f = m4*c - 1, e = m/f;  e == -n (mod m4) */
                u64 e0 = (u64)mod(-(i128)n, m4);
                if (e0 == 0) e0 = m4;
                for (int side = 0; side < 2; side++) {
                    u64 x = side == 0 ? m4 - 1 : e0; /* f-values or e-values */
                    for (; (i128)x * x <= m; x += m4) {
                        if (m % x) continue;
                        u64 f = side == 0 ? x : (u64)(m / x);
                        u64 e = side == 0 ? (u64)(m / x) : x;
                        if (side == 1 && (i128)f * f <= m) continue; /* counted on side 0 */
                        if ((f + 1) % m4) continue;
                        u64 c = (f + 1) / m4;
                        i128 bb = (i128)c * e - a;
                        if (bb < (i128)a) continue;
                        u64 b = (u64)bb;
                        if ((i128)4 * a * b * c * d != (i128)a + b + (i128)n * c) { fprintf(stderr, "BUG\n"); exit(2); }
                        if (c % 17 == 0 || d % 17 == 0) continue;
                        cnt++;
                        printf("P %llu\n", mod(-(i128)f, F));
                        printf("P %llu\n", mod(-((i128)4 * b * c * d - 1), F));
                    }
                }
            }
    }
    fprintf(stderr, "%c %d data=%llu\n", mode, k, cnt);
    return 0;
}
