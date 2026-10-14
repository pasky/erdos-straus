/* R206 from-scratch check of TORSION_FIRING §4.1: which primes p <= P have NO Type II solution
 * 4/p = 1/x + 1/(p y') + 1/(p z')  (p !| x) such that 4y'-1 is prime (either ordering of y', z').
 *
 * Stage 1 (sieve, uses only the (c,d)-form h | p + 4c^2 d, 4cd | h+1, of FIXED_MODULUS_SHOTS Lemma 1.1, written
 *   independently of the author's c/j-form): for each prime h = 3 mod 4, h <= H0, and each (c,d) with cd | (h+1)/4,
 *   mark all p = -4c^2 d (mod h).
 * Stage 2 (direct, no lemma): for each unmarked prime p, enumerate ALL Type II solutions by x in [ceil((p+1)/4),
 *   (p-1)/2], e = 4x - p, y' in (x/e, 2x/e], z' = x y'/(e y' - x) integer; record moduli 4y'-1, 4z'-1; test primality.
 * Mode "check": run stage 2 on ALL primes <= P and compare with stage 1 at H0 = (P+1)(P+5)/4 (validation).
 * Usage: review_tf_primemod run P H0 [S] | review_tf_primemod check P | review_tf_primemod list p
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef unsigned long long u64;
typedef unsigned __int128 u128;

static u64 mulmod(u64 a, u64 b, u64 m) { return (u64)((u128)a * b % m); }
static u64 powmod(u64 a, u64 e, u64 m) { u64 r = 1; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int isprime64(u64 n) {
    if (n < 2) return 0;
    static const u64 sp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (int i = 0; i < 12; i++) { if (n % sp[i] == 0) return n == sp[i]; }
    u64 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
    for (int i = 0; i < 12; i++) {
        u64 x = powmod(sp[i], d, n);
        if (x == 1 || x == n - 1) continue;
        int ok = 0;
        for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } }
        if (!ok) return 0;
    }
    return 1;
}

static unsigned char *comp;   /* simple sieve of Eratosthenes up to N */
static void eratos(u64 N) {
    comp = calloc(N + 1, 1);
    comp[0] = comp[1] = 1;
    for (u64 i = 2; i * i <= N; i++) if (!comp[i]) for (u64 j = i * i; j <= N; j += i) comp[j] = 1;
}

static unsigned char *marked;
static void stage1(u64 P, u64 H0) {
    marked = calloc(P + 1, 1);
    u64 divs[4096]; int nd;
    for (u64 h = 3; h <= H0; h += 4) {           /* h = 3 mod 4 */
        if (comp[h]) continue;
        u64 k = (h + 1) / 4;
        nd = 0;
        for (u64 a = 1; a * a <= k; a++) if (k % a == 0) { divs[nd++] = a; if (a * a != k) divs[nd++] = k / a; }
        for (int i = 0; i < nd; i++) {
            u64 m = divs[i];                       /* m = cd */
            for (int jj = 0; jj < nd; jj++) {
                u64 c = divs[jj];
                if (c > m || m % c) continue;
                u64 d = m / c;
                u64 v = (u64)((u128)4 * c * c * d % h);
                u64 r = (h - v) % h;                 /* p = -4c^2 d mod h */
                for (u64 p = r; p <= P; p += h) marked[p] = 1;
            }
        }
    }
}

/* returns number of prime moduli; optionally prints all solutions */
static int stage2(u64 p, int verbose, int *nsol) {
    int nprime = 0; *nsol = 0;
    for (u64 x = (p + 1 + 3) / 4; 2 * x < p; x++) {
        u64 e = 4 * x - p;
        if (x % p == 0) continue;
        u64 lo = x / e + 1, hi = 2 * x / e;
        for (u64 y = lo; y <= hi; y++) {
            u64 den = e * y - x;
            u128 num = (u128)x * y;
            if (num % den) continue;
            u64 z = (u64)(num / den);
            (*nsol)++;
            u64 h1 = 4 * y - 1, h2 = 4 * z - 1;
            int a = isprime64(h1), b = isprime64(h2);
            nprime += a + (b && h2 != h1);
            if (verbose) printf("  x=%llu y'=%llu z'=%llu  h=%llu%s  h'=%llu%s\n", x, y, z, h1, a ? "(P)" : "", h2, b ? "(P)" : "");
        }
    }
    return nprime;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    if (!strcmp(argv[1], "list")) {
        u64 p = strtoull(argv[2], 0, 10); int ns;
        int np = stage2(p, 1, &ns);
        printf("p=%llu: %d unordered Type II solutions, %d prime moduli\n", p, ns, np);
        return 0;
    }
    u64 P = strtoull(argv[2], 0, 10);
    if (!strcmp(argv[1], "check")) {
        u64 H0 = (P + 1) * (P + 5) / 4;
        eratos(H0); stage1(P, H0);
        int bad = 0, cnt = 0, none = 0;
        for (u64 p = 5; p <= P; p += 2) if (!comp[p]) {
            int ns; int np = stage2(p, 0, &ns); cnt++;
            if ((np > 0) != (marked[p] != 0)) { bad++; printf("MISMATCH p=%llu stage2=%d sieve=%d\n", p, np, marked[p]); }
            if (!np) { none++; printf("no prime-modulus cert: p=%llu (%d solutions)\n", p, ns); }
        }
        printf("check: %d primes 5..%llu, mismatches %d, without prime cert %d\n", cnt, P, bad, none);
        return 0;
    }
    u64 H0 = strtoull(argv[3], 0, 10);
    eratos(P > H0 ? P : H0); stage1(P, H0);
    if (argc > 4) {   /* spot-check: the last S marked primes <= P really have a prime-modulus certificate */
        int S = atoi(argv[4]), done = 0, bad = 0;
        for (u64 p = P; p > 5 && done < S; p--) if (!comp[p] && (p & 1) && marked[p]) {
            int ns; int np = stage2(p, 0, &ns); done++; if (!np) { bad++; printf("FALSE MARK p=%llu\n", p); }
        }
        printf("spot-check: %d marked primes near %llu re-enumerated directly, false marks %d\n", done, P, bad);
    }
    int cnt = 0, unm = 0, none = 0;
    for (u64 p = 5; p <= P; p += 2) if (!comp[p]) {
        cnt++;
        if (marked[p]) continue;
        unm++;
        int ns; int np = stage2(p, 0, &ns);
        if (!np) { none++; printf("NO prime-modulus Type II certificate: p=%llu (%d unordered solutions)\n", p, ns); }
        else printf("unmarked at H0 but has prime cert: p=%llu (%d prime moduli)\n", p, np);
        fflush(stdout);
    }
    printf("run: %d primes 5..%llu, unmarked after stage 1 (H0=%llu): %d, without prime cert: %d\n", cnt, P, H0, unm, none);
    return 0;
}
