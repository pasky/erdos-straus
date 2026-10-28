/* z49_i3fable_crt.c — prime-Haar CRT model of the interior-word count I3 conditioned on n's local data.
 *
 * Model: n has independent residues r_l mod l^E (l^E < 2^62) for every prime l <= Pmax.  Types:
 *   gen   : r_l uniform mod l^E, optionally constrained (n ≡ r mod q for prime powers q);
 *   sq    : n = m^2 with m's residues s_l uniform (constraints apply to m), r_l = s_l^2;
 *   sq2   : n = 2 m^2 likewise.
 * A word (t,u,v) with u <= v is detected either by the larger endpoint v (a := -n mod v is the smaller endpoint;
 * word iff 3 <= a and a v | n + a + v, or a = 0 and v^2 | n + 2v), or — for v > X0 ~ sqrt(N) — by the pair
 * (u, A) with A = tu - 1 <= (N+u)/X0, u | A+1, 3 <= u <= (A+1)/3 and A | n + u (then v = (n+u)/A > X0).
 * N is the nominal size of n (the size enters only through the cut-offs 3uv <= N + u + v, enforced in both passes;
 * in count mode no cut-off is applied, i.e. n is treated as >> CAP^2).
 *
 * mode split: fixed-effort splitting over dyadic blocks of v up to X0 (fresh residues for untouched primes at
 *   each resampling), then a plain pass over the (u,A) pairs on the distinct survivors.  Prints the survival
 *   P1(X) = P(no interior word with larger endpoint <= X) at X = 8,16,..., then P2 = P(no word with v > X0 | ...)
 *   and P = P1 * P2 = model P(I3(n) = 0), with binomial errors, and survivor statistics.
 * mode count: plain sampling; mean number of words with v <= X per dyadic block and the (t mod 8, u mod 8)
 *   cell table of words with v <= CAP (both endpoints counted, i.e. ordered words).
 *
 * Usage: z49_i3fable_crt split N M seed type [q:r ...]       (e.g. split 2433600 10000 1 sq 2:0)
 *        z49_i3fable_crt count CAP M seed type [q:r ...]
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned __int128 u128; typedef uint64_t u64; typedef int64_t i64;
static u64 S[2] = {0x12345678abcdefULL, 0x9e3779b97f4a7c15ULL};
static inline u64 rnd(void) { u64 s1 = S[0]; const u64 s0 = S[1]; S[0] = s0; s1 ^= s1 << 23; S[1] = s1 ^ s0 ^ (s1 >> 17) ^ (s0 >> 26); return S[1] + s0; }
static inline u64 rndmod(u64 q) { return rnd() % q; }   /* q < 2^62, bias negligible */

static int *spf; static long Lspf;            /* smallest prime factor table up to Lspf */
static u64 *pw; static int *pidx; static long NP; static u64 *plist;   /* prime powers l^E, prime index */
static u64 inv_mod(u64 a, u64 m) { i64 old_r = (i64)(a % m), r = (i64)m, old_s = 1, s = 0; while (r) { i64 q = old_r / r, t = old_r - q * r; old_r = r; r = t; t = old_s - q * s; old_s = s; s = t; } i64 v = old_s % (i64)m; if (v < 0) v += (i64)m; return (u64)v; }

/* n mod prod(pr[i]^ex[i]) from the particle's residues R (indexed by prime index) */
static u64 crt_mod(const u64 *R, const u64 *pr, const int *ex, int k) {
    u64 x = 0, M = 1;
    for (int i = 0; i < k; i++) {
        u64 q = 1; for (int j = 0; j < ex[i]; j++) q *= pr[i];
        u64 r = R[pidx[pr[i]]] % q;
        u64 inv = inv_mod(M % q, q); u64 d = (r + q - x % q) % q; u64 tt = (u64)(((u128)d * inv) % q);
        x += M * tt; M *= q;
    }
    return x;
}
static int fac(u64 x, u64 *pr, int *ex) { int k = 0; while (x > 1) { u64 l = (u64)spf[x]; int e = 0; while (x % l == 0) { x /= l; e++; } pr[k] = l; ex[k] = e; k++; } return k; }
static int merge(const u64 *p1, const int *e1, int k1, const u64 *p2, const int *e2, int k2, u64 *pr, int *ex) {
    int k = 0; for (int i = 0; i < k1; i++) { pr[k] = p1[i]; ex[k] = e1[i]; k++; }
    for (int j = 0; j < k2; j++) { int f = 0; for (int i = 0; i < k1; i++) if (pr[i] == p2[j]) { ex[i] += e2[j]; f = 1; break; } if (!f) { pr[k] = p2[j]; ex[k] = e2[j]; k++; } }
    return k;
}
/* is there an interior word with larger endpoint v?  returns 1 and sets *tmod8,*umod8 if so */
static u64 PR_v[64]; static int EX_v[64]; static int K_v;      /* cached factorization of current v */
static u64 NOMN;   /* nominal size of n: interior needs 3uv <= n + u + v */
static int test_v(const u64 *R, u64 v, int *t8, int *u8) {
    u64 nv = crt_mod(R, PR_v, EX_v, K_v);
    u64 a = (v - nv % v) % v;
    u64 pr[64]; int ex[64]; int k;
    if (a == 0) { /* u = v: v^2 | n + 2v */
        if (3 * v * v > NOMN + 2 * v) return 0;
        for (int i = 0; i < K_v; i++) { pr[i] = PR_v[i]; ex[i] = 2 * EX_v[i]; } k = K_v;
        /* append 2^3 for t mod 8 */
        u64 pr2[64]; int ex2[64]; int k2 = k; for (int i = 0; i < k; i++) { pr2[i] = pr[i]; ex2[i] = ex[i]; }
        { int f = 0; for (int i = 0; i < k2; i++) if (pr2[i] == 2) { ex2[i] += 3; f = 1; } if (!f) { pr2[k2] = 2; ex2[k2] = 3; k2++; } }
        u64 nm = crt_mod(R, pr2, ex2, k2); u64 m = v * v; u64 s = (nm + 2 * v) % (8 * m);
        if (s % m) return 0; *t8 = (int)((s / m) & 7); *u8 = (int)(v & 7); return 2;
    }
    if (a < 3) return 0;
    if (3 * a * v > NOMN + a + v) return 0;   /* level t would be < 3: a free word, not interior */
    u64 pa[64]; int ea[64]; int ka = fac(a, pa, ea);
    k = merge(PR_v, EX_v, K_v, pa, ea, ka, pr, ex);
    { int f = 0; for (int i = 0; i < k; i++) if (pr[i] == 2) { ex[i] += 3; f = 1; } if (!f) { pr[k] = 2; ex[k] = 3; k++; } }
    u64 nm = crt_mod(R, pr, ex, k); u64 m = a * v; u64 s = (nm + a + v) % (8 * m);
    if (s % m) return 0; *t8 = (int)((s / m) & 7); *u8 = (int)(a & 7); return 1;
}
/* words with v > X0: pairs (u, A), A | n+u, u | A+1, 3 <= u <= (A+1)/3, A <= (N+u)/X0 */
static int test_tail(const u64 *R, u64 N, u64 X0) {
    u64 Amax = (N + X0) / X0 + 1;
    for (u64 A = 8; A <= Amax; A++) {
        u64 pr[64]; int ex[64]; int k = fac(A, pr, ex);
        u64 nA = crt_mod(R, pr, ex, k);           /* n mod A */
        u64 B = A + 1;
        for (u64 u = 3; u * 3 <= B; u++) if (B % u == 0) {
            if (A > (N + u) / X0) continue;        /* v = (n+u)/A would be <= X0: already covered */
            if ((nA + u) % A == 0) return 1;
        }
    }
    return 0;
}
/* sampling of residues */
static int TYPE; static int NC; static u64 CQ[32], CR[32], CL[32];   /* constraints q = l^j, residue r */
static void sample_prime(u64 *R, long i) {
    u64 l = plist[i], q = pw[l]; u64 s;
    int c = -1; for (int j = 0; j < NC; j++) if (CL[j] == l) c = j;
    if (c >= 0) s = CR[c] + CQ[c] * rndmod(q / CQ[c]); else s = rndmod(q);
    if (TYPE == 0) R[i] = s; else { u64 r = (u64)(((u128)s * s) % q); if (TYPE == 2) r = (u64)(((u128)2 * r) % q); R[i] = r; }
}
int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: %s split|count N|CAP M seed gen|sq|sq2 [q:r ...]\n", argv[0]); return 1; }
    int mode = strcmp(argv[1], "count") == 0; u64 N = strtoull(argv[2], 0, 10); long M = atol(argv[3]); S[0] ^= strtoull(argv[4], 0, 10) * 0x9E3779B97F4A7C15ULL; for (int i = 0; i < 20; i++) rnd();
    TYPE = strcmp(argv[5], "sq") == 0 ? 1 : strcmp(argv[5], "sq2") == 0 ? 2 : 0;
    NC = 0; for (int i = 6; i < argc; i++) { u64 q, r; if (sscanf(argv[i], "%llu:%llu", (unsigned long long *)&q, (unsigned long long *)&r) == 2) { CQ[NC] = q; CR[NC] = r; u64 l = q; for (u64 d = 2; d <= l; d++) if (l % d == 0) { CL[NC] = d; break; } NC++; } }
    u64 X0 = mode ? N : (u64)floor(sqrt((double)N)) + 2; NOMN = mode ? ~0ULL / 8 : N;
    long Pmax = (long)X0 + 10; Lspf = Pmax;
    spf = calloc(Lspf + 1, sizeof(int)); for (long i = 2; i <= Lspf; i++) if (!spf[i]) for (long j = i; j <= Lspf; j += i) if (!spf[j]) spf[j] = i;
    pw = calloc(Lspf + 1, 8); pidx = calloc(Lspf + 1, sizeof(int)); plist = calloc(Lspf + 1, 8); NP = 0;
    for (long l = 2; l <= Lspf; l++) if (spf[l] == l) { u64 q = 1; while ((u128)q * l < ((u128)1 << 62)) q *= l; pw[l] = q; pidx[l] = NP; plist[NP++] = l; }
    u64 *POP = malloc((size_t)M * NP * 8), *POP2 = malloc((size_t)M * NP * 8); int *alive = malloc(M * sizeof(int));
    if (!POP || !POP2 || !alive) { fprintf(stderr, "alloc failed (M*NP*16 = %.2f GB)\n", (double)M * NP * 16 / 1e9); return 2; }
    for (long p = 0; p < M; p++) for (long i = 0; i < NP; i++) sample_prime(POP + (size_t)p * NP, i);
    printf("# mode=%s N=%llu M=%ld type=%s X0=%llu NP=%ld constraints:", mode ? "count" : "split", (unsigned long long)N, M, argv[5], (unsigned long long)X0, NP);
    for (int j = 0; j < NC; j++) printf(" %llu:%llu", (unsigned long long)CQ[j], (unsigned long long)CR[j]); printf("\n");
    if (mode) {   /* count mode */
        long cell[8][8] = {{0}}; double blk[64] = {0}; long blkn = 0;
        for (long p = 0; p < M; p++) { const u64 *R = POP + (size_t)p * NP;
            for (u64 v = 3; v <= X0; v++) { K_v = fac(v, PR_v, EX_v); int t8, u8, w = test_v(R, v, &t8, &u8);
                if (w) { int b = 0; while ((1ULL << (b + 1)) <= v) b++; blk[b] += (w == 2 ? 1 : 2); cell[t8][u8] += 1; if (w == 1) cell[t8][v & 7] += 1; } } }
        printf("# mean number of words with larger endpoint in [2^b, 2^(b+1)) per sample, and cumulative mean up to 2^(b+1)\n");
        double cum = 0; for (int b = 1; b < 64 && (1ULL << b) <= X0; b++) { cum += blk[b] / M; printf("b=%2d  mean=%.4f  cum=%.4f\n", b, blk[b] / M, cum); }
        printf("# cell table (t mod 8 rows, endpoint mod 8 cols), ordered words with larger endpoint <= %llu\n", (unsigned long long)X0);
        for (int r = 0; r < 8; r++) { for (int c = 0; c < 8; c++) printf("%8ld", cell[r][c]); printf("\n"); }
        (void)blkn; return 0;
    }
    /* split mode */
    double P1 = 1; u64 lo = 3; int stage = 0; long nsurv = M; long long distinct = M;
    for (int b = 3; ; b++) {
        u64 hi = (1ULL << b); if (hi > X0) hi = X0;
        for (long p = 0; p < M; p++) alive[p] = 1;
        for (u64 v = lo; v <= hi; v++) { K_v = fac(v, PR_v, EX_v); int t8, u8; for (long p = 0; p < M; p++) if (alive[p] && test_v(POP + (size_t)p * NP, v, &t8, &u8)) alive[p] = 0; }
        nsurv = 0; for (long p = 0; p < M; p++) nsurv += alive[p];
        double s = (double)nsurv / M; P1 *= s; stage++;
        printf("X=%llu  stage-survival=%.5f  P1(no word with v<=X)=%.4e  survivors=%ld\n", (unsigned long long)hi, s, P1, nsurv);
        if (nsurv == 0) { printf("P1=0 (population died); increase M\n"); return 0; }
        if (hi >= X0) break;
        /* resample with fresh residues for primes > hi */
        long *idx = malloc(nsurv * sizeof(long)); long c = 0; for (long p = 0; p < M; p++) if (alive[p]) idx[c++] = p;
        long first_untouched = NP; for (long i = 0; i < NP; i++) if (plist[i] > hi) { first_untouched = i; break; }
        for (long p = 0; p < M; p++) { long src = idx[rndmod(nsurv)]; u64 *dst = POP2 + (size_t)p * NP; memcpy(dst, POP + (size_t)src * NP, first_untouched * 8); for (long i = first_untouched; i < NP; i++) sample_prime(dst, i); }
        free(idx); u64 *tmp = POP; POP = POP2; POP2 = tmp; lo = hi + 1;
    }
    /* tail pass on the distinct survivors (no resampling after the last stage) */
    long n2 = 0; long c3 = 0, c5 = 0, c4 = 0, c8 = 0, c7 = 0, c9 = 0;
    for (long p = 0; p < M; p++) if (alive[p]) { const u64 *R = POP + (size_t)p * NP; if (!test_tail(R, N, X0)) { n2++; alive[p] = 2;
            u64 r2 = R[pidx[2]] % 64, r3 = R[pidx[3]] % 9, r5 = R[pidx[5]] % 5, r7 = R[pidx[7]] % 7;
            c4 += (r2 % 4 == 0); c8 += (r2 % 8 == 0); c3 += (r3 % 3 == 0); c9 += (r3 == 0); c5 += (r5 == 0); c7 += (r7 == 0); } }
    double P2 = (double)n2 / nsurv; double P = P1 * P2;
    printf("P1(X0=%llu)=%.4e  tail: %ld of %ld survivors have no word with v>X0 -> P2=%.4f (+-%.4f)  P(I3=0)=%.4e\n",
           (unsigned long long)X0, P1, n2, nsurv, P2, nsurv ? sqrt(P2 * (1 - P2) / nsurv) : 0, P);
    if (n2) printf("zero-survivors: frac 4|n=%.3f 8|n=%.3f 3|n=%.3f 9|n=%.3f 5|n=%.3f 7|n=%.3f\n", (double)c4 / n2, (double)c8 / n2, (double)c3 / n2, (double)c9 / n2, (double)c5 / n2, (double)c7 / n2);
    (void)distinct; return 0;
}
