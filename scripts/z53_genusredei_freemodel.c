// z53_genusredei_freemodel.c — falsifier for hidden joint laws on all prime factors (Z53_GENUSREDEI §4).
// For n in a family (primes p ≡ 1 mod 4 / odd squares / near-squares / explicit list) and the lines
//   A_C : N = 4Cn + 1, level t = 4C (alpha = 4C, beta = 1),   C = 1..CM
//   B_d : N = n + 4d,  level t = 4d (alpha = 1,  beta = 4d),  d = 1..DM
// factor N, split N = s * (large primes > B), and compare the observed event E = [-1 in Sigma(N) mod t]
// (Sigma = subset products of prime factors with multiplicity) with the FREE MODEL: small part with its actual
// classes, large factors' classes i.i.d. uniform on (Z/t)^* conditioned only on the product law (L1).
// Also: law checks (L3 parity link, L2 for n = 4) and decoration statistics (quartic symbol at p, mutual symbols).
// usage: z53_genusredei_freemodel MODE A B [CM DM [MODEL]]   (MODEL 0 uniform, 1 harmonic-weighted, default 1)
//   MODE P: primes p ≡ 1 (4) in [A, B];  S: odd squares m^2 in [A, B];  N: primes p = m^2 + k in [A,B], k = |k| <= 12;
//   MODE L: explicit list read from stdin (one n per line), A, B ignored.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef unsigned long long u64; typedef long long i64; typedef unsigned __int128 u128;
#define BSM 61
static int CM = 15, DM = 15;
static int *pr; static int npr;
static u64 mulmod(u64 a, u64 b, u64 m) { return (u64)((u128)a * b % m); }
static u64 pw(u64 a, u64 e, u64 m) { u64 r = 1 % m; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int legendre(i64 a, u64 l) { i64 r = a % (i64)l; if (r < 0) r += l; if (r == 0) return 0; u64 v = pw(r, (l - 1) / 2, l); return v == 1 ? 1 : -1; }
static int isprime_u(u64 n) { if (n < 2) return 0; for (int i = 0; i < npr && (u64)pr[i] * pr[i] <= n; i++) if (n % pr[i] == 0) return n == (u64)pr[i]; return 1; }

static u64 mulmask(u64 S, int x, int t) { u64 R = 0; while (S) { int r = __builtin_ctzll(S); S &= S - 1; R |= 1ULL << ((r * x) % t); } return R; }
static u64 addelt(u64 S, int x, int t) { return S | mulmask(S, x, t); }

// ---- model cache ----
typedef struct { int line; u64 smask; int g; int k; double P; int used; } Ent;
#define HS (1 << 20)
static Ent *H;
static int units[64][64], nunits[64], inv_[64][64];
static u64 rng = 88172645463325252ULL;
static u64 xr(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }
static int MODEL = 1; // 0: uniform classes; 1: harmonic-weighted classes (w(a) = sum 1/l over primes B<l<=2e5, l = a mod t)
static double W[64][64];
static double wt(int t, int x) { return MODEL ? W[t][x] : 1.0; }
static double model_prob(int t, u64 smask, int g, int k) {
  int U = nunits[t]; int *u = units[t]; int target = t - 1;
  if (k == 0) return (smask >> target) & 1;
  if (k <= 3) {
    double tot = 0, hit = 0; int x[3];
    int lim1 = (k >= 2) ? U : 1, lim2 = (k >= 3) ? U : 1;
    for (int i = 0; i < lim1; i++) for (int j = 0; j < lim2; j++) {
      int nfree = 0, prod = 1; double w = 1;
      if (k >= 2) { x[nfree++] = u[i]; prod = prod * u[i] % t; w *= wt(t, u[i]); }
      if (k >= 3) { x[nfree++] = u[j]; prod = prod * u[j] % t; w *= wt(t, u[j]); }
      int last = g * inv_[t][prod] % t; x[nfree++] = last; w *= wt(t, last);
      u64 S = smask; for (int a = 0; a < nfree; a++) S = addelt(S, x[a], t);
      tot += w; if ((S >> target) & 1) hit += w;
    }
    return hit / tot;
  }
  // importance sampling: first k-1 uniform, weight = prod of wt over all k factors
  int NS = 16384; double hit = 0, tot = 0;
  for (int s = 0; s < NS; s++) {
    int prod = 1; u64 S = smask; double w = 1;
    for (int a = 0; a < k - 1; a++) { int xx = u[xr() % U]; prod = prod * xx % t; S = addelt(S, xx, t); w *= wt(t, xx); }
    int last = g * inv_[t][prod] % t; S = addelt(S, last, t); w *= wt(t, last); tot += w; if ((S >> target) & 1) hit += w;
  }
  return hit / tot;
}
static double get_model(int line, int t, u64 smask, int g, int k) {
  u64 h = (smask * 0x9E3779B97F4A7C15ULL) ^ ((u64)line << 40) ^ ((u64)g << 20) ^ (u64)k; h ^= h >> 29; h *= 0xBF58476D1CE4E5B9ULL; h ^= h >> 32;
  u64 i = h & (HS - 1);
  while (H[i].used) { if (H[i].line == line && H[i].smask == smask && H[i].g == g && H[i].k == k) return H[i].P; i = (i + 1) & (HS - 1); }
  H[i].used = 1; H[i].line = line; H[i].smask = smask; H[i].g = g; H[i].k = k; H[i].P = model_prob(t, smask, g, k); return H[i].P;
}

// ---- accumulators ----
#define NL 64
#define NSTR 12
static const char *strname[NSTR] = {"all", "p=1(8)", "p=5(8)", "1(8):2 quartic res", "1(8):2 not quartic", "1(8):p=x2+32y2", "1(8):p!=x2+32y2", "1(3):2 cubic res", "1(3):2 not cubic", "k=1", "k=2", "k>=3"};
static double O[NL][NSTR], E[NL][NSTR], V[NL][NSTR]; static long Ncnt[NL][NSTR];
static long skipsq[NL], skipgcd[NL];
// decorations
static long q4n[NL][64][2], q4h[NL][64][2];   // [line][class a][kbucket 0:k=1,1:k>=2] count of QR large factors, # quartic residues
static long parviol = 0, parchk = 0, l2viol = 0, l2chk = 0;
static long mutn[NL][64], muth[NL][64]; // k==2, s arbitrary: class of smaller factor, (l1/l2)=+1 count

static int is_x2_32y2(u64 p) { for (u64 y = 1; 32 * y * y < p; y++) { u64 r = p - 32 * y * y; u64 x = (u64)sqrtl((long double)r); while (x * x > r) x--; while ((x + 1) * (x + 1) <= r) x++; if (x * x == r) return 1; } return 0; }

static int nlines(void) { return CM + DM; }
static void line_info(int L, u64 n, u64 *N, int *t, i64 *ab, i64 *betamodp) {
  if (L < CM) { int C = L + 1; *N = 4ULL * C * n + 1; *t = 4 * C; *ab = 4LL * C; *betamodp = 1; }
  else { int d = L - CM + 1; *N = n + 4ULL * d; *t = 4 * d; *ab = 4LL * d; *betamodp = 4 * d; }
}

static void process(u64 n, int isprime_n, FILE *fl) {
  int str[NSTR]; memset(str, 0, sizeof str); str[0] = 1;
  if (isprime_n) {
    u64 p = n;
    if (p % 8 == 1) { str[1] = 1; u64 v = pw(2, (p - 1) / 4, p); if (v == 1) str[3] = 1; else str[4] = 1; if (is_x2_32y2(p)) str[5] = 1; else str[6] = 1; }
    else if (p % 8 == 5) str[2] = 1;
    if (p % 3 == 1) { if (pw(2, (p - 1) / 3, p) == 1) str[7] = 1; else str[8] = 1; }
  }
  int failall = 1; double logmodel_fail = 0;
  for (int L = 0; L < nlines(); L++) {
    u64 N; int t; i64 ab, bm; line_info(L, n, &N, &t, &ab, &bm);
    // factor
    u64 m = N; u64 fq[64]; int fe[64], nf = 0;
    for (int i = 0; i < npr && (u64)pr[i] * pr[i] <= m; i++) { if (m % pr[i] == 0) { int e = 0; while (m % pr[i] == 0) { m /= pr[i]; e++; } fq[nf] = pr[i]; fe[nf++] = e; } }
    if (m > 1) { fq[nf] = m; fe[nf++] = 1; }
    u64 Sall = 2ULL; u64 smask = 2ULL; /* bit r = residue r; start {1} */ int k = 0, sqbad = 0; u64 smallpart = 1;
    int lc[64]; u64 lq[64]; int nl = 0;
    for (int i = 0; i < nf; i++) {
      int c = fq[i] % t;
      for (int e = 0; e < fe[i]; e++) Sall = addelt(Sall, c, t);
      if (fq[i] <= BSM) { for (int e = 0; e < fe[i]; e++) { smask = addelt(smask, c, t); smallpart *= fq[i]; } }
      else { k += fe[i]; if (fe[i] > 1) sqbad = 1; lc[nl] = c; lq[nl++] = fq[i]; }
    }
    { u64 a = N % t, b = t; while (b) { u64 r = a % b; a = b; b = r; } if (a != 1) { skipgcd[L]++; continue; } } // composite n only
    int ev = (Sall >> (t - 1)) & 1;
    if (!ev) ; else failall = 0;
    if (sqbad) { skipsq[L]++; continue; }
    // g = class of N/s mod t
    int sm = smallpart % t; int g = (int)(N % t) * inv_[t][sm] % t;
    double P = get_model(L, t, smask, g, k);
    logmodel_fail += log(1 - P + 1e-300);
    int kb = k == 1 ? 9 : (k == 2 ? 10 : (k >= 3 ? 11 : -1));
    for (int s = 0; s < NSTR; s++) {
      int on = (s < 9) ? str[s] : (s == kb);
      if (!on) continue;
      O[L][s] += ev; E[L][s] += P; V[L][s] += P * (1 - P); Ncnt[L][s]++;
    }
    if (isprime_n) {
      u64 p = n;
      // L2 check n=4 (p ≡ 1 mod 4): prod over all prime factors of l^{(p-1)/4} == (beta mod p)^{(p-1)/4}
      u64 prod = 1; for (int i = 0; i < nf; i++) for (int e = 0; e < fe[i]; e++) prod = mulmod(prod, pw(fq[i], (p - 1) / 4, p), p);
      u64 rhs = pw(bm % p, (p - 1) / 4, p); l2chk++; if (prod != rhs) l2viol++;
      for (int a = 0; a < nl; a++) {
        u64 l = lq[a]; int lp = legendre(l % p, p); int chi = legendre(-ab, l); parchk++; if (lp != chi) parviol++;
        if (lp == 1) { int qr4 = pw(l % p, (p - 1) / 4, p) == 1; int kb2 = (k == 1) ? 0 : 1; q4n[L][lc[a]][kb2]++; q4h[L][lc[a]][kb2] += qr4; }
      }
      if (k == 2 && nl == 2) { int a0 = lq[0] < lq[1] ? 0 : 1; int s = legendre(lq[a0], lq[1 - a0]); mutn[L][lc[a0]]++; if (s == 1) muth[L][lc[a0]]++; }
    }
    if (fl) { fprintf(fl, "%llu\tL%d\tt=%d\tk=%d\tsm=%llu\tev=%d\tP=%.4f\n", n, L, t, k, smallpart, ev, P); }
  }
  if (fl) fprintf(fl, "%llu\tfailall=%d\tmodel_log_fail_all=%.3f\n", n, failall, logmodel_fail);
}

int main(int argc, char **argv) {
  if (argc < 4) { fprintf(stderr, "usage\n"); return 1; }
  char mode = argv[1][0]; u64 A = strtoull(argv[2], 0, 10), Bn = strtoull(argv[3], 0, 10);
  if (argc > 5) { CM = atoi(argv[4]); DM = atoi(argv[5]); }
  int LIM = 200000; char *c = calloc(LIM + 1, 1); pr = malloc(sizeof(int) * LIM); npr = 0;
  for (int i = 2; i <= LIM; i++) if (!c[i]) { pr[npr++] = i; for (long j = (long)i * i; j <= LIM; j += i) c[j] = 1; }
  for (int t = 1; t < 64; t++) { nunits[t] = 0; for (int x = 1; x < t || (t == 1 && x == 1); x++) { int a = x, b = t; while (b) { int r = a % b; a = b; b = r; } if (a == 1) units[t][nunits[t]++] = x % t; } for (int x = 0; x < t; x++) for (int y = 0; y < t; y++) if (x * y % t == 1 % t) inv_[t][x] = y; }
  if (argc > 6) MODEL = atoi(argv[6]);
  for (int t = 4; t < 64; t++) for (int i = 0; i < npr; i++) if (pr[i] > BSM) W[t][pr[i] % t] += 1.0 / pr[i];
  H = calloc(HS, sizeof(Ent));
  FILE *fl = NULL; if (mode == 'L') fl = stdout;
  long cnt = 0;
  if (mode == 'P') { for (u64 p = A | 1; p <= Bn; p += 2) if (p % 4 == 1 && isprime_u(p)) { process(p, 1, NULL); cnt++; } }
  else if (mode == 'S') { for (u64 m = 3; m * m <= Bn; m += 2) if (m * m >= A) { process(m * m, 0, NULL); cnt++; } }
  else if (mode == 'N') { for (u64 m = 2; m * m <= Bn; m++) for (int kk = -12; kk <= 12; kk++) { if (kk == 0) continue; i64 v = (i64)(m * m) + kk; if (v < (i64)A || v > (i64)Bn) continue; if (v % 4 != 1 || !isprime_u(v)) continue; process(v, 1, NULL); cnt++; } }
  else if (mode == 'L') { u64 v; while (scanf("%llu", &v) == 1) { process(v, isprime_u(v), fl); cnt++; } }
  printf("# mode %c range [%llu,%llu] count %ld CM=%d DM=%d B=%d MODEL=%d\n", mode, A, Bn, cnt, CM, DM, BSM, MODEL);
  printf("# law checks: parity link (L3) %ld/%ld violations; L2(n=4) %ld/%ld violations\n", parviol, parchk, l2viol, l2chk);
  printf("# line\tt\tstratum\tN\tobs\tmodel\tz\n");
  double chi2 = 0; int dof = 0;
  for (int L = 0; L < nlines(); L++) { u64 N; int t; i64 ab, bm; line_info(L, 1, &N, &t, &ab, &bm);
    for (int s = 0; s < NSTR; s++) { if (!Ncnt[L][s]) continue; double z = V[L][s] > 0 ? (O[L][s] - E[L][s]) / sqrt(V[L][s]) : 0; if (s > 0) { chi2 += z * z; dof++; }
      printf("%s%d\t%d\t%s\t%ld\t%.0f\t%.1f\t%+.2f\n", L < CM ? "A_C=" : "B_d=", L < CM ? L + 1 : L - CM + 1, t, strname[s], Ncnt[L][s], O[L][s], E[L][s], z); } }
  printf("# sum z^2 over non-'all' strata = %.1f (dof %d; strata overlap, rough)\n", chi2, dof);
  // stratum-difference tests: residual per instance in S minus in complement (robust to model bias common to both)
  { int pa[4][2] = {{1, 2}, {3, 4}, {5, 6}, {7, 8}}; double cz2 = 0; int cdf = 0;
    printf("# stratum-difference z (residual/instance in S1 minus S2): pairs p1/p5(8) | 2 quartic res yes/no | x2+32y2 yes/no | 2 cubic yes/no\n");
    for (int L = 0; L < nlines(); L++) { printf("%s%d", L < CM ? "A_C=" : "B_d=", L < CM ? L + 1 : L - CM + 1);
      for (int q = 0; q < 4; q++) { int a = pa[q][0], b = pa[q][1]; if (Ncnt[L][a] < 30 || Ncnt[L][b] < 30) { printf("\t   -"); continue; }
        double d = (O[L][a] - E[L][a]) / Ncnt[L][a] - (O[L][b] - E[L][b]) / Ncnt[L][b];
        double v = V[L][a] / ((double)Ncnt[L][a] * Ncnt[L][a]) + V[L][b] / ((double)Ncnt[L][b] * Ncnt[L][b]);
        double z = v > 0 ? d / sqrt(v) : 0; if (v > 0) { cz2 += z * z; cdf++; } printf("\t%+.2f", z); }
      printf("\n"); }
    printf("# sum of squared stratum-difference z = %.1f over %d correlated contrasts (descriptive diagnostic, not a calibrated chi2 test)\n", cz2, cdf); }
  printf("# skipped (large square factor): "); for (int L = 0; L < nlines(); L++) printf("%ld ", skipsq[L]); printf("\n");
  printf("# skipped (gcd(N,t)>1, composite n only): "); for (int L = 0; L < nlines(); L++) printf("%ld ", skipgcd[L]); printf("\n");
  if (mode == 'P' || mode == 'N') {
    printf("# quartic-residue rate of large QR factors by class a mod t (k>=2 lines; k=1 in brackets)\n");
    for (int L = 0; L < nlines(); L++) { u64 N; int t; i64 ab, bm; line_info(L, 1, &N, &t, &ab, &bm); printf("%s%d", L < CM ? "A_C=" : "B_d=", L < CM ? L + 1 : L - CM + 1);
      double ch = 0; int df = 0; long tn = 0, th = 0; for (int a = 0; a < t; a++) { tn += q4n[L][a][1]; th += q4h[L][a][1]; }
      double pbar = tn ? (double)th / tn : 0;
      for (int a = 0; a < t; a++) if (q4n[L][a][1] + q4n[L][a][0]) { printf("  %d:%.3f(%ld)[%.3f/%ld]", a, q4n[L][a][1] ? (double)q4h[L][a][1] / q4n[L][a][1] : -1, q4n[L][a][1], q4n[L][a][0] ? (double)q4h[L][a][0] / q4n[L][a][0] : -1, q4n[L][a][0]);
        if (q4n[L][a][1] > 20) { double e = pbar * q4n[L][a][1]; double v = e * (1 - pbar); ch += (q4h[L][a][1] - e) * (q4h[L][a][1] - e) / v; df++; } }
      printf("   | pooled %.4f chi2=%.1f dof=%d\n", pbar, ch, df - 1); }
    printf("# mutual symbol (l1/l2)=+1 rate, k=2, by class of smaller factor mod t\n");
    for (int L = 0; L < nlines(); L++) { u64 N; int t; i64 ab, bm; line_info(L, 1, &N, &t, &ab, &bm); printf("%s%d", L < CM ? "A_C=" : "B_d=", L < CM ? L + 1 : L - CM + 1);
      for (int a = 0; a < t; a++) if (mutn[L][a]) printf("  %d:%.3f(%ld)", a, (double)muth[L][a] / mutn[L][a], mutn[L][a]);
      printf("\n"); }
  }
  return 0;
}
