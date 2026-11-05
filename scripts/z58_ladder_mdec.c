// z58 LADDER: exact decision of R(n) >= 1 for all non-square n in Mordell's classes (n mod 840 in M) in [A, B],
// via the symmetric least hit modulus mu(n) (Z58_LADDER.md Lemma 1.1): R(n) >= 1 iff some modulus m with
// 9 m^3 <= 64 (n+1)^2 carries a hit:  m = 3 (4): r = (-n mod m) >= 1 divides (m+1)/4;
// m = 0 (4): some u | m/4, B = m/(4u), with m | n + u + B and n + u + B >= m  (no coprimality imposed: exact for
// composite n too).  The scan runs m = 3, 4, ... up to the integer cap; the first hit gives mu(n).
// Output: "Z n prime|comp" for every zero; per category "S" lines with count, zeros, max FINITE mu, and unconditional
// tail fractions P(mu > D) (zeros counted in every tail) plus the raw tail numerators.
// Usage: z58_ladder_mdec A B   (supported 5 <= A <= B <= 1e13; deterministic Miller-Rabin for 64-bit n).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;

static u64 mulmod(u64 a, u64 b, u64 m) { return (u64)((u128)a * b % m); }
static u64 powmod(u64 a, u64 e, u64 m) {
  u64 r = 1; a %= m;
  while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; }
  return r;
}
static int isprime(u64 n) {  // deterministic for all uint64 n (12 bases suffice below 318665857834031151167461)
  static const u64 Bs[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
  if (n < 2) return 0;
  for (int i = 0; i < 12; i++) if (n % Bs[i] == 0) return n == Bs[i];
  u64 d = n - 1; int s = 0;
  while (!(d & 1)) { d >>= 1; s++; }
  for (int i = 0; i < 12; i++) {
    u64 x = powmod(Bs[i], d, n);
    if (x == 1 || x == n - 1) continue;
    int ok = 0;
    for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } }
    if (!ok) return 0;
  }
  return 1;
}
static int issq(u64 n) {
  u64 s = (u64)sqrtl((long double)n);
  while (s * s > n) s--;
  while ((s + 1) * (s + 1) <= n) s++;
  return s * s == n;
}
// largest integer m with 9 m^3 <= 64 (n+1)^2  (exact, integer arithmetic)
static u64 capof(u64 n) {
  u64 m = (u64)(1.92300 * pow((double)n + 1, 2.0 / 3.0)) + 3;
  u128 rhs = (u128)64 * (n + 1) * (n + 1);
  while ((u128)9 * m * m * m > rhs) m--;
  while ((u128)9 * (m + 1) * (m + 1) * (m + 1) <= rhs) m++;
  return m;
}
static uint32_t *spf; static u64 SPFN;
#define MAXDIV 8192
static u64 mu_of(u64 n, u64 cap) {
  u64 divs[MAXDIV];
  for (u64 m = 3; m <= cap; m++) {
    if ((m & 3) == 3) {
      u64 r = (m - n % m) % m;
      if (r && ((m + 1) / 4) % r == 0) return m;
    } else if ((m & 3) == 0) {
      u64 q = m / 4, t = q, pr[24]; int ex[24], k = 0, nd = 1;
      while (t > 1) { u64 p = spf[t]; int e = 0; while (t % p == 0) { t /= p; e++; } pr[k] = p; ex[k] = e; k++; }
      divs[0] = 1;
      for (int i = 0; i < k; i++) {
        int cur = nd; u64 pp = 1;
        for (int e = 1; e <= ex[i]; e++) {
          pp *= pr[i];
          for (int j = 0; j < cur; j++) {
            if (nd >= MAXDIV) { fprintf(stderr, "divisor overflow at q=%llu\n", q); exit(4); }
            divs[nd++] = divs[j] * pp;
          }
        }
      }
      u64 nm = n % m;
      for (int j = 0; j < nd; j++) {
        u64 u = divs[j], B = q / u;
        if ((nm + u + B) % m == 0 && n + u + B >= m) return m;
      }
    }
  }
  return 0;
}
int main(int argc, char **argv) {
  if (argc != 3) { fprintf(stderr, "usage: %s A B\n", argv[0]); return 2; }
  u64 A = strtoull(argv[1], 0, 10), Bn = strtoull(argv[2], 0, 10);
  if (A < 5 || Bn < A || Bn > 10000000000000ULL) { fprintf(stderr, "range\n"); return 2; }
  u64 capmax = capof(Bn);
  SPFN = capmax / 4 + 2;
  spf = calloc(SPFN + 1, sizeof *spf);
  if (!spf) { fprintf(stderr, "alloc\n"); return 3; }
  for (u64 i = 2; i <= SPFN; i++)
    if (!spf[i])
      for (u64 j = i; j <= SPFN; j += i)
        if (!spf[j]) spf[j] = (uint32_t)i;
  static const int Mc[6] = {1, 121, 169, 289, 361, 529};
  u64 cnt[2] = {0, 0}, z[2] = {0, 0}, g100[2] = {0, 0}, g1k[2] = {0, 0}, g10k[2] = {0, 0}, mx[2] = {0, 0},
      am[2] = {0, 0};
  double s[2] = {0, 0};
  for (u64 base = A - A % 840; base <= Bn; base += 840)
    for (int i = 0; i < 6; i++) {
      u64 n = base + Mc[i];
      if (n < A || n > Bn || issq(n)) continue;
      int c = isprime(n) ? 0 : 1;
      u64 mu = mu_of(n, capof(n));
      cnt[c]++;
      if (!mu) {
        z[c]++; g100[c]++; g1k[c]++; g10k[c]++;
        printf("Z %llu %s\n", n, c ? "comp" : "prime");
        fflush(stdout);
        continue;
      }
      if (mu > 100) g100[c]++;
      if (mu > 1000) g1k[c]++;
      if (mu > 10000) g10k[c]++;
      if (mu > mx[c]) { mx[c] = mu; am[c] = n; }
      s[c] += log((double)mu) / log(log((double)n));
    }
  for (int c = 0; c < 2; c++) {
    if (!cnt[c]) continue;
    printf("S %llu-%llu %s count=%llu zeros=%llu max_finite_mu=%llu at %llu tails(>1e2,>1e3,>1e4)=%llu,%llu,%llu "
           "frac>100=%.5f frac>1e3=%.6f frac>1e4=%.7f meanlogmu/loglogn(finite)=%.4f\n",
           A, Bn, c ? "compM" : "primeM", cnt[c], z[c], mx[c], am[c], g100[c], g1k[c], g10k[c],
           (double)g100[c] / cnt[c], (double)g1k[c] / cnt[c], (double)g10k[c] / cnt[c],
           cnt[c] > z[c] ? s[c] / (cnt[c] - z[c]) : 0);
  }
  return 0;
}
