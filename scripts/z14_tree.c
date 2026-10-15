// z14_tree.c — DFS tree covering of the exponent space Ẑ for n_s = 4^s + k with an ON-THE-FLY class supply.
// Node: precisions e_l and residues c_l = mu mod l^{e_l} for primes l <= B.  A prime q (from z14_primes output) is ACTIVE at
// a node iff ord_q(4) | L = prod l^{e_l}; then g_q = n mod q = 4^{mu mod ord} + k mod q is known.
// Leaf tests (f = product of distinct active primes, unbounded):
//   D   : q | n, q !| k                                   (ES(n) from ES(q))
//   II2 : (a,d), 4ad <= A2:  f | n + 4a^2 d,  f = -1 mod 4ad
//   I3  : (c,d), 4cd <= A3:  f | n^2 + 4c^2 d, f = -n mod 4cd   (needs ord_{odd(cd)}(4) | L, and s >= 6 for the 2-part)
// Split: refine one l by one digit; choose l maximising covered fraction of children (ties: smaller l^{e+1}).
// Output stream (text): "S l" | "D q" | "P a d q1 .. qr" (II2) | "I c d q1 .. qr" (I3) | "X" (stuck).
// Usage: z14_tree primes.bin k B A2 A3 NODEMAX maxdepth out.txt [caps l:e,...]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef uint64_t u64; typedef int64_t i64; typedef unsigned __int128 u128;
#define MAXL 128
static u64 pw(u64 b, u64 e, u64 m) { u64 r = 1 % m; b %= m; while (e) { if (e & 1) r = (u128)r * b % m; b = (u128)b * b % m; e >>= 1; } return r; }
static i64 egcd_inv(i64 a, i64 m) { i64 g = m, x = 0, x1 = 1, a1 = a % m; if (a1 < 0) a1 += m; i64 b = a1; while (b) { i64 t = g / b, r = g - t * b; g = b; b = r; i64 y = x - t * x1; x = x1; x1 = y; } if (x < 0) x += m; return x; }
// (x above: inverse of a mod m, valid when gcd = 1)
int nH; u64 HP[MAXL]; int CAP[MAXL]; u64 PW[MAXL][64];
u64 K; int A2, A3;
// primes
int nq; u64 *Qv, *Qo; unsigned char *Qnc; unsigned char (*Qli)[12]; unsigned char (*Qv_)[12];
u64 *G; // g value when active
int **bucket; int *nbucket; // index li*64+e -> primes with v_l(ord) = e (e>=1)
// pairs
typedef struct { int a, d, m; u64 tgt; int nc; unsigned char li[8], v[8]; int ready; u64 w; } Pair; // tgt for II2 = m-1
Pair *P2, *P3; int nP2, nP3;
int **bucket3; int *nbucket3;
// G lists per pair (as stacks)
int *L2len, *L3len; int **L2, **L3; int LMAXG = 64;
// join log
int *jlog; int jlen = 0, jcap = 1 << 24;
int *actlog; int alen = 0;
int e[MAXL]; u64 c[MAXL];
u64 nodes = 0, NODEMAX, leaves = 0, stuck = 0; int maxdepth, curdepth = 0;
double meas = 1.0, covmeas = 0.0; FILE *out;
u64 stuckdepth[512]; u64 leafdepth[512];
// witness
char wit[4096];
int dbgshow = 0;

static int active_ok(int i) { for (int t = 0; t < Qnc[i]; t++) if (Qv_[i][t] > e[Qli[i][t]]) return 0; return 1; }
static u64 mu_mod(int nc, unsigned char *li, unsigned char *v, u64 *modout) {
  u64 x = 0, M = 1;
  for (int t = 0; t < nc; t++) { int l = li[t]; u64 md = PW[l][v[t]]; u64 r = c[l] % md;
    // x mod M, r mod md -> mod M*md
    u64 inv = (u64)egcd_inv((i64)(M % md), (i64)md); u64 h = (u128)((r + md - x % md) % md) * inv % md; x = x + M * h; M *= md; }
  *modout = M; return x;
}
static int subset_hit(int *lst, int n, u64 m, u64 target, u64 newq, u64 *mask) {
  // find subset of lst[0..n-1] with product * newq = target mod m (newq = 0: no new prime; subset nonempty)
  if (n > 18) n = 18;
  u64 base = newq ? newq % m : 1;
  for (u64 s = 0; s < (1ULL << n); s++) {
    if (!newq && !s) continue;
    u64 p = base;
    for (int t = 0; t < n; t++) if (s >> t & 1) p = p * (Qv[lst[t]] % m) % m;
    if (p == target % m) { *mask = s; return 1; }
  }
  return 0;
}
static int wit_list(char *b, int *lst, int n, u64 mask, int extra) {
  int o = 0; for (int t = 0; t < n && t < 64; t++) if (mask >> t & 1) o += sprintf(b + o, " %llu", (unsigned long long)Qv[lst[t]]);
  if (extra >= 0) o += sprintf(b + o, " %llu", (unsigned long long)Qv[extra]);
  return o;
}
static u64 i3target(Pair *p) { // -n mod m
  u64 mw; u64 x = mu_mod(p->nc, p->li, p->v, &mw); // mu mod ord_w(4)
  u64 m = p->m, w = p->w, two = m / w;
  u64 nw = w > 1 ? (pw(4, x, w) + K) % w : 0;
  u64 n2 = K % two;
  // CRT n mod two and mod w
  u64 n;
  if (w == 1) n = n2; else { u64 inv = (u64)egcd_inv((i64)(two % w), (i64)w); u64 h = (u128)((nw + w - n2 % w) % w) * inv % w; n = n2 + two * h; }
  return (m - n % m) % m;
}
// activate prime i; return 1 if leaf found (witness in wit)
// value index: pairs by V = 4a^2 d (CSR)
int *V2s, *V2i, *V3s, *V3i; u64 V2MAX, V3MAX;
static int try2(int j, u64 q, int i) { Pair *p = &P2[j]; if (p->a % q == 0 || p->d % q == 0) return 0;
  u64 mask; if (subset_hit(L2[j], L2len[j], p->m, p->m - 1, q, &mask)) { int o = sprintf(wit, "P %d %d", p->a, p->d); wit_list(wit + o, L2[j], L2len[j], mask, i); return 1; }
  if (L2len[j] < LMAXG) { L2[j][L2len[j]++] = i; jlog[jlen++] = j; } return 0; }
static int try3(int j, u64 q, int i) { Pair *p = &P3[j]; if (p->a % q == 0 || p->d % q == 0) return 0;
  if (p->ready) { u64 mask; if (subset_hit(L3[j], L3len[j], p->m, p->tgt, q, &mask)) { int o = sprintf(wit, "I %d %d", p->a, p->d); wit_list(wit + o, L3[j], L3len[j], mask, i); return 1; } }
  if (L3len[j] < LMAXG) { L3[j][L3len[j]++] = i; jlog[jlen++] = nP2 + j; } return 0; }
static int activate(int i, u64 t4) {  // t4 = 4^mu mod q
  u64 q = Qv[i];
  u64 g = (t4 + K) % q; G[i] = g; actlog[alen++] = i;
  if (g == 0 && K % q) { sprintf(wit, "D %llu", (unsigned long long)q); return 1; }
  u64 v0 = (q - g) % q; if (!v0) v0 = q;
  if (V2MAX / q > (u64)nP2) { for (int j = 0; j < nP2; j++) if ((u128)4 * P2[j].a * P2[j].a % q * P2[j].d % q == v0 % q && try2(j, q, i)) return 1; }
  else for (u64 v = v0; v <= V2MAX; v += q) for (int t = V2s[v]; t < V2s[v + 1]; t++) if (try2(V2i[t], q, i)) return 1;
  u64 g2 = (u128)g * g % q; v0 = (q - g2) % q; if (!v0) v0 = q;
  if (V3MAX / q > (u64)nP3) { for (int j = 0; j < nP3; j++) if ((u128)4 * P3[j].a * P3[j].a % q * P3[j].d % q == v0 % q && try3(j, q, i)) return 1; }
  else for (u64 v = v0; v <= V3MAX; v += q) for (int t = V3s[v]; t < V3s[v + 1]; t++) if (try3(V3i[t], q, i)) return 1;
  return 0;
}
static void undo_to(int j0, int a0) { while (jlen > j0) { int j = jlog[--jlen]; if (j < nP2) L2len[j]--; else L3len[j - nP2]--; } alen = a0; }
// raise e[l] by one (c[l] already set); activate new primes; return 1 if leaf
static int *readylog; int rlen = 0;
// collect primes activated by raising e[l]; T[t] = 4^mu mod q at child 0 (c[l] = base), R[t] = multiplier per child step
static int collect(int l, int *buf, u64 *T, u64 *R) { int n = 0; e[l]++; int bi = l * 64 + e[l]; u64 base = c[l], step = PW[l][e[l] - 1];
  for (int t = 0; t < nbucket[bi]; t++) { int i = bucket[bi][t]; if (!active_ok(i)) continue;
    u64 q = Qv[i], mo; u64 x0 = mu_mod(Qnc[i], Qli[i], Qv_[i], &mo); c[l] = base + step; u64 x1 = mu_mod(Qnc[i], Qli[i], Qv_[i], &mo); c[l] = base;
    T[n] = pw(4, x0, q); R[n] = pw(4, (x1 + mo - x0) % mo, q); buf[n++] = i; }
  e[l]--; return n; }
static int raise_and_test(int l, int *buf, int nb, u64 *T, u64 *R) {
  e[l]++; int hit0 = 0;
  // pairs becoming ready
  int bi = l * 64 + e[l];
  for (int t = 0; t < nbucket3[bi]; t++) { int j = bucket3[bi][t]; Pair *p = &P3[j];
    int ok = 1; for (int s = 0; s < p->nc; s++) if (p->v[s] > e[p->li[s]]) { ok = 0; break; }
    if (!ok || p->ready) continue;
    p->ready = 1; readylog[rlen++] = j; p->tgt = i3target(p);
    u64 mask; if (!hit0 && L3len[j] && subset_hit(L3[j], L3len[j], p->m, p->tgt, 0, &mask)) { int o = sprintf(wit, "I %d %d", p->a, p->d); wit_list(wit + o, L3[j], L3len[j], mask, -1); hit0 = 1; } }
  int hit = hit0;
  for (int t = 0; t < nb; t++) { u64 t4 = T[t]; T[t] = T[t] * R[t] % Qv[buf[t]]; if (!hit && activate(buf[t], t4)) hit = 1; }
  return hit;
}
static void lower(int l, int j0, int a0, int r0) { undo_to(j0, a0); while (rlen > r0) P3[readylog[--rlen]].ready = 0; e[l]--; }
int *cbuf; u64 *cT, *cR;
static void solve(int known) {
  nodes++;
  if (nodes > NODEMAX) { fprintf(stderr, "node budget\n"); fprintf(out, "ABORT\n"); fclose(out); exit(2); }
  if (nodes % 1000000 == 0) fprintf(stderr, "nodes %llu leaves %llu stuck %llu covered %.12f\n", (unsigned long long)nodes, (unsigned long long)leaves, (unsigned long long)stuck, covmeas);
  (void)known;
  int best = -1; double bs = -1; u64 bcost = 0;
  for (int l = 0; l < nH; l++) {
    if (e[l] >= CAP[l]) continue;
    u64 base = c[l], step = PW[l][e[l]]; int k = 0; int nb = collect(l, cbuf, cT, cR);
    for (u64 j = 0; j < HP[l]; j++) { c[l] = base + j * step; int j0 = jlen, a0 = alen, r0 = rlen; k += raise_and_test(l, cbuf, nb, cT, cR); lower(l, j0, a0, r0); }
    c[l] = base;
    if (!k) continue;
    double s = (double)k / HP[l]; u64 cost = PW[l][e[l] + 1];
    if (s > bs + 1e-12 || (s > bs - 1e-12 && cost < bcost)) { bs = s; best = l; bcost = cost; }
  }
  if (best < 0) for (int l = 0; l < nH; l++) if (e[l] < CAP[l]) { u64 cost = PW[l][e[l] + 1]; if (best < 0 || cost < bcost) { best = l; bcost = cost; } }
  if (best < 0 || curdepth >= maxdepth) { fprintf(out, "X\n"); stuck++; stuckdepth[curdepth]++;
    if (dbgshow > 0) { dbgshow--; fprintf(stderr, "stuck:"); for (int l = 0; l < nH; l++) if (e[l]) fprintf(stderr, " %llu^%d:%llu", (unsigned long long)HP[l], e[l], (unsigned long long)c[l]); fprintf(stderr, "\n"); }
    return; }
  fprintf(out, "S %llu\n", (unsigned long long)HP[best]);
  u64 base = c[best], step = PW[best][e[best]]; double om = meas; meas /= HP[best]; curdepth++;
  int *buf = malloc(sizeof(int) * (nq + 1)); u64 *T = malloc(8 * (nq + 1)), *R = malloc(8 * (nq + 1)); int nb = collect(best, buf, T, R);
  for (u64 j = 0; j < HP[best]; j++) {
    c[best] = base + j * step; int j0 = jlen, a0 = alen, r0 = rlen;
    if (raise_and_test(best, buf, nb, T, R)) { fprintf(out, "%s\n", wit); leaves++; leafdepth[curdepth]++; covmeas += meas; }
    else solve(1);
    lower(best, j0, a0, r0);
  }
  free(buf); free(T); free(R); c[best] = base; meas = om; curdepth--;
}
static int lidx(u64 l) { for (int t = 0; t < nH; t++) if (HP[t] == l) return t; return -1; }
int main(int argc, char **argv) {
  if (argc < 9) { fprintf(stderr, "usage\n"); return 1; }
  const char *pf = argv[1]; K = atoll(argv[2]); u64 B = atoll(argv[3]); A2 = atoi(argv[4]); A3 = atoi(argv[5]);
  NODEMAX = atoll(argv[6]); maxdepth = atoi(argv[7]); out = fopen(argv[8], "w");
  if (getenv("SHOWSTUCK")) dbgshow = atoi(getenv("SHOWSTUCK"));
  nH = 0; for (u64 l = 2; l <= B; l++) { int pr = 1; for (u64 d = 2; d * d <= l; d++) if (l % d == 0) pr = 0; if (pr) { HP[nH] = l; CAP[nH] = 1; nH++; } }
  for (int l = 0; l < nH; l++) { PW[l][0] = 1; for (int t = 1; t < 64; t++) PW[l][t] = (PW[l][t - 1] < (1ULL << 40)) ? PW[l][t - 1] * HP[l] : PW[l][t - 1]; }
  CAP[lidx(2)] = 8; CAP[lidx(3)] = 5; if (B >= 5) CAP[lidx(5)] = 3; if (B >= 7) CAP[lidx(7)] = 2; if (B >= 11) CAP[lidx(11)] = 2; if (B >= 13) CAP[lidx(13)] = 2;
  if (argc > 9) { char *s = strdup(argv[9]); for (char *t = strtok(s, ","); t; t = strtok(NULL, ",")) { u64 l; int v; sscanf(t, "%llu:%d", (unsigned long long *)&l, &v); int i = lidx(l); if (i >= 0) CAP[i] = v; } }
  // load primes
  FILE *f = fopen(pf, "rb"); fseek(f, 0, SEEK_END); long sz = ftell(f); fseek(f, 0, SEEK_SET);
  int nall = sz / 8; uint32_t *raw = malloc(sz); fread(raw, 8, nall, f); fclose(f);
  Qv = malloc(8 * nall); Qo = malloc(8 * nall); Qnc = malloc(nall); Qli = malloc(12 * nall); Qv_ = malloc(12 * nall); G = malloc(8 * nall);
  nq = 0;
  for (int i = 0; i < nall; i++) { u64 q = raw[2 * i], o = raw[2 * i + 1];
    if (q == 2) continue;
    u64 y = o; int nc = 0, ok = 1;
    for (int l = 0; l < nH && y > 1; l++) if (y % HP[l] == 0) { int v = 0; while (y % HP[l] == 0) { y /= HP[l]; v++; } if (v > CAP[l] || nc >= 12) { ok = 0; break; } Qli[nq][nc] = l; Qv_[nq][nc] = v; nc++; }
    if (!ok || y > 1) continue;
    Qv[nq] = q; Qo[nq] = o; Qnc[nq] = nc; nq++; }
  free(raw);
  bucket = calloc(MAXL * 64, sizeof(int *)); nbucket = calloc(MAXL * 64, sizeof(int));
  for (int i = 0; i < nq; i++) for (int t = 0; t < Qnc[i]; t++) nbucket[Qli[i][t] * 64 + Qv_[i][t]]++;
  for (int bi = 0; bi < MAXL * 64; bi++) { bucket[bi] = malloc(sizeof(int) * (nbucket[bi] + 1)); nbucket[bi] = 0; }
  for (int i = 0; i < nq; i++) for (int t = 0; t < Qnc[i]; t++) { int bi = Qli[i][t] * 64 + Qv_[i][t]; bucket[bi][nbucket[bi]++] = i; }
  // pairs
  P2 = malloc(sizeof(Pair) * 200000); P3 = malloc(sizeof(Pair) * 200000); nP2 = nP3 = 0;
  for (int a = 1; 4 * a <= A2; a++) for (int d = 1; 4 * a * d <= A2; d++) { Pair *p = &P2[nP2++]; p->a = a; p->d = d; p->m = 4 * a * d; p->tgt = p->m - 1; p->nc = 0; p->ready = 1; }
  bucket3 = calloc(MAXL * 64, sizeof(int *)); nbucket3 = calloc(MAXL * 64, sizeof(int));
  for (int bi = 0; bi < MAXL * 64; bi++) bucket3[bi] = malloc(sizeof(int) * 4096);
  int nroot3 = 0;
  for (int cc = 1; 4 * cc <= A3; cc++) for (int d = 1; 4 * cc * d <= A3; d++) {
    Pair *p = &P3[nP3]; p->a = cc; p->d = d; p->m = 4 * cc * d; u64 w = p->m; while (w % 2 == 0) w /= 2; p->w = w;
    u64 o = 1; if (w > 1) { o = 1; u64 x = 4 % w; while (x != 1) { x = x * 4 % w; o++; } }
    u64 y = o; int nc = 0, ok = 1;
    for (int l = 0; l < nH && y > 1; l++) if (y % HP[l] == 0) { int v = 0; while (y % HP[l] == 0) { y /= HP[l]; v++; } if (v > CAP[l] || nc >= 8) { ok = 0; break; } p->li[nc] = l; p->v[nc] = v; nc++; }
    if (!ok || y > 1) continue;
    p->nc = nc; p->ready = 0;
    if (nc == 0) { p->ready = 2; nroot3++; } else { // bucket on max-index component (any component suffices since we re-check)
      for (int s = 0; s < nc; s++) { int bi = p->li[s] * 64 + p->v[s]; if (nbucket3[bi] < 4096) bucket3[bi][nbucket3[bi]++] = nP3; } }
    nP3++; }
  V2MAX = 0; for (int j = 0; j < nP2; j++) { u64 v = 4ULL * P2[j].a * P2[j].a * P2[j].d; if (v > V2MAX) V2MAX = v; }
  V3MAX = 0; for (int j = 0; j < nP3; j++) { u64 v = 4ULL * P3[j].a * P3[j].a * P3[j].d; if (v > V3MAX) V3MAX = v; }
  V2s = calloc(V2MAX + 2, sizeof(int)); V3s = calloc(V3MAX + 2, sizeof(int)); V2i = malloc(sizeof(int) * nP2); V3i = malloc(sizeof(int) * nP3);
  for (int j = 0; j < nP2; j++) V2s[4ULL * P2[j].a * P2[j].a * P2[j].d + 1]++;
  for (u64 v = 0; v <= V2MAX; v++) V2s[v + 1] += V2s[v];
  { int *pos = malloc(sizeof(int) * (V2MAX + 2)); memcpy(pos, V2s, sizeof(int) * (V2MAX + 2)); for (int j = 0; j < nP2; j++) V2i[pos[4ULL * P2[j].a * P2[j].a * P2[j].d]++] = j; free(pos); }
  for (int j = 0; j < nP3; j++) V3s[4ULL * P3[j].a * P3[j].a * P3[j].d + 1]++;
  for (u64 v = 0; v <= V3MAX; v++) V3s[v + 1] += V3s[v];
  { int *pos = malloc(sizeof(int) * (V3MAX + 2)); memcpy(pos, V3s, sizeof(int) * (V3MAX + 2)); for (int j = 0; j < nP3; j++) V3i[pos[4ULL * P3[j].a * P3[j].a * P3[j].d]++] = j; free(pos); }
  cbuf = malloc(sizeof(int) * (nq + 1)); cT = malloc(8 * (nq + 1)); cR = malloc(8 * (nq + 1));
  L2len = calloc(nP2, sizeof(int)); L3len = calloc(nP3, sizeof(int)); L2 = malloc(sizeof(int *) * nP2); L3 = malloc(sizeof(int *) * nP3);
  for (int j = 0; j < nP2; j++) L2[j] = malloc(sizeof(int) * LMAXG);
  for (int j = 0; j < nP3; j++) L3[j] = malloc(sizeof(int) * LMAXG);
  jlog = malloc(sizeof(int) * jcap); actlog = malloc(sizeof(int) * (nq + 1)); readylog = malloc(sizeof(int) * (nP3 + 1));
  fprintf(stderr, "k=%llu B=%llu: %d split primes, %d active-capable q, %d II2 pairs, %d I3 pairs\n", (unsigned long long)K, (unsigned long long)B, nH, nq, nP2, nP3);
  memset(e, 0, sizeof e); memset(c, 0, sizeof c);
  // root: ready pairs with w-order 1 (w = 1 or w | 3)
  for (int j = 0; j < nP3; j++) if (P3[j].ready == 2) { P3[j].ready = 1; P3[j].tgt = i3target(&P3[j]); }
  // root activation: primes with ord 1
  int rootleaf = 0;
  for (int i = 0; i < nq; i++) if (Qnc[i] == 0) { if (activate(i, 1 % Qv[i])) rootleaf = 1; }
  if (rootleaf) { fprintf(out, "%s\n", wit); fprintf(stderr, "root leaf\n"); return 0; }
  solve(0);
  fclose(out);
  fprintf(stderr, "nodes %llu leaves %llu stuck %llu uncovered measure %.3e\n", (unsigned long long)nodes, (unsigned long long)leaves, (unsigned long long)stuck, 1.0 - covmeas);
  fprintf(stderr, "depth: leaves/stuck:"); for (int d = 0; d <= maxdepth && d < 512; d++) if (leafdepth[d] || stuckdepth[d]) fprintf(stderr, " %d:%llu/%llu", d, (unsigned long long)leafdepth[d], (unsigned long long)stuckdepth[d]);
  fprintf(stderr, "\n");
  return stuck ? 1 : 0;
}
