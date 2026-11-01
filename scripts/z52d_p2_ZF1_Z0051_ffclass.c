/* z52d_p2_ZF1_Z0051_ffclass.c — ZF1 item Z0051 (FF Type II count vs class numbers, q = 3).
 * Reuses the engine of scripts/ffl_es.c (included with FFL_NO_MAIN): N_II(P) = # Type II solutions of
 * A/P = 1/X+1/Y+1/Z over F_q[T] (FUNCTIONFIELD_ES.md §2), for every monic P of degree n.
 * Adds, for each irreducible P of ODD degree n (∞ ramified in K = F_q(T, sqrt P): "imaginary"):
 *   the L-polynomial L(u, chi_P) = sum_{j<n} a_j u^j, a_j = sum_{f monic, deg f = j} (f/P),
 *   computed for j <= (n-1)/2 and completed by the functional equation a_{n-1-j} = q^{(n-1)/2 - j} a_j,
 *   class number h(P) = L(1, chi_P) (= #Pic^0 of y^2 = P(T)), and Weil check |roots| = sqrt q.
 * Also the "BM-type" pair sum T(P) = sum_{(a,b) coprime monic, deg(Aab) <= n} (-ab/P)/Phi(Aab)  (FF analogue
 * of BM_CORRECTED_COUNT T(p) = sum (-uB/p)/phi(4uB)) and M0 = sum 1/Phi(Aab) over the same pairs.
 * Output: one line per irreducible P: idx N_II h T PmodA(index) a_1;  M0 and #pairs on stderr.
 * usage: z52d_p2_ZF1_Z0051_ffclass q A n   (q odd prime only)
 */
#define FFL_NO_MAIN
#include "ffl_es.c"
#include <math.h>

static int chiq(int c) { /* quadratic character of F_q (q odd prime) */
    if (c == 0) return 0; long r = 1, b = c, e = (Q - 1) / 2; while (e) { if (e & 1) r = r * b % Q; b = b * b % Q; e >>= 1; }
    return r == 1 ? 1 : -1; }
/* Jacobi symbol (a/b), b monic nonconstant-or-1 */
static int jac(poly a, poly b) {
    int s = 1;
    for (;;) {
        if (b.d == 0) return s;            /* b = 1 */
        p_divmod(NULL, &a, &a, &b);
        if (a.d < 0) return 0;
        int c = a.c[a.d]; int cc = chiq(c); if (b.d & 1) s *= cc;  /* (c/b) = chi(c)^deg b */
        p_monic(&a);
        if (((Q - 1) / 2) % 2 == 1 && (a.d & 1) && (b.d & 1)) s = -s;
        poly t = a; a = b; b = t;
    }
}
static uint16_t *cnt2; static uint8_t *red2;
static void cnt2_cb(uint64_t idx, void *ctx) { (void)ctx; if (cnt2[idx] < 65535) cnt2[idx]++; }
static void red2_cb(uint64_t idx, void *ctx) { (void)ctx; red2[idx >> 3] |= 1 << (idx & 7); }
static double Phi(const poly *m) { poly pr[64]; int ex[64]; poly mm = *m; int np = factor(&mm, pr, ex); double r = 1;
    for (int i = 0; i < np; i++) { double N = pow(Q, pr[i].d); r *= (N - 1) * pow(N, ex[i] - 1); } return r; }

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage\n"); return 1; }
    field_init(atoi(argv[1]));
    { int nc = 0; int cs[64]; for (char *s = argv[2]; *s; s++) cs[nc++] = *s - '0';
      Apoly.d = nc - 1; for (int i = 0; i < nc; i++) Apoly.c[nc - 1 - i] = cs[i]; K = Apoly.d; }
    int n = atoi(argv[3]); if (!(n & 1)) { fprintf(stderr, "odd n only\n"); return 1; }
    int D = n; spf_build(D);
    uint64_t NP = qpow[n]; poly zero = {.d = -1};
    red2 = calloc(NP / 8 + 1, 1); cnt2 = calloc(NP, 2);
    for (int e = 1; e <= n / 2; e++) for (uint64_t i = 0; i < qpow[e]; i++) { poly g; p_from_idx(&g, e, i); if (is_irr_small(&g)) prog(&g, &zero, n, red2_cb, NULL); }
    static poly pr[64], dv[MAXDIV]; static int ex[64], cd[MAXDIV], rdx[64];
    /* pair list for T(P), M0: store codes of a and b (off[deg]+idx) and weight 1/Phi(Aab) */
    int maxpairs = 20000000; uint32_t *ca = malloc(4 * (size_t)maxpairs), *cb = malloc(4 * (size_t)maxpairs);
    double *pw = malloc(8 * (size_t)maxpairs); int npairs = 0;
    for (int sa = 0; sa <= n - K; sa++) for (int sb = 0; sa + sb <= n - K; sb++)
    for (uint64_t ia = 0; ia < qpow[sa]; ia++) for (uint64_t ib = 0; ib < qpow[sb]; ib++) {
        poly a, b, g, S, f; p_from_idx(&a, sa, ia); p_from_idx(&b, sb, ib);
        p_gcd(&g, &a, &b); if (g.d != 0) continue;
        p_add(&S, &a, &b); if (S.d < 0) continue;
        p_mul(&f, &a, &b); p_mul(&f, &f, &Apoly);
        if (npairs < maxpairs) { ca[npairs] = off[sa] + ia; cb[npairs] = off[sb] + ib; pw[npairs] = 1.0 / Phi(&f); npairs++; }
        poly Sm = S; p_monic(&Sm); int np = Sm.d > 0 ? factor(&Sm, pr, ex) : 0;
        int nd = divisors(pr, ex, np, dv, cd, rdx);
        for (int t = 0; t < nd; t++) { poly E, mE; p_divmod(&E, NULL, &S, &dv[t]); p_neg(&mE, &E); prog(&f, &mE, n, cnt2_cb, NULL); }
    }
    if (npairs >= maxpairs) { fprintf(stderr, "pairs overflow\n"); return 1; }
    int g2 = (n - 1) / 2; int dmax = n - K > g2 ? n - K : g2; int8_t *chi = malloc(off[dmax + 1]);
    double M0 = 0; for (int t = 0; t < npairs; t++) M0 += pw[t];
    fprintf(stderr, "pairs=%d M0=%.4f\n", npairs, M0);
    for (uint64_t i = 0; i < NP; i++) {
        if (red2[i >> 3] >> (i & 7) & 1) continue;
        poly P; p_from_idx(&P, n, i);
        for (int j = 0; j <= dmax; j++) for (uint64_t k = 0; k < qpow[j]; k++) { poly f; p_from_idx(&f, j, k); chi[off[j] + k] = jac(f, P); }
        double a[64] = {0};
        for (int j = 0; j <= g2; j++) { long s = 0; for (uint64_t k = 0; k < qpow[j]; k++) s += chi[off[j] + k]; a[j] = s; }
        for (int j = 0; j < g2; j++) a[n - 1 - j] = a[j] * pow(Q, g2 - j);
        double h = 0; for (int j = 0; j < n; j++) h += a[j];
        int cm1 = (n & 1) ? chiq(gneg[1]) : 1;   /* (-1/P) = chi_q(-1)^deg P */
        double T = 0; for (int t = 0; t < npairs; t++) T += chi[ca[t]] * chi[cb[t]] * pw[t];
        T *= cm1;
        poly rr; p_divmod(NULL, &rr, &P, &Apoly); uint64_t key = 0; for (int t = K - 1; t >= 0; t--) key = key * Q + (t <= rr.d ? rr.c[t] : 0);
        printf("%llu %u %.0f %.6f %llu %.0f\n", (unsigned long long)i, cnt2[i], h, T, (unsigned long long)key, a[1]);
    }
    return 0;
}
