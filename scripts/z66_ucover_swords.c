/* z66 UCOVER: (S)-families (Z64_SDEEPF good length-3 words) containing the profile e_g (1 at p != ell, g at ell).
 *
 * Word families (exactly one of t, u, v grows with n; SDEEPF Thm 3.6 uses these):
 *   W1 (t, u fixed, A = tu - 1):  class n = -u (mod A), good iff (A/n) = -1.  At e_g: A = ell^k A', A' | u + 1,
 *      good iff (g/ell)^k = -1;  caught rho = -u mod ell^k.
 *      Event equation: u + 1 = A' s, A'(ts - N) = t + 1  (N = ell^k);  X := ts - N >= 1, t + 1 = X A'.
 *   W2 (u, v fixed, t = (n+u+v)/(uv)):  class n = -(u+v) (mod uv), good iff 8 | (n+t)(n+u+v).
 *      At e_g: u = ell^k1 u', v = ell^k2 v', u'v' | u + v + 1, rho = -(u+v) mod ell^k; goodness depends only on
 *      the 2-adic component (= 1):  t = w^{-1} (1+u+v)/2^a (mod 8), uv = 2^a w.
 *      Event equation: M1 u' + M2 v' + 1 = u'v's, i.e. (u's - M2)(v's - M1) = N + s, M1 = ell^k1, M2 = ell^k2.
 * Enumeration in O(sqrt(N) log N) per (k, split) by divisor-in-residue-class scanning (see Z66_UCOVER.md §6);
 * the number of candidates scanned is printed and is an explicit upper bound for the number of events.
 * Output lines: "W1 rho t u A'"  /  "W2 rho u v good(0/1)".  Usage: z66_ucover_swords ELL K
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef __int128 i128;
typedef long long ll;

static ll ipow(ll b, int e) { ll r = 1; while (e-- > 0) r *= b; return r; }
static ll isqrt_ll(ll x) { ll r = (ll)sqrtl((long double)x); while (r * r > x) r--; while ((r + 1) * (r + 1) <= x) r++; return r; }
static void pr128(i128 x) {   /* print a signed 128-bit integer in decimal */
    char b[64]; int i = 63; b[i] = 0; int neg = x < 0; if (neg) x = -x;
    do { b[--i] = (char)('0' + (int)(x % 10)); x /= 10; } while (x);
    if (neg) b[--i] = '-';
    fputs(b + i, stdout);
}
static ll md(i128 x, ll m) { ll r = (ll)(x % m); return r < 0 ? r + m : r; }

static ll ELL; static int K; static ll N;
static long long cand = 0;

static void w1_try(ll X, ll t, ll s) {
    /* t s = N + X, X | t + 1 */
    if (t < 2 || s < 1) return;
    if ((i128)t * s != (i128)N + X) return;
    if ((t + 1) % X) return;
    ll Ap = (t + 1) / X;
    if (Ap % ELL == 0) return;
    i128 u = (i128)Ap * s - 1;
    if (u < 2) return;
    /* sanity: t u - 1 = N A' */
    if ((i128)t * u - 1 != (i128)N * Ap) { fprintf(stderr, "W1 sanity\n"); exit(2); }
    ll rho = md(-u, N);
    printf("W1 %lld %lld ", rho, t); pr128(u); printf(" %lld\n", Ap);
}

static void enum_w1(void) {
    ll X0 = isqrt_ll(2 * N) + 2;
    for (ll X = 1; X <= X0; X++) {
        ll R = isqrt_ll(N + X) + 1;
        /* t = -1 mod X, t <= R */
        for (ll t = X - 1; t <= R; t += X) { cand++; if (t >= 1 && (N + X) % t == 0) w1_try(X, t, (N + X) / t); }
        /* s = -N mod X, s <= R, t = (N+X)/s */
        ll s0 = md(-(i128)N, X); if (s0 == 0) s0 = X;
        for (ll s = s0; s <= R; s += X) { cand++; if ((N + X) % s == 0) w1_try(X, (N + X) / s, s); }
    }
    /* large X > X0: s <= S, X = (N + s)/z with z <= Z, s = -N mod z */
    ll S = isqrt_ll(N / 2) + 3, Z = S;
    for (ll z = 1; z <= Z; z++) {
        ll s0 = md(-(i128)N, z); if (s0 == 0) s0 = z;
        for (ll s = s0; s <= S; s += z) {
            cand++;
            ll X = (N + s) / z;
            if (X <= X0) continue;
            if ((N + X) % s) continue;
            w1_try(X, (N + X) / s, s);
        }
    }
}

static int v2(i128 x) { int a = 0; while (x % 2 == 0) { x /= 2; a++; } return a; }

static void w2_try(ll M1, ll M2, ll s, ll X, ll Y) {
    /* X = u's - M2, Y = v's - M1, X Y = N + s */
    if (X < 1 || Y < 1) return;
    if ((i128)X * Y != (i128)N + s) return;
    if ((X + M2) % s || (Y + M1) % s) return;
    ll up = (X + M2) / s, vp = (Y + M1) / s;
    if (up % ELL == 0 || vp % ELL == 0) return;
    i128 u = (i128)M1 * up, v = (i128)M2 * vp;
    if (u < 2 || v < 2) return;
    i128 S1 = u + v + 1;
    if (S1 % ((i128)up * vp)) { fprintf(stderr, "W2 sanity\n"); exit(3); }
    /* goodness from the 2-adic component 1 */
    i128 uv = u * v; int a = v2(uv); i128 w = uv >> a;
    i128 q = S1 >> a; /* (1+u+v)/2^a, integral since 2^a | u'v' | 1+u+v */
    if ((q << a) != S1) { fprintf(stderr, "W2 2-adic\n"); exit(4); }
    int wi = 0; for (int x = 1; x < 8; x += 2) if (((w % 8) * x) % 8 == 1) wi = x;
    int t8 = (int)(((q % 8) * wi) % 8);
    int vA = 0, vB = 0; int A8 = (1 + t8) % 8; int B8 = (int)(S1 % 8);
    if (A8 == 0) vA = 3; else { while (A8 % 2 == 0) { A8 /= 2; vA++; } }
    if (B8 == 0) vB = 3; else { while (B8 % 2 == 0) { B8 /= 2; vB++; } }
    int good = (vA + vB >= 3);
    ll rho = md(-(u + v), N);
    printf("W2 %lld ", rho); pr128(u); printf(" "); pr128(v); printf(" %d\n", good);
}

static void enum_w2(void) {
    ll s0 = isqrt_ll(2 * N) + 2;
    for (int k1 = 0; k1 <= K; k1++) {
        ll M1 = ipow(ELL, k1), M2 = ipow(ELL, K - k1);
        for (ll s = 1; s <= s0; s++) {
            ll R = isqrt_ll(N + s) + 1;
            ll r2 = md(-(i128)M2, s); if (r2 == 0) r2 = s;
            for (ll X = r2; X <= R; X += s) { cand++; if ((N + s) % X == 0) w2_try(M1, M2, s, X, (N + s) / X); }
            ll r1 = md(-(i128)M1, s); if (r1 == 0) r1 = s;
            for (ll Y = r1; Y <= R; Y += s) { cand++; if ((N + s) % Y == 0) w2_try(M1, M2, s, (N + s) / Y, Y); }
        }
        /* large s > s0: the smaller factor r < s equals its residue; s | M + r with M in {M2 (r = X), M1 (r = Y)} */
        ll Rr = isqrt_ll(2 * N) + 4, Z = isqrt_ll(N / 2) + 4;
        for (int side = 0; side < 2; side++) {
            ll Mside = side == 0 ? M2 : M1;
            for (ll z = 1; z <= Z; z++) {
                ll r0 = md(-(i128)Mside, z); if (r0 == 0) r0 = z;
                for (ll r = r0; r <= Rr; r += z) {
                    cand++;
                    i128 ss = ((i128)Mside + r) / z;
                    if (ss <= s0 || ss >= ((i128)1 << 62)) continue;
                    ll s = (ll)ss;
                    if ((N + s) % r) continue;
                    ll other = (N + s) / r;
                    if (side == 0) w2_try(M1, M2, s, r, other); else w2_try(M1, M2, s, other, r);
                }
            }
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s ELL K\n", argv[0]); return 1; }
    ELL = atoll(argv[1]); K = atoi(argv[2]); N = ipow(ELL, K);
    enum_w1();
    enum_w2();
    fprintf(stderr, "# ell=%lld k=%d N=%lld candidates_scanned=%lld\n", ELL, K, N, cand);
    return 0;
}
