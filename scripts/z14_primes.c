// z14_primes.c — odd primes q <= Q (q != 2) with ord_q(4) B-smooth.  Output binary pairs (uint32 q, uint32 ord).
// Usage: z14_primes Q B out.bin      (memory: 4*Q bytes for the smallest-prime-factor sieve)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u64; typedef uint32_t u32;
static u64 pw(u64 b, u64 e, u64 m) { u64 r = 1 % m; b %= m; while (e) { if (e & 1) r = r * b % m; b = b * b % m; e >>= 1; } return r; }
int main(int argc, char **argv) {
  u32 Q = (u32)atoll(argv[1]), B = (u32)atoll(argv[2]);
  FILE *out = fopen(argv[3], "wb");
  u32 *spf = calloc((size_t)Q + 2, 4);
  for (u64 i = 2; i <= Q + 1; i++) if (!spf[i]) for (u64 j = i; j <= Q + 1; j += i) if (!spf[j]) spf[j] = (u32)i;
  u64 cnt = 0, tot = 0;
  for (u64 q = 3; q <= Q; q += 2) {
    if (spf[q] != q) continue;
    tot++;
    u64 o = q - 1, x = q - 1;
    while (x > 1) { u32 p = spf[x]; while (x % p == 0) x /= p; while (o % p == 0 && pw(4, o / p, q) == 1) o /= p; }
    // B-smooth?
    u64 y = o; int ok = 1;
    while (y > 1) { u32 p = spf[y]; if (p > B) { ok = 0; break; } while (y % p == 0) y /= p; }
    if (!ok) continue;
    u32 rec[2] = {(u32)q, (u32)o}; fwrite(rec, 4, 2, out); cnt++;
  }
  fclose(out);
  fprintf(stderr, "primes %llu, kept %llu (B=%u)\n", (unsigned long long)tot, (unsigned long long)cnt, B);
  return 0;
}
