/* Z2874: tetrahedral analogue of the altitude form of ES.  For a tetrahedron, 1/r = sum_{i=1..4} 1/h_i, face areas
 * A_i = 3V/h_i.  Four positive numbers are face areas of a (non-degenerate) tetrahedron iff each is < the sum of the other
 * three (Minkowski: close a spatial 4-gon of unit normals weighted by A_i), and the volume can then be matched by scaling,
 * so "4/n = sum 1/h_i realisable" <=> every h_i > n/2.  h_i = n (regular tetrahedron) always works; this program asks
 * the non-trivial version: DISTINCT integer altitudes h1<h2<h3<h4, all > n/2, sum 1/h_i = 4/n, for every n in [3, NMAX];
 * also, for comparison, the triangle version (3 terms, all > n/2), which the repo shows fails at every prime p = 1 (4).
 * usage: tetra NMAX   (exact integer arithmetic)
 */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef __int128 i128;
static ll gcdl(ll a, ll b) { while (b) { ll t = a % b; a = b; b = t; } return a; }
static int distinct4(ll n, ll *w) {
    for (ll h1 = n / 2 + 1; h1 < n; h1++) {               /* min h < n because 4 distinct terms average 1/n */
        ll a1 = 4 * h1 - n, b1 = n * h1; if (a1 <= 0) continue; ll g = gcdl(a1, b1); a1 /= g; b1 /= g;   /* R1 = a1/b1 */
        for (ll h2 = h1 + 1; (i128)3 * b1 > (i128)a1 * h2; h2++) {        /* 3/h2 > R1 */
            i128 a2 = (i128)a1 * h2 - b1, b2 = (i128)b1 * h2; if (a2 <= 0) continue;
            ll g2 = gcdl((ll)(a2 % ((i128)1 << 62)), 0); (void)g2;
            for (ll h3 = h2 + 1; 2 * b2 > a2 * h3; h3++) {               /* 2/h3 > R2 */
                i128 a3 = a2 * h3 - b2, b3 = b2 * h3; if (a3 <= 0) continue;
                if (b3 % a3) continue; i128 h4 = b3 / a3; if (h4 <= h3) continue;
                w[0] = h1; w[1] = h2; w[2] = h3; w[3] = (ll)h4; return 1;
            }
        }
    }
    return 0;
}
static int tri3(ll n) {  /* 4/n = 1/x+1/y+1/z, all > n/2 (non-degenerate triangle) */
    for (ll x = n / 2 + 1; 3 * x <= 3 * n; x++) { ll a1 = 4 * x - n, b1 = n * x; if (a1 <= 0) continue;
        for (ll y = x; (i128)2 * b1 >= (i128)a1 * y; y++) { i128 a2 = (i128)a1 * y - b1, b2 = (i128)b1 * y; if (a2 <= 0) continue;
            if (b2 % a2 == 0 && b2 / a2 >= y && 2 * (b2 / a2) > n) return 1; } }
    return 0;
}
int main(int argc, char **argv) {
    ll NMAX = atoll(argv[1]); ll fail4 = 0, maxh1rel = 0; ll tri_fail_p1 = 0, tri_p1 = 0, tri_fail_other = 0;
    for (ll n = 3; n <= NMAX; n++) {
        ll w[4]; if (!distinct4(n, w)) { fail4++; printf("DISTINCT4-FAIL n=%lld\n", n); }
        int isp = 1; for (ll d = 2; d * d <= n; d++) if (n % d == 0) { isp = 0; break; }
        if (n <= 3000) { int t = tri3(n); if (isp && n % 4 == 1) { tri_p1++; if (!t) tri_fail_p1++; } else if (!t) tri_fail_other++; }
        if (n % 1000 == 0 || n == NMAX) { printf("n=%lld example %lld %lld %lld %lld\n", n, w[0], w[1], w[2], w[3]); fflush(stdout); }
    }
    printf("distinct realisable 4-term failures for 3<=n<=%lld: %lld\n", NMAX, fail4);
    printf("triangle (3-term, all > n/2), n <= 3000: primes p=1(4): %lld, failing %lld; other n failing: %lld\n", tri_p1, tri_fail_p1, tri_fail_other);
    return 0;
}
