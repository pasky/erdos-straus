/* fz_enum.c (O220): exact counts of Case B tuples (FF_STERILE_PUSH (B)) per pattern (s; a, z, y, t), a <= b, over
   F_q, q in {3, 5, 7, 9} (F_9 = F_3[i]/(i^2+1)), via loss-free reconstructions (FF_STERILE_SMALL §5):
   M2: C1 (deg b-1) -> v1 = -(T^{s-2} mod C1), K = m'w1 = T^{s-2} div C1; then w1 = sigma + T v1 h (w1 = -C1 mod T v1)
       or m' | K, whichever is cheaper;
   M3: w1 (deg a-1), v1 in the class -T^{s-2} mod w1; K' = m'C1; then C1 = -w1 + T v1 h' or m' | K';
   M5: (m', g', v1 in class mod m'): w1, C1 = roots of X^2 - T g' v1 X + (T^{s-2}+v1)/m'.
   Every candidate is checked against the full definition: m', w1, C1, g' monic, nonzero constant terms, exact degrees,
   m' w1 C1 = T^{s-2} + v1, w1 + C1 = T g' v1, deg v1 = t - 2, lc(v1) = lc(w + C).
   Counts ordered tuples with deg w = a <= b = deg C (a = b: both orders).
   usage: fz_enum q SMIN SMAX logq_cap [method=0 auto|2|3|5]   prints "s a z y t count method" or "s a z y t SKIP cost" */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXD 160
typedef unsigned char u8;
typedef struct { int d; u8 c[MAXD]; } poly;
static int Q, PCH;
static u8 ADD[9][9], MUL[9][9], NEG[9], INV[9];
static void field_init(int q) {
  Q = q;
  if (q == 9) {
    PCH = 3;
    for (int x = 0; x < 9; x++) for (int y = 0; y < 9; y++) {
      int a1 = x % 3, b1 = x / 3, a2 = y % 3, b2 = y / 3;
      ADD[x][y] = (a1 + a2) % 3 + 3 * ((b1 + b2) % 3);
      int re = ((a1 * a2 - b1 * b2) % 3 + 3) % 3, im = (a1 * b2 + a2 * b1) % 3;   /* i^2 = -1 */
      MUL[x][y] = re + 3 * im;
    }
  } else {
    PCH = q;
    for (int x = 0; x < q; x++) for (int y = 0; y < q; y++) { ADD[x][y] = (x + y) % q; MUL[x][y] = (x * y) % q; }
  }
  for (int x = 0; x < q; x++) for (int y = 0; y < q; y++) { if (ADD[x][y] == 0) NEG[x] = y; if (MUL[x][y] == 1) INV[x] = y; }
}
static void norm(poly *a) { while (a->d >= 0 && a->c[a->d] == 0) a->d--; }
static void padd(poly *r, const poly *a, const poly *b) {
  int d = a->d > b->d ? a->d : b->d; poly t; t.d = d;
  for (int i = 0; i <= d; i++) t.c[i] = ADD[i <= a->d ? a->c[i] : 0][i <= b->d ? b->c[i] : 0];
  norm(&t); *r = t;
}
static void psub(poly *r, const poly *a, const poly *b) {
  int d = a->d > b->d ? a->d : b->d; poly t; t.d = d;
  for (int i = 0; i <= d; i++) t.c[i] = ADD[i <= a->d ? a->c[i] : 0][NEG[i <= b->d ? b->c[i] : 0]];
  norm(&t); *r = t;
}
static void pmul(poly *r, const poly *a, const poly *b) {
  poly t; if (a->d < 0 || b->d < 0) { r->d = -1; return; }
  t.d = a->d + b->d; memset(t.c, 0, t.d + 1);
  for (int i = 0; i <= a->d; i++) if (a->c[i]) for (int j = 0; j <= b->d; j++) t.c[i + j] = ADD[t.c[i + j]][MUL[a->c[i]][b->c[j]]];
  norm(&t); *r = t;
}
/* quo, rem of a by b (b != 0) */
static void pdivmod(poly *quo, poly *rem, const poly *a, const poly *b) {
  poly r = *a, qq; int il = INV[b->c[b->d]];
  qq.d = a->d - b->d; if (qq.d < 0) qq.d = -1; else memset(qq.c, 0, qq.d + 1);
  while (r.d >= b->d) {
    int f = MUL[r.c[r.d]][il], sft = r.d - b->d; qq.c[sft] = f;
    for (int i = 0; i <= b->d; i++) r.c[sft + i] = ADD[r.c[sft + i]][NEG[MUL[f][b->c[i]]]];
    norm(&r);
  }
  norm(&qq); if (quo) *quo = qq; if (rem) *rem = r;
}
static void pscal(poly *r, const poly *a, int c) { *r = *a; for (int i = 0; i <= r->d; i++) r->c[i] = MUL[c][r->c[i]]; norm(r); }
static void pshift(poly *r, const poly *a, int k) { poly t; if (a->d < 0) { r->d = -1; return; } t.d = a->d + k; memset(t.c, 0, k); memcpy(t.c + k, a->c, a->d + 1); *r = t; }
static int peq(const poly *a, const poly *b) { return a->d == b->d && !memcmp(a->c, b->c, a->d + 1); }
/* odometer over coefficient vectors c[lo..hi-1] in F_q, with c[lo] restricted to nonzero if nz0 */
static int odo(u8 *c, int lo, int hi, int nz0) {
  for (int i = lo; i < hi; i++) {
    int x = c[i] + 1;
    if (x < Q) { c[i] = x; return 1; }
    c[i] = (i == lo && nz0) ? 1 : 0;
  }
  return 0;
}
static poly TS2;     /* T^{s-2} */
static int S_, A_, Z_, Y_, T_, B_, LC;
/* full check of a candidate (m', w1, C1, v1); g' computed. returns 1 if valid tuple of the pattern */
static int check(const poly *m, const poly *w1, const poly *C1, const poly *v1) {
  if (m->d != Z_ || w1->d != A_ - 1 || C1->d != B_ - 1 || v1->d != T_ - 2) return 0;
  if (m->c[m->d] != 1 || w1->c[w1->d] != 1 || C1->c[C1->d] != 1 || v1->c[v1->d] != LC) return 0;
  if (!m->c[0] || !w1->c[0] || !C1->c[0] || !v1->c[0]) return 0;
  poly p, f; pmul(&p, m, w1); pmul(&p, &p, C1); padd(&f, &TS2, v1); if (!peq(&p, &f)) return 0;
  poly sm, tv, g, rm; padd(&sm, w1, C1); pshift(&tv, v1, 1); pdivmod(&g, &rm, &sm, &tv);
  if (rm.d >= 0 || g.d != Y_ || g.c[g.d] != 1 || !g.c[0]) return 0;
  return 1;
}
static double lgq;
static double cost2(void) { return (B_ - 1) + fmin(Z_, fmax(0, A_ - T_)); }
static double cost3(void) { return (A_ - 1) + fmax(0, T_ - 1 - A_) + fmin(Y_, Z_); }
static double cost5(void) { return Z_ + Y_ + fmax(0, T_ - 2 - Z_); }
/* enumerate monic polys of degree d with nonzero constant term: callback via loop macro */
static long run2(void) {
  long cnt = 0; poly C1; C1.d = B_ - 1; memset(C1.c, 0, MAXD); C1.c[B_ - 1] = 1; if (B_ - 1 > 0) C1.c[0] = 1;
  do {
    poly K, R, v1; pdivmod(&K, &R, &TS2, &C1); pscal(&v1, &R, NEG[1]);
    if (v1.d != T_ - 2 || v1.c[v1.d] != LC || !v1.c[0]) continue;
    poly M; pshift(&M, &v1, 1);                          /* T v1, deg t-1 */
    if (Z_ <= (A_ - T_ > 0 ? A_ - T_ : 0)) {           /* enumerate m' | K */
      poly m; m.d = Z_; memset(m.c, 0, MAXD); m.c[Z_] = 1; if (Z_ > 0) m.c[0] = 1;
      do { poly w1, rr; pdivmod(&w1, &rr, &K, &m); if (rr.d >= 0) continue; cnt += check(&m, &w1, &C1, &v1);
      } while (Z_ > 0 && odo(m.c, 0, Z_, 1));
    } else {                                             /* w1 = sigma + M h */
      poly sig, nC; pscal(&nC, &C1, NEG[1]); pdivmod(NULL, &sig, &nC, &M);
      if (A_ - 1 < T_ - 1) { if (sig.d == A_ - 1) { poly m, rr; pdivmod(&m, &rr, &K, &sig); if (rr.d < 0) cnt += check(&m, &sig, &C1, &v1); } }
      else {
        int hd = A_ - T_; poly h; h.d = hd; memset(h.c, 0, MAXD); h.c[hd] = INV[LC];
        do { poly w1, Mh, m, rr; pmul(&Mh, &M, &h); padd(&w1, &sig, &Mh); pdivmod(&m, &rr, &K, &w1); if (rr.d >= 0) continue;
             cnt += check(&m, &w1, &C1, &v1); } while (hd > 0 && odo(h.c, 0, hd, 0));
      }
    }
  } while (B_ - 1 > 0 && odo(C1.c, 0, B_ - 1, 1));
  return cnt;
}
static long run3(void) {
  long cnt = 0; poly w1; w1.d = A_ - 1; memset(w1.c, 0, MAXD); w1.c[A_ - 1] = 1; if (A_ - 1 > 0) w1.c[0] = 1;
  do {
    poly R; pdivmod(NULL, &R, &TS2, &w1); poly r0; pscal(&r0, &R, NEG[1]);   /* v1 = r0 + w1 h */
    int hd = T_ - 2 - (A_ - 1);
    poly h; if (hd >= 0) { h.d = hd; memset(h.c, 0, MAXD); h.c[hd] = LC; }
    do {
      poly v1; if (hd >= 0) { poly wh; pmul(&wh, &w1, &h); padd(&v1, &r0, &wh); } else v1 = r0;
      if (v1.d != T_ - 2 || v1.c[v1.d] != LC || !v1.c[0]) continue;
      poly F, Kp, rr; padd(&F, &TS2, &v1); pdivmod(&Kp, &rr, &F, &w1); if (rr.d >= 0) continue;
      if (Z_ <= Y_) {
        poly m; m.d = Z_; memset(m.c, 0, MAXD); m.c[Z_] = 1; if (Z_ > 0) m.c[0] = 1;
        do { poly C1, r2; pdivmod(&C1, &r2, &Kp, &m); if (r2.d >= 0) continue; cnt += check(&m, &w1, &C1, &v1);
        } while (Z_ > 0 && odo(m.c, 0, Z_, 1));
      } else {
        poly M, nw, sig; pshift(&M, &v1, 1); pscal(&nw, &w1, NEG[1]); pdivmod(NULL, &sig, &nw, &M);
        int kd = B_ - T_; poly k; k.d = kd; memset(k.c, 0, MAXD); k.c[kd] = INV[LC];
        do { poly C1, Mk, m, r2; pmul(&Mk, &M, &k); padd(&C1, &sig, &Mk); pdivmod(&m, &r2, &Kp, &C1); if (r2.d >= 0) continue;
             cnt += check(&m, &w1, &C1, &v1); } while (kd > 0 && odo(k.c, 0, kd, 0));
      }
    } while (hd > 0 && odo(h.c, 0, hd, 0));
  } while (A_ - 1 > 0 && odo(w1.c, 0, A_ - 1, 1));
  return cnt;
}
/* square root of a polynomial D (deg even, or D = 0): returns number of roots found (0 or 1), R with R^2 = D */
static int psqrt(poly *R, const poly *D) {
  if (D->d < 0) { R->d = -1; return 1; }
  if (D->d % 2) return 0;
  int n = D->d / 2, l = -1;
  for (int x = 1; x < Q; x++) if (MUL[x][x] == D->c[D->d]) { l = x; break; }
  if (l < 0) return 0;
  R->d = n; memset(R->c, 0, n + 1); R->c[n] = l; int i2l = INV[ADD[l][l]];
  for (int k = 1; k <= n; k++) {     /* coefficient of T^{2n-k}: 2 l R_{n-k} + sum_{i+j = 2n-k, n-k < i,j <= n} R_i R_j */
    int sum = 0;
    for (int i = n - k + 1; i <= n; i++) { int j = 2 * n - k - i; if (j > n - k && j <= n) sum = ADD[sum][MUL[R->c[i]][R->c[j]]]; }
    R->c[n - k] = MUL[ADD[D->c[2 * n - k]][NEG[sum]]][i2l];
  }
  poly sq; pmul(&sq, R, R); return peq(&sq, D);
}
static long run5(void) {
  long cnt = 0; poly m; m.d = Z_; memset(m.c, 0, MAXD); m.c[Z_] = 1; if (Z_ > 0) m.c[0] = 1;
  int i2 = INV[ADD[1][1]];
  do {
    poly R; pdivmod(NULL, &R, &TS2, &m); poly r0; pscal(&r0, &R, NEG[1]);
    int hd = T_ - 2 - Z_; poly h; if (hd >= 0) { h.d = hd; memset(h.c, 0, MAXD); h.c[hd] = LC; }
    do {
      poly v1; if (hd >= 0) { poly mh; pmul(&mh, &m, &h); padd(&v1, &r0, &mh); } else v1 = r0;
      if (v1.d != T_ - 2 || v1.c[v1.d] != LC || !v1.c[0]) continue;
      poly F, G, rr; padd(&F, &TS2, &v1); pdivmod(&G, &rr, &F, &m); if (rr.d >= 0) continue;
      poly g; g.d = Y_; memset(g.c, 0, MAXD); g.c[Y_] = 1; if (Y_ > 0) g.c[0] = 1;
      do {
        poly Sm, tv, D, S2, G4, Rt; pshift(&tv, &v1, 1); pmul(&Sm, &g, &tv); pmul(&S2, &Sm, &Sm);
        pscal(&G4, &G, ADD[ADD[1][1]][ADD[1][1]]); psub(&D, &S2, &G4);
        if (!psqrt(&Rt, &D)) continue;
        for (int sg = 0; sg < 2; sg++) {
          if (sg == 1 && Rt.d < 0) break;                    /* double root counted once */
          poly x, w1, C1; if (sg == 0) padd(&x, &Sm, &Rt); else psub(&x, &Sm, &Rt);
          pscal(&w1, &x, i2); psub(&C1, &Sm, &w1);
          cnt += check(&m, &w1, &C1, &v1);
        }
      } while (Y_ > 0 && odo(g.c, 0, Y_, 1));
    } while (hd > 0 && odo(h.c, 0, hd, 0));
  } while (Z_ > 0 && odo(m.c, 0, Z_, 1));
  return cnt;
}
int main(int argc, char **argv) {
  int q = atoi(argv[1]), s0 = atoi(argv[2]), s1 = atoi(argv[3]); double cap = atof(argv[4]); int meth = argc > 5 ? atoi(argv[5]) : 0;
  field_init(q); lgq = log(q);
  for (int s = s0; s <= s1; s++) {
    S_ = s; TS2.d = s - 2; memset(TS2.c, 0, MAXD); TS2.c[s - 2] = 1;
    for (int a = 1; a < s; a++) for (int z = 0; a + z < s; z++) {
      int b = s - a - z; if (b < a) continue;
      for (int y = 0; y <= b - 2; y++) {
        int t = b - y; A_ = a; Z_ = z; Y_ = y; T_ = t; B_ = b; LC = (a < b) ? 1 : ADD[1][1];
        double c2 = cost2(), c3 = cost3(), c5 = cost5(); int m = meth;
        if (!m) { m = 2; double c = c2; if (c3 < c) { c = c3; m = 3; } if (c5 < c) { c = c5; m = 5; } }
        double c = m == 2 ? c2 : m == 3 ? c3 : c5;
        if (c > cap) { printf("%d %d %d %d %d SKIP %.1f\n", s, a, z, y, t, c); continue; }
        long n = m == 2 ? run2() : m == 3 ? run3() : run5();
        printf("%d %d %d %d %d %ld M%d\n", s, a, z, y, t, n, m); fflush(stdout);
      }
    }
  }
  return 0;
}
