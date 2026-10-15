/* zc_sum9.c (O226): q = 9, k = 1 union bound restricted to the 4 primitive slices u0 in F_9^* with u0^4 = -1
   (FF_ODD_ABSENCE §2). By Thm 1.2, a Case B tuple of pattern (s; a, z, y, t) can lie on such a slice only if 4 | s and
   eps(s; a, z, t) = (-1)^{s/4}, eps = (-1)^{t + tz + z(1+s) + ts} lam^{z+s}, lam = -1 iff a = b.
   Per s: exact part (DIR/p_<s>.txt from zc_enum with slice filter 2 = primitive slices only, lines "s a z y t count Mx",
   all compatible patterns listed) or route bound (fz1_sum.c pattern_bound1, unchanged), weighted mult * 9^{-ceil((s-1)/2)}.
   usage: zc_sum9 SMIN SMAX [DIR|-]   prints per-s parts and the total over s in [SMIN, SMAX]. */
#define NO_MAIN1
#include "fz1_sum.c"
static char SEEN[260][260][260];
int eps_ok(int s, int a, int z, int t) {
  int b = s - a - z, e = (t + t * z + z * (1 + s) + t * s) & 1;
  if (a == b && ((z + s) & 1)) e ^= 1;
  if (s % 4) return 0;
  return e == ((s / 4) & 1);
}
#ifndef NO_MAIN9
int main(int argc, char **argv) {
  int S0 = atoi(argv[1]), S = atoi(argv[2]); const char *dir = argc > 3 ? argv[3] : "-";
  int r = 2; lq = r * logl(3.0L); lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  long double q = powl(3.0L, r); init_omstar(q); init_rankin(q);
  LD cum = 0, cumex = 0, cumall = 0;
  for (int s = S0; s <= S; s++) {
    FILE *f = NULL; int nlines = 0, npat = 0;
    if (strcmp(dir, "-")) { char fn[512]; snprintf(fn, sizeof fn, "%s/p_%d.txt", dir, s); f = fopen(fn, "r"); }
    memset(HAS, 0, sizeof HAS); memset(SEEN, 0, sizeof SEEN);
    if (f) { char line[256]; while (fgets(line, sizeof line, f)) { int ss, a, z, y, t; char m[32];
        if (sscanf(line, "%d %d %d %d %d %31s", &ss, &a, &z, &y, &t, m) != 6 || ss != s) { fprintf(stderr, "bad line %s", line); return 1; }
        if (!eps_ok(s, a, z, t)) { fprintf(stderr, "incompatible pattern in file: %s", line); return 1; }
        /* R-O226 repair: fail closed on malformed / inconsistent / duplicate lines */
        if (a < 0 || z < 0 || y < 0 || a + z > s || s - a - z < a || y > s - a - z || t != s - a - z - y) { fprintf(stderr, "bad pattern %s", line); return 1; }
        if (SEEN[a][z][y]) { fprintf(stderr, "duplicate %s", line); return 1; } SEEN[a][z][y] = 1;
        nlines++; if (!strcmp(m, "SKIP")) continue;
        char *ep; long cnt = strtol(m, &ep, 10); if (*ep || cnt < 0) { fprintf(stderr, "bad count %s", line); return 1; }
        EX[a][z][y] = cnt; HAS[a][z][y] = 1; } fclose(f); }
    LD ex = 0, bd = 0, all = 0, w = expl(-((s - 1 + 1) / 2) * lq);
    for (int a = 0; a <= s; a++) for (int z = 0; a + z <= s; z++) { int b = s - a - z; if (b < a) continue;
      for (int y = 0; y <= b; y++) { int t = b - y, am; LD mult = (a == b ? 1 : 2);
        LD e = pattern_bound1(s, a, z, y, t, &am); all += mult * expl(e) * w;
        if (!eps_ok(s, a, z, t)) continue;
        npat++;
        if (getenv("ZC_PAT")) printf("P %d %d %d %d %d %.6Le\n", s, a, z, y, t, mult * expl(e) * w);
        if (HAS[a][z][y]) ex += mult * EX[a][z][y] * w; else bd += mult * expl(e) * w; } }
    if (f && nlines != npat) { fprintf(stderr, "s=%d: file has %d lines, %d compatible patterns\n", s, nlines, npat); return 1; }
    cum += ex + bd; cumex += ex; cumall += all;
    if (s % 4 == 0) printf("s=%d exact=%.6Le bound=%.10Le cum=%.10Le (unfiltered all-pattern bound %.4Le)\n", s, ex, bd, cum, all);
  }
  printf("q=9 k=1 primitive slices: total(%d<=s<=%d)=%.12Le exact_part=%.6Le\n", S0, S, cum, cumex);
  return 0;
}
#endif
