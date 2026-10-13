// cf_census: for all odd n <= N, count positive words (t,u,v) of X_n (tuv-u-v=n, letters >= 1)
// and the number with chi = (-A/n) = -1, A = tu-1. Output per n (odd): n W Nminus  (to stdout, filtered by mode)
// usage: cf_census N mode   mode: all | primes1mod8 | squares
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int jacobi(long long a, long long n) {
    a %= n; if (a < 0) a += n;
    int r = 1;
    while (a) {
        while ((a & 1) == 0) { a >>= 1; long long m = n & 7; if (m == 3 || m == 5) r = -r; }
        long long t = a; a = n; n = t;
        if ((a & 3) == 3 && (n & 3) == 3) r = -r;
        a %= n;
    }
    return n == 1 ? r : 0;
}
int main(int argc, char **argv) {
    long long N = atoll(argv[1]);
    const char *mode = argc > 2 ? argv[2] : "all";
    int *W = calloc(N + 1, sizeof(int)), *M = calloc(N + 1, sizeof(int));
    for (long long t = 1; t <= N + 2; t++)
        for (long long u = 1;; u++) {
            long long A = t * u - 1;
            // v >= 1: n = A v - u >= A - u
            long long lower = (A - u >= 1) ? A - u : 2 * A - u;
            if (lower > N) break;
            if (A <= 0) { // t=u=1: n = -1 for all v... A=0 -> n=-u <0
                continue;
            }
            for (long long v = 1;; v++) {
                long long n = A * v - u;
                if (n > N) break;
                if (n < 1 || (n & 1) == 0) continue;
                W[n]++;
                if (jacobi(-A, n) == -1) M[n]++;
            }
        }
    char *comp = calloc(N + 1, 1);
    for (long long i = 2; i * i <= N; i++) if (!comp[i]) for (long long j = i * i; j <= N; j += i) comp[j] = 1;
    for (long long n = 3; n <= N; n += 2) {
        int pr = !comp[n];
        long long r = 0; while ((r + 1) * (r + 1) <= n) r++;
        int sq = (r * r == n);
        if (!strcmp(mode, "all") || (!strcmp(mode, "primes1mod8") && pr && n % 8 == 1) || (!strcmp(mode, "squares") && sq))
            printf("%lld %d %d\n", n, W[n], M[n]);
    }
    return 0;
}
