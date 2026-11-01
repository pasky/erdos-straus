/* Z2794 part 2: the scribes' 2-part rule transported to 4/p:  4/p = 1/X + 1/(pX/d1) + 1/(pX/d2),  4X - p = d1 + d2, d1,d2 | X.
 * For primes p this is exactly the (★) line: d1 = u, d2 = B coprime, X = uBC (FRONTIER §2.1), so the rule's certificates are
 * the R(p)/2 unordered (★) triples.  For every prime p == 1 (4) <= PMAX we enumerate them (trial form over (u,C)) and compare
 * certificate selectors:  RH = Rhind/Abdulaziz "minimal a/x" = minimal X/min(d1,d2) (= minimal largest denominator);
 * GR = smallest X (closest to p/4, greedy-like); LV = smallest C; RD = "roundest" X (max number of divisors tau(X)).
 * usage: select PMAX
 */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int tau(ll x) { int t = 1; for (ll q = 2; q * q <= x; q++) { int e = 0; while (x % q == 0) { x /= q; e++; } t *= e + 1; } if (x > 1) t *= 2; return t; }
int main(int argc, char **argv) {
    ll PMAX = atoll(argv[1]); char *comp = calloc(PMAX + 1, 1);
    for (ll i = 2; i * i <= PMAX; i++) if (!comp[i]) for (ll j = i * i; j <= PMAX; j += i) comp[j] = 1;
    ll np = 0, zero = 0, rh_eq_gr = 0, rh_eq_lv = 0, rh_eq_rd = 0, gr_eq_lv = 0, rh_even = 0, rh_tau_best = 0;
    double sum_rank = 0; ll zlist[40]; int nz = 0;
    for (ll p = 5; p <= PMAX; p += 4) {
        if (comp[p]) continue; np++;
        ll bestRH[4] = {0}, bestGR[4] = {0}, bestLV[4] = {0}, bestRD[4] = {0}; double vRH = 1e300; ll vGR = 1LL << 62, vLV = 1LL << 62; int vRD = -1; int cnt = 0;
        int taus[100000]; int nt = 0;
        for (ll u = 1; 4 * u - 1 <= p + u; u++) for (ll C = 1; 4 * u * C - 1 <= p + u; C++) {
            ll m = 4 * u * C - 1; if ((p + u) % m) continue; ll B = (p + u) / m; if (B < u) continue;  /* unordered: u <= B */
            ll X = u * B * C; cnt++;
            double rh = (double)X / (u < B ? u : B); int t = tau(X); if (nt < 100000) taus[nt++] = t;
            if (rh < vRH) { vRH = rh; bestRH[0] = u; bestRH[1] = B; bestRH[2] = C; bestRH[3] = t; }
            if (X < vGR) { vGR = X; bestGR[0] = u; bestGR[1] = B; bestGR[2] = C; }
            if (C < vLV || (C == vLV && X < (ll)bestLV[0] * bestLV[1] * bestLV[2])) { vLV = C; bestLV[0] = u; bestLV[1] = B; bestLV[2] = C; }
            if (t > vRD) { vRD = t; bestRD[0] = u; bestRD[1] = B; bestRD[2] = C; }
        }
        if (!cnt) { zero++; if (nz < 40) zlist[nz++] = p; continue; }
        #define EQ(a, b) (a[0] == b[0] && a[1] == b[1] && a[2] == b[2])
        rh_eq_gr += EQ(bestRH, bestGR); rh_eq_lv += EQ(bestRH, bestLV); rh_eq_rd += EQ(bestRH, bestRD); gr_eq_lv += EQ(bestGR, bestLV);
        rh_even += ((bestRH[0] * bestRH[1] * bestRH[2]) % 2 == 0); rh_tau_best += (bestRH[3] == vRD);
        int above = 0; for (int i = 0; i < nt; i++) if (taus[i] > bestRH[3]) above++; sum_rank += (double)above / nt;
    }
    ll nn = np - zero;
    printf("primes p=1(4) <= %lld: %lld; no 2-part scribes' certificate (R(p)=0): %lld:", PMAX, np, zero);
    for (int i = 0; i < nz; i++) printf(" %lld", zlist[i]); printf("\n");
    printf("RH (min a/x) == GR (min X): %.4f; RH == LV (min C): %.4f; RH == RD (max tau(X)): %.4f; GR == LV: %.4f\n",
           (double)rh_eq_gr / nn, (double)rh_eq_lv / nn, (double)rh_eq_rd / nn, (double)gr_eq_lv / nn);
    printf("RH-selected X even: %.4f; RH-selected X has maximal tau among certificates: %.4f; mean fraction of certificates with larger tau: %.4f\n",
           (double)rh_even / nn, (double)rh_tau_best / nn, sum_rank / nn);
    return 0;
}
