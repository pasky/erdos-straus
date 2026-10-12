/* ffl_cover.c — finite coverings by linear families (FUNCTIONFIELD_ES.md §6.2, O161).
 * Linear family F = (E; ta,a0; tb,b0): E nonzero with E | W (up to unit), a0,b0 monic, A*E*lcm(a0,b0) | W,
 * types t: 0 -> a0, 1 -> P*a0, 2 -> X/a0, 3 -> P*X/a0, X = (P+E)/A.  F is valid at P iff A | P+E, a0,b0 | X,
 * s = a+b != 0, E | s, lc(s) = lc(E)  (then Lemma 1.3 gives an NC solution).  Validity depends only on P mod W
 * (for deg P large), so F covers a whole unit class r mod W iff it is valid at one representative
 * P_r = r + W*T^m.  For each unit class r mod W we test all families; prints #covered / #unit classes and the
 * uncovered classes (residues r, coefficients high->low).
 * usage: ffl_cover q A W m [maxprint]
 */
#define FFL_NO_MAIN
#define MAXC 600
#include "ffl_es.c"

static long nverified, nvfail; static poly Wp;
static uint64_t rng = 88172645463325252ULL;
static uint64_t xs(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; } static poly wdiv[MAXDIV]; static int nwdiv;
static int divides(const poly *d, const poly *x) { poly r; p_divmod(NULL, &r, x, d); return r.d < 0; }
static void mk(poly *out, int t, const poly *a0, const poly *P, const poly *X) {
    poly q; switch (t) { case 0: *out = *a0; break; case 1: p_mul(out, P, a0); break;
    case 2: p_divmod(&q, NULL, X, a0); *out = q; break; default: p_divmod(&q, NULL, X, a0); p_mul(out, P, &q); }
}
int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: ffl_cover q A W m [maxprint]\n"); return 1; }
    field_init(atoi(argv[1]));
    poly *targets[2] = {&Apoly, &Wp};
    for (int w = 0; w < 2; w++) { /* factors separated by '*', each high->low coefficients (comma list or digits) */
        char all[512]; strncpy(all, argv[2 + w], 511); poly acc = {.d = 0}; acc.c[0] = 1; char *sv; char *fac = strtok_r(all, "*", &sv);
        while (fac) { int cs[64], nc = 0; if (strchr(fac, ',')) { char *sv2; char *t = strtok_r(fac, ",", &sv2); while (t) { cs[nc++] = atoi(t); t = strtok_r(NULL, ",", &sv2); } }
            else for (char *s = fac; *s; s++) cs[nc++] = *s - '0';
            poly f; f.d = nc - 1; for (int i = 0; i < nc; i++) f.c[nc - 1 - i] = cs[i]; p_mul(&acc, &acc, &f); fac = strtok_r(NULL, "*", &sv); }
        *targets[w] = acc; }
    K = Apoly.d; int m = atoi(argv[4]); int maxprint = argc > 5 ? atoi(argv[5]) : 20;
    spf_build(Wp.d);
    { static poly pr[64]; static int ex[64], cd[MAXDIV], rdx[64]; int np = factor(&Wp, pr, ex); nwdiv = divisors(pr, ex, np, wdiv, cd, rdx); }
    if (!divides(&Apoly, &Wp)) { fprintf(stderr, "A must divide W\n"); return 1; }
    int dW = Wp.d; uint64_t ncls = 0, ncov = 0; int printed = 0;
    poly Tm; Tm.d = m; memset(Tm.c, 0, m + 1); Tm.c[m] = 1; poly WT; p_mul(&WT, &Wp, &Tm);
    for (uint64_t ri = 0; ri < qpow[dW]; ri++) {
        poly r; r.d = dW - 1; for (int i = 0; i < dW; i++) r.c[i] = (ri / qpow[i]) % Q; p_trim(&r);
        poly g; p_gcd(&g, &r, &Wp); if (g.d != 0) continue;   /* unit classes only */
        ncls++; poly P; p_add(&P, &WT, &r);
        int ok = 0;
        for (int ie = 0; ie < nwdiv && !ok; ie++) for (int u = 1; u < Q && !ok; u++) {
            poly E = wdiv[ie]; for (int i = 0; i <= E.d; i++) E.c[i] = gmul[E.c[i]][u];
            poly AE; p_mul(&AE, &Apoly, &wdiv[ie]); if (!divides(&AE, &Wp)) continue;
            poly PE, X, rm; p_add(&PE, &P, &E); p_divmod(&X, &rm, &PE, &Apoly); if (rm.d >= 0) continue;
            poly Wr; p_divmod(&Wr, NULL, &Wp, &AE);          /* lcm(a0,b0) | Wr */
            for (int ia = 0; ia < nwdiv && !ok; ia++) { const poly *a0 = &wdiv[ia]; if (!divides(a0, &Wr) || !divides(a0, &X)) continue;
            for (int ib = 0; ib < nwdiv && !ok; ib++) { const poly *b0 = &wdiv[ib]; if (!divides(b0, &Wr) || !divides(b0, &X)) continue;
                poly gg, l, lq; p_gcd(&gg, a0, b0); p_mul(&l, a0, b0); p_divmod(&lq, NULL, &l, &gg); if (!divides(&lq, &Wr)) continue;
                for (int ta = 0; ta < 4 && !ok; ta++) for (int tb = 0; tb < 4 && !ok; tb++) {
                    poly a, b, s; mk(&a, ta, a0, &P, &X); mk(&b, tb, b0, &P, &X); p_add(&s, &a, &b);
                    if (s.d < 0 || s.c[s.d] != E.c[E.d]) continue;
                    if (!divides(&E, &s)) continue;
                    ok = 1;
                    if (getenv("FFL_SHOW")) { printf("class r="); p_print(stdout, &r); printf(" E="); p_print(stdout, &E);
                        printf(" a=(t%d,", ta); p_print(stdout, a0); printf(") b=(t%d,", tb); p_print(stdout, b0); printf(")\n"); }
                    if (getenv("FFL_VERIFY")) { int nv = atoi(getenv("FFL_VERIFY"));
                        for (int v = 0; v < nv; v++) { /* random P = r + W*h, h monic of random degree, deg P in (2 deg W, 2 deg W + 15] */
                            int dh = dW + 1 + (int)(xs() % 15); poly h; h.d = dh; for (int i = 0; i < dh; i++) h.c[i] = xs() % Q; h.c[dh] = 1;
                            poly Pv, Xv, rr, av, bv, sv, kap, Yv, Zv, t1, t2;
                            p_mul(&Pv, &Wp, &h); p_add(&Pv, &Pv, &r); p_add(&t1, &Pv, &E); p_divmod(&Xv, &rr, &t1, &Apoly);
                            if (rr.d >= 0) { printf("VERIFY FAIL (A|P+E)\n"); continue; }
                            mk(&av, ta, a0, &Pv, &Xv); mk(&bv, tb, b0, &Pv, &Xv); p_add(&sv, &av, &bv);
                            p_divmod(&kap, &rr, &sv, &E); if (rr.d >= 0 || kap.d < 0 || kap.c[kap.d] != 1) { printf("VERIFY FAIL (kappa)\n"); continue; }
                            poly N; p_mul(&N, &Pv, &Xv); p_mul(&t1, &kap, &N);
                            p_divmod(&Yv, &rr, &t1, &av); if (rr.d >= 0) { printf("VERIFY FAIL (a|kN)\n"); continue; }
                            p_divmod(&Zv, &rr, &t1, &bv); if (rr.d >= 0) { printf("VERIFY FAIL (b|kN)\n"); continue; }
                            /* direct check: A*X*Y*Z == P*(XY+YZ+ZX), all monic, degrees >= n-k */
                            poly XY, YZ, ZX, L, R; p_mul(&XY, &Xv, &Yv); p_mul(&YZ, &Yv, &Zv); p_mul(&ZX, &Zv, &Xv);
                            p_mul(&L, &XY, &Zv); p_mul(&L, &L, &Apoly); p_add(&t2, &XY, &YZ); p_add(&t2, &t2, &ZX); p_mul(&R, &Pv, &t2);
                            int good = 1; poly df; p_sub(&df, &L, &R); if (df.d >= 0) good = 0;
                            int mn = Pv.d - K; if (Xv.d < mn || Yv.d < mn || Zv.d < mn) good = 0;
                            if (Xv.c[Xv.d] != 1 || Yv.c[Yv.d] != 1 || Zv.c[Zv.d] != 1) good = 0;
                            nverified += good; nvfail += !good; if (!good) printf("VERIFY FAIL (identity)\n"); } } } } }
        }
        if (ok) ncov++; else if (printed < maxprint) { printf("uncovered r="); p_print(stdout, &r); printf("\n"); printed++; }
    }
    printf("q=%d A=", Q); p_print(stdout, &Apoly); printf(" W="); p_print(stdout, &Wp);
    printf(" covered %llu / %llu unit classes", (unsigned long long)ncov, (unsigned long long)ncls);
    if (getenv("FFL_VERIFY")) printf("  verified %ld random P (identity A*XYZ = P*(XY+YZ+ZX), monic, NC), failures %ld", nverified, nvfail);
    printf("\n");
    return 0;
}
