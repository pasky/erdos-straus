// z53 HYPKLOOST falsifier F1: conductor decomposition of the (*) block count at fixed n.
//
// For the block (U,2U] x (V,2V] and an integer n, the sharp block count is
//   N(n) = #{(u,B) : 4uB | n+u+B}
// and its exact Ramanujan (additive-character, grouped by conductor d) expansion is
//   N(n) = sum_{(u,B)} (1/q) sum_{d | q} c_d(n+u+B),   q = 4uB.
// We accumulate the conductor pieces into
//   * absolute dyadic bins  j = floor(log2 d)            (P_abs[j])
//   * relative dyadic bins  k = floor(log2 (q/d))         (P_rel[k], k=0 is d=q, the top conductor)
// and check that the bins sum to N(n).
// c_d(m) is evaluated multiplicatively: for l^E || q and v = v_l(m),
//   c_{l^e}(m) = phi(l^e) if e <= v, -l^v if e = v+1, 0 if e >= v+2.
// Usage: ./cond U V < list_of_n   (one integer per line; n < 2^62)
// Output (tab separated): n  N  sumcheck  P_abs[0..NA-1]  P_rel[0..NR-1]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

#define NA 40
#define NR 40
typedef unsigned long long u64;
typedef __int128 i128;

static int *spf;
static int factor(u64 x, u64 *pr, int *ex) {  // x <= table size
  int k = 0;
  while (x > 1) {
    int p = spf[x]; int e = 0;
    while (x % p == 0) { x /= p; e++; }
    pr[k] = p; ex[k] = e; k++;
  }
  return k;
}
static int ilog2(u64 x) { int r = -1; while (x) { x >>= 1; r++; } return r; }

int main(int argc, char **argv) {
  if (argc < 3) { fprintf(stderr, "usage: %s U V < ns\n", argv[0]); return 1; }
  long U = atol(argv[1]), V = atol(argv[2]);
  long M = (U > V ? U : V) * 2 + 2;
  spf = malloc(sizeof(int) * (M + 1));
  for (long i = 0; i <= M; i++) spf[i] = 0;
  for (long i = 2; i <= M; i++) if (!spf[i]) for (long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
  // read all n
  size_t cap = 1024, cnt = 0; u64 *ns = malloc(cap * sizeof(u64));
  unsigned long long t;
  while (scanf("%llu", &t) == 1) { if (cnt == cap) { cap *= 2; ns = realloc(ns, cap * sizeof(u64)); } ns[cnt++] = t; }
  double *out = malloc(sizeof(double) * cnt * (NA + NR + 2));
  long *Nout = malloc(sizeof(long) * cnt);
#pragma omp parallel for schedule(dynamic, 1)
  for (size_t idx = 0; idx < cnt; idx++) {
    u64 n = ns[idx];
    long double Pa[NA], Pr[NR];
    for (int i = 0; i < NA; i++) Pa[i] = 0;
    for (int i = 0; i < NR; i++) Pr[i] = 0;
    long N = 0;
    u64 pu[16], pb[16], pq[24]; int eu[16], eb[16], eq[24];
    for (long u = U + 1; u <= 2 * U; u++) {
      int ku = factor(u, pu, eu);
      for (long B = V + 1; B <= 2 * V; B++) {
        int kb = factor(B, pb, eb);
        // merge 4*u*B
        int kq = 0;
        pq[kq] = 2; eq[kq] = 2; kq++;
        for (int i = 0; i < ku; i++) {
          int f = -1; for (int j = 0; j < kq; j++) if (pq[j] == pu[i]) f = j;
          if (f >= 0) eq[f] += eu[i]; else { pq[kq] = pu[i]; eq[kq] = eu[i]; kq++; }
        }
        for (int i = 0; i < kb; i++) {
          int f = -1; for (int j = 0; j < kq; j++) if (pq[j] == pb[i]) f = j;
          if (f >= 0) eq[f] += eb[i]; else { pq[kq] = pb[i]; eq[kq] = eb[i]; kq++; }
        }
        u64 q = 4ULL * (u64)u * (u64)B;
        u64 m = n + (u64)u + (u64)B;
        if (m % q == 0) N++;
        // local value tables: for prime i, exponent e in 0..emax_i, value and prime power
        int emax[24]; double lv[24][64]; u64 pp[24][64];
        for (int i = 0; i < kq; i++) {
          u64 l = pq[i]; int E = eq[i];
          int v = 0; u64 mm = m; while (v < E && mm % l == 0) { mm /= l; v++; }
          int em = (v + 1 < E) ? v + 1 : E;
          emax[i] = em;
          u64 P = 1;
          for (int e = 0; e <= em; e++) {
            pp[i][e] = P;
            if (e == 0) lv[i][e] = 1.0;
            else if (e <= v) lv[i][e] = (double)(P - P / l);  // phi(l^e)
            else lv[i][e] = -(double)(P / l);                 // e == v+1: -l^v
            P *= l;
          }
        }
        // enumerate divisors with nonzero local factors
        int e[24]; for (int i = 0; i < kq; i++) e[i] = 0;
        long double invq = 1.0L / (long double)q;
        while (1) {
          u64 d = 1; double val = 1.0;
          for (int i = 0; i < kq; i++) { d *= pp[i][e[i]]; val *= lv[i][e[i]]; }
          long double c = (long double)val * invq;
          Pa[ilog2(d)] += c;
          Pr[ilog2(q / d)] += c;
          int i = 0;
          while (i < kq) { if (e[i] < emax[i]) { e[i]++; break; } e[i] = 0; i++; }
          if (i == kq) break;
        }
      }
    }
    long double s = 0; for (int i = 0; i < NA; i++) s += Pa[i];
    double *o = out + idx * (NA + NR + 2);
    o[0] = (double)s;
    for (int i = 0; i < NA; i++) o[1 + i] = (double)Pa[i];
    for (int i = 0; i < NR; i++) o[1 + NA + i] = (double)Pr[i];
    Nout[idx] = N;
  }
  for (size_t idx = 0; idx < cnt; idx++) {
    double *o = out + idx * (NA + NR + 2);
    printf("%llu\t%ld\t%.9f", ns[idx], Nout[idx], o[0]);
    for (int i = 0; i < NA + NR; i++) printf("\t%.9e", o[1 + i]);
    printf("\n");
  }
  return 0;
}
