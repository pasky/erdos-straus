// z68_sign_cells.c — all length-3 words of single odd n ≡ 1 (mod 4) (n <= 9e12: factorisation by trial division with primes < 3.1e6), with sign and 2-adic cell counts.
// Word: (t,u,v), t,u,v >= 2, tuv - u - v = n, A = tu - 1.  Enumeration: the smaller outer letter u <= sqrt(n/2)+1;
// for each such u, all divisors A of n+u with A ≡ -1 (mod u), 2u-1 <= A <= (n+u)/2, v = (n+u)/A >= u
// (v = u counted once).  Sign (A/n) by direct Jacobi.  Prints per n: #words (ordered pairs counted once per
// unordered {u,v}), N- (pairs with Jacobi -1), #pairs with 4|t, with 8|t, and the -1 pairs.
// Usage: ./z68_sign_cells n1 n2 ...   (or read n from stdin if no args)
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long ull; typedef __int128 i128;
static int jacobi(ull a, ull n) { // n odd positive
    int s = 1; a %= n;
    while (a) {
        while ((a & 1) == 0) { a >>= 1; ull r = n & 7; if (r == 3 || r == 5) s = -s; }
        ull t = a; a = n; n = t;
        if ((a & 3) == 3 && (n & 3) == 3) s = -s;
        a %= n;
    }
    return n == 1 ? s : 0;
}
static ull fac_p[64]; static int fac_e[64]; static int nf;
static unsigned *pr; static int npr;
static void sieve(unsigned lim) {
    char *c = calloc(lim + 1, 1); pr = malloc(sizeof(unsigned) * (lim / 2 + 10)); npr = 0;
    for (unsigned i = 2; i <= lim; i++) if (!c[i]) { pr[npr++] = i; for (unsigned long j = (unsigned long)i * i; j <= lim; j += i) c[j] = 1; }
    free(c);
}
static void factor(ull m) {
    nf = 0;
    for (int i = 0; i < npr && (ull)pr[i] * pr[i] <= m; i++) {
        ull q = pr[i];
        if (m % q == 0) { fac_p[nf] = q; fac_e[nf] = 0; while (m % q == 0) { m /= q; fac_e[nf]++; } nf++; }
    }
    if (m > 1) { fac_p[nf] = m; fac_e[nf] = 1; nf++; }
}
static ull divs[200000]; static int nd;
static void gen(int i, ull d) {
    if (i == nf) { divs[nd++] = d; return; }
    ull x = d; for (int e = 0; e <= fac_e[i]; e++) { gen(i + 1, x); x *= fac_p[i]; }
}
static void doit(ull n) {
    if (n < 5 || n % 4 != 1 || n > 9000000000000ULL) { fprintf(stderr, "domain: n = 1 (mod 4), 5 <= n <= 9e12 (trial-division sieve to 3.1e6 must exceed sqrt(n + u))\n"); exit(1); }
    ull umax = 2; while ((umax + 1) * (umax + 1) <= n / 2 + 2) umax++; umax += 1;
    long pairs = 0, neg = 0, t4 = 0, t8 = 0, t4neg = 0;
    int printed = 0;
    for (ull u = 2; u <= umax; u++) {
        ull N = n + u; factor(N); nd = 0; gen(0, 1);
        for (int k = 0; k < nd; k++) {
            ull A = divs[k];
            if ((A + 1) % u) continue;
            if (A < 2 * u - 1 || A > N / 2) continue;
            ull v = N / A; if (v < u) continue;     // u = smaller outer letter
            ull t = (A + 1) / u; if (t < 2) continue;
            // sanity
            if ((i128)t * u * v - u - v != (i128)n) { fprintf(stderr, "BUG\n"); exit(1); }
            int s = jacobi(A, n);
            pairs++; if (s == -1) neg++;
            if (t % 4 == 0) { t4++; if (s == -1) t4neg++; }
            if (t % 8 == 0) t8++;
            if (s == -1 && printed < 6) { printf("  neg word (t,u,v)=(%llu,%llu,%llu) A=%llu cell=(%llu,%llu,%llu)mod4\n", t, u, v, A, t % 4, u % 4, v % 4); printed++; }
        }
    }
    printf("n=%llu pairs=%ld Nneg=%ld t4=%ld t8=%ld t4neg=%ld\n", n, pairs, neg, t4, t8, t4neg);
    if (t4 != t4neg) { fprintf(stderr, "4|t word with sign +1 at %llu: contradicts DK Prop 3.1\n", n); exit(1); }
    fflush(stdout);
}
int main(int argc, char **argv) {
    sieve(3100000);   // enough for n + u < 9.6e12
    if (argc > 1) for (int i = 1; i < argc; i++) doit(strtoull(argv[i], 0, 10));
    else { ull n; while (scanf("%llu", &n) == 1) doit(n); }
    return 0;
}
