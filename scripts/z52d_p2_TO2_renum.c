// R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n}, for all n <= N (ordered triples, u,B,C >= 1).
// Also per n: minC = min C over triples, minUBC = min u*B*C over triples (0 if none).
// Output (binary-free, text): for each n in [1..N] with R(n)>0 or n odd prime-like handled by python.
// Usage: z52d_p2_TO2_renum N outfile   (writes "n R minC minUBC" for every n<=N with R(n)>0)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char **argv) {
    long N = atol(argv[1]);
    uint32_t *R = calloc(N + 1, sizeof(uint32_t));
    uint32_t *minC = malloc((N + 1) * sizeof(uint32_t));
    uint32_t *minW = malloc((N + 1) * sizeof(uint32_t));
    for (long n = 0; n <= N; n++) { minC[n] = 0xFFFFFFFFu; minW[n] = 0xFFFFFFFFu; }
    for (long u = 1; 3 * u - 1 <= N; u++) {
        for (long B = 1; 4 * u * B - u - B <= N; B++) {
            long m4 = 4 * u * B;
            for (long C = 1;; C++) {
                long n = m4 * C - u - B;
                if (n > N) break;
                R[n]++;
                if (C < minC[n]) minC[n] = (uint32_t)C;
                long w = u * B * C;
                if (w < minW[n]) minW[n] = (uint32_t)w;
            }
        }
    }
    FILE *f = fopen(argv[2], "w");
    for (long n = 1; n <= N; n++) if (R[n]) fprintf(f, "%ld %u %u %u\n", n, R[n], minC[n], minW[n]);
    fclose(f);
    return 0;
}
