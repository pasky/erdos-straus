// z68_sign_lengths.c — KT3: per prime p ≡ 1 (mod 8), p <= P, the number of A in (0,p) with HJ length r(p/A) = r
// and the number of those with Legendre symbol (A/p) = -1, for r = 2..5 (A and A* = A^{-1} both counted).
// Usage: ./z68_sign_lengths P > out ; columns: p |L2| neg2 |L3| neg3 |L4| neg4 |L5| neg5
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int hjlen_le(ll N, ll D, int cap) {
    int r = 0;
    while (D > 0) { r++; if (r > cap) return cap + 1; ll b = (N + D - 1) / D; ll nd = b * D - N; N = D; D = nd; }
    return r;
}
static int jacobi(ll a, ll n) {
    int s = 1; a %= n; if (a < 0) a += n;
    while (a) {
        while ((a & 1) == 0) { a >>= 1; ll r = n & 7; if (r == 3 || r == 5) s = -s; }
        ll t = a; a = n; n = t;
        if ((a & 3) == 3 && (n & 3) == 3) s = -s;
        a %= n;
    }
    return n == 1 ? s : 0;
}
int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: P\n"); return 1; }
    ll P = atoll(argv[1]);
    if (P < 10 || P > 100000000) { fprintf(stderr, "10 <= P <= 1e8\n"); return 1; }
    
    char *c = calloc(P + 1, 1);
    for (ll i = 2; i * i <= P; i++) if (!c[i]) for (ll j = i * i; j <= P; j += i) c[j] = 1;
    printf("# p L2 neg2 L3 neg3 L4 neg4 L5 neg5  (HJ length r(p/A), A in (0,p))\n");
    for (ll p = 9; p <= P; p += 8) {
        if (c[p]) continue;
        long L[7] = {0}, N[7] = {0};
        for (ll A = 1; A < p; A++) {
            int r = hjlen_le(p, A, 5);
            if (r < 2 || r > 5) continue;
            L[r]++;
            if (jacobi(A, p) == -1) N[r]++;
        }
        printf("%lld %ld %ld %ld %ld %ld %ld %ld %ld\n", p, L[2], N[2], L[3], N[3], L[4], N[4], L[5], N[5]);
    }
    return 0;
}
