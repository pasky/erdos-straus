/* review_fs_tailcheck.c (R217): validates the per-cube route bounds of review_fs_tail.c against the exact per-pattern
   bounds of review_fs_fin.c: for random integer patterns (s; a, z, y, t) and every level lev, the cube containing
   (a, z, y)/s (with S = s - 1) must give  min_route exp(s phi + kap) (s+1)^pi  >=  exp(lbound(pattern)).
   usage: review_fs_tailcheck r ntests seed */
#define NOMAIN
#include "review_fs_tail.c"
#undef NOMAIN
static void setLtail(double x) { L = x; }
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
    for (int lv = 2; lv <= 9; lv++) {
      ll Wl = 1LL << lv;
      /* cube containing p (any cube whose closure contains p is fine; take floor) */
      ll i = (a * Wl) / s, j = (z * Wl) / s, k = (y * Wl) / s;
      ci = i; cj = j; ck = k; lev = lv; W = Wl; S = s - 1;
      routes();
      double bm = 1e300;
      for (int u = 0; u < nr; u++) { double v = s * rt[u].phi + rt[u].kap + rt[u].pi * log(s + 1.0); if (v < bm) bm = v; }
      if (bm < ex - 1e-9) { bad++; if (bad < 10) printf("BAD s=%ld a=%ld z=%ld y=%ld t=%ld lev=%d cube=%.6f exact=%.6Lf\n", s, a, z, y, t, lv, bm, ex); }
      if ((double)(ex - bm) > worst) worst = (double)(ex - bm);
    }
    done++;
  }
  printf("r=%d tests=%ld bad=%ld max(exact - cube) = %.6f (must be <= 0)\n", r, nt, bad, worst);
  return bad ? 1 : 0;
}
