/* review_fs_count.c (R217, from scratch): exact enumeration of Case B tuples (B) over F_p (p prime, odd):
     m' w C = T^s + v,  w + C = g' v,  T || w, T || C, T not| m' g', v != 0,  m', g', w, C monic.
   Enumeration by (m', g', w = T w1): E = m'g'w - 1 must divide g'T^s + w (DEPTH_ASPECT Lemma 2.1 (R3)), C := quotient;
   then (B) is re-checked literally. Prints per-pattern counts "P s a z y t count" (a = deg w, unnormalised: both orders
   appear) and per-s totals, and the exact sum  sum_s count(s) / p^{ceil(s/2) - 1}  (k = 2, relative c-slice units,
   summed over all c) as a fraction with denominator p^{ceil(smax/2)-1}.
   Also asserts Lemma 1.1: E v = T^s + m' w^2 and y + t = max(a, b).
   usage: review_fs_count p smax */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MD 64
static int p;
typedef struct { int d; int c[MD]; } P;   /* d = degree (-1 for zero) */
static void norm(P *a) { while (a->d >= 0 && a->c[a->d] == 0) a->d--; }
static void pmul(const P *a, const P *b, P *r) {
  P t; memset(&t, 0, sizeof t);
  if (a->d < 0 || b->d < 0) { t.d = -1; *r = t; return; }
  t.d = a->d + b->d;
  for (int i = 0; i <= a->d; i++) if (a->c[i]) for (int j = 0; j <= b->d; j++) t.c[i + j] = (t.c[i + j] + a->c[i] * b->c[j]) % p;
  norm(&t); *r = t;
}
static void padd(const P *a, const P *b, int sb, P *r) {   /* a + sb*b */
  P t; memset(&t, 0, sizeof t); t.d = a->d > b->d ? a->d : b->d;
  for (int i = 0; i <= t.d; i++) { int x = i <= a->d ? a->c[i] : 0, y = i <= b->d ? b->c[i] : 0; t.c[i] = ((x + sb * y) % p + p) % p; }
  norm(&t); *r = t;
}
/* divide a by monic m; returns 1 if exact, quotient in q */
static int pdiv(const P *a, const P *m, P *q) {
  P r = *a; P Q; memset(&Q, 0, sizeof Q);
  if (r.d < m->d) { if (r.d < 0) { Q.d = -1; *q = Q; return 1; } return 0; }
  Q.d = r.d - m->d;
  for (int i = r.d; i >= m->d; i--) {
    int c = r.c[i];
    if (c) { Q.c[i - m->d] = c; for (int j = 0; j <= m->d; j++) r.c[i - m->d + j] = ((r.c[i - m->d + j] - c * m->c[j]) % p + p) % p; }
  }
  norm(&r); *q = Q; return r.d < 0;
}
/* iterate monic polys of degree d with nonzero constant term (if d >= 1) via counter */
static int first(P *f, int d) { memset(f, 0, sizeof *f); f->d = d; f->c[d] = 1; if (d >= 1) f->c[0] = 1; return 1; }
static int next(P *f) {
  int d = f->d; if (d == 0) return 0;
  /* c[0] in 1..p-1, c[1..d-1] in 0..p-1 */
  if (f->c[0] < p - 1) { f->c[0]++; return 1; }
  f->c[0] = 1;
  for (int i = 1; i < d; i++) { if (f->c[i] < p - 1) { f->c[i]++; return 1; } f->c[i] = 0; }
  return 0;
}
int main(int argc, char **argv) {
  p = atoi(argv[1]); int smax = atoi(argv[2]);
  /* exact sum: numerator over p^{E0}, E0 = ceil(smax/2) - 1 */
  int E0 = (smax + 1) / 2 - 1; long double dummy = 0; (void)dummy;
  unsigned long long num = 0;  /* sum count(s) * p^{E0 - (ceil(s/2)-1)} ; fits for the sizes used */
  for (int s = 3; s <= smax; s++) {
    long cnt = 0;
    P Ts; memset(&Ts, 0, sizeof Ts); Ts.d = s; Ts.c[s] = 1;
    for (int a = 1; a < s; a++) for (int z = 0; a + z < s; z++) {
      int b = s - a - z; int mx = a > b ? a : b;
      for (int y = 0; y <= mx - 2; y++) {
        long pc = 0;
        P mp, gp, w1;
        first(&mp, z);
        do {
          first(&gp, y);
          do {
            P L; pmul(&mp, &gp, &L);
            P gT; pmul(&gp, &Ts, &gT);
            first(&w1, a - 1);
            do {
              P w; memset(&w, 0, sizeof w); w.d = a; for (int i = 0; i < a; i++) w.c[i + 1] = w1.c[i];
              P E, one; memset(&one, 0, sizeof one); one.d = 0; one.c[0] = 1;
              pmul(&L, &w, &E); padd(&E, &one, -1, &E);
              P numr; padd(&gT, &w, 1, &numr);
              P C; if (!pdiv(&numr, &E, &C)) continue;
              if (C.d != b || C.c[b] != 1) { fprintf(stderr, "degree/lc anomaly\n"); return 2; }
              if (C.c[0] != 0 || C.c[1] == 0) continue;               /* T || C */
              P mw, mwC, v; pmul(&mp, &w, &mw); pmul(&mw, &C, &mwC); padd(&mwC, &Ts, -1, &v);
              if (v.d < 0) continue;
              P gv, wC; pmul(&gp, &v, &gv); padd(&w, &C, 1, &wC);
              if (gv.d != wC.d || memcmp(gv.c, wC.c, sizeof(int) * (gv.d + 1))) continue;
              /* Lemma 1.1 checks */
              P Ev, ww, mww, rhs; pmul(&E, &v, &Ev); pmul(&w, &w, &ww); pmul(&mp, &ww, &mww); padd(&Ts, &mww, 1, &rhs);
              if (Ev.d != rhs.d || memcmp(Ev.c, rhs.c, sizeof(int) * (Ev.d + 1))) { fprintf(stderr, "Ev identity FAILS\n"); return 3; }
              if (y + v.d != mx) { fprintf(stderr, "y+t identity FAILS\n"); return 4; }
              if (v.c[0] || v.c[1] || !v.c[2]) { fprintf(stderr, "T^2||v FAILS\n"); return 5; }
              pc++;
              /* per-pattern record uses t = deg v */
              if (pc == 1) {}
              { static int lastkey[5] = {-1}; (void)lastkey; }
              printf("P %d %d %d %d %d\n", s, a, z, y, v.d);
            } while (next(&w1));
          } while (next(&gp));
        } while (next(&mp));
        cnt += pc;
      }
    }
    unsigned long long w8 = 1; for (int i = 0; i < E0 - ((s + 1) / 2 - 1); i++) w8 *= p;
    num += (unsigned long long)cnt * w8;
    fprintf(stderr, "p=%d s=%d count=%ld\n", p, s, cnt);
    printf("S %d %ld\n", s, cnt);
  }
  printf("SUM numerator=%llu denominator=%d^%d\n", num, p, E0);
  return 0;
}
