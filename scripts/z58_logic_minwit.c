// z58 LOGIC: least witnesses for (MS) at primes p = 1 (4) <= N: d_min (least hit d = 4uC-1), C_min (least level C with a
// hit, i.e. least C such that 4Cp+1 has a divisor = -1 mod 4C), u_min (least u such that p+u has a divisor = -1 mod 4u).
// Per decade, over primes in Mordell's classes (and over all primes = 1 (4)), prints the max of each and an argmax.
// These measure the cost of three search strategies: trial over d (no factoring), factor 4Cp+1 for C = 1, 2, ...,
// factor p+u for u = 1, 2, ....  Build: gcc -O2 -o /tmp/z58minwit scripts/z58_logic_minwit.c -lm ; run: /tmp/z58minwit N
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll;
int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage: N (100 <= N <= 3e9)\n"); return 1; }
  ll N = atoll(argv[1]); if (N < 100 || N > 3000000000LL) { fprintf(stderr, "N out of safe range\n"); return 1; }
  ll H = N / 4 + 1, I = (N - 1) / 4;
  uint32_t *dm = malloc(H * sizeof *dm); uint16_t *cm = malloc(H * sizeof *cm), *um = malloc(H * sizeof *um);
  if (!dm || !cm || !um) { fprintf(stderr, "alloc\n"); return 2; }
  for (ll i = 0; i < H; i++) { dm[i] = 0xffffffff; cm[i] = 0xffff; um[i] = 0xffff; }
  for (ll u = 1; 3 * u - 1 <= N; u++)
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 3) != 3) continue;
      ll s = u * B, i = (4 * u * B - u - B - 1) / 4;
      for (ll C = 1; i <= I; i += s, C++) {
        ll d = 4 * u * C - 1;
        ll dc = d > 0xfffffffeLL ? 0xfffffffeLL : d;   // clamp below the no-hit sentinel (d < 4e9 in the safe range)
        if (dc < dm[i]) dm[i] = (uint32_t)dc;
        if (C < cm[i]) cm[i] = C;
        if (u < um[i]) um[i] = u;
      }
    }
  char *comp = calloc(N / 2 + 1, 1); if (!comp) { fprintf(stderr, "alloc\n"); return 2; }
  for (ll q = 3; q * q <= N; q += 2) if (!comp[q / 2]) for (ll j = q * q; j <= N; j += 2 * q) comp[j / 2] = 1;
  int Mo[840] = {0}; Mo[1] = Mo[121] = Mo[169] = Mo[289] = Mo[361] = Mo[529] = 1;
  ll mx[2][20][3] = {{{0}}}, am[2][20][3] = {{{0}}}; ll cnt[2][20] = {{0}};
  for (ll p = 5; p <= N; p += 4) {
    if (comp[p / 2]) continue; ll i = (p - 1) / 4; if (dm[i] == 0xffffffff) continue;  // zeros skipped
    int k = (int)log10((double)p); ll v[3] = {dm[i], cm[i], um[i]};
    for (int g = 0; g < 2; g++) { if (g == 1 && !Mo[p % 840]) continue; cnt[g][k]++;
      for (int j = 0; j < 3; j++) if (v[j] > mx[g][k][j]) { mx[g][k][j] = v[j]; am[g][k][j] = p; } }
  }
  printf("# C_min / u_min values of 65535 mean >= 65535 (uint16 saturation; flagged 'cap' below)\n");
  printf("# least witnesses at primes p = 1 (4) <= %lld with R(p) >= 1 (zeros skipped); per decade: count, max d_min (argmax), max C_min (argmax), max u_min (argmax)\n", N);
  for (int g = 0; g < 2; g++) for (int k = 0; k < 20; k++) if (cnt[g][k])
    printf("%s 1e%d n=%lld dmin=%lld (%lld) Cmin=%lld%s (%lld) umin=%lld%s (%lld)\n", g ? "MORD" : "ALL", k, cnt[g][k],
      mx[g][k][0], am[g][k][0], mx[g][k][1], mx[g][k][1] >= 65535 ? "cap" : "", am[g][k][1],
      mx[g][k][2], mx[g][k][2] >= 65535 ? "cap" : "", am[g][k][2]);
  return 0;
}
