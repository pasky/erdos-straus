/* R198 from-scratch census (independent of cf_census.c).
   For every odd n <= N: X_n = positive words (t,u,v), tuv-u-v=n (boundary words included);
   chi = (-A/n), A = tu-1. Enumeration: for (t,u) with A=tu-1>=1, v>=1, n = A v - u.
   Output: odd non-square n with chi == +1 on all of X_n; odd n with chi == -1 on all of X_n (count, list);
   squares; primes p = 1 mod 8 statistics; parity facts at p = 1 mod 4.
   Build: gcc -O2 -o /tmp/rcc scripts/review_cf_census.c ; run /tmp/rcc 1000000 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static int jac(long a, long n) { /* Jacobi (a/n), n odd > 0 */
    a %= n; if (a < 0) a += n;
    int r = 1;
    while (a) {
        while (!(a & 1)) { a >>= 1; long m = n & 7; if (m == 3 || m == 5) r = -r; }
        long t = a; a = n; n = t;
        if ((a & 3) == 3 && (n & 3) == 3) r = -r;
        a %= n;
    }
    return n == 1 ? r : 0;
}

int main(int argc, char **argv) {
    long N = atol(argv[1]);
    int *tot = calloc(N + 1, sizeof(int)), *neg = calloc(N + 1, sizeof(int)), *zero = calloc(N + 1, sizeof(int));
    for (long t = 1; t <= N + 2; t++)
        for (long u = 1; u <= N + 2; u++) {
            long A = t * u - 1;
            if (A <= 0) continue;
            if (A - u > N) break;
            for (long v = 1;; v++) {
                long n = A * v - u;
                if (n > N) break;
                if (n < 1 || !(n & 1)) continue;
                tot[n]++;
                int j = jac(-A, n);
                if (j == -1) neg[n]++; else if (j == 0) zero[n]++;
            }
        }
    char *comp = calloc(N + 1, 1);
    for (long i = 2; i * i <= N; i++) if (!comp[i]) for (long j = i * i; j <= N; j += i) comp[j] = 1;
    long nz = 0, cplus = 0, cminus = 0, nsq = 0, sqbad = 0; double sqmean = 0;
    long np = 0; double rsum = 0, rmin = 2; long amin = 0, mn = 0, mt = 0;
    long par_bad = 0, half_even = 0, half_odd = 0;
    printf("odd non-square n with chi==+1 on X_n: ");
    for (long n = 1; n <= N; n += 2) {
        if (zero[n]) nz++;
        long r = (long)llround(sqrt((double)n)); int sq = (r * r == n);
        if (sq) { if (n > 1) { nsq++; sqmean += tot[n]; if (neg[n]) sqbad++; } continue; }
        if (tot[n] > 0 && neg[n] == 0) { cplus++; printf("%ld(|X|=%d) ", n, tot[n]); }
        if (tot[n] == 0) printf("[EMPTY %ld] ", n);
    }
    printf("\ncount %ld\nodd n with chi==-1 on all of X_n: ", cplus);
    for (long n = 3; n <= N; n += 2)
        if (tot[n] > 0 && neg[n] == tot[n]) { cminus++; if (cminus <= 12) printf("%ld%s ", n, (n % 4 == 3) ? "" : "(!1mod4)"); if (n % 4 != 3) printf("[NOT 3 mod 4: %ld] ", n); }
    printf("\ncount %ld\n", cminus);
    printf("odd squares 9..N: %ld, with a chi=-1 word: %ld, mean |X| %.1f\n", nsq, sqbad, sqmean / nsq);
    for (long p = 3; p <= N; p += 2) {
        if (comp[p]) continue;
        if (p % 4 == 1) { if (neg[p] % 2 || tot[p] % 2 == 0) par_bad++; }
        if (p % 8 == 1) {
            np++; double r = (double)neg[p] / tot[p]; rsum += r;
            if (r < rmin) { rmin = r; amin = p; mn = neg[p]; mt = tot[p]; }
            if (p < 100000) { if ((neg[p] / 2) % 2) half_odd++; else half_even++; }
        }
    }
    printf("words with gcd(A,n)>1 at %ld odd n\n", nz);
    printf("primes p=1 mod 8: %ld, mean N-/|X| %.3f, min %ld/%ld at p=%ld\n", np, rsum / np, mn, mt, amin);
    printf("p=1 mod 4 violating (N- even, |X| odd): %ld; p=1 mod 8 <1e5: N-/2 even %ld, odd %ld\n", par_bad, half_even, half_odd);
    return 0;
}
