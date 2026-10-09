/* R100: independent complete enumeration of the new part of POINTWISE_MORDELL13C Comp. 3.1.
 * T-generic II3/I1/I3 data with a_T = 11^2 13^2, d_T = e_T = 1  <->  (a',d',m,j), a',d' prime to 143,
 *   4 a' d' m j = L a' + m + j,  L = 11^4 13^4,     e = 4a'd'm - 1,   subcell u = -e mod 11^2 13^2.
 * Enumerate unordered {s<=t} = {m,j}: a' = (s+t)/(4d'st - L), need 4d'st > L and
 * (4d's-1)(4d't-1) <= 4d'L+1  (equivalent to a' >= 1).
 * Output: every datum (a',d',m,j,u mod 121, u mod 169) with u = 2 mod 11 and 2 mod 13; summary counts.
 */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef __int128 i128;
int main(int argc, char **argv) {
    const ll L = argc > 1 ? atoll(argv[1]) : 418161601LL, F = 20449; /* argv[1]: test lambda */
    ll ndata = 0, ncell = 0;
    static int hit[121][169];
    for (ll d = 1; 4 * d - 1 <= 4 * d * 0 + (ll)1e18; d++) {
        i128 B = (i128)4 * d * L + 1;
        if ((i128)(4 * d - 1) * (4 * d - 1) > B) break;
        for (ll s = 1; (i128)(4 * d * s - 1) * (4 * d * s - 1) <= B; s++) {
            ll t0 = L / (4 * d * s) + 1; if (t0 < s) t0 = s;
            for (ll t = t0; (i128)(4 * d * s - 1) * (4 * d * t - 1) <= B; t++) {
                i128 den = (i128)4 * d * s * t - L;
                if (den <= 0) continue;
                if ((s + t) % den) continue;
                ll a = (ll)((s + t) / den);
                if (d % 11 == 0 || d % 13 == 0 || a % 11 == 0 || a % 13 == 0) continue;
                for (int k = 0; k < 2; k++) {
                    ll m = k ? t : s, j = k ? s : t;
                    if (k && s == t) break;
                    i128 e = (i128)4 * a * d * m - 1;
                    /* sanity: identity and divisibility e | 4 a^2 d + 1 with a = F*a' */
                    i128 lhs = (i128)4 * a * d * m * j, rhs = (i128)L * a + m + j;
                    if (lhs != rhs) { printf("IDENTITY FAIL\n"); return 1; }
                    i128 big = (i128)4 * L * a * a * d + 1;
                    if (big % e) { printf("DIV FAIL\n"); return 1; }
                    ndata++;
                    ll u = (ll)(((-e) % F + F) % F);
                    if (argc > 1) printf("T %lld %lld %lld\n", a, d, (ll)e);
                    if (u % 11 == 2 && u % 13 == 2) {
                        ncell++; hit[u % 121][u % 169]++;
                        printf("DATUM a'=%lld d'=%lld m=%lld j=%lld e=%lld u=%lld u11=%lld u13=%lld\n",
                               a, d, m, j, (ll)e, u, u % 121, u % 169);
                    }
                }
            }
        }
    }
    printf("data %lld, in (2,2) cell %lld\n", ndata, ncell);
    return 0;
}
