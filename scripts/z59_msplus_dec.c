// z59 MSPLUS: single-n hit search for R(n) >= 1 (n odd, n = 1 mod 4, n < 2^62), no precomputed tables.
// Scans moduli m = 3, 4, 5, ... <= LIM in the symmetric order of scripts/z58_ladder_mdec.c (z58 LADDER Lemma 1.1):
//   m = 3 (4): hit iff r = (-n mod m) >= 1 divides (m+1)/4                 [d-form: d = m, u = r, C = (m+1)/(4r)]
//   m = 0 (4): hit iff some u | m/4, B = m/(4u) with m | n + u + B, n + u + B >= m   [C = (n+u+B)/m]
// Each hit found is re-verified as an explicit (u, B, C) with 4uBC - u - B = n in 128-bit arithmetic.
// Output per input line "n [tag]":  "n mu u B C [tag]"  or  "n UNK LIM [tag]" if no hit with m <= LIM
// (UNK is NOT a zero; it must be decided by an exhaustive engine).  Usage: z59_msplus_dec LIM < list
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;
static int verify(u64 n, u64 u, u64 B, u64 C) {
  u128 v = (u128)4 * u * B * C;
  return v >= (u128)u + B && v - u - B == (u128)n;
}
int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage: LIM < list\n"); return 1; }
  u64 LIM = strtoull(argv[1], 0, 10);
  char line[256];
  while (fgets(line, sizeof line, stdin)) {
    char tag[200] = ""; u64 n;
    if (sscanf(line, "%llu %199s", &n, tag) < 1) continue;
    if (n % 4 != 1 || n >= (1ULL << 62)) { printf("%llu BADINPUT %s\n", n, tag); continue; }
    u64 found = 0, fu = 0, fB = 0, fC = 0;
    for (u64 m = 3; m <= LIM && !found; m++) {
      if ((m & 3) == 3) {
        u64 r = (m - n % m) % m, A = (m + 1) / 4;
        if (r && A % r == 0) { found = m; fu = r; fC = A / r; fB = (n + r) / m; }
      } else if ((m & 3) == 0) {
        u64 q = m / 4, nm = n % m;
        for (u64 u = 1; u * u <= q && !found; u++) {
          if (q % u) continue;
          u64 pair[2] = {u, q / u};
          for (int t = 0; t < 2 && !found; t++) {
            u64 uu = pair[t], BB = q / uu;
            if ((nm + uu % m + BB % m) % m == 0 && n + uu + BB >= m) { found = m; fu = uu; fB = BB; fC = (n + uu + BB) / m; }
          }
        }
      }
    }
    if (found) {
      if (!verify(n, fu, fB, fC)) { printf("%llu VERIFYFAIL %s\n", n, tag); continue; }
      printf("%llu %llu %llu %llu %llu %s\n", n, found, fu, fB, fC, tag);
    } else printf("%llu UNK %llu %s\n", n, LIM, tag);
    fflush(stdout);
  }
  return 0;
}
