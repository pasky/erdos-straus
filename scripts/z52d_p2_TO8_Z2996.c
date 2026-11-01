// z52d P2 TO8 Z2996/Z2997: N_p(T) = #{(a,c,d) in Z^3 : a d - p c = 1, 1<=c<=T, |a|,|d|<=T}
// (a,d same sign; ad = 1+pc). Also per-c counts. Output N(T) for several T and the ratios N/T, N/(T log T).
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
long Npc(long p, long T) {
    long N = 0;
    for (long c = 1; c <= T; c++) {
        long m = 1 + p * c;
        // count divisors a>0 of m with a<=T and m/a<=T ; both signs => x2
        for (long a = 1; a * a <= m; a++) {
            if (m % a) continue;
            long d = m / a;
            if (a > T || d > T) continue;
            N += (a == d) ? 2 : 4;   // ordered (a,d) and (d,a), two signs
        }
    }
    return N;
}
int main(int argc, char **argv) {
    long p = atol(argv[1]);
    for (long T = 1000; T <= 256000; T *= 4) {
        long N = Npc(p, T);
        printf("p=%ld T=%ld N=%ld N/T=%.3f N/(T lnT)=%.4f\n", p, T, N, (double)N / T, (double)N / (T * log((double)T)));
    }
    return 0;
}
