// z56 PRIMET1: exact (★) count R(p) = #{(u,B,C) in N^3 : 4uBC - u - B = p} for ALL primes p ≡ 1 (mod 24) in [N0, N1].
// Pair sieve: for each (u,B) the admissible p form the AP p ≡ -(u+B) (mod 4uB), p >= 4uB-u-B (C >= 1).
// For p ≡ 1 (24): u+B must be ≡ 7 (mod 8) (then 8 | 4uB and -(u+B) ≡ 1 (8)); the mod-3 condition picks one class mod 12uB
// (or all/none if 3 | uB). gcd(u,B)=1 is automatic at primes (g | p), so it is not checked (values at composites are not used).
// Counts are stored only for n ≡ 1 (24), index (n-1)/24. Output: binary records (uint64 p, uint16 R) to stdout, or text with "t".
// Usage: z56_primet1_rsieve N0 N1 [t]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef unsigned long long u64;
int main(int argc, char **argv) {
  u64 N0 = strtoull(argv[1], 0, 10), N1 = strtoull(argv[2], 0, 10);
  int text = argc > 3;
  u64 K = N1 / 24 + 1;
  uint16_t *R = calloc(K, sizeof(uint16_t));
  if (!R) { fprintf(stderr, "oom\n"); return 1; }
  for (u64 u = 1; 4 * u - u - 1 <= N1; u++) {
    for (u64 B = 1; 4 * u * B - u - B <= N1; B++) {
      if (((u + B) & 7) != 7) continue;
      u64 q = 4 * u * B, n0 = q - u - B, step;
      if ((u * B) % 3 == 0) {
        if (n0 % 3 != 1) continue;
        step = q;
      } else {
        // find j in {0,1,2} with n0 + j q ≡ 1 (mod 3)
        u64 j = 0;
        while ((n0 + j * q) % 3 != 1) j++;
        n0 += j * q; step = 3 * q;
      }
      if (n0 < N0) { u64 k = (N0 - n0 + step - 1) / step; n0 += k * step; }
      for (u64 n = n0; n <= N1; n += step) R[n / 24]++;
    }
  }
  // primality: segmented-free simple odd sieve over [0, N1] as bitset
  u64 nb = N1 / 2 + 1;
  uint8_t *comp = calloc(nb / 8 + 1, 1);
  if (!comp) { fprintf(stderr, "oom2\n"); return 1; }
  for (u64 i = 3; i * i <= N1; i += 2)
    if (!(comp[(i / 2) >> 3] & (1 << ((i / 2) & 7))))
      for (u64 j = i * i; j <= N1; j += 2 * i) comp[(j / 2) >> 3] |= 1 << ((j / 2) & 7);
  u64 start = N0 < 25 ? 25 : N0;
  u64 n = start + ((24 + 1 - start % 24) % 24);
  for (; n <= N1; n += 24) {
    if (comp[(n / 2) >> 3] & (1 << ((n / 2) & 7))) continue;
    uint16_t r = R[n / 24];
    if (text) printf("%llu %u\n", n, r);
    else { fwrite(&n, 8, 1, stdout); fwrite(&r, 2, 1, stdout); }
  }
  return 0;
}
