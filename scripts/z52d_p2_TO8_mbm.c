// z52d P2 TO8: per prime p: R*(p) (genus-split form, should equal R(p)), M_BM(p)=sum_{P(p), gcd(p,q)=1}(1-chi_{-4uB}(p))/phi(4uB), M0(p)=sum 1/phi(4uB)
// P(p) = {(u,B): gcd(u,B)=1, u+B odd, 4uB-u-B <= p}; q=4uB; chi_{-4uB}(p) = Legendre(-uB / p) (p≡1 mod 4).
// usage: z52d_p2_TO8_mbm < primes  -> p Rstar M_BM M0
#include <stdio.h>
#include <stdlib.h>
#define NPHI 2000000
static long phi_t[NPHI + 1];
static long gcdl(long a, long b) { while (b) { long t = a % b; a = b; b = t; } return a; }
int main(void) {
    for (long i = 0; i <= NPHI; i++) phi_t[i] = i;
    for (long i = 2; i <= NPHI; i++) if (phi_t[i] == i) for (long j = i; j <= NPHI; j += i) phi_t[j] -= phi_t[j] / i;
    long p;
    signed char *leg = NULL; long lcap = 0;
    while (scanf("%ld", &p) == 1) {
        if (p + 8 > lcap) { free(leg); lcap = p + 8; leg = malloc(lcap); }
        for (long x = 0; x < p; x++) leg[x] = -1;
        leg[0] = 0;
        for (long x = 1; x < p; x++) leg[(x * x) % p] = 1;
        long Rs = 0; double M = 0, M0 = 0;
        for (long u = 1; u <= p; u++) {
            for (long B = 1; ; B++) {
                long q = 4 * u * B;
                if (q - u - B > p) break;     // 4uB-u-B increasing in B for u>=1 (q grows faster)
                if (((u + B) & 1) == 0) continue;
                if (gcdl(u, B) != 1) continue;
                long ph = 4 * phi_t[u] * phi_t[B];  // phi(4uB)=4 phi(u) phi(B) since exactly one of u,B is even (u+B odd)
                // careful: phi(4uB)=phi(4)phi(uB)/... use exact: phi(4uB)=2*phi(2uB)*? replace by direct:
                ph = 0; { long m = 4 * u * B; /* exact phi via factorization of m */ long mm = m, r = m; for (long f = 2; f * f <= mm; f++) if (mm % f == 0) { while (mm % f == 0) mm /= f; r -= r / f; } if (mm > 1) r -= r / mm; ph = r; }
                M0 += 1.0 / ph;
                long nq = (p + u + B);        // need p ≡ -(u+B) mod q
                if ((nq) % q == 0) Rs++;       // p ≡ -(u+B) (mod q)  <=> q | p+u+B
                if (p % q == 0) continue;
                long t = ((-(u * B)) % p + p) % p;
                int chi = leg[t];
                M += (1.0 - chi) / ph;
            }
        }
        printf("%ld %ld %.6f %.6f\n", p, Rs, M, M0);
    }
    return 0;
}
