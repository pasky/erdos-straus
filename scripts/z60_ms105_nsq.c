// z60 MS105: near-square family n = m^2 + c (c signed, c = 0 mod 8 so that n = 1 mod 8 for odd m), n < 2^64.
// Domain: odd m in [mlo, mhi], n > 0, n = 1 (4), gcd(n, 105) = 1, n not a perfect square.  d-form decision as in
// z60_ms105_sm2.c (hit verified in 128-bit arithmetic).  Output "S c mlo mhi count maxd argm unk late10 late14",
// "U c m n" (no d-form hit <= LIM; NOT a zero), "L c m n d" (first hit >= LATE).
// Usage: z60_ms105_nsq mlo mhi LIM LATE c1 [c2 ...]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64;
typedef long long i64;
typedef unsigned __int128 u128;
static int issq(u64 n) { u64 r = (u64)sqrtl((long double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++; return r * r == n; }
int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage: mlo mhi LIM LATE c...\n"); return 1; }
  u64 mlo = strtoull(argv[1], 0, 10), mhi = strtoull(argv[2], 0, 10), LIM = strtoull(argv[3], 0, 10),
      LATE = strtoull(argv[4], 0, 10);
  if (mhi > 4200000000ULL) { fprintf(stderr, "mhi too large\n"); return 1; }
  for (int ai = 5; ai < argc; ai++) {
    i64 c = strtoll(argv[ai], 0, 10);
    if (c > (1LL << 40) || c < -(1LL << 40)) { fprintf(stderr, "c out of range\n"); return 2; }
    u64 cnt = 0, maxd = 0, argm = 0, unk = 0, l10 = 0, l14 = 0;
    for (u64 m = mlo | 1; m <= mhi; m += 2) {
      i64 nn = (i64)0; u64 n;
      u128 sq = (u128)m * m;
      if (c < 0 && sq <= (u128)(-c)) continue;
      u128 nn128 = c < 0 ? sq - (u128)(-c) : sq + (u128)c;
      if (nn128 >> 64) { fprintf(stderr, "overflow\n"); return 3; }
      n = (u64)nn128;
      (void)nn;
      if ((n & 3) != 1 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0 || issq(n)) continue;
      u64 found = 0;
      for (u64 d = 3; d <= LIM; d += 4) {
        u64 rm = n % d;
        if (rm == 0) continue;
        u64 r = d - rm, A = (d + 1) >> 2;
        if (A % r == 0) {
          u64 C = A / r;
          if (((u128)n + r) % d != 0 || 4 * r * C - 1 != d) { printf("VERIFYFAIL %lld %llu\n", c, m); return 4; }
          found = d; break;
        }
      }
      cnt++;
      if (!found) { unk++; printf("U %lld %llu %llu\n", c, m, n); fflush(stdout); continue; }
      if (found > maxd) { maxd = found; argm = m; }
      if (found >= 1024) l10++;
      if (found >= 16384) l14++;
      if (found >= LATE) printf("L %lld %llu %llu %llu\n", c, m, n, found);
    }
    printf("S %lld %llu %llu %llu %llu %llu %llu %llu %llu\n", c, mlo, mhi, cnt, maxd, argm, unk, l10, l14);
    fflush(stdout);
  }
  return 0;
}
