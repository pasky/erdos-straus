// z51_ffield_enum.c — FF analogue of U (and ES5-analogue) over F_p[T], p prime, p ≡ 3 (mod 4).
// For every monic f of degree n, counts U-witness words:
//   W_U(f) = #{(t,u,v) monic : f = t u v − u − v, deg u ≥ 1, (deg t odd or deg v odd)}.
// (shift v, divisor A = t v − 1 ≡ −1 (mod v) of f + v, cofactor u nonconstant, colour forced at ∞:
//  (−v/A) = (−1)^{(deg t+1)(deg v+1)−1} = −1.)
// Optional: W_E(f) = #{words with gcd(u,v)=1, (uv/f) = −1}: (uv/f) = (−1)^{s(a+b)+ab} for monic words.
// Usage: z51_ffield_enum p n [es5] [dumpfail_file]
// Output: summary lines; with dumpfail, writes the failing non-square f (coefficient vectors).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static int p, n;
static long long pw[64];

static int pdeg(const int *a, int da) { while (da >= 0 && a[da] == 0) da--; return da; }
// gcd degree of monic-ish polys over F_p (returns degree of gcd)
static int inv_mod(int x) { int r = 1, e = p - 2, b = x % p; while (e) { if (e & 1) r = r * b % p; b = b * b % p; e >>= 1; } return r; }
static int gcd_deg(const int *u, int du, const int *v, int dv) {
    int a[64], b[64]; memcpy(a, u, sizeof(int) * (du + 1)); memcpy(b, v, sizeof(int) * (dv + 1));
    int da = du, db = dv;
    while (db >= 0) {
        // a mod b
        int ib = inv_mod(b[db]);
        while (da >= db) {
            int c = a[da] * ib % p;
            for (int i = 0; i <= db; i++) a[da - db + i] = ((a[da - db + i] - c * b[i]) % p + p) % p;
            da = pdeg(a, da - 1);
        }
        // swap
        int tmp[64]; memcpy(tmp, a, sizeof(int) * 64); memcpy(a, b, sizeof(int) * 64); memcpy(b, tmp, sizeof(int) * 64);
        int t = da; da = db; db = t;
    }
    return da;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    p = atoi(argv[1]); n = atoi(argv[2]);
    int do_es5 = argc > 3 && strcmp(argv[3], "es5") == 0;
    const char *dump = argc > 4 ? argv[4] : NULL;
    pw[0] = 1; for (int i = 1; i <= n; i++) pw[i] = pw[i - 1] * p;
    long long N = pw[n];
    uint16_t *WU = calloc(N, sizeof(uint16_t));
    uint16_t *WE = do_es5 ? calloc(N, sizeof(uint16_t)) : NULL;
    if (!WU || (do_es5 && !WE)) { fprintf(stderr, "oom\n"); return 1; }
    long long nshapesU = 0, nshapesE = 0;
    for (int s = 0; s <= n; s++) for (int b = 0; s + b <= n; b++) {
        int a = n - s - b;
        int isU = (a >= 1) && ((s & 1) || (b & 1));
        int isE = ((s * (a + b) + a * b) & 1);
        if (!isU && !(do_es5 && isE)) continue;
        if (s + b == 0 || s + a == 0) continue; // degenerate (f not of degree n)
        if (isU) nshapesU++;
        if (do_es5 && isE) nshapesE++;
        // enumerate t (deg s), v (deg b), u (deg a), all monic
        int t[64], v[64], u[64], A[64], f[64];
        long long Tn = pw[s], Vn = pw[b], Un = pw[a];
        for (long long ti = 0; ti < Tn; ti++) {
            long long x = ti; for (int i = 0; i < s; i++) { t[i] = x % p; x /= p; } t[s] = 1;
            for (long long vi = 0; vi < Vn; vi++) {
                long long y = vi; for (int i = 0; i < b; i++) { v[i] = y % p; y /= p; } v[b] = 1;
                int dA = s + b;
                memset(A, 0, sizeof(A));
                for (int i = 0; i <= s; i++) for (int j = 0; j <= b; j++) A[i + j] = (A[i + j] + t[i] * v[j]) % p;
                A[0] = (A[0] + p - 1) % p;
                // f = A*T^a - v + sum u_i A T^i, start u_i = 0
                memset(f, 0, sizeof(f));
                for (int i = 0; i <= dA; i++) f[i + a] = (f[i + a] + A[i]) % p;
                for (int i = 0; i <= b; i++) f[i] = (f[i] + p - v[i]) % p;
                if (f[n] != 1) { fprintf(stderr, "not monic? s=%d a=%d b=%d\n", s, a, b); return 2; }
                long long idx = 0; for (int i = 0; i < n; i++) idx += f[i] * pw[i];
                for (int i = 0; i < a; i++) u[i] = 0; u[a] = 1;
                for (long long ui = 0; ui < Un; ui++) {
                    if (isU) WU[idx]++;
                    if (do_es5 && isE) {
                        if (gcd_deg(u, a, v, b) == 0) WE[idx]++;
                    }
                    // odometer increment of u, updating f += A*T^i
                    for (int i = 0; i < a; i++) {
                        u[i]++; int wrap = (u[i] == p); if (wrap) u[i] = 0;
                        for (int k = 0; k <= dA; k++) {
                            int pos = i + k; int old = f[pos]; int nw = old + A[k]; if (nw >= p) nw -= p;
                            f[pos] = nw; idx += (long long)(nw - old) * pw[pos];
                        }
                        if (!wrap) break;
                    }
                }
            }
        }
    }
    // squares
    char *sq = calloc(N, 1);
    long long nsq = 0;
    if (n % 2 == 0) {
        int m = n / 2, g[64], h[64];
        for (long long gi = 0; gi < pw[m]; gi++) {
            long long x = gi; for (int i = 0; i < m; i++) { g[i] = x % p; x /= p; } g[m] = 1;
            memset(h, 0, sizeof(h));
            for (int i = 0; i <= m; i++) for (int j = 0; j <= m; j++) h[i + j] = (h[i + j] + g[i] * g[j]) % p;
            long long idx = 0; for (int i = 0; i < n; i++) idx += h[i] * pw[i];
            if (!sq[idx]) { sq[idx] = 1; nsq++; }
        }
    }
    long long failU = 0, failU_ns = 0, sqfailU = 0, failE = 0, failE_ns = 0, sqfailE = 0, sumW = 0;
    long long hist[64] = {0};
    FILE *df = dump ? fopen(dump, "w") : NULL;
    for (long long i = 0; i < N; i++) {
        sumW += WU[i];
        hist[WU[i] < 63 ? WU[i] : 63]++;
        if (WU[i] == 0) { failU++; if (sq[i]) sqfailU++; else { failU_ns++; if (df) { long long x = i; for (int k = 0; k < n; k++) { fprintf(df, "%lld ", x % p); x /= p; } fprintf(df, "\n"); } } }
        if (do_es5 && WE[i] == 0) { failE++; if (sq[i]) sqfailE++; else failE_ns++; }
    }
    if (df) fclose(df);
    printf("p=%d n=%d N=%lld shapesU=%lld meanWU=%.6f squares=%lld sqfailU=%lld failU_nonsq=%lld frac=%.6f\n",
           p, n, N, nshapesU, (double)sumW / N, nsq, sqfailU, failU_ns, (double)failU_ns / N);
    if (do_es5) printf("ES5: shapesE=%lld sqfailE=%lld failE_nonsq=%lld frac=%.6f\n", nshapesE, sqfailE, failE_ns, (double)failE_ns / N);
    printf("histWU:"); for (int k = 0; k < 20; k++) printf(" %lld", hist[k]); printf("\n");
    return 0;
}
