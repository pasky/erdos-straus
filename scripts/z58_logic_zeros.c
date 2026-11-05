// z58 LOGIC: zero census of R(n) over ALL n = 1 (mod 4), n <= N (bitset sieve; only hit / no-hit is recorded).
// R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n}; n = 1 (4) forces u + B = 3 (4).
// Output (stdout): every n = 1 (4), 5 <= n <= N, with R(n) = 0, as "n" (classification done downstream).
// Build: gcc -O2 -o /tmp/z58zeros scripts/z58_logic_zeros.c ; run: /tmp/z58zeros N > out
// Memory: N/4 bits (N = 1e9 -> 31 MB).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long long ll;
int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage: N\n"); return 1; }
  ll N = atoll(argv[1]); if (N < 5 || N > 40000000000LL) { fprintf(stderr, "N out of safe range [5, 4e10]\n"); return 1; }
  ll H = N / 4 + 1;                         // index (n-1)/4 for n = 1 (4)
  uint64_t *hit = calloc(H / 64 + 1, 8);
  if (!hit) { fprintf(stderr, "alloc\n"); return 2; }
  for (ll u = 1; 3 * u - 1 <= N; u++)
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 3) != 3) continue;
      ll step = 4 * u * B, n = step - u - B;   // n = 1 (4); step = 0 (4) so index stride step/4
      ll i = (n - 1) / 4, s = step / 4, I = (N - 1) / 4;
      for (; i <= I; i += s) hit[i >> 6] |= 1ULL << (i & 63);
    }
  ll z = 0;
  for (ll n = 5; n <= N; n += 4) { ll i = (n - 1) / 4; if (!(hit[i >> 6] >> (i & 63) & 1)) { printf("%lld\n", n); z++; } }
  fprintf(stderr, "N=%lld zeros(n=1 mod 4, n>=5)=%lld\n", N, z);
  return 0;
}
