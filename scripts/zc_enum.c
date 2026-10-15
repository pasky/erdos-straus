/* fz1_enum.c (O220): k = 1 version of fz_enum.c — exact counts of the tuples (B^{k=1}) of FF_STERILE_SMALL §6:
   m'wC = T^s + v, w + C = g'v, all monic, T not dividing m'g'wCv, deg w = a <= b = deg C, z = deg m', y = deg g', t = deg v.
   Same eight routes with w1 -> w, C1 -> C, v1 -> v, T^{s-2} -> T^s and the modulus T v1 -> v.
   Original header: fz_enum.c (O220): exact counts of Case B tuples (FF_STERILE_PUSH (B)) per pattern (s; a, z, y, t), a <= b, over
   F_q, q in {3, 5, 7, 9} (F_9 = F_3[i]/(i^2+1)), via loss-free reconstructions (FF_STERILE_SMALL §5):
   M2: C1 (deg b-1) -> v1 = -(T^{s-2} mod C1), K = m'w1 = T^{s-2} div C1; then w1 = sigma + T v1 h (w1 = -C1 mod T v1)
       or m' | K, whichever is cheaper;
   M3: w1 (deg a-1), v1 in the class -T^{s-2} mod w1; K' = m'C1; then C1 = -w1 + T v1 h' or m' | K';
   M5: (m', g', v1 in class mod m'): w1, C1 = roots of X^2 - T g' v1 X + (T^{s-2}+v1)/m'.
   Every candidate is checked against the full definition: m', w1, C1, g' monic, nonzero constant terms, exact degrees,
   m' w1 C1 = T^{s-2} + v1, w1 + C1 = T g' v1, deg v1 = t - 2, lc(v1) = lc(w + C).
   Counts ordered tuples with deg w = a <= b = deg C (a = b: both orders).
   usage: fz_enum q SMIN SMAX logq_cap [method=0 auto|2|3|5|11|12|13|14|16] [usefactor=1] [FOV=3]   prints "s a z y t count method" or "s a z y t SKIP cost" */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXD 160
typedef unsigned char u8;
typedef struct { int d; u8 c[MAXD]; } poly;
static int Q, PCH;
static u8 ADD[27][27], MUL[27][27], NEG[27], INV[27];
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
  } else if (q == 27) {   /* F_27 = F_3[x]/(x^3 - x - 1); element c0 + 3 c1 + 9 c2 */
    PCH = 3;
    for (int x = 0; x < 27; x++) for (int y = 0; y < 27; y++) {
      int a[3] = {x % 3, x / 3 % 3, x / 9}, b[3] = {y % 3, y / 3 % 3, y / 9}, p[5] = {0};
      ADD[x][y] = (a[0] + b[0]) % 3 + 3 * ((a[1] + b[1]) % 3) + 9 * ((a[2] + b[2]) % 3);
      for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) p[i + j] += a[i] * b[j];
      for (int k = 4; k >= 3; k--) { p[k - 2] += p[k]; p[k - 3] += p[k]; p[k] = 0; }   /* x^3 = x + 1 */
      MUL[x][y] = p[0] % 3 + 3 * (p[1] % 3) + 9 * (p[2] % 3);
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
static int S_, A_, Z_, Y_, T_, B_, LC; static int SLICEF = 0; static int DUMP = 0; static int PATF = 0; static int ZC_LO = -1, ZC_ZO, ZC_YO;   /* zc: env ZC_ONLY="a z y" runs one pattern */
/* zc (O226): eps of FF_ODD_ABSENCE Thm 1.2; PATF = 1 keeps only patterns with 4 | s and eps = (-1)^{s/4} */
static int zc_eps_ok(int s, int a, int z, int t) { int b = s - a - z, e = (t + t * z + z * (1 + s) + t * s) & 1; if (a == b && ((z + s) & 1)) e ^= 1; if (s % 4) return 0; return e == ((s / 4) & 1); }
/* full check of a candidate (m', w1, C1, v1); g' computed. returns 1 if valid tuple of the pattern */
static int check(const poly *m, const poly *w1, const poly *C1, const poly *v1) {
  if (m->d != Z_ || w1->d != A_ || C1->d != B_ || v1->d != T_) return 0;
  if (m->c[m->d] != 1 || w1->c[w1->d] != 1 || C1->c[C1->d] != 1 || v1->c[v1->d] != LC) return 0;
  if (!m->c[0] || !w1->c[0] || !C1->c[0] || !v1->c[0]) return 0;
  poly p, f; pmul(&p, m, w1); pmul(&p, &p, C1); padd(&f, &TS2, v1); if (!peq(&p, &f)) return 0;
  poly sm, g, rm; padd(&sm, w1, C1); pdivmod(&g, &rm, &sm, v1);
  if (rm.d >= 0 || g.d != Y_ || g.c[g.d] != 1 || !g.c[0]) return 0;
  if (SLICEF) {   /* FF_STERILE_SMALL §7: only tuples whose cylinder lies in a slice u0 = -E(0) outside F_3^*: E(0) not in F_3 */
    int e0 = MUL[MUL[m->c[0]][g.c[0]]][w1->c[0]]; e0 = ADD[e0][NEG[1]];
    if (e0 == 0 || e0 == 1 || e0 == ADD[1][1]) return 0;
    if (SLICEF == 2) { int p4 = MUL[MUL[e0][e0]][MUL[e0][e0]]; if (p4 == 1) return 0; }   /* zc (O226): q = 9 primitive slices only */
  }
  if (DUMP) { /* zc (O226): dump tuple: s a z y t | E0 | m' | w | C | g' | v  (coefficients low->high, field codes) */
    int e0 = ADD[MUL[MUL[m->c[0]][g.c[0]]][w1->c[0]]][NEG[1]];
    printf("T %d %d %d %d %d E0 %d |", S_, A_, Z_, Y_, T_, e0);
    const poly *L[5] = {m, w1, C1, &g, v1};
    for (int k = 0; k < 5; k++) { printf(" "); for (int i = 0; i <= L[k]->d; i++) printf("%d%s", L[k]->c[i], i < L[k]->d ? "," : ""); }
    printf("\n");
  }
  return 1;
}
static double lgq; static int USEF = 1;
static double cost2(void) { return B_ + fmin(Z_, fmax(0, A_ - T_)); }
static double cost3(void) { return A_ + fmax(0, T_ - A_) + fmin(Y_, Z_); }
static double cost5(void) { return Z_ + Y_ + fmax(0, T_ - Z_); }
/* enumerate monic polys of degree d with nonzero constant term: callback via loop macro */
static long run2(void) {
  long cnt = 0; poly C1; C1.d = B_; memset(C1.c, 0, MAXD); C1.c[B_] = 1; if (B_ > 0) C1.c[0] = 1;
  do {
    poly K, R, v1; pdivmod(&K, &R, &TS2, &C1); pscal(&v1, &R, NEG[1]);
    if (B_ <= T_) {   /* k = 1, y = 0: deg C = t does not determine v; v = r0 + LC*C (Lemma 1.3), K = (T^s + v)/C */
      poly lcC, F2, rr; pscal(&lcC, &C1, LC); padd(&v1, &v1, &lcC); padd(&F2, &TS2, &v1); pdivmod(&K, &rr, &F2, &C1); if (rr.d >= 0) continue; }
    if (v1.d != T_ || v1.c[v1.d] != LC || !v1.c[0]) continue;
    poly M; pshift(&M, &v1, 0);                          /* T v1, deg t-1 */
    if (Z_ <= (A_ - T_ > 0 ? A_ - T_ : 0)) {           /* enumerate m' | K */
      poly m; m.d = Z_; memset(m.c, 0, MAXD); m.c[Z_] = 1; if (Z_ > 0) m.c[0] = 1;
      do { poly w1, rr; pdivmod(&w1, &rr, &K, &m); if (rr.d >= 0) continue; cnt += check(&m, &w1, &C1, &v1);
      } while (Z_ > 0 && odo(m.c, 0, Z_, 1));
    } else {                                             /* w1 = sigma + M h */
      poly sig, nC; pscal(&nC, &C1, NEG[1]); pdivmod(NULL, &sig, &nC, &M);
      if (A_ < T_) { if (sig.d == A_) { poly m, rr; pdivmod(&m, &rr, &K, &sig); if (rr.d < 0) cnt += check(&m, &sig, &C1, &v1); } }
      else {
        int hd = A_ - T_; poly h; h.d = hd; memset(h.c, 0, MAXD); h.c[hd] = INV[LC];
        do { poly w1, Mh, m, rr; pmul(&Mh, &M, &h); padd(&w1, &sig, &Mh); pdivmod(&m, &rr, &K, &w1); if (rr.d >= 0) continue;
             cnt += check(&m, &w1, &C1, &v1); } while (hd > 0 && odo(h.c, 0, hd, 0));
      }
    }
  } while (B_ > 0 && odo(C1.c, 0, B_, 1));
  return cnt;
}
static long run3(void) {
  long cnt = 0; poly w1; w1.d = A_; memset(w1.c, 0, MAXD); w1.c[A_] = 1; if (A_ > 0) w1.c[0] = 1;
  do {
    poly R; pdivmod(NULL, &R, &TS2, &w1); poly r0; pscal(&r0, &R, NEG[1]);   /* v1 = r0 + w1 h */
    int hd = T_ - (A_);
    poly h; if (hd >= 0) { h.d = hd; memset(h.c, 0, MAXD); h.c[hd] = LC; }
    do {
      poly v1; if (hd >= 0) { poly wh; pmul(&wh, &w1, &h); padd(&v1, &r0, &wh); } else v1 = r0;
      if (v1.d != T_ || v1.c[v1.d] != LC || !v1.c[0]) continue;
      poly F, Kp, rr; padd(&F, &TS2, &v1); pdivmod(&Kp, &rr, &F, &w1); if (rr.d >= 0) continue;
      if (Z_ <= Y_) {
        poly m; m.d = Z_; memset(m.c, 0, MAXD); m.c[Z_] = 1; if (Z_ > 0) m.c[0] = 1;
        do { poly C1, r2; pdivmod(&C1, &r2, &Kp, &m); if (r2.d >= 0) continue; cnt += check(&m, &w1, &C1, &v1);
        } while (Z_ > 0 && odo(m.c, 0, Z_, 1));
      } else {
        poly M, nw, sig; pshift(&M, &v1, 0); pscal(&nw, &w1, NEG[1]); pdivmod(NULL, &sig, &nw, &M);
        int kd = B_ - T_; poly k; k.d = kd; memset(k.c, 0, MAXD); k.c[kd] = INV[LC];
        do { poly C1, Mk, m, r2; pmul(&Mk, &M, &k); padd(&C1, &sig, &Mk); pdivmod(&m, &r2, &Kp, &C1); if (r2.d >= 0) continue;
             cnt += check(&m, &w1, &C1, &v1); } while (kd > 0 && odo(k.c, 0, kd, 0));
      }
    } while (hd > 0 && odo(h.c, 0, hd, 0));
  } while (A_ > 0 && odo(w1.c, 0, A_, 1));
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
    int hd = T_ - Z_; poly h; if (hd >= 0) { h.d = hd; memset(h.c, 0, MAXD); h.c[hd] = LC; }
    do {
      poly v1; if (hd >= 0) { poly mh; pmul(&mh, &m, &h); padd(&v1, &r0, &mh); } else v1 = r0;
      if (v1.d != T_ || v1.c[v1.d] != LC || !v1.c[0]) continue;
      poly F, G, rr; padd(&F, &TS2, &v1); pdivmod(&G, &rr, &F, &m); if (rr.d >= 0) continue;
      poly g; g.d = Y_; memset(g.c, 0, MAXD); g.c[Y_] = 1; if (Y_ > 0) g.c[0] = 1;
      do {
        poly Sm, tv, D, S2, G4, Rt; pshift(&tv, &v1, 0); pmul(&Sm, &g, &tv); pmul(&S2, &Sm, &Sm);
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
/* ---------- factoring over F_q (squarefree + distinct-degree + Cantor-Zassenhaus), FF_STERILE_SMALL §5 ---------- */
static void pmonic(poly *a) { if (a->d >= 0 && a->c[a->d] != 1) pscal(a, a, INV[a->c[a->d]]); }
static void pgcd(poly *r, const poly *a, const poly *b) {
  poly x = *a, y = *b;
  while (y.d >= 0) { poly rr; pdivmod(NULL, &rr, &x, &y); x = y; y = rr; }
  pmonic(&x); *r = x;
}
static void pderiv(poly *r, const poly *a) {
  poly t; t.d = a->d - 1; if (t.d < 0) { r->d = -1; return; }
  for (int i = 1; i <= a->d; i++) { int c = 0; for (int k = 0; k < i % PCH; k++) c = ADD[c][a->c[i]]; t.c[i - 1] = c; }
  norm(&t); *r = t;
}
static void pmulmod(poly *r, const poly *a, const poly *b, const poly *m) { poly t; pmul(&t, a, b); pdivmod(NULL, r, &t, m); }
static void ppowmod(poly *r, const poly *a, unsigned long e, const poly *m) {
  poly res, base; res.d = 0; res.c[0] = 1; pdivmod(NULL, &base, a, m);
  while (e) { if (e & 1) pmulmod(&res, &res, &base, m); e >>= 1; if (e) pmulmod(&base, &base, &base, m); }
  pdivmod(NULL, r, &res, m);
}
static int PROOT[27];   /* p-th root in F_q: x^{q/p} */
#define MAXF 128
typedef struct { poly f[MAXF]; int e[MAXF]; int n; } fact;
static unsigned long long rng = 88172645463325252ULL;
static unsigned long long xr(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }
static void addfac(fact *F, const poly *p, int e) {
  for (int i = 0; i < F->n; i++) if (peq(&F->f[i], p)) { F->e[i] += e; return; }
  if (F->n >= MAXF) { fprintf(stderr, "MAXF\n"); exit(3); }
  F->f[F->n] = *p; F->e[F->n] = e; F->n++;
}
static void edf(fact *F, const poly *g, int d, int e) {
  if (g->d <= d) { if (g->d > 0) addfac(F, g, e); return; }
  for (;;) {
    poly a; a.d = g->d - 1; for (int i = 0; i <= a.d; i++) a.c[i] = xr() % Q; norm(&a); if (a.d < 1) continue;
    poly c, x, pr; ppowmod(&c, &a, (Q - 1) / 2, g); x = c; pr = c;
    for (int i = 1; i < d; i++) { ppowmod(&x, &x, Q, g); pmulmod(&pr, &pr, &x, g); }
    poly one; one.d = 0; one.c[0] = 1; psub(&pr, &pr, &one); poly h; pgcd(&h, &pr, g);
    if (h.d > 0 && h.d < g->d) { poly h2; pdivmod(&h2, NULL, g, &h); pmonic(&h2); edf(F, &h, d, e); edf(F, &h2, d, e); return; }
  }
}
static void ddf(fact *F, const poly *g0, int e) {
  poly g = *g0, h, X; X.d = 1; X.c[0] = 0; X.c[1] = 1; h = X;
  for (int d = 1; 2 * d <= g.d; d++) {
    ppowmod(&h, &h, Q, &g); poly hx, gd; psub(&hx, &h, &X); pgcd(&gd, &hx, &g);
    if (gd.d > 0) { edf(F, &gd, d, e); poly t; pdivmod(&t, NULL, &g, &gd); g = t; pmonic(&g); pdivmod(NULL, &h, &h, &g); }
  }
  if (g.d > 0) addfac(F, &g, e);
}
static void sqf(fact *F, const poly *f0, int mult) {   /* f0 monic */
  poly f = *f0; if (f.d <= 0) return;
  poly df; pderiv(&df, &f);
  if (df.d < 0) {    /* f = g^p */
    poly g; g.d = f.d / PCH; for (int i = 0; i <= g.d; i++) g.c[i] = PROOT[f.c[i * PCH]]; sqf(F, &g, mult * PCH); return;
  }
  poly c, w; pgcd(&c, &f, &df); pdivmod(&w, NULL, &f, &c); int i = 1;
  while (w.d > 0) {
    poly y, fac; pgcd(&y, &w, &c); pdivmod(&fac, NULL, &w, &y);
    if (fac.d > 0) ddf(F, &fac, i * mult);
    w = y; poly t; pdivmod(&t, NULL, &c, &y); c = t; i++;
  }
  if (c.d > 0) { poly g; g.d = c.d / PCH; for (int k = 0; k <= g.d; k++) g.c[k] = PROOT[c.c[k * PCH]]; sqf(F, &g, mult * PCH); }
}
static int SELFCHECK = 1;
/* Rabin irreducibility test: f monic of degree d >= 1 */
static int irreducible(const poly *f) {
  int d = f->d; if (d == 1) return 1;
  poly X, h; X.d = 1; X.c[0] = 0; X.c[1] = 1;
  for (int p = 2; p <= d; p++) if (d % p == 0) { int isp = 1; for (int u = 2; u * u <= p; u++) if (p % u == 0) isp = 0; if (!isp) continue;
    h = X; for (int i = 0; i < d / p; i++) ppowmod(&h, &h, Q, f); poly hx, g; psub(&hx, &h, &X); pgcd(&g, &hx, f); if (g.d != 0) return 0; }
  h = X; for (int i = 0; i < d; i++) ppowmod(&h, &h, Q, f); poly hx; psub(&hx, &h, &X); pdivmod(NULL, &hx, &hx, f); return hx.d < 0;
}
static void factor(fact *F, const poly *f) {
  F->n = 0; poly g = *f; pmonic(&g); sqf(F, &g, 1);
  if (SELFCHECK) {   /* fail closed: product must reproduce f, every factor irreducible and monic, factors distinct */
    poly p; p.d = 0; p.c[0] = 1;
    for (int i = 0; i < F->n; i++) { if (F->f[i].c[F->f[i].d] != 1 || !irreducible(&F->f[i])) { fprintf(stderr, "FACTOR CHECK FAILED (irreducible)\n"); exit(4); }
      for (int j = 0; j < i; j++) if (peq(&F->f[i], &F->f[j])) { fprintf(stderr, "FACTOR CHECK FAILED (dup)\n"); exit(4); }
      for (int k = 0; k < F->e[i]; k++) pmul(&p, &p, &F->f[i]); }
    if (!peq(&p, &g)) { fprintf(stderr, "FACTOR CHECK FAILED (product)\n"); exit(4); }
  }
}
/* enumerate divisors of degree D (monic) of the factored poly, with optional exponent caps; callback */
typedef void (*dcb)(const poly *);
static fact *DF; static int DEX[MAXF]; static dcb DCB; static int DTARGET; static int DREM[MAXF + 1];
static void dfs(int i, const poly *cur) {
  if (cur->d == DTARGET) { DCB(cur); return; }
  if (i >= DF->n || cur->d + DREM[i] < DTARGET) return;
  poly p = *cur; int dd = DF->f[i].d;
  for (int k = 0; k <= DF->e[i] && p.d <= DTARGET; k++) {
    DEX[i] = k; dfs(i + 1, &p);
    if (p.d + dd > DTARGET) break;
    pmul(&p, &p, &DF->f[i]);
  }
  DEX[i] = 0;
}
static void divisors(fact *F, int D, dcb cb) {
  DF = F; DCB = cb; DTARGET = D; DREM[F->n] = 0;
  for (int i = F->n - 1; i >= 0; i--) DREM[i] = DREM[i + 1] + F->f[i].d * F->e[i];
  poly one; one.d = 0; one.c[0] = 1; dfs(0, &one);
}
/* ---- factoring routes ---- */
static long FCNT; static poly G_m, G_w1, G_v1, G_g, G_F, G_mod; static int G_mode;
static int congr(const poly *E, const poly *M, int val) {   /* E == val (mod M) ? */
  if (M->d == 0) return 1;                                     /* k = 1: the modulus may be a unit */
  poly r, cst; pdivmod(NULL, &r, E, M); cst.d = 0; cst.c[0] = val; norm(&cst); return peq(&r, &cst);
}
static void cb_E(const poly *E) {   /* E candidate: E == -1 mod G_mod, reconstruct by mode */
  if (!congr(E, &G_mod, NEG[1])) return;
  poly one, Ep1, rr; one.d = 0; one.c[0] = 1; padd(&Ep1, E, &one);
  if (G_mode == 2) {            /* (m', g'): L' = m'g', w = (E+1)/L', C = (g'T^s + w)/E */
    poly L, w, w1, C, C1, gts, num, v1, prod, TS2v;
    pmul(&L, &G_m, &G_g); pdivmod(&w, &rr, &Ep1, &L); if (rr.d >= 0) return; w1 = w;   /* k = 1: L'w = E + 1 */
    pshift(&gts, &G_g, S_); padd(&num, &gts, &w); pdivmod(&C, &rr, &num, E); if (rr.d >= 0) return; C1 = C;
    pmul(&prod, &G_m, &w1); pmul(&prod, &prod, &C1); psub(&v1, &prod, &TS2); (void)TS2v;
    FCNT += check(&G_m, &w1, &C1, &v1);
  } else if (G_mode == 3) {     /* (w1, g'): L' = (E+1)/(T w1), m' = L'/g', C1 = F/E */
    poly Tw, L, m, C1, v1, prod; pshift(&Tw, &G_w1, 0); pdivmod(&L, &rr, &Ep1, &Tw); if (rr.d >= 0) return;
    pdivmod(&m, &rr, &L, &G_g); if (rr.d >= 0) return; pdivmod(&C1, &rr, &G_F, E); if (rr.d >= 0) return;
    pmul(&prod, &m, &G_w1); pmul(&prod, &prod, &C1); psub(&v1, &prod, &TS2);
    FCNT += check(&m, &G_w1, &C1, &v1);
  } else if (G_mode == 4) {     /* (m', w1): v1 = F/E, C1 = (T^{s-2}+v1)/(m'w1) */
    poly v1, f2, mw, C1; pdivmod(&v1, &rr, &G_F, E); if (rr.d >= 0) return;
    padd(&f2, &TS2, &v1); pmul(&mw, &G_m, &G_w1); pdivmod(&C1, &rr, &f2, &mw); if (rr.d >= 0) return;
    FCNT += check(&G_m, &G_w1, &C1, &v1);
  }
}
static void cb_w1(const poly *w1) {   /* mode 1: G_F = w1 C1 (given m', v1) */
  poly C1, rr; pdivmod(&C1, &rr, &G_F, w1); if (rr.d >= 0) return; FCNT += check(&G_m, w1, &C1, &G_v1);
}
static void cb_C1(const poly *C1) {   /* mode 5: G_F = m' C1 (given w1, v1) */
  { poly sm, r; padd(&sm, C1, &G_w1); pdivmod(NULL, &r, &sm, &G_mod); if (r.d >= 0) return; }   /* C1 == -w1 mod T v1 */
  poly m, rr; pdivmod(&m, &rr, &G_F, C1); if (rr.d >= 0) return; FCNT += check(&m, &G_w1, C1, &G_v1);
}
/* iterate monic polys of degree d with nonzero constant term */
#define FOR_MONIC(P, D) for (int _f = (P.d = (D), memset(P.c, 0, MAXD), P.c[D] = 1, (D) > 0 ? (P.c[0] = 1) : 0, 1); _f; _f = ((D) > 0 && odo(P.c, 0, (D), 1)))
static long runF(int mode) {
  FCNT = 0; fact F; G_mode = mode;
  if (mode == 2) {            /* (m', g'): E | 1 + T^s m' g'^2, deg a+y+z, E == -1 mod T L' */
    poly m, g; FOR_MONIC(m, Z_) FOR_MONIC(g, Y_) {
      poly gg, D, one, L; pmul(&gg, &g, &g); pmul(&gg, &gg, &m); pshift(&D, &gg, S_); one.d = 0; one.c[0] = 1; padd(&D, &D, &one);
      G_m = m; G_g = g; pmul(&L, &m, &g); pshift(&G_mod, &L, 0); factor(&F, &D); divisors(&F, A_ + Y_ + Z_, cb_E);
    }
  } else if (mode == 3) {     /* (w1, g'): E | g' T^{s-1} + w1, E == -1 mod T w1 g' */
    poly w1, g; FOR_MONIC(w1, A_) FOR_MONIC(g, Y_) {
      poly D, L; pshift(&D, &g, S_); padd(&D, &D, &w1); G_w1 = w1; G_g = g; G_F = D;
      pmul(&L, &w1, &g); pshift(&G_mod, &L, 0); factor(&F, &D); divisors(&F, A_ + Y_ + Z_, cb_E);
    }
  } else if (mode == 4) {     /* (m', w1): E | T^{s-2} + m' w1^2, E == -1 mod T m' w1 */
    poly m, w1; FOR_MONIC(m, Z_) FOR_MONIC(w1, A_) {
      poly D, L; pmul(&D, &w1, &w1); pmul(&D, &D, &m); padd(&D, &D, &TS2); G_m = m; G_w1 = w1; G_F = D;
      pmul(&L, &m, &w1); pshift(&G_mod, &L, 0); factor(&F, &D); divisors(&F, A_ + Y_ + Z_, cb_E);
    }
  } else if (mode == 1) {     /* (m', v1 in class mod m'): G = w1 C1 = (T^{s-2}+v1)/m', w1 | G */
    poly m; FOR_MONIC(m, Z_) {
      poly R, r0; pdivmod(NULL, &R, &TS2, &m); pscal(&r0, &R, NEG[1]);
      int hd = T_ - Z_; poly h; if (hd >= 0) { h.d = hd; memset(h.c, 0, MAXD); h.c[hd] = LC; }
      do {
        poly v1; if (hd >= 0) { poly mh; pmul(&mh, &m, &h); padd(&v1, &r0, &mh); } else v1 = r0;
        if (v1.d != T_ || v1.c[v1.d] != LC || !v1.c[0]) continue;
        poly Fp, G, rr; padd(&Fp, &TS2, &v1); pdivmod(&G, &rr, &Fp, &m); if (rr.d >= 0) continue;
        G_m = m; G_v1 = v1; G_F = G; factor(&F, &G); divisors(&F, A_, cb_w1);
      } while (hd > 0 && odo(h.c, 0, hd, 0));
    }
  } else if (mode == 6) {     /* (w1, v1 in class mod w1): K' = m' C1, C1 | K', C1 == -w1 mod T v1 */
    poly w1; FOR_MONIC(w1, A_) {
      poly R, r0; pdivmod(NULL, &R, &TS2, &w1); pscal(&r0, &R, NEG[1]);
      int hd = T_ - (A_); poly h; if (hd >= 0) { h.d = hd; memset(h.c, 0, MAXD); h.c[hd] = LC; }
      do {
        poly v1; if (hd >= 0) { poly wh; pmul(&wh, &w1, &h); padd(&v1, &r0, &wh); } else v1 = r0;
        if (v1.d != T_ || v1.c[v1.d] != LC || !v1.c[0]) continue;
        poly Fp, K, rr; padd(&Fp, &TS2, &v1); pdivmod(&K, &rr, &Fp, &w1); if (rr.d >= 0) continue;
        G_w1 = w1; G_v1 = v1; G_F = K; pshift(&G_mod, &v1, 0); factor(&F, &K); divisors(&F, B_, cb_C1);
      } while (hd > 0 && odo(h.c, 0, hd, 0));
    }
  }
  return FCNT;
}
static double FOV = 3.0;   /* factoring overhead, log_q units */
static double costF(int mode) {
  switch (mode) {
    case 1: return Z_ + fmax(0, T_ - Z_) + FOV;
    case 2: return Y_ + Z_ + FOV;
    case 3: return A_ + Y_ + FOV;
    case 4: return Z_ + A_ + FOV;
    case 6: return A_ + fmax(0, T_ - A_) + FOV;
  }
  return 1e9;
}
int main(int argc, char **argv) {
  int q = atoi(argv[1]); if (q != 3 && q != 5 && q != 7 && q != 9 && q != 27) { fprintf(stderr, "q unsupported\n"); return 2; } int s0 = atoi(argv[2]), s1 = atoi(argv[3]); double cap = atof(argv[4]); int meth = argc > 5 ? atoi(argv[5]) : 0; USEF = argc > 6 ? atoi(argv[6]) : 1; if (argc > 7) FOV = atof(argv[7]); if (argc > 8) SLICEF = atoi(argv[8]); if (argc > 9) DUMP = atoi(argv[9]); if (argc > 10) PATF = atoi(argv[10]);
  field_init(q); lgq = log(q); if (getenv("ZC_ONLY")) sscanf(getenv("ZC_ONLY"), "%d %d %d", &ZC_LO, &ZC_ZO, &ZC_YO);
  for (int x = 0; x < q; x++) for (int y = 0; y < q; y++) { int p = 1; for (int k = 0; k < PCH; k++) p = MUL[p][y]; if (p == x) PROOT[x] = y; }
  for (int s = s0; s <= s1; s++) {
    S_ = s; TS2.d = s; memset(TS2.c, 0, MAXD); TS2.c[s] = 1;
    for (int a = 0; a <= s; a++) for (int z = 0; a + z <= s; z++) {
      int b = s - a - z; if (b < a) continue;
      for (int y = 0; y <= b; y++) {
        int t = b - y; if (PATF && !zc_eps_ok(s, a, z, t)) continue; if (ZC_LO >= 0 && (a != ZC_LO || z != ZC_ZO || y != ZC_YO)) continue; A_ = a; Z_ = z; Y_ = y; T_ = t; B_ = b; LC = (a < b) ? 1 : ADD[1][1];
        /* methods: 2, 3, 5 (candidate search); 11, 12, 13, 14, 16 (factoring: modes 1, 2, 3, 4, 6) */
        int ms[8] = {2, 3, 5, 11, 12, 13, 14, 16}; double cs[8] = {cost2(), cost3(), cost5(), costF(1), costF(2), costF(3), costF(4), costF(6)};
        int m = meth; double c = 1e9;
        for (int i = 0; i < 8; i++) { if (meth && ms[i] != meth) continue; if (!meth && !USEF && ms[i] > 10) continue; if (cs[i] < c) { c = cs[i]; m = ms[i]; } }
        if (c > cap) { printf("%d %d %d %d %d SKIP %.1f\n", s, a, z, y, t, c); continue; }
        long n = m == 2 ? run2() : m == 3 ? run3() : m == 5 ? run5() : runF(m - 10);
        printf("%d %d %d %d %d %ld M%d\n", s, a, z, y, t, n, m); fflush(stdout);
      }
    }
  }
  return 0;
}
