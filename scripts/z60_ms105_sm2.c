// z60 MS105: twisted-square family search  n = s*m^2  (brief item (1)).
// For each s given on the command line (or via -f file) and each odd m in [mlo, mhi] with gcd(m, 105) = 1,
// decide R(n) >= 1 by scanning the d-form: d = 3, 7, 11, ... <= LIM, hit iff r = (-n mod d) in [1, d-1] divides (d+1)/4
// (then u = r, C = (d+1)/(4r), B = (n+r)/d; 4uBC - u - B = n).  Every first hit is re-verified in 128-bit arithmetic.
// The d-form is complete: every solution (u,B,C) has d = 4uC-1 <= (4n+1)/3 (z58 LADDER Lemma 1.1 / WITNESS).
// A miss up to LIM is reported as "UNK" (NOT a zero; must be decided separately).
// Output: per-s summary line  "S s mlo mhi count maxd argm unk late(>=2^10) late(>=2^14)"  plus "U s m n" lines for UNK
// and "L s m n d" lines for first hit d >= LATE.
// Usage: z60_ms105_sm2 mlo mhi LIM LATE s1 [s2 ...]
// Compile with -DR8 for the C-even sub-line R8 (sensitivity control; F2).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;
static u64 gcd(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage: mlo mhi LIM LATE s...\n"); return 1; }
  u64 mlo = strtoull(argv[1], 0, 10), mhi = strtoull(argv[2], 0, 10), LIM = strtoull(argv[3], 0, 10),
      LATE = strtoull(argv[4], 0, 10);
  for (int ai = 5; ai < argc; ai++) {
    u64 s = strtoull(argv[ai], 0, 10);
    if (s % 4 != 1) { fprintf(stderr, "s=%llu not 1 mod 4\n", s); return 2; }
    u64 cnt = 0, maxd = 0, argm = 0, unk = 0, l10 = 0, l14 = 0;
    for (u64 m = mlo | 1; m <= mhi; m += 2) {
      if (m % 3 == 0 || m % 5 == 0 || m % 7 == 0) continue;
      u128 N = (u128)s * m * m;
      if (N >> 64) { fprintf(stderr, "overflow s=%llu m=%llu\n", s, m); return 3; }
      u64 n = (u64)N;
      u64 found = 0;
#ifdef R8
      for (u64 d = 7; d <= LIM; d += 8) {   // R8 (C even): d = 4uC - 1 with C even <=> d = 7 (8), r | (d+1)/8
        u64 rm = n % d;
        if (rm == 0) continue;
        u64 r = d - rm, A = (d + 1) >> 3;
#else
      for (u64 d = 3; d <= LIM; d += 4) {
        u64 rm = n % d;
        if (rm == 0) continue;
        u64 r = d - rm, A = (d + 1) >> 2;
#endif
        if (A % r == 0) {
#ifdef R8
          u64 u = r, C = 2 * (A / r);
#else
          u64 u = r, C = A / r;
#endif
          u128 B = ((u128)n + r) / d;
          u128 v = (u128)4 * u * B * C;
          if (((u128)n + r) % d != 0 || v - u - B != (u128)n) { printf("VERIFYFAIL %llu %llu\n", s, m); return 4; }
          found = d; break;
        }
      }
      cnt++;
      if (!found) { unk++; printf("U %llu %llu %llu\n", s, m, n); fflush(stdout); continue; }
      if (found > maxd) { maxd = found; argm = m; }
      if (found >= 1024) l10++;
      if (found >= 16384) l14++;
      if (found >= LATE) printf("L %llu %llu %llu %llu\n", s, m, n, found);
    }
    printf("S %llu %llu %llu %llu %llu %llu %llu %llu %llu\n", s, mlo, mhi, cnt, maxd, argm, unk, l10, l14);
    fflush(stdout);
  }
  return 0;
}
