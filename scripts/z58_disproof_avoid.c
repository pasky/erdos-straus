// z58 DISPROOF §5.1: avoider sets A_D := {p : p mod d not in H_d for every d = 3 (4), d <= D} (equivalently d_min(p) > D,
// Lemma A.1 of Z57_SYNTH) among primes p = 1 (4) in [lo, hi] and in Mordell classes; conditional (★)-zero rate
// #zeros / #A_D, and the independence prediction prod_{d <= D} (1 - h_d / phi-ish) replaced by the exact local density
// dens(D) := fraction of residues n mod d hit, combined as prod (1 - |H_d|/d) (naive independence).
// Output: D  #A_D(all)  #A_D(Mordell)  zeros(all)  zeros(Mordell)  naive_pred_all
// Build: gcc -O2 -o /tmp/z58avoid scripts/z58_disproof_avoid.c -lm ; run: /tmp/z58avoid lo hi
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int tau4(ll m) { int c = 0; for (ll k = 1; k * k <= m; k++) if (m % k == 0) c += (k * k == m) ? 1 : 2; return c; }
int main(int argc, char **argv) {
  ll lo = atoll(argv[1]), hi = atoll(argv[2]); ll DMAX = 1LL << 25;
  static const ll Ds[] = {3, 7, 11, 19, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431};
  enum { ND = 25 }; long cntA[ND] = {0}, cntM[ND] = {0}, zA[ND] = {0}, zM[ND] = {0}; long nA = 0, nM = 0;
  char *comp = calloc(hi + 1, 1); for (ll i = 2; i * i <= hi; i++) if (!comp[i]) for (ll j = i * i; j <= hi; j += i) comp[j] = 1;
  static const int MM[6] = {1, 121, 169, 289, 361, 529};
  for (ll p = lo | 1; p <= hi; p += 2) {
    if ((p & 3) != 1 || comp[p]) continue;
    int isM = 0; for (int k = 0; k < 6; k++) if (p % 840 == MM[k]) isM = 1;
    ll dm = -1; ll lim = (4 * p + 1) / 3; if (lim > DMAX) lim = DMAX;
    for (ll d = 3; d <= lim; d += 4) { ll r = (d - p % d) % d; if (r && ((d + 1) / 4) % r == 0) { dm = d; break; } }
    int zero = 0;
    if (dm < 0 && (4 * p + 1) / 3 > DMAX) { fprintf(stderr, "undecided %lld\n", p); }
    if (dm < 0 && (4 * p + 1) / 3 <= DMAX) zero = 1;
    nA++; nM += isM;
    for (int k = 0; k < ND; k++) if (dm < 0 || dm > Ds[k]) { cntA[k]++; cntM[k] += isM; zA[k] += zero; zM[k] += zero && isM; }
  }
  double pr = 1; ll dd = 3;
  printf("# primes p = 1 (4) in [%lld, %lld]: %ld (Mordell %ld)\n# D  #A_D  #A_D(M)  zeros  zeros(M)  naive_indep_share  share_A  share_A(M)\n", lo, hi, nA, nM);
  for (int k = 0; k < ND; k++) {
    for (; dd <= Ds[k]; dd += 4) pr *= 1.0 - (double)tau4((dd + 1) / 4) / (double)dd;
    printf("%lld %ld %ld %ld %ld %.4e %.4e %.4e\n", Ds[k], cntA[k], cntM[k], zA[k], zM[k], pr, (double)cntA[k] / nA, (double)cntM[k] / (nM ? nM : 1));
  }
  return 0;
}
