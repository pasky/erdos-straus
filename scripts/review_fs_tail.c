/* review_fs_tail.c (R217, from scratch): rigorous upper bound for the Case B tail  sum_{s > S}  of the left side of
   (Sigma) in FF_STERILE_PUSH, q = 3^r, k = 2, using the Lemma 1.6 route bounds as re-derived in the R217 review.
   Written independently of scripts/fs_tail.c. Differences in design:
   * boxes are dyadic cubes in p = (al, ze, ps) = (a, z, y)/s with INTEGER corner coordinates (scaled by 2^lev);
     ta = 1 - al - ze - ps, be = 1 - al - ze; every linear form is maximised EXACTLY over the cube by evaluating it at
     the 8 corners in integer arithmetic (no interval over-estimation, no floating point in any decision);
   * q-power counts keep their integer shifts (N*(a-1) <= q^{a-1}, N*(t-2) <= q^{t-2}, ...);
   * Coppersmith is searched over j = m + k <= JMAX with, for each j, a window of m around the optimum at the cube
     centre (any (m, j) that passes the exact corner test is valid; the window only affects strength, not validity);
   * every binomial / multinomial is bounded by exp(B(d+, e+)) where d <= s d+, n - d <= s e+ (all integer shifts of
     d and n - d in the table are <= 0, checked by hand in the review), B(x, y) = (x+y)log(x+y) - x log x - y log y.
   Per box and route: count(s, pattern) <= exp(s*phi + kap) * (s+1)^pi for every integer pattern of level s > S whose
   normalisation lies in the box; #patterns of level s in the box <= (floor(s w) + 1)^3 <= (s w + 1)^3.
   Box contribution: sum_{s > S} 2 (s w + 1)^3 exp(s phi + kap) (s+1)^pi q^{1 - s/2}, summed term by term until the
   ratio bound ((s+2)/(s+1))^{3+pi} e^{phi - L/2} (valid for all larger s) is <= (1 + e^{phi - L/2})/2, then
   closed by a geometric series (overestimating the remainder by at most a factor 2).
   Fails closed (exit 1) if some box at maximal level has no route with phi < L/2 or the sum does not converge.
   usage: review_fs_tail r S [MAXLEV=8] [EPS=1e-7] [JMAX=120] */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static double L; static ll S; static int MAXLEV = 8, JMAX = 200; static double EPS = 1e-7;
static ll ci, cj, ck; static int lev; static ll W;   /* cube [ci,ci+1]x[cj,cj+1]x[ck,ck+1] / W, W = 2^lev */
/* linear form f(p) = c0 + ca al + cz ze + cy ps (ta, be expressed through these). Return max over cube of W*f. */
typedef struct { ll c0, ca, cz, cy; } LF;
static LF mk(ll c0, ll ca, ll cz, ll cy) { LF f = {c0, ca, cz, cy}; return f; }
static LF lin(ll k1, ll kal, ll kze, ll kps, ll kta) {   /* k1 + kal al + kze ze + kps ps + kta ta */
  return mk(k1 + kta, kal - kta, kze - kta, kps - kta);
}
static ll maxW(LF f) {
  ll best = -(1LL << 62);
  for (int e = 0; e < 8; e++) {
    ll v = f.c0 * W + f.ca * (ci + (e & 1)) + f.cz * (cj + ((e >> 1) & 1)) + f.cy * (ck + ((e >> 2) & 1));
    if (v > best) best = v;
  }
  return best;
}
static double maxf(LF f) { return (double)maxW(f) / (double)W; }
static LF add(LF f, LF g, ll cg) { return mk(f.c0 + cg * g.c0, f.ca + cg * g.ca, f.cz + cg * g.cz, f.cy + cg * g.cy); }
static double xlx(double x) { return x <= 0 ? 0 : x * log(x); }
static double Bp(double d, double e) { if (d < 0) d = 0; if (e < 0) e = 0; return (xlx(d + e) - xlx(d) - xlx(e)) * (1 + 1e-12) + 1e-15; }
/* condition  s*F(p) + f0 < 0  for all p in cube and all s >= S+1 (F linear, f0 const) */
static int neg_all(LF F, ll f0) { ll m = maxW(F); return m <= 0 && (S + 1) * m + f0 * W < 0; }
/* class bound on the cube: n = s N + n0, d = s D + d0, rho = s R + r0. returns smallest valid kappa, 0 if none */
static int cls(LF N, ll n0, LF D, ll d0, LF R, ll r0, int cof) {
  if (neg_all(add(D, R, -1), d0 - r0)) return 1;                                         /* d < rho */
  if (cof && neg_all(add(add(N, D, -1), R, -1), n0 - d0 - r0)) return 1;               /* n - d < rho */
  int best = 0;
  if (neg_all(add(N, R, -3), n0 - 3 * r0)) best = 2;                                     /* n - 3 rho < 0 */
  for (int ver = 0; ver <= cof; ver++) {
    LF Dv = ver ? add(N, D, -1) : D; ll dv0 = ver ? n0 - d0 : d0;
    /* prefilter (a necessary condition, so skipping is safe): (C) for all s at the cube centre needs n X < d^2 there */
    double cN = 0, cD = 0, cR = 0;
    { LF fs[3] = {N, Dv, R}; double *out[3] = {&cN, &cD, &cR};
      for (int u = 0; u < 3; u++) *out[u] = fs[u].c0 + fs[u].ca * (ci + 0.5) / W + fs[u].cz * (cj + 0.5) / W + fs[u].cy * (ck + 0.5) / W; }
    if (!(cN * (cD - cR) < cD * cD)) continue;
    for (ll j = 1; j <= JMAX && (!best || j < best); j++) {
      int ok = 0;
      double ms = (2.0 * (j + 1) * cD - cN) / (2.0 * cN);     /* convex optimum at the centre; try a window */
      ll mlo = (ll)floor(ms) - 3, mhi = (ll)floor(ms) + 4;
      if (mlo < 1) mlo = 1; if (mhi > j) mhi = j;
      for (ll m = mlo; m <= mhi && !ok; m++) {
        /* n m(m+1) + (d - rho) j(j+1) - 2 (j+1) m d < 0 */
        ll A = m * (m + 1), B = j * (j + 1), Cc = 2 * (j + 1) * m;
        LF F = add(add(mk(0, 0, 0, 0), N, A), add(add(mk(0, 0, 0, 0), Dv, B - Cc), R, -B), 1);
        ll f0 = A * n0 + (B - Cc) * dv0 - B * r0;
        if (neg_all(F, f0)) ok = 1;
      }
      if (ok) { best = (int)j; break; }
    }
  }
  return best;
}
typedef struct { double phi, kap; int pi; } RT;
static RT rt[64]; static int nr;
static void put(double phi, double kap, int pi) { rt[nr].phi = phi; rt[nr].kap = kap; rt[nr].pi = pi; nr++; }
/* class route: base (phi, kap, pi) times min(binomial bound exp(s*bin), class bound) */
static void croute(double phi, double kap, int pi, double bin, LF N, ll n0, LF D, ll d0, LF R, ll r0, int cof) {
  put(phi + bin, kap, pi);
  int c = cls(N, n0, D, d0, R, r0, cof);
  if (c) put(phi, kap + log((double)c), pi);
}
static void routes(void) {
  nr = 0;
  LF al = lin(0, 1, 0, 0, 0), ze = lin(0, 0, 1, 0, 0), ps = lin(0, 0, 0, 1, 0), ta = lin(0, 0, 0, 0, 1);
  LF be = lin(0, 0, 0, 1, 1), one = lin(1, 0, 0, 0, 0);
  double m_ = L * maxf(ze), g_ = L * maxf(ps), w_ = L * maxf(al), c_ = L * maxf(be), v_ = L * maxf(ta);
  double kw = -L, kc = -L, kv = -2 * L, l2 = log(2.0);
  double alp = maxf(al), zep = maxf(ze), bep = maxf(be);
  double Bs_a = Bp(alp, maxf(add(one, al, -1)));            /* C(s-2, a-1) <= exp(s B(al+, (1-al)+)) */
  double Bs_b = Bp(bep, maxf(add(one, be, -1)));            /* C(s-2, b-1) */
  double Bab = Bp(alp, bep);                                /* C(a+b-2, a-1) */
  double Bs_z = Bp(zep, maxf(add(one, ze, -1)));            /* C(s-2, z) */
  put(m_ + g_ + w_, kw, 0);                                 /* T0 */
  put(m_ + w_ + v_, kw + kv, 0);                            /* R4' */
  put(m_ + g_ + v_, l2 + kv, 0);                            /* X1 */
  put(g_ + v_ + w_, kv + kw, 0);                            /* X2 */
  {   /* R1: multinomial (s-2)!/(z!(a-1)!(b-1)!) <= exp(s G(ze+, al+, be+)), G increasing in each argument */
    double x = zep, y = alp, z = bep;
    double G = (xlx(x + y + z) - xlx(x) - xlx(y) - xlx(z)) * (1 + 1e-12) + 1e-15;
    put(v_ + G, kv, 0);
  }
  /* R2: (m',g'), n = s+2y+z, d = a+y+z, rho = 1+y+z, cofactor ok */
  { LF N = lin(1, 0, 1, 2, 0), D = lin(0, 1, 1, 1, 0), R = lin(0, 0, 1, 1, 0);
    croute(m_ + g_, 0, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, 0, D, 0, R, 1, 1); }
  /* R3: (w1,g'), n = s-1+y, d = a+y+z, rho = a+y, E only */
  { LF N = lin(1, 0, 0, 1, 0), D = lin(0, 1, 1, 1, 0), R = lin(0, 1, 0, 1, 0);
    croute(w_ + g_, kw, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, -1, D, 0, R, 0, 0); }
  /* R4: (m',w1), n = s-2, d = a+y+z, rho = a+z, cofactor ok */
  { LF N = one, D = lin(0, 1, 1, 1, 0), R = lin(0, 1, 1, 0, 0);
    croute(m_ + w_, kw, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, -2, D, 0, R, 0, 1); }
  /* R3C: (C1,g'), n = s-1+y, d = b+y+z, rho = b+y, E' only */
  { LF N = lin(1, 0, 0, 1, 0), D = add(lin(0, 0, 1, 1, 0), be, 1), R = add(ps, be, 1);
    croute(c_ + g_, kc, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, -1, D, 0, R, 0, 0); }
  /* R4C: (m',C1), n = z+2b-2, d = b+y+z, rho = b+z, cofactor ok */
  { LF N = add(ze, be, 2), D = add(lin(0, 0, 1, 1, 0), be, 1), R = add(ze, be, 1);
    croute(m_ + c_, kc, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, -2, D, 0, R, 0, 1); }
  /* R5a: (v1,w1), C1 | (T^{s-2}+v1)/w1: n = s-1-a, d = b-1, rho = t-1, cofactor ok */
  { LF N = add(one, al, -1), D = be, R = ta;
    croute(v_ + w_, kv + kw, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, -1, D, -1, R, -1, 1);
    /* R6a: v1, w1 | T^{s-2}+v1 (C(s-2,a-1)), then as R5a */
    croute(v_ + Bs_a, kv, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, -1, D, -1, R, -1, 1); }
  /* R5b: (v1,C1): n = s-1-b, d = a-1, rho = t-1 */
  { LF N = add(one, be, -1), D = al, R = ta;
    croute(v_ + c_, kv + kc, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, -1, D, -1, R, -1, 1);
    croute(v_ + Bs_b, kv, 0, Bp(maxf(D), maxf(add(N, D, -1))), N, -1, D, -1, R, -1, 1); }
  put(g_ + v_ + Bs_a, kv, 0);                               /* R8a */
  put(g_ + v_ + Bs_b, kv, 0);                               /* R8b */
  put(m_ + v_ + Bab, kv, 0);                                /* R9a */
  /* R10a/b: 2 * Som(t-2) <= 2 q^{t-2} (s+1); w1 | G2 = (T^{s-2}+v1)/m' (deg a+b-2), d = a-1, rho = t-1, cofactor ok */
  { LF N = add(al, be, 1), D = al, R = ta;
    croute(m_ + v_, kv + l2, 1, Bab, N, -2, D, -1, R, -1, 1);
    croute(v_ + Bs_z, kv + l2, 1, Bab, N, -2, D, -1, R, -1, 1); }
}
static int failed = 0;
static long double boxtail(void) {
  double w = 1.0 / (double)W; long double best = INFINITY;
  for (int i = 0; i < nr; i++) {
    double g = rt[i].phi - L / 2;
    if (!(g < 0)) continue;
    long double sum = 0;
    for (ll s = S + 1; ; s++) {
      long double lt = logl(2.0L) + 3 * logl(s * (long double)w + 1) + s * (long double)rt[i].phi + rt[i].kap
                       + rt[i].pi * logl(s + 1.0L) + (1 - s / 2.0L) * L;
      long double term = expl(lt);
      sum += term;
      long double ratio = powl((s + 2.0L) / (s + 1.0L), 3 + rt[i].pi) * expl((long double)g);
      /* close once the (decreasing) ratio bound is <= (1 + e^g)/2: overestimates the remaining sum by <= 2x */
      if (ratio <= (1 + expl((long double)g)) / 2) { sum += term * ratio / (1 - ratio); break; }
      if (s > S + 5000000) { sum = INFINITY; break; }
    }
    if (sum < best) best = sum;
  }
  return best * (1 + 1e-9L);
}
static long double total = 0; static long nbox = 0;
static void rec(ll i, ll j, ll k, int lv) {
  ll Wl = 1LL << lv;
  if (i + j + k > Wl) return;          /* ta < 0 on the whole cube (ta >= 0 needs al+ze+ps <= 1 at the min corner) */
  if (2 * i + j > Wl) return;          /* be < al on the whole cube */
  ci = i; cj = j; ck = k; lev = lv; W = Wl;
  routes();
  long double t = boxtail();
  if ((!(t <= EPS) ) && lv < MAXLEV) {
    for (int e = 0; e < 8; e++) rec(2 * i + (e & 1), 2 * j + ((e >> 1) & 1), 2 * k + ((e >> 2) & 1), lv + 1);
    return;
  }
  if (!isfinite((double)t)) { failed++; if (failed < 10) printf("FAIL cube lev=%d (%lld,%lld,%lld)/%lld\n", lv, i, j, k, Wl); }
  total += t; nbox++;
}
#ifndef NOMAIN
int main(int argc, char **argv) {
  int r = atoi(argv[1]); S = atoll(argv[2]);
  if (argc > 3) MAXLEV = atoi(argv[3]); if (argc > 4) EPS = atof(argv[4]); if (argc > 5) JMAX = atoi(argv[5]);
  L = r * log(3.0);
  for (ll i = 0; i < 4; i++) for (ll j = 0; j < 4; j++) for (ll k = 0; k < 4; k++) rec(i, j, k, 2);
  printf("TAIL r=%d S=%lld maxlev=%d eps=%g boxes=%ld failed=%d tail_upper=%.10Le\n", r, S, MAXLEV, EPS, nbox, failed, total);
  return (failed || !isfinite((double)total)) ? 1 : 0;
}
#endif
