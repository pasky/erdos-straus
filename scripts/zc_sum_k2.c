/* zc_sum_k2.c (O226): fz_sum.c (k >= 2 Case B route-bound sums, FF_STERILE_PUSH/SMALL) with the parity law of
   FF_ODD_ABSENCE Cor. 1.7: a pattern (s; a, z, y, t) of (B) is empty unless eps' = (-1)^{s-2}, where
   eps' = (-1)^{t' + t'z + z(1+s') + t's'} lam^{z+s'}, s' = s-2, t' = t-2, lam = -1 iff a = b.
   usage: zc_sum_k2 r S COP every NEWR RANK PARITY   (PARITY = 0 reproduces fz_sum) */
#define NO_MAIN
#include "fz_sum.c"
static int par_ok(int s, int a, int z, int t) {
  int sp = s - 2, tp = t - 2, b = s - a - z, e = (tp + tp * z + z * (1 + sp) + tp * sp) & 1;
  if (a == b && ((z + sp) & 1)) e ^= 1;
  return e == (sp & 1);
}
int main(int argc, char **argv) {
  int r = atoi(argv[1]), S = atoi(argv[2]); COP = atoi(argv[3]); int every = atoi(argv[4]); NEWR = REF = atoi(argv[5]);
  init_omstar(powl(3.0L, r)); RANK = atoi(argv[6]); if (RANK) init_rankin(powl(3.0L, r)); int PAR = atoi(argv[7]);
  lq = r * logl(3.0L); lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  LD tot = 0;
  for (int s = 3; s <= S; s++) {
    LD acc = 0;
    for (int a = 1; a < s; a++) for (int z = 0; a + z < s; z++) {
      int b = s - a - z; if (b < a) continue;
      for (int y = 0; y <= b - 2; y++) { int t = b - y, am;
        if (PAR && !par_ok(s, a, z, t)) continue;
        LD e = pattern_bound(s, a, z, y, t, &am); acc += (a == b ? 1 : 2) * expl(e + (1 - (s + 1) / 2) * lq); } }
    tot += acc;
    if (s % every == 0) printf("s=%d term=%.6Le cum=%.6Le\n", s, acc, tot);
  }
  printf("r=%d PAR=%d total(3<=s<=%d)=%.10Le\n", r, PAR, S, tot);
  return 0;
}
