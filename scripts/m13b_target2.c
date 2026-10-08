/* m13b_target2.c — targeted search for U-type (II1, I4) and I2 classes containing the T-generic point
 * x(u): x_11 = u11, x_13 = u13 (given mod 11^16, 13^16).  POINTWISE_MORDELL13B §5.
 * Parametrisation: h = 4 x y t - 1 (x, y prime to 143, t >= 1 arbitrary), T-unit ratio rho = R_n/R_d
 * (R_n = 11^{i+} 13^{j+}, R_d = 11^{i-} 13^{j-}, |i|,|j| <= E), first = R_n x, second = R_d y.
 * The common T-factor s of (first, second) can be taken 1 (it only refines the box; s does not affect the
 * T-free conditions as gcd(s, h) = 1).
 *  U (II1/I4): (a,b,e) = (R_n x, R_d y, h): e | a + b  <=>  rho = -y/x (mod e); boxes: q | R_n R_d:
 *     II1: e = -u_q, I4: u_q e = -1  (mod q^{v_q(ab)});  gcd(e, ab) = 1.
 *  I2: (a,c,f) = (R_n x, R_d y, h), B = f_T, g = f/B: f' | a + c <=> rho = -y/x (mod g); boxes:
 *     q | R_n R_d: f = -u_q (mod q^v);  q | B: c = -u_q a  (mod q^{v_q(f)});  gcd(ac, f) = 1.
 * usage: m13b_target2 u11 u13 X E      prints HIT lines.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __int128 i128; typedef unsigned __int128 u128;
static u64 Q16[2]; static const u64 QQ[2] = {11, 13}; static u64 U[2];
static u64 mulm(u64 a, u64 b, u64 m) { return (u64)((u128)a * b % m); }
static u64 powm(u64 b, u64 e, u64 m) { u64 r = 1 % m; b %= m; while (e) { if (e & 1) r = mulm(r, b, m); b = mulm(b, b, m); e >>= 1; } return r; }
static i128 inv(i128 a, i128 m) { i128 g = m, x = 0, x1 = 1, b = a % m; if (b < 0) b += m; while (b) { i128 q = g / b, t = g - q * b; g = b; b = t; t = x - q * x1; x = x1; x1 = t; } if (g != 1) return -1; x %= m; if (x < 0) x += m; return x; }
typedef struct { u64 v; int i, j; } ent;
static int cmp(const void *a, const void *b) { u64 x = ((const ent *)a)->v, y = ((const ent *)b)->v; return x < y ? -1 : x > y; }
static u64 ipow(u64 b, int e) { u64 r = 1; while (e--) r *= b; return r; }
static ent *mk(u64 g, int E, int no11, int no13, int *nt) {
    static ent *tab = 0; if (!tab) tab = malloc(sizeof(ent) * (2 * E + 1) * (2 * E + 1));
    u64 i11 = g > 1 ? (u64)inv(11, g) : 0, i13 = g > 1 ? (u64)inv(13, g) : 0; int n = 0;
    for (int i = -E; i <= E; i++) { if (no11 && i) continue;
        u64 p = i >= 0 ? powm(11, i, g) : powm(i11, -i, g);
        for (int j = -E; j <= E; j++) { if (no13 && j) continue;
            u64 v = mulm(p, j >= 0 ? powm(13, j, g) : powm(i13, -j, g), g);
            tab[n].v = v; tab[n].i = i; tab[n].j = j; n++; } }
    qsort(tab, n, sizeof(ent), cmp); *nt = n; return tab;
}
/* value of 11^a 13^b * z mod q^16 for the prime index t */
static u64 tval(int t, int e11, int e13, u64 z) {
    u64 m = Q16[t]; int ev[2] = {e11, e13};
    if (ev[t] >= 16) return 0;
    return mulm(mulm(ipow(QQ[t], ev[t]), powm(QQ[1 - t], ev[1 - t], m), m), z % m, m);
}
int main(int argc, char **argv) {
    Q16[0] = ipow(11, 16); Q16[1] = ipow(13, 16);
    U[0] = strtoull(argv[1], 0, 10) % Q16[0]; U[1] = strtoull(argv[2], 0, 10) % Q16[1];
    u64 X = strtoull(argv[3], 0, 10); int E = atoi(argv[4]); u64 hits = 0, L = X / 4 + 2;
    uint32_t *spf = calloc(L + 1, 4);
    for (u64 i = 2; i <= L; i++) if (!spf[i]) for (u64 j = i; j <= L; j += i) if (!spf[j]) spf[j] = (uint32_t)i;
    static u64 dv[1 << 16]; int nd;
    for (u64 h = 3; h <= X; h += 4) {
        u64 B = 1, g = h; int vB[2] = {0, 0};
        for (int t = 0; t < 2; t++) while (g % QQ[t] == 0) { g /= QQ[t]; B *= QQ[t]; vB[t]++; }
        u64 n4 = (h + 1) / 4;
        nd = 1; dv[0] = 1;
        { u64 mm = n4; while (mm > 1) { u64 p = spf[mm]; int ex = 0; while (mm % p == 0) { mm /= p; ex++; }
            if (p == 11 || p == 13) continue;
            int cur = nd; u64 pp = 1; for (int k2 = 1; k2 <= ex; k2++) { pp *= p; for (int k3 = 0; k3 < cur; k3++) dv[nd++] = dv[k3] * pp; } } }
        for (int pass = 0; pass < 2; pass++) {       /* pass 0: U (modulus h), pass 1: I2 (modulus g) */
            u64 mod = pass == 0 ? h : g; int nt;
            ent *tab = mk(mod, E, vB[0] > 0, vB[1] > 0, &nt);
            for (int ia = 0; ia < nd; ia++) for (int ib = 0; ib < nd; ib++) {
                u64 x = dv[ia], y = dv[ib]; if ((n4 / x) % y) continue;
                u64 c = 0;
                if (mod > 1) { i128 iv = inv((i128)(x % mod), mod); if (iv < 0) continue; c = mulm(mod - y % mod, (u64)iv, mod); }
                int lo = 0, hi = nt; while (lo < hi) { int md = (lo + hi) / 2; if (tab[md].v < c) lo = md + 1; else hi = md; }
                for (int k = lo; k < nt && tab[k].v == c; k++) {
                    int i = tab[k].i, j = tab[k].j; if (!i && !j && pass == 0) continue;
                    int vn[2] = {i > 0 ? i : 0, j > 0 ? j : 0}, vd[2] = {i < 0 ? -i : 0, j < 0 ? -j : 0};
                    int ok1 = 1, ok4 = 1, ok2 = 1;
                    for (int t = 0; t < 2; t++) {
                        int v = vn[t] + vd[t];
                        if (v) { if (v > 16) { ok1 = ok4 = ok2 = 0; continue; }
                            u64 qv = ipow(QQ[t], v);
                            if ((h % qv + U[t] % qv) % qv) ok1 = ok2 = 0;
                            if ((mulm(U[t] % qv, h % qv, qv) + 1) % qv) ok4 = 0; }
                        if (vB[t]) { u64 qv = ipow(QQ[t], vB[t]);
                            u64 a = tval(t, vn[0], vn[1], x), cc = tval(t, vd[0], vd[1], y);
                            if ((cc + mulm(U[t], a, Q16[t])) % qv) ok2 = 0; }
                    }
                    if (pass == 0) {
                        if (ok1) { printf("HIT II1 a=11^%d*13^%d*%llu b=11^%d*13^%d*%llu e=%llu\n", vn[0], vn[1], x, vd[0], vd[1], y, h); hits++; }
                        if (ok4) { printf("HIT I4 a=11^%d*13^%d*%llu b=11^%d*13^%d*%llu e=%llu\n", vn[0], vn[1], x, vd[0], vd[1], y, h); hits++; }
                    } else if (ok2 && (i || j || B > 1)) { printf("HIT I2 a=11^%d*13^%d*%llu c=11^%d*13^%d*%llu f=%llu\n", vn[0], vn[1], x, vd[0], vd[1], y, h); hits++; }
                }
            }
        }
    }
    fprintf(stderr, "# done X=%llu E=%d hits=%llu\n", X, E, hits);
    return 0;
}
