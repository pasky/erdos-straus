// z57 SYNTH: sieve-style enumeration of ALL (★) triples 4uBC - u - B = n for odd n <= N (both orders (u,B), all C),
// recording per odd n: R(n) (capped at 65535) and R8(n) := #{triples with C even} (= the c = 1 Type II line of
// numerator 8: 8uBC' - u - B = n, C = 2C').  Output: for every prime p <= N with p = 1 (4) and R8(p) = 0 (or R(p) = 0),
// a line "p R R8"; summary counts per decade to stderr.
// Optional 2nd argument Rmax: also print every prime p = 1 (4) with R(p) <= Rmax.
// Build: gcc -O2 -o /tmp/z57tri scripts/z57_synth_tri.c -lm ; run: /tmp/z57tri N [Rmax] > out
// Memory: 2 uint16 arrays of N/2 entries (N = 1e8 -> 200 MB). Use ulimit -v.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll;
int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage: N\n"); return 1; }
  ll N = atoll(argv[1]); int Rmax = argc > 2 ? atoi(argv[2]) : 0;
  ll H = N / 2 + 1;                       // index (n-1)/2 for odd n
  uint16_t *R = calloc(H, 2), *R8 = calloc(H, 2);
  if (!R || !R8) { fprintf(stderr, "alloc\n"); return 2; }
  for (ll u = 1; 4 * u - u - 1 <= N; u++)
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 1) == 0) continue;    // n odd forces u + B odd
      ll step = 4 * u * B, n = step - u - B;
      for (ll C = 1; n <= N; C++, n += step) {
        ll i = (n - 1) / 2;
        if (R[i] < 65535) R[i]++;
        if (!(C & 1) && R8[i] < 65535) R8[i]++;
      }
    }
  // primes by simple sieve on odd numbers
  char *comp = calloc(H, 1);
  for (ll q = 3; q * q <= N; q += 2) if (!comp[(q - 1) / 2]) for (ll j = q * q; j <= N; j += 2 * q) comp[(j - 1) / 2] = 1;
  long zR = 0, z8 = 0, np = 0; double sR[20] = {0}, s8[20] = {0}, sab[20] = {0}, saa[20] = {0}, sbb[20] = {0}, sa[20] = {0}, sb[20] = {0}; long cn[20] = {0};
  for (ll p = 5; p <= N; p += 4) {
    ll i = (p - 1) / 2; if (comp[i]) continue; np++;
    if (R[i] == 0) zR++;
    if (R8[i] == 0) z8++;
    if (R[i] <= Rmax || R8[i] == 0 || R8[i] == R[i]) printf("%lld %u %u\n", p, R[i], R8[i]);
    { double L = log((double)p); int dk = (int)log10((double)p); sR[dk] += R[i] / (L * L); s8[dk] += R8[i] / (L * L); cn[dk]++;
      double a = R[i] - R8[i], b = R8[i]; sab[dk] += a * b; saa[dk] += a * a; sbb[dk] += b * b; sa[dk] += a; sb[dk] += b; }
  }
  fprintf(stderr, "N=%lld primes(1 mod 4)=%ld zeros R=%ld R8=%ld\n", N, np, zR, z8);
  for (int k = 0; k < 20; k++) if (cn[k]) { double n = cn[k], ma = sa[k] / n, mb = sb[k] / n, va = saa[k] / n - ma * ma, vb = sbb[k] / n - mb * mb;
    fprintf(stderr, "decade 1e%d: n=%ld mean R/L2=%.4f mean R8/L2=%.4f  mean(Rodd)=%.2f mean(R8)=%.2f var/mean Rodd=%.2f R8=%.2f corr(Rodd,R8)=%.3f\n",
      k, cn[k], sR[k] / n, s8[k] / n, ma, mb, va / ma, vb / mb, (sab[k] / n - ma * mb) / sqrt(va * vb)); }
  // also primes p = 3 (4) zeros of R8 (numerator-8 exceptions 131, 241 are = 3 (4)) to a side count
  long z8b = 0, npb = 0; for (ll p = 3; p <= N; p += 4) { ll i = (p - 1) / 2; if (comp[i]) continue; npb++; if (R8[i] == 0) { z8b++; if (p < 100000) fprintf(stderr, "R8zero(3mod4) %lld R=%u\n", p, R[i]); } }
  fprintf(stderr, "primes(3 mod 4)=%ld zeros R8=%ld\n", npb, z8b);
  return 0;
}
