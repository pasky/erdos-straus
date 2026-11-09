// z68_sign_moves.c — KT3 re-analysis after internal review (finding F1): exact single-step rescaling-move predicates.
// For each prime p ≡ 1 (mod 8), 1e4 < p <= P, and every word [[b1..b4]] of length 4, test at every cut j = 0..3
// (big letter b = b_{j+1}, data X, X', Y, Y' of Lemma 1, endpoint conventions 1/0) whether a rescaling move of
// Lemma 2 exists with some k >= 2 (it suffices to test primes k):
//   right-out: k | b, k | Y' (Y' = 0 allowed), b/k >= 2, gcd(k, X') = 1, X' >= 1;
//   left-out : k | b, k | X' (X' = 0 allowed), b/k >= 2, gcd(k, Y') = 1, Y' >= 1;
//   right-in : k | X, X/k > X' >= 1, k*Y' < Y or (Y' = 0), gcd(k, Y) = 1      (w is the image of a right-out move);
//   left-in  : k | Y, Y/k > Y' >= 1, k*X' < X or (X' = 0), gcd(k, X) = 1.
// Classes: NOOUT = no out-move at any cut (corrected version of the reviewer's "no permitted move" set, now
// including endpoint cuts); ISOL = no move in or out at any cut.  Output per prime:
//   p L3 neg3 L4 neg4 NOOUT negNOOUT ISOL negISOL
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int jac(ll a, ll n) { int s = 1; a %= n; if (a < 0) a += n;
    while (a) { while ((a & 1) == 0) { a >>= 1; ll r = n & 7; if (r == 3 || r == 5) s = -s; }
        ll t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) s = -s; a %= n; } return n == 1 ? s : 0; }
static ll gcd(ll a, ll b) { while (b) { ll t = a % b; a = b; b = t; } return a; }
static int nprimes(ll m, ll *q) { int c = 0; for (ll d = 2; d * d <= m; d++) if (m % d == 0) { q[c++] = d; while (m % d == 0) m /= d; } if (m > 1) q[c++] = m; return c; }
static ll K(ll *w, int i, int j) { ll a = 1, b = 0; for (int t = i; t <= j; t++) { ll c = w[t] * a - b; b = a; a = c; } return a; } // K(w_i..w_j), empty = 1
static ll Km(ll *w, int i, int j) { if (j < i - 1) return 0; return K(w, i, j); }   // length -1 -> 0
static int any_move(ll *w, int r, int want_in) {
    ll q[64];
    for (int j = 0; j < r; j++) {
        ll b = w[j];
        ll X = K(w, 0, j - 1), Xp = (j >= 1) ? Km(w, 0, j - 2) : 0;
        ll Y = K(w, j + 1, r - 1), Yp = (j <= r - 2) ? Km(w, j + 2, r - 1) : 0;
        if (j == 0) { X = 1; Xp = 0; }
        if (j == r - 1) { Y = 1; Yp = 0; }
        int c = nprimes(b, q);
        for (int i = 0; i < c; i++) { ll k = q[i]; if (b / k < 2) continue;
            if (Xp >= 1 && Yp % k == 0 && gcd(k, Xp) == 1) return 1;          // right-out
            if (Yp >= 1 && Xp % k == 0 && gcd(k, Yp) == 1) return 1; }        // left-out
        if (!want_in) continue;
        if (Xp >= 1) { c = nprimes(X, q); for (int i = 0; i < c; i++) { ll k = q[i];
            if (X / k > Xp && (Yp == 0 || k * Yp < Y) && gcd(k, Y) == 1) return 1; } }     // right-in
        if (Yp >= 1) { c = nprimes(Y, q); for (int i = 0; i < c; i++) { ll k = q[i];
            if (Y / k > Yp && (Xp == 0 || k * Xp < X) && gcd(k, X) == 1) return 1; } }     // left-in
    }
    return 0;
}
int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: P\n"); return 1; }
    ll P = atoll(argv[1]); if (P < 10 || P > 100000000) return 1;
    char *cp = calloc(P + 1, 1); if (!cp) { fprintf(stderr, "calloc failed\n"); return 1; }
    for (ll i = 2; i * i <= P; i++) if (!cp[i]) for (ll j = i * i; j <= P; j += i) cp[j] = 1;
    printf("# p L3 neg3 L4 neg4 NOOUT negNOOUT ISOL negISOL\n");
    for (ll p = 10009; p <= P; p += 8) {
        if (p % 8 != 1 || cp[p]) continue;
        long L3 = 0, n3 = 0, L4 = 0, n4 = 0, no = 0, nno = 0, is = 0, nis = 0;
        for (ll A = 1; A < p; A++) {
            ll N = p, D = A, w[6]; int r = 0;
            while (D > 0 && r <= 4) { ll b = (N + D - 1) / D; w[r++] = b; ll nd = b * D - N; N = D; D = nd; }
            if (D > 0) continue;
            if (r == 3) { L3++; if (jac(A, p) == -1) n3++; }
            if (r != 4) continue;
            int s = jac(A, p); L4++; if (s == -1) n4++;
            if (K(w, 0, 3) != p) { printf("BUG\n"); return 1; }
            if (!any_move(w, 4, 0)) { no++; if (s == -1) nno++; }
            if (!any_move(w, 4, 1)) { is++; if (s == -1) nis++; }
        }
        printf("%lld %ld %ld %ld %ld %ld %ld %ld %ld\n", p, L3, n3, L4, n4, no, nno, is, nis);
    }
    return 0;
}
