/* review_fz1_routecheck.c (R226): EVERY route of the author's fz1_sum.c pattern_bound1 (k = 1 Case B, 19 routes), separately,
   against the R226 exact counts of review_fz1_tuples.py (lines "s a z y t count count_filtered"; s >= 2 used).
   usage: review_fz1_routecheck q < data/fz1_review/tuples_q<q>.txt */
#define NO_MAIN1
#include "fz1_sum.c"
int main(int argc, char **argv) {
  int q = atoi(argv[1]); lq = logl((LD)q); lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  init_omstar(q); init_rankin(q);
  int s, a, z, y, t; long c, cf; char line[256]; long viol = 0, pats = 0, tight[19] = {0}; LD worst[19] = {0};
  while (fgets(line, sizeof line, stdin)) {
    if (sscanf(line, "%d %d %d %d %d %ld %ld", &s, &a, &z, &y, &t, &c, &cf) != 7 || s < 2) continue;
    int am; pattern_bound1(s, a, z, y, t, &am); pats++;
    for (int i = 0; i < 19; i++) { LD bd = expl(E1[i]); LD rt = c / bd;
      if (c > bd * (1 + 1e-9L) + 1e-9L) { viol++; printf("VIOL s=%d a=%d z=%d y=%d t=%d count=%ld route %s bound %.4Lf\n", s, a, z, y, t, c, rn1[i], bd); }
      if (rt > worst[i]) worst[i] = rt; if (rt > 0.999L) tight[i]++; } }
  printf("q=%d patterns(with tuples)=%ld route-violations=%ld\n  max count/bound per route:", q, pats, viol);
  for (int i = 0; i < 19; i++) printf(" %s:%.3Lf", rn1[i], worst[i]); printf("\n");
  return viol ? 1 : 0; }
