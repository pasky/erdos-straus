/* R284 from-scratch check of BOARD2_SLATE item (4) (8/n c = 1 line).  Written independently of z42_zero_law.c.
 *
 * Object: hit at odd n  <=>  exists ordered (u,B), u,B >= 1, gcd(u,B) = 1, u+B odd, with 8uB | n+u+B and
 *         8uB - u - B <= n  (C = (n+u+B)/(8uB) >= 1).
 * modes:
 *   zeros N            : byte-array marking over odd n <= N; prints "Z n" for odd non-squares n >= 5 that are not hit,
 *                        and a summary.  (Loop order B outer, u inner; plain byte array.)
 *   M N < list         : M_8(n) = sum over ordered pairs with 8uB-u-B <= n, gcd(n, uB) = 1 of (1 - (-uB/n))/phi(8uB);
 *                        also direct per-n hit test (divisor-free: loops all pairs) -> prints "n M hit".
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

static long g(long a, long b) { while (b) { long t = a % b; a = b; b = t; } return a; }
static int J(long a, long n) {           /* Jacobi (a/n), n odd > 0 */
    a %= n; if (a < 0) a += n; int s = 1;
    while (a != 0) {
        int tz = 0; while ((a & 1) == 0) { a >>= 1; tz ^= 1; }
        if (tz && ((n % 8 == 3) || (n % 8 == 5))) s = -s;
        if ((a % 4 == 3) && (n % 4 == 3)) s = -s;
        long t = n % a; n = a; a = t;
    }
    return n == 1 ? s : 0;
}
static int sq(long n) { long r = (long)sqrt((double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++; return r * r == n; }

int main(int argc, char **argv) {
    if (argc < 3) return 1;
    long N = atol(argv[2]);
    if (!strcmp(argv[1], "zeros")) {
        unsigned char *h = calloc(N + 1, 1);
        for (long B = 1; 8 * B - B - 1 <= N; B++)
            for (long u = 1; 8 * u * B - u - B <= N; u++) {
                if (((u + B) % 2) == 0 || g(u, B) != 1) continue;
                long q = 8 * u * B;
                for (long n = q - u - B; n <= N; n += q) h[n] = 1;
            }
        long adm = 0, z = 0;
        for (long n = 5; n <= N; n += 2) {
            if (sq(n)) continue;
            adm++;
            if (!h[n]) { z++; printf("Z %ld\n", n); }
        }
        printf("# N=%ld admissible(odd nonsq >=5)=%ld zeros=%ld\n", N, adm, z);
        return 0;
    }
    if (!strcmp(argv[1], "zerosm")) {     /* zerosm N m lo : general m (4 | m), window [lo, N], m = 12: n prime to 3 */
        long m = atol(argv[3]), lo = atol(argv[4]);
        unsigned char *h = calloc(N + 1, 1);
        for (long B = 1; m * B - B - 1 <= N; B++)
            for (long u = 1; m * u * B - u - B <= N; u++) {
                if (((u + B) % 2) == 0 || g(u, B) != 1) continue;
                long q = m * u * B;
                for (long n = q - u - B; n <= N; n += q) h[n] = 1;
            }
        long adm = 0, z = 0;
        for (long n = 5; n <= N; n += 2) {
            if (n < lo || sq(n) || (m % 3 == 0 && n % 3 == 0)) continue;
            adm++; if (!h[n]) z++;
        }
        printf("# m=%ld window [%ld,%ld] admissible=%ld zeros=%ld\n", m, lo, N, adm, z);
        return 0;
    }
    if (!strcmp(argv[1], "M")) {
        long X = N / 7 + 10;
        long *phi = malloc((X + 1) * sizeof(long));
        for (long i = 0; i <= X; i++) phi[i] = i;
        for (long p = 2; p <= X; p++) if (phi[p] == p) for (long j = p; j <= X; j += p) phi[j] -= phi[j] / p;
        long n;
        while (scanf("%ld", &n) == 1) {
            double M = 0; int hit = 0;
            for (long u = 1; 7 * u - 1 <= n; u++)
                for (long B = 1; 8 * u * B - u - B <= n; B++) {
                    if (((u + B) % 2) == 0 || g(u, B) != 1) continue;
                    if ((n + u + B) % (8 * u * B) == 0) hit = 1;
                    if (g(n, u * B) != 1) continue;
                    long m = u * B;           /* even, so phi(8m) = 8 phi(m) */
                    M += (1 - J(-m, n)) / (8.0 * phi[m]);
                }
            printf("%ld %.4f %d\n", n, M, hit);
            fflush(stdout);
        }
        return 0;
    }
    return 1;
}
