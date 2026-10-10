/* O128 step 3: per-p "Heegner" prediction of f_II(p) and its per-d families.
 * For each prime p (read from stdin, one per line), loop over (a,c,d), gcd(a,c)=1, f = 4acd-1, in the
 * Type II range with a <= b (b_real = (a+pc)/f >= a, c <= a + b_real), weight w = 2 (1 if b = a):
 *   actual  += w * [ (2ad)^2 + dp ≡ 0 (mod f) ]          (= Type II solution; Lemma 1.1.2 / §4)
 *   E_heeg  += w * rho_{-dp}(f) / f                         (random-residue model for fixed p)
 *   E_avg   += w * 1/phi(f)                                 (average-over-p model)
 * where rho_D(f) = #{nu mod f : nu^2 ≡ D (mod f)}. Families: d = 1, d = 2..7, d in [8,63], d >= 64.
 * Output per p: p actual E_heeg E_avg  and per family actual/E_heeg.
 * Usage: t2s_predict PMAX < primes.txt   (PMAX bounds the spf sieve: need 4*PMAX)
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

static uint32_t *spf; static uint64_t SMAX;
static uint64_t gcd(uint64_t x, uint64_t y) { while (y) { uint64_t t = x % y; x = y; y = t; } return x; }
static int jacobi(int64_t a, int64_t n) { /* n odd positive */
    a %= n; if (a < 0) a += n; int r = 1;
    while (a) { while (!(a & 1)) { a >>= 1; int m = n & 7; if (m == 3 || m == 5) r = -r; }
        int64_t t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) r = -r; a %= n; }
    return n == 1 ? r : 0;
}
/* rho_{-dp}(f) and phi(f) for odd f, gcd(f,d)=1 */
static void rho_phi(uint64_t f, uint64_t d, uint64_t p, double *rho, double *phi) {
    double r = 1, ph = 1; uint64_t m = f;
    while (m > 1) {
        uint64_t q = spf[m]; int k = 0; uint64_t qk = 1;
        while (m % q == 0) { m /= q; k++; qk *= q; }
        ph *= (double)(qk / q) * (q - 1);
        if (q == p) { r *= (k == 1) ? 1 : 0; }
        else { int64_t D = -(int64_t)((d % q) * (p % q) % q); r *= 1 + jacobi(D, q); }
    }
    *rho = r; *phi = ph;
}

int main(int argc, char **argv) {
    uint64_t PMAX = strtoull(argv[1], 0, 10); SMAX = 4 * PMAX + 16;
    spf = calloc(SMAX + 1, 4);
    for (uint64_t i = 2; i <= SMAX; i++) if (!spf[i]) for (uint64_t j = i; j <= SMAX; j += i) if (!spf[j]) spf[j] = i;
    uint64_t p;
    printf("# p actual E_heeg E_avg | fam d=1: act E | d=2..7 | d=8..63 | d>=64\n");
    while (scanf("%llu", (unsigned long long *)&p) == 1) {
        double act = 0, Eh = 0, Ea = 0, fa[4] = {0}, fe[4] = {0};
        for (uint64_t a = 1; 4 * a * a <= p + 4 * a; a++)
            for (uint64_t d = 1; 4 * a * a * d <= p + 2 * a; d++)
                for (uint64_t c = 1;; c++) {
                    uint64_t f = 4 * a * c * d - 1;
                    double breal = (double)(a + p * c) / f;
                    if (breal < a) break;                 /* b decreasing in c */
                    if (c > a + breal) break;
                    if (gcd(a, c) != 1) continue;
                    if (f > SMAX) { fprintf(stderr, "f too big\n"); exit(1); }
                    double rho, phi; rho_phi(f, d, p, &rho, &phi);
                    uint64_t nu = (2 * a * d) % f;
                    int hit = ((nu * nu + (d % f) * (p % f)) % f) == 0;
                    double w = 2;
                    if (hit && (a + p * c) / f == a) w = 1;
                    int fam = d == 1 ? 0 : d < 8 ? 1 : d < 64 ? 2 : 3;
                    double eh = w * rho / f;
                    if (hit) { act += w; fa[fam] += w; }
                    Eh += eh; fe[fam] += eh; Ea += w / phi;
                }
        printf("%llu %.0f %.3f %.3f", (unsigned long long)p, act, Eh, Ea);
        for (int i = 0; i < 4; i++) printf(" | %.0f %.3f", fa[i], fe[i]);
        printf("\n"); fflush(stdout);
    }
    return 0;
}
