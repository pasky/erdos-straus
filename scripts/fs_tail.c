/* fs_tail.c (O216): rigorous tail bound for the Case B union-bound sum, s > S, for q = 3^r.
   Normalised pattern p = (al, ze, ps, ta) = (a, z, y, t)/s, al + ze + ps + ta = 1, be = ps + ta >= al.
   Adaptive dyadic boxes in (al, ze, ps); on each box, every route of FF_STERILE_PUSH Lemma 1.6 is bounded by
       count <= M(s) * kappa * exp(s * phi_plus)
   (phi_plus an upper bound of the route's per-unit-s log over the box, valid for every integer pattern with s >= S
   whose normalisation lies in the box; class-count conditions are checked uniformly for s >= S, including the integer
   shifts of n, d, rho). The box contributes  sum_{s > S} P_B(s) * 2 * min_route [...] * q^{1 - s/2}  where
   P_B(s) = prod (floor(s*width) + 1) bounds the number of integer patterns of level s in the box.
   usage: fs_tail r S [minwidth_log2=9] [eps-target]   prints the total tail bound (relative c-slice units). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static double lq;
static long SMIN;
typedef struct { double lo, hi; } I;
static I box[3]; static I tau, be;
/* linear form value per unit s: c0 + ca*al + cz*ze + cy*ps + ct*ta ; integer shift sh */
static I lf(double c0, double ca, double cz, double cy, double ct) {
  I r = {c0, c0}; double c[4] = {ca, cz, cy, ct}; I v[4] = {box[0], box[1], box[2], tau};
  for (int i = 0; i < 4; i++) { if (c[i] >= 0) { r.lo += c[i] * v[i].lo; r.hi += c[i] * v[i].hi; } else { r.lo += c[i] * v[i].hi; r.hi += c[i] * v[i].lo; } }
  return r;
}
static double xlx(double x) { return x <= 0 ? 0 : x * log(x); }
/* upper bound of B(d,e) = (d+e)log(d+e) - d log d - e log e, increasing in d and e */
static double Bup(I d, I e) { double D = d.hi > 0 ? d.hi : 0, E = e.hi > 0 ? e.hi : 0; return xlx(D + E) - xlx(D) - xlx(E) + 1e-12; }
static double Gup(I x, I y, I z) { double X = x.hi > 0 ? x.hi : 0, Y = y.hi > 0 ? y.hi : 0, Z = z.hi > 0 ? z.hi : 0;
  return xlx(X + Y + Z) - xlx(X) - xlx(Y) - xlx(Z) + 1e-12; }
/* class-count bound valid on the whole box for all s >= SMIN.
   n = s*N + n0, d = s*D + d0, rho = s*R + r0 (forms N, D, R as intervals per unit s). returns kappa or 0 */
static int cls_box(I N, double n0, I D, double d0, I R, double r0, int both) {
  /* trivial: d < rho  <=>  s(D - R) + (d0 - r0) < 0 for all s >= SMIN */
  double hi = D.hi - R.lo, c = d0 - r0;
  if (hi <= 0 && hi * SMIN + c < 0) return 1;
  if (both) { double hi2 = (N.hi - D.lo) - R.lo, c2 = (n0 - d0) - r0; if (hi2 <= 0 && hi2 * SMIN + c2 < 0) return 1; }
  int best = 0;
  /* Lenstra: 3 rho - n > 0 */
  { double lo = 3 * R.lo - N.hi, c3 = 3 * r0 - n0; if (lo >= 0 && lo * SMIN + c3 > 0) best = 2; }
  /* Coppersmith: A n + B (d - rho) - M d < 0 with A = m(m+1)/2, B = m(m+1)/2 + km + k(k+1)/2, M = (m+k+1) m.
     Also need d >= rho (else trivial case, handled) -- the lemma needs rho <= d; if d < rho somewhere in the box
     the count is 1 there anyway, so the bound max(1, m+k) is valid. Cofactor version: d -> n - d. */
  for (int ver = 0; ver < (both ? 2 : 1); ver++) {
    I Dv = D; double dv0 = d0;
    if (ver == 1) { Dv.lo = N.lo - D.hi; Dv.hi = N.hi - D.lo; dv0 = n0 - d0; }
    for (long m = 1; m <= 40; m++) for (long k = 0; k <= 160; k++) {
      double A = m * (m + 1) / 2.0, B = m * (m + 1) / 2.0 + k * m + k * (k + 1) / 2.0, M = (double)(m + k + 1) * m;
      /* coefficient form: A n + (B - M) d - B rho ; maximise over box: n at hi, d at lo if B-M<0, rho at lo */
      double coefD = B - M;
      double hiL = A * N.hi + (coefD >= 0 ? coefD * Dv.hi : coefD * Dv.lo) - B * R.lo;
      double c0 = A * n0 + coefD * dv0 - B * r0;
      if (hiL < 0 && hiL * SMIN + c0 < 0) { if (!best || m + k < best) best = (int)(m + k); break; }
    }
  }
  return best;
}
/* route evaluation on the current box: returns phi_plus (nats per unit s) and the s-dependent prefactor type */
typedef struct { double phi; double logk; int polys; } RB;   /* count <= exp(s*phi + logk) * (s+1)^polys */
static int nr;
static RB R[32];
static void add(double phi, double logk, int polys) { R[nr].phi = phi; R[nr].logk = logk; R[nr].polys = polys; nr++; }
static void classroute(double base, I N, double n0, I D, double d0, I Rr, double r0, int both, double binom, double logk0, int polys) {
  int kap = cls_box(N, n0, D, d0, Rr, r0, both);
  add(base + binom, logk0, polys);
  if (kap) add(base, logk0 + log((double)kap), polys);
}
static void routes(void) {
  nr = 0;
  I al = box[0], ze = box[1], ps = box[2], ta = tau;
  I one = {1, 1};
  double L = lq;
  /* q-power exponents (upper bounds, per unit s, N*(d) <= q^d) */
  double Wa = lf(0, 1, 0, 0, 0).hi * L, Wb = lf(0, 0, 0, 1, 1).hi * L, Z = ze.hi * L, Y = ps.hi * L, V = ta.hi * L;
  add(Z + Y + Wa, 0, 0);                 /* T0 */
  add(Z + Wa + V, 0, 0);                 /* R4' */
  add(Y + V + Z, log(2.0), 0);           /* X1 */
  add(Y + V + Wa, 0, 0);                 /* X2 */
  I bb = lf(0, 0, 0, 1, 1);              /* be */
  add(V + Gup(ze, al, bb), 0, 0);        /* R1 */
  /* R2: n = s+2y+z, d = a+y+z, rho = y+z+1 ; binom C(n,d): B(d, n-d) with n - d = s + y - a */
  classroute(Z + Y, lf(1, 0, 1, 2, 0), 0, lf(0, 1, 1, 1, 0), 0, lf(0, 0, 1, 1, 0), 1, 1,
             Bup(lf(0, 1, 1, 1, 0), lf(1, -1, 0, 1, 0)), 0, 0);
  /* R3: n = s-1+y, d = a+y+z, rho = a+y, E only ; binom <= C(s+y, a+y+z): B(a+y+z, s-a-z) */
  classroute(Wa + Y, lf(1, 0, 0, 1, 0), -1, lf(0, 1, 1, 1, 0), 0, lf(0, 1, 0, 1, 0), 0, 0,
             Bup(lf(0, 1, 1, 1, 0), lf(1, -1, -1, 0, 0)), 0, 0);
  /* R4: n = s-2, d = a+y+z, rho = a+z, both ; binom <= C(s,t): B(t, s-t) */
  classroute(Z + Wa, one, -2, lf(0, 1, 1, 1, 0), 0, lf(0, 1, 1, 0, 0), 0, 1,
             Bup(ta, lf(1, 0, 0, 0, -1)), 0, 0);
  /* R3C: n = s-1+y, d = b+y+z, rho = b+y, E only ; binom <= C(s+y, b+y+z): B(b+y+z, a) */
  classroute(Wb + Y, lf(1, 0, 0, 1, 0), -1, lf(0, 0, 1, 2, 1), 0, lf(0, 0, 0, 2, 1), 0, 0,
             Bup(lf(0, 0, 1, 2, 1), al), 0, 0);
  /* R4C: n = z+2b-2, d = b+y+z, rho = z+b, both ; binom <= C(z+2b, t): B(t, z+2b-t) */
  classroute(Z + Wb, lf(0, 0, 1, 2, 2), -2, lf(0, 0, 1, 2, 1), 0, lf(0, 0, 1, 1, 1), 0, 1,
             Bup(ta, lf(0, 0, 1, 2, 1)), 0, 0);
  /* R5a: (v1,w1): n = s-1-a, d = b-1, rho = t-1, both ; binom <= C(s-a, b): B(b, z) */
  classroute(V + Wa, lf(1, -1, 0, 0, 0), -1, bb, -1, ta, -1, 1, Bup(bb, ze), 0, 0);
  /* R5b: (v1,C1): n = s-1-b, d = a-1, rho = t-1, both ; binom <= C(s-b, a): B(a, z) */
  classroute(V + Wb, lf(1, 0, 0, -1, -1), -1, al, -1, ta, -1, 1, Bup(al, ze), 0, 0);
  /* R6a: v1, w1 | T^{s-2}+v1 (C(s,a)), then as R5a */
  classroute(V + Bup(al, lf(1, -1, 0, 0, 0)), lf(1, -1, 0, 0, 0), -1, bb, -1, ta, -1, 1, Bup(bb, ze), 0, 0);
  /* R6b */
  classroute(V + Bup(bb, lf(1, 0, 0, -1, -1)), lf(1, 0, 0, -1, -1), -1, al, -1, ta, -1, 1, Bup(al, ze), 0, 0);
  /* R8a, R8b, R9a */
  add(Y + V + Bup(al, lf(1, -1, 0, 0, 0)), 0, 0);
  add(Y + V + Bup(bb, lf(1, 0, 0, -1, -1)), 0, 0);
  add(Z + V + Bup(al, bb), 0, 0);
  /* R10a: q^z * 2 * (t-1+...) q^{t-2} * cls(a+b-2, a-1, t-1), both ; Somega(e) <= q^e (e+1) <= q^e (s+1) */
  classroute(Z + V, lf(0, 1, 0, 1, 1), -2, al, -1, ta, -1, 1, Bup(al, bb), log(2.0), 1);
  /* R10b: 2 Somega * C(s, z) * cls */
  classroute(V + Bup(ze, lf(1, 0, -1, 0, 0)), lf(0, 1, 0, 1, 1), -2, al, -1, ta, -1, 1, Bup(al, bb), log(2.0), 1);
}
/* tail of one box: sum_{s > SMIN} P(s) * 2 * min_i exp(s phi_i + logk_i) (s+1)^{polys_i} * q^{1 - s/2} */
static double boxtail(double w0, double w1, double w2) {
  double best = INFINITY;
  for (int i = 0; i < nr; i++) {
    double g = R[i].phi - lq / 2;                 /* per-s exponent */
    if (g >= -1e-9) continue;
    double sum = 0, prev = 0;
    for (long s = SMIN + 1;; s++) {
      double P = (s * w0 + 1) * (s * w1 + 1) * (s * w2 + 1);   /* >= number of integer points */
      double lt = log(2.0) + log(P) + s * R[i].phi + R[i].logk + R[i].polys * log(s + 1.0) + lq * (1 - s / 2.0);
      double term = exp(lt);
      sum += term;
      /* ratio bound for all larger s: poly degree <= 3 + polys, ratio <= ((s+2)/(s+1))^{3+polys} e^{g} */
      double ratio = pow((s + 2.0) / (s + 1.0), 3 + R[i].polys) * exp(g);
      if (ratio < 1 && term < 1e-300) { sum += term * ratio / (1 - ratio); break; }
      if (ratio < 0.999 && s > SMIN + 50) { sum += term * ratio / (1 - ratio); break; }
      if (s > SMIN + 2000000) { sum = INFINITY; break; }
      prev = term;
    }
    (void)prev;
    if (sum < best) best = sum;
  }
  return best;
}
static double total = 0, worstphi = -1e9; static long nboxes = 0, nfail = 0; static int MINW;
static double target;
static void rec(double a0, double z0, double y0, int lev) {
  double w = ldexp(1.0, -lev);
  box[0].lo = a0; box[0].hi = a0 + w; box[1].lo = z0; box[1].hi = z0 + w; box[2].lo = y0; box[2].hi = y0 + w;
  if (a0 + z0 + y0 > 1) return;                       /* tau < 0 */
  if (2 * a0 + z0 > 1) return;                        /* be < al everywhere */
  tau.lo = 1 - (a0 + w) - (z0 + w) - (y0 + w); if (tau.lo < 0) tau.lo = 0; tau.hi = 1 - a0 - z0 - y0;
  routes();
  double t = boxtail(w, w, w);
  double vol = w * w * w;
  if (t <= target * vol * 6 || lev >= MINW) {        /* 6 = 1/volume of the simplex part, rough budget */
    if (!isfinite(t)) { nfail++; if (nfail < 20) printf("FAIL box a=[%g,%g] z=[%g,%g] y=[%g,%g]\n", a0, a0 + w, z0, z0 + w, y0, y0 + w); }
    total += t; nboxes++; return;
  }
  double h = w / 2;
  for (int i = 0; i < 2; i++) for (int j = 0; j < 2; j++) for (int k = 0; k < 2; k++) rec(a0 + i * h, z0 + j * h, y0 + k * h, lev + 1);
}
int main(int argc, char **argv) {
  int r = atoi(argv[1]); SMIN = atol(argv[2]); MINW = argc > 3 ? atoi(argv[3]) : 9; target = argc > 4 ? atof(argv[4]) : 1e-3;
  lq = r * log(3.0);
  for (int i = 0; i < 8; i++) for (int j = 0; j < 8; j++) for (int k = 0; k < 8; k++) rec(i / 8.0, j / 8.0, k / 8.0, 3);
  printf("r=%d S=%ld boxes=%ld failed=%ld tail(s>S) <= %.6e\n", r, SMIN, nboxes, nfail, total);
  return 0;
}
