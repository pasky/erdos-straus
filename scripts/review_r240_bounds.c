/* R240: print the (J)56 route bound (fz1_sum.c pattern_bound1, FF_STERILE_SMALL Lemma 7.1, reviewed in R226) for EVERY k = 1
   Case B pattern (s; a, z, y, t), a <= b, at q = 9, as natural log of the count bound. No filtering, no weighting
   (done independently in review_r240_certify.py).  usage: review_r240_bounds SMIN SMAX */
#define NO_MAIN1
#include "fz1_sum.c"
int main(int argc, char **argv) {
  int S0 = atoi(argv[1]), S = atoi(argv[2]), r = 2;
  lq = r * logl(3.0L); lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  long double q = powl(3.0L, r); init_omstar(q); init_rankin(q);
  for (int s = S0; s <= S; s++) for (int a = 0; a <= s; a++) for (int z = 0; a + z <= s; z++) { int b = s - a - z; if (b < a) continue;
    for (int y = 0; y <= b; y++) { int t = b - y, am; LD e = pattern_bound1(s, a, z, y, t, &am); printf("%d %d %d %d %d %.15Le\n", s, a, z, y, t, e); } }
  return 0;
}
