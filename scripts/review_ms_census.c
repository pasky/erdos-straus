/* R197 from-scratch census for m/p = 1/x + 1/y + 1/z, p odd prime, p !| m (MODEL_SPECIFIC §1, §2, §6).
 *
 * Complete search: smallest denominator x in (p/m, 3p/m]; A = m x - p > 0, B = p x, gcd(A,B) = 1 for prime p
 * (p !| m x since x < p; gcd(mx - p, x) = gcd(p, x) = 1). Then 1/y + 1/z = A/B  <=>  (Ay - B)(Az - B) = B^2,
 * so y = (d + B)/A, z = (B^2/d + B)/A for divisors d | B^2 with d == -B (mod A); d <= B gives y <= z.
 * Every solution is re-verified exactly (A y - B = d, A z - B = B^2/d, d * (B^2/d) = B^2 in 128-bit, and the
 * resulting identity m*x*y*z == p*(xy+yz+zx) modulo three 61-bit primes).
 *
 * usage: review_ms_census m N mode       mode: all | t1 | t2 | oneodd | alleven     -> prints failing primes <= N
 *        review_ms_census m p count       -> number of solutions x<=y<=z and their breakdowns (p prime)
 * Filters: t1 = exactly one denominator divisible by p; t2 = exactly two; oneodd = exactly one odd denominator.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef unsigned long long u64;
typedef unsigned __int128 u128;

static uint32_t *spf;
static u64 M, P, A, B;
static u128 B2;
static int mode; /* 0 all, 1 t1, 2 t2, 3 oneodd, 4 alleven, 9 count */
static u64 X;
static long long cnt, cnt_t1, cnt_t2, cnt_odd[4];
static int found;
static u64 pr[64]; static int ex[64]; static int np;

static u64 mulmod(u64 a, u64 b, u64 q) { return (u64)((u128)a * b % q); }

static int verify(u64 x, u64 y, u128 z, u64 d) {
    u128 e = B2 / d;
    if ((u128)A * y - B != d) return 0;
    if ((u128)A * z - B != e) return 0;
    if ((u128)d * e != B2) return 0;
    static const u64 Q[3] = {2305843009213693951ULL, 2305843009213693921ULL, 2305843009213693907ULL};
    for (int i = 0; i < 3; i++) {
        u64 q = Q[i];
        u64 zq = (u64)(z % q);
        u64 l = mulmod(mulmod(M % q, x % q, q), mulmod(y % q, zq, q), q);
        u64 s = (mulmod(x % q, y % q, q) + mulmod(y % q, zq, q)) % q;
        s = (s + mulmod(zq, x % q, q)) % q;
        if (l != mulmod(P % q, s, q)) return 0;
    }
    return 1;
}

static int accept(u64 x, u64 y, u128 z) {
    int dp = (x % P == 0) + (y % P == 0) + (z % P == 0);
    int odd = (x & 1) + (y & 1) + (z & 1);
    switch (mode) {
    case 0: return 1;
    case 1: return dp == 1;
    case 2: return dp == 2;
    case 3: return odd == 1;
    case 4: return odd == 0;
    case 9:
        cnt++; if (dp == 1) cnt_t1++; if (dp == 2) cnt_t2++;
        cnt_odd[odd]++;
        return 0;
    }
    return 0;
}

static void rec(int i, u64 d) {
    if (found) return;
    if (i == np) {
        if ((d + B) % A) return;
        u64 y = (d + B) / A;
        u128 z = (B2 / d + B) / A;
        if (mode == 9 && y < X) return; /* x <= y <= z for counting */
        if (!verify(X, y, z, d)) { fprintf(stderr, "VERIFY FAIL p=%llu x=%llu\n", P, X); exit(3); }
        if (accept(X, y, z)) found = 1;
        return;
    }
    u64 q = 1;
    for (int e = 0; e <= ex[i]; e++) {
        if ((u128)d * q > B) break;
        rec(i + 1, d * q);
        if ((u128)q * pr[i] > B) break;
        q *= pr[i];
    }
}

static int solve(u64 m, u64 p) {
    M = m; P = p; found = 0;
    u64 x0 = p / m + 1, x1 = 3 * p / m;
    for (u64 x = x0; x <= x1 && !found; x++) {
        X = x; A = m * x - p; B = p * x; B2 = (u128)B * B;
        np = 0; pr[np] = p; ex[np++] = 2;
        u64 r = x;
        while (r > 1) {
            u64 q = spf[r]; int e = 0;
            while (r % q == 0) { r /= q; e++; }
            pr[np] = q; ex[np++] = 2 * e;
        }
        rec(0, 1);
    }
    return found;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage\n"); return 1; }
    u64 m = strtoull(argv[1], 0, 10), N = strtoull(argv[2], 0, 10);
    const char *md = argv[3];
    mode = !strcmp(md, "all") ? 0 : !strcmp(md, "t1") ? 1 : !strcmp(md, "t2") ? 2 : !strcmp(md, "oneodd") ? 3
         : !strcmp(md, "alleven") ? 4 : 9;
    u64 S = 3 * N / m + 2;
    spf = calloc(S + 1, sizeof(uint32_t));
    for (u64 i = 2; i <= S; i++) if (!spf[i]) for (u64 j = i; j <= S; j += i) if (!spf[j]) spf[j] = i;
    if (mode == 9) {
        for (u64 q = 2; q * q <= N; q++) if (N % q == 0) { fprintf(stderr, "%llu not prime\n", N); return 1; }
        cnt = cnt_t1 = cnt_t2 = 0; memset(cnt_odd, 0, sizeof cnt_odd);
        solve(m, N);
        printf("m=%llu p=%llu solutions=%lld typeI=%lld typeII=%lld odd-count[0..3]=%lld %lld %lld %lld\n", m, N,
               cnt, cnt_t1, cnt_t2, cnt_odd[0], cnt_odd[1], cnt_odd[2], cnt_odd[3]);
        return 0;
    }
    /* odd primes up to N by sieve */
    char *comp = calloc(N + 1, 1);
    long nf = 0, np_ = 0;
    for (u64 i = 2; i * i <= N; i++) if (!comp[i]) for (u64 j = i * i; j <= N; j += i) comp[j] = 1;
    for (u64 p = 3; p <= N; p += 2) {
        if (comp[p] || m % p == 0) continue;
        np_++;
        if (!solve(m, p)) { printf("%llu\n", p); nf++; fflush(stdout); }
    }
    fprintf(stderr, "m=%llu N=%llu mode=%s primes=%ld failing=%ld\n", m, N, md, np_, nf);
    return 0;
}
