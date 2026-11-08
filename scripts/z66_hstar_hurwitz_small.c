/* z66 HSTAR — KT3: exhaustive realisability of 3-point branch data S^2 -> S^2 in small degree N.
 *
 * For every partition lam1 of N (one representative s1) and EVERY permutation s2 in S_N we form
 * s3 = (s1 s2)^{-1}; if <s1,s2> is transitive, the triple (type s1, type s2, type s3) is a realisable
 * 3-point datum (product s1 s2 s3 = 1).  We also record whether some realisation has PRIMITIVE monodromy
 * (no non-trivial block system), and, for imprimitive-only data, the set of block sizes that occur.
 * Every datum (unordered triple of partitions, all != [1^N]) with Riemann-Hurwitz compatibility
 * sum_i (N - len(lam_i)) = 2N - 2 + 2g, g >= 0, is then classified realisable / exceptional.
 *
 * Output (stdout): one line per compatible datum:  R|E  g  lam1 ; lam2 ; lam3  [P|I blocks=...]
 * Usage: z66_hstar_hurwitz_small N   (N <= 10)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 10
static int N;
static int nparts;               /* number of partitions of N */
static int parts[64][MAXN + 1];  /* parts[k][0] = length, then parts descending */

static void gen_parts(int rem, int maxp, int *cur, int len) {
    if (rem == 0) {
        parts[nparts][0] = len;
        for (int i = 0; i < len; i++) parts[nparts][i + 1] = cur[i];
        nparts++;
        return;
    }
    for (int p = (rem < maxp ? rem : maxp); p >= 1; p--) {
        cur[len] = p;
        gen_parts(rem - p, p, cur, len + 1);
    }
}

static int type_index(const int *perm) {
    int seen[MAXN] = {0}, cyc[MAXN], nc = 0;
    for (int i = 0; i < N; i++)
        if (!seen[i]) {
            int l = 0, j = i;
            while (!seen[j]) { seen[j] = 1; j = perm[j]; l++; }
            cyc[nc++] = l;
        }
    /* sort descending */
    for (int a = 0; a < nc; a++)
        for (int b = a + 1; b < nc; b++)
            if (cyc[b] > cyc[a]) { int t = cyc[a]; cyc[a] = cyc[b]; cyc[b] = t; }
    for (int k = 0; k < nparts; k++) {
        if (parts[k][0] != nc) continue;
        int ok = 1;
        for (int i = 0; i < nc; i++) if (parts[k][i + 1] != cyc[i]) { ok = 0; break; }
        if (ok) return k;
    }
    return -1;
}

/* union-find transitivity */
static int uf[MAXN];
static int fnd(int x) { while (uf[x] != x) x = uf[x] = uf[uf[x]]; return x; }
static int transitive(const int *a, const int *b) {
    for (int i = 0; i < N; i++) uf[i] = i;
    int comps = N;
    for (int i = 0; i < N; i++) {
        int x = fnd(i), y = fnd(a[i]);
        if (x != y) { uf[x] = y; comps--; }
        x = fnd(i); y = fnd(b[i]);
        if (x != y) { uf[x] = y; comps--; }
    }
    return comps == 1;
}

/* block systems: for a transitive group <a,b>, the minimal block containing {0, j} (j != 0) is computed
 * by union-find closure; the group is primitive iff every such block is everything. Returns bitmask of
 * block sizes d (1<d<N) that occur. */
static int block_sizes(const int *a, const int *b) {
    int mask = 0;
    for (int j = 1; j < N; j++) {
        for (int i = 0; i < N; i++) uf[i] = i;
        uf[fnd(0)] = fnd(j);
        int changed = 1;
        while (changed) {
            changed = 0;
            for (int x = 0; x < N; x++)
                for (int y = 0; y < N; y++)
                    if (x < y && fnd(x) == fnd(y)) {
                        int ax = fnd(a[x]), ay = fnd(a[y]);
                        if (ax != ay) { uf[ax] = ay; changed = 1; }
                        int bx = fnd(b[x]), by = fnd(b[y]);
                        if (bx != by) { uf[bx] = by; changed = 1; }
                    }
        }
        int r = fnd(0), sz = 0;
        for (int i = 0; i < N; i++) if (fnd(i) == r) sz++;
        if (sz < N) mask |= 1 << sz;
    }
    return mask;
}

/* realised[k1][k2][k3]: bit0 = realisable, bit1 = primitive realisation exists; blk = OR of block masks
 * of imprimitive realisations */
static unsigned char realised[64][64][64];
static int blk[64][64][64];

int main(int argc, char **argv) {
    N = argc > 1 ? atoi(argv[1]) : 5;
    if (N < 2 || N > MAXN) { fprintf(stderr, "N in 2..%d\n", MAXN); return 1; }
    int cur[MAXN];
    gen_parts(N, N, cur, 0);
    int perm[MAXN], s1[MAXN], s12[MAXN], s3[MAXN];
    for (int k1 = 0; k1 < nparts; k1++) {
        /* representative of class k1: consecutive cycles */
        int pos = 0;
        for (int c = 1; c <= parts[k1][0]; c++) {
            int l = parts[k1][c];
            for (int i = 0; i < l; i++) s1[pos + i] = pos + (i + 1) % l;
            pos += l;
        }
        /* iterate all permutations perm (s2) via Heap's algorithm */
        for (int i = 0; i < N; i++) perm[i] = i;
        int c[MAXN] = {0};
        int idx = 0;
        for (;;) {
            /* process perm */
            /* composition convention: (s1 s2)(x) = s1(s2(x)); s3 = inverse */
            for (int i = 0; i < N; i++) s12[i] = s1[perm[i]];
            for (int i = 0; i < N; i++) s3[s12[i]] = i;
            if (transitive(s1, perm)) {
                int k2 = type_index(perm), k3 = type_index(s3);
                unsigned char *r = &realised[k1][k2][k3];
                *r |= 1;
                if (!(*r & 2)) { /* block structure only needed until a primitive realisation is seen */
                    int bm = block_sizes(s1, perm);
                    if (bm == 0) *r |= 2; else blk[k1][k2][k3] |= bm;
                }
            }
            /* next permutation (Heap) */
            while (idx < N) {
                if (c[idx] < idx) {
                    int a = (idx % 2 == 0) ? 0 : c[idx];
                    int t = perm[a]; perm[a] = perm[idx]; perm[idx] = t;
                    c[idx]++;
                    idx = 0;
                    break;
                } else {
                    c[idx] = 0;
                    idx++;
                }
            }
            if (idx >= N) break;
        }
    }
    /* enumerate unordered compatible data k1 <= k2 <= k3, none = [1^N] (the last partition) */
    int ident = nparts - 1; /* parts generated descending: last is 1^N */
    int nR = 0, nE = 0, nI = 0;
    for (int k1 = 0; k1 < nparts; k1++)
        for (int k2 = k1; k2 < nparts; k2++)
            for (int k3 = k2; k3 < nparts; k3++) {
                if (k1 == ident || k2 == ident || k3 == ident) continue;
                int v = 3 * N - parts[k1][0] - parts[k2][0] - parts[k3][0];
                int t = v - (2 * N - 2);
                if (t < 0 || t % 2) continue;
                int g = t / 2;
                /* realisable if any ordering realised (realised[] is symmetric under permutation of
                   positions up to inversion/conjugation; check all orderings to be safe) */
                int ks[3] = {k1, k2, k3};
                int perms6[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
                unsigned char r = 0; int bm = 0;
                for (int q = 0; q < 6; q++) {
                    r |= realised[ks[perms6[q][0]]][ks[perms6[q][1]]][ks[perms6[q][2]]];
                    bm |= blk[ks[perms6[q][0]]][ks[perms6[q][1]]][ks[perms6[q][2]]];
                }
                printf("%c g=%d ", (r & 1) ? 'R' : 'E', g);
                for (int q = 0; q < 3; q++) {
                    printf("[");
                    for (int i = 1; i <= parts[ks[q]][0]; i++) printf(i > 1 ? ",%d" : "%d", parts[ks[q]][i]);
                    printf("]%s", q < 2 ? " " : "");
                }
                if (r & 1) {
                    if (r & 2) printf(" P");
                    else {
                        printf(" I blocks=");
                        for (int d = 2; d < N; d++) if (bm >> d & 1) printf("%d,", d);
                        nI++;
                    }
                    nR++;
                } else nE++;
                printf("\n");
            }
    fprintf(stderr, "N=%d partitions=%d compatible data: realisable %d (imprimitive-only %d), exceptional %d\n",
            N, nparts, nR, nI, nE);
    return 0;
}
