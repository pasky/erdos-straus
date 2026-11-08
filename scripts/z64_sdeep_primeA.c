/* z64 SDEEP: "prime-A" sub-statement of (S).  For primes p == 1 (mod 8), p <= X: count reversal pairs of -1 words
   (t,u,v), u<v, for which A = tu-1 or A* = tv-1 is prime ("prime-A words"); print primes with none, and per-decade
   means of log-normalised counts.  gcc -O2 -o /tmp/z64pa scripts/z64_sdeep_primeA.c -lm ; /tmp/z64pa 20000000 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static uint32_t *spf;
static int jac(uint64_t a, uint64_t n) { int s = 1; a %= n; while (a) { while (!(a & 1)) { a >>= 1; uint64_t r = n & 7; if (r == 3 || r == 5) s = -s; } uint64_t t = a; a = n; n = t; if ((a & 3) == 3 && (n & 3) == 3) s = -s; a %= n; } return n == 1 ? s : 0; }
static uint64_t divs[20000];
static int ndivs(uint64_t m) { int k = 1; divs[0] = 1; while (m > 1) { uint32_t p = spf[m]; int e = 0; while (m % p == 0) { m /= p; e++; } int k0 = k; uint64_t pw = 1; for (int j = 1; j <= e; j++) { pw *= p; for (int i = 0; i < k0; i++) divs[k++] = divs[i] * pw; } } return k; }
int main(int argc, char **argv) {
  uint64_t X = strtoull(argv[1], 0, 10), L = 2 * X + 10;  /* A* = tv-1 < p, and tp+1 not needed: A* prime test needs spf up to p */
  spf = calloc(L + 1, 4);
  for (uint64_t i = 2; i <= L; i++) if (!spf[i]) for (uint64_t j = i; j <= L; j += i) if (!spf[j]) spf[j] = i;
  double sumr[12] = {0}, sumt[12] = {0}; long cntd[12] = {0}; long fails = 0;
  for (uint64_t p = 17; p <= X; p += 8) {
    if (spf[p] != p) continue;
    long negp = 0, negall = 0;
    for (uint64_t u = 2; 2 * u * (u - 1) <= p; u++) {
      uint64_t m = p + u; int k = ndivs(m);
      for (int i = 0; i < k; i++) {
        uint64_t d = divs[i];
        if (d < 2 * u - 1 || (d + 1) % u) continue;
        uint64_t v = m / d; if (v <= u) continue;
        uint64_t t = (d + 1) / u, As = t * v - 1;
        if (jac(d, p) != -1) continue;
        negall++;
        if (spf[d] == d || spf[As] == As) negp++;
      }
    }
    int dec = (int)log10((double)p);
    sumr[dec] += negp / log((double)p); sumt[dec] += negall / (log((double)p) * log((double)p)); cntd[dec]++;
    if (negp == 0) { fails++; if (fails <= 60 || p > X / 2) printf("primeA-fail %lu (all -1 pairs %ld)\n", (unsigned long)p, negall); }
  }
  for (int d = 0; d < 12; d++) if (cntd[d]) printf("decade 1e%d: primes %ld  mean primeA(-1)/log p %.4f  mean all(-1)/log^2 p %.4f\n", d, cntd[d], sumr[d] / cntd[d], sumt[d] / cntd[d]);
  printf("total primeA failures %ld\n", fails);
  return 0;
}
