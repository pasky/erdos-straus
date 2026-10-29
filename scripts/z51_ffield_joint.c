// z51_ffield_joint.c — independence test for Conjecture 3.6 of EXSET_FUNCTION_FIELD.md.
// For every monic f of degree n over F_p, records per-shape word counts W_sigma(f) for all non-degenerate shapes,
// groups the genuine shapes (s,a,b >= 1) into unordered classes {(s,a,b),(s,b,a)} (identical fibres),
// and the f+1 data (shapes with s = 0: number of monic divisors of f+1 of each degree).
// Reports: per class c: mean, P(W_c = 0); joint P(all genuine classes 0) vs product of marginals;
// P(all genuine 0 AND f+1 condition) vs product; pairwise E[W_c W_d] (c != d) vs E[W_c] E[W_d].
// f+1 condition (U-failure part): n odd -> f+1 irreducible; n even -> f+1 has no monic divisor of odd degree.
// Usage: z51_ffield_joint p n
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static int p, n; static long long pw[64];

int main(int argc, char **argv) {
    p = atoi(argv[1]); n = atoi(argv[2]);
    pw[0] = 1; for (int i = 1; i <= n; i++) pw[i] = pw[i - 1] * p;
    long long N = pw[n];
    // classes: genuine shapes keyed by (s, min(a,b)); f+1 profile: divisors of degree b, 1<=b<=n-1 (shape (0,n-b,b))
    int cls[64][64]; int ncls = 0; int cs[64], ca[64], cb[64];
    for (int s = 1; s <= n; s++) for (int a = 1; s + a < n; a++) { int b = n - s - a; if (b < a) continue; cls[s][a] = ncls; cs[ncls] = s; ca[ncls] = a; cb[ncls] = b; ncls++; }
    uint8_t *W = calloc(N * ncls, 1);
    uint8_t *odddiv = calloc(N, 1);   // number of monic divisors of f+1 of odd degree in [1, n-1] (capped)
    uint8_t *anydiv = calloc(N, 1);   // number of proper monic divisors of f+1 (capped)
    if (!W || !odddiv || !anydiv) { fprintf(stderr, "oom\n"); return 1; }
    for (int s = 0; s <= n; s++) for (int b = 0; s + b <= n; b++) {
        int a = n - s - b;
        if (s + b == 0 || s + a == 0) continue;
        int genuine = (s >= 1 && a >= 1 && b >= 1);
        int f1 = (s == 0 && a >= 1 && b >= 1);
        if (!genuine && !f1) continue;
        int c = -1; if (genuine) c = cls[s][a < b ? a : b];
        int t[64], v[64], A[64], f[64], u[64];
        for (long long ti = 0; ti < pw[s]; ti++) {
            long long x = ti; for (int i = 0; i < s; i++) { t[i] = x % p; x /= p; } t[s] = 1;
            for (long long vi = 0; vi < pw[b]; vi++) {
                long long y = vi; for (int i = 0; i < b; i++) { v[i] = y % p; y /= p; } v[b] = 1;
                int dA = s + b; memset(A, 0, sizeof(A));
                for (int i = 0; i <= s; i++) for (int j = 0; j <= b; j++) A[i + j] = (A[i + j] + t[i] * v[j]) % p;
                A[0] = (A[0] + p - 1) % p;
                memset(f, 0, sizeof(f));
                for (int i = 0; i <= dA; i++) f[i + a] = (f[i + a] + A[i]) % p;
                for (int i = 0; i <= b; i++) f[i] = (f[i] + p - v[i]) % p;
                long long idx = 0; for (int i = 0; i < n; i++) idx += f[i] * pw[i];
                for (int i = 0; i < a; i++) u[i] = 0; u[a] = 1;
                for (long long ui = 0; ui < pw[a]; ui++) {
                    if (genuine) { if (W[idx * ncls + c] < 255) W[idx * ncls + c]++; }
                    else { if (anydiv[idx] < 255) anydiv[idx]++; if ((b & 1) && odddiv[idx] < 255) odddiv[idx]++; }
                    for (int i = 0; i < a; i++) {
                        u[i]++; int wrap = (u[i] == p); if (wrap) u[i] = 0;
                        for (int k = 0; k <= dA; k++) { int pos = i + k; int old = f[pos]; int nw = old + A[k]; if (nw >= p) nw -= p; f[pos] = nw; idx += (long long)(nw - old) * pw[pos]; }
                        if (!wrap) break;
                    }
                }
            }
        }
    }
    double mean[64] = {0}, zero[64] = {0}, prod[64][64] = {{0}};
    double allz = 0, f1c = 0, allz_f1 = 0;
    for (long long i = 0; i < N; i++) {
        int az = 1;
        for (int c = 0; c < ncls; c++) { int w = W[i * ncls + c]; mean[c] += w; if (w == 0) zero[c]++; else az = 0; }
        for (int c = 0; c < ncls; c++) for (int d = c + 1; d < ncls; d++) prod[c][d] += (double)W[i * ncls + c] * W[i * ncls + d];
        int cond = (n & 1) ? (anydiv[i] == 0) : (odddiv[i] == 0);
        if (cond) f1c++;
        if (az) allz++;
        if (az && cond) allz_f1++;
    }
    printf("p=%d n=%d classes=%d\n", p, n, ncls);
    double pz = 1;
    for (int c = 0; c < ncls; c++) { mean[c] /= N; zero[c] /= N; pz *= zero[c];
        printf("  class (s=%d,{%d,%d}): mean=%.4f P0=%.4f\n", cs[c], ca[c], cb[c], mean[c], zero[c]); }
    f1c /= N; allz /= N; allz_f1 /= N;
    printf("  P(all genuine 0)=%.5f  product=%.5f  ratio=%.4f\n", allz, pz, allz / pz);
    printf("  P(f+1 cond)=%.5f  P(all0 & f+1)=%.5f  product=%.5f  ratio=%.4f\n", f1c, allz_f1, pz * f1c, allz_f1 / (pz * f1c));
    for (int c = 0; c < ncls; c++) for (int d = c + 1; d < ncls; d++)
        printf("  E[W%d W%d]=%.4f vs %.4f\n", c, d, prod[c][d] / N, mean[c] * mean[d]);
    return 0;
}
