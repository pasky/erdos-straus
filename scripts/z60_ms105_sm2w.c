// z60 MS105: n = s*m^2 family search in m-windows beyond 2^64 (n < 2^127).
// Same d-form decision as z60_ms105_sm2.c, but n mod d is computed as s*(m mod d)^2 mod d (d < 2^31), so m < 2^63 and
// s < 2^31 are allowed; every first hit is re-verified in 128-bit arithmetic: (n + r) % d == 0 and 4rC - 1 == d.
// Domain per s: odd m in [mlo, mhi] with gcd(m, 105) = 1.  Output as z60_ms105_sm2.c ("S ..." summary, "U s m" for no
// d-form hit <= LIM (NOT a zero), "L s m d" for first hit >= LATE).
// Usage: z60_ms105_sm2w mlo mhi LIM LATE s1 [s2 ...]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;
int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage: mlo mhi LIM LATE s...\n"); return 1; }
  u64 mlo = strtoull(argv[1], 0, 10), mhi = strtoull(argv[2], 0, 10), LIM = strtoull(argv[3], 0, 10),
      LATE = strtoull(argv[4], 0, 10);
  if (LIM >= (1ULL << 31) || mhi >= (1ULL << 63)) { fprintf(stderr, "range\n"); return 1; }
  for (int ai = 5; ai < argc; ai++) {
    u64 s = strtoull(argv[ai], 0, 10);
    if (s % 4 != 1 || s >= (1ULL << 31)) { fprintf(stderr, "bad s\n"); return 2; }
    u64 cnt = 0, maxd = 0, argm = 0, unk = 0, l10 = 0, l14 = 0;
    for (u64 m = mlo | 1; m <= mhi; m += 2) {
      if (m % 3 == 0 || m % 5 == 0 || m % 7 == 0) continue;
      u128 n = (u128)s * m * m;
      if (n >> 126) { fprintf(stderr, "overflow\n"); return 3; }
      u64 found = 0;
      for (u64 d = 3; d <= LIM; d += 4) {
        u64 md = m % d, rm = ((s % d) * ((md * md) % d)) % d;
        if (rm == 0) continue;
        u64 r = d - rm, A = (d + 1) >> 2;
        if (A % r == 0) {
          if ((n + r) % d != 0 || 4 * r * (A / r) - 1 != d) { printf("VERIFYFAIL %llu %llu\n", s, m); return 4; }
          found = d; break;
        }
      }
      cnt++;
      if (!found) { unk++; printf("U %llu %llu\n", s, m); fflush(stdout); continue; }
      if (found > maxd) { maxd = found; argm = m; }
      if (found >= 1024) l10++;
      if (found >= 16384) l14++;
      if (found >= LATE) printf("L %llu %llu %llu\n", s, m, found);
    }
    printf("S %llu %llu %llu %llu %llu %llu %llu %llu %llu\n", s, mlo, mhi, cnt, maxd, argm, unk, l10, l14);
    fflush(stdout);
  }
  return 0;
}
