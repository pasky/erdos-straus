// Enumerate all length-3 words (t,u,v), n = tuv-u-v <= N, n = 1 mod 4, and record per n which
// good sub-families are nonempty. Uses the (verified) local rule for (A/n).
// usage: ./families N [listmax]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

enum {
  F_ANY = 1, F_GOOD = 2, F_T0 = 4, F_U0 = 8, F_T3E = 16, F_T2U3 = 32, F_TN7 = 64,
  F_U4 = 128, F_T4 = 256, F_U2G = 512, F_T2G = 1024, F_ALLODD = 2048, F_U8 = 4096, F_T8 = 8192
};

static int good(long t, long u, long v, long n) {
  int tm = t & 3, um = u & 3, vm = v & 3;
  if (tm == 0) return 1;
  if (tm == 2) return (um == 0 || um == 3 || vm == 0 || vm == 3);
  if (tm == 1) return (um == 0 || vm == 0);
  if (!(u & 1) || !(v & 1)) return 1;
  return ((t * n) & 7) == 7;
}

int main(int argc, char **argv) {
  long N = atol(argv[1]);
  int listmax = argc > 2 ? atoi(argv[2]) : 20;
  uint16_t *f = calloc(N + 1, sizeof(uint16_t));
  for (long t = 2; 4 * t - 4 <= N; t++) {
    for (long u = 2;; u++) {
      long A = t * u - 1;
      if (2 * A - u > N) break;
      long vmax = (N + u) / A;
      for (long v = 2; v <= vmax; v++) {
        long n = v * A - u;
        if ((n & 3) != 1) continue;
        int g = good(t, u, v, n);
        uint16_t m = F_ANY;
        if (g) {
          m |= F_GOOD;
          if ((t & 3) == 0) m |= F_T0;
          if ((u & 3) == 0 || (v & 3) == 0) m |= F_U0;
          if ((t & 3) == 3 && (!(u & 1) || !(v & 1))) m |= F_T3E;
          if ((t & 3) == 2 && ((u & 3) == 3 || (v & 3) == 3)) m |= F_T2U3;
          if ((t & 3) == 3 && ((t * n) & 7) == 7) m |= F_TN7;
          if (u == 4 || v == 4) m |= F_U4;
          if (t == 4) m |= F_T4;
          if (u == 2 || v == 2) m |= F_U2G;
          if (t == 2) m |= F_T2G;
          if ((t & 1) && (u & 1) && (v & 1)) m |= F_ALLODD;
          if (u == 8 || v == 8) m |= F_U8;
          if (t == 8) m |= F_T8;
        }
        f[n] |= m;
      }
    }
  }
  const char *names[] = {"ANY","GOOD","T0mod4","U0mod4","T3&Ueven","T2&U3","TN7","U=4","T=4","U=2good","T=2good","ALLODD","U=8","T=8"};
  long cnt[14] = {0}, tot1 = 0, tot5 = 0, cnt5[14] = {0};
  long sqfail = 0, nonsq_fail = 0;
  for (long n = 1; n <= N; n += 4) {
    long r = (long)sqrt((double)n);
    while (r * r < n) r++;
    while (r * r > n) r--;
    int sq = (r * r == n);
    if (!(f[n] & F_ANY)) continue;
    if (sq) { if (f[n] & F_GOOD) sqfail++; continue; }
    if (!(f[n] & F_GOOD)) { nonsq_fail++; printf("COUNTEREXAMPLE %ld\n", n); }
    if ((n & 7) == 1) { tot1++; for (int b = 0; b < 14; b++) if (f[n] & (1 << b)) cnt[b]++; }
    else { tot5++; for (int b = 0; b < 14; b++) if (f[n] & (1 << b)) cnt5[b]++; }
  }
  printf("N=%ld nonsquare n=1(8) with words: %ld ; n=5(8): %ld ; square-with-good=%ld ; nonsq-without-good=%ld\n", N, tot1, tot5, sqfail, nonsq_fail);
  for (int b = 0; b < 14; b++) printf("  %-10s n=1(8): %ld lacking=%ld | n=5(8): %ld lacking=%ld\n", names[b], cnt[b], tot1 - cnt[b], cnt5[b], tot5 - cnt5[b]);
  // list smallest n = 1 (8) nonsquare lacking each family
  for (int b = 2; b < 14; b++) {
    printf("lack %s:", names[b]);
    int k = 0;
    for (long n = 1; n <= N && k < listmax; n += 8) {
      long r = (long)sqrt((double)n); while (r * r < n) r++; while (r * r > n) r--;
      if (r * r == n) continue;
      if ((f[n] & F_ANY) && !(f[n] & (1 << b))) { printf(" %ld", n); k++; }
    }
    printf("\n");
  }
  // dump flags for later use
  if (argc > 3) {
    FILE *o = fopen(argv[3], "wb");
    fwrite(f, sizeof(uint16_t), N + 1, o);
    fclose(o);
  }
  return 0;
}
