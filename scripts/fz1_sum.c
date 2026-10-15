/* fz1_sum.c (O220): union-bound mass of Case B tuples for A = T (k = 1), q = 3^r, on the slices u0 in F_q^* \ F_3^*
   (FF_STERILE_SMALL §6-§7). Tuples (B^{k=1}): m'wC = T^s + v, w + C = g'v, all monic, T not dividing m'g'wCv; degrees
   a = deg w <= b = deg C, z = deg m', y = deg g', t = deg v, a + b + z = s, y + t = b; relative mass q^{-ceil((s-1)/2)}.
   Routes: FF_STERILE_SMALL §7 table (k = 1 versions of FF_STERILE_PUSH Lemma 1.6 + FF_STERILE_SMALL Lemmas 1.1-1.4, 4.1).
   Helpers (class bounds with T-adic refinement, Rankin divisor bound, omega*, tau-bound) from fz_sum.c.
   Optional exact counts: DIR/e_<s>.txt from fz1_enum (lines "s a z y t count Mx" or "... SKIP cost"), all patterns listed.
   usage: fz1_sum r SMAX [DIR|-] [every]  prints per-s exact/bound parts and the total. */
#define NO_MAIN
#include "fz_sum.c"
#include <string.h>
static LD logNv(int t) { return t <= 0 ? 0.0L : logl((LD)(expl(lq) - 1)) + (t - 1) * lq; }   /* v: deg t, fixed lc, v(0) != 0 */
static LD logVv(int t, int d) { LD a = d <= t ? (t - d) * lq : 0.0L, b = logNv(t); return a < b ? a : b; }  /* v in a class mod D */
static LD min2(LD x, LD y) { return x < y ? x : y; }
static LD E1[19];
static const char *rn1[] = {"T0","R4'","X1","X2","R1","R2","R3","R4","R3C","R4C","R5a","R5b","R6a","R6b","R8a","R8b","R9a","R10a","R10b"};
LD pattern_bound1(int s, int a, int z, int y, int t, int *arg) {
  int b = y + t;
  LD W = Ns(a), WB = Ns(b), Z = Ns(z), Y = Ns(y), NV = logNv(t), L2 = logl(2.0L);
  LD e[19];
  e[0] = Z + Y + W;                                              /* (m', g', w) -> E = L'w - 1, C = (g'T^s + w)/E */
  e[1] = Z + W + logVv(t, z + a);                                /* (m', w, v), v == -T^s mod m'w */
  e[2] = L2 + Y + Z + logVv(t, z);                               /* (m', g', v): w, C roots of a quadratic */
  e[3] = Y + W + logVv(t, a);                                    /* (g', v, w) */
  { LD m = lfact[s] - lfact[z] - lfact[a] - lfact[b];            /* v, then (m', w, C) | T^s + v */
    m = min2(m, lD(s, z) + lD(s - z, a)); m = min2(m, lD(s, a) + lD(s - a, z)); m = min2(m, lD(s, b) + lD(s - b, z));
    e[4] = NV + m; }
  e[5] = Z + Y + divc(s + 2 * y + z, a + y + z, y + z, 1);       /* (m', g'): E | 1 + T^s m'g'^2, E == -1 mod L' */
  e[6] = W + Y + divc(s + y, a + y + z, a + y, 0);               /* (w, g'): E | g'T^s + w, E == -1 mod w g' */
  e[7] = Z + W + divc(s, a + y + z, z + a, 1);                   /* (m', w): E | T^s + m'w^2, E == -1 mod m'w */
  e[8] = WB + Y + divc(s + y, b + y + z, b + y, 0);              /* (C, g') */
  e[9] = Z + WB + divc(z + 2 * b, b + y + z, z + b, 1);          /* (m', C) */
  e[10] = W + logVv(t, a) + divc(s - a, b, t, 1);                /* (w, v): C | m'C, C == -w mod v */
  e[11] = WB + logVv(t, b) + divc(s - b, a, t, 1);               /* (C, v) */
  e[12] = NV + lD(s, a) + divc(s - a, b, t, 1);                  /* v, w | T^s + v, then C */
  e[13] = NV + lD(s, b) + divc(s - b, a, t, 1);
  e[14] = Y + NV + lD(s, a);                                     /* (g', v), w | T^s + v, C = g'v - w */
  e[15] = Y + NV + lD(s, b);
  e[16] = Z + logVv(t, z) + lD(a + b, a);                        /* (m', v), w | wC */
  e[17] = Z + logSomClass(t, z) + divc(a + b, a, t, 1);          /* (m', v), w in <= 2^omega(v) sqrt classes mod v */
  e[18] = Somega(t) + lD(s, z) + divc(a + b, a, t, 1);           /* v, m' | T^s + v, classes */
  for (int i = 0; i < 19; i++) E1[i] = e[i];
  int am = 0; for (int i = 1; i < 19; i++) if (e[i] < e[am]) am = i;
  if (arg) *arg = am;
  return e[am];
}
static long EX[260][260][260]; static char HAS[260][260][260];
#ifndef NO_MAIN1
int main(int argc, char **argv) {
  int r = atoi(argv[1]), S = atoi(argv[2]); const char *dir = argc > 3 ? argv[3] : "-"; int every = argc > 4 ? atoi(argv[4]) : 10;
  lq = r * logl(3.0L); lfact[0] = 0; for (int i = 1; i < NF; i++) lfact[i] = lfact[i - 1] + logl((LD)i);
  long double q = powl(3.0L, r); init_omstar(q); init_rankin(q);
  LD cum = 0, cumex = 0; long cnt[19] = {0};
  for (int s = 2; s <= S; s++) {
    FILE *f = NULL; int nlines = 0, npat = 0;
    if (strcmp(dir, "-")) { char fn[512]; snprintf(fn, sizeof fn, "%s/e_%d.txt", dir, s); f = fopen(fn, "r"); }
    memset(HAS, 0, sizeof HAS);
    if (f) { char line[256]; while (fgets(line, sizeof line, f)) { int ss, a, z, y, t; char m[32];
        if (sscanf(line, "%d %d %d %d %d %31s", &ss, &a, &z, &y, &t, m) != 6 || ss != s) { fprintf(stderr, "bad line %s", line); return 1; }
        nlines++; if (!strcmp(m, "SKIP")) continue; EX[a][z][y] = atol(m); HAS[a][z][y] = 1; } fclose(f); }
    LD ex = 0, bd = 0, w = expl(-((s - 1 + 1) / 2) * lq);      /* q^{-ceil((s-1)/2)} */
    for (int a = 0; a <= s; a++) for (int z = 0; a + z <= s; z++) { int b = s - a - z; if (b < a) continue;
      for (int y = 0; y <= b; y++) { int t = b - y, am; npat++; LD mult = (a == b ? 1 : 2);
        if (HAS[a][z][y]) ex += mult * EX[a][z][y] * w;
        else { LD e = pattern_bound1(s, a, z, y, t, &am); cnt[am]++; bd += mult * expl(e) * w; } } }
    if (f && nlines != npat) { fprintf(stderr, "s=%d: file has %d lines, %d patterns\n", s, nlines, npat); return 1; }
    cum += ex + bd; cumex += ex;
    if (s <= 14 || s % every == 0) printf("s=%d exact=%.6Le bound=%.10Le cum=%.10Le\n", s, ex, bd, cum);
  }
  printf("r=%d k=1 total(2<=s<=%d)=%.12Le exact_part=%.6Le\nroute argmin counts:", r, S, cum, cumex);
  for (int i = 0; i < 19; i++) printf(" %s:%ld", rn1[i], cnt[i]);
  printf("\n");
  return 0;
}
#endif
