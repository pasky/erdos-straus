/* Independent Lemma-N census: mark residue classes of prime factors directly.
   Run: cc -O2 this.c -o /tmp/u7norm && /tmp/u7norm 100000000
   Memory N+10 bytes; no factor tables or campaign engine reused. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
    uint64_t N = argc > 1 ? strtoull(argv[1], 0, 10) : 100000000;
    if (N < 17 || N > 100000000) return 2;
    uint64_t end = N + 8;
    unsigned char *a = calloc(end + 1, 1);
    if (!a) return 3;
    for (uint64_t q = 2; q <= end; ++q) {
        if (a[q] & 1) continue;
        unsigned char flags = (q % 4 == 3 ? 2 : 0)
            | (q % 8 == 5 || q % 8 == 7 ? 4 : 0)
            | (q % 8 == 3 ? 8 : 0) | (q % 8 == 5 ? 16 : 0)
            | (q % 8 == 7 ? 32 : 0);
        a[q] |= flags;
        for (uint64_t j = 2*q; j <= end; j += q) a[j] |= 1 | flags;
    }
    uint64_t total = 0, c3 = 0, c4 = 0;
    for (uint64_t p = 17; p <= N; p += 8) {
        if (a[p] & 1) continue;
        ++total;
        if ((a[(p+1)/2] & 2) || (a[p+4] & 2) || (a[p+2] & 4)) continue;
        ++c3;
        unsigned char b = a[p+8];
        if (!(b & 32) && !((b & 8) && (b & 16))) ++c4;
    }
    printf("N=%llu total=%llu chain123=%llu chain1234=%llu\n",
           (unsigned long long)N, (unsigned long long)total,
           (unsigned long long)c3, (unsigned long long)c4);
    free(a);
    return N == 100000000 && (total != 1439970 || c3 != 41866 || c4 != 15468);
}
