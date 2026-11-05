// z58 MORDELL: class statistics of R(p) (full (★) count) for primes p ≡ 1 (4), p ≤ N, by p mod 840.
// R(n) enumerated exactly as in scripts/z57_synth_tri.c (all triples 4uBC - u - B = n ≤ N; uint16 cap 65535).
// Output per class r mod 840 (r ≡ 1 mod 4, unit): #primes in [N/10, N], mean R/L^2 (L = log p), #R=0, #R<=4, #R<=8
// (over all p ≤ N for the zero / low counts), and the decade breakdown for the six Mordell classes.
// Optional 2nd arg: file to dump "p R(p)" for every prime p <= N in the six Mordell classes.
// Build: gcc -O2 -o /tmp/z58cs scripts/z58_mordell_classstats.c -lm ; run: /tmp/z58cs N
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll;
int main(int argc, char **argv) {
  ll N = atoll(argv[1]);
  FILE *dump = argc > 2 ? fopen(argv[2], "w") : NULL;   // optional: dump "p R" for every Mordell-class prime
  ll H = N / 2 + 1;
  uint16_t *R = calloc(H, 2);
  char *comp = calloc(H, 1);
  if (!R || !comp) return 2;
  for (ll u = 1; 3 * u - 1 <= N; u++)
    for (ll B = 1; 4 * u * B - u - B <= N; B++) {
      if (((u + B) & 1) == 0) continue;
      ll step = 4 * u * B, n = step - u - B;
      for (; n <= N; n += step) { ll i = (n - 1) / 2; if (R[i] < 65535) R[i]++; }
    }
  for (ll i = 1; i < H; i++) {            // odd sieve: index i <-> n = 2i+1
    if (comp[i]) continue;
    ll p = 2 * i + 1; if (p * p > N) continue;
    for (ll m = p * p; m <= N; m += 2 * p) comp[(m - 1) / 2] = 1;
  }
  static double s[840]; static ll cnt[840], z[840], l4[840], l8[840], all[840];
  for (ll i = 2; i < H; i++) {
    if (comp[i]) continue;
    ll p = 2 * i + 1; if (p > N || (p & 3) != 1) continue;
    int r = p % 840, v = R[i];
    if (dump && (r==1||r==121||r==169||r==289||r==361||r==529)) fprintf(dump, "%lld %d\n", p, v);
    all[r]++;
    if (v == 0) z[r]++;
    if (v <= 4) l4[r]++;
    if (v <= 8) l8[r]++;
    if (p >= N / 10) { double L = log((double)p); s[r] += v / (L * L); cnt[r]++; }
  }
  printf("# N=%lld; cols: r=p mod 840, mordell?, #p<=N, #p in [N/10,N], mean R/L^2 there, #R=0, #R<=4, #R<=8\n", N);
  int M[6] = {1, 121, 169, 289, 361, 529};
  for (int r = 1; r < 840; r += 4) {
    if (!all[r]) continue;
    int m = 0; for (int j = 0; j < 6; j++) if (M[j] == r) m = 1;
    printf("%d %c %lld %lld %.5f %lld %lld %lld\n", r, m ? 'M' : '-', all[r], cnt[r], cnt[r] ? s[r] / cnt[r] : 0.0, z[r], l4[r], l8[r]);
  }
  return 0;
}
