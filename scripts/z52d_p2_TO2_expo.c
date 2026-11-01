// Z0512/Z0513/Z0590: odd n <= N not of the form p + sum of k powers of 2 (exponents >= 0, multiset), k = 2 or 3.
// Usage: z52d_p2_TO2_expo N k outfile   (writes exception count and first 40 exceptions, and residues mod 3,5,7,8 histograms)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
int main(int argc, char **argv) {
    long N = atol(argv[1]); int k = atoi(argv[2]);
    char *comp = calloc(N + 1, 1);            // sieve
    comp[0] = comp[1] = 1;
    for (long i = 2; i * i <= N; i++) if (!comp[i]) for (long j = i * i; j <= N; j += i) comp[j] = 1;
    uint8_t *cov = calloc(N + 1, 1);          // covered flags
    // list powers of 2 up to N
    long pw[64]; int np = 0; int e0 = (argc > 4) ? atoi(argv[4]) : 0; for (long q = 1; q <= N; q *= 2) { if (np >= e0) pw[np - e0 + 0] = q; np++; } np -= e0;
    // all sums s of k powers (multiset), s <= N
    long *sums = malloc(sizeof(long) * 200000); int ns = 0;
    if (k == 2) { for (int a = 0; a < np; a++) for (int b = a; b < np; b++) { long s = pw[a] + pw[b]; if (s <= N) sums[ns++] = s; } }
    else { for (int a = 0; a < np; a++) for (int b = a; b < np; b++) for (int c = b; c < np; c++) { long s = pw[a] + pw[b] + pw[c]; if (s <= N) sums[ns++] = s; } }
    // mark p + s
    for (int i = 0; i < ns; i++) {
        long s = sums[i];
        for (long p = 2; p + s <= N; p++) if (!comp[p]) cov[p + s] = 1;
    }
    long exc = 0, odd = 0; long hist3[3] = {0}, hist8[8] = {0};
    FILE *f = fopen(argv[3], "w"); if (!f) { perror("fopen"); return 1; } int shown = 0;
    for (long n = 3; n <= N; n += 2) {
        odd++;
        if (!cov[n]) { exc++; hist3[n % 3]++; hist8[n % 8]++; if (shown < 40) { fprintf(f, "%ld\n", n); shown++; } }
    }
    fclose(f);
    printf("N=%ld k=%d odd_n=%ld exceptions=%ld  mod3:[%ld %ld %ld] mod8:[%ld %ld %ld %ld %ld %ld %ld %ld] sums=%d\n",
           N, k, odd, exc, hist3[0], hist3[1], hist3[2], hist8[0], hist8[1], hist8[2], hist8[3], hist8[4], hist8[5], hist8[6], hist8[7], ns);
    return 0;
}
