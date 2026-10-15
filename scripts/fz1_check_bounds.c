/* fz1_check_bounds.c (O220): every route of fz1_sum.c (pattern_bound1), separately, against exact k = 1 counts from
   fz1_enum output (q prime or 9). usage: fz1_enum q 2 S 99 > f; fz1_check_bounds q < f */
#define NO_MAIN1
#include "fz1_sum.c"
int main(int argc, char **argv) {
  int q = atoi(argv[1]); lq = logl((LD)q); lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  init_omstar(q); init_rankin(q);
  int s, a, z, y, t; long c; char m[32], line[256]; long viol = 0, pats = 0; LD worst = 0;
  while (fgets(line, sizeof line, stdin)) { if (sscanf(line, "%d %d %d %d %d %ld %31s", &s, &a, &z, &y, &t, &c, m) != 7) continue;
    int am; pattern_bound1(s, a, z, y, t, &am); pats++;
    for (int i = 0; i < 19; i++) { LD bd = expl(E1[i]); if (c > bd * (1 + 1e-9) + 1e-9) { viol++; printf("VIOL s=%d a=%d z=%d y=%d t=%d count=%ld route %s bound %.3Lf\n", s, a, z, y, t, c, rn1[i], bd); }
      if (c / bd > worst) worst = c / bd; } }
  printf("q=%d patterns=%ld route-violations=%ld max count/bound(any route)=%.3Lf\n", q, pats, viol, worst); return viol ? 1 : 0; }
