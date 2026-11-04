/* z56 K4TRY census: for primes p <= X, p = 1 (mod 8), classify N1 = p+4 and N2 = 4p+1 by their Q-anatomy
   (Q = primes = 3 mod 4).  Reports, for several theta, among p with N2 in S (exact) [resp. N1 in S]:
     A(theta) = #{p : N1 has no Q-prime factor < X^theta}
     E        = #{p : N1 in S}   (= A for theta > 1/2 - eps, by parity)
     T(theta) = A(theta) - E     (N1 = m q q' with q, q' >= X^theta; by parity exactly two Q-factors)
   so T/A is the empirical "switched mass" compared with the model B(theta)/F(1/theta).
   Also the symmetric table with the roles of N1, N2 exchanged, and the r*-weighted sum.
   Usage: ./z56_k4try_census X      (X <= 1e9; memory: spf array of 4X+2 uint32 = 16X bytes -> use X <= 2.5e8)
   Build: gcc -O2 -o z56_k4try_census z56_k4try_census.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

static uint32_t *spf;

static void build_spf(uint64_t N) {
    spf = (uint32_t *)calloc(N + 1, sizeof(uint32_t));
    if (!spf) { fprintf(stderr, "alloc fail\n"); exit(1); }
    for (uint64_t i = 2; i <= N; i++) {
        if (spf[i] == 0) {
            spf[i] = (uint32_t)i;
            if (i * i <= N) for (uint64_t j = i * i; j <= N; j += i) if (spf[j] == 0) spf[j] = (uint32_t)i;
        }
    }
}

/* returns: minimal Q-prime factor (0 if none), number of distinct Q-primes, and 2^{omega_split}; in S iff nq==0 */
static void anatomy(uint64_t n, uint32_t *minq, int *nq, int *omega_split) {
    *minq = 0; *nq = 0; *omega_split = 0;
    while (n > 1) {
        uint32_t q = spf[n];
        int e = 0;
        while (n % q == 0) { n /= q; e++; }
        if (q == 2) continue;
        if (q % 4 == 3) { (*nq)++; if (*minq == 0 || q < *minq) *minq = q; }
        else (*omega_split)++;
    }
}

int main(int argc, char **argv) {
    uint64_t X = (argc > 1) ? strtoull(argv[1], 0, 10) : 100000000ULL;
    uint64_t N = 4 * X + 2;
    build_spf(N);
    const int NT = 7;
    double thetas[7] = {0.25, 0.30, 0.35, 0.40, 0.45, 0.48, 0.50};
    uint64_t zc[7];
    for (int i = 0; i < NT; i++) zc[i] = (uint64_t)floor(pow((double)X, thetas[i]));
    uint64_t np = 0, nE1 = 0, nE2 = 0, nboth = 0;
    uint64_t A1[7] = {0}, A2[7] = {0};       /* A1[t]: N2 in S and N1 Q-rough to X^theta;  A2: roles exchanged */
    double wsum = 0.0;                        /* sum over p with N1 in S of r*(N2)/8 = 2^{omega(N2)-1} 1_S(N2) */
    for (uint64_t p = 17; p <= X; p += 8) {
        if (spf[p] != p) continue;
        np++;
        uint32_t q1, q2; int n1, n2, w1, w2;
        anatomy(p + 4, &q1, &n1, &w1);
        anatomy(4 * p + 1, &q2, &n2, &w2);
        int S1 = (n1 == 0), S2 = (n2 == 0);
        if (S1) nE1++;
        if (S2) nE2++;
        if (S1 && S2) { nboth++; wsum += ldexp(1.0, w2 - 1); }
        if (S2) for (int t = 0; t < NT; t++) if (S1 || q1 >= zc[t]) A1[t]++;
        if (S1) for (int t = 0; t < NT; t++) if (S2 || q2 >= zc[t]) A2[t]++;
    }
    printf("X=%llu  primes p=1(8): %llu   N1 in S: %llu   N2 in S: %llu   both: %llu   sum_{both} r*(N2)/8 = %.1f  (ratio %.4f)\n",
           (unsigned long long)X, (unsigned long long)np, (unsigned long long)nE1, (unsigned long long)nE2,
           (unsigned long long)nboth, wsum, wsum / (double)nboth);
    printf("# theta  z        A1=#{N2 in S, N1 Q-rough>=z}  T1=A1-both  T1/A1   |  A2=#{N1 in S, N2 Q-rough>=z}  T2=A2-both  T2/A2\n");
    for (int t = 0; t < NT; t++)
        printf("%.2f  %10llu  %10llu  %8llu  %.4f  |  %10llu  %8llu  %.4f\n", thetas[t], (unsigned long long)zc[t],
               (unsigned long long)A1[t], (unsigned long long)(A1[t] - nboth), (double)(A1[t] - nboth) / A1[t],
               (unsigned long long)A2[t], (unsigned long long)(A2[t] - nboth), (double)(A2[t] - nboth) / A2[t]);
    return 0;
}
