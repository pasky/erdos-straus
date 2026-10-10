/* O128: f_II(n) for all n <= N (Type II solutions of 4/n, ordered in (y,z)), plus the subfamilies
 * d = 1 and c = 1.  Enumeration over ET quadruples (a,b,c,d), 4abcd = a+b+nc, gcd(a,c)=1, with a <= b
 * (weight 2 if a < b, 1 if a = b), parametrised by (a,c,d,e): f = 4acd-1, n = e f - 4a^2 d, b = ce - a.
 * a <= b  <=>  ce >= 2a.  Output: raw uint32 arrays tot[0..N], d1[0..N], c1[0..N] to OUTFILE.
 * Usage: t2s_count N OUTFILE
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

static uint64_t gcd(uint64_t x, uint64_t y) { while (y) { uint64_t t = x % y; x = y; y = t; } return x; }

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s N OUT\n", argv[0]); return 1; }
    uint64_t N = strtoull(argv[1], 0, 10);
    uint32_t *tot = calloc(N + 1, 4), *d1 = calloc(N + 1, 4), *c1 = calloc(N + 1, 4);
    if (!tot || !d1 || !c1) { fprintf(stderr, "oom\n"); return 1; }
    uint64_t iters = 0;
    for (uint64_t a = 1; 4 * a * a <= N + 4 * a; a++) {
        for (uint64_t c = 1;; c++) {
            uint64_t e0 = (2 * a + c - 1) / c;              /* ceil(2a/c): b >= a */
            /* n_min at d = 1 */
            int64_t nmin1 = (int64_t)(e0 * (4 * a * c - 1)) - (int64_t)(4 * a * a);
            if (nmin1 > (int64_t)N) break;
            if (gcd(a, c) != 1) continue;
            for (uint64_t d = 1;; d++) {
                uint64_t f = 4 * a * c * d - 1, s = 4 * a * a * d;
                int64_t nmin = (int64_t)(e0 * f) - (int64_t)s;
                if (nmin > (int64_t)N) break;
                for (uint64_t e = e0;; e++) {
                    int64_t n = (int64_t)(e * f) - (int64_t)s;
                    if (n > (int64_t)N) break;
                    if (n <= 0) continue;
                    uint64_t b = c * e - a;
                    uint32_t w = (b == a) ? 1 : 2;
                    tot[n] += w;
                    if (d == 1) d1[n] += w;
                    if (c == 1) c1[n] += w;
                    iters++;
                }
            }
        }
    }
    FILE *fo = fopen(argv[2], "wb");
    fwrite(tot, 4, N + 1, fo); fwrite(d1, 4, N + 1, fo); fwrite(c1, 4, N + 1, fo);
    fclose(fo);
    fprintf(stderr, "N=%llu tuples=%llu\n", (unsigned long long)N, (unsigned long long)iters);
    return 0;
}
