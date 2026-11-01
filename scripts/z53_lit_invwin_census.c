/* z53 LIT F2b: large-sample test of whether the Garaev–Shparlinski inverse-window discrepancy D_p(N), N = floor(log^2 p),
 * predicts the (★) count R(p) beyond small-divisor (residue-class) data of p.
 * R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n}, computed by direct enumeration for all n <= X.
 * Output (stdout, TSV): p R D G tm tp s50  for primes p ≡ 1 (mod 24) in [Y, X], where
 *   D = sup-discrepancy of {xbar/p : 1<=x<=N}, G = #{x<=N : xbar < 2p/N},
 *   tm = #{x<=N : x | p-1}, tp = #{x<=N : x | p+1}, s50 = #{primes l<=50 : l | p-1}.
 * Build: gcc -O2 -o /tmp/z53_invwin scripts/z53_lit_invwin_census.c -lm ; run: /tmp/z53_invwin Y X > out.tsv
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

static long inv(long a, long m) { long t = 0, nt = 1, r = m, nr = a % m; while (nr) { long q = r / nr, x; x = t - q * nt; t = nt; nt = x; x = r - q * nr; r = nr; nr = x; } if (t < 0) t += m; return t; }
static int cmpd(const void *a, const void *b) { double x = *(const double *)a, y = *(const double *)b; return (x > y) - (x < y); }

int main(int argc, char **argv) {
    long Y = atol(argv[1]), X = atol(argv[2]);
    uint16_t *R = calloc(X + 1, sizeof(uint16_t));
    char *comp = calloc(X + 2, 1);
    if (!R || !comp) return 1;
    for (long u = 1; 4 * u - u - 1 <= X; u++)
        for (long B = 1; 4 * u * B - u - B <= X; B++)
            for (long C = 1;; C++) { long n = 4 * u * B * C - u - B; if (n > X) break; R[n]++; }
    for (long i = 2; i * i <= X + 1; i++) if (!comp[i]) for (long j = i * i; j <= X + 1; j += i) comp[j] = 1;
    static const int sp[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
    double *v = malloc(sizeof(double) * 4096);
    for (long p = Y; p <= X; p++) {
        if (p % 24 != 1 || comp[p]) continue;
        double L = log((double)p); int N = (int)(L * L);
        int k = 0, G = 0, tm = 0, tp = 0, s50 = 0;
        for (int x = 1; x <= N; x++) {
            long xb = inv(x, p); v[k++] = (double)xb / p; if (xb < 2.0 * p / N) G++;
            if ((p - 1) % x == 0) tm++; if ((p + 1) % x == 0) tp++;
        }
        for (int i = 0; i < 15; i++) if ((p - 1) % sp[i] == 0) s50++;
        qsort(v, k, sizeof(double), cmpd);
        double D = 0; for (int i = 0; i < k; i++) { double a = fabs((i + 1.0) / k - v[i]), b = fabs((double)i / k - v[i]); if (a > D) D = a; if (b > D) D = b; }
        printf("%ld\t%d\t%.5f\t%d\t%d\t%d\t%d\n", p, R[p], D, G, tm, tp, s50);
    }
    return 0;
}
