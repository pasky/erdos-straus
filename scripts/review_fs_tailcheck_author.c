/* review_fs_tailcheck_author.c (R217): validates the per-box route bounds of the AUTHOR's scripts/fs_tail.c against the
   exact per-pattern bounds of R217's review_fs_fin.c (an independent implementation of Lemma 1.6), on random patterns:
   the dyadic box of fs_tail containing p = (a, z, y)/s, with SMIN = s - 1, must satisfy
   min_route exp(s phi + logk) (s+1)^polys >= exp(lbound). usage: review_fs_tailcheck_author r ntests seed */
#define main fs_tail_main
#include "fs_tail.c"
#undef main
static void setLtail(double x) { lq = x; }
#define L LFIN
#define JMAX JMAXFIN
#define mn mnfin
#define lf lffin
#define NOMAIN
#include "review_fs_fin.c"
int main(int argc, char **argv) {
  int r = atoi(argv[1]); long nt = atol(argv[2]); srand(atoi(argv[3]));
  LFIN = r * logl(3.0L); lffin[0] = 0; for (int i = 1; i < 4000; i++) lffin[i] = lffin[i - 1] + logl((long double)i);
  setLtail(r * log(3.0));
  long bad = 0, done = 0; double worst = -1e9;
  while (done < nt) {
    long s = 20 + rand() % 400;
    long a = 1 + rand() % s, z = rand() % s, y = rand() % s; long t = s - a - z - y;
    if (t < 2 || y + t < a || z < 0) continue;
    long double ex = lbound(s, a, z, y, t);
    for (int lv = 3; lv <= 9; lv++) {
      double w = ldexp(1.0, -lv);
      double a0 = floor((double)a / s / w) * w, z0 = floor((double)z / s / w) * w, y0 = floor((double)y / s / w) * w;
      box[0].lo = a0; box[0].hi = a0 + w; box[1].lo = z0; box[1].hi = z0 + w; box[2].lo = y0; box[2].hi = y0 + w;
      tau.lo = 1 - (a0 + w) - (z0 + w) - (y0 + w); if (tau.lo < 0) tau.lo = 0; tau.hi = 1 - a0 - z0 - y0;
      SMIN = s - 1;
      routes();
      double bm = 1e300;
      for (int u = 0; u < nr; u++) { double v = s * R[u].phi + R[u].logk + R[u].polys * log(s + 1.0); if (v < bm) bm = v; }
      if (bm < ex - 1e-9) { bad++; if (bad < 10) printf("BAD s=%ld a=%ld z=%ld y=%ld t=%ld lev=%d box=%.6f exact=%.6Lf\n", s, a, z, y, t, lv, bm, ex); }
      if ((double)(ex - bm) > worst) worst = (double)(ex - bm);
    }
    done++;
  }
  printf("author fs_tail: r=%d tests=%ld bad=%ld max(exact - box) = %.6f (must be <= 0)\n", r, nt, bad, worst);
  return bad ? 1 : 0;
}
