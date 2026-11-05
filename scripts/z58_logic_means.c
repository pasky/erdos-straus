// z58 LOGIC: mean R(n)/log^2 n and zero counts by class, over n = 1 (4) in [N/10, N]:
// classes: P (prime), SQ (odd square), CM (composite non-square, n mod 840 in Mordell's set), C3 (composite non-square, 3 | n),
// CO (other composite non-squares).  Also the same split restricted to n mod 840 in M for primes (PM).
// Build: gcc -O2 -o /tmp/z58means scripts/z58_logic_means.c -lm ; run: /tmp/z58means N
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll;
int main(int argc, char **argv) {
  ll N = atoll(argv[1]), H = N / 4 + 1;
  uint16_t *R = calloc(H, 2); char *comp = calloc(N / 2 + 1, 1);
  for (ll u = 1; 3 * u - 1 <= N; u++)
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 3) != 3) continue;
      ll s = u * B, i = (4 * u * B - u - B - 1) / 4, I = (N - 1) / 4;
      for (; i <= I; i += s) if (R[i] < 65535) R[i]++;
    }
  for (ll q = 3; q * q <= N; q += 2) if (!comp[q / 2]) for (ll j = q * q; j <= N; j += 2 * q) comp[j / 2] = 1;
  int Mo[840] = {0}; Mo[1] = Mo[121] = Mo[169] = Mo[289] = Mo[361] = Mo[529] = 1;
  const char *nm[6] = {"P", "PM", "SQ", "CM", "C3", "CO"}; double s[6] = {0}; ll c[6] = {0}, z[6] = {0};
  for (ll n = N / 10 + ((5 - N / 10 % 4) % 4); n <= N; n += 4) {
    if (n % 4 != 1) continue;
    ll i = (n - 1) / 4; double L = log((double)n), v = R[i] / (L * L); ll r = (ll)sqrt((double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++;
    int k;
    if (!comp[n / 2]) k = Mo[n % 840] ? 1 : 0; else if (r * r == n) k = 2; else if (Mo[n % 840]) k = 3; else if (n % 3 == 0) k = 4; else k = 5;
    s[k] += v; c[k]++; if (R[i] == 0) z[k]++;
    if (k == 1) { s[0] += v; c[0]++; if (R[i] == 0) z[0]++; }
  }
  printf("# n = 1 (4) in [%lld, %lld]: class count mean(R/L^2) zeros   (P includes PM)\n", N / 10, N);
  for (int k = 0; k < 6; k++) printf("%s %lld %.4f %lld\n", nm[k], c[k], c[k] ? s[k] / c[k] : 0, z[k]);
  return 0;
}
