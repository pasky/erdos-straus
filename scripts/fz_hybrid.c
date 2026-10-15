/* fz_hybrid.c (O220): finite part of (Σ) for q = 3^r with exact per-pattern Case B counts (fz_enum output files
   DIR/e_<s>.txt, lines "s a z y t count Mx" or "... SKIP cost") where available, and the fz_sum route bound otherwise.
   A pattern's contribution is mult * min(exact, bound) * q^{1 - ceil(s/2)} (exact when present; bound is then irrelevant
   but reported). Files are trusted only if they list every pattern of their level (checked; else exit 1).
   usage: fz_hybrid r SMAX DIR   prints per-s exact part, bound part and cumulative. */
#define NO_MAIN
#include "fz_sum.c"
#include <string.h>
static long EX[200][200][200]; static char HAS[200][200][200];
int main(int argc, char **argv) {
  int r = atoi(argv[1]), S = atoi(argv[2]); const char *dir = argv[3];
  lq = r * logl(3.0L); lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  long double q = powl(3.0L, r); init_omstar(q); init_rankin(q);
  LD cum = 0, cumex = 0;
  for (int s = 3; s <= S; s++) {
    char fn[512]; snprintf(fn, sizeof fn, "%s/e_%d.txt", dir, s); FILE *f = fopen(fn, "r");
    memset(HAS, 0, sizeof HAS); int nlines = 0, npat = 0;
    if (f) { char line[256]; while (fgets(line, sizeof line, f)) { int ss, a, z, y, t; long c; char m[32];
        if (sscanf(line, "%d %d %d %d %d %31s", &ss, &a, &z, &y, &t, m) != 6 || ss != s) { fprintf(stderr, "bad line %s", line); return 1; }
        nlines++; if (!strcmp(m, "SKIP")) continue; c = atol(m); EX[a][z][y] = c; HAS[a][z][y] = 1; } fclose(f); }
    LD ex = 0, bd = 0; int nex = 0;
    for (int a = 1; a < s; a++) for (int z = 0; a + z < s; z++) { int b = s - a - z; if (b < a) continue;
      for (int y = 0; y <= b - 2; y++) { int t = b - y, am; npat++; LD mult = (a == b ? 1 : 2), w = expl((1 - (s + 1) / 2) * lq);
        if (HAS[a][z][y]) { ex += mult * EX[a][z][y] * w; nex++; } else bd += mult * expl(pattern_bound(s, a, z, y, t, &am)) * w; } }
    if (f && nlines != npat) { fprintf(stderr, "s=%d: file has %d lines, %d patterns\n", s, nlines, npat); return 1; }
    cum += ex + bd; cumex += ex;
    printf("s=%d exact_patterns=%d/%d exact=%.10Le bound=%.10Le cum=%.10Le\n", s, nex, npat, ex, bd, cum);
  }
  printf("r=%d total(3<=s<=%d)=%.12Le exact_part=%.6Le\n", r, S, cum, cumex);
  return 0;
}
