/* review_fz9_tail.c (R221): R220's review_fz_tail.c (reviewer code, independent of the author) + R221's OWN linearised
   Lemma 4.1 (FF_STERILE_SMALL Lemma 5.1) in every binomial divisor count Bn(d, e), and the R1 alternative
   (m' | F, then w1 | F/m', F = T^{s-2} + v1).  Own constants: rho in {k/32}, n0 in {S/2, S, 2S, 4S, 8S}; items (P, e) with
   e*deg P <= W = 20000 (all items included up to that weight); every omitted item has ratio <= min(1/W, rho^W)
   (gain = log(1 + y^e/S_{e-1}(y)) <= min(1/e, y^e), y = rho^j), and we REQUIRE lambda > that bound (else exit 2).
   Bound per unit s: -log(rho) min(d, e) + lambda (d + e) + max(c, 0)/(S + 1), c = V(n0) - lambda n0 (outward).
   Set NORANK=1 in the environment to recover R220's code path.
   --- original header (R220) --- */
/* review_fz_tail.c (R220): R218's review_fs2_tail.c (independent of the author) extended from the TEXT of FF_STERILE_SMALL
   §1: (i) Lemma 1.4 on every class route: j = ceil(theta*s) <= theta*s + 1 extra T-adic digits, cost q^{theta s + 1},
   class conditions checked with rho_eff = s*(R + theta) + r0 <= rho + j (all conditions monotone in rho);
   (ii) Lemma 1.3 routes D1, D1c (omega*(e) <= (q-1)/2 + e/2), D2, D3, X1', X2', R4''; V(d) <= q^{max(0, t - d)}.
   usage: review_fz_tail r S maxlev budget [new=1]
   Original header: review_fs2_tail.c (R218, from scratch; NOT derived from fs_tail.c).
   Rigorous upper bound for the Case B tail  sum_{s > S} q^{1-ceil(s/2)} sum_patterns mult * min_route(bound),
   q = 3^r, k = 2.  Pattern p = (al, ze, et) = (a, z, y)/s, ta = 1 - al - ze - et = t/s, be = 1 - al - ze = b/s.
   Adaptive octree in p-space starting from width 1/8. On a box, every quantity entering a route is a linear form
   L(p)*s + c (c integer); we use sup_box L computed coordinatewise (exact dyadic arithmetic) and
     N*(d) <= q^d,  C(n,d) <= exp(B(d, n-d)), multinomial <= exp(G(.)), B, G increasing, homogeneous degree 1,
   each evaluated at upper bounds of the (shift-dropped, enlarged) arguments.
   Class conditions (Lemma 1.4: 3 rho - n > 0; Lemma 1.5: A n + (B - M) d - B rho < 0; trivial: d - rho < 0,
   cofactor n - d - rho < 0) are combined into ONE linear form in p before taking the sup, and required to hold for every
   s >= S+1 (sup <= 0 and sup*(S+1) + c < 0, resp. inf >= 0 and inf*(S+1)+c > 0).
   Patterns of level s in a box of width h: <= (s h + 1)^3. Multiplicity 2 for all. q^{1-ceil(s/2)} <= q^{1-s/2}.
   Sum over s: closed-form unimodal sum + integral bound (see boxsum).
   Rounding: +1e-9 per unit s on every exponent, final x1.001; fails closed (exit 1) if some box at max depth
   has no route with negative exponent.   usage: review_fs2_tail r S maxlev  */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static double LQ; static long S; static int MAXLEV;
static double lo[3], hi[3];
/* sup / inf over the box of c0 + ca*al + cz*ze + cy*et  (ta = 1-al-ze-et substituted by caller) */
static double sup3(double c0, double ca, double cz, double cy) {
  double c[3] = {ca, cz, cy}, r = c0; for (int i = 0; i < 3; i++) r += c[i] >= 0 ? c[i] * hi[i] : c[i] * lo[i]; return r; }
static double inf3(double c0, double ca, double cz, double cy) {
  double c[3] = {ca, cz, cy}, r = c0; for (int i = 0; i < 3; i++) r += c[i] >= 0 ? c[i] * lo[i] : c[i] * hi[i]; return r; }
/* a linear form per unit s: (c0, ca, cz, cy) for c0 + ca al + cz ze + cy et; ta = 1 - al - ze - et */
typedef struct { double c0, ca, cz, cy; } LF;
static LF mk(double c0, double ca, double cz, double cy, double ct) { LF f = {c0 + ct, ca - ct, cz - ct, cy - ct}; return f; }
static LF lin(LF f, double x, LF g, double y) { LF h = {x * f.c0 + y * g.c0, x * f.ca + y * g.ca, x * f.cz + y * g.cz, x * f.cy + y * g.cy}; return h; }
static double SUP(LF f) { double v = sup3(f.c0, f.ca, f.cz, f.cy); return v > 0 ? v : 0; }
static double INF(LF f) { return inf3(f.c0, f.ca, f.cz, f.cy); }
static double xl(double x) { return x > 0 ? x * log(x) : 0; }
static double Bn0(double d, double e) { return xl(d + e) - xl(d) - xl(e); }           /* d, e >= 0 upper bounds */
#define NRH 32
#define NN0 5
#define WMAX 20000
static int RANKON = 1; static double RLR[NRH], RL[NRH][NN0], RC[NRH][NN0];
typedef struct { double ratio; long j; double cnt; } IT;
static int icmp(const void *x, const void *y) { double a = ((const IT *)x)->ratio, b = ((const IT *)y)->ratio; return a < b ? 1 : a > b ? -1 : 0; }
static void rk_init(long Q) {
  double *Ir = calloc(WMAX + 1, sizeof(double));
  for (long j = 1; j <= WMAX; j++) { long double sm = 0; for (long i = 1; i <= j; i++) if (j % i == 0) { long m = i; int mu = 1;
      for (long p = 2; p * p <= m; p++) if (m % p == 0) { m /= p; if (m % p == 0) { mu = 0; break; } mu = -mu; } if (mu && m > 1) mu = -mu;
      long double lt = (j / i) * logl((long double)Q); sm += mu * (lt > 11000 ? 1e4000L : powl((long double)Q, (long double)(j / i))); }
    long double v = sm / j - (j == 1); Ir[j] = v > 1e12L ? 1e12 : (double)v; }   /* capacity <= 8S < 1e12: cap harmless */
  IT *it = malloc(sizeof(IT) * 400000); long n0s[NN0] = {S / 2, S, 2 * S, 4 * S, 8 * S};
  for (int k = 0; k < NRH; k++) { double rho = (k + 1.0) / NRH; RLR[k] = -log(rho); long ni = 0;
    for (long j = 1; j <= WMAX; j++) { double y = pow(rho, (double)j); double Sp = 1;
      for (long e = 1; e * j <= WMAX; e++) { double ye = pow(y, (double)e); double g = log1p(ye / Sp); Sp += ye; if (!(g > 0)) break;
        if (ni >= 400000) { fprintf(stderr, "items\n"); exit(2); } it[ni].ratio = g / j; it[ni].j = j; it[ni].cnt = Ir[j]; ni++; } }
    qsort(it, ni, sizeof(IT), icmp);
    double omit = fmin(1.0 / WMAX, pow(rho, (double)WMAX));
    for (int u = 0; u < NN0; u++) { double need = n0s[u], val = 0, lam = -1; long i;
      for (i = 0; i < ni; i++) { double cap = it[i].cnt * it[i].j; if (cap > need) { val += need * it[i].ratio; lam = it[i].ratio; break; }
        val += cap * it[i].ratio; need -= cap; if (need <= 0) { lam = i + 1 < ni ? it[i + 1].ratio : 0; break; } }
      /* items dropped by the !(g > 0) underflow test have ratio 0 in floating point: < 1e-300; covered by omit-check below */
      if (lam < 0 || !(lam > omit) || !(lam > 1e-290)) { fprintf(stderr, "rank: lambda %g not above omitted-item bound %g (k=%d u=%d)\n", lam, omit, k, u); exit(2); }
      lam = lam * (1 + 1e-9); val = val * (1 + 1e-9) + 1e-9;
      RL[k][u] = lam; RC[k][u] = val - lam * n0s[u]; } }
  free(it); free(Ir); }
static double Bn(double d, double e) { double b = Bn0(d, e); if (!RANKON) return b; double dp = d < e ? d : e;
  for (int k = 0; k < NRH; k++) for (int u = 0; u < NN0; u++) { double v = RLR[k] * dp + RL[k][u] * (d + e) + (RC[k][u] > 0 ? RC[k][u] : 0) / (S + 1); if (v < b) b = v; }
  return b; }
static double Gm(double x, double y, double z) { return xl(x + y + z) - xl(x) - xl(y) - xl(z); }
/* class bound kappa valid on the box for all s >= S+1: forms n = s*N + n0, d = s*D + d0, rho = s*R + r0 */
static int holds_neg(LF f, double c) { double u = sup3(f.c0, f.ca, f.cz, f.cy); return u <= 0 && u * (S + 1) + c < 0; }
static int holds_pos(LF f, double c) { double l = INF(f); return l >= 0 && l * (S + 1) + c > 0; }
static int kappa(LF N, double n0, LF D, double d0, LF R, double r0, int both) {
  if (holds_neg(lin(D, 1, R, -1), d0 - r0)) return 1;
  if (both && holds_neg(lin(lin(N, 1, D, -1), 1, R, -1), n0 - d0 - r0)) return 1;
  int best = 0;
  if (holds_pos(lin(R, 3, N, -1), 3 * r0 - n0)) best = 2;
  for (int ver = 0; ver <= both; ver++) {
    LF Dv = ver ? lin(N, 1, D, -1) : D; double dv0 = ver ? n0 - d0 : d0;
    for (int K = 1; K <= 60 && (!best || K < best); K++) {
      int ok = 0;
      for (int m = 1; m <= K && !ok; m++) {
        double k = K - m, A = m * (m + 1) / 2.0, B = A + k * m + k * (k + 1) / 2.0, M = (m + k + 1) * (double)m;
        /* A n + B (d - rho) - M d < 0 */
        LF f = lin(lin(N, A, Dv, B - M), 1, R, -B); double c = A * n0 + (B - M) * dv0 - B * r0;
        if (holds_neg(f, c)) ok = 1;
      }
      if (ok) { best = K; break; }
    }
  }
  return best;
}
typedef struct { double phi, lk; int p; } RT;
static RT rt[80]; static int nr;
static void add(double phi, double lk, int p) { rt[nr].phi = phi + 1e-9; rt[nr].lk = lk; rt[nr].p = p; nr++; }
static int NEW = 1;
static void croute(double base, double binom, LF N, double n0, LF D, double d0, LF R, double r0, int both, double lk, int p) {
  add(base + binom, lk, p); int k = kappa(N, n0, D, d0, R, r0, both); if (k) { add(base, lk + log((double)k), p); return; }
  if (!NEW) return;
  /* Lemma 1.4: smallest theta = i/256 (bisection; validity re-checked) with a class bound at rho + ceil(theta s) */
  int lo = 0, hi = 256; LF R2 = R; R2.c0 += 1.0; if (!kappa(N, n0, D, d0, R2, r0, both)) return;
  while (hi - lo > 1) { int mid = (lo + hi) / 2; LF R3 = R; R3.c0 += mid / 256.0; if (kappa(N, n0, D, d0, R3, r0, both)) hi = mid; else lo = mid; }
  LF R3 = R; R3.c0 += hi / 256.0; int k3 = kappa(N, n0, D, d0, R3, r0, both); if (!k3) { fprintf(stderr, "bisection error\n"); exit(3); }
  add(base + hi / 256.0 * LQ, lk + log((double)k3) + LQ, p); }
static void routes(void) {
  nr = 0;
  LF A = mk(0, 1, 0, 0, 0), Z = mk(0, 0, 1, 0, 0), Y = mk(0, 0, 0, 1, 0), Tt = mk(0, 0, 0, 0, 1), Bb = mk(1, -1, -1, 0, 0), One = mk(1, 0, 0, 0, 0);
  double a = SUP(A), z = SUP(Z), y = SUP(Y), t = SUP(Tt), b = SUP(Bb), L = LQ;
  add((z + y + a) * L, 0, 0);                 /* T0: N*(z)N*(y)N*(a-1) */
  add((z + a + t) * L, 0, 0);                 /* R4' */
  add((y + t + z) * L, log(2.0), 0);          /* X1 */
  add((y + t + a) * L, 0, 0);                 /* X2 */
  add(t * L + Gm(z, a, b), 0, 0);             /* R1: N*(t-2) (s-2)!/(z!(a-1)!(b-1)!) */
  if (RANKON) add(t * L + Bn(z, SUP(mk(1, 0, -1, 0, 0))) + Bn(a, b), 0, 0);   /* R221: R1 via m' | F (C(s,z)), w1 | F/m' (C(a+b, a)) */
  /* R2: E | 1+T^s m'g'^2: n = s+2y+z, d = a+y+z, rho = y+z+1; C(n,d)=C(n, s+y-a) */
  { LF N = mk(1, 0, 1, 2, 0), D = mk(0, 1, 1, 1, 0), R = mk(0, 0, 1, 1, 0);
    croute((z + y) * L, Bn(SUP(D), SUP(mk(1, -1, 0, 1, 0))), N, 0, D, 0, R, 1, 1, 0, 0); }
  /* R3: n = s-1+y, d = a+y+z, rho = a+y, E only; C(s-1+y, a+y+z) <= exp B(a+y+z, s-a-z) */
  { LF N = mk(1, 0, 0, 1, 0), D = mk(0, 1, 1, 1, 0), R = mk(0, 1, 0, 1, 0);
    croute((a + y) * L, Bn(SUP(D), SUP(mk(1, -1, -1, 0, 0))), N, -1, D, 0, R, 0, 0, 0, 0); }
  /* R4: n = s-2, d = a+y+z, rho = a+z, both; C(s-2, t-2) <= exp B(t, s-t) */
  { LF D = mk(0, 1, 1, 1, 0), R = mk(0, 1, 1, 0, 0);
    croute((z + a) * L, Bn(t, SUP(mk(1, 0, 0, 0, -1))), One, -2, D, 0, R, 0, 1, 0, 0); }
  /* R3C: n = s-1+y, d = b+y+z, rho = b+y; C <= exp B(b+y+z, a) */
  { LF N = mk(1, 0, 0, 1, 0), D = mk(0, 0, 1, 2, 1), R = mk(0, 0, 0, 2, 1);
    croute((b + y) * L, Bn(SUP(D), a), N, -1, D, 0, R, 0, 0, 0, 0); }
  /* R4C: n = z+2b-2, d = b+y+z, rho = z+b, both; C(z+2b-2, t-2) <= exp B(t, z+b+y) */
  { LF N = mk(0, 0, 1, 2, 2), D = mk(0, 0, 1, 2, 1), R = mk(0, 0, 1, 1, 1);
    croute((z + b) * L, Bn(t, SUP(D)), N, -2, D, 0, R, 0, 1, 0, 0); }
  /* R5a: (v1,w1): n = s-1-a, d = b-1, rho = t-1, both; C(s-1-a, b-1) <= exp B(b, z) */
  LF N5a = mk(1, -1, 0, 0, 0), N5b = mk(1, 0, 0, -1, -1);
  croute((t + a) * L, Bn(b, z), N5a, -1, Bb, -1, Tt, -1, 1, 0, 0);
  croute((t + b) * L, Bn(a, z), N5b, -1, A, -1, Tt, -1, 1, 0, 0);                     /* R5b */
  croute(t * L + Bn(a, SUP(N5a)), Bn(b, z), N5a, -1, Bb, -1, Tt, -1, 1, 0, 0);        /* R6a: C(s-2,a-1) <= B(a, s-a) */
  croute(t * L + Bn(b, SUP(N5b)), Bn(a, z), N5b, -1, A, -1, Tt, -1, 1, 0, 0);         /* R6b */
  add((y + t) * L + Bn(a, SUP(N5a)), 0, 0);                                            /* R8a */
  add((y + t) * L + Bn(b, SUP(N5b)), 0, 0);                                            /* R8b */
  add((z + t) * L + Bn(a, b), 0, 0);                                                   /* R9a */
  /* R10a: N*(z) * 2 * Somega(t-2) * cls(a+b-2, a-1, t-1); Somega(t-2) <= (t-1) q^{t-2} <= (s+1) q^t */
  LF N10 = mk(0, 1, 0, 1, 1);
  croute((z + t) * L, Bn(a, b), N10, -2, A, -1, Tt, -1, 1, log(2.0), 1);
  croute(t * L + Bn(z, SUP(mk(1, 0, -1, 0, 0))), Bn(a, b), N10, -2, A, -1, Tt, -1, 1, log(2.0), 1);   /* R10b */
  if (!NEW) return;
  /* Lemma 1.3: V(d) = #{v1 in class mod D, deg D = d} <= q^{max(0, t-2-d)} <= exp(s * SUP(t - d/s) * LQ) */
  double Vz = SUP(mk(0, 0, -1, 0, 1)) * L, Va = SUP(mk(0, -1, 0, 0, 1)) * L, Vb = SUP(mk(0, 0, 0, -1, 0)) * L,
         Vza = SUP(mk(0, -1, -1, 0, 1)) * L, Q = exp(L);
  add(z * L + Vz + Bn(a, b), 0, 0);                                                   /* D1 */
  croute(z * L + Vz + 0.5 * t * log(2.0), Bn(a, b), N10, -2, A, -1, Tt, -1, 1,
         log(2.0) * (1 + (Q - 1) / 2), 0);                                            /* D1c: 2 * V * 2^{omega*} */
  croute(a * L + Va, Bn(b, z), N5a, -1, Bb, -1, Tt, -1, 1, 0, 0);                     /* D2 */
  croute(b * L + Vb, Bn(a, z), N5b, -1, A, -1, Tt, -1, 1, 0, 0);                      /* D3 */
  add((y + z) * L + Vz, log(2.0), 0);                                                 /* X1' */
  add((y + a) * L + Va, 0, 0);                                                        /* X2' */
  add((z + a) * L + Vza, 0, 0);                                                       /* R4'' */
}
/* sum_{s >= S+1} 2 (s h + 1)^3 (s+1)^p e^{s phi + lk} q^{1 - s/2}
   <= 2 e^{lk} q (h + 1/(S+1))^3 * sum_{s >= S+1} (s+1)^j e^{g s},  j = 3 + p, g = phi - LQ/2 < 0
   [since s h + 1 <= (s+1)(h + 1/(S+1)) for s >= S+1]. With u = s+1, x = -g: sum = e^{x} sum_{u >= S+2} u^j e^{-x u};
   u^j e^{-xu} is unimodal, so sum_{u >= U} <= max_{u >= U} + int_U^inf u^j e^{-xu} du, and
   int_U^inf u^j e^{-xu} du = e^{-xU} sum_{i=0}^{j} j!/(j-i)! U^{j-i} / x^{i+1}. */
static double boxsum(double h, int *ok) {
  double best = INFINITY;
  for (int i = 0; i < nr; i++) {
    double g = rt[i].phi - LQ / 2; if (g >= 0) continue;
    double x = -g, U = S + 2.0; int j = 3 + rt[i].p;
    double umax = j / x; if (umax < U) umax = U;
    double lmax = j * log(umax) - x * umax;                  /* log max_{u >= U} u^j e^{-xu} */
    double integ = 0, fact = 1;
    for (int k = 0; k <= j; k++) { integ += fact * pow(U, j - k) / pow(x, k + 1); fact *= (j - k); }
    double lsum = x + log(exp(lmax) + exp(-x * U) * integ);
    double v = exp(log(2.0) + rt[i].lk + LQ + 3 * log(h + 1.0 / (S + 1)) + lsum);
    if (v < best) best = v;
  }
  *ok = isfinite(best); return best;
}
/* returns the best valid bound for the box: min(own bound, sum of children's best bounds) -- both are valid
   coverings of the patterns in the box. INFINITY if no valid bound at depth MAXLEV. */
static long nleaf; static double budget; static int RATE = 0; static double ratemax = -1e9, ratept[3];
/* RATE mode: uniform depth MAXLEV, max over boxes of min_route phi^+ / LQ - 1/2 (an upper bound for the continuum exponent
   max_p min_route phi(p) - 1/2, up to the O(width) enlargement of phi^+) */
static double raterec(double a0, double z0, double y0, int lev) {
  double h = ldexp(1.0, -lev);
  if (a0 + z0 + y0 >= 1 || 2 * a0 + z0 > 1) return 0;
  if (lev < MAXLEV) { double g = h / 2; for (int i = 0; i < 8; i++) raterec(a0 + (i & 1) * g, z0 + ((i >> 1) & 1) * g, y0 + ((i >> 2) & 1) * g, lev + 1); return 0; }
  lo[0] = a0; hi[0] = a0 + h; lo[1] = z0; hi[1] = z0 + h; lo[2] = y0; hi[2] = y0 + h;
  routes(); double m = INFINITY; for (int i = 0; i < nr; i++) if (rt[i].phi < m) m = rt[i].phi;
  m = m / LQ - 0.5; if (m > ratemax) { ratemax = m; ratept[0] = a0; ratept[1] = z0; ratept[2] = y0; } return 0; }
static double rec(double a0, double z0, double y0, int lev) {
  double h = ldexp(1.0, -lev);
  if (a0 + z0 + y0 >= 1) return 0;          /* ta <= 0 on the whole box: no patterns */
  if (2 * a0 + z0 > 1) return 0;            /* b < a on the whole box */
  lo[0] = a0; hi[0] = a0 + h; lo[1] = z0; hi[1] = z0 + h; lo[2] = y0; hi[2] = y0 + h;
  routes(); int ok; double v = boxsum(h, &ok);
  nleaf++;
  if (lev >= MAXLEV || (ok && v <= budget * h * h * h)) return v;
  double g = h / 2, c = 0;
  for (int i = 0; i < 8 && c < v; i++) c += rec(a0 + (i & 1) * g, z0 + ((i >> 1) & 1) * g, y0 + ((i >> 2) & 1) * g, lev + 1);
  return c < v ? c : v;
}
int main(int argc, char **argv) {
  int r = atoi(argv[1]); S = atol(argv[2]); MAXLEV = argc > 3 ? atoi(argv[3]) : 8; budget = argc > 4 ? atof(argv[4]) : 1e-2;
  LQ = r * log(3.0); if (argc > 5) NEW = atoi(argv[5]);
  if (getenv("NORANK")) RANKON = 0; if (RANKON) { long Q = 1; for (int i = 0; i < r; i++) Q *= 3; rk_init(Q); }
  if (getenv("RATE")) { for (int i = 0; i < 512; i++) raterec((i & 7) / 8.0, ((i >> 3) & 7) / 8.0, (i >> 6) / 8.0, 3);
    printf("RATE r=%d new=%d lev=%d: max_box min_route phi+/log q - 1/2 = %.4f at box corner (a,z,y)=(%.4f,%.4f,%.4f)\n", r, NEW, MAXLEV, ratemax, ratept[0], ratept[1], ratept[2]); return 0; }
  double total = 0;
  for (int i = 0; i < 512; i++) total += rec((i & 7) / 8.0, ((i >> 3) & 7) / 8.0, (i >> 6) / 8.0, 3);
  printf("r=%d S=%ld maxlev=%d boxes_evaluated=%ld tail<=%.6e certified(x1.001)=%.6e\n", r, S, MAXLEV, nleaf, total, total * 1.001);
  return isfinite(total) ? 0 : 1;
}
