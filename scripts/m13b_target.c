/* m13b_target.c — targeted search for P/Q-type classes (II3, I3, I1) containing a T-generic point
 * x(u): x_11 = u11, x_13 = u13 (11-, 13-adic units given mod 11^16, 13^16), x_q = 1 otherwise.
 * (POINTWISE_MORDELL13B §5.)  No cap on the T-level: the T-part lam = a_T^2 d_T = 11^i 13^j is found
 * by a discrete-log test, i, j <= E.
 * Parametrisation (Lemma 2.1): a = a_T a', d = d_T d' (a', d' prime to 143), e = 4a'd'm - 1 = B g,
 * B = e_T.  T-free conditions: g | 4 lam a'^2 d' + 1  <=>  lam = -1/(4a'^2 d')  (mod g).
 * Box conditions (Lemma 1.1): q | lam:  e = -u_q (mod q^{v_q(ad)});  q | B:  q^{v_q(e)} | u_q + 4a^2 d (II3),
 * | u_q^2 + 4a^2 d (I3);  I1: e | 4a^2 d + 1 (then no condition at q | B).  gcd(lam, B) = 1 throughout.
 * usage: m13b_target u11 u13 X E [X0]  (u_q as integers mod q^16; searches all e = 4a'd'm - 1 in (X0, X])
 * prints "HIT fam a d e" with a, d as (a_T, a', d_T, d') and the T-exponents.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __int128 i128; typedef unsigned __int128 u128;
static u64 Q16[2]; static const u64 QQ[2] = {11, 13}; static u64 U[2];
static u64 mulm(u64 a, u64 b, u64 m) { return (u64)((u128)a * b % m); }
static u64 powm(u64 b, u64 e, u64 m) { u64 r = 1 % m; b %= m; while (e) { if (e & 1) r = mulm(r, b, m); b = mulm(b, b, m); e >>= 1; } return r; }
static i128 egcd_inv(i128 a, i128 m) { i128 g = m, x = 0, x1 = 1, a1 = a % m; if (a1 < 0) a1 += m; i128 b = a1; while (b) { i128 q = g / b, t = g - q * b; g = b; b = t; t = x - q * x1; x = x1; x1 = t; } if (g != 1) return -1; x %= m; if (x < 0) x += m; return x; }
typedef struct { u64 v; int i, j; } ent;
static int cmp(const void *a, const void *b) { u64 x = ((const ent *)a)->v, y = ((const ent *)b)->v; return x < y ? -1 : x > y; }
static u64 ipow(u64 b, int e) { u64 r = 1; while (e--) r *= b; return r; }

int main(int argc, char **argv) {
    Q16[0] = ipow(11, 16); Q16[1] = ipow(13, 16);
    U[0] = strtoull(argv[1], 0, 10) % Q16[0]; U[1] = strtoull(argv[2], 0, 10) % Q16[1];
    u64 X = strtoull(argv[3], 0, 10); int E = atoi(argv[4]);
    ent *tab = malloc(sizeof(ent) * (E + 1) * (E + 1));
    u64 hits = 0; u64 L = X / 4 + 2;
    uint32_t *spf = calloc(L + 1, 4);
    for (u64 i = 2; i <= L; i++) if (!spf[i]) for (u64 j = i; j <= L; j += i) if (!spf[j]) spf[j] = (uint32_t)i;
    static u64 dv[1 << 16]; int nd;
    u64 X0 = argc > 5 ? strtoull(argv[5], 0, 10) : 0;   /* optional start: search X0 < e <= X */
    u64 e0 = X0 - X0 % 4 + 3; if (e0 <= X0) e0 += 4;
    for (u64 e = e0; e <= X; e += 4) {           /* e = -1 mod 4 */
        if ((e & ((1ULL << 24) - 1)) == 3) { fprintf(stderr, "# progress e=%llu\n", e); fflush(stderr); }
        u64 B = 1, g = e; int vB[2] = {0, 0};
        for (int t = 0; t < 2; t++) while (g % QQ[t] == 0) { g /= QQ[t]; B *= QQ[t]; vB[t]++; }
        /* T-units mod g, avoiding primes of B */
        int nt = 0;
        for (int i = 0; i <= (vB[0] ? 0 : E); i++) for (int j = 0; j <= (vB[1] ? 0 : E); j++) {
            tab[nt].v = mulm(powm(11, i, g), powm(13, j, g), g); tab[nt].i = i; tab[nt].j = j; nt++;
        }
        qsort(tab, nt, sizeof(ent), cmp);
        u64 n4 = (e + 1) / 4;                    /* = a' d' m */
        /* T-free divisors of n4 */
        nd = 1; dv[0] = 1;
        { u64 mm = n4; while (mm > 1) { u64 p = spf[mm]; int ex = 0; while (mm % p == 0) { mm /= p; ex++; }
            if (p == 11 || p == 13) continue;
            int cur = nd; u64 pp = 1; for (int k2 = 1; k2 <= ex; k2++) { pp *= p; for (int k3 = 0; k3 < cur; k3++) dv[nd++] = dv[k3] * pp; } } }
        for (int ia = 0; ia < nd; ia++) {
            u64 ap = dv[ia];
            for (int id = 0; id < nd; id++) {
                u64 dp = dv[id];
                if ((n4 / ap) % dp) continue;
                /* c = -1/(4 a'^2 d') mod g */
                u64 c;
                if (g == 1) c = 0; else { i128 iv = egcd_inv((i128)mulm(mulm(4 * ap % g, ap, g), dp, g), g); if (iv < 0) continue; c = (g - (u64)iv) % g; }
                /* binary search all entries with value c */
                int lo = 0, hi = nt; while (lo < hi) { int md = (lo + hi) / 2; if (tab[md].v < c) lo = md + 1; else hi = md; }
                for (int k = lo; k < nt && tab[k].v == c; k++) {
                    int I = tab[k].i, J = tab[k].j;
                    /* splits lam = a_T^2 d_T: a_T = 11^x 13^y with 2x<=I, 2y<=J */
                    for (int x = 0; 2 * x <= I; x++) for (int y = 0; 2 * y <= J; y++) {
                        int va[2] = {x, y}, vd[2] = {I - 2 * x, J - 2 * y}; int ok3 = 1, okI3 = 1, ok1 = 1, ok2 = 1;
                        u64 a2d[2];
                        for (int t = 0; t < 2; t++) {
                            /* a^2 d mod q^16 (zero if divisible enough) */
                            int v = 2 * va[t] + vd[t];
                            u64 m = Q16[t], lamq = 1;
                            u64 other = powm(QQ[1 - t], 2 * va[1 - t] + vd[1 - t], m);
                            if (v >= 16) lamq = 0; else lamq = ipow(QQ[t], v);
                            a2d[t] = mulm(mulm(mulm(lamq, other, m), mulm(ap % m, ap % m, m), m), dp % m, m);
                            int vad = va[t] + vd[t];
                            if (vad) {   /* e = -u (mod q^vad) */
                                if (vad > 16) { ok3 = okI3 = ok1 = 0; continue; }
                                u64 qv = ipow(QQ[t], vad);
                                if ((e % qv + U[t] % qv) % qv) { ok3 = okI3 = ok1 = 0; }
                            }
                            if (vB[t]) {
                                u64 qv = ipow(QQ[t], vB[t]);
                                u64 s1 = (U[t] + 4 * a2d[t]) % qv, s2 = (mulm(U[t], U[t], qv) + 4 * a2d[t]) % qv;
                                if (s1) ok3 = ok2 = 0;
                                if (s2) okI3 = 0;
                                if ((4 * a2d[t] + 1) % qv) ok1 = 0;  /* I1 needs B | 4a^2d+1 */
                            }
                        }
                        /* II2 with T in ad: (a,d) = (a_T a', d_T d'), 4ad | e+1, box only at B (no condition at lam) */
                        if (ok2 && B > 1) {
                            u64 aTdT = 1; int ex11 = va[0] + vd[0], ex13 = va[1] + vd[1];
                            if (ex11 < 40 && ex13 < 40) { u128 w = 1; for (int z = 0; z < ex11; z++) w *= 11; for (int z = 0; z < ex13; z++) w *= 13;
                                if (w <= n4 && (n4 / (ap * dp)) % (u64)w == 0 && n4 % (ap * dp) == 0) { aTdT = (u64)w;
                                    printf("HIT II2 aT=11^%d*13^%d a'=%llu dT=11^%d*13^%d d'=%llu f=%llu (aTdT=%llu)\n", va[0], va[1], ap, vd[0], vd[1], dp, e, aTdT); hits++; } }
                        }
                        if (ok3) { printf("HIT II3 aT=11^%d*13^%d a'=%llu dT=11^%d*13^%d d'=%llu e=%llu\n", va[0], va[1], ap, vd[0], vd[1], dp, e); hits++; }
                        if (okI3) { printf("HIT I3 cT=11^%d*13^%d c'=%llu dT=11^%d*13^%d d'=%llu f=%llu\n", va[0], va[1], ap, vd[0], vd[1], dp, e); hits++; }
                        if (ok1 && (I || J)) { printf("HIT I1 aT=11^%d*13^%d a'=%llu dT=11^%d*13^%d d'=%llu f=%llu\n", va[0], va[1], ap, vd[0], vd[1], dp, e); hits++; }
                    }
                }
            }
        }
    }
    fprintf(stderr, "# done X=%llu E=%d hits=%llu\n", X, E, hits);
    return 0;
}
