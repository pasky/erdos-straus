/* R217: per-level exponent of the Lemma 1.6 bounds: for level s, max over patterns of (log bound)/(s log q) - 1/2, using
   R217's lbound (review_fs_fin.c). EVIDENCE-level check of fs_rate's continuum exponents. usage: review_fs_rate r s */
#define NOMAIN
#include "review_fs_fin.c"
int main(int argc, char **argv) {
  int r = atoi(argv[1]); long s = atol(argv[2]);
  L = r * logl(3.0L); lf[0] = 0; for (int i = 1; i < 4000; i++) lf[i] = lf[i - 1] + logl((LD)i);
  LD best = -1e30L; long ba = 0, bz = 0, by = 0, bt = 0;
  for (long a = 1; a <= s; a++) for (long z = 0; a + z <= s; z++) for (long y = 0; a + z + y <= s; y++) {
    long t = s - a - z - y, b = y + t; if (t < 2 || b < a) continue;
    LD e = lbound(s, a, z, y, t); if (e > best) { best = e; ba = a; bz = z; by = y; bt = t; }
  }
  printf("r=%d s=%ld max_pattern log(bound)/(s log q) - 1/2 = %+.4Lf at (a,z,y,t)/s = (%.3f, %.3f, %.3f, %.3f)\n", r, s,
         best / (s * L) - 0.5L, (double)ba / s, (double)bz / s, (double)by / s, (double)bt / s);
  return 0;
}
