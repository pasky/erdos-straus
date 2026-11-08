// Count n <= N, n = 1 mod 8, nonsquare, that escape the explicit prime-factor criteria of Prop 3.3:
//  c1: n+4 has prime q=3(4), q>=7       c2: 4n+1 has prime q=3(4), q>=7, 4n+1 != 3q
//  c3: n+2 has prime q=5,7(8), q!=n+2   c4: 2n+1 has prime q=5,7(8), q!=2n+1
//  c5: n+3 has prime q=2(3), q>=5       c6: 3n+1 has prime q=2(3), q>=5
//  c7k: n+4k has prime q=-1(4k), 8k-1<=q<n+4k ; c8k: 4kn+1 has prime q=-1(4k), 8k-1<=q<=(4kn+1)/(8k-1)  (k=2..K)
// usage: ./escape N K
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static uint32_t *spf;
static int has_prime(long m, int (*pred)(long q, long m, long k), long k) {
  while (m > 1) { long q = spf[m]; if (pred(q, m, k)) return 1; while (m % q == 0) m /= q; }
  return 0;
}
static long cur_m; // the full number being tested
static int p1(long q, long m, long k) { return q % 4 == 3 && q >= 7; }
static int p2(long q, long m, long k) { return q % 4 == 3 && q >= 7 && cur_m != 3 * q; }
static int p3(long q, long m, long k) { return (q % 8 == 5 || q % 8 == 7) && q != cur_m; }
static int p5(long q, long m, long k) { return q % 3 == 2 && q >= 5; }
static int p7(long q, long m, long k) { return q % (4 * k) == 4 * k - 1 && q >= 8 * k - 1 && q < cur_m; }
static int p8(long q, long m, long k) { return q % (4 * k) == 4 * k - 1 && q >= 8 * k - 1 && q * (8 * k - 1) <= cur_m; }
int main(int argc, char **argv) {
  long N = atol(argv[1]); int K = atoi(argv[2]);
  long M = (4 * (long)K > 4 ? 4 * (long)K : 4) * N + 2;
  spf = calloc(M + 1, sizeof(uint32_t));
  for (long i = 2; i <= M; i++) if (!spf[i]) { spf[i] = i; if (i * i <= M) for (long j = i * i; j <= M; j += i) if (!spf[j]) spf[j] = i; }
  // escape counters: after criteria c1; c1-2; c1-4; c1-6; c1-6+k=2; ... ; c1-6+k<=K
  int nlev = 4 + (K - 1);
  long *esc = calloc(nlev, sizeof(long)); long tot = 0;
  long *last = calloc(nlev, sizeof(long));
  for (long n = 1; n <= N; n += 8) {
    long r = (long)llround(sqrt((double)n)); if (r * r == n) continue;
    tot++;
    int lev = 0;
    cur_m = n + 4; int c1 = has_prime(n + 4, p1, 0);
    cur_m = 4 * n + 1; int c2 = has_prime(4 * n + 1, p2, 0);
    cur_m = n + 2; int c3 = has_prime(n + 2, p3, 0);
    cur_m = 2 * n + 1; int c4 = has_prime(2 * n + 1, p3, 0);
    int c5 = has_prime(n + 3, p5, 0), c6 = has_prime(3 * n + 1, p5, 0);
    int ok[64]; ok[0] = c1; ok[1] = c1 | c2; ok[2] = ok[1] | c3 | c4; ok[3] = ok[2] | c5 | c6;
    int acc = ok[3];
    for (int k = 2; k <= K; k++) {
      cur_m = n + 4 * k; int c7 = has_prime(n + 4 * k, p7, k);
      cur_m = 4 * k * n + 1; int c8 = has_prime(4 * k * n + 1, p8, k);
      acc |= c7 | c8; ok[4 + k - 2] = acc;
    }
    for (int l = 0; l < nlev; l++) if (!ok[l]) { esc[l]++; last[l] = n; }
  }
  printf("N=%ld K=%d  n=1(8) nonsquare: %ld\n", N, K, tot);
  const char *nm[] = {"c1", "c1-2", "c1-4", "c1-6"};
  for (int l = 0; l < nlev; l++) {
    if (l < 4) printf("  escape %-6s : %ld  (frac %.3e, largest %ld)\n", nm[l], esc[l], (double)esc[l] / tot, last[l]);
    else printf("  escape c1-6+k<=%d: %ld  (frac %.3e, largest %ld)\n", l - 2, esc[l], (double)esc[l] / tot, last[l]);
  }
  return 0;
}
