/* z49_i3fable_count.c — exact interior-word data for every n <= N.
 * A word of n is (t,u,v) with tuv - u - v = n; interior means t,u,v >= 3.  Words are enumerated by unordered
 * endpoint pairs u <= v (uv | n+u+v, t = (n+u+v)/(uv) >= 3); ordered count I3 = 2*(#u<v) + (#u=v).
 * Outputs (binary, little endian, index n):
 *   <prefix>_i3.u16   : I3(n), saturating at 65535
 *   <prefix>_minv.u32 : least larger endpoint v of an interior word (0xFFFFFFFF if none)
 *   <prefix>_mint.u32 : least level t of an interior word (0xFFFFFFFF if none)
 *   <prefix>_lev8.u8  : bitmask of level classes t mod 8 that carry at least one interior word
 * and <prefix>_zeros.txt listing all n with I3(n)=0.
 * Usage: z49_i3fable_count N prefix          (N=1e7: ~5 s, 110 MB; N=1e8: ~2 min, 1.1 GB)
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s N prefix\n", argv[0]); return 1; }
    uint64_t N = strtoull(argv[1], 0, 10);
    uint16_t *I3 = calloc(N + 1, 2); uint32_t *MV = malloc(4 * (N + 1)), *MT = malloc(4 * (N + 1)); uint8_t *L8 = calloc(N + 1, 1);
    if (!I3 || !MV || !MT || !L8) { fprintf(stderr, "alloc failed\n"); return 2; }
    memset(MV, 0xFF, 4 * (N + 1)); memset(MT, 0xFF, 4 * (N + 1));
    for (int64_t u = 3; 3 * u * u - 2 * u <= (int64_t)N; u++) {
        for (int64_t v = u; ; v++) {
            int64_t uv = u * v; int64_t n0 = 3 * uv - u - v; if (n0 > (int64_t)N) break;
            int inc = (u == v) ? 1 : 2;
            int64_t t = 3;
            for (int64_t n = n0; n <= (int64_t)N; n += uv, t++) {
                uint32_t c = I3[n] + inc; I3[n] = c > 65535 ? 65535 : (uint16_t)c;
                if ((uint64_t)v < MV[n]) MV[n] = (uint32_t)v;
                if ((uint64_t)t < MT[n]) MT[n] = (uint32_t)t;
                L8[n] |= (uint8_t)(1u << (t & 7));
            }
        }
    }
    char fn[600]; FILE *f;
    snprintf(fn, sizeof fn, "%s_i3.u16", argv[2]); f = fopen(fn, "wb"); fwrite(I3, 2, N + 1, f); fclose(f);
    snprintf(fn, sizeof fn, "%s_minv.u32", argv[2]); f = fopen(fn, "wb"); fwrite(MV, 4, N + 1, f); fclose(f);
    snprintf(fn, sizeof fn, "%s_mint.u32", argv[2]); f = fopen(fn, "wb"); fwrite(MT, 4, N + 1, f); fclose(f);
    snprintf(fn, sizeof fn, "%s_lev8.u8", argv[2]); f = fopen(fn, "wb"); fwrite(L8, 1, N + 1, f); fclose(f);
    snprintf(fn, sizeof fn, "%s_zeros.txt", argv[2]); f = fopen(fn, "w");
    uint64_t z = 0; for (uint64_t n = 3; n <= N; n++) if (I3[n] == 0) { fprintf(f, "%llu\n", (unsigned long long)n); z++; }
    fclose(f); printf("N=%llu zeros=%llu\n", (unsigned long long)N, (unsigned long long)z); return 0;
}
