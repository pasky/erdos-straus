/* z64 SDEEP: enumerate all length-3 HJ words (t,u,v), u<v, of primes p == 1 (mod 8), p <= X, and print per-prime
   sub-counts for the KS1 parity test.  Word: tuv - u - v = p, t,u,v >= 2; A = tu-1 | p+u, A == -1 (mod u), v = (p+u)/A.
   One word per reversal pair (u < v; u = v impossible at primes).  Sign = Jacobi (A/p) (checked against the mod-4 cell
   law: -1 iff 4 | one of t,u,v,A,A*).  Also checks Lemma 1: (A/p) = (t(u+v)/p) = ((t(u+v)-4)/p) when coprime to p.
   Output line per prime:  p  then for each restriction r = 0..7  (all; t<=2; t<=3; t<=4; t<=8; u<=4; u<=8; u<=16):
     Nneg Npos S_t S_A S_u  c[0..39]   (c index = 10*(t%4) + pairindex(min(u%4,v%4), max(..)))
   gcc -O2 -o /tmp/z64w scripts/z64_sdeep_words.c ; /tmp/z64w 2000000 > /tmp/z64_words.txt */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static uint32_t *spf;
static int jac(uint64_t a, uint64_t n) {
  int s = 1; a %= n;
  while (a) {
    while (!(a & 1)) { a >>= 1; uint64_t r = n & 7; if (r == 3 || r == 5) s = -s; }
    uint64_t t = a; a = n; n = t;
    if ((a & 3) == 3 && (n & 3) == 3) s = -s;
    a %= n;
  }
  return n == 1 ? s : 0;
}
static uint64_t divs[20000];
static int ndivs(uint64_t m) {
  int k = 1; divs[0] = 1;
  while (m > 1) {
    uint32_t p = spf[m]; int e = 0;
    while (m % p == 0) { m /= p; e++; }
    int k0 = k; uint64_t pw = 1;
    for (int j = 1; j <= e; j++) { pw *= p; for (int i = 0; i < k0; i++) divs[k++] = divs[i] * pw; }
  }
  return k;
}
static int pairidx(int a, int b) { /* a<=b in 0..3 -> 0..9 */
  static const int base[4] = {0, 4, 7, 9};
  return base[a] + (b - a);
}
#define NR 8
int main(int argc, char **argv) {
  uint64_t X = strtoull(argv[1], 0, 10);
  uint64_t L = X + 2000000;
  spf = calloc(L + 1, 4);
  for (uint64_t i = 2; i <= L; i++) if (!spf[i]) for (uint64_t j = i; j <= L; j += i) if (!spf[j]) spf[j] = i;
  long lemma_bad = 0, cell_bad = 0, nprimes = 0;
  for (uint64_t p = 17; p <= X; p += 8) {
    if (spf[p] != p) continue;
    nprimes++;
    long cnt[NR][45]; for (int r = 0; r < NR; r++) for (int i = 0; i < 45; i++) cnt[r][i] = 0;
    for (uint64_t u = 2; 2 * u * (u - 1) <= p; u++) {
      uint64_t m = p + u; int k = ndivs(m);
      for (int i = 0; i < k; i++) {
        uint64_t d = divs[i];
        if (d < 2 * u - 1 || (d + 1) % u) continue;
        uint64_t v = m / d; if (v <= u) continue;
        uint64_t t = (d + 1) / u;
        if (t * u * v - u - v != p) { fprintf(stderr, "BUG\n"); return 1; }
        int s = jac(d, p);
        uint64_t As = t * v - 1;
        int cellneg = (t % 4 == 0) || (u % 4 == 0) || (v % 4 == 0) || (d % 4 == 0) || (As % 4 == 0);
        if ((s == -1) != cellneg) cell_bad++;
        uint64_t T2 = t * (u + v);
        if (T2 % p && (T2 - 4) % p) { if (jac(T2, p) != s || jac(T2 - 4, p) != s) lemma_bad++; }
        int ci = 10 * (t % 4) + pairidx(u % 4 < v % 4 ? u % 4 : v % 4, u % 4 < v % 4 ? v % 4 : u % 4);
        int inr[NR] = {1, t <= 2, t <= 3, t <= 4, t <= 8, u <= 4, u <= 8, u <= 16};
        for (int r = 0; r < NR; r++) if (inr[r]) {
          if (s == -1) cnt[r][0]++; else cnt[r][1]++;
          if (t % 4 == 0) cnt[r][2]++;
          if (d % 4 == 0 || As % 4 == 0) cnt[r][3]++;
          if (u % 4 == 0 || v % 4 == 0) cnt[r][4]++;
          cnt[r][5 + ci]++;
        }
      }
    }
    printf("%lu", (unsigned long)p);
    for (int r = 0; r < NR; r++) for (int i = 0; i < 45; i++) printf(" %ld", cnt[r][i]);
    printf("\n");
  }
  fprintf(stderr, "primes %ld  cell-law failures %ld  Lemma1 failures %ld\n", nprimes, cell_bad, lemma_bad);
  return 0;
}
