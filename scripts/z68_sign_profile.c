// z68_sign_profile.c — level-1 catching of non-residue profiles e_{l,g} by HJ word families of length R.
//
// A word family of length R with "big letter" at one position is a pair of HJ fractions (X/X', Y/Y') with
// HJ lengths a + c = R - 1 (a = 0 means X/X' = 1/0); its class is n ≡ -(X'Y + XY') (mod XY) and its words are
// n/A = [[..left.., b, ..right..]], b = (n + X'Y + XY')/(XY) (Z68_SIGN Lemma 1). At the profile e_{l,g}
// (g at l, 1 at every other prime incl. 2) the family applies iff, with l^k || XY, M = XY/l^k:
//   s := X'Y + XY' ≡ -1 (mod M)  and  g ≡ -s (mod l^k);  it is GOOD (chi = -1) iff k odd and g non-residue.
// We use level k = 1 only (catches the whole class g mod l).  By reversal symmetry only shapes a <= c are scanned.
// Output: for each prime l in [lmin,lmax] and each length R' in {2..R}, the set of non-residue classes caught.
// Usage: ./z68_sign_profile lmin lmax R B     (all families with XY <= B)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
typedef unsigned long long ull;

static int hjlen_le(ll N, ll D, int cap) { // HJ length of N/D (N > D >= 1, coprime), returns cap+1 if > cap
    int r = 0;
    while (D > 0) {
        r++;
        if (r > cap) return cap + 1;
        ll b = (N + D - 1) / D;
        ll nd = b * D - N;
        N = D; D = nd;
    }
    return r;
}
static ll gcdll(ll a, ll b) { while (b) { ll t = a % b; a = b; b = t; } return a < 0 ? -a : a; }
static int isprime(ll n) { if (n < 2) return 0; for (ll d = 2; d * d <= n; d++) if (n % d == 0) return 0; return 1; }

static int L;            // the prime l
static char *qr;         // qr[g] = 1 if g is a nonzero square mod l
static unsigned char caught[8][4096]; // caught[R'][g]
static ll witness[8][4096][4];
static ll nevents[8], maxXY[8];          // good level-1 events (with multiplicity) and their largest modulus XY

static void record(int Rp, ll X, ll Xp, ll Y, ll Yp) {
    // check level-1 condition
    ll XY = X * Y;
    if (XY % L) return;
    ll M = XY / L;
    if (M % L == 0) return;                 // need l || XY
    ll s = Xp * Y + X * Yp;
    if ((s + 1) % M != 0) return;           // s ≡ -1 mod M
    ll g = ((-s) % L + L) % L;
    if (g == 0 || qr[g]) return;            // must be a non-residue unit
    nevents[Rp]++;
    if (XY > maxXY[Rp]) maxXY[Rp] = XY;
    if (!caught[Rp][g]) {
        caught[Rp][g] = 1;
        witness[Rp][g][0] = X; witness[Rp][g][1] = Xp; witness[Rp][g][2] = Y; witness[Rp][g][3] = Yp;
    }
}

// enumerate HJ fractions N/D of HJ length exactly c with N <= Nmax, call f for each.
// Length 0: (1,0). Length 1: (N,1), N>=2. Length >=2: N/D = [[b, rest]] with D/D2 of length c-1, N = b*D - D2.
typedef void (*fracfn)(ll N, ll D, void *ctx);
static void enum_len(int c, ll Nmax, fracfn f, void *ctx);
struct rec_ctx { int c; ll Nmax; fracfn f; void *ctx; };
static void enum_up(ll D, ll D2, void *vctx) { // given D/D2 of length c-1, extend by first letter b >= 2
    struct rec_ctx *rc = (struct rec_ctx *)vctx;
    for (ll b = 2;; b++) {
        ll N = b * D - D2;
        if (N > rc->Nmax) break;
        rc->f(N, D, rc->ctx);
    }
}
static void enum_len(int c, ll Nmax, fracfn f, void *ctx) {
    if (c == 0) { f(1, 0, ctx); return; }
    if (c == 1) { for (ll N = 2; N <= Nmax; N++) f(N, 1, ctx); return; }
    struct rec_ctx rc = { c, Nmax, f, ctx };
    // D/D2 of length c-1 with D <= Nmax/2 + 1 (since N >= 2D - D2 > D)
    enum_len(c - 1, Nmax, enum_up, &rc);
}

// shape (a, c): for each X/X' of length a, enumerate Y/Y' of length c with XY <= B.
struct pair_ctx { int Rp; ll X, Xp; };
static void inner_Y(ll Y, ll Yp, void *vctx) {
    struct pair_ctx *pc = (struct pair_ctx *)vctx;
    record(pc->Rp, pc->X, pc->Xp, Y, Yp);
}
static ll gB; static int gc; static int gRp;
static void outer_X(ll X, ll Xp, void *vctx) {
    (void)vctx;
    struct pair_ctx pc = { gRp, X, Xp };
    ll Ymax = gB / X;
    if (Ymax < 1) return;
    enum_len(gc, Ymax, inner_Y, &pc);
}

// fast path for shape (0, c): Y = L*m, Y' = j*m - 1 (forced by Y' ≡ -1 mod m, 1 <= Y' < Y), check HJ length == c
static void shape0(int c, ll B, int Rp) {
    for (ll m = 1; L * m <= B; m++) {
        if (m % L == 0) continue;
        ll Y = (ll)L * m;
        for (ll j = 1; j <= L; j++) {
            ll Yp = j * m - 1;
            if (Yp < 1 || Yp >= Y) continue;
            if (c == 1 && Yp != 1) continue;
            if (gcdll(Y, Yp) != 1) continue;
            if (hjlen_le(Y, Yp, c) != c) continue;
            record(Rp, 1, 0, Y, Yp);
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: lmin lmax R B\n"); return 1; }
    int lmin = atoi(argv[1]), lmax = atoi(argv[2]), R = atoi(argv[3]);
    ll B = atoll(argv[4]);
    if (R > 7 || lmax >= 4096) { fprintf(stderr, "R<=7, l<4096\n"); return 1; }
    printf("# z68_sign_profile lmin=%d lmax=%d R=%d B=%lld ; level-1 catching of non-residue profiles e_{l,g}\n", lmin, lmax, R, B);
    printf("# cols: l Rlen #nonres #caught_exact_len #caught_len<=Rlen ev=#good_events(shapes a<=c) maxXY uncaught_list(len<=Rlen) exact_uncaught\n");
    for (L = lmin; L <= lmax; L++) {
        if (!isprime(L) || L < 3) continue;
        qr = calloc(L, 1);
        for (ll x = 1; x < L; x++) qr[(x * x) % L] = 1;
        memset(caught, 0, sizeof caught); memset(nevents, 0, sizeof nevents); memset(maxXY, 0, sizeof maxXY);
        for (int Rp = 2; Rp <= R; Rp++) {
            int tot = Rp - 1;
            shape0(tot, B, Rp);                 // shape (0, tot)
            for (int a = 1; a <= tot - a; a++) { // shapes (a, tot - a), a >= 1
                gB = B; gc = tot - a; gRp = Rp;
                enum_len(a, B / 2, outer_X, NULL);
            }
        }
        int nonres = 0; for (int g = 1; g < L; g++) if (!qr[g]) nonres++;
        unsigned char cum[4096]; memset(cum, 0, sizeof cum);
        for (int Rp = 2; Rp <= R; Rp++) {
            int ce = 0, cc = 0;
            for (int g = 1; g < L; g++) if (!qr[g]) { if (caught[Rp][g]) { ce++; cum[g] = 1; } if (cum[g]) cc++; }
            printf("%d %d %d %d %d ev=%lld maxXY=%lld", L, Rp, nonres, ce, cc, nevents[Rp], maxXY[Rp]);
            printf(" [");
            int first = 1;
            for (int g = 1; g < L; g++) if (!qr[g] && !cum[g]) { printf(first ? "%d" : ",%d", g); first = 0; }
            printf("] exact_uncaught=[");
            first = 1;
            for (int g = 1; g < L; g++) if (!qr[g] && !caught[Rp][g]) { printf(first ? "%d" : ",%d", g); first = 0; }
            printf("]\n");
        }
        // witnesses for exact length R
        for (int g = 1; g < L; g++) if (!qr[g] && caught[R][g])
            printf("W %d %d g=%d X/X'=%lld/%lld Y/Y'=%lld/%lld\n", L, R, g, witness[R][g][0], witness[R][g][1], witness[R][g][2], witness[R][g][3]);
        free(qr);
        fflush(stdout);
    }
    return 0;
}
