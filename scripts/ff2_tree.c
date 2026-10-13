/* ff2_tree.c (O166 copy of ffl_tree.c; FFL_ALLUNC prints all uncovered) — adaptive covering trees of linear families (FUNCTIONFIELD_ES.md §6.2, O161).
 * A node is a unit class r mod W (A | W).  It is a leaf if some linear family F = (E; ta,a0; tb,b0) with
 * A*E*lcm(a0,b0) | W is valid at the representative P_r = r + W*T^m (then valid on the whole class for all
 * deg P = n > NTH, Lemma 6.2; families are restricted to deg a0 + deg b0 + k < NTH and deg E < NTH).
 * Otherwise the node is refined by the next factor of the refinement list (W -> W*ell), recursing on all unit
 * subclasses.  Every leaf family is re-verified on V random P of the class (degrees NTH+1..NTH+16) by the direct
 * identity A*X*Y*Z == P*(X*Y+Y*Z+Z*X), monic, all degrees >= n-k.
 * usage: ffl_tree q A root_W refine_list NTH maxdepth [V]
 *   root_W, refine_list: '*'-separated factors (high->low coefficients, digits or comma lists); refine_list is
 *   used in order, one factor per depth level (repeat a factor to go to higher powers).
 * Output: #leaves, #uncovered nodes at maxdepth (listed), max leaf modulus degree, verification counts.
 */
#define FFL_NO_MAIN
#define MAXC 600
#include "ffl_es.c"

static uint64_t rng = 88172645463325252ULL;
static uint64_t xs(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }
static int NTH, MAXDEPTH, V; static poly refl[64]; static int nref;
static long nleaf, nunc, nver, nvfail; static double umass, nroot; static int maxleafdeg, maxdepthused;
static int divides(const poly *d, const poly *x) { poly r; p_divmod(NULL, &r, x, d); return r.d < 0; }
static void mk(poly *out, int t, const poly *a0, const poly *P, const poly *X) {
    poly q; switch (t) { case 0: *out = *a0; break; case 1: p_mul(out, P, a0); break;
    case 2: p_divmod(&q, NULL, X, a0); *out = q; break; default: p_divmod(&q, NULL, X, a0); p_mul(out, P, &q); }
}
/* monic divisors of a monic poly g (deg <= 64), by trial division with refinement-list primes and W's primes */
static poly primes[64]; static int nprimes;
static int divs_of(const poly *g, poly *out) {
    int n = 1; out[0].d = 0; out[0].c[0] = 1; poly x = *g;
    for (int i = 0; i < nprimes; i++) { int e = 0; for (;;) { poly qt, rm; if (x.d < primes[i].d) break; p_divmod(&qt, &rm, &x, &primes[i]); if (rm.d >= 0) break; x = qt; e++; }
        if (!e) continue; int cur = n; for (int t = 0; t < cur; t++) { poly w = out[t]; for (int j = 1; j <= e; j++) { p_mul(&w, &w, &primes[i]); out[n++] = w; } } }
    if (x.d > 0) { fprintf(stderr, "divs_of: unexpected prime factor\n"); exit(1); }
    return n;
}
/* returns 1 and the family if found */
static int find_family(const poly *P, const poly *W, poly *Eo, int *tao, poly *a0o, int *tbo, poly *b0o) {
    static poly dW[65536]; poly Wa; p_divmod(&Wa, NULL, W, &Apoly);
    int nd = divs_of(&Wa, dW);
    for (int ie = 0; ie < nd; ie++) { if (dW[ie].d >= NTH) continue;
        for (int u = 1; u < Q; u++) {
            poly E = dW[ie]; for (int i = 0; i <= E.d; i++) E.c[i] = gmul[E.c[i]][u];
            poly PE, X, rm; p_add(&PE, P, &E); p_divmod(&X, &rm, &PE, &Apoly); if (rm.d >= 0) continue;
            poly Wr; p_divmod(&Wr, NULL, &Wa, &dW[ie]);
            poly g; p_gcd(&g, &X, &Wr); static poly dg[65536]; int ng = divs_of(&g, dg);
            for (int ia = 0; ia < ng; ia++) for (int ib = 0; ib < ng; ib++) {
                if (K + dg[ia].d + dg[ib].d >= NTH) continue;
                poly gg, l, lq; p_gcd(&gg, &dg[ia], &dg[ib]); p_mul(&l, &dg[ia], &dg[ib]); p_divmod(&lq, NULL, &l, &gg); if (!divides(&lq, &g)) continue;
                for (int ta = 0; ta < 4; ta++) for (int tb = 0; tb < 4; tb++) {
                    poly a, b, s; mk(&a, ta, &dg[ia], P, &X); mk(&b, tb, &dg[ib], P, &X); p_add(&s, &a, &b);
                    if (s.d < 0 || s.c[s.d] != E.c[E.d] || !divides(&E, &s)) continue;
                    *Eo = E; *tao = ta; *a0o = dg[ia]; *tbo = tb; *b0o = dg[ib]; return 1; } } } }
    return 0;
}
static int verify(const poly *r, const poly *W, const poly *E, int ta, const poly *a0, int tb, const poly *b0) {
    int bad = 0;
    for (int v = 0; v < V; v++) {
        int n = NTH + 1 + (int)(xs() % 16); int dh = n - W->d; if (dh < 0) continue;
        poly h; h.d = dh; for (int i = 0; i < dh; i++) h.c[i] = xs() % Q; h.c[dh] = 1;
        poly P, X, rr, a, b, s, kap, N, t1, Y, Z; p_mul(&P, W, &h); p_add(&P, &P, r);
        p_add(&t1, &P, E); p_divmod(&X, &rr, &t1, &Apoly); if (rr.d >= 0) { bad++; continue; }
        if (!divides(a0, &X) || !divides(b0, &X)) { bad++; continue; }
        mk(&a, ta, a0, &P, &X); mk(&b, tb, b0, &P, &X); p_add(&s, &a, &b);
        p_divmod(&kap, &rr, &s, E); if (s.d < 0 || rr.d >= 0 || kap.c[kap.d] != 1) { bad++; continue; }
        p_mul(&N, &P, &X); p_mul(&t1, &kap, &N);
        p_divmod(&Y, &rr, &t1, &a); if (rr.d >= 0) { bad++; continue; }
        p_divmod(&Z, &rr, &t1, &b); if (rr.d >= 0) { bad++; continue; }
        poly XY, YZ, ZX, L, R, t2, df; p_mul(&XY, &X, &Y); p_mul(&YZ, &Y, &Z); p_mul(&ZX, &Z, &X);
        p_mul(&L, &XY, &Z); p_mul(&L, &L, &Apoly); p_add(&t2, &XY, &YZ); p_add(&t2, &t2, &ZX); p_mul(&R, &P, &t2);
        p_sub(&df, &L, &R); int mn = P.d - K;
        if (df.d >= 0 || X.d < mn || Y.d < mn || Z.d < mn || X.c[X.d] != 1 || Y.c[Y.d] != 1 || Z.c[Z.d] != 1) bad++;
        else nver++;
    }
    nvfail += bad; return bad;
}
static void node(const poly *r, const poly *W, int depth, double mass) {
    poly Tm; int m = W->d > NTH ? W->d : NTH; m += 2; Tm.d = m; memset(Tm.c, 0, m + 1); Tm.c[m] = 1;
    poly P; p_mul(&P, W, &Tm); p_add(&P, &P, r);
    poly E, a0, b0; int ta, tb;
    if (find_family(&P, W, &E, &ta, &a0, &tb, &b0)) {
        nleaf++; if (W->d > maxleafdeg) maxleafdeg = W->d; if (depth > maxdepthused) maxdepthused = depth;
        if (V && verify(r, W, &E, ta, &a0, tb, &b0)) { printf("VERIFY FAIL at r="); p_print(stdout, r); printf("\n"); }
        if (getenv("FFL_SHOW")) { printf("leaf W="); p_print(stdout, W); printf(" r="); p_print(stdout, r); printf(" E="); p_print(stdout, &E);
            printf(" a=(t%d,", ta); p_print(stdout, &a0); printf(") b=(t%d,", tb); p_print(stdout, &b0); printf(")\n"); }
        return;
    }
    if (depth >= MAXDEPTH || depth >= nref) { nunc++; umass += mass; if (nunc <= 40 || getenv("FFL_ALLUNC")) { printf("uncovered W="); p_print(stdout, W); printf(" r="); p_print(stdout, r); printf("\n"); } return; }
    const poly *ell = &refl[depth]; poly W2; p_mul(&W2, W, ell);
    int nch = 0;
    for (uint64_t t = 0; t < qpow[ell->d]; t++) { poly tt; tt.d = ell->d - 1; for (int i = 0; i < ell->d; i++) tt.c[i] = (t / qpow[i]) % Q; p_trim(&tt);
        poly r2; p_mul(&r2, W, &tt); p_add(&r2, &r2, r); poly g; p_gcd(&g, &r2, &W2); if (g.d == 0) nch++; }
    for (uint64_t t = 0; t < qpow[ell->d]; t++) {
        poly tt; tt.d = ell->d - 1; for (int i = 0; i < ell->d; i++) tt.c[i] = (t / qpow[i]) % Q; p_trim(&tt);
        poly r2; p_mul(&r2, W, &tt); p_add(&r2, &r2, r);
        poly g; p_gcd(&g, &r2, &W2); if (g.d != 0) continue;
        node(&r2, &W2, depth + 1, mass / nch);
    }
}
static int parse(const char *spec, poly *list, int split) {
    char all[1024]; strncpy(all, spec, 1023); int cnt = 0; char *sv; char *fac = strtok_r(all, "*", &sv); poly acc = {.d = 0}; acc.c[0] = 1;
    while (fac) { int cs[64], nc = 0; if (strchr(fac, ',')) { char *sv2; char *t = strtok_r(fac, ",", &sv2); while (t) { cs[nc++] = atoi(t); t = strtok_r(NULL, ",", &sv2); } }
        else for (const char *s = fac; *s; s++) cs[nc++] = *s - '0';
        poly f; f.d = nc - 1; for (int i = 0; i < nc; i++) f.c[nc - 1 - i] = cs[i];
        if (split) list[cnt++] = f; else p_mul(&acc, &acc, &f); fac = strtok_r(NULL, "*", &sv); }
    if (!split) { list[0] = acc; return 1; } return cnt;
}
static void add_prime(const poly *f) { for (int i = 0; i < nprimes; i++) if (primes[i].d == f->d && !memcmp(primes[i].c, f->c, f->d + 1)) return; primes[nprimes++] = *f; }
int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: ffl_tree q A root_W refine_list NTH maxdepth [V]\n"); return 1; }
    field_init(atoi(argv[1])); parse(argv[2], &Apoly, 0); K = Apoly.d;
    poly roots[64]; int nr = parse(argv[3], roots, 1); poly W; parse(argv[3], &W, 0);
    nref = parse(argv[4], refl, 1); NTH = atoi(argv[5]); MAXDEPTH = atoi(argv[6]); V = argc > 7 ? atoi(argv[7]) : 0;
    for (int i = 0; i < nr; i++) add_prime(&roots[i]); for (int i = 0; i < nref; i++) add_prime(&refl[i]);
    poly Ap[64]; int na = parse(argv[2], Ap, 1); for (int i = 0; i < na; i++) add_prime(&Ap[i]);
    if (!divides(&Apoly, &W)) { fprintf(stderr, "A must divide root W\n"); return 1; }
    for (uint64_t ri = 0; ri < qpow[W.d]; ri++) {
        poly r; r.d = W.d - 1; for (int i = 0; i < W.d; i++) r.c[i] = (ri / qpow[i]) % Q; p_trim(&r);
        poly g; p_gcd(&g, &r, &W); if (g.d != 0) continue;
        nroot++; node(&r, &W, 0, 1.0);
    }
    printf("q=%d A=", Q); p_print(stdout, &Apoly); printf(" rootW="); p_print(stdout, &W);
    printf(" NTH=%d: leaves=%ld uncovered=%ld maxleafdeg=%d maxdepth=%d verified=%ld vfail=%ld uncovered_density=%.5f\n", NTH, nleaf, nunc, maxleafdeg, maxdepthused, nver, nvfail, umass / nroot);
    return 0;
}
