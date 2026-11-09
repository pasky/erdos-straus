// z68_sign_graph.c — §10 of Z68_SIGN: the rescaling-move graph on ALL words of an odd n.
// Vertices: A in [1, n-1], gcd(A, n) = 1 (word = HJ expansion of n/A, any length).  Edges: Lemma-2 moves at every
// cut j (incl. endpoints) with every k >= 2:
//   right move: k | b, k | Y' (Y' = 0 allowed), b/k >= 2, gcd(k, X') = 1, X' >= 1      -> A' = A * k^{-1} (mod n)
//   left  move: k | b, k | X' (X' = 0 allowed), b/k >= 2, gcd(k, Y') = 1, Y' >= 1      -> A' = A * k      (mod n)
// (inverse moves are the same edges read backwards; the graph is stored undirected).  Edge label: chi_n(k).
// Every move is verified by rebuilding the target word from the move data and checking that it is the HJ word of
// n/A' (when VERIFY=1, default on).
// Reports for n:  components of (V,E) and of (V,E+) (E+ = edges with chi(k) = +1); for good (chi = -1) vertices of
// length >= 4: fraction whose E-component / E+-component contains a good L3 vertex; fraction from which a strictly
// length-decreasing path (E, resp. E+) reaches a good L3 vertex (sets D, D+); and two deterministic descent rules from
// registered starts:  Rmin  : go to the neighbour of least length (ties: least A) while it is shorter;
//                     Rmin+ : the same through E+ edges only.
// Starts: S1 = A = least prime q with chi_n(q) = -1 (as a denominator), S2 = the shortest good word of length >= 4
// (least A among those), S3 = every good word whose HJ letters are all <= 4 and length >= 6 (bounded-digit; success
// fraction reported).  Success = descent ends at a GOOD vertex of length 3.
// Usage: ./z68_sign_graph n1 n2 ...   (implemented domain: n ≡ 1 (mod 4), 9 <= n <= 2e7; E counts generating move
// instances (multi-edges), not distinct vertex pairs; for odd squares S1 is the sentinel A = 1 and S2 is absent (-1))
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static ll N;
static int jac(ll a, ll n) { int s = 1; a %= n; if (a < 0) a += n;
    while (a) { while ((a & 1) == 0) { a >>= 1; ll r = n & 7; if (r == 3 || r == 5) s = -s; }
        ll t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) s = -s; a %= n; } return n == 1 ? s : 0; }
static ll gcdl(ll a, ll b) { while (b) { ll t = a % b; a = b; b = t; } return a < 0 ? -a : a; }
static ll inv(ll a, ll m) { ll g = m, x = 0, x1 = 1, a1 = a % m; if (a1 < 0) a1 += m; ll b = a1;
    while (b) { ll q = g / b, t = g - q * b; g = b; b = t; t = x - q * x1; x = x1; x1 = t; } return (x % m + m) % m; }
static int hjword(ll n, ll a, ll *w) { int r = 0; while (a > 0) { ll b = (n + a - 1) / a; w[r++] = b; ll nd = b * a - n; n = a; a = nd; } return r; }
static ll *W, *Pc, *Sc;      // word buffer, prefix continuants Pc[j] = K(w0..w_{j-1}), suffix Sc[j] = K(w_j..w_{r-1})
static int *len; static signed char *sg;
static int *par, *par2;
static int fnd(int *p, int x) { while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; } return x; }
static void uni(int *p, int a, int b) { a = fnd(p, a); b = fnd(p, b); if (a != b) p[a] = b; }
// adjacency (CSR, undirected): off[A]..off[A+1]
static ll *off; static int *adj; static signed char *adjs; static ll nedge;
static int VERIFY = 1;
static ll *W2, *Tm;
// enumerate moves from A; mode 0 = count, 1 = fill
static ll *fillpos;
static void moves(ll A, int mode) {
    int r = hjword(N, A, W);
    Pc[0] = 1;
    for (int i = 0; i < r; i++) { ll c = W[i] * Pc[i] - (i ? Pc[i - 1] : 0); Pc[i + 1] = c; }
    Sc[r] = 1; Sc[r + 1] = 0; for (int i = r - 1; i >= 0; i--) Sc[i] = W[i] * Sc[i + 1] - Sc[i + 2];
    for (int j = 0; j < r; j++) {            // cut at letter index j (0-based); prefix = w[0..j-1], suffix = w[j+1..]
        ll b = W[j];
        ll X = Pc[j], Xp = (j >= 1) ? Pc[j - 1] : 0;      // K(w0..w_{j-1}), K(w0..w_{j-2}); j=0: 1/0
        if (j == 1) Xp = 1;                               // K(empty) = 1
        ll Y = Sc[j + 1], Yp = (j + 2 <= r) ? Sc[j + 2] : 0;
        if (j == r - 1) { Y = 1; Yp = 0; }
        if (j == r - 2) Yp = 1;
        for (ll k = 2; k * 2 <= b; k++) {
            if (b % k) continue;
            for (int side = 0; side < 2; side++) {
                ll A2f;
                if (side == 0) { if (!(Xp >= 1 && Yp % k == 0 && gcdl(k, Xp) == 1)) continue; }
                else           { if (!(Yp >= 1 && Xp % k == 0 && gcdl(k, Yp) == 1)) continue; }
                // rebuild the target word: right move (kX/X', b/k, Y/(Y'/k)); left move (X/(X'/k), b/k, kY/Y')
                ll LX, LXp, RY, RYp;
                if (side == 0) { LX = k * X; LXp = Xp; RY = Y; RYp = Yp / k; }
                else { LX = X; LXp = Xp / k; RY = k * Y; RYp = Yp; }
                int nr = 0;
                if (LXp > 0) { int lr = hjword(LX, LXp, Tm); for (int i = lr - 1; i >= 0; i--) W2[nr++] = Tm[i]; }
                W2[nr++] = b / k;
                if (RYp > 0) { int rr = hjword(RY, RYp, Tm); for (int i = 0; i < rr; i++) W2[nr++] = Tm[i]; }
                ll a1 = 1, b1 = 0; for (int i = 0; i < nr; i++) { ll c = W2[i] * a1 - b1; b1 = a1; a1 = c; }
                ll a2 = 1, b2 = 0; for (int i = 1; i < nr; i++) { ll c = W2[i] * a2 - b2; b2 = a2; a2 = c; }
                if (a1 != N) { fprintf(stderr, "MOVE FAIL n=%lld A=%lld j=%d k=%lld side=%d\n", N, A, j, k, side); exit(1); }
                ll A2 = a2;
                if (VERIFY && gcdl(k, N) == 1) { A2f = side == 0 ? (A * inv(k, N)) % N : (A * k) % N;
                    if (A2f != A2) { fprintf(stderr, "FORMULA FAIL n=%lld A=%lld k=%lld\n", N, A, k); exit(1); } }
                int s = jac(k, N);
                if (mode == 0) { off[A + 1]++; off[A2 + 1]++; nedge++; }
                else { adj[fillpos[A]] = (int)A2; adjs[fillpos[A]++] = (signed char)s; adj[fillpos[A2]] = (int)A; adjs[fillpos[A2]++] = (signed char)s; }
            }
        }
    }
}
static int descend(ll A, int plusonly) {   // returns final vertex: repeatedly go to the shortest neighbour (least A on ties) if shorter
    for (;;) {
        ll best = -1; int bl = len[A];
        for (ll e = off[A]; e < off[A + 1]; e++) {
            if (plusonly && adjs[e] != 1) continue;
            int B = adj[e];
            if (len[B] < bl || (len[B] == bl && best >= 0 && B < best)) { bl = len[B]; best = B; }
        }
        if (best < 0) return (int)A;
        A = best;
    }
}
int main(int argc, char **argv) {
    char *v = getenv("VERIFY"); if (v) VERIFY = atoi(v);
    for (int ai = 1; ai < argc; ai++) {
        N = atoll(argv[ai]);
        if (N < 9 || N % 4 != 1 || N > 20000000) { fprintf(stderr, "bad n\n"); return 1; }
        W = malloc(sizeof(ll) * (N + 8)); W2 = malloc(sizeof(ll) * (N + 8)); Tm = malloc(sizeof(ll) * (N + 8)); Pc = malloc(sizeof(ll) * (N + 8)); Sc = malloc(sizeof(ll) * (N + 8));
        len = calloc(N, sizeof(int)); sg = calloc(N, 1); par = malloc(sizeof(int) * N); par2 = malloc(sizeof(int) * N);
        off = calloc(N + 2, sizeof(ll)); fillpos = malloc(sizeof(ll) * (N + 1));
        if (!W || !W2 || !Tm || !Pc || !Sc || !len || !sg || !par || !par2 || !off || !fillpos) { fprintf(stderr, "alloc\n"); return 1; }
        nedge = 0;
        for (ll A = 1; A < N; A++) { par[A] = par2[A] = (int)A; if (gcdl(A, N) != 1) { len[A] = 0; continue; }
            len[A] = hjword(N, A, W); sg[A] = (signed char)jac(A, N); }
        for (ll A = 1; A < N; A++) if (len[A]) moves(A, 0);
        for (ll A = 1; A <= N; A++) off[A] += off[A - 1];
        adj = malloc(sizeof(int) * (off[N] + 1)); adjs = malloc(off[N] + 1);
        if (!adj || !adjs) { fprintf(stderr, "alloc adj\n"); return 1; }
        for (ll A = 0; A <= N - 1; A++) fillpos[A] = off[A];
        for (ll A = 1; A < N; A++) if (len[A]) moves(A, 1);
        for (ll A = 1; A < N; A++) if (fillpos[A] != off[A + 1]) { fprintf(stderr, "CSR mismatch at %lld\n", A); return 1; }
        for (ll A = 1; A < N; A++) for (ll e = off[A]; e < off[A + 1]; e++) { uni(par, (int)A, adj[e]); if (adjs[e] == 1) uni(par2, (int)A, adj[e]); }
        // components containing a good L3 vertex
        char *goodcomp = calloc(N, 1), *goodcomp2 = calloc(N, 1);
        if (!goodcomp || !goodcomp2) { fprintf(stderr, "alloc\n"); return 1; }
        long nL3 = 0, gL3 = 0, nv = 0, comps = 0, comps2 = 0;
        for (ll A = 1; A < N; A++) if (len[A]) { nv++; if (fnd(par, A) == A) comps++; if (fnd(par2, A) == A) comps2++;
            if (len[A] == 3) { nL3++; if (sg[A] == -1) { gL3++; goodcomp[fnd(par, A)] = 1; goodcomp2[fnd(par2, A)] = 1; } } }
        // D, D+ by increasing length
        int maxlen = 0; for (ll A = 1; A < N; A++) if (len[A] > maxlen) maxlen = len[A];
        char *D = calloc(N, 1), *Dp = calloc(N, 1);
        ll *ord = malloc(sizeof(ll) * N); ll cnt = 0;
        if (!D || !Dp || !ord) { fprintf(stderr, "alloc\n"); return 1; }
        { ll *bucket = calloc(maxlen + 2, sizeof(ll)); if (!bucket) { fprintf(stderr, "alloc\n"); return 1; }
          for (ll A = 1; A < N; A++) if (len[A]) bucket[len[A] + 1]++;
          for (int l = 1; l <= maxlen + 1; l++) bucket[l] += bucket[l - 1];
          for (ll A = 1; A < N; A++) if (len[A]) ord[bucket[len[A]]++] = A;
          cnt = nv; free(bucket); }
        for (ll i = 0; i < cnt; i++) { ll A = ord[i];
            if (len[A] == 3 && sg[A] == -1) { D[A] = Dp[A] = 1; continue; }
            if (len[A] <= 3) continue;
            for (ll e = off[A]; e < off[A + 1]; e++) { int B = adj[e]; if (len[B] < len[A]) { if (D[B]) D[A] = 1; if (adjs[e] == 1 && Dp[B]) Dp[A] = 1; } } }
        long ng4 = 0, inC = 0, inC2 = 0, inD = 0, inDp = 0;
        for (ll A = 1; A < N; A++) if (len[A] >= 4 && sg[A] == -1) { ng4++; if (goodcomp[fnd(par, A)]) inC++; if (goodcomp2[fnd(par2, A)]) inC2++; if (D[A]) inD++; if (Dp[A]) inDp++; }
        // starts
        ll q = 2; while (q < N && jac(q, N) != -1) q++;
        if (q >= N) q = 1;   // no non-residue (odd square): S1 = A = 1
        ll S2 = -1; int S2l = 1 << 30; for (ll A = 1; A < N; A++) if (len[A] >= 4 && sg[A] == -1 && len[A] < S2l) { S2l = len[A]; S2 = A; }
        #define RES(x) ((len[x] == 3 && sg[x] == -1) ? "GOOD-L3" : (len[x] == 3 ? "bad-L3" : "stuck"))
        int e1 = descend(q, 0), e1p = descend(q, 1);
        int e2 = S2 > 0 ? descend(S2, 0) : 0, e2p = S2 > 0 ? descend(S2, 1) : 0;
        long nb = 0, sb = 0, sbp = 0, sbD = 0, sbDp = 0;
        for (ll A = 1; A < N; A++) { if (len[A] < 6 || sg[A] != -1) continue; int r = hjword(N, A, W), ok = 1;
            for (int i = 0; i < r; i++) if (W[i] > 4) { ok = 0; break; }
            if (!ok) continue;
            nb++; int e = descend(A, 0); if (len[e] == 3 && sg[e] == -1) sb++; e = descend(A, 1); if (len[e] == 3 && sg[e] == -1) sbp++;
            if (D[A]) sbD++;
            if (Dp[A]) sbDp++; }
        // giant components and registered-start component membership
        int *csz = calloc(N, sizeof(int)), *csz2 = calloc(N, sizeof(int));
        if (!csz || !csz2) { fprintf(stderr, "alloc\n"); return 1; } long gmax = 0, gmax2 = 0; ll groot = 0, groot2 = 0;
        for (ll A = 1; A < N; A++) if (len[A]) { int r1 = fnd(par, A), r2 = fnd(par2, A); csz[r1]++; csz2[r2]++;
            if (csz[r1] > gmax) { gmax = csz[r1]; groot = r1; } if (csz2[r2] > gmax2) { gmax2 = csz2[r2]; groot2 = r2; } }
        long L3inG = 0, gL3inG = 0, gL3inG2 = 0, L3inG2 = 0;
        for (ll A = 1; A < N; A++) if (len[A] == 3) { if (fnd(par, A) == groot) { L3inG++; if (sg[A] == -1) gL3inG++; } if (fnd(par2, A) == groot2) { L3inG2++; if (sg[A] == -1) gL3inG2++; } }
        int s1c = goodcomp[fnd(par, q)], s1c2 = goodcomp2[fnd(par2, q)], s2c = S2 > 0 ? goodcomp[fnd(par, S2)] : 0, s2c2 = S2 > 0 ? goodcomp2[fnd(par2, S2)] : 0;
        printf("n=%lld giant=%.4f giant+=%.4f giant+sign=%d L3inGiant=%ld/%ld goodL3inGiant=%ld L3inGiant+=%ld goodL3inGiant+=%ld S1comp:%d S1comp+:%d S1D:%d S1D+:%d S2comp:%d S2comp+:%d S2D:%d S2D+:%d\n",
               N, (double)gmax / nv, (double)gmax2 / nv, (int)sg[groot2], L3inG, nL3, gL3inG, L3inG2, gL3inG2, s1c, s1c2, D[q], Dp[q], s2c, s2c2, S2 > 0 ? D[S2] : 0, S2 > 0 ? Dp[S2] : 0);
        free(csz); free(csz2);
        // minimax height: least H such that, in the subgraph of words of length <= H, the start is connected (E, resp. E+)
        // to a good L3 vertex
        { int hS[2][2] = {{-1, -1}, {-1, -1}}; ll st[2] = {q, S2};
          for (int pl = 0; pl < 2; pl++) {
            int *pp = malloc(sizeof(int) * N); if (!pp) { fprintf(stderr, "alloc\n"); return 1; }
            for (ll A = 0; A < N; A++) pp[A] = (int)A;
            ll i = 0; int done = 0;
            for (int H = 1; H <= maxlen && !done; H++) {
              for (; i < cnt && len[ord[i]] <= H; i++) { ll A = ord[i];
                for (ll e = off[A]; e < off[A + 1]; e++) { int B = adj[e]; if (len[B] <= len[A] && (!pl || adjs[e] == 1)) uni(pp, (int)A, B); } }
              if (H < 3) continue;
              for (int t = 0; t < 2; t++) if (hS[pl][t] < 0 && st[t] > 0 && len[st[t]] <= H) {
                int rt = fnd(pp, (int)st[t]);
                for (ll j = 0; j < cnt && len[ord[j]] <= 3; j++) { ll A = ord[j]; if (len[A] == 3 && sg[A] == -1 && fnd(pp, (int)A) == rt) { hS[pl][t] = H; break; } } }
              if (hS[pl][0] >= 0 && hS[pl][1] >= 0) done = 1;
            }
            free(pp);
          }
          printf("n=%lld minimax-height to a good L3: S1(len %d): E %d E+ %d | S2(len %d): E %d E+ %d   (-1 = never)\n", N, len[q], hS[0][0], hS[1][0], S2 > 0 ? len[S2] : -1, hS[0][1], hS[1][1]); }
        { long s2r = 0, s2rp = 0, s1r = 0, s1rp = 0, s3any = 0, s3anyD = 0;
          s1r = (len[e1] == 3 && sg[e1] == -1); s1rp = (len[e1p] == 3 && sg[e1p] == -1);
          if (S2 > 0) { s2r = (len[e2] == 3 && sg[e2] == -1); s2rp = (len[e2p] == 3 && sg[e2p] == -1); }
          s3any = sb > 0; s3anyD = sbD > 0;
          printf("n=%lld COUNTS goodlen4=%ld inD=%ld inDp=%ld S3n=%ld S3Rmin=%ld S3Rminp=%ld S3D=%ld S3Dp=%ld S3anyRmin=%ld S3anyD=%ld"
                 " S1len=%d S1good=%d S1Rmin=%ld S1Rminp=%ld S1D=%d S1Dp=%d S2A=%lld S2Rmin=%ld S2Rminp=%ld S2D=%d S2Dp=%d moves=%lld V=%ld\n",
                 N, ng4, inD, inDp, nb, sb, sbp, sbD, sbDp, s3any, s3anyD, len[q], (int)(sg[q] == -1), s1r, s1rp, (int)D[q], (int)Dp[q],
                 S2, s2r, s2rp, S2 > 0 ? (int)D[S2] : 0, S2 > 0 ? (int)Dp[S2] : 0, nedge, nv); }
        printf("n=%lld V=%ld E=%lld comps=%ld comps+=%ld L3=%ld goodL3=%ld | good len>=4: %ld inGoodComp=%.4f inGoodComp+=%.4f D=%.4f D+=%.4f"
               " | S1 q=%lld len=%d Rmin:%s(len%d) Rmin+:%s | S2 A=%lld len=%d Rmin:%s Rmin+:%s | S3 bounded(<=4,len>=6) good=%ld Rmin=%.3f Rmin+=%.3f D=%.3f D+=%.3f\n",
               N, nv, nedge, comps, comps2, nL3, gL3, ng4, ng4 ? (double)inC / ng4 : 0, ng4 ? (double)inC2 / ng4 : 0, ng4 ? (double)inD / ng4 : 0, ng4 ? (double)inDp / ng4 : 0,
               q, len[q], RES(e1), len[e1], RES(e1p), S2, S2 > 0 ? S2l : -1, S2 > 0 ? RES(e2) : "-", S2 > 0 ? RES(e2p) : "-",
               nb, nb ? (double)sb / nb : 0, nb ? (double)sbp / nb : 0, nb ? (double)sbD / nb : 0, nb ? (double)sbDp / nb : 0);
        fflush(stdout);
        free(W); free(W2); free(Tm); free(Pc); free(Sc); free(len); free(sg); free(par); free(par2); free(off); free(fillpos); free(adj); free(adjs);
        free(goodcomp); free(goodcomp2); free(D); free(Dp); free(ord);
    }
    return 0;
}
