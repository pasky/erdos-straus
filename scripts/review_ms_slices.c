/* R197 from-scratch: primes p <= N (odd, p !| m) with S_m(p) empty, i.e. no word (t,u,v) >= 1,
 * t*u*v - u - v = p, with m | tu-1, m | tv-1, m | t, m | u or m | v  (MODEL_SPECIFIC Cor 3.2 EVIDENCE, §6 row 1).
 * Direct enumeration: t = 1 via divisors of p+1; t >= 2, 1 <= u <= (p+1)/(t-1), v = (p+u)/(tu-1). Early exit.
 * usage: review_ms_slices m N
 */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll M;
static int in(ll t, ll u, ll v) {
    return (t * u - 1) % M == 0 || (t * v - 1) % M == 0 || t % M == 0 || u % M == 0 || v % M == 0;
}
static int has(ll p) {
    for (ll a = 1; a * a <= p + 1; a++)
        if ((p + 1) % a == 0) {
            ll b = (p + 1) / a;
            if (in(1, a + 1, b + 1) || in(1, b + 1, a + 1)) return 1;
        }
    for (ll t = 2; t <= p + 2; t++) {
        ll um = (p + 1) / (t - 1);
        for (ll u = 1; u <= um; u++) {
            ll A = t * u - 1;
            if ((p + u) % A == 0) {
                ll v = (p + u) / A;
                if (in(t, u, v)) return 1;
            }
        }
    }
    return 0;
}
int main(int argc, char **argv) {
    M = atoll(argv[1]);
    ll N = atoll(argv[2]);
    char *c = calloc(N + 1, 1);
    for (ll i = 2; i * i <= N; i++) if (!c[i]) for (ll j = i * i; j <= N; j += i) c[j] = 1;
    long k = 0, np = 0;
    for (ll p = 3; p <= N; p += 2) {
        if (c[p] || M % p == 0) continue;
        np++;
        if (!has(p)) { printf("%lld\n", p); fflush(stdout); k++; }
    }
    fprintf(stderr, "m=%lld N=%lld primes=%ld S_m empty at %ld\n", M, N, np, k);
    return 0;
}
