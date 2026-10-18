/* R280 from-scratch census for O269 Prop S (and DEDEKIND §9.1 as used there).
   For n ≡ 1 (mod 4), n ≤ NMAX: L3[n] = 1 iff some ES word (t,u,v) (t,u,v ≥ 2, tuv−u−v = n) has (tv−1 / n) = −1
   (HJ length-3 A = tv−1, since n/A = [[u, t, v]]); L2[n] = 1 iff some b | n+1, 2 ≤ b ≤ (n+1)/2, has (b/n) = −1
   (HJ length 2: n/b = a − 1/b, n = ab − 1).  λ(n) ≤ 3 iff L2 or L3 (length 1 is A = 1, symbol +1).
   Prints: non-squares with λ > 3 (Z \ □), non-squares with no length-3 certificate ({N₋ = 0} \ □),
   and odd squares wrongly certified (must be none).
   Build: gcc -O2 -o /tmp/r280_census scripts/review_r280_census.c ; run: /tmp/r280_census 1000000 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static int jacobi(long a, long n) { /* n odd positive */
    int s = 1; a %= n; if (a < 0) a += n;
    while (a) {
        while (!(a & 1)) { a >>= 1; long r = n & 7; if (r == 3 || r == 5) s = -s; }
        long t = a; a = n; n = t;
        if ((a & 3) == 3 && (n & 3) == 3) s = -s;
        a %= n;
    }
    return n == 1 ? s : 0;
}
static int issq(long n) { long r = (long)sqrtl((long double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++; return r * r == n; }

int main(int argc, char **argv) {
    long NMAX = argc > 1 ? atol(argv[1]) : 1000000;
    char *L2 = calloc(NMAX + 1, 1), *L3 = calloc(NMAX + 1, 1);
    long words = 0;
    for (long t = 2; 4 * t - 4 <= NMAX; t++)
        for (long u = 2; t * u * 2 - u - 2 <= NMAX; u++)
            for (long v = 2; ; v++) {
                long n = t * u * v - u - v; if (n > NMAX) break;
                words++;
                if ((n & 3) != 1 || L3[n]) continue;
                if (jacobi(t * v - 1, n) == -1) L3[n] = 1;
            }
    for (long b = 2; 2 * b - 1 <= NMAX; b++)
        for (long a = 2; a * b - 1 <= NMAX; a++) {
            long n = a * b - 1;
            if ((n & 3) != 1 || L2[n]) continue;
            if (jacobi(b, n) == -1) L2[n] = 1;
        }
    long nz = 0, nn = 0, badsq = 0, nsq = 0;
    printf("words enumerated: %ld\nZ \\ squares (lambda>3):", words);
    for (long n = 1; n <= NMAX; n += 4) {
        int sq = issq(n);
        if (sq) { nsq++; if (L2[n] || L3[n]) badsq++; continue; }
        if (!L2[n] && !L3[n]) { printf(" %ld", n); nz++; }
    }
    printf("\n{N- = 0} \\ squares (no length-3 certificate):");
    for (long n = 1; n <= NMAX; n += 4) if (!issq(n) && !L3[n]) { printf(" %ld", n); nn++; }
    printf("\ncounts: |Z\\sq|=%ld |N-=0 \\ sq|=%ld odd squares=%ld certified-squares(bad)=%ld\n", nz, nn, nsq, badsq);
    printf("105 m^2, m odd 3..97, lambda<=3 for all:");
    int ok = 1; for (long m = 3; m <= 97; m += 2) { long n = 105 * m * m; if (n > NMAX) { ok = -1; break; } if (!L2[n] && !L3[n]) { ok = 0; printf(" FAIL %ld", m); } }
    printf(" %s; with interior (length-3) certificate for all:", ok == 1 ? "yes" : "NO");
    ok = 1; for (long m = 3; m <= 97; m += 2) { long n = 105 * m * m; if (n <= NMAX && !L3[n]) { ok = 0; printf(" no-L3 %ld", m); } }
    printf(" %s\n", ok ? "yes" : "NO");
    long mm = 1; while (105 * (mm + 2) * (mm + 2) <= NMAX && (L2[105 * (mm + 2) * (mm + 2)] || L3[105 * (mm + 2) * (mm + 2)])) mm += 2;
    printf("largest odd m0 with 105 m^2 <= NMAX and lambda(105 m^2) <= 3 for all odd 3 <= m <= m0: %ld (periods M <= %ld excluded)\n", mm, mm - 1);
    return 0;
}
