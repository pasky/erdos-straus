/* z48 forestfable — full forest F_p scan for primes p ≡ 1 (mod 4) up to N.
 *
 * F_p: vertices 1..p+2, edge {u,v} iff uv | p+u+v.  Every edge has a smaller
 * endpoint u ≤ sqrt(p+1)+1 and larger endpoint v | p+u with v ≡ -p (mod u).
 * We enumerate edges by u, factoring p+u with a smallest-prime-factor sieve.
 *
 * Per prime we output one line:
 *  p r W B H4 umin tmin Amin viol_slot viol_classB
 *  L0 L7 L3 Lodd Lp1 Lp2 Lp3 Lp4 Lp7 Lp15 Lt2 Lt3 Lt4 Lt7 Lt15 LprimeA
 *  ncomp maxc maxbi c1size c1bi nbicomp bi_in_big nonisol
 *  m_i m_ii m_iii   (monochromatic edges by Theorem B class, p ≡ 1 mod 8 only)
 * where
 *  r = least QNR, W = #edges, B = #bichromatic edges, H4 = least larger
 *  endpoint of a bichromatic edge, umin = least smaller endpoint of one,
 *  tmin = least level t of one, Amin = least numerator min(A,A*) of one
 *  (A=(p+u)/v, A*=(p+v)/u), viol_* = number of edges contradicting Thm A/B,
 *  L0: some bichromatic edge has an endpoint ≡ 0 (4); L7: ≡ 7 (8);
 *  L3: ≡ 3 (8); Lodd: both endpoints odd;
 *  Lp_u: line u (smaller endpoint u) carries a bichromatic edge;
 *  Lt_t: level t carries one; LprimeA: some bichromatic edge has A or A* prime;
 *  components (over non-isolated vertices): count, largest size, largest is
 *  bichromatic, size/bichromacy of comp(1), number of bichromatic components,
 *  whether some bichromatic edge lies in a component of size ≥ 3, number of
 *  non-isolated vertices.
 * Usage: scan N [pmin]      (primes p ≡ 1 mod 4 in [pmin, N])
 *        scan N pmin modc   (restrict to p ≡ 1 mod modc; modc=0: odd squares
 *                            n=m^2 ≤ N; modc=1: explicit list n1 n2 ... in argv)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>

typedef uint64_t u64;
typedef int64_t i64;

static uint32_t *spf;

static int jacobi(u64 a, u64 n) { /* n odd positive */
    a %= n;
    int r = 1;
    while (a) {
        while ((a & 1) == 0) { a >>= 1; u64 m = n & 7; if (m == 3 || m == 5) r = -r; }
        u64 tmp = a; a = n; n = tmp;
        if ((a & 3) == 3 && (n & 3) == 3) r = -r;
        a %= n;
    }
    return n == 1 ? r : 0;
}

#define MAXE 200000
static u64 EU[MAXE], EV[MAXE];
static int ECOL[MAXE];
static u64 VERTS[2 * MAXE];
static int PARENT[2 * MAXE], SZ[2 * MAXE];

static int cmpu64(const void *a, const void *b) {
    u64 x = *(const u64 *)a, y = *(const u64 *)b;
    return x < y ? -1 : x > y;
}
static int findv(u64 *arr, int n, u64 x) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) { int m = (lo + hi) / 2; if (arr[m] == x) return m; if (arr[m] < x) lo = m + 1; else hi = m - 1; }
    return -1;
}
static int uf_find(int x) { while (PARENT[x] != x) { PARENT[x] = PARENT[PARENT[x]]; x = PARENT[x]; } return x; }
static void uf_union(int a, int b) { a = uf_find(a); b = uf_find(b); if (a == b) return; if (SZ[a] < SZ[b]) { int t = a; a = b; b = t; } PARENT[b] = a; SZ[a] += SZ[b]; }


int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: %s N [pmin] [modc]\n", argv[0]); return 1; }
    u64 N = strtoull(argv[1], 0, 10);
    u64 pmin = argc > 2 ? strtoull(argv[2], 0, 10) : 5;
    u64 modc = argc > 3 ? strtoull(argv[3], 0, 10) : 4;
    u64 S = N + 2 * (u64)sqrt((double)N) + 16;
    spf = calloc(S + 1, sizeof(uint32_t));
    if (!spf) { fprintf(stderr, "alloc\n"); return 1; }
    for (u64 i = 2; i <= S; i++) if (!spf[i]) { for (u64 j = i; j <= S; j += i) if (!spf[j]) spf[j] = (uint32_t)i; }

    printf("p r W B H4 umin tmin Amin viol_slot viol_classB L0 L7 L3 Lodd Lp1 Lp2 Lp3 Lp4 Lp7 Lp15 Lt2 Lt3 Lt4 Lt7 Lt15 LprimeA ncomp maxc maxbi c1size c1bi nbicomp bi_in_big nonisol m_i m_ii m_iii E0 E7 E08 Lleg Ltuv4 LA7 n07 nleg ntuv4 nA7 v07min lmin\n");

    int nlist = argc > 4 ? argc - 4 : 0;
    u64 *list = 0; if (nlist) { list = malloc(nlist * sizeof(u64)); for (int i = 0; i < nlist; i++) list[i] = strtoull(argv[4 + i], 0, 10); }
    int li = 0;
    for (u64 p = pmin | 1; p <= N; p += 2) {
        if (modc >= 2) {
            if (spf[p] != p) continue;
            if (p % modc != 1) continue;
        } else if (modc == 0) { /* odd squares */
            u64 m = (u64)sqrt((double)p); while (m * m < p) m++; while (m * m > p) m--;
            if (m * m != p) continue;
        } else { /* explicit list */
            if (li >= nlist) break;
            p = list[li++];
        }
        if (p < 5) continue;
        /* least QNR */
        u64 r = 2; while (jacobi(r, p) != -1) { r++; if (r > 1000000) { r = 0; break; } }
        int ne = 0;
        u64 umax = (u64)sqrt((double)(p + 1)) + 2;
        for (u64 u = 1; u <= umax; u++) {
            u64 n = p + u;
            u64 rr = (u - (p % u)) % u; /* -p mod u */
            /* factor n */
            u64 pr[64]; int ex[64]; int k = 0; u64 m = n;
            while (m > 1) { u64 q = spf[m]; int e = 0; while (m % q == 0) { m /= q; e++; } pr[k] = q; ex[k] = e; k++; }
            /* enumerate divisors */
            u64 divs[8192]; int nd = 1; divs[0] = 1;
            for (int i = 0; i < k; i++) { int cur = nd; u64 pw = 1; for (int e = 1; e <= ex[i]; e++) { pw *= pr[i]; for (int j = 0; j < cur; j++) divs[nd++] = divs[j] * pw; } }
            for (int i = 0; i < nd; i++) {
                u64 v = divs[i];
                if (v <= u) continue;
                if (v % u != rr) continue;
                if ((p + u + v) % (u * v) != 0) { if (modc >= 2) { fprintf(stderr, "edge predicate failure p=%llu u=%llu v=%llu\n", (unsigned long long)p, (unsigned long long)u, (unsigned long long)v); return 2; } continue; }
                if (ne >= MAXE) { fprintf(stderr, "too many edges\n"); return 3; }
                EU[ne] = u; EV[ne] = v; ne++;
            }
        }
        /* stats */
        u64 W = ne, B = 0, H4 = 0, umin = 0, tmin = 0, Amin = 0;
        u64 viol_slot = 0, viol_cB = 0;
        int L0 = 0, L7 = 0, L3 = 0, Lodd = 0, Lp[16] = {0}, Lt[16] = {0}, LprimeA = 0;
        int E0 = 0, E7 = 0, E08 = 0; /* sign-free: some edge (any colour) has an endpoint ≡ 0(4) / 7(8) / 0(8) */
        int Lleg = 0, Ltuv4 = 0, LA7 = 0;
        u64 n07 = 0, nleg = 0, ntuv4 = 0, nA7 = 0; /* word counts per sign-free family */
        u64 v07min = 0; /* least vertex ≡ 0 (4) or 7 (8) that is non-isolated */
        u64 lmin = 0;   /* least prime numerator (A or A*) of a bichromatic edge */
        u64 m_i = 0, m_ii = 0, m_iii = 0;
        for (int i = 0; i < ne; i++) {
            u64 u = EU[i], v = EV[i];
            u64 t = (p + u + v) / (u * v);
            u64 A = (p + u) / v, As = (p + v) / u;
            int cu = jacobi(u, p), cv = jacobi(v, p);
            int bi = (cu * cv == -1);
            ECOL[i] = bi;
            int sl = (t % 4 == 0) || (u % 4 == 0) || (v % 4 == 0) || ((t * u - 1) % 4 == 0) || ((t * v - 1) % 4 == 0);
            if (bi != sl) viol_slot++;
            if (u % 4 == 0 || v % 4 == 0) E0 = 1;
            if (u % 8 == 7 || v % 8 == 7) E7 = 1;
            if (u % 8 == 0 || v % 8 == 0) E08 = 1;
            { u64 tt = t; while (tt % 4 == 0) tt /= 4; int leg = (tt % 8 == 7); /* Legendre level (p ≡ 1 mod 8) */
              int f07 = (u % 4 == 0 || v % 4 == 0 || u % 8 == 7 || v % 8 == 7);
              int f4 = (t % 4 == 0 || u % 4 == 0 || v % 4 == 0);
              int fA7 = (A % 4 == 0 || As % 4 == 0 || A % 8 == 7 || As % 8 == 7);
              if (leg) { nleg++; if (bi) Lleg = 1; }
              if (f07) { n07++; u64 q = (u % 4 == 0 || u % 8 == 7) ? u : v; if (!v07min || q < v07min) v07min = q; }
              if (f4) { ntuv4++; if (bi) Ltuv4 = 1; }
              if (fA7) { nA7++; if (bi) LA7 = 1; } }
            {
                /* Theorem B: monochromatic iff {u mod 8, v mod 8} is one of the listed unordered pairs */
                int a8 = u % 8, b8 = v % 8; if (a8 > b8) { int x = a8; a8 = b8; b8 = x; }
                int ci = (u % 4 == 1 && v % 4 == 1);                      /* {1,1},{1,5},{5,5} */
                int cii, ciii;
                if (p % 8 == 1) {
                    cii = (a8 == 1 && b8 == 2) || (a8 == 5 && b8 == 6);     /* {1,2},{5,6} */
                    ciii = (a8 == 2 && b8 == 3) || (a8 == 3 && b8 == 6);    /* {2,3},{3,6} */
                } else {
                    cii = (a8 == 1 && b8 == 6) || (a8 == 2 && b8 == 5);     /* {1,6},{2,5} */
                    ciii = (a8 == 2 && b8 == 7) || (a8 == 6 && b8 == 7);    /* {2,7},{6,7} */
                }
                int mono_pred = ci || cii || ciii;
                if ((!bi) != mono_pred) viol_cB++;
                if (!bi) { if (ci) m_i++; else if (cii) m_ii++; else if (ciii) m_iii++; }
            }
            if (bi) {
                B++;
                if (!H4 || v < H4) H4 = v;
                if (!umin || u < umin) umin = u;
                if (!tmin || t < tmin) tmin = t;
                u64 Am = A < As ? A : As; if (!Amin || Am < Amin) Amin = Am;
                if (u % 4 == 0 || v % 4 == 0) L0 = 1;
                if (u % 8 == 7 || v % 8 == 7) L7 = 1;
                if (u % 8 == 3 || v % 8 == 3) L3 = 1;
                if (u % 2 == 1 && v % 2 == 1) Lodd = 1;
                if (u < 16) Lp[u] = 1;
                if (t < 16) Lt[t] = 1;
                if (A <= S && spf[A] == A) { LprimeA = 1; if (!lmin || A < lmin) lmin = A; }
                if (As <= S && spf[As] == As) { LprimeA = 1; if (!lmin || As < lmin) lmin = As; }
            }
        }
        /* components */
        int nv = 0;
        for (int i = 0; i < ne; i++) { VERTS[nv++] = EU[i]; VERTS[nv++] = EV[i]; }
        qsort(VERTS, nv, sizeof(u64), cmpu64);
        int nu = 0; for (int i = 0; i < nv; i++) if (i == 0 || VERTS[i] != VERTS[i - 1]) VERTS[nu++] = VERTS[i];
        for (int i = 0; i < nu; i++) { PARENT[i] = i; SZ[i] = 1; }
        for (int i = 0; i < ne; i++) uf_union(findv(VERTS, nu, EU[i]), findv(VERTS, nu, EV[i]));
        /* bichromatic components: a component is bichromatic iff it contains a bichromatic edge */
        static char CB[2 * MAXE];
        memset(CB, 0, nu);
        for (int i = 0; i < ne; i++) if (ECOL[i]) CB[uf_find(findv(VERTS, nu, EU[i]))] = 1;
        int ncomp = 0, maxc = 0, maxbi = 0, nbicomp = 0, bi_in_big = 0;
        for (int i = 0; i < nu; i++) if (uf_find(i) == i) {
            ncomp++;
            if (CB[i]) { nbicomp++; if (SZ[i] >= 3) bi_in_big = 1; }
            if (SZ[i] > maxc || (SZ[i] == maxc && CB[i] && !maxbi)) { maxc = SZ[i]; maxbi = CB[i]; }
        }
        int i1 = findv(VERTS, nu, 1);
        int c1size = i1 >= 0 ? SZ[uf_find(i1)] : 1;
        int c1bi = i1 >= 0 ? CB[uf_find(i1)] : 0;
        printf("%llu %llu %llu %llu %llu %llu %llu %llu %llu %llu %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %llu %llu %llu %d %d %d %d %d %d %llu %llu %llu %llu %llu %llu\n",
               (unsigned long long)p, (unsigned long long)r, (unsigned long long)W, (unsigned long long)B, (unsigned long long)H4,
               (unsigned long long)umin, (unsigned long long)tmin, (unsigned long long)Amin, (unsigned long long)viol_slot, (unsigned long long)viol_cB,
               L0, L7, L3, Lodd, Lp[1], Lp[2], Lp[3], Lp[4], Lp[7], Lp[15], Lt[2], Lt[3], Lt[4], Lt[7], Lt[15], LprimeA,
               ncomp, maxc, maxbi, c1size, c1bi, nbicomp, bi_in_big, nu,
               (unsigned long long)m_i, (unsigned long long)m_ii, (unsigned long long)m_iii, E0, E7, E08, Lleg, Ltuv4, LA7,
               (unsigned long long)n07, (unsigned long long)nleg, (unsigned long long)ntuv4, (unsigned long long)nA7, (unsigned long long)v07min, (unsigned long long)lmin);
    }
    return 0;
}
