// z57 SYNTH §3.I: zero sets of the "high-Burgess-margin" sub-families of 𝔊*_{1/15} = A ∩ G_{1/15} (Z56_FAMDESIGN §1):
// F_mu := {(★) solutions with P := min(u,B), Q := max(u,B), P^15 > n and Q^4 >= P * n^{1+4 mu}} (log-coordinates:
// x = log P/log n > 1/15, y - (1+x)/4 >= mu).  mu = 0 is F4L (validated against FAMDESIGN's 302 F4L zeros <= 1e8).
// Membership via long-double logarithms (EVIDENCE-grade at the region boundary; the margin sets are model families).
// Sieve-style enumeration over all triples with 4uBC - u - B <= N (as z57_synth_tri.c).  Output: for each prime p = 1 (4),
// p >= 1e5, with some family empty: "p h0 h1 h2 h3" (hit counts, ordered); summary to stderr.
// Build: gcc -O2 -o /tmp/z57trim scripts/z57_synth_trimargin.c -lm ; run: /tmp/z57trim N > out
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll;
static const double MU[4] = {0.0, 0.0533114024, 0.1, 0.2179029330};
int main(int argc, char **argv) {
  ll N = atoll(argv[1]); ll H = N / 2 + 1;
  uint8_t *F[4]; for (int j = 0; j < 4; j++) { F[j] = calloc(H, 1); if (!F[j]) return 2; }
  for (ll u = 1; 3 * u - 1 <= N; u++) {
    double lu = log((double)u);
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 1) == 0) continue;
      ll P = u < B ? u : B, Q = u < B ? B : u; double lP = log((double)P), lQ = log((double)Q);
      ll step = 4 * u * B, n = step - u - B;
      for (; n <= N; n += step) {
        double ln = log((double)n);
        if (15 * lP <= ln) continue;                      // P^15 > n required
        double g = 4 * lQ - lP - ln;                      // margin*4*ln = g - 4 mu ln
        ll i = (n - 1) / 2;
        for (int j = 0; j < 4; j++) if (g >= 4 * MU[j] * ln && F[j][i] < 255) F[j][i]++;
      }
    }
    (void)lu;
  }
  char *comp = calloc(H, 1);
  for (ll q = 3; q * q <= N; q += 2) if (!comp[(q - 1) / 2]) for (ll j = q * q; j <= N; j += 2 * q) comp[(j - 1) / 2] = 1;
  long z[4] = {0}, np = 0;
  for (ll p = 5; p <= N; p += 4) { ll i = (p - 1) / 2; if (comp[i]) continue; np++;
    int any = 0; for (int j = 0; j < 4; j++) if (F[j][i] == 0) { z[j]++; any = 1; }
    if (any && p >= 100000) printf("%lld %u %u %u %u\n", p, F[0][i], F[1][i], F[2][i], F[3][i]); }
  fprintf(stderr, "N=%lld primes(1 mod 4)=%ld zeros: mu=0:%ld mu=0.0533:%ld mu=0.1:%ld mu=0.2179:%ld\n", N, np, z[0], z[1], z[2], z[3]);
  return 0;
}
