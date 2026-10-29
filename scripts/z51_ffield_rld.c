// z51_ffield_rld.c — prime-modulus U family over F_p[T] (p prime ≡ 3 mod 4) and the RLD-U test.
// Forbidden classes: f ≡ −v (mod A), A monic irreducible, deg A ≤ z (and < n), v monic | A+1,
// (deg A odd or deg v odd)  [Def 1.4 of EXSET_FUNCTION_FIELD.md]. Equivalently: U-witness words (t,u,v)
// with A = tv − 1 irreducible, deg A ≤ z.
// Output, for each z = 1..n−1: number of non-square f avoiding all classes with deg A ≤ z ("sifted"),
// the Mertens product M(z) = prod_{deg A ≤ z} (1 − w(A)/|A|), mass mu(z) = sum w(A)/|A|, and ratio sifted/(q^n M(z)).
// Usage: z51_ffield_rld p n
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>

static int p, n;
static long long pw[64];
static long long off[64];      // offset of degree-d monic polys in the table
static char *isirr;            // irreducibility flag for monic polys of degree 1..n-1
static int *wcount;            // admissible (t,v) pairs per prime A

static long long midx(const int *a, int d) { long long x = 0; for (int i = 0; i < d; i++) x += a[i] * pw[i]; return off[d] + x; }

int main(int argc, char **argv) {
    p = atoi(argv[1]); n = atoi(argv[2]);
    pw[0] = 1; for (int i = 1; i <= n; i++) pw[i] = pw[i - 1] * p;
    off[0] = 0; for (int d = 1; d <= n; d++) off[d] = off[d - 1] + pw[d - 1];
    long long T = off[n];
    isirr = malloc(T); memset(isirr, 1, T);
    wcount = calloc(T, sizeof(int));
    // sieve reducibles: products of monic g (deg i) and h (deg d−i), 1 ≤ i ≤ d−i, d ≤ n−1
    for (int d = 2; d <= n - 1; d++) for (int i = 1; 2 * i <= d; i++) {
        int g[64], h[64], r[64];
        for (long long gi = 0; gi < pw[i]; gi++) {
            long long x = gi; for (int k = 0; k < i; k++) { g[k] = x % p; x /= p; } g[i] = 1;
            for (long long hi = 0; hi < pw[d - i]; hi++) {
                long long y = hi; for (int k = 0; k < d - i; k++) { h[k] = y % p; y /= p; } h[d - i] = 1;
                memset(r, 0, sizeof(int) * (d + 1));
                for (int a = 0; a <= i; a++) for (int b = 0; b <= d - i; b++) r[a + b] = (r[a + b] + g[a] * h[b]) % p;
                isirr[midx(r, d)] = 0;
            }
        }
    }
    long long N = pw[n];
    uint8_t *minz = malloc(N); memset(minz, 255, N);   // least deg A of a prime-family hit
    for (int s = 0; s <= n; s++) for (int b = 0; s + b <= n - 1; b++) {
        int a = n - s - b; int dA = s + b;
        if (a < 1 || dA < 1) continue;
        if (!((s & 1) || (b & 1))) continue;
        int t[64], v[64], A[64], f[64], u[64];
        for (long long ti = 0; ti < pw[s]; ti++) {
            long long x = ti; for (int i = 0; i < s; i++) { t[i] = x % p; x /= p; } t[s] = 1;
            for (long long vi = 0; vi < pw[b]; vi++) {
                long long y = vi; for (int i = 0; i < b; i++) { v[i] = y % p; y /= p; } v[b] = 1;
                memset(A, 0, sizeof(A));
                for (int i = 0; i <= s; i++) for (int j = 0; j <= b; j++) A[i + j] = (A[i + j] + t[i] * v[j]) % p;
                A[0] = (A[0] + p - 1) % p;
                long long Ai = midx(A, dA);
                if (!isirr[Ai]) continue;
                wcount[Ai]++;
                memset(f, 0, sizeof(f));
                for (int i = 0; i <= dA; i++) f[i + a] = (f[i + a] + A[i]) % p;
                for (int i = 0; i <= b; i++) f[i] = (f[i] + p - v[i]) % p;
                long long idx = 0; for (int i = 0; i < n; i++) idx += f[i] * pw[i];
                for (int i = 0; i < a; i++) u[i] = 0; u[a] = 1;
                for (long long ui = 0; ui < pw[a]; ui++) {
                    if (minz[idx] > dA) minz[idx] = dA;
                    for (int i = 0; i < a; i++) {
                        u[i]++; int wrap = (u[i] == p); if (wrap) u[i] = 0;
                        for (int k = 0; k <= dA; k++) { int pos = i + k; int old = f[pos]; int nw = old + A[k]; if (nw >= p) nw -= p; f[pos] = nw; idx += (long long)(nw - old) * pw[pos]; }
                        if (!wrap) break;
                    }
                }
            }
        }
    }
    // squares
    char *sq = calloc(N, 1);
    if (n % 2 == 0) {
        int m = n / 2, g[64], h[64];
        for (long long gi = 0; gi < pw[m]; gi++) {
            long long x = gi; for (int i = 0; i < m; i++) { g[i] = x % p; x /= p; } g[m] = 1;
            memset(h, 0, sizeof(h));
            for (int i = 0; i <= m; i++) for (int j = 0; j <= m; j++) h[i + j] = (h[i + j] + g[i] * g[j]) % p;
            long long idx = 0; for (int i = 0; i < n; i++) idx += h[i] * pw[i];
            sq[idx] = 1;
        }
    }
    // Mertens products per z; w(A) = admissible pairs − [deg A odd] (v=1 and v=A+1 give the same class)
    double logM[64] = {0}, mu[64] = {0};
    for (int d = 1; d <= n - 1; d++) {
        double lm = 0, mm = 0;
        for (long long i = 0; i < pw[d]; i++) {
            long long Ai = off[d] + i; if (!isirr[Ai]) continue;
            int w = wcount[Ai] - (d & 1);
            double x = (double)w / (double)pw[d];
            lm += log1p(-x); mm += x;
        }
        logM[d] = logM[d - 1] + lm; mu[d] = mu[d - 1] + mm;
    }
    for (int z = 1; z <= n - 1; z++) {
        long long sifted = 0, siftsq = 0;
        for (long long i = 0; i < N; i++) if (minz[i] > z) { if (sq[i]) siftsq++; else sifted++; }
        double M = exp(logM[z]);
        printf("p=%d n=%d z=%d mu=%.4f M=%.6e sifted_nonsq=%lld sifted_sq=%lld ratio=%.4f\n",
               p, n, z, mu[z], M, sifted, siftsq, sifted / (M * (double)N));
    }
    return 0;
}
