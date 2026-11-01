/* Z1739: fractional parts {(n+u)/(4uC-1)} over the trial set R(n) = {(u,C): 4uC-1 <= n+u} (PARITY_AUDIT Lemma 2.1).
 * For each n: three modulus ranges m <= n^{1/2}, n^{1/2} < m <= n^{3/4}, m > n^{3/4}: count, zeros (= the (★) events),
 * sum 1/m (integer density), sum 1/phi(m) (prime density), mean frac, 2000-bin histogram of frac.
 * usage: frac n1 n2 ...   output: one line per (n, range): n range N zeros sum1m sum1phi meanfrac hist[2000]
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define NB 2000
static int *phi; static long PM;
int main(int argc, char **argv) {
    long nmax = 0; for (int a = 1; a < argc; a++) if (atol(argv[a]) > nmax) nmax = atol(argv[a]);
    PM = 2 * nmax + 10; phi = malloc(sizeof(int) * PM); for (long i = 0; i < PM; i++) phi[i] = i;
    for (long i = 2; i < PM; i++) if (phi[i] == i) for (long j = i; j < PM; j += i) phi[j] -= phi[j] / i;
    static long hist[3][NB];
    for (int a = 1; a < argc; a++) {
        long n = atol(argv[a]); double r1 = sqrt((double)n), r2 = pow((double)n, 0.75);
        long cnt[3] = {0}, z[3] = {0}; double s1[3] = {0}, sp[3] = {0}, mf[3] = {0};
        for (int k = 0; k < 3; k++) for (int b = 0; b < NB; b++) hist[k][b] = 0;
        for (long u = 1; 4 * u - 1 <= n + u; u++)
            for (long C = 1; 4 * u * C - 1 <= n + u; C++) {
                long m = 4 * u * C - 1; int k = m <= r1 ? 0 : (m <= r2 ? 1 : 2);
                long r = (n + u) % m; double f = (double)r / m;
                cnt[k]++; if (!r) z[k]++; s1[k] += 1.0 / m; sp[k] += 1.0 / phi[m]; mf[k] += f;
                int bb = (int)(f * NB); if (bb >= NB) bb = NB - 1; hist[k][bb]++;
            }
        for (int k = 0; k < 3; k++) { printf("%ld %d %ld %ld %.6f %.6f %.6f", n, k, cnt[k], z[k], s1[k], sp[k], mf[k] / cnt[k]);
            for (int b = 0; b < NB; b++) printf(" %ld", hist[k][b]); printf("\n"); }
        fflush(stdout);
    }
    return 0;
}
