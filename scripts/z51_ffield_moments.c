// z51_ffield_moments.c — factorial moments E[(W_sigma)_k], k = 1..8, of the number of rational words of ONE shape
// sigma = (s,a,b) over all monic f of degree n over F_p. Big monodromy (k-transitivity) predicts E[(W)_k] -> 1
// (a != b) as q -> infinity for every k <= D_sigma; exact CRT proves it for k(a+b) <= n (EXSET_FUNCTION_FIELD §3.9).
// Usage: z51_ffield_moments p n s a b
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
int main(int argc, char **argv) {
    int p = atoi(argv[1]), n = atoi(argv[2]), s = atoi(argv[3]), a = atoi(argv[4]), b = atoi(argv[5]);
    if (s + a + b != n) { fprintf(stderr, "bad shape\n"); return 1; }
    long long pw[64]; pw[0] = 1; for (int i = 1; i <= n; i++) pw[i] = pw[i - 1] * p;
    long long N = pw[n];
    uint16_t *W = calloc(N, sizeof(uint16_t));
    int t[64], v[64], A[64], f[64], u[64]; int dA = s + b;
    for (long long ti = 0; ti < pw[s]; ti++) {
        long long x = ti; for (int i = 0; i < s; i++) { t[i] = x % p; x /= p; } t[s] = 1;
        for (long long vi = 0; vi < pw[b]; vi++) {
            long long y = vi; for (int i = 0; i < b; i++) { v[i] = y % p; y /= p; } v[b] = 1;
            memset(A, 0, sizeof(A));
            for (int i = 0; i <= s; i++) for (int j = 0; j <= b; j++) A[i + j] = (A[i + j] + t[i] * v[j]) % p;
            A[0] = (A[0] + p - 1) % p;
            memset(f, 0, sizeof(f));
            for (int i = 0; i <= dA; i++) f[i + a] = (f[i + a] + A[i]) % p;
            for (int i = 0; i <= b; i++) f[i] = (f[i] + p - v[i]) % p;
            long long idx = 0; for (int i = 0; i < n; i++) idx += f[i] * pw[i];
            for (int i = 0; i < a; i++) u[i] = 0; u[a] = 1;
            for (long long ui = 0; ui < pw[a]; ui++) {
                W[idx]++;
                for (int i = 0; i < a; i++) {
                    u[i]++; int wrap = (u[i] == p); if (wrap) u[i] = 0;
                    for (int k = 0; k <= dA; k++) { int pos = i + k; int old = f[pos]; int nw = old + A[k]; if (nw >= p) nw -= p; f[pos] = nw; idx += (long long)(nw - old) * pw[pos]; }
                    if (!wrap) break;
                }
            }
        }
    }
    double mom[9] = {0}; long long zero = 0;
    for (long long i = 0; i < N; i++) {
        double w = W[i], ff = 1; if (W[i] == 0) zero++;
        for (int k = 1; k <= 8; k++) { ff *= (w - k + 1); mom[k] += ff; }
    }
    printf("p=%d n=%d shape=(%d,%d,%d) P0=%.5f", p, n, s, a, b, (double)zero / N);
    for (int k = 1; k <= 8; k++) printf(" m%d=%.4f", k, mom[k] / N);
    printf("\n");
    return 0;
}
