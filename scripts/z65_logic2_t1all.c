/* z65 LOGIC2 kill test K3: R(m^2) = 0 for ALL m (odd and even) up to M,
 * where R(n) = #{(u,B,C) >= 1 : 4uBC - u - B = n}.  Also R(0) = 0 trivially.
 * Sieve over all triples with 4uBC - u - B <= N = M^2, mark hits, report any square hit.
 * Usage: z65_logic2_t1all M   (N = M^2 must fit; memory N/8 bytes)
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char **argv) {
    long M = argc > 1 ? atol(argv[1]) : 3000;
    long N = M * M;
    uint8_t *bits = calloc(N / 8 + 1, 1);
    if (!bits) { fprintf(stderr, "alloc\n"); return 1; }
    long triples = 0;
    for (long u = 1; 4 * u - u - 1 <= N; u++)
        for (long B = 1; 4 * u * B - u - B <= N; B++) {
            long step = 4 * u * B;
            for (long v = step - u - B; v <= N; v += step) {
                bits[v >> 3] |= (uint8_t)(1u << (v & 7));
                triples++;
            }
        }
    long sqhits = 0, nsq = 0, nonsq_zero_1mod4 = 0;
    for (long m = 1; m <= M; m++) {
        long v = m * m; nsq++;
        if (bits[v >> 3] & (1u << (v & 7))) { sqhits++; printf("SQUARE HIT m=%ld\n", m); }
    }
    printf("M=%ld N=%ld triples=%ld squares_tested=%ld square_hits=%ld\n", M, N, triples, nsq, sqhits);
    return 0;
}
