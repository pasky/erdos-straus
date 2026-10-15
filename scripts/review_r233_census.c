/* R233 from-scratch census: for odd non-square n = 1 (8), n < N, count over all positive words (t,u,v),
   tuv - u - v = n (ordered):  Ntot, Nm (chi = -1), U (no clean side), U2 (A and B unclean),
   minmin = least min(t,u,v) over unforced words.
   Cleanliness of a side is multiplicative: N_t = A B, N_u = A v, N_v = B u.
   usage: census N primes_only(0/1) > out   ; output lines: n Ntot Nm U U2 minmin  (all n in scope) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

static uint32_t *spf;
static int64_t N;

static int jac(int64_t a, int64_t n) { /* Jacobi (a/n), n odd > 0 */
    int s = 1; a %= n; if (a < 0) a += n;
    while (a) {
        while (!(a & 1)) { a >>= 1; int r = n & 7; if (r == 3 || r == 5) s = -s; }
        int64_t t = a; a = n; n = t;
        if ((a & 3) == 3 && (n & 3) == 3) s = -s;
        a %= n;
    }
    return n == 1 ? s : 0;
}
static int clean(int64_t x, int64_t n) {
    while (x > 1) {
        int64_t r = spf[x];
        if (jac(r, n) == -1) return 0;
        while (x % r == 0) x /= r;
    }
    return 1;
}
static double SN[5], SM[5], SU[5]; /* strata: min=1, 2, 3..9, 10..49, >=50 */
static int bin(int64_t m) { return m == 1 ? 0 : m == 2 ? 1 : m < 10 ? 2 : m < 50 ? 3 : 4; }
int main(int argc, char **argv) {
    N = atoll(argv[1]); int primes_only = atoi(argv[2]);
    int64_t lo = argc > 3 ? atoll(argv[3]) : 0, hi = argc > 4 ? atoll(argv[4]) : 0;
    int64_t S = 2 * N + 8;
    spf = calloc(S + 1, 4);
    for (int64_t i = 2; i <= S; i++) if (!spf[i]) for (int64_t j = i; j <= S; j += i) if (!spf[j]) spf[j] = i;
    int64_t M = N / 8 + 1;
    int32_t *Nt = calloc(M, 4), *Nm = calloc(M, 4), *U = calloc(M, 4), *U2 = calloc(M, 4);
    int32_t *mm = malloc(M * 4);
    char *ok = calloc(M, 1);
    for (int64_t k = 0; k < M; k++) {
        int64_t n = 8 * k + 1; mm[k] = 1 << 30;
        if (n >= N || n < 9) continue;
        int64_t r = (int64_t)sqrtl((long double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++;
        if (r * r == n) continue;
        if (primes_only && spf[n] != n) continue;
        ok[k] = 1;
    }
    for (int64_t t = 1; t <= N + 2; t++) {
        for (int64_t u = 1;; u++) {
            int64_t m = t * u - 1;
            if (m == 0) continue;
            int64_t nlow = (t == 1) ? u - 2 : u * (t - 1) - 1; /* least n over v >= 1 with n >= -1 */
            if (nlow >= N) break;
            int64_t vmin = (u + 1 + m - 1) / m; if (vmin < 1) vmin = 1;
            for (int64_t v0 = vmin; v0 < vmin + 8; v0++) {
                int64_t n0 = v0 * m - u;
                if (((n0 % 8) + 8) % 8 != 1) continue;
                for (int64_t v = v0;; v += 8) {
                    int64_t n = v * m - u;
                    if (n >= N) break;
                    if (n < 1) continue;
                    int64_t k = n >> 3;
                    if (!ok[k]) continue;
                    int64_t A = m, B = t * v - 1;
                    int chi = jac(A, n);
                    Nt[k]++;
                    int unf, u2;
                    if (chi == -1) { Nm[k]++; unf = 1; u2 = 1; }
                    else {
                        int cA = clean(A, n), cB = clean(B, n);
                        u2 = !cA && !cB;
                        int forced = (cA && cB) || (cA && clean(v, n)) || (cB && clean(u, n));
                        unf = !forced;
                    }
                    if (unf) { U[k]++; int64_t mn = t < u ? t : u; if (v < mn) mn = v; if (mn < mm[k]) mm[k] = mn; }
                    if (u2) U2[k]++;
                    if (n >= lo && n < hi) { int64_t mn = t < u ? t : u; if (v < mn) mn = v; int b = bin(mn);
                        SN[b]++; SM[b] += (chi == -1); SU[b] += unf; }
                }
            }
        }
    }
    if (hi) for (int m0 = 0; m0 < 5; m0++) { double a = 0, b = 0, c = 0;
        for (int j = m0; j < 5; j++) { a += SN[j]; b += SM[j]; c += SU[j]; }
        fprintf(stderr, "stratum min>=%d: N=%.0f N-/N=%.3f N-/U=%.3f\n", (int[]){1, 2, 3, 10, 50}[m0], a, b / a, b / c); }
    for (int64_t k = 0; k < M; k++) if (ok[k])
        printf("%lld %d %d %d %d %d\n", (long long)(8 * k + 1), Nt[k], Nm[k], U[k], U2[k], mm[k] == (1 << 30) ? 0 : mm[k]);
    return 0;
}
