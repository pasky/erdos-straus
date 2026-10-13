/* R174 from-scratch check of HJ_DEEP (W) and (S).
   Own equivalent form (derived in reviews/hj-deep-review.md):
     n = tuv - u - v, t,u,v >= 2   <=>   n + u = d * v  with  d = tu - 1 = A,
     i.e. d | n+u, d == -1 (mod u), d >= 2u-1, v = (n+u)/d >= 2.
   WLOG u <= v (reversal u<->v maps A -> A* = tv-1, and A*A* = tn+1 == 1 mod n, same Jacobi),
   hence 2u(u-1) <= n.  Per-n search with a smallest-prime-factor table, early exit.
   (W): n>=2 with no word.  (S): non-square n == 1 (4) with words but no Jacobi -1 word.
   Squares: full enumeration, count -1 words (must be 0, T1).
   gcc -O2 -o /tmp/rhjws scripts/review_hj_ws.c ; /tmp/rhjws N  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static uint32_t *spf;
static int jac(uint64_t a, uint64_t n) { /* Jacobi (a/n), n odd positive */
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
/* mode 0: stop at first word; mode 1: stop at first -1 word; mode 2: count all words and -1 words.
   returns: bit0 = has word, bit1 = has -1 word; *cnt,*cneg filled in mode 2 */
static int search(uint64_t n, int mode, long *cnt, long *cneg, long *ufirst) {
  int res = 0; long c = 0, cn = 0;
  for (uint64_t u = 2; 2 * u * (u - 1) <= n; u++) {
    uint64_t m = n + u; int k = ndivs(m);
    for (int i = 0; i < k; i++) {
      uint64_t d = divs[i];
      if (d < 2 * u - 1 || (d + 1) % u) continue;
      uint64_t v = m / d; if (v < u) continue; /* WLOG u <= v */
      /* sanity: reconstruct */
      uint64_t t = (d + 1) / u;
      if (t * u * v - u - v != n) { fprintf(stderr, "BUG n=%lu\n", (unsigned long)n); exit(1); }
      res |= 1; c++;
      if (ufirst && *ufirst == 0) *ufirst = u;
      if (n & 1) { int j = jac(d, n); if (j == -1) { res |= 2; cn++; } }
      if (mode == 0) return res;
      if (mode == 1 && (res & 2)) return res;
    }
  }
  if (cnt) *cnt = c; if (cneg) *cneg = cn;
  return res;
}
int main(int argc, char **argv) {
  uint64_t N = strtoull(argv[1], 0, 10);
  uint64_t M = N + 2 * (uint64_t)sqrt((double)N) + 16;
  spf = calloc(M + 1, sizeof(uint32_t));
  for (uint64_t i = 2; i <= M; i++) if (!spf[i]) {
    spf[i] = i; if (i * i <= M) for (uint64_t j = i * i; j <= M; j += i) if (!spf[j]) spf[j] = i;
  }
  long nW = 0, nS = 0, sqneg = 0, nsq = 0; long umaxW = 0, umaxS = 0; uint64_t argW = 0, argS = 0;
  printf("(W) exceptions:");
  for (uint64_t n = 2; n < N; n++) {
    uint64_t r = (uint64_t)sqrtl((long double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++;
    int issq = (r * r == n);
    long uf = 0;
    if ((n & 3) == 1 && issq) {
      long c, cn; int res = search(n, 2, &c, &cn, &uf); nsq++;
      if (!(res & 1)) { nW++; printf(" %lu", (unsigned long)n); }
      if (cn) { sqneg++; fprintf(stderr, "square with -1 word: %lu\n", (unsigned long)n); }
      continue;
    }
    int mode = ((n & 3) == 1) ? 1 : 0;
    int res = search(n, mode, 0, 0, &uf);
    if (!(res & 1)) { nW++; printf(" %lu", (unsigned long)n); fflush(stdout); continue; }
    if (uf > umaxW) { umaxW = uf; argW = n; }
    if (mode == 1 && !(res & 2)) { nS++; fprintf(stderr, "(S) violation: %lu\n", (unsigned long)n); }
  }
  printf("\n#W=%ld  max first-u=%ld at n=%lu\n#S violations=%ld\nodd squares ==1(4) checked=%ld, with -1 word=%ld\n",
         nW, umaxW, (unsigned long)argW, nS, nsq, sqneg);
  return 0;
}
