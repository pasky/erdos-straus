/* z48_ltfable_lines.c — census of ES "word" lines at every integer n <= N.
 *
 * A word of n is (t,u,v) in N^3 with t*u*v - u - v = n.  (tu-1)(tv-1) = tn+1.
 * Lines (each word is counted once per flag; ordered words (u,v) and (v,u) both counted):
 *   W   : all words                                   (sign-free total)
 *   MP  : words with u >= 3 and v >= 3                (model problem, sign-free, prime-free)
 *   I3  : words with t >= 3, u >= 3, v >= 3            (interior model problem: no class-free level)
 *   W2  : words with t,u,v >= 2                         (proper HJ length-3 fractions, DEDEKIND's L_3)
 *   L3  : t = 3 (mod 4) and uv even                      (level-class line; every such word is a certificate, Cor 1.3)
 *   L1  : t = 1 (mod 4) and 4 | uv                       (level-class line; ditto)
 *   ST  : 4 | t                                       (= the (*) line, R(n))
 *   SU  : 4 | u or 4 | v                              (= the b=1 / Lopez Type A line)
 *   SAB : 4 | tu-1 or 4 | tv-1                        (= X_slice, Type I a=1, and its reversal)
 *   ANY : at least one of the five slots              (= five-slice certificate count N_-(n) for n = 1 mod 4)
 * Counts are saturating uint8 (255 = ">=255").
 *
 * Output: a binary file of 10*(N+1) bytes (arrays W,MP,ST,SU,SAB,ANY,I3,W2,L3,L1 consecutively), plus a text summary
 * of failures (count 0) of MP for all n in [3,N] and of each line / union at primes p = 1 mod 4.
 *
 * Usage: z48_ltfable_lines N outprefix          (N <= 2^31-1; memory 6N bytes + N/8 for the prime sieve)
 * Compile: gcc -O2 -o z48_ltfable_lines z48_ltfable_lines.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static inline void inc(uint8_t *a, uint64_t i) { if (a[i] < 255) a[i]++; }

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s N outprefix\n", argv[0]); return 1; }
    uint64_t N = strtoull(argv[1], 0, 10);
    const char *pre = argv[2];
    uint8_t *W = calloc(N + 1, 1), *MP = calloc(N + 1, 1), *ST = calloc(N + 1, 1),
            *SU = calloc(N + 1, 1), *SAB = calloc(N + 1, 1), *ANY = calloc(N + 1, 1),
            *I3 = calloc(N + 1, 1), *W2 = calloc(N + 1, 1), *L3 = calloc(N + 1, 1), *L1 = calloc(N + 1, 1);
    if (!W || !MP || !ST || !SU || !SAB || !ANY || !I3 || !W2 || !L3 || !L1) { fprintf(stderr, "alloc failed\n"); return 2; }

    /* enumerate words with u <= v; record both orders when u != v */
    for (int64_t u = 1; ; u++) {
        if (u * u - 2 * u > (int64_t)N) break;      /* smallest n with v=u, t=1 is u^2-2u */
        for (int64_t v = u; ; v++) {
            int64_t uv = u * v;
            int64_t tmin = (u + v + uv - 1) / uv;   /* least t with t*uv - u - v >= 0 */
            if (tmin < 1) tmin = 1;
            if (tmin * uv - u - v > (int64_t)N) break;
            for (int64_t t = tmin; ; t++) {
                int64_t n = t * uv - u - v;         /* n = t*uv - u - v */
                if (n > (int64_t)N) break;
                int mult = (u == v) ? 1 : 2;
                int st = (t % 4 == 0);
                int su = (u % 4 == 0) || (v % 4 == 0);
                int sa = ((t * u - 1) % 4 == 0) || ((t * v - 1) % 4 == 0);
                int mp = (u >= 3) && (v >= 3);
                int i3 = mp && (t >= 3);
                int w2 = (t >= 2) && (u >= 2) && (v >= 2);
                int l3 = (t % 4 == 3) && ((u * v) % 2 == 0);
                int l1 = (t % 4 == 1) && ((u * v) % 4 == 0);
                for (int k = 0; k < mult; k++) {
                    inc(W, n);
                    if (mp) inc(MP, n);
                    if (i3) inc(I3, n);
                    if (w2) inc(W2, n);
                    if (l3) inc(L3, n);
                    if (l1) inc(L1, n);
                    if (st) inc(ST, n);
                    if (su) inc(SU, n);
                    if (sa) inc(SAB, n);
                    if (st || su || sa) inc(ANY, n);
                }
            }
        }
    }

    /* write binary arrays */
    char fn[512];
    snprintf(fn, sizeof fn, "%s.bin", pre);
    FILE *f = fopen(fn, "wb");
    if (f) {
        fwrite(W, 1, N + 1, f); fwrite(MP, 1, N + 1, f); fwrite(ST, 1, N + 1, f);
        fwrite(SU, 1, N + 1, f); fwrite(SAB, 1, N + 1, f); fwrite(ANY, 1, N + 1, f);
        fwrite(I3, 1, N + 1, f); fwrite(W2, 1, N + 1, f); fwrite(L3, 1, N + 1, f); fwrite(L1, 1, N + 1, f);
        fclose(f);
    }

    /* prime sieve (odd numbers) */
    uint8_t *comp = calloc(N / 2 + 1, 1); /* comp[i] for odd 2i+1 */
    for (uint64_t i = 1; (2 * i + 1) * (2 * i + 1) <= N; i++) {
        if (comp[i]) continue;
        uint64_t p = 2 * i + 1;
        for (uint64_t j = (p * p - 1) / 2; j <= N / 2; j += p) comp[j] = 1;
    }

    snprintf(fn, sizeof fn, "%s.txt", pre);
    FILE *g = fopen(fn, "w");
    fprintf(g, "# N = %llu\n", (unsigned long long)N);
    fprintf(g, "# MP failures (all n in [3,N], no word with u,v >= 3):\n");
    uint64_t nmp = 0;
    for (uint64_t n = 3; n <= N; n++) if (MP[n] == 0) { if (nmp < 2000) fprintf(g, "MP0 %llu W=%u\n", (unsigned long long)n, W[n]); nmp++; }
    fprintf(g, "# MP failures total: %llu\n", (unsigned long long)nmp);
    uint64_t ni3 = 0, nw2 = 0;
    for (uint64_t n = 3; n <= N; n++) if (I3[n] == 0) { if (ni3 < 3000) fprintf(g, "I30 %llu W=%u MP=%u W2=%u\n", (unsigned long long)n, W[n], MP[n], W2[n]); ni3++; }
    fprintf(g, "# I3 failures total (all n in [3,N]): %llu\n", (unsigned long long)ni3);
    for (uint64_t n = 3; n <= N; n++) if (W2[n] == 0) { if (nw2 < 3000) fprintf(g, "W20 %llu W=%u\n", (unsigned long long)n, W[n]); nw2++; }
    fprintf(g, "# W2 failures total (all n in [3,N]): %llu\n", (unsigned long long)nw2);
    fprintf(g, "# primes p = 1 mod 4 in [5,N]: failures of lines (ST=(*), SU=b1, SAB=Xslice, ANY=five-slice)\n");
    uint64_t np = 0, f_st = 0, f_su = 0, f_sab = 0, f_any = 0, f_stsu = 0, f_stsab = 0, f_susab = 0, f_mp = 0, f_l3 = 0, f_l1 = 0, f_stl3 = 0, f_l3l1 = 0;
    for (uint64_t p = 5; p <= N; p += 4) {
        if (comp[p / 2]) continue;
        np++;
        if (ST[p] == 0) { f_st++; fprintf(g, "ST0 %llu W=%u MP=%u SU=%u SAB=%u ANY=%u\n", (unsigned long long)p, W[p], MP[p], SU[p], SAB[p], ANY[p]); }
        if (SU[p] == 0) { f_su++; fprintf(g, "SU0 %llu W=%u MP=%u ST=%u SAB=%u ANY=%u\n", (unsigned long long)p, W[p], MP[p], ST[p], SAB[p], ANY[p]); }
        if (SAB[p] == 0) { f_sab++; fprintf(g, "SAB0 %llu W=%u MP=%u ST=%u SU=%u ANY=%u\n", (unsigned long long)p, W[p], MP[p], ST[p], SU[p], ANY[p]); }
        if (ANY[p] == 0) { f_any++; fprintf(g, "ANY0 %llu W=%u MP=%u\n", (unsigned long long)p, W[p], MP[p]); }
        if (ST[p] == 0 && SU[p] == 0) f_stsu++;
        if (ST[p] == 0 && SAB[p] == 0) f_stsab++;
        if (SU[p] == 0 && SAB[p] == 0) f_susab++;
        if (MP[p] == 0) f_mp++;
        if (L3[p] == 0) { f_l3++; fprintf(g, "L30 %llu ST=%u L1=%u\n", (unsigned long long)p, ST[p], L1[p]); }
        if (L1[p] == 0) { f_l1++; if (f_l1 <= 200) fprintf(g, "L10 %llu ST=%u L3=%u\n", (unsigned long long)p, ST[p], L3[p]); }
        if (ST[p] == 0 && L3[p] == 0) f_stl3++;
        if (L3[p] == 0 && L1[p] == 0) f_l3l1++;
    }
    fprintf(g, "# primes=1(4): %llu  failures: ST %llu  SU %llu  SAB %llu  ANY %llu  ST&SU %llu  ST&SAB %llu  SU&SAB %llu  MP %llu  L3 %llu  L1 %llu  ST&L3 %llu  L3&L1 %llu\n",
            (unsigned long long)np, (unsigned long long)f_st, (unsigned long long)f_su, (unsigned long long)f_sab,
            (unsigned long long)f_any, (unsigned long long)f_stsu, (unsigned long long)f_stsab, (unsigned long long)f_susab, (unsigned long long)f_mp,
            (unsigned long long)f_l3, (unsigned long long)f_l1, (unsigned long long)f_stl3, (unsigned long long)f_l3l1);
    fclose(g);
    printf("done N=%llu MPfail=%llu I3fail=%llu W2fail=%llu primes=%llu STfail=%llu SUfail=%llu SABfail=%llu ANYfail=%llu\n",
           (unsigned long long)N, (unsigned long long)nmp, (unsigned long long)ni3, (unsigned long long)nw2, (unsigned long long)np, (unsigned long long)f_st,
           (unsigned long long)f_su, (unsigned long long)f_sab, (unsigned long long)f_any);
    return 0;
}
