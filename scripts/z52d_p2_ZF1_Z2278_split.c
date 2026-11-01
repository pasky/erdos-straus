/* Z2278: unit-fraction splitting identities that keep p in the denominators, applied to the constrained witness
 * 4/n = 1/X + e/(nX), X = (n+e)/4 (greedy-type first term; e ≡ -n mod 4):
 *   e/(nX) = 1/y + 1/z,  y = nX(a+b)/(e a), z = nX(a+b)/(e b),  a, b | nX,  e | a+b    (the splitting identity).
 * (A) polynomial splittings (odd e only: e ≡ -n mod 4 with n odd): a, b of fixed "type" t in {0: a0, 1: n*a0, 2: X/a0, 3: nX/a0} (a0 constant) are identities in n
 *     on residue classes mod W = 4*e*lcm(a0,b0)*... ; for every family with e <= EMAX, a0,b0 <= AMAX we list its valid unit
 *     classes r mod W and test whether r is a square mod W (Schinzel: never; Mordell: square classes mod 840 stay open).
 * (B) per-prime splittings (a, b genuine divisors of X, i.e. both new denominators divisible by p): for every prime
 *     p ≡ 1,121,169,289,361,529 (mod 840) up to PMAX, the least e for which the split exists; histogram and maximum.
 * usage: split EMAX AMAX PMAX
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static ll gcdl(ll a, ll b) { while (b) { ll t = a % b; a = b; b = t; } return a < 0 ? -a : a; }
static int valid(ll n, ll e, int ta, ll a0, int tb, ll b0) {
    if ((n + e) % 4) return 0; ll X = (n + e) / 4; ll nX = n * X;
    ll a, b;
    switch (ta) { case 0: a = a0; break; case 1: a = n * a0; break; case 2: if (X % a0) return 0; a = X / a0; break; default: if (nX % a0) return 0; a = nX / a0; }
    switch (tb) { case 0: b = b0; break; case 1: b = n * b0; break; case 2: if (X % b0) return 0; b = X / b0; break; default: if (nX % b0) return 0; b = nX / b0; }
    if (nX % a || nX % b) return 0;
    if ((a % e + b % e) % e) return 0;
    return 1;
}
int main(int argc, char **argv) {
    int EMAX = atoi(argv[1]), AMAX = atoi(argv[2]); ll PMAX = atoll(argv[3]);
    /* (A) */
    long fam = 0, famvalid = 0, classes = 0, sqviol = 0, mism = 0; static char issq[2000000];
    static int sq840cov[840];
    for (int e = 1; e <= EMAX; e += 2) for (int ta = 0; ta < 4; ta++) for (int tb = ta; tb < 4; tb++)
    for (ll a0 = 1; a0 <= AMAX; a0++) for (ll b0 = (ta == tb ? a0 : 1); b0 <= AMAX; b0++) {
        fam++;
        ll L = a0 / gcdl(a0, b0) * b0; ll W = 4LL * e * L * e; if (W > 1900000) continue;   /* W: safe period (X mod a0*e) */
        memset(issq, 0, W); for (ll x = 0; x < W; x++) issq[(x * x) % W] = 1;
        int any = 0;
        for (ll r = 1; r < W; r++) { if (gcdl(r, W) != 1) continue;
            ll n1 = r + W * 3, n2 = r + W * 7;   /* keep nX < 2^63 */
            int v1 = valid(n1, e, ta, a0, tb, b0), v2 = valid(n2, e, ta, a0, tb, b0);
            if (v1 != v2) { mism++; continue; }
            if (!v1) continue;
            any = 1; classes++; if (issq[r]) { sqviol++; printf("SQUARE-CLASS e=%d ta=%d a0=%lld tb=%d b0=%lld r=%lld W=%lld\n", e, ta, a0, tb, b0, r, W); }
            if (W % 840 == 0) sq840cov[r % 840] = 1; }
        famvalid += any;
    }
    int sqc[6] = {1, 121, 169, 289, 361, 529}, cov = 0; for (int i = 0; i < 6; i++) cov += sq840cov[sqc[i]];
    printf("(A) families=%ld with_valid_class=%ld valid_unit_classes=%ld classes_that_are_squares_mod_W=%ld square_classes_mod_840_touched=%d period_mismatches=%ld\n", fam, famvalid, classes, sqviol, cov, mism);
    /* (B) */
    ll M = PMAX / 4 + 1000; int *spf = calloc(M + 1, sizeof(int));
    for (ll i = 2; i <= M; i++) if (!spf[i]) for (ll j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    char *comp = calloc(PMAX + 1, 1); for (ll i = 2; i * i <= PMAX; i++) if (!comp[i]) for (ll j = i * i; j <= PMAX; j += i) comp[j] = 1;
    long hist[4000] = {0}; ll np = 0, emaxall = 0, pworst = 0, unres = 0;
    for (ll p = 2; p <= PMAX; p++) {
        if (comp[p]) continue; int c = p % 840; if (!(c == 1 || c == 121 || c == 169 || c == 289 || c == 361 || c == 529)) continue;
        np++; ll found = 0;
        for (ll e = 3; e < 4000 && !found; e += 4) {
            ll X = (p + e) / 4; if (X > M) break;
            /* divisors of X */
            ll pr[32]; int ex[32], k = 0; ll x = X; while (x > 1) { int q = spf[x]; int t = 0; while (x % q == 0) { x /= q; t++; } pr[k] = q; ex[k] = t; k++; }
            static ll dv[100000]; int nd = 1; dv[0] = 1;
            for (int i = 0; i < k; i++) { int cur = nd; ll pw = 1; for (int t = 1; t <= ex[i]; t++) { pw *= pr[i]; for (int j = 0; j < cur; j++) dv[nd++] = dv[j] * pw; } }
            static char res[4000]; memset(res, 0, e); for (int j = 0; j < nd; j++) res[dv[j] % e] = 1;
            for (ll r0 = 0; r0 < e && !found; r0++) if (res[r0] && res[(e - r0) % e]) found = e;
        }
        if (!found) { unres++; continue; }
        hist[found]++; if (found > emaxall) { emaxall = found; pworst = p; }
    }
    printf("(B) square-class primes <= %lld: %lld; unresolved with e < 4000: %lld; max least-e = %lld (p = %lld); least-e histogram:", PMAX, np, unres, emaxall, pworst);
    for (int e = 3; e < 4000; e += 4) if (hist[e]) printf(" %d:%ld", e, hist[e]); printf("\n");
    return 0;
}
