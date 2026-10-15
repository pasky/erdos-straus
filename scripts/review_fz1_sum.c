/* review_fz1_sum.c (R226): independent finite Case B part of the k = 1 union bound (FF_STERILE_SMALL §7), written from the
   TEXT of §6/§7 and FF_STERILE_PUSH Lemmas 1.3-1.5 / FF_STERILE_SMALL Lemmas 1.1, 1.3, 1.4 — NOT from fz1_sum.c / fz_sum.c.
   Tuples (B^{k=1}): m'wC = T^s + v, w + C = g'v, m', g', w, C monic, T not dividing m'g'wCv; a = deg w <= b = deg C,
   z = deg m', y = deg g', t = deg v, s = a + b + z, y + t = b; lc(v) = lc(w + C) fixed by the pattern.
   Weight q^{-ceil((s-1)/2)}; mult 2 for a < b (w <-> C), 1 for a = b.
   Routes (each: data fixed -> tuple determined; all derived by R226, see review §3):
     T0 (m',g',w) -> E = m'g'w - 1, C = (g'T^s + w)/E          N(z)N(y)N(a)
     R4' (m',w, v == -T^s mod m'w) -> C                          N(z)N(a)V(t, z+a)
     X1 (m',g', v == -T^s mod m'): w, C roots of quadratic      2 N(z)N(y)V(t, z)
     X2 (g', w, v == -T^s mod w) -> C = g'v - w                 N(y)N(a)V(t, a);  X2C same with C: N(y)N(b)V(t, b)
     W1 (C, v == -T^s mod C), w == -C mod v, deg a              N(b)V(t, b) q^{max(0, a - t)}
     R1 v, ordered factorisation (m', w, C) of T^s + v           Nv(t) s!/(z!a!b!)
     R2 (m',g'): E | 1 + T^s m'g'^2, E == -1 mod L'               N(z)N(y) clsr(s+z+2y, a+y+z, y+z, cof)
     R3 (w,g'):  E | g'T^s + w,      E == -1 mod g'w              N(a)N(y) clsr(s+y, a+y+z, a+y, E-only)
     R4 (m',w):  E | T^s + m'w^2,    E == -1 mod m'w              N(z)N(a) clsr(s, a+y+z, z+a, cof)
     R3C, R4C: same with C, E' = L'C - 1                          N(b)N(y) clsr(s+y, b+y+z, b+y, E-only); N(z)N(b) clsr(z+2b, b+y+z, z+b, cof)
     R5a (w, v in class mod w): C | m'C = (T^s+v)/w, C == -w mod v   N(a)V(t,a) clsr(z+b, b, t, cof);  R5b symmetric
     R6a v, w | T^s + v (C(s,a)), then C as R5a                   Nv(t) C(s,a) clsr(z+b, b, t, cof);   R6b symmetric
     R8a (g', v), w | T^s + v, C = g'v - w                       N(y) Nv(t) C(s,a)
     R9a (m', v in class mod m'), w | wC                          N(z) V(t,z) C(a+b, a)
   N(d) = q^d - q^{d-1} (monic, T-free; 1 if d = 0); Nv(t) = (q-1) q^{t-1} (fixed lc, v(0) != 0; 1 if t = 0);
   V(t, d) = min(Nv(t), q^{t-d}) if d <= t, else 1 (Lemma 1.1/1.3: v == -T^s mod D, D monic factor of m'wC).
   clsr(n, d, rho, cof) = min_{j >= 0} q^j cls(n, d, rho + j) (FF_STERILE_SMALL Lemma 1.4: every counted divisor is prime
   to T, every F is prime to T and to Q); cls = min(C(n,d), 1 if d < rho [or n - d < rho, cof], 2 if 3 rho > n (PUSH Lemma 1.4),
   m + k for the least m + k <= 60 satisfying PUSH Lemma 1.5 (C) for (n, d, rho) [or (n, n-d, rho), cof]).
   NO Rankin bound, NO omega-star or 2^omega routes.
   Optional exact counts: file with lines "s a z y t count" (a <= b convention, a = b both orders) for complete levels s <= SEX.
   Arithmetic: long double logs; each term has relative error < 1e-12; output total * (1 + 1e-9).
   usage: review_fz1_sum r S [exact_file SEX] */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long double LD;
static LD LQ, Q; static LD lfac[2000];
static LD lbin(int n, int d) { if (d < 0 || d > n) return -1e30L; return lfac[n] - lfac[d] - lfac[n - d]; }
static LD V_(int t, int d);
/* exact maxima over monic T-free F of degree <= n: TAU[n] = log max tau(F), TAU3[n] = log max tau_3(F) (ordered triples),
   by DP over irreducible degrees j (I(1) = q - 1, I(j) = (1/j) sum mu(i) q^{j/i}): within degree j the best way to
   spread total exponent K over m = min(I(j), K) primes is balanced (log-concavity of e -> e+1 and e -> C(e+2,2)). */
#define TN 1200
static LD TAU[TN + 1], TAU3[TN + 1];
static LD nirr(int j) { if (j * LQ > 100) return 1e30L;   /* I(j) >= (q^j - 2 q^{j/2})/j > 10^40: more than any n <= TN can use */
  LD s = 0; for (int i = 1; i <= j; i++) if (j % i == 0) { int m = i, mu = 1;
    for (int p = 2; p * p <= m; p++) if (m % p == 0) { m /= p; if (m % p == 0) { mu = 0; break; } mu = -mu; } if (mu && m > 1) mu = -mu;
    LD e = (LD)(j / i) * LQ; s += mu * (e > 11000 ? 1e4000L : expl(e)); } s /= j; if (j == 1) s -= 1; return s; }
static void init_tau(void) {
  static LD cur[TN + 1], nxt[TN + 1];
  for (int k3 = 0; k3 < 2; k3++) {
    for (int n = 0; n <= TN; n++) cur[n] = 0;
    for (int j = 1; j <= TN; j++) { LD I = nirr(j);
      for (int n = 0; n <= TN; n++) nxt[n] = cur[n];
      for (int K = 1; K * j <= TN; K++) { LD m = I < K ? I : K; long mm = (long)m; if (mm < 1) break;
        long e = K / mm, rr = K % mm;   /* rr primes with exponent e+1, mm - rr with e */
        LD f = k3 ? rr * logl((LD)(e + 3) * (e + 2) / 2) + (mm - rr) * logl((LD)(e + 2) * (e + 1) / 2)
                  : rr * logl((LD)(e + 2)) + (mm - rr) * logl((LD)(e + 1));
        for (int n = K * j; n <= TN; n++) { LD c = cur[n - K * j] + f; if (c > nxt[n]) nxt[n] = c; } }
      for (int n = 0; n <= TN; n++) cur[n] = nxt[n]; }
    for (int n = 0; n <= TN; n++) (k3 ? TAU3 : TAU)[n] = cur[n] * (1 + 1e-12L) + 1e-12L; }
}
/* Rankin: #{monic D | F, deg D = d} <= x^{-d'} sum_{D | F} x^{deg D} = x^{-d'} prod_P S_{e_P}(x^{deg P}), d' = min(d, n - d)
   (D <-> F/D), 0 < x <= 1; maximised over T-free F of degree <= n by the same DP (log S_e(x^j) is concave in e). */
#define RN_ 260
#define NX 48
static LD RK[NX][RN_ + 1], LX[NX];
static void init_rk(void) {
  static LD cur[RN_ + 1], nxt[RN_ + 1];
  for (int k = 0; k < NX; k++) { LD x = (k + 1.0L) / NX; LX[k] = logl(x);
    for (int n = 0; n <= RN_; n++) cur[n] = 0;
    for (int j = 1; j <= RN_; j++) { LD I = nirr(j), y = powl(x, j);
      for (int n = 0; n <= RN_; n++) nxt[n] = cur[n];
      for (int K = 1; K * j <= RN_; K++) { LD m = I < K ? I : K; long mm = (long)m; if (mm < 1) break;
        long e = K / mm, rr = K % mm; LD Se = 0, Se1 = 0, p = 1;
        for (long i = 0; i <= e + 1; i++) { if (i <= e) Se += p; Se1 += p; p *= y; }
        LD f = rr * logl(Se1) + (mm - rr) * logl(Se);
        for (int n = K * j; n <= RN_; n++) { LD c = cur[n - K * j] + f; if (c > nxt[n]) nxt[n] = c; } }
      for (int n = 0; n <= RN_; n++) cur[n] = nxt[n]; }
    for (int n = 0; n <= RN_; n++) RK[k][n] = cur[n] * (1 + 1e-12L) + 1e-12L; }
}
static int NORK = 0;
static int OMS[TN + 1];   /* omega*(e): max # distinct monic irreducibles != T of total degree <= e (greedy by degree) */
static void init_oms(void) { for (int e = 0; e <= TN; e++) { int left = e, om = 0;
    for (int j = 1; j <= e && left >= j; j++) { LD I = nirr(j); long take = left / j; if ((LD)take > I) take = (long)I; om += take; left -= take * j; }
    OMS[e] = om; } }
/* log sum_{v: deg t, fixed lc, v == sigma (mod D), deg D = d, sigma unit} 2^omega(v):
   <= min( V(t,d) 2^{omega*(t)},  2 sum_{j=0}^{t/2} q^j max(1, q^{t-d-j}) )   [2^omega <= tau <= 2 #{delta | v, deg <= t/2},
   delta coprime to D, v in a class mod D delta] */
static LD SomCl(int t, int d) { LD a = V_(t, d) + OMS[t] * logl(2.0L);
  LD sm = 0; for (int j = 0; j <= t / 2; j++) sm += expl(j * LQ + (t - d - j > 0 ? (t - d - j) * LQ : 0.0L) - t * LQ);
  LD b = logl(2.0L * sm) + t * LQ; return a < b ? a : b; }
/* log sum_{v monic deg t} 2^omega(v) = q^t (2 + (t-1)(1 - 1/q)), t >= 1 (sum over squarefree d | v) */
static LD Som(int t) { return t <= 0 ? 0.0L : t * LQ + logl(2.0L + (t - 1) * (1.0L - 1.0L / Q)); }
static LD ldivc(int n, int d) { LD b = lbin(n, d); if (n <= TN && TAU[n] < b) b = TAU[n];
  if (!NORK && n <= RN_) { int dp = d < n - d ? d : n - d; for (int k = 0; k < NX; k++) { LD c = -dp * LX[k] + RK[k][n]; if (c < b) b = c; } }
  return b; }
static LD N_(int d) { return d <= 0 ? 0.0L : d * LQ + log1pl(-1.0L / Q); }
static LD Nv(int t) { return t <= 0 ? 0.0L : logl(Q - 1) + (t - 1) * LQ; }
static LD V_(int t, int d) { if (d > t) return 0.0L; LD x = (t - d) * LQ, y = Nv(t); return x < y ? x : y; }
static int copC(long n, long d, long rho) {   /* least m + k (<= 60) with Delta(m,k) < (m+k+1) m d, X = d - rho >= 0 */
  long X = d - rho;
  for (long K = 1; K <= 60; K++) for (long m = 1; m <= K; m++) { long k = K - m;
      long A = m * (m + 1) / 2, lhs = n * A + X * (A + k * m + k * (k + 1) / 2), rhs = (m + k + 1) * m * d;
      if (lhs < rhs) return (int)K; }
  return 0;
}
static LD lcls(int n, int d, int rho, int cof) {
  LD best = ldivc(n, d);
  if (d < rho || (cof && n - d < rho)) return best < 0 ? best : 0.0L;
  int c = 0;
  if (3 * rho > n) c = 2;
  int c1 = copC(n, d, rho); if (c1 && (!c || c1 < c)) c = c1;
  if (cof) { int c2 = copC(n, n - d, rho); if (c2 && (!c || c2 < c)) c = c2; }
  if (c && logl((LD)c) < best) best = logl((LD)c);
  return best;
}
/* memo */
static LD *memo; static int MN = 260;
static LD lclsr(int n, int d, int rho, int cof) {
  if (n >= MN || d >= MN || rho >= MN || n < 0 || d < 0) { fprintf(stderr, "range %d %d %d\n", n, d, rho); exit(2); }
  size_t idx = (((size_t)n * MN + d) * MN + rho) * 2 + cof;
  if (memo[idx] > -1e29L) return memo[idx];
  LD best = lcls(n, d, rho, cof);
  for (int j = 1; j <= d - rho + 1; j++) { if (j * LQ >= best) break; LD c = j * LQ + lcls(n, d, rho + j, cof); if (c < best) best = c; }
  memo[idx] = best; return best;
}
static const char *RN[] = {"T0","R4'","X1","X2","X2C","W1","R1","R2","R3","R4","R3C","R4C","R5a","R5b","R6a","R6b","R8a","R9a","R10a","R10b"};
#define NRT 20
static LD route[NRT];
static LD minroute(int s, int a, int z, int y, int t, int *arg) {
  int b = y + t; LD l2 = logl(2.0L);
  LD *e = route;
  e[0] = N_(z) + N_(y) + N_(a);
  e[1] = N_(z) + N_(a) + V_(t, z + a);
  e[2] = l2 + N_(z) + N_(y) + V_(t, z);
  e[3] = N_(y) + N_(a) + V_(t, a);
  e[4] = N_(y) + N_(b) + V_(t, b);
  e[5] = N_(b) + V_(t, b) + (a >= t ? (a - t) * LQ : 0.0L);
  e[6] = Nv(t) + lfac[s] - lfac[z] - lfac[a] - lfac[b]; if (TAU3[s] < e[6] - Nv(t)) e[6] = Nv(t) + TAU3[s];
  e[7] = N_(z) + N_(y) + lclsr(s + z + 2 * y, a + y + z, y + z, 1);
  e[8] = N_(a) + N_(y) + lclsr(s + y, a + y + z, a + y, 0);
  e[9] = N_(z) + N_(a) + lclsr(s, a + y + z, z + a, 1);
  e[10] = N_(b) + N_(y) + lclsr(s + y, b + y + z, b + y, 0);
  e[11] = N_(z) + N_(b) + lclsr(z + 2 * b, b + y + z, z + b, 1);
  e[12] = N_(a) + V_(t, a) + lclsr(z + b, b, t, 1);
  e[13] = N_(b) + V_(t, b) + lclsr(z + a, a, t, 1);
  e[14] = Nv(t) + ldivc(s, a) + lclsr(z + b, b, t, 1);
  e[15] = Nv(t) + ldivc(s, b) + lclsr(z + a, a, t, 1);
  e[16] = N_(y) + Nv(t) + ldivc(s, a);
  e[17] = N_(z) + V_(t, z) + ldivc(a + b, a);
  /* R10a: (m', v in class mod m'), w^2 == -G (mod v), G = (T^s+v)/m' = wC a unit mod v: <= 2^omega(v) classes (q odd),
     w | G of degree a in one class: clsr(a+b, a, t, cof).  Sum over v of 2^omega(v): Som_class(t, z).
     R10b: v free (Sum 2^omega(v) <= Som(t)), m' | T^s + v (ldivc(s, z)), then as R10a. */
  e[18] = N_(z) + SomCl(t, z) + lclsr(a + b, a, t, 1);
  e[19] = Som(t) + ldivc(s, z) + lclsr(a + b, a, t, 1);
  int am = 0; for (int i = 1; i < NRT; i++) if (e[i] < e[am]) am = i;
  if (arg) *arg = am; return e[am];
}

int main(int argc, char **argv) {
  int r = atoi(argv[1]), S = atoi(argv[2]); const char *ef = argc > 3 ? argv[3] : NULL; int SEX = argc > 4 ? atoi(argv[4]) : 0;
  int CHECK = getenv("R226_CHECK") != NULL;
  Q = powl(3.0L, r); if (getenv("R226_Q")) Q = atof(getenv("R226_Q")); LQ = logl(Q);
  lfac[0] = 0; for (int i = 1; i < 2000; i++) lfac[i] = lfac[i - 1] + logl((LD)i);
  init_tau(); init_rk(); init_oms(); NORK = getenv("R226_NORK") != NULL; if (getenv("R226_NOTAU")) for (int n = 0; n <= TN; n++) TAU[n] = TAU3[n] = 1e30L;
  memo = malloc(sizeof(LD) * (size_t)MN * MN * MN * 2); for (size_t i = 0; i < (size_t)MN * MN * MN * 2; i++) memo[i] = -1e30L;
  if (CHECK) {   /* per-route check against exact counts on stdin: "s a z y t count [..]" */
    char line[256]; int s, a, z, y, t; long c; long viol = 0, n = 0; LD worst[NRT] = {0};
    while (fgets(line, sizeof line, stdin)) { if (sscanf(line, "%d %d %d %d %d %ld", &s, &a, &z, &y, &t, &c) != 6 || s < 2) continue;
      n++; minroute(s, a, z, y, t, NULL);
      for (int i = 0; i < NRT; i++) { LD bd = expl(route[i]); if (c > bd * (1 + 1e-9L) + 1e-9L) { viol++; printf("VIOL s=%d a=%d z=%d y=%d t=%d c=%ld %s %.3Lf\n", s, a, z, y, t, c, RN[i], bd); }
        if (c / bd > worst[i]) worst[i] = c / bd; } }
    printf("q=%.0Lf patterns=%ld violations=%ld max count/bound:", Q, n, viol); for (int i = 0; i < NRT; i++) printf(" %s:%.3Lf", RN[i], worst[i]); printf("\n");
    return viol ? 1 : 0;
  }
  int COL = getenv("R226_COL") ? atoi(getenv("R226_COL")) : 6;   /* 6: total count, 7: filtered count (E(0) not in F_3) */
  if (ef) { FILE *f = fopen(ef, "r"); if (!f) { perror(ef); return 1; } fclose(f); }
  /* exact counts: re-read into a per-s map keyed by (a, z, y) */
  static long EXc[100][100][100]; static char EXh[100][100][100];
  LD tot = 0; long rc[NRT] = {0};
  for (int s = 2; s <= S; s++) {
    memset(EXh, 0, sizeof EXh);
    int useex = ef && s <= SEX;
    if (useex) { FILE *f = fopen(ef, "r"); char line[256]; int ss, a, z, y, t; long c;
      while (fgets(line, sizeof line, f)) { long c7 = -1; int nf = sscanf(line, "%d %d %d %d %d %ld %ld", &ss, &a, &z, &y, &t, &c, &c7);
        if (nf < 6 || (COL == 7 && nf < 7)) { fprintf(stderr, "bad line %s", line); return 1; }
        if (COL == 7) c = c7;
        if (ss == s) { if (y + t != s - a - z) { fprintf(stderr, "inconsistent pattern\n"); return 1; } EXc[a][z][y] = c; EXh[a][z][y] = 1; } }
      fclose(f); }
    LD acc = 0, comp = 0, w = -(LD)((s - 1 + 1) / 2) * LQ;   /* log q^{-ceil((s-1)/2)} */
    for (int a = 0; a <= s; a++) for (int z = 0; a + z <= s; z++) { int b = s - a - z; if (b < a) continue;
      for (int y = 0; y <= b; y++) { int t = b - y; LD mult = (a < b ? 2.0L : 1.0L), term;
        if (useex) term = EXh[a][z][y] ? mult * EXc[a][z][y] * expl(w) : 0.0L;   /* complete level: absent = 0 */
        else { int am; LD e = minroute(s, a, z, y, t, &am); rc[am]++; term = mult * expl(e + w);
          if (getenv("R226_DUMP") && atoi(getenv("R226_DUMP")) == s) printf("P %d %d %d %d %.6Le %s\n", a, z, y, t, expl(e), RN[am]); }
        LD yk = term - comp, tk = acc + yk; comp = (tk - acc) - yk; acc = tk; } }
    tot += acc;
    if (s <= 16 || s % 10 == 0 || s == S) printf("s=%d %s term=%.10Le cum=%.10Le\n", s, useex ? "EXACT" : "bound", acc, tot);
  }
  printf("r=%d S=%d finite_total=%.12Le certified(x(1+1e-9))=%.12Le\nargmin:", r, S, tot, tot * (1 + 1e-9L));
  for (int i = 0; i < NRT; i++) printf(" %s:%ld", RN[i], rc[i]); printf("\n");
  return 0;
}
