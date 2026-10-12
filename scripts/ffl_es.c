/* ffl_es.c — Erdős–Straus analogue over F_q[T] (FUNCTIONFIELD_ES.md, O161).
 *
 * ES_q(A,P): A/P = 1/X+1/Y+1/Z, X,Y,Z monic, all deg >= n-k (NC).  Lemma 1.3 (all chars):
 *   exists monic X, deg X = n-k, monic a,b | P X with E = A X - P | a+b != 0, lc(a+b) = lc(E).
 * Type II solutions (P | Y,Z) <-> (a,b,c,d) monic, gcd(a,b)=1, c | a+b, P = A a b d - (a+b)/c.
 * Engine: (1) global Type II counts N_II(P) for all monic P of degree n (progression marking);
 *         (2) irreducible P with N_II = 0 get the complete Lemma 1.3 decision (Type I and II);
 *         (3) optional: full counts N(P) (= #ordered (X,Y,Z), deg X = n-k) on a sample of irreducible P.
 * usage: ffl_es q A n [nsample] [seed] [failfile]
 *   A = coefficients high->low, comma separated field labels (e.g. "1,0" = T, "1,0,0" = T^2, "1,0,2" = T^2+2)
 * Field labels: element = base-p digit vector of the label (GF(p^r) via fixed irreducible modulus).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAXC 72
typedef struct { int d; uint8_t c[MAXC]; } poly;   /* d = -1 for zero */

static int Q, PCH, RDEG;
static uint8_t gadd[32][32], gmul[32][32], gneg[32], ginv[32];
static uint64_t qpow[40];

static void field_init(int q) {
    Q = q; int p = 0, r = 0;
    for (int t = 2; t <= q; t++) if (q % t == 0) { p = t; break; }
    for (int t = q; t > 1; t /= p) r++;
    PCH = p; RDEG = r;
    int mod[5] = {0};  /* x^r + mod[r-1] x^{r-1} + ... + mod[0] */
    if (r == 1) {}
    else if (q == 4) { mod[0] = 1; mod[1] = 1; }
    else if (q == 8) { mod[0] = 1; mod[1] = 1; mod[2] = 0; }
    else if (q == 9) { mod[0] = 1; mod[1] = 0; }
    else if (q == 16) { mod[0] = 1; mod[1] = 1; mod[2] = 0; mod[3] = 0; }
    else if (q == 25) { mod[0] = 2; mod[1] = 1; }
    else if (q == 27) { mod[0] = 1; mod[1] = 2; mod[2] = 0; } /* x^3+2x+1 over F3 */
    else { fprintf(stderr, "unsupported q\n"); exit(1); }
    for (int a = 0; a < q; a++) for (int b = 0; b < q; b++) {
        int da[5], db[5], s = 0, pw = 1, x = a, y = b;
        for (int i = 0; i < r; i++) { da[i] = x % p; x /= p; db[i] = y % p; y /= p; }
        for (int i = 0; i < r; i++) { s += ((da[i] + db[i]) % p) * pw; pw *= p; }
        gadd[a][b] = s;
        int pr[10] = {0};
        for (int i = 0; i < r; i++) for (int j = 0; j < r; j++) pr[i + j] = (pr[i + j] + da[i] * db[j]) % p;
        for (int t = 2 * r - 2; t >= r; t--) { int c = pr[t]; if (!c) continue; pr[t] = 0;
            for (int i = 0; i < r; i++) pr[t - r + i] = ((pr[t - r + i] - c * mod[i]) % p + p) % p; }
        s = 0; pw = 1; for (int i = 0; i < r; i++) { s += pr[i] * pw; pw *= p; }
        gmul[a][b] = s;
    }
    for (int a = 0; a < q; a++) { for (int b = 0; b < q; b++) { if (gadd[a][b] == 0) gneg[a] = b; if (gmul[a][b] == 1) ginv[a] = b; } }
    for (int a = 1; a < q; a++) if (gmul[a][ginv[a]] != 1) { fprintf(stderr, "field table broken\n"); exit(1); }
    qpow[0] = 1; for (int i = 1; i < 40; i++) qpow[i] = qpow[i - 1] * q;
}
#define GSUB(a,b) gadd[a][gneg[b]]

static void p_trim(poly *a) { while (a->d >= 0 && a->c[a->d] == 0) a->d--; }
static void p_set(poly *a, const poly *b) { a->d = b->d; memcpy(a->c, b->c, b->d + 1 > 0 ? b->d + 1 : 0); }
static void p_add(poly *r, const poly *a, const poly *b) {
    poly t; int d = a->d > b->d ? a->d : b->d; t.d = d;
    for (int i = 0; i <= d; i++) t.c[i] = gadd[i <= a->d ? a->c[i] : 0][i <= b->d ? b->c[i] : 0];
    p_trim(&t); *r = t;
}
static void p_neg(poly *r, const poly *a) { r->d = a->d; for (int i = 0; i <= a->d; i++) r->c[i] = gneg[a->c[i]]; }
static void p_sub(poly *r, const poly *a, const poly *b) { poly nb; p_neg(&nb, b); p_add(r, a, &nb); }
static void p_mul(poly *r, const poly *a, const poly *b) {
    poly t; if (a->d < 0 || b->d < 0) { r->d = -1; return; }
    t.d = a->d + b->d; memset(t.c, 0, t.d + 1);
    for (int i = 0; i <= a->d; i++) if (a->c[i]) for (int j = 0; j <= b->d; j++) t.c[i + j] = gadd[t.c[i + j]][gmul[a->c[i]][b->c[j]]];
    *r = t;
}
/* qt = a div b, rm = a mod b (either may be NULL) */
static void p_divmod(poly *qt, poly *rm, const poly *a, const poly *b) {
    poly r = *a, qq; int db = b->d; uint8_t inv = ginv[b->c[db]];
    qq.d = r.d - db; if (qq.d < 0) qq.d = -1; else memset(qq.c, 0, qq.d + 1);
    for (int i = r.d; i >= db; i--) { uint8_t c = gmul[r.c[i]][inv]; if (!c) continue; qq.c[i - db] = c;
        for (int j = 0; j <= db; j++) r.c[i - db + j] = GSUB(r.c[i - db + j], gmul[c][b->c[j]]); }
    r.d = db - 1 < r.d ? db - 1 : r.d; p_trim(&r); p_trim(&qq);
    if (qt) *qt = qq; if (rm) *rm = r;
}
static void p_monic(poly *a) { if (a->d < 0) return; uint8_t inv = ginv[a->c[a->d]]; for (int i = 0; i <= a->d; i++) a->c[i] = gmul[a->c[i]][inv]; }
static void p_gcd(poly *g, const poly *a, const poly *b) {
    poly x = *a, y = *b, r; while (y.d >= 0) { p_divmod(NULL, &r, &x, &y); x = y; y = r; } p_monic(&x); *g = x;
}
static uint64_t p_idx(const poly *a) { uint64_t s = 0; for (int i = a->d - 1; i >= 0; i--) s = s * Q + a->c[i]; return s; } /* monic */
static void p_from_idx(poly *a, int d, uint64_t idx) { a->d = d; for (int i = 0; i < d; i++) { a->c[i] = idx % Q; idx /= Q; } a->c[d] = 1; }
static uint64_t p_key(const poly *a) { uint64_t s = 0; for (int i = a->d; i >= 0; i--) s = s * Q + a->c[i]; return s * 64 + (a->d + 1); }
static void p_print(FILE *f, const poly *a) { if (a->d < 0) { fprintf(f, "0"); return; }
    for (int i = a->d; i >= 0; i--) fprintf(f, Q > 10 ? "%d%s" : "%d%s", a->c[i], (Q > 10 && i) ? "," : ""); }

/* ---------- progression: all P = f*h + r, h monic deg n - deg f; callback on index of P ---------- */
typedef void (*cbfn)(uint64_t idx, void *ctx);
static void prog(const poly *f, const poly *r, int n, cbfn cb, void *ctx) {
    int m = f->d, L = n - m; uint8_t cur[MAXC] = {0}, h[MAXC] = {0}; int64_t idx = 0;
    for (int i = 0; i <= m; i++) cur[L + i] = f->c[i];
    for (int i = 0; i <= r->d; i++) cur[i] = gadd[cur[i]][r->c[i]];
    for (int t = 0; t < n; t++) idx += (int64_t)cur[t] * qpow[t];
    cb((uint64_t)idx, ctx);
    for (;;) {
        int j = 0;
        while (j < L) { int o = h[j], nw = (o + 1) % Q; uint8_t dl = GSUB(nw, o); h[j] = nw;
            for (int i = 0; i <= m; i++) if (f->c[i]) { int t = j + i; uint8_t nv = gadd[cur[t]][gmul[dl][f->c[i]]];
                idx += ((int64_t)nv - cur[t]) * (int64_t)qpow[t]; cur[t] = nv; }
            if (nw) break; j++; }
        if (j == L) break;
        cb((uint64_t)idx, ctx);
    }
}

/* ---------- smallest-factor tables for monic polys of degree <= DMAX ---------- */
static int DMAX; static uint32_t *spf[40]; static uint64_t off[41];
/* code of monic poly g = off[deg]+idx */
static void code_to_poly(poly *a, uint32_t code) { int d = 0; while (off[d + 1] <= code) d++; p_from_idx(a, d, code - off[d]); }
struct spfctx { uint32_t *tab; uint32_t code; };
static void spf_cb(uint64_t idx, void *ctx) { struct spfctx *s = ctx; if (!s->tab[idx]) s->tab[idx] = s->code; }
static void spf_build(int D) {
    DMAX = D; off[0] = 0; for (int d = 0; d <= D; d++) off[d + 1] = off[d] + qpow[d];
    for (int d = 1; d <= D; d++) { spf[d] = calloc(qpow[d], 4); if (!spf[d]) { fprintf(stderr, "oom\n"); exit(1); } }
    poly zero = {.d = -1};
    for (int e = 1; e <= D; e++) for (uint64_t i = 0; i < qpow[e]; i++) {
        if (spf[e][i]) continue;
        uint32_t code = off[e] + i + 1; spf[e][i] = code; poly g; p_from_idx(&g, e, i);
        for (int d = 2 * e; d <= D; d++) { struct spfctx s = {spf[d], code}; prog(&g, &zero, d, spf_cb, &s); }
    }
}
/* factor monic a (deg <= DMAX) into primes[], exps[]; returns count */
static int factor(const poly *a, poly *pr, int *ex) {
    poly x = *a; int np = 0;
    while (x.d > 0) { uint32_t code = spf[x.d][p_idx(&x)] - 1; poly g; code_to_poly(&g, code);
        int e = 0; while (x.d > 0) { poly qt, rm; p_divmod(&qt, &rm, &x, &g); if (rm.d >= 0) break; x = qt; e++; }
        pr[np] = g; ex[np] = e; np++; }
    return np;
}
static int is_irr_small(const poly *a) { if (a->d < 1) return 0; return spf[a->d][p_idx(a)] - 1 == off[a->d] + p_idx(a); }

/* ---------- divisors ---------- */
#define MAXDIV 4096
static int divisors(poly *pr, int *ex, int np, poly *dv, int *code, int *radix) {
    /* code = mixed-radix exponent vector */
    int nd = 1; dv[0].d = 0; dv[0].c[0] = 1; code[0] = 0; int mult = 1;
    for (int i = 0; i < np; i++) { int cur = nd; radix[i] = mult;
        for (int t = 0; t < cur; t++) { poly w = dv[t]; for (int e = 1; e <= ex[i]; e++) { p_mul(&w, &w, &pr[i]);
            if (nd >= MAXDIV) { fprintf(stderr, "MAXDIV\n"); exit(1); } dv[nd] = w; code[nd] = code[t] + e * mult; nd++; } }
        mult *= ex[i] + 1; }
    return nd;
}

/* ---------- complete decision / count for one P (Lemma 1.3) ---------- */
static poly Apoly; static int K; static long tot2g;
/* returns number of canonical (lcm(a,b)=PX) witnesses if count, else 1/0 on first witness */
static long decide(const poly *P, int count, poly *wX, poly *wa, poly *wb) {
    int n = P->d, dx = n - K; long tot = 0; tot2g = 0;
    static poly pr[64], dv[MAXDIV], rs[MAXDIV]; static int ex[64], cd[MAXDIV], rdx[64];
    for (uint64_t ix = 0; ix < qpow[dx]; ix++) {
        poly X, AX, E; p_from_idx(&X, dx, ix); p_mul(&AX, &Apoly, &X); p_sub(&E, &AX, P);
        int np = dx > 0 ? factor(&X, pr, ex) : 0;
        /* merge P (coprime to X since deg E < n, E != 0) */
        pr[np] = *P; ex[np] = 1; np++;
        int nd = divisors(pr, ex, np, dv, cd, rdx);
        for (int i = 0; i < nd; i++) p_divmod(NULL, &rs[i], &dv[i], &E);
        for (int i = 0; i < nd; i++) for (int j = 0; j < nd; j++) {
            poly s; p_add(&s, &rs[i], &rs[j]); if (s.d >= 0) continue;
            poly ab; p_add(&ab, &dv[i], &dv[j]); if (ab.d < 0 || ab.c[ab.d] != E.c[E.d]) continue;
            if (count) { int ok = 1; for (int t = 0; t < np; t++) { int ea = cd[i] / rdx[t] % (ex[t] + 1), eb = cd[j] / rdx[t] % (ex[t] + 1);
                    if ((ea > eb ? ea : eb) != ex[t]) { ok = 0; break; } }
                if (ok) { tot++; if (cd[i] / rdx[np-1] % 2 && cd[j] / rdx[np-1] % 2) tot2g++; } }
            else { if (wX) { *wX = X; *wa = dv[i]; *wb = dv[j]; } return 1; }
        }
    }
    return tot;
}

/* ---------- main ---------- */
static uint16_t *cnt; static uint8_t *red;
static void cnt_cb(uint64_t idx, void *ctx) { (void)ctx; if (cnt[idx] < 65535) cnt[idx]++; }
static void red_cb(uint64_t idx, void *ctx) { (void)ctx; red[idx >> 3] |= 1 << (idx & 7); }

static uint64_t rng = 88172645463325252ULL;
static uint64_t xs(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: ffl_es q A n [nsample] [seed] [failfile]\n"); return 1; }
    field_init(atoi(argv[1]));
    { char buf[256]; strncpy(buf, argv[2], 255); int cs[64], nc = 0; char *t = strtok(buf, ",");
      while (t) { cs[nc++] = atoi(t); t = strtok(NULL, ","); }
      if (nc == 1 && strlen(argv[2]) > 1 && Q <= 10) { nc = 0; for (char *s = argv[2]; *s; s++) cs[nc++] = *s - '0'; }
      Apoly.d = nc - 1; for (int i = 0; i < nc; i++) Apoly.c[nc - 1 - i] = cs[i]; K = Apoly.d; }
    int n = atoi(argv[3]); long nsample = argc > 4 ? atol(argv[4]) : 0; if (argc > 5) rng ^= atoll(argv[5]) * 0x9E3779B97F4A7C15ULL;
    FILE *ff = argc > 6 ? fopen(argv[6], "w") : NULL;
    if (Apoly.c[K] != 1 || K < 1 || n <= K) { fprintf(stderr, "need monic A, 1 <= k < n\n"); return 1; }
    int D = n - K; if (n / 2 > D) D = n / 2; spf_build(D);
    uint64_t NP = qpow[n];
    /* irreducibles of degree n: sieve */
    red = calloc(NP / 8 + 1, 1); poly zero = {.d = -1};
    for (int e = 1; e <= n / 2; e++) for (uint64_t i = 0; i < qpow[e]; i++) { poly g; p_from_idx(&g, e, i); if (is_irr_small(&g)) prog(&g, &zero, n, red_cb, NULL); }
    /* Type II counts */
    cnt = calloc(NP, 2); if (!cnt || !red) { fprintf(stderr, "oom\n"); return 1; }
    static poly pr[64], dv[MAXDIV]; static int ex[64], cd[MAXDIV], rdx[64];
    for (int sa = 0; sa <= n - K; sa++) for (int sb = 0; sa + sb <= n - K; sb++)
    for (uint64_t ia = 0; ia < qpow[sa]; ia++) for (uint64_t ib = 0; ib < qpow[sb]; ib++) {
        poly a, b, g, S, f; p_from_idx(&a, sa, ia); p_from_idx(&b, sb, ib);
        p_gcd(&g, &a, &b); if (g.d != 0) continue;
        p_add(&S, &a, &b); if (S.d < 0) continue;
        p_mul(&f, &a, &b); p_mul(&f, &f, &Apoly);
        poly Sm = S; p_monic(&Sm); int np = Sm.d > 0 ? factor(&Sm, pr, ex) : 0;
        int nd = divisors(pr, ex, np, dv, cd, rdx);
        for (int t = 0; t < nd; t++) { poly E, mE; p_divmod(&E, NULL, &S, &dv[t]); p_neg(&mE, &E); prog(&f, &mE, n, cnt_cb, NULL); }
    }
    /* stats over irreducible P */
    poly Mm = {.d = -1}; double *cs1 = NULL; uint64_t *csn = NULL, *cs0 = NULL;
    if (getenv("FFL_MOD")) { char buf[256]; strncpy(buf, getenv("FFL_MOD"), 255); int cs[64], nc = 0; char *t = strtok(buf, ",");
        while (t) { cs[nc++] = atoi(t); t = strtok(NULL, ","); } Mm.d = nc - 1; for (int i = 0; i < nc; i++) Mm.c[nc - 1 - i] = cs[i];
        cs1 = calloc(qpow[Mm.d], 8); csn = calloc(qpow[Mm.d], 8); cs0 = calloc(qpow[Mm.d], 8); }
    uint64_t nirr = 0, nzero = 0, nfail = 0; double s1 = 0, s2 = 0; uint32_t mn = 1u << 30; uint64_t hist[8] = {0};
    for (uint64_t i = 0; i < NP; i++) { if (red[i >> 3] >> (i & 7) & 1) continue; poly P; p_from_idx(&P, n, i);
        if (!(K >= 1 && 1)) continue; /* P | A impossible: deg P = n > k */
        nirr++; uint32_t c = cnt[i];
        if (cs1) { poly rr; p_divmod(NULL, &rr, &P, &Mm); uint64_t key = 0; for (int t = Mm.d - 1; t >= 0; t--) key = key * Q + (t <= rr.d ? rr.c[t] : 0); cs1[key] += c; csn[key]++; if (!c) cs0[key]++; } s1 += c; s2 += (double)c * c; if (c < mn) mn = c; if (c < 8) hist[c]++;
        if (c == 0 && getenv("FFL_DUMP0") && nzero < 200) { printf("NII0 "); p_print(stdout, &P); printf("\n"); }
        if (c == 0) { nzero++; if (!decide(&P, 0, NULL, NULL, NULL)) { nfail++; if (ff) { p_print(ff, &P); fprintf(ff, "\n"); } } }
    }
    printf("q=%d A=", Q); p_print(stdout, &Apoly); printf(" n=%d irr=%llu NII0=%llu FAIL=%llu meanNII=%.3f sdNII=%.3f minNII=%u hist0-7:",
        n, (unsigned long long)nirr, (unsigned long long)nzero, (unsigned long long)nfail, s1 / nirr, s1 > 0 ? __builtin_sqrt(s2 / nirr - (s1 / nirr) * (s1 / nirr)) : 0, mn);
    for (int i = 0; i < 8; i++) printf(" %llu", (unsigned long long)hist[i]); printf("\n");
    if (cs1) for (uint64_t key = 0; key < qpow[Mm.d]; key++) if (csn[key]) { printf("  class ");
        for (int t = Mm.d - 1; t >= 0; t--) printf("%d%s", (int)(key / qpow[t] % Q), Q > 10 && t ? "," : "");
        printf(" n=%llu mean=%.3f nii0=%llu\n", (unsigned long long)csn[key], cs1[key] / csn[key], (unsigned long long)cs0[key]); }
    /* sample: full counts N(P) on random irreducible P, check N_II consistency */
    if (nsample < 0) { for (uint64_t i = 0; i < NP; i++) { if (red[i >> 3] >> (i & 7) & 1) continue; poly P; p_from_idx(&P, n, i);
        p_print(stdout, &P); printf(" %ld\n", decide(&P, 1, NULL, NULL, NULL)); } }
    if (nsample > 0) { double t1 = 0, t2 = 0; long mnN = 1L << 40; long done = 0;
        for (long s = 0; s < nsample * 50 && done < nsample; s++) { uint64_t i = xs() % NP; if (red[i >> 3] >> (i & 7) & 1) continue;
            poly P; p_from_idx(&P, n, i); long N = decide(&P, 1, NULL, NULL, NULL); done++; if (tot2g != cnt[i]) { printf("MISMATCH NII idx=%llu %ld vs %u\n", (unsigned long long)i, tot2g, cnt[i]); } t1 += N; t2 += (double)N * N; if (N < mnN) mnN = N; }
        printf("  sample=%ld meanN=%.3f sdN=%.3f minN=%ld\n", done, t1 / done, __builtin_sqrt(t2 / done - (t1 / done) * (t1 / done)), mnN); }
    if (ff) fclose(ff);
    return 0;
}
