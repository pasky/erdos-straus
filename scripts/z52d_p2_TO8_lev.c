// z52d Pass2 TO8 common tool (see data/z52b/pass2/TO8/README.txt).
// L_C(p) = #{u>=1 : (4uC-1) | (p+u)}  (trial form of (★), FRONTIER §2.1; each hit = one (u,C,B) with B=(p+u)/(4uC-1)).
// R(p) = sum_C L_C(p) over all C>=1 (when mode "all").  Level C "fails" iff L_C(p)=0.
// usage:  z52d_p2_TO8_lev all   < primes      -> p R(p) nfail_levels(C<=(p+2)/4)
//         z52d_p2_TO8_lev c1,c2,... < primes  -> p R_listed failbits(0/1 per listed level)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static long Lcount(long p, long C) {
    long L = 0;
    for (long u = 1; (4 * u * C - 1) <= p + u; u++)
        if ((p + u) % (4 * u * C - 1) == 0) L++;
    return L;
}

// b1 mode: b=1 line count: #{(d,k): d>=1,k>=1, (4dk-1) | (p+4d)}  (divisor form of López Type A: p+4d has divisor w≡-1 mod 4d)
static long B1count(long p) {
    long B = 0;
    for (long d = 1; 4 * d - 1 <= p + 1; d++)
        for (long k = 1; (4 * d * k - 1) <= p + 4 * d; k++)
            if ((p + 4 * d) % (4 * d * k - 1) == 0) B++;
    return B;
}
int main(int argc, char **argv) {
    char *spec = argc > 1 ? argv[1] : "all";
    if (strcmp(spec, "par200") == 0) { // for C=1..200: print p, #odd L_C, #levels with L_C>0 (C<=200), and list of odd C
        long p; while (scanf("%ld", &p) == 1) { long nodd = 0, npos = 0; printf("%ld", p);
            for (long C = 1; C <= 200 && C <= (p + 2) / 4; C++) { long L = Lcount(p, C); if (L & 1) { nodd++; printf(" o%ld", C); } if (L) npos++; }
            printf(" | nodd=%ld npos=%ld\n", nodd, npos); }
        return 0; }
    if (strcmp(spec, "b1") == 0) { long p; while (scanf("%ld", &p) == 1) printf("%ld %ld\n", p, B1count(p)); return 0; }
    long *cl = NULL; long ncl = 0;
    int all = strcmp(spec, "all") == 0;
    if (!all) {
        char *s = strdup(spec); char *t = strtok(s, ",");
        cl = malloc(sizeof(long) * 100000);
        while (t) { cl[ncl++] = atol(t); t = strtok(NULL, ","); }
    }
    long p;
    while (scanf("%ld", &p) == 1) {
        if (all) {
            long R = 0, nf = 0, cm = (p + 2) / 4;
            for (long C = 1; C <= cm; C++) { long L = Lcount(p, C); R += L; if (!L) nf++; }
            printf("%ld %ld %ld\n", p, R, nf);
        } else {
            long R = 0; char *bits = malloc(ncl + 1);
            for (long i = 0; i < ncl; i++) {
                long L = (cl[i] <= (p + 2) / 4) ? Lcount(p, cl[i]) : 0;
                R += L; bits[i] = L ? '0' : '1';
            }
            bits[ncl] = 0;
            printf("%ld %ld %s\n", p, R, bits);
            free(bits);
        }
    }
    return 0;
}
