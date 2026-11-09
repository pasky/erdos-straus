// z68_sign_contract.c — Contraction Lemma check + KT3 decomposition.
// For each prime p ≡ 1 (mod 8), p <= P: enumerate all A with r(p/A) = 4, word [[a,b,c,d]].
// Contraction (Z68_SIGN Lemma 2): position 2 (big letter b): X=a, X'=1, Y=K(c,d)=cd-1, Y'=d; if d | b and b >= 2d:
//   (t,u,v) = (b/d, cd-1, ad) is a length-3 word of p and chi(tu-1) = chi(A)*chi(d).
// position 3 (big letter c): X=K(a,b)=ab-1, X'=a, Y=d, Y'=1; if a | c and c >= 2a: (t,u,v) = (c/a, ad, ab-1),
//   chi(tu-1) = chi(A)*chi(a).
// Verifies both (numerator and sign) on every refinement; outputs per prime:
//   p L3 neg3 L4 neg4 R4 negR4 (refinements of length 4: words with a contraction) NR4 negNR4 (the rest)
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int jac(ll a, ll n) {
    int s = 1; a %= n; if (a < 0) a += n;
    while (a) { while ((a & 1) == 0) { a >>= 1; ll r = n & 7; if (r == 3 || r == 5) s = -s; }
        ll t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) s = -s; a %= n; }
    return n == 1 ? s : 0;
}
int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: P\n"); return 1; }
    ll P = atoll(argv[1]);
    if (P < 10 || P > 100000000) { fprintf(stderr, "10 <= P <= 1e8\n"); return 1; }
    
    char *c = calloc(P + 1, 1); if (!c) { fprintf(stderr, "calloc failed\n"); return 1; }
    for (ll i = 2; i * i <= P; i++) if (!c[i]) for (ll j = i * i; j <= P; j += i) c[j] = 1;
    long checked = 0;
    printf("# p L3 neg3 L4 neg4 R4 negR4 NR4 negNR4 U4 negU4 (U4: gcd-one subset gcd(b,d)=gcd(a,c)=1 -- NOT the exact no-move set, see z68_sign_moves.c)\n");
    for (ll p = 9; p <= P; p += 8) {
        if (c[p]) continue;
        long L3 = 0, n3 = 0, L4 = 0, n4 = 0, R4 = 0, nR4 = 0, U4 = 0, nU4 = 0;
        for (ll A = 1; A < p; A++) {
            ll N = p, D = A, w[6]; int r = 0;
            while (D > 0 && r <= 4) { ll b = (N + D - 1) / D; w[r++] = b; ll nd = b * D - N; N = D; D = nd; }
            if (D > 0) continue;          // length > 4 (loop exited with r = 5)
            if (r == 3) { L3++; if (jac(A, p) == -1) n3++; }
            if (r != 4) continue;
            int s = jac(A, p);
            L4++; if (s == -1) n4++;
            ll a = w[0], b = w[1], cc = w[2], d = w[3];
            int ref = 0;
            if (b % d == 0 && b >= 2 * d) {
                ll t = b / d, u = cc * d - 1, v = a * d;
                if (t * u * v - u - v != p || jac(t * u - 1, p) != s * jac(d, p)) { printf("FAIL1 %lld %lld\n", p, A); return 1; }
                ref = 1; checked++;
            }
            if (cc % a == 0 && cc >= 2 * a) {
                ll t = cc / a, u = a * d, v = a * b - 1;
                if (t * u * v - u - v != p || jac(t * u - 1, p) != s * jac(a, p)) { printf("FAIL2 %lld %lld\n", p, A); return 1; }
                ref = 1; checked++;
            }
            if (ref) { R4++; if (s == -1) nR4++; }
            { ll x = b, y = d; while (y) { ll t = x % y; x = y; y = t; }
              ll x2 = a, y2 = cc; while (y2) { ll t = x2 % y2; x2 = y2; y2 = t; }
              if (x == 1 && x2 == 1) { U4++; if (s == -1) nU4++; } }   // gcd-one subset (sufficient for "no interior out-move", not the exact no-move set)
        }
        printf("%lld %ld %ld %ld %ld %ld %ld %ld %ld %ld %ld\n", p, L3, n3, L4, n4, R4, nR4, L4 - R4, n4 - nR4, U4, nU4);
    }
    fprintf(stderr, "contractions verified: %ld\n", checked);
    return 0;
}
