// z58 LADDER: symmetric least hit modulus mu(n) for (*) 4uBC - u - B = n  (Z58_LADDER.md Lemma 1.1).
// For each solution (u,B,C): n = -u (mod 4uC-1), n = -B (mod 4BC-1), n = -(u+B) (mod 4uB).
// mu(n) := min over solutions of min(4uC-1, 4BC-1, 4uB);  dm(n) := min over solutions of the d-form moduli (both roles);
// qm(n) := min over solutions of the pair modulus 4uB.  mu = min(dm, qm).  Values > CAP are stored as 0 ("> CAP").
// If CAP >= 1.9231 (X+1)^(2/3) then "mu > CAP" <=> R(n) = 0 for every n <= X (Lemma 1.1(b)).
// Tail fractions count a zero (mu = infinity) in every tail ("frac_mu>D" is P(mu > D) unconditionally);
// max_mu is the maximum FINITE mu in the bin.
// Usage: z58_ladder_mu X CAP Y   (n <= X, moduli <= CAP, roughness threshold Y);  supported: X <= 4e8, CAP <= 4e9.
// Memory: 12 bytes per n (X = 1e8: 1.2 GB).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

static int inM(uint64_t n) {
  uint64_t r = n % 840;
  return r == 1 || r == 121 || r == 169 || r == 289 || r == 361 || r == 529;
}
static int issq(uint64_t n) {
  uint64_t s = (uint64_t)sqrtl((long double)n);
  while (s * s > n) s--;
  while ((s + 1) * (s + 1) <= n) s++;
  return s * s == n;
}

int main(int argc, char **argv) {
  if (argc != 4) { fprintf(stderr, "usage: %s X CAP Y\n", argv[0]); return 2; }
  uint64_t X = strtoull(argv[1], 0, 10), CAP = strtoull(argv[2], 0, 10), Y = strtoull(argv[3], 0, 10);
  if (X < 10 || X > 400000000ULL || CAP < 3 || CAP > 4000000000ULL) { fprintf(stderr, "range\n"); return 2; }
  uint32_t *lp = calloc(X + 1, sizeof *lp), *dm = calloc(X + 1, sizeof *dm), *qm = calloc(X + 1, sizeof *qm);
  if (!lp || !dm || !qm) { fprintf(stderr, "alloc\n"); return 3; }
  for (uint64_t i = 2; i <= X; i++)
    if (!lp[i])
      for (uint64_t j = i; j <= X; j += i)
        if (!lp[j]) lp[j] = (uint32_t)i;
  // sieve A: d = 4uC - 1 <= CAP, n = B d - u (B >= 1)
  for (uint64_t u = 1; 4 * u - 1 <= CAP; u++)
    for (uint64_t C = 1; 4 * u * C - 1 <= CAP; C++) {
      uint64_t d = 4 * u * C - 1;
      for (uint64_t n = d - u; n <= X; n += d)
        if (!dm[n] || d < dm[n]) dm[n] = (uint32_t)d;
    }
  // sieve B: q = 4uB <= CAP, n = 4uBC - u - B (C >= 1)
  for (uint64_t u = 1; 4 * u <= CAP; u++)
    for (uint64_t B = 1; 4 * u * B <= CAP; B++) {
      uint64_t q = 4 * u * B;
      for (uint64_t n = q - u - B; n <= X; n += q)
        if (!qm[n] || q < qm[n]) qm[n] = (uint32_t)q;
    }
  // categories: 0 prime in M, 1 prime p = 1 (4) not in M, 2 nonsquare composite lpf >= Y in M, 3 same not in M,
  // 4 nonsquare composite lpf < Y
  const char *cn[5] = {"primeM", "primeNotM", "roughCompM", "roughCompNotM", "smoothComp"};
  printf("# X=%llu CAP=%llu Y=%llu ; mu=min(dm,qm); 0 means > CAP\n", (unsigned long long)X, (unsigned long long)CAP,
         (unsigned long long)Y);
  printf("# decade cat count max_finite_mu argmax dm_at qm_at zeros(mu>CAP) frac_mu>100 frac_mu>1000 frac_mu>10000 "
         "mean(log mu/loglog n | finite)   [fractions include zeros in every tail]\n");
  for (uint64_t lo = 1000; lo < X; lo *= 10) {
    uint64_t hi = lo * 10 < X ? lo * 10 : X;
    for (int c = 0; c < 5; c++) {
      uint64_t cnt = 0, mx = 0, am = 0, big = 0, g100 = 0, g1000 = 0, g10k = 0;
      double s = 0;
      for (uint64_t n = lo + 1; n <= hi; n++) {
        if (n % 4 != 1) continue;
        int cat, pr = (lp[n] == n);
        if (pr) cat = inM(n) ? 0 : 1;
        else {
          if (issq(n)) continue;
          cat = (lp[n] >= Y) ? (inM(n) ? 2 : 3) : 4;
        }
        if (cat != c) continue;
        cnt++;
        uint64_t mu = dm[n] ? (qm[n] && qm[n] < dm[n] ? qm[n] : dm[n]) : qm[n];
        if (!mu) { big++; g100++; g1000++; g10k++; continue; }
        if (mu > mx) { mx = mu; am = n; }
        if (mu > 100) g100++;
        if (mu > 1000) g1000++;
        if (mu > 10000) g10k++;
        s += log((double)mu) / log(log((double)n));
      }
      printf("%llu-%llu %s %llu %llu %llu %u %u %llu %.5f %.6f %.7f %.3f\n", (unsigned long long)lo,
             (unsigned long long)hi, cn[c], (unsigned long long)cnt, (unsigned long long)mx, (unsigned long long)am,
             am ? dm[am] : 0, am ? qm[am] : 0, (unsigned long long)big, cnt ? (double)g100 / cnt : 0,
             cnt ? (double)g1000 / cnt : 0, cnt ? (double)g10k / cnt : 0, (cnt > big) ? s / (cnt - big) : 0);
    }
  }
  printf("# zeros (mu>CAP) outside smoothComp: Z n cat\n");
  for (uint64_t n = 5; n <= X; n += 4) {
    if (dm[n] || qm[n]) continue;
    int pr = (lp[n] == n);
    if (!pr && issq(n)) continue;
    int cat;
    if (pr) cat = inM(n) ? 0 : 1;
    else cat = (lp[n] >= Y) ? (inM(n) ? 2 : 3) : 4;
    if (cat == 4) continue;
    printf("Z %llu %s\n", (unsigned long long)n, cn[cat]);
  }
  printf("# running records of finite mu over primes p=1(4) (zeros listed as >CAP): p mu dm qm inM\n");
  uint64_t rec = 0;
  for (uint64_t n = 5; n <= X; n += 4) {
    if (lp[n] != n) continue;
    uint64_t mu = dm[n] ? (qm[n] && qm[n] < dm[n] ? qm[n] : dm[n]) : qm[n];
    if (!mu) { printf("R %llu >CAP dm=%u qm=%u %d\n", (unsigned long long)n, dm[n], qm[n], inM(n)); continue; }
    if (mu > rec) {
      rec = mu;
      printf("R %llu %llu %u %u %d\n", (unsigned long long)n, (unsigned long long)mu, dm[n], qm[n], inM(n));
    }
  }
  return 0;
}
