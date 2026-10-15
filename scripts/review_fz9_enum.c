/* review_fz9_enum.c (R221, from scratch): exact Case B tuple counts over F_q per pattern (s; a, z, y, t), a <= b,
   for FF_STERILE_PUSH (B):  m'wC = T^s + v,  w + C = g'v,  T || w, T || C, T ∤ m'g', v != 0, all monic.
   Independent of fz_enum: own field model F_9 = F_3[α]/(α^2 - α - 1) (fz_enum uses i^2 = -1), own poly code, and two
   routes that use no factoring:
     P: (m', w1) -> v1 ≡ -T^{s-2} (mod m'w1), v1 = -r + M h  (deg M = z + a - 1), C1 = (T^{s-2} div M) + h;
     Q: (m', w1, g') -> v1 = (T^{s-2} + m'w1^2) / (T m'w1 g' - 1)  (exact division required);
     R: (w1, v1 ≡ -T^{s-2} mod w1, g') -> C1 = T g'v1 - w1, m' = (T^{s-2} + v1)/(w1 C1).
   Completeness: every tuple has these data (Lemma 1.1(iii) of FF_STERILE_PUSH: w = Tw1, C = TC1, v = T^2 v1), and the
   data determine the tuple, so each tuple is produced exactly once by each route.  Every candidate is checked against
   (B) itself (rebuilding w, C, v), not against (B1).  Option ALLLC=1: do not fix lc(v1) (enumerate all 8 values).
   usage: review_fz9_enum q SMIN SMAX [route=0 auto|1 P|2 Q|4 R|3 all-three-and-compare] [ALLLC=0] [costcap=99]
   output: "s a z y t count" per pattern; "# level s mass=..." (mass = Σ mult*count*q^{1-ceil(s/2)}).               */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MD 64
typedef struct { int d; int c[MD]; } P;
static int q, p;
static int FA[9][9], FM[9][9], FN[9], FI[9];
static void field(void) {
  if (q == 9) {  /* x = u + 3 w  <-> u + w α,  α^2 = α + 1 */
    p = 3;
    for (int x = 0; x < 9; x++) for (int y = 0; y < 9; y++) {
      int u1 = x % 3, w1 = x / 3, u2 = y % 3, w2 = y / 3;
      FA[x][y] = (u1 + u2) % 3 + 3 * ((w1 + w2) % 3);
      /* (u1 + w1 α)(u2 + w2 α) = u1u2 + (u1w2 + u2w1) α + w1w2 (α + 1) */
      int re = (u1 * u2 + w1 * w2) % 3, im = (u1 * w2 + u2 * w1 + w1 * w2) % 3;
      FM[x][y] = re + 3 * im;
    }
  } else { p = q; for (int x = 0; x < q; x++) for (int y = 0; y < q; y++) { FA[x][y] = (x + y) % q; FM[x][y] = x * y % q; } }
  for (int x = 0; x < q; x++) { FN[x] = -1; FI[x] = -1; for (int y = 0; y < q; y++) { if (FA[x][y] == 0) FN[x] = y; if (FM[x][y] == 1) FI[x] = y; } }
  /* axioms */
  for (int x = 0; x < q; x++) { if (FN[x] < 0 || (x && FI[x] < 0)) { fprintf(stderr, "field fail\n"); exit(2); }
    for (int y = 0; y < q; y++) for (int z = 0; z < q; z++) {
      if (FM[FM[x][y]][z] != FM[x][FM[y][z]] || FA[FA[x][y]][z] != FA[x][FA[y][z]] || FM[x][FA[y][z]] != FA[FM[x][y]][FM[x][z]] || FM[x][y] != FM[y][x]) { fprintf(stderr, "axiom fail\n"); exit(2); } } }
}
static void nrm(P *a) { while (a->d >= 0 && a->c[a->d] == 0) a->d--; }
static void add(P *r, const P *a, const P *b) { P t; t.d = a->d > b->d ? a->d : b->d; for (int i = 0; i <= t.d; i++) t.c[i] = FA[i <= a->d ? a->c[i] : 0][i <= b->d ? b->c[i] : 0]; nrm(&t); *r = t; }
static void sub(P *r, const P *a, const P *b) { P t; t.d = a->d > b->d ? a->d : b->d; for (int i = 0; i <= t.d; i++) t.c[i] = FA[i <= a->d ? a->c[i] : 0][FN[i <= b->d ? b->c[i] : 0]]; nrm(&t); *r = t; }
static void mul(P *r, const P *a, const P *b) { P t; if (a->d < 0 || b->d < 0) { r->d = -1; return; } t.d = a->d + b->d; if (t.d >= MD) { fprintf(stderr, "MD\n"); exit(2); }
  for (int i = 0; i <= t.d; i++) t.c[i] = 0;
  for (int i = 0; i <= a->d; i++) if (a->c[i]) for (int j = 0; j <= b->d; j++) t.c[i + j] = FA[t.c[i + j]][FM[a->c[i]][b->c[j]]]; nrm(&t); *r = t; }
/* division by b with arbitrary nonzero lc */
static void dm(P *qq, P *rr, const P *a, const P *b) { P r = *a, Qt; int il = FI[b->c[b->d]]; Qt.d = a->d - b->d; if (Qt.d < 0) Qt.d = -1; for (int i = 0; i <= Qt.d; i++) Qt.c[i] = 0;
  while (r.d >= b->d && r.d >= 0) { int f = FM[r.c[r.d]][il], sh = r.d - b->d; Qt.c[sh] = f; for (int i = 0; i <= b->d; i++) r.c[sh + i] = FA[r.c[sh + i]][FN[FM[f][b->c[i]]]]; if (r.c[r.d] != 0) { fprintf(stderr, "div\n"); exit(2); } nrm(&r); }
  nrm(&Qt); if (qq) *qq = Qt; if (rr) *rr = r; }
static int eq(const P *a, const P *b) { if (a->d != b->d) return 0; for (int i = 0; i <= a->d; i++) if (a->c[i] != b->c[i]) return 0; return 1; }
static void shT(P *r, const P *a, int k) { P t; if (a->d < 0) { r->d = -1; return; } t.d = a->d + k; for (int i = 0; i < k; i++) t.c[i] = 0; for (int i = 0; i <= a->d; i++) t.c[i + k] = a->c[i]; *r = t; }
/* monic, deg d, nonzero const term (d>0); iterate */
static void first_monic(P *a, int d) { a->d = d; for (int i = 0; i <= d; i++) a->c[i] = 0; a->c[d] = 1; if (d > 0) a->c[0] = 1; }
static int next_monic(P *a) { int d = a->d; if (d == 0) return 0; for (int i = 0; i < d; i++) { int x = a->c[i] + 1; if (x < q) { a->c[i] = x; return 1; } a->c[i] = (i == 0) ? 1 : 0; } return 0; }
/* deg d, lc fixed (lc), arbitrary other coeffs (incl. const 0) */
static void first_lc(P *a, int d, int lc) { a->d = d; for (int i = 0; i < d; i++) a->c[i] = 0; a->c[d] = lc; }
static int next_lc(P *a) { int d = a->d; for (int i = 0; i < d; i++) { int x = a->c[i] + 1; if (x < q) { a->c[i] = x; return 1; } a->c[i] = 0; } return 0; }

static int s, A, Z, Y, Tt, B; static P TS, TS2, ONE, TT;
/* full (B) check from (m', g', w1, C1, v1) */
static int checkB(const P *m, const P *g, const P *w1, const P *C1, const P *v1) {
  P w, C, v, x, y;
  shT(&w, w1, 1); shT(&C, C1, 1); shT(&v, v1, 2);
  if (m->d != Z || g->d != Y || w.d != A || C.d != B || v.d != Tt) return 0;
  if (m->c[m->d] != 1 || g->c[g->d] != 1 || w.c[w.d] != 1 || C.c[C.d] != 1) return 0;
  if (m->c[0] == 0 || g->c[0] == 0) return 0;               /* T ∤ m'g' */
  if (w.c[1] == 0 || C.c[1] == 0) return 0;                 /* T || w, T || C (w.c[0] = 0 by construction) */
  if (v.d < 0) return 0;
  mul(&x, m, &w); mul(&x, &x, &C); add(&y, &TS, &v); if (!eq(&x, &y)) return 0;
  add(&x, &w, &C); mul(&y, g, &v); if (!eq(&x, &y)) return 0;
  return 1;
}
static int ALLLC = 0, LC;
static long routeP(void) {   /* (m', w1) -> v1 class mod M -> C1 */
  long cnt = 0; P m, w1, M, K, r, v1, C1, sm, tv, g, rr, h, nr;
  first_monic(&m, Z);
  do { first_monic(&w1, A - 1);
    do {
      mul(&M, &m, &w1); dm(&K, &r, &TS2, &M); sub(&nr, &(P){-1}, &r);   /* nr = -r */
      int hd = Tt - 2 - M.d;
      if (hd < 0) {
        v1 = nr; if (v1.d != Tt - 2) continue;
        sub(&C1, &K, &(P){-1});   /* C1 = K (h = 0) */
        add(&sm, &w1, &C1); shT(&tv, &v1, 1); dm(&g, &rr, &sm, &tv); if (rr.d >= 0) continue;
        cnt += checkB(&m, &g, &w1, &C1, &v1);
      } else {
        for (int lc = 1; lc < q; lc++) { if (!ALLLC && lc != LC) continue;
          first_lc(&h, hd, lc);
          do { P Mh; mul(&Mh, &M, &h); add(&v1, &nr, &Mh); add(&C1, &K, &h);
               add(&sm, &w1, &C1); shT(&tv, &v1, 1); if (tv.d < 0) continue; dm(&g, &rr, &sm, &tv); if (rr.d >= 0) continue;
               cnt += checkB(&m, &g, &w1, &C1, &v1); } while (next_lc(&h));
        }
      }
    } while (next_monic(&w1));
  } while (next_monic(&m));
  return cnt;
}
static long routeQ(void) {   /* (m', w1, g') -> v1 = (T^{s-2} + m'w1^2)/(T m'w1 g' - 1) */
  long cnt = 0; P m, w1, g, N, D, v1, rr, C1, x;
  first_monic(&m, Z);
  do { first_monic(&w1, A - 1);
    do { mul(&N, &w1, &w1); mul(&N, &N, &m); add(&N, &N, &TS2);
      first_monic(&g, Y);
      do { mul(&D, &m, &w1); mul(&D, &D, &g); shT(&D, &D, 1); sub(&D, &D, &ONE);
           dm(&v1, &rr, &N, &D); if (rr.d >= 0 || v1.d < 0) continue;
           mul(&x, &g, &v1); shT(&x, &x, 1); sub(&C1, &x, &w1);
           cnt += checkB(&m, &g, &w1, &C1, &v1);
      } while (next_monic(&g));
    } while (next_monic(&w1));
  } while (next_monic(&m));
  return cnt;
}
static long routeR(void) {   /* (w1, v1 ≡ -T^{s-2} mod w1, g') -> C1 = T g'v1 - w1, m' = (T^{s-2} + v1)/(w1 C1) */
  long cnt = 0; P m, w1, g, v1, r, nr, h, x, C1, F, wc, rr;
  first_monic(&w1, A - 1);
  do { dm(NULL, &r, &TS2, &w1); sub(&nr, &(P){-1}, &r); int hd = Tt - 2 - w1.d;
    for (int lc = 1; lc < q; lc++) {
      if (hd < 0) { if (lc > 1) break; h.d = -1; } else { if (!ALLLC && lc != LC) continue; first_lc(&h, hd, lc); }
      do { P wh; mul(&wh, &w1, &h); add(&v1, &nr, &wh); if (v1.d != Tt - 2) continue;
           add(&F, &TS2, &v1);
           first_monic(&g, Y);
           do { mul(&x, &g, &v1); shT(&x, &x, 1); sub(&C1, &x, &w1); mul(&wc, &w1, &C1); if (wc.d < 0) continue;
                dm(&m, &rr, &F, &wc); if (rr.d >= 0) continue;
                cnt += checkB(&m, &g, &w1, &C1, &v1);
           } while (next_monic(&g));
      } while (hd >= 0 && next_lc(&h));
    }
  } while (next_monic(&w1));
  return cnt;
}
int main(int argc, char **argv) {
  q = atoi(argv[1]); int s0 = atoi(argv[2]), s1 = atoi(argv[3]); int route = argc > 4 ? atoi(argv[4]) : 0; ALLLC = argc > 5 ? atoi(argv[5]) : 0;
  double cap = argc > 6 ? atof(argv[6]) : 99;
  field(); ONE.d = 0; ONE.c[0] = 1; TT.d = 1; TT.c[0] = 0; TT.c[1] = 1;
  for (s = s0; s <= s1; s++) {
    TS.d = s; for (int i = 0; i < s; i++) TS.c[i] = 0; TS.c[s] = 1; shT(&TS2, &ONE, s - 2);
    double mass = 0, w8 = pow(q, 1 - (s + 1) / 2); long ntup = 0;
    for (A = 1; A < s; A++) for (Z = 0; A + Z < s; Z++) { B = s - A - Z; if (B < A) continue;
      for (Y = 0; Y <= B - 2; Y++) { Tt = B - Y; LC = A < B ? 1 : FA[1][1];
        double nst = (Z ? Z * log(q) + log(1 - 1.0 / q) : 0) + (A - 1 ? (A - 1) * log(q) + log(1 - 1.0 / q) : 0);
        double cP = nst + fmax(0, Tt - 2 - (Z + A - 1)) * log(q) + (ALLLC ? log(q - 1) : 0);
        double cQ = nst + (Y ? Y * log(q) + log(1 - 1.0 / q) : 0);
        double cR = (A - 1 ? (A - 1) * log(q) + log(1 - 1.0 / q) : 0) + (Y ? Y * log(q) + log(1 - 1.0 / q) : 0) + fmax(0, Tt - 2 - (A - 1)) * log(q) + (ALLLC ? log(q - 1) : 0);
        int r = route ? route : (cP <= cQ && cP <= cR ? 1 : cQ <= cR ? 2 : 4);
        if (fmin(fmin(cP, cQ), cR) / log(q) > cap) { printf("%d %d %d %d %d SKIP\n", s, A, Z, Y, Tt); continue; }
        long n;
        if (r == 3) { long n1 = routeP(), n2 = routeQ(), n3 = routeR(); if (n1 != n2 || n1 != n3) { fprintf(stderr, "MISMATCH s=%d %d %d %d %d: P=%ld Q=%ld R=%ld\n", s, A, Z, Y, Tt, n1, n2, n3); return 1; } n = n1; }
        else n = r == 1 ? routeP() : r == 2 ? routeQ() : routeR();
        printf("%d %d %d %d %d %ld\n", s, A, Z, Y, Tt, n); fflush(stdout);
        ntup += n; mass += (A == B ? 1 : 2) * n * w8;
      } }
    printf("# level %d tuples=%ld mass=%.10e\n", s, ntup, mass); fflush(stdout);
  }
  return 0;
}
