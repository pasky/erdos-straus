// z60 MS105: single-n d-form decider for n < 2^127 (n = 1 mod 4), for pseudosquares and other big structured inputs.
// Scans d = 3, 7, 11, ... <= LIM; a hit is d with r = (-n mod d) in [1, d-1], r | (d+1)/4 (u = r, C = (d+1)/(4r),
// B = (n+r)/d).  Reports the first hit (verified: d | n + r and 4rC - 1 = d, which is equivalent to 4uBC - u - B = n) and the number of
// hits with d <= LIM (= the number of ordered solutions (u,B,C) whose d = 4uC-1 is <= LIM).  Output: "n first_d u C nhits LIM [tag]" or "n UNK LIM nhits=0 [tag]".
// Usage: z60_ms105_dec128 LIM < list   (list lines: "n [tag]")
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;
static int ovf;
static u128 parse(const char *s) {
  u128 v = 0; ovf = 0;
  while (*s >= '0' && *s <= '9') { if (__builtin_mul_overflow(v, (u128)10, &v) || __builtin_add_overflow(v, (u128)(*s++ - '0'), &v)) ovf = 1; }
  return v;
}
static void pr(u128 v, char *buf) {
  char t[64]; int k = 0; if (!v) t[k++] = '0';
  while (v) { t[k++] = '0' + (int)(v % 10); v /= 10; }
  for (int i = 0; i < k; i++) buf[i] = t[k - 1 - i]; buf[k] = 0;
}
int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage: LIM < list\n"); return 1; }
  u64 LIM = strtoull(argv[1], 0, 10);
  char line[512];
  while (fgets(line, sizeof line, stdin)) {
    char ns[128], tag[256] = "";
    if (sscanf(line, "%127s %255s", ns, tag) < 1 || ns[0] == '#') continue;
    u128 n = parse(ns);
    char nb[64]; pr(n, nb);
    if (ovf || (u64)(n & 3) != 1 || (n >> 126)) { printf("%s BADINPUT %s\n", nb, tag); continue; }
    u64 first = 0, fu = 0, fC = 0, nh = 0;
    for (u64 d = 3; d <= LIM; d += 4) {
      u64 rm = (u64)(n % d);
      if (rm == 0) continue;
      u64 r = d - rm, A = (d + 1) >> 2;
      if (A % r == 0) {
        nh++;
        if (!first) {
          first = d; fu = r; fC = A / r;
          // verify: (n + r) = d*B exactly and 4uBC - u - B = n  <=>  B*(4uC - 1) = n + u  with 4uC - 1 = d.
          if ((n + r) % d != 0 || (u128)4 * fu * fC - 1 != d) { printf("%s VERIFYFAIL %s\n", nb, tag); return 4; }
        }
      }
    }
    if (first) printf("%s %llu %llu %llu %llu %llu %s\n", nb, first, fu, fC, nh, LIM, tag);
    else printf("%s UNK %llu 0 %s\n", nb, LIM, tag);
    fflush(stdout);
  }
  return 0;
}
