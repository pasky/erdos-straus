// si_census: for odd n <= N, weighted counts of positive words (t,u,v) of X_n: tuv-u-v=n, chi=(-A/n), A=tu-1.
// Output (odd n): n Np Nm NpI NmI SpT SmT
//   Np/Nm: all words with chi=+1/-1; NpI/NmI: interior words (t,u,v>=2); SpT/SmT: sum of t over chi=+1/-1 words.
// usage: si_census N
#include <stdio.h>
#include <stdlib.h>
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
    long long *c[6];
    for (int i = 0; i < 6; i++) c[i] = calloc(N + 1, sizeof(long long));
    for (long long t = 1; t <= N + 2; t++)
        for (long long u = 1;; u++) {
            long long A = t * u - 1;
            if (A <= 0) continue;
            long long lower = (A - u >= 1) ? A - u : 2 * A - u;
            if (lower > N) break;
            for (long long v = 1;; v++) {
                long long n = A * v - u;
                if (n > N) break;
                if (n < 1 || (n & 1) == 0) continue;
                int j = jacobi(-A, n);
                int s = (j == -1);
                c[s][n]++;
                if (t >= 2 && u >= 2 && v >= 2) c[2 + s][n]++;
                c[4 + s][n] += t;
            }
        }
    for (long long n = 1; n <= N; n += 2)
        printf("%lld %lld %lld %lld %lld %lld %lld\n", n, c[0][n], c[1][n], c[2][n], c[3][n], c[4][n], c[5][n]);
    return 0;
}
