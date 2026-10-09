/* m13d_wit.c — complete ET-class witness engine at a node x + L*Z (task O103).
 *
 * Finds ALL (or the first) ET classes (seven families, mordell_lib conventions) whose modulus M divides L
 * and which contain the progression x + L*Z.  Same reductions as scripts/m13c_witness.py
 * (POINTWISE_MORDELL13C §2), re-organised for speed (POINTWISE_MORDELL13D §1):
 *  (A) II3 (a,d,e=f), I2 (a,c=d,f), I3 (c=a,d,f):  f | L odd, m = 4ad | L, gcd(f,m)=1, m | x+f
 *      => m | G_f := gcd(L_f, x+f), L_f = part of L coprime to f; then test f | x+4a^2d, a x+d, x^2+4a^2d.
 *  (B) m = 4Q | L:  I1 (a,d,f), ad = Q, f | am+1, f = -x mod m (f<m) or f = (am+1)/g, g = -1/x mod m;
 *      II1 / I4 (a,b,e): ab = Q, e | a+b, e = -x resp. -1/x mod m (then e <= a+b <= Q+1, and
 *      min(a,b) <= 2Q/e).
 *  (C) II2 (a,d,f): f | L, f = 3 mod 4, ad | A=(f+1)/4, x = -4a^2 d mod f (A factored by Pollard rho).
 * Hypothesis 4 | L.  Requires L < 2^126.
 * Optional `req` (a prime power exactly dividing L): only classes with req | M are reported
 * (used for children of nodes known to be open: a class with M | L_parent would cover the parent).
 *
 * I/O (stdin): lines "L x req mode"  (mode 0 = first witness, 1 = all).  Output per line:
 *   "N k" then k lines "fam p1 p2 p3"; I1 found via g is printed as "I1g a d g" (f = (4a^2d+1)/g).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef unsigned __int128 u128;
typedef __int128 i128;
typedef uint64_t u64;

static u128 parse(const char *s) { u128 v = 0; while (*s >= '0' && *s <= '9') v = v * 10 + (*s++ - '0'); return v; }
static void pr(FILE *o, u128 v) { char b[64]; int i = 63; b[i] = 0; if (!v) b[--i] = '0'; while (v) { b[--i] = '0' + (int)(v % 10); v /= 10; } fputs(b + i, o); }

static u128 mulmod(u128 a, u128 b, u128 m) {
    if (m == 1) return 0;
    a %= m; b %= m;
    if ((m >> 64) == 0) return (u128)((u64)a) * (u64)b % m;
    if ((a >> 64) == 0 && (b >> 64) == 0) return (a * b) % m;
    u128 r = 0;               /* m < 2^127: additions do not overflow */
    while (b) { if (b & 1) { r += a; if (r >= m) r -= m; } a += a; if (a >= m) a -= m; b >>= 1; }
    return r;
}
static u128 gcd128(u128 a, u128 b) { while (b) { u128 t = a % b; a = b; b = t; } return a; }
/* inverse of a mod m (gcd must be 1), m >= 1 */
static u64 inv64(u64 a, u64 m) {
    int64_t t = 0, nt = 1; u64 r = m, nr = a % m;
    while (nr) { u64 q = r / nr; int64_t tt = t - (int64_t)q * nt; t = nt; nt = tt; u64 rr = r - q * nr; r = nr; nr = rr; }
    if (r != 1) { fprintf(stderr, "inv64: not invertible\n"); exit(2); }
    if (t < 0) t += (int64_t)m;
    return (u64)t;
}
static u128 inv128(u128 a, u128 m) {
    if (m == 1) return 0;
    if ((m >> 63) == 0) return inv64((u64)(a % m), (u64)m);
    i128 t = 0, nt = 1; u128 r = m, nr = a % m;
    while (nr) { u128 q = r / nr; i128 tt = t - (i128)q * nt; t = nt; nt = tt; u128 rr = r - q * nr; r = nr; nr = rr; }
    if (r != 1) { fprintf(stderr, "inv128: not invertible\n"); exit(2); }
    if (t < 0) t += (i128)m;
    return (u128)t;
}

/* ---------------- factor of L ---------------- */
#define MAXP 40
static int K; static u64 P[MAXP]; static int E[MAXP]; static u128 PP[MAXP];
static u128 Lcur = 0;
static void factorL(u128 L) {
    K = 0; u64 p = 2;
    while (L > 1) {
        if (L % p == 0) { int e = 0; u128 q = 1; while (L % p == 0) { L /= p; e++; q *= p; } P[K] = p; E[K] = e; PP[K] = q; K++; }
        p++;
        if (p > 100000) { fprintf(stderr, "L not smooth\n"); exit(2); }
    }
}
/* odd divisors f of L with their prime masks */
typedef struct { u128 v; unsigned mask; } dv;
static dv *ODD = 0; static int nODD = 0, capODD = 0;
static u128 *D4 = 0; static int nD4 = 0, capD4 = 0;  /* divisors of L/4 (unsorted) */
static void gen_odd(int i, u128 v, unsigned mask) {
    if (i == K) { if (nODD == capODD) { capODD = capODD ? 2 * capODD : 1024; ODD = realloc(ODD, capODD * sizeof(dv)); } ODD[nODD].v = v; ODD[nODD].mask = mask; nODD++; return; }
    if (P[i] == 2) { gen_odd(i + 1, v, mask); return; }
    u128 w = v; for (int e = 0; e <= E[i]; e++) { gen_odd(i + 1, w, e ? (mask | (1u << i)) : mask); w *= P[i]; }
}
static int E4[MAXP];
static void gen_d4(int i, u128 v) {
    if (i == K) { if (nD4 == capD4) { capD4 = capD4 ? 2 * capD4 : 1024; D4 = realloc(D4, capD4 * sizeof(u128)); } D4[nD4++] = v; return; }
    u128 w = v; for (int e = 0; e <= E4[i]; e++) { gen_d4(i + 1, w); w *= P[i]; }
}

/* ---------------- output ---------------- */
static int MODE; static int nout; static char outbuf[1 << 20]; static int outlen;
static int emit(const char *fam, u128 p1, u128 p2, u128 p3) {
    nout++;
    FILE *o = fmemopen(outbuf + outlen, sizeof(outbuf) - outlen - 1, "w");
    fprintf(o, "%s ", fam); pr(o, p1); fputc(' ', o); pr(o, p2); fputc(' ', o); pr(o, p3); fputc('\n', o);
    long n = ftell(o); fclose(o); outlen += (int)n;
    if (outlen > (int)sizeof(outbuf) - 200) { fprintf(stderr, "outbuf\n"); exit(2); }
    return MODE == 0;   /* stop? */
}

/* ---------------- (A) ---------------- */
static u128 X, REQ;
static int gE[MAXP];          /* exponents of G/4 (2-part already reduced by 2) */
static u128 curf, xf, x2f;    /* x mod f, x^2 mod f */
static int reqA_m;            /* req must divide m */
static int stopA;
/* enumerate a,d with a*d = Q | G/4 : choose for each prime exponents ia,id with ia+id <= gE */
static void recA(int i, u128 a, u128 d, int hasreq) {
    if (stopA) return;
    if (i == K) {
        if (reqA_m && !hasreq) return;
        u128 f = curf;
        u128 a2d4 = mulmod(mulmod(4 * a, a, f), d, f);
        if ((xf + a2d4) % f == 0 && emit("II3", a, d, f)) { stopA = 1; return; }
        if ((mulmod(a, xf, f) + d % f) % f == 0 && emit("I2", a, d, f)) { stopA = 1; return; }
        if ((x2f + a2d4) % f == 0 && emit("I3", a, d, f)) { stopA = 1; return; }
        return;
    }
    u128 pa = 1;
    for (int ia = 0; ia <= gE[i]; ia++) {
        u128 pd = 1;
        for (int id = 0; ia + id <= gE[i]; id++) {
            int full = 0;
            if (reqA_m && PP[i] == REQ) { /* req = p^E: need total exponent of p in m = 4ad equal E */
                int tot = ia + id + (P[i] == 2 ? 2 : 0);
                full = (tot == E[i]);
            }
            recA(i + 1, a * pa, d * pd, hasreq | full);
            if (stopA) return;
            pd *= P[i];
        }
        pa *= P[i];
    }
}
static int famA(void) {
    stopA = 0;
    for (int j = 0; j < nODD; j++) {
        u128 f = ODD[j].v; unsigned mask = ODD[j].mask;
        if (((X + f) & 3) != 0) continue;
        int req_in_f = (REQ > 1) && (f % REQ == 0);
        reqA_m = (REQ > 1) && !req_in_f;
        u128 Lf = Lcur;
        for (int i = 0; i < K; i++) if (mask >> i & 1) Lf /= PP[i];
        u128 G = gcd128(Lf, X + f);
        if (reqA_m && G % REQ) continue;
        if (G % 4) continue;
        u128 g = G / 4;
        for (int i = 0; i < K; i++) { int e = 0; while (g % P[i] == 0) { g /= P[i]; e++; } gE[i] = e; }
        curf = f; xf = X % f; x2f = mulmod(xf, xf, f);
        recA(0, 1, 1, 0);
        if (stopA) return 1;
    }
    return 0;
}

/* ---------------- (B) ---------------- */
static int qE[MAXP];
static u128 *DQ = 0; static int nDQ = 0, capDQ = 0;
static void gen_q(int i, u128 v) {
    if (i == K) { if (nDQ == capDQ) { capDQ = capDQ ? 2 * capDQ : 1024; DQ = realloc(DQ, capDQ * sizeof(u128)); } DQ[nDQ++] = v; return; }
    u128 w = v; for (int e = 0; e <= qE[i]; e++) { gen_q(i + 1, w); w *= P[i]; }
}
static void divs_of(u128 Q) {
    nDQ = 0; u128 q = Q;
    for (int i = 0; i < K; i++) { int e = 0; while (q % P[i] == 0) { q /= P[i]; e++; } qE[i] = e; }
    gen_q(0, 1);
}
static int cmpu(const void *a, const void *b) { u128 x = *(const u128 *)a, y = *(const u128 *)b; return x < y ? -1 : x > y; }

/* all a | Q with a == a0 mod f0 (1 <= a <= Q); calls cb */
static int I1_try(u128 m, u128 Q, u128 h, int isg) {
    /* h = f0 or g0 (< m, coprime to m); need a | Q, h | a m + 1 */
    if (h == 1) {
        divs_of(Q);
        for (int t = 0; t < nDQ; t++) if (emit(isg ? "I1g" : "I1", DQ[t], Q / DQ[t], 1)) return 1;
        return 0;
    }
    u128 a0 = (h - inv128(m % h, h)) % h;   /* a == -1/m mod h, a0 in [1,h-1] */
    if (a0 == 0 || a0 > Q) return 0;
    u128 cnt = (Q - a0) / h + 1;
    if (cnt <= 64) {
        for (u128 a = a0; a <= Q; a += h)
            if (Q % a == 0 && emit(isg ? "I1g" : "I1", a, Q / a, h)) return 1;
    } else {
        divs_of(Q);
        for (int t = 0; t < nDQ; t++) if (DQ[t] % h == a0 && emit(isg ? "I1g" : "I1", DQ[t], Q / DQ[t], h)) return 1;
    }
    return 0;
}
/* II1/I4: ab = Q, e | a+b; min(a,b) <= 2Q/e.  D4 sorted ascending. */
static int E14_try(u128 Q, u128 e, const char *fam) {
    if (e > Q + 1) return 0;
    u128 B = 2 * Q / e;
    for (int t = 0; t < nD4 && D4[t] <= B; t++) {
        u128 s = D4[t];
        if (Q % s) continue;
        u128 b = Q / s;
        if ((s + b) % e) continue;
        if (emit(fam, s, b, e)) return 1;
        if (b > B && emit(fam, b, s, e)) return 1;
    }
    return 0;
}
static u128 XI;
static int famB(void) {
    for (int t = 0; t < nD4; t++) {
        u128 Q = D4[t], m = 4 * Q;
        if (REQ > 1 && m % REQ) continue;
        u128 xm = X % m, xim = XI % m;
        u128 f0 = m - xm, g0 = m - xim;
        if (I1_try(m, Q, f0, 0)) return 1;
        if (I1_try(m, Q, g0, 1)) return 1;
        if (E14_try(Q, f0, "II1")) return 1;
        if (E14_try(Q, g0, "I4")) return 1;
    }
    return 0;
}

/* ---------------- (C) II2 ---------------- */
static int is_prime_u128(u128 n);
static void factor_rec(u128 n, u128 *fs, int *nf);
static u128 powmod(u128 a, u128 e, u128 m) { u128 r = 1 % m; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int is_prime_u128(u128 n) {
    if (n < 2) return 0;
    static const u64 sp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71};
    for (int i = 0; i < 20; i++) { if (n == sp[i]) return 1; if (n % sp[i] == 0) return 0; }
    u128 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
    for (int i = 0; i < 20; i++) {   /* 20 bases: deterministic far beyond 2^64, probabilistic-strong above */
        u128 x = powmod(sp[i], d, n);
        if (x == 1 || x == n - 1) continue;
        int ok = 0; for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } }
        if (!ok) return 0;
    }
    return 1;
}
static u128 rho(u128 n) {
    if (n % 2 == 0) return 2;
    for (u128 c = 1;; c++) {
        u128 x = 2, y = 2, d = 1, q = 1; int it = 0;
        u128 ys = 0, xs = 0;
        while (d == 1) {
            xs = x; ys = y;
            for (int k = 0; k < 64; k++) {
                x = (mulmod(x, x, n) + c) % n; y = (mulmod(y, y, n) + c) % n; y = (mulmod(y, y, n) + c) % n;
                u128 df = x > y ? x - y : y - x; q = mulmod(q, df, n);
            }
            d = gcd128(q, n); it++;
        }
        if (d == n) {   /* backtrack */
            x = xs; y = ys; d = 1;
            while (d == 1) { x = (mulmod(x, x, n) + c) % n; y = (mulmod(y, y, n) + c) % n; y = (mulmod(y, y, n) + c) % n; d = gcd128(x > y ? x - y : y - x, n); }
        }
        if (d != n) return d;
    }
}
static void factor_rec(u128 n, u128 *fs, int *nf) {
    if (n == 1) return;
    if (is_prime_u128(n)) { fs[(*nf)++] = n; return; }
    u128 d = rho(n); factor_rec(d, fs, nf); factor_rec(n / d, fs, nf);
}
static u128 AP[128]; static int AE[128], nAP;
static void factorA(u128 A) {
    u128 fs[256]; int nf = 0; nAP = 0;
    for (u64 p = 2; p < 1000 && A > 1; p++) if (A % p == 0) { int e = 0; while (A % p == 0) { A /= p; e++; } AP[nAP] = p; AE[nAP++] = e; }
    factor_rec(A, fs, &nf);
    qsort(fs, nf, sizeof(u128), cmpu);
    for (int i = 0; i < nf; i++) { if (nAP && AP[nAP - 1] == fs[i]) AE[nAP - 1]++; else { AP[nAP] = fs[i]; AE[nAP++] = 1; } }
}
/* global cache f -> sorted residues r = -4a^2 d mod f over ad | A = (f+1)/4 (built lazily, flushed when full) */
typedef struct { u128 r, a, d; } II2e;
typedef struct { u128 f; II2e *e; int n; } II2f;
static u128 *ADV; static int nADV, capADV;
static void gen_A(int i, u128 v) {
    if (i == nAP) { if (nADV == capADV) { capADV = capADV ? 2 * capADV : 1024; ADV = realloc(ADV, capADV * sizeof(u128)); } ADV[nADV++] = v; return; }
    u128 w = v; for (int e = 0; e <= AE[i]; e++) { gen_A(i + 1, w); w *= AP[i]; }
}
static int cmpe(const void *a, const void *b) { u128 x = ((const II2e *)a)->r, y = ((const II2e *)b)->r; return x < y ? -1 : x > y; }
#define HBITS 21
#define HCAP (1L << HBITS)
static II2f *H = 0; static long Hused = 0, Hent = 0;
static long hslot(u128 f) {
    long h = (long)(((u64)f ^ (u64)(f >> 64)) * 0x9E3779B97F4A7C15ull >> (64 - HBITS));
    while (H[h].f && H[h].f != f) h = (h + 1) & (HCAP - 1);
    return h;
}
static II2f *get_II2(u128 f) {
    if (!H) H = calloc(HCAP, sizeof(II2f));
    long h = hslot(f);
    if (H[h].f == f) return &H[h];
    if (Hused > HCAP / 2 || Hent > 4000000) {
        for (long t = 0; t < HCAP; t++) free(H[t].e);
        memset(H, 0, HCAP * sizeof(II2f)); Hused = Hent = 0; h = hslot(f);
    }
    u128 A = (f + 1) / 4; factorA(A); nADV = 0; gen_A(0, 1);
    II2e *arr = 0; int n = 0, cap = 0;
    for (int t = 0; t < nADV; t++) {             /* pairs (a,d): a | A, d | A/a */
        u128 a = ADV[t], R = A / a;
        for (int s = 0; s < nADV; s++) {
            u128 d = ADV[s]; if (R % d) continue;
            if (n == cap) { cap = cap ? 2 * cap : 64; arr = realloc(arr, cap * sizeof(II2e)); }
            u128 r = (f - mulmod(mulmod(4 * a % f, a, f), d, f)) % f;
            arr[n].r = r; arr[n].a = a; arr[n].d = d; n++;
        }
    }
    qsort(arr, n, sizeof(II2e), cmpe);
    H[h].f = f; H[h].e = arr; H[h].n = n; Hused++; Hent += n;
    return &H[h];
}
static int famC(void) {
    for (int j = 0; j < nODD; j++) {
        u128 f = ODD[j].v;
        if (f % 4 != 3) continue;
        if (REQ > 1 && f % REQ) continue;
        II2f *c = get_II2(f);
        u128 r = X % f; II2e *e = c->e; int lo = 0, hi = c->n;
        while (lo < hi) { int md = (lo + hi) / 2; if (e[md].r < r) lo = md + 1; else hi = md; }
        for (; lo < c->n && e[lo].r == r; lo++) if (emit("II2", e[lo].a, e[lo].d, f)) return 1;
    }
    return 0;
}

static void setL(u128 L) {
    if (L == Lcur) return;
    Lcur = L; factorL(L);
    nODD = 0; gen_odd(0, 1, 0);
    for (int i = 0; i < K; i++) E4[i] = (P[i] == 2) ? E[i] - 2 : E[i];
    nD4 = 0; gen_d4(0, 1);
    qsort(D4, nD4, sizeof(u128), cmpu);
}

int main(int argc, char **argv) {
    char l1[128], l2[128], l3[128]; int mode;
    while (scanf("%127s %127s %127s %d", l1, l2, l3, &mode) == 4) {
        u128 L = parse(l1), x = parse(l2), req = parse(l3);
        MODE = mode; nout = 0; outlen = 0; outbuf[0] = 0;
        if (L % 4 || L >> 126) { fprintf(stderr, "bad L\n"); return 2; }
        setL(L);
        X = x % L; REQ = req;
        if (gcd128(X, L) != 1) { fprintf(stderr, "x not unit\n"); return 2; }
        XI = inv128(X, L);
        if (!famA() && !famB()) famC();
        printf("N %d\n", nout); fwrite(outbuf, 1, outlen, stdout); fflush(stdout);
    }
    return 0;
}
