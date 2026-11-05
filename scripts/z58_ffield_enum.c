// z58_ffield_enum.c — function-field analogue of (★)/(MS) over F_p[T], p prime ≡ 3 (mod 4).
//
// (★)_q word of a monic f of degree n:  (t,u,v) monic with  f = t u v − u − v  and  deg t odd.
// (Dictionary: t = 4C, u = u, v = B; "4 | t" ↦ "deg t odd" (colour forced at ∞); n ≡ 1 (4) ↦ deg f even.)
// R_q(f) := #(★)_q words (ordered).  Sub-lines by s = deg t:  class 0: s = 1;  class 1: s ≡ 1 (4), s ≥ 5;
// class 2: s ≡ 3 (4).   Mode "U" instead counts z51's U_q witnesses (a ≥ 1, s or b odd) in class 0 (cross-check).
//
// Also classifies every f: square / irreducible / composite non-square (sieve by products).
// Usage: z58_ffield_enum p n mode(star|U) outprefix
// Writes  <outprefix>.sum (summary) and <outprefix>.zeros (one line per non-square f that is a zero of the full
// family, or an irreducible zero of the s≡1 (4) or s≡3 (4) sub-line:
//   idx coeffs(low..high) type(S/P/C) R_full R_s1 R_s1mod4 R_s3mod4 [counts saturate at 65535]).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static int p, n;
static long long pw[64];

static void pmul(const int *a, int da, const int *b, int db, int *c) { // c = a*b, deg da+db
    for (int i = 0; i <= da + db; i++) c[i] = 0;
    for (int i = 0; i <= da; i++) if (a[i]) for (int j = 0; j <= db; j++) c[i + j] = (c[i + j] + a[i] * b[j]) % p;
}
static void setmonic(int *x, int d, long long code) { // lower coeffs from base-p code, leading 1
    for (int i = 0; i < d; i++) { x[i] = code % p; code /= p; }
    x[d] = 1;
}

static uint16_t *cnt[3];

static inline void bump(uint16_t *c, long long idx) { if (c[idx] != 65535) c[idx]++; }

// inner loop: f starts at f0 (degree n monic, coefficients f0[0..n-1]); iterate over all q^k lower-coefficient
// vectors of the inner variable of degree k; each digit increment of position i adds T^i * M (deg dm) to f.
static void inner(int *f0, int k, const int *M, int dm, uint16_t *c) {
    int f[64]; memcpy(f, f0, sizeof(int) * (n + 1));
    long long idx = 0; for (int j = 0; j < n; j++) idx += f[j] * pw[j];
    int dig[64]; memset(dig, 0, sizeof dig);
    long long tot = pw[k];
    for (long long it = 0; it < tot; it++) {
        bump(c, idx);
        if (it + 1 == tot) break;
        int i = 0;
        for (;;) {
            // add T^i * M
            for (int j = 0; j <= dm; j++) if (M[j]) {
                int pos = i + j; int o = f[pos]; int nw = o + M[j]; if (nw >= p) nw -= p;
                f[pos] = nw; idx += (long long)(nw - o) * pw[pos];
            }
            dig[i]++;
            if (dig[i] < p) break;
            dig[i] = 0; i++;
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: p n star|U outprefix\n"); return 1; }
    p = atoi(argv[1]); n = atoi(argv[2]);
    int modeU = strcmp(argv[3], "U") == 0;
    const char *pref = argv[4];
    pw[0] = 1; for (int i = 1; i <= n; i++) pw[i] = pw[i - 1] * p;
    long long N = pw[n];
    for (int c = 0; c < 3; c++) { cnt[c] = calloc(N, sizeof(uint16_t)); if (!cnt[c]) { fprintf(stderr, "oom\n"); return 1; } }
    long long nsh[3] = {0, 0, 0};
    for (int s = 0; s <= n; s++) for (int b = 0; s + b <= n; b++) {
        int a = n - s - b;
        if (s + b == 0 || s + a == 0) continue;
        int cls;
        if (modeU) { if (!((a >= 1) && ((s & 1) || (b & 1)))) continue; cls = 0; }
        else {
            if (!(s & 1)) continue;
            cls = (s == 1) ? 0 : ((s % 4 == 1) ? 1 : 2);
        }
        nsh[cls]++;
        // choose inner variable = largest degree
        int t[64], u[64], v[64], M[128], X[128], f0[128];
        int inn = (s >= a && s >= b) ? 0 : (a >= b ? 1 : 2);
        if (inn == 0) {
            for (long long ui = 0; ui < pw[a]; ui++) { setmonic(u, a, ui);
            for (long long vi = 0; vi < pw[b]; vi++) { setmonic(v, b, vi);
                pmul(u, a, v, b, M); // M = uv
                memset(f0, 0, sizeof(int) * (n + 1));
                for (int j = 0; j <= a + b; j++) f0[s + j] = M[j];
                for (int j = 0; j <= a; j++) f0[j] = (f0[j] - u[j] + p) % p;
                for (int j = 0; j <= b; j++) f0[j] = (f0[j] - v[j] + p) % p;
                inner(f0, s, M, a + b, cnt[cls]);
            } }
        } else {
            // inner = u (deg a) with other = v (deg b); or inner = v with other = u: symmetric, so
            // write: inner var w (deg k), other var o (deg l): f = w*(t*o - 1) - o
            int k = (inn == 1) ? a : b, l = (inn == 1) ? b : a;
            int *o = (inn == 1) ? v : u;
            for (long long ti = 0; ti < pw[s]; ti++) { setmonic(t, s, ti);
            for (long long oi = 0; oi < pw[l]; oi++) { setmonic(o, l, oi);
                pmul(t, s, o, l, M); M[0] = (M[0] - 1 + p) % p; // M = t o - 1, deg s+l
                memset(f0, 0, sizeof(int) * (n + 1));
                for (int j = 0; j <= s + l; j++) f0[k + j] = M[j];
                for (int j = 0; j <= l; j++) f0[j] = (f0[j] - o[j] + p) % p;
                inner(f0, k, M, s + l, cnt[cls]);
            } }
        }
        (void)X;
    }
    // classification sieve: 0 = irreducible, 1 = composite, 2 = square
    uint8_t *ty = calloc(N, 1);
    {
        int g[64], h[64], P[128];
        for (int k = 1; k <= n / 2; k++)
            for (long long gi = 0; gi < pw[k]; gi++) { setmonic(g, k, gi);
                for (long long hi = 0; hi < pw[n - k]; hi++) { setmonic(h, n - k, hi);
                    pmul(g, k, h, n - k, P);
                    long long idx = 0; for (int j = 0; j < n; j++) idx += P[j] * pw[j];
                    if (ty[idx] == 0) ty[idx] = 1;
                } }
        if (n % 2 == 0) for (long long gi = 0; gi < pw[n / 2]; gi++) { setmonic(g, n / 2, gi);
            pmul(g, n / 2, g, n / 2, P);
            long long idx = 0; for (int j = 0; j < n; j++) idx += P[j] * pw[j];
            ty[idx] = 2; }
    }
    char fn[512]; snprintf(fn, sizeof fn, "%s.zeros", pref);
    FILE *fz = fopen(fn, "w");
    // families: 0 full (any class), 1 s=1 (cls0), 2 s≡1 mod 4 (cls0|cls1), 3 s≡3 mod 4 (cls2)
    long long zero[4][3]; memset(zero, 0, sizeof zero);
    long long ntype[3] = {0, 0, 0};
    long double sum[4][3]; memset(sum, 0, sizeof sum);
    long long mod3irr[3] = {0, 0, 0}; // R_full mod 3 among irreducibles
    static long long hist[2][256]; // histogram of R_full: [irr, comp]
    for (long long idx = 0; idx < N; idx++) {
        int T = ty[idx]; ntype[T]++;
        long long r[4];
        r[1] = cnt[0][idx]; r[2] = (long long)cnt[0][idx] + cnt[1][idx]; r[3] = cnt[2][idx];
        r[0] = r[2] + r[3];
        int anyz = 0;
        for (int fam = 0; fam < 4; fam++) { sum[fam][T] += r[fam]; if (r[fam] == 0) { zero[fam][T]++; anyz = 1; } }
        if (T == 0) mod3irr[r[0] % 3]++;
        if (T != 2) hist[T][r[0] < 255 ? r[0] : 255]++;
        // record: every non-square zero of the full family, and irreducible zeros of the half-mass sub-lines
        int rec = (r[0] == 0) || (T == 0 && (r[2] == 0 || r[3] == 0));
        (void)anyz;
        if (rec && T != 2) {
            fprintf(fz, "%lld ", idx);
            long long x = idx; for (int j = 0; j < n; j++) { fprintf(fz, "%lld", x % p); x /= p; }
            fprintf(fz, "1 %c %lld %lld %lld %lld\n", "PCS"[T], r[0], r[1], r[2], r[3]);
        }
    }
    fclose(fz);
    snprintf(fn, sizeof fn, "%s.sum", pref);
    FILE *fs = fopen(fn, "w");
    FILE *outs[2] = {stdout, fs};
    for (int o = 0; o < 2; o++) {
        FILE *F = outs[o];
        fprintf(F, "q=%d n=%d mode=%s shapes(cls0,cls1,cls2)=%lld,%lld,%lld  #irr=%lld #comp=%lld #sq=%lld\n",
                p, n, modeU ? "U" : "star", nsh[0], nsh[1], nsh[2], ntype[0], ntype[1], ntype[2]);
        const char *nm[4] = {modeU ? "U" : "full", "s=1", "s=1mod4", "s=3mod4"};
        for (int fam = 0; fam < (modeU ? 1 : 4); fam++)
            fprintf(F, "  %-8s zeros: irr=%lld comp=%lld sq=%lld | mean R: irr=%.4Lf comp=%.4Lf sq=%.4Lf all=%.4Lf\n", nm[fam],
                    zero[fam][0], zero[fam][1], zero[fam][2],
                    ntype[0] ? sum[fam][0] / ntype[0] : 0.0L, ntype[1] ? sum[fam][1] / ntype[1] : 0.0L,
                    ntype[2] ? sum[fam][2] / ntype[2] : 0.0L, (sum[fam][0] + sum[fam][1] + sum[fam][2]) / N);
        if (!modeU) fprintf(F, "  R_full mod 3 among irreducibles: %lld %lld %lld\n", mod3irr[0], mod3irr[1], mod3irr[2]);
        for (int T = 0; T < 2; T++) {
            fprintf(F, "  hist R_full %s (R:count, R<=40):", T ? "comp" : "irr");
            for (int v = 0; v <= 40; v++) if (hist[T][v]) fprintf(F, " %d:%lld", v, hist[T][v]);
            fprintf(F, "\n");
        }
    }
    fclose(fs);
    return 0;
}
