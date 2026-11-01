/* z52d pass2 SK3, item Z2363: least level C with a (*) certificate for prime p,
   and the best (smallest) max(x,y,z)/p at that level.
   Divisor form: R_C(p) > 0 iff N = 4Cp+1 has a divisor d with d = -1 mod 4C, 1 < d <= sqrt(N).
   Pair (d, e=N/d): u=(d+1)/(4C), B=(e+1)/(4C); solution (x,y,z)=(uBC, pBC, puC) (FRONTIER 2.2),
   max(x,y,z) = pBC or puC, so max(x,y,z)/p = max(u,B)*C = (e+1)/4 for e = larger factor. We take the d closest to sqrt(N) (smallest e).
   Usage: z52d_p2_SK3_cmin PMAX CMAX  -> prints per-prime lines for p with Cmin > 40 or no level <= CMAX.
   Also prints histograms. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
int main(int argc, char **argv) {
    uint64_t PMAX = strtoull(argv[1], 0, 10);
    uint64_t CMAX = strtoull(argv[2], 0, 10);
    char *comp = calloc(PMAX + 1, 1);
    comp[0] = comp[1] = 1;
    for (uint64_t i = 2; i * i <= PMAX; i++)
        if (!comp[i]) for (uint64_t j = i * i; j <= PMAX; j += i) comp[j] = 1;
    /* histogram of Cmin by decade of p */
    long long hist[12][64]; memset(hist, 0, sizeof(hist));
    long long nnone[12]; memset(nnone, 0, sizeof(nnone));
    long long nprimes[12]; memset(nprimes, 0, sizeof(nprimes));
    double sumC[12]; memset(sumC, 0, sizeof(sumC));
    double sumlogC2[12]; memset(sumlogC2, 0, sizeof(sumlogC2));
    double maxratio[12]; for (int i=0;i<12;i++) maxratio[i]=0;
    uint64_t maxC_found = 0, maxC_p = 0;
    uint64_t bestRatioP[12]; memset(bestRatioP,0,sizeof(bestRatioP));
    for (uint64_t p = 5; p <= PMAX; p += 4) {
        if (comp[p]) continue;
        int dec = 0; { uint64_t t = p; while (t >= 10) { t /= 10; dec++; } }
        nprimes[dec]++;
        uint64_t Cfound = 0; uint64_t bestE = 0;
        for (uint64_t C = 1; C <= CMAX && !Cfound; C++) {
            uint64_t N = 4 * C * p + 1, m = 4 * C;
            /* d = m*u - 1, u>=1, d*d <= N */
            uint64_t bestd = 0;
            for (uint64_t u = 1; ; u++) {
                uint64_t d = m * u - 1;
                if (d * d > N) break;
                if (N % d == 0) bestd = d;  /* increasing d: last one is closest to sqrt N */
            }
            if (bestd) { Cfound = C; bestE = N / bestd; }
        }
        if (!Cfound) {
            nnone[dec]++;
            if (CMAX >= 1) printf("NONE p=%llu\n", (unsigned long long)p);
            continue;
        }
        double ratio = (double)(bestE + 1) / 4.0;  /* max(x,y,z)/p at this level */
        double rnorm = ratio / sqrt((double)p);
        if (Cfound < 64) hist[dec][Cfound]++; else hist[dec][63]++;
        sumC[dec] += Cfound; sumlogC2[dec] += (double)Cfound * Cfound;
        if (rnorm > maxratio[dec]) { maxratio[dec] = rnorm; bestRatioP[dec] = p; }
        if (Cfound > maxC_found) { maxC_found = Cfound; maxC_p = p; }
        if (Cfound >= 100) printf("CMIN p=%llu C=%llu maxxyz/p=%.4g\n", (unsigned long long)p, (unsigned long long)Cfound, ratio);
    }
    printf("== summary (p ≡ 1 mod 4 <= %llu, C <= %llu)\n", (unsigned long long)PMAX, (unsigned long long)CMAX);
    for (int dec = 0; dec < 12; dec++) {
        if (!nprimes[dec]) continue;
        long long nf = nprimes[dec] - nnone[dec];
        printf("decade 1e%d: primes=%lld found=%lld none<=%llu=%lld meanC=%.3f rmsC=%.2f max(max(x,y,z)/p)/sqrt(p)=%.4g at p=%llu\n",
               dec, nprimes[dec], nf, (unsigned long long)CMAX, nnone[dec], nf ? sumC[dec]/nf : 0.0,
               nf ? sqrt(sumlogC2[dec]/nf) : 0.0, maxratio[dec], (unsigned long long)bestRatioP[dec]);
        printf("  C-hist:");
        for (int c = 1; c < 64; c++) if (hist[dec][c]) printf(" %d:%lld", c, hist[dec][c]);
        printf(" >=64:%lld\n", hist[dec][63]);
    }
    printf("largest Cmin found: C=%llu at p=%llu\n", (unsigned long long)maxC_found, (unsigned long long)maxC_p);
    return 0;
}
