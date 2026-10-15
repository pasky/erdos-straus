// z11_tree.c — DFS tree covering of the exponent space (see z11_pool.py for the pool format).
// Node: for each prime l in HP a precision e_l and the residue c_l = mu mod l^{e_l}.  Leaf: some period P with f_P <= e
// has E_P[idx(c)] = 1.  Split: refine one prime l by one digit (l children), chosen to maximise the covered fraction of
// children (ties: smaller l^{e+1}); fallback: two-digit lookahead on the cheapest pair; then smallest l^{e+1}.
// Output stream (text): "S l" (split on l; children j = 0..l-1 in order c_l + j l^{e_l}), "C p" (leaf by period index p),
// "X" (stuck).  Usage: z11_tree pool.bin NODEMAX out.txt [maxdepth]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef int64_t i64;
int nH; i64 HP[512], CAP[512], PW[512][16];
int nP; typedef struct { int nc; int li[16]; i64 rad[16], stride[16]; int f[16]; i64 Lp; unsigned char *E; } Per;
Per *P;
int *byl[512]; int nbyl[512];
i64 e[512], c[512];
i64 nodes = 0, NODEMAX, leaves = 0, stuck = 0; int maxdepth = 400, curdepth = 0, deepest = 0;
FILE *out;
double meas = 1.0, covmeas = 0.0;
int *newl[512][64]; int nnewl[512][64];

static int covered_by(int p) {  // assumes divisibility
  Per *q = &P[p]; i64 idx = 0;
  for (int t = 0; t < q->nc; t++) idx += (c[q->li[t]] % q->rad[t]) * q->stride[t];
  return q->E[idx];
}
static int divides(int p) {
  Per *q = &P[p];
  for (int t = 0; t < q->nc; t++) if (q->f[t] > e[q->li[t]]) return 0;
  return 1;
}
static int leaf(void) {
  for (int p = 0; p < nP; p++) if (divides(p) && covered_by(p)) return p;
  return -1;
}
// periods newly dividing after e[l]++ : f_l == e[l]+1, others <= e
static int lsts[1 << 20]; int lstn = 0;
static int newlist(int l, int *buf) {  // periods that newly divide after e[l]++
  int n = 0; e[l]++;
  for (int t = 0; t < nbyl[l]; t++) { int p = byl[l][t]; Per *q = &P[p]; int ok = 0, dv = 1;
    for (int s = 0; s < q->nc; s++) { if (q->f[s] > e[q->li[s]]) { dv = 0; break; } if (q->li[s] == l && q->f[s] == e[l]) ok = 1; }
    if (dv && ok) buf[n++] = p; }
  e[l]--; return n;
}
static int newcov(int l, int *buf, int n, unsigned char *cv) {
  i64 base = c[l], step = PW[l][e[l]]; int cnt = 0;
  e[l]++;
  for (i64 j = 0; j < HP[l]; j++) {
    c[l] = base + j * step; cv[j] = 0;
    for (int t = 0; t < n; t++) if (covered_by(buf[t])) { cnt++; cv[j] = 1; break; }
  }
  e[l]--; c[l] = base;
  return cnt;
}
static void solve(int known);
static void solve(int known) {  // known: 1 if the caller already established that this node is not a leaf
  nodes++;
  if (nodes > NODEMAX) { fprintf(stderr, "node budget\n"); fprintf(out, "ABORT\n"); fclose(out); exit(2); }
  if (nodes % 200000 == 0) fprintf(stderr, "nodes %lld leaves %lld covered measure %.12f\n", (long long)nodes, (long long)leaves, covmeas);
  if (curdepth > deepest) deepest = curdepth;
  if (!known) { int p = leaf(); if (p >= 0) { fprintf(out, "C %d\n", p); leaves++; covmeas += meas; return; } }
  int best = -1; double bs = -1; i64 bcost = 0;
  int *buf = malloc(sizeof(int) * nP); unsigned char cv[2048], bcv[2048];
  for (int l = 0; l < nH; l++) {
    if (e[l] >= CAP[l]) continue;
    int n = newlist(l, buf); if (!n) continue;
    int k = newcov(l, buf, n, cv);
    if (!k) continue;
    double s = (double)k / HP[l];
    i64 cost = PW[l][e[l] + 1];
    if (s > bs + 1e-12 || (s > bs - 1e-12 && cost < bcost)) { bs = s; best = l; bcost = cost; memcpy(bcv, cv, HP[l]); }
  }
  free(buf);
  int haveinfo = best >= 0;
  if (best < 0) {
    for (int l = 0; l < nH; l++) if (e[l] < CAP[l]) { i64 cost = PW[l][e[l] + 1]; if (best < 0 || cost < bcost) { best = l; bcost = cost; } }
  }
  if (best < 0 || curdepth >= maxdepth) { fprintf(out, "X\n"); stuck++; if (stuck <= 5) { fprintf(stderr, "stuck:"); for (int l = 0; l < nH; l++) if (e[l]) fprintf(stderr, " %lld^%lld:%lld", (long long)HP[l], (long long)e[l], (long long)c[l]); fprintf(stderr, "\n"); } return; }
  fprintf(out, "S %lld\n", (long long)HP[best]);
  i64 base = c[best], step = PW[best][e[best]];
  e[best]++; curdepth++; double om = meas; meas /= HP[best];
  for (i64 j = 0; j < HP[best]; j++) { c[best] = base + j * step; solve(haveinfo && !bcv[j]); }
  e[best]--; curdepth--; c[best] = base; meas = om;
}
int main(int argc, char **argv) {
  FILE *f = fopen(argv[1], "rb"); NODEMAX = atoll(argv[2]); out = fopen(argv[3], "w");
  if (argc > 4) maxdepth = atoi(argv[4]);
  i64 x; fread(&x, 8, 1, f); nH = x;
  fread(HP, 8, nH, f); fread(CAP, 8, nH, f);
  for (int l = 0; l < nH; l++) { PW[l][0] = 1; for (int t = 1; t < 16; t++) PW[l][t] = PW[l][t - 1] * HP[l]; }
  fread(&x, 8, 1, f); nP = x; P = calloc(nP, sizeof(Per));
  i64 fv[512];
  for (int p = 0; p < nP; p++) {
    fread(fv, 8, nH, f); fread(&P[p].Lp, 8, 1, f);
    i64 stride = 1; P[p].nc = 0;
    for (int l = 0; l < nH; l++) if (fv[l]) { int t = P[p].nc++; P[p].li[t] = l; P[p].f[t] = fv[l]; P[p].rad[t] = PW[l][fv[l]]; P[p].stride[t] = stride; stride *= PW[l][fv[l]]; }
    if (stride != P[p].Lp) { fprintf(stderr, "bad period\n"); return 1; }
    P[p].E = malloc(P[p].Lp); fread(P[p].E, 1, P[p].Lp, f);
  }
  for (int l = 0; l < nH; l++) { byl[l] = malloc(sizeof(int) * nP); nbyl[l] = 0; }
  for (int p = 0; p < nP; p++) for (int t = 0; t < P[p].nc; t++) { int l = P[p].li[t]; byl[l][nbyl[l]++] = p; }
  fprintf(stderr, "loaded %d primes, %d periods\n", nH, nP);
  memset(e, 0, sizeof e); memset(c, 0, sizeof c);
  solve(0);
  fclose(out);
  fprintf(stderr, "nodes %lld leaves %lld stuck %lld deepest %d\n", (long long)nodes, (long long)leaves, (long long)stuck, deepest);
  return stuck ? 1 : 0;
}
