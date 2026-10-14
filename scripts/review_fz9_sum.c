/* review_fz9_sum.c (R221): R220's review_fz_sum.c (reviewer code, independent of the author; Lemma 1.4 + Lemma 1.3 routes,
   no tau-bound) + R221's OWN implementation of FF_STERILE_SMALL Lemma 4.1 (Rankin/fractional knapsack), applied to every
   binomial divisor count C(n, d) (all such F are prime to T, see review §3), and the R1 alternatives m' | F, w1 | F/m'
   (and permutations).  Own Lemma 4.1: rho in {k/48}, items (P, e) restricted to e*deg P <= n (an integer solution never uses
   others, so the restricted fractional knapsack is still a relaxation), V_rho(n) by greedy in long double, outward 1e-12.
   Optional exact counts: files DIR/e_<s>.txt ("s a z y t count ...") used for s <= SEX (a pattern without a line -> bound).
   usage: review_fz9_sum r S [print_every] [VMODE] [DIR SEX]
   --- original header (R220) --- */
/* review_fz_sum.c (R220): R218's review_fs2_sum.c (independent of the author) extended, from the TEXT of FF_STERILE_SMALL
   §1, by Lemma 1.4 (cls -> min_j q^j cls(n,d,rho+j)) and the Lemma 1.3 routes (v1 in a class mod the fixed factors).
   Lemma 4.1 (Rankin) is NOT used; the undocumented tau-bound of fz_sum's R10a3 is NOT used (omega* only).
   VMODE=0: V(d) = q^{t-2-d} (sharp count), VMODE=1: document's max(1, q^{t-1-d}).
   Original header: review_fs2_sum.c (R218, from scratch; written from the text of FF_STERILE_PUSH Lemma 1.6, not from fs_sum.c).
   Finite Case B part of (Σ): sum_{3<=s<=S} q^{1-ceil(s/2)} sum_{patterns a<=b} mult * min_route bound,
   q = 3^r, mult = 2 (a<b), 1 (a=b).
   Arithmetic: logs in long double (64-bit mantissa). Error budget: every log-bound is a sum of <= 6 terms, each with
   absolute error <= 1e-15 (log-factorials are cumulative sums of <= 2000 logl values, error <= 2000*2^-64*1e4 < 1e-12),
   so each exponentiated term has relative error < 1e-11; the sum of <= 1e8 positive terms adds < 1e-10 relative.
   We output total*(1+1e-8) as the certified upper bound.
   Class counts are exact integers (minimal m+k over m+k <= KMAX, Lemma 1.5; 2 by Lemma 1.4; 1 trivial).
   usage: review_fz_sum r S [print_every] [VMODE]  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long double LD;
static int q_r; static LD LQ; static LD lfac[4096];
#define KMAX 200
/* exact Coppersmith search: least K=m+k<=KMAX, m>=1, with n*A + X*(A + k*m + k(k+1)/2) < (m+k+1)*m*d */
static int cop(long n, long d, long rho) {
  long X = d - rho; if (X < 0) return 1;
  for (long K = 1; K <= KMAX; K++) for (long m = 1; m <= K; m++) {
    long k = K - m, A = m * (m + 1) / 2;
    long lhs = n * A + X * (A + k * m + k * (k + 1) / 2), rhs = (m + k + 1) * m * d;
    if (lhs < rhs) return (int)K;
  }
  return 0;
}
/* memo for cop over (n,d,rho) with n<=NMAX */
#define NMAX 700
static short *memo;  /* index n*(NMAX+1)*... too big; use (n, d, X) with X<=d<=n: map via hash */
#define HB 25
static unsigned long long *hk; static int *hv;
static int copm(long n, long d, long rho) {
  if (d < rho) return 1;
  unsigned long long key = ((unsigned long long)n << 42) | ((unsigned long long)d << 21) | (unsigned long long)rho | (1ULL << 63);
  unsigned long long h = (key * 11400714819323198485ULL) >> (64 - HB);
  for (;;) { if (hk[h] == key) return hv[h]; if (!hk[h]) break; h = (h + 1) & ((1ULL << HB) - 1); }
  int c = cop(n, d, rho); hk[h] = key; hv[h] = c; return c;
}
static LD lbin0(long n, long d) { return lfac[n] - lfac[d] - lfac[n - d]; }
/* ---- R221: Lemma 4.1 ---- */
#define NRH 48
#define NV 400
static LD VR[NRH + 1][NV + 1]; static int RANKON = 1;
typedef struct { LD ratio; long j, e; LD cnt; } ITM;
static int icmp(const void *x, const void *y) { LD a = ((const ITM *)x)->ratio, b = ((const ITM *)y)->ratio; return a < b ? 1 : a > b ? -1 : 0; }
static void rankin_init(long Q) {
  static LD Ir[NV + 1];
  for (long j = 1; j <= NV; j++) { LD sm = 0; for (long i = 1; i <= j; i++) if (j % i == 0) { long m = i; int mu = 1;
      for (long p = 2; p * p <= m; p++) if (m % p == 0) { m /= p; if (m % p == 0) { mu = 0; break; } mu = -mu; } if (mu && m > 1) mu = -mu;
      sm += mu * powl((LD)Q, (LD)(j / i)); }
    Ir[j] = sm / j - (j == 1); if (Ir[j] > 1e7L) Ir[j] = 1e7L; }   /* capacity <= NV: more copies never used */
  ITM *it = malloc(sizeof(ITM) * 400000);
  for (int k = 1; k <= NRH; k++) {
    LD rho = (LD)k / NRH; long ni = 0;
    for (long j = 1; j <= NV; j++) { LD y = powl(rho, (LD)j); if (y < 1e-4000L) break; LD Sp = 1;
      for (long e = 1; e * j <= NV; e++) { if (ni >= 400000) { fprintf(stderr, "items\n"); exit(2); } LD Se = Sp + powl(y, (LD)e); LD g = logl(Se / Sp); Sp = Se; if (!(g > 0)) break;
        it[ni].ratio = g / j; it[ni].j = j; it[ni].e = e; it[ni].cnt = Ir[j]; ni++; } }
    qsort(it, ni, sizeof(ITM), icmp);
    VR[k][0] = 0;
    for (long n = 1; n <= NV; n++) {      /* items with e*j <= n only */
      LD need = n, val = 0;
      for (long i = 0; i < ni && need > 0; i++) { if (it[i].e * it[i].j > n) continue;
        LD cap = it[i].cnt * it[i].j, tk = cap < need ? cap : need; val += tk * it[i].ratio; need -= tk; }
      VR[k][n] = val * (1 + 1e-12L) + 1e-12L;
    }
  }
  free(it);
}
static LD lbin(long n, long d) {
  LD b = lbin0(n, d);
  if (RANKON && n <= NV) { long dp = d < n - d ? d : n - d;
    for (int k = 1; k <= NRH; k++) { LD v = -dp * logl((LD)k / NRH) + VR[k][n]; if (v < b) b = v; } }
  return b;
}
/* log of class-divisor bound: min(C(n,d), 1 trivial, 2 Lenstra, m+k Coppersmith, cofactor versions if both) */
static LD lcls(long n, long d, long rho, int both) {
  LD best = lbin(n, d);
  if (d < rho || (both && n - d < rho)) return best < 0 ? best : 0.0L;
  long c = 0;
  if (3 * rho > n) c = 2;
  long c1 = copm(n, d, rho); if (c1 && (!c || c1 < c)) c = c1;
  if (both) { long c2 = copm(n, n - d, rho); if (c2 && (!c || c2 < c)) c = c2; }
  if (c && logl((LD)c) < best) best = logl((LD)c);
  return best;
}
static LD LQg;
static LD lclsr(long n, long d, long rho, int both) {   /* Lemma 1.4 */
  LD best = lcls(n, d, rho, both);
  for (long j = 1; j * LQg < best; j++) { LD c = j * LQg + lcls(n, d, rho + j, both); if (c < best) best = c; }
  return best;
}
static int VMODE = 0; static int omst[4096];
static LD lV(long e, long d) { if (VMODE == 0) return d <= e ? (e - d) * LQg : 0.0L; return d <= e + 1 ? (e + 1 - d) * LQg : 0.0L; }
static LD lN(long d) { return d <= 0 ? 0.0L : d * LQ + log1pl(-expl(-LQ)); }
static LD lSom(long e) { /* 2 q^e + (e-1)(q^e - q^{e-1}) */
  if (e <= 0) return 0.0L; return e * LQ + logl(2.0L + (e - 1) * (1.0L - expl(-LQ))); }
static const char *RN[26] = {"T0","R4'","X1","X2","R1","R2","R3","R4","R3C","R4C","R5a","R5b","R6a","R6b","R8a","R8b","R9a","R10a","R10b","D1","D1c","D2","D3","X1'","X2'","R4''"};
static LD minroute(long s, long a, long z, long y, long t, int *arg) {
  long b = y + t; LD W = lN(a - 1), WB = lN(b - 1), Z = lN(z), Y = lN(y), V = lN(t - 2), l2 = logl(2.0L);
  LD e[30];
  e[0] = Z + Y + W; e[1] = Z + W + V; e[2] = l2 + Y + V + Z; e[3] = Y + V + W;
  e[4] = V + lfac[s - 2] - lfac[z] - lfac[a - 1] - lfac[b - 1];
  { LD r1 = V + lbin(s - 2, z) + lbin(s - 2 - z, a - 1), r2 = V + lbin(s - 2, a - 1) + lbin(s - 1 - a, z),
       r3 = V + lbin(s - 2, b - 1) + lbin(s - 1 - b, z);   /* R221: F = T^{s-2}+v1, m' | F, w1 | F/m' (all prime to T) */
    if (r1 < e[4]) e[4] = r1; if (r2 < e[4]) e[4] = r2; if (r3 < e[4]) e[4] = r3; }
  e[5] = Z + Y + lclsr(s + 2 * y + z, a + y + z, y + z + 1, 1);
  e[6] = W + Y + lclsr(s - 1 + y, a + y + z, a + y, 0);
  e[7] = Z + W + lclsr(s - 2, a + y + z, a + z, 1);
  e[8] = WB + Y + lclsr(s - 1 + y, b + y + z, b + y, 0);
  e[9] = Z + WB + lclsr(z + 2 * b - 2, b + y + z, b + z, 1);
  LD c5a = lclsr(s - 1 - a, b - 1, t - 1, 1), c5b = lclsr(s - 1 - b, a - 1, t - 1, 1), c10 = lclsr(a + b - 2, a - 1, t - 1, 1);
  e[10] = V + W + c5a; e[11] = V + WB + c5b;
  e[12] = V + lbin(s - 2, a - 1) + c5a; e[13] = V + lbin(s - 2, b - 1) + c5b;
  e[14] = Y + V + lbin(s - 2, a - 1); e[15] = Y + V + lbin(s - 2, b - 1);
  e[16] = Z + V + lbin(a + b - 2, a - 1);
  e[17] = Z + l2 + lSom(t - 2) + c10;
  e[18] = l2 + lSom(t - 2) + lbin(s - 2, z) + c10;
  long ev = t - 2;
  e[19] = Z + lV(ev, z) + lbin(a + b - 2, a - 1);                       /* D1 */
  e[20] = Z + l2 + lV(ev, z) + omst[ev] * l2 + c10;                     /* D1c (omega*) */
  e[21] = W + lV(ev, a - 1) + c5a;                                      /* D2 */
  e[22] = WB + lV(ev, b - 1) + c5b;                                     /* D3 */
  e[23] = l2 + Y + Z + lV(ev, z);                                       /* X1' */
  e[24] = Y + W + lV(ev, a - 1);                                        /* X2' */
  e[25] = Z + W + lV(ev, z + a - 1);                                    /* R4'' */
  int am = 0; for (int i = 1; i < 26; i++) if (e[i] < e[am]) am = i;
  if (arg) *arg = am; return e[am];
}
int main(int argc, char **argv) {
  q_r = atoi(argv[1]); long S = atol(argv[2]); long every = argc > 3 ? atol(argv[3]) : 10;
  LQ = q_r * logl(3.0L); LQg = LQ; if (argc > 4) VMODE = atoi(argv[4]);
  const char *DIR = argc > 6 ? argv[5] : NULL; long SEX = argc > 6 ? atol(argv[6]) : 0;
  if (getenv("NORANK")) RANKON = 0;
  { long Q = 1; for (int i = 0; i < q_r; i++) Q *= 3;
    /* omega*(e): greedy, irreducible counts I'(j) (j=1: Q-1), exact in long double up to j where q^j overflows -> cap */
    LD I[64]; for (int j = 1; j < 64; j++) { LD sm = 0; for (int i = 1; i <= j; i++) if (j % i == 0) { int m = i, mu = 1;
          for (int p = 2; p * p <= m; p++) if (m % p == 0) { m /= p; if (m % p == 0) { mu = 0; break; } mu = -mu; } if (mu && m > 1) mu = -mu;
          sm += mu * powl((LD)Q, (LD)(j / i)); } I[j] = sm / j - (j == 1); }
    for (int e = 0; e < 4096; e++) { long left = e, om = 0; for (int j = 1; j < 64 && left >= j; j++) { LD tk = (LD)(left / j); if (tk > I[j]) tk = I[j]; om += (long)tk; left -= (long)tk * j; } omst[e] = (int)om; } }
  lfac[0] = 0; for (int i = 1; i < 4096; i++) lfac[i] = lfac[i - 1] + logl((LD)i);
  { long Q = 1; for (int i = 0; i < q_r; i++) Q *= 3; if (RANKON) rankin_init(Q); }
  static long EXC[40][40][40]; static char HAS[40][40][40]; LD totex = 0;
  hk = calloc(1ULL << HB, sizeof *hk); hv = calloc(1ULL << HB, sizeof *hv);
  LD tot = 0; long rc[26] = {0}, nviol = 0;
  for (long s = 3; s <= S; s++) {
    LD acc = 0, comp = 0; memset(HAS, 0, sizeof HAS);
    if (DIR && s <= SEX) { char fn[600]; snprintf(fn, sizeof fn, "%s/e_%ld.txt", DIR, s); FILE *f = fopen(fn, "r");
      if (!f) { fprintf(stderr, "missing %s\n", fn); return 1; }
      char line[300]; while (fgets(line, sizeof line, f)) { long ss, a, z, y, t, c; if (line[0] == '#') continue;
        if (sscanf(line, "%ld %ld %ld %ld %ld %ld", &ss, &a, &z, &y, &t, &c) != 6 || ss != s) continue;   /* SKIP lines -> bound */
        if (s >= 40 || a + z + y + t != s) { fprintf(stderr, "bad line\n"); return 1; }
        if (HAS[a][z][y]) { fprintf(stderr, "duplicate line\n"); return 1; }
        EXC[a][z][y] = c; HAS[a][z][y] = 1; }
      fclose(f); }
    for (long a = 1; a < s; a++) for (long z = 0; a + z < s; z++) {
      long b = s - a - z; if (b < a) continue;
      for (long y = 0; y + 2 <= b; y++) {
        int am; LD e = minroute(s, a, z, y, b - y, &am); rc[am]++;
        LD term = (a < b ? 2.0L : 1.0L) * expl(e - ((s + 1) / 2 - 1) * LQ);
        if (s < 40 && HAS[a][z][y]) { LD ex = (a < b ? 2.0L : 1.0L) * (LD)EXC[a][z][y] * expl(-((s + 1) / 2 - 1) * LQ);
          if (ex > term * (1 + 1e-9L)) { fprintf(stderr, "EXACT > BOUND s=%ld a=%ld z=%ld y=%ld: %Lg > %Lg\n", s, a, z, y, ex, term); nviol++; }
          term = ex; totex += ex; }
        LD yk = term - comp, tk = acc + yk; comp = (tk - acc) - yk; acc = tk;   /* Kahan */
      }
    }
    tot += acc;
    if (s <= 12 || s % every == 0 || s == S) printf("s=%ld term=%.12Le cum=%.12Le\n", s, acc, tot);
  }
  printf("exact_part=%.12Le bound<exact violations=%ld\n", totex, nviol);
  printf("r=%d S=%ld finite_total=%.15Le certified_upper(x(1+1e-8))=%.15Le\nargmin:", q_r, S, tot, tot * (1 + 1e-8L));
  for (int i = 0; i < 26; i++) printf(" %s:%ld", RN[i], rc[i]); printf("\n");
  return 0;
}
