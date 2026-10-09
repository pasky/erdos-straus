/* R99 from-scratch engine for regime-(v) fibre certificates at level L, v_7(k)=b (POINTWISE_TYPEI6 Comp 4.1).
   Necessary condition (Lemma 3.1(b), re-derived by R99, weakened by sqrt d >= c_o delta):
       c := 16 P X^2 = Q u^2 + 1 > 64 c_o^4 delta^8 / T^4,   Q = d/P,  d = c_o M,  M = c_o delta^2 + T.
   <=>  P*(64 c_o^4 delta^8 - T^4) < u^2 d T^4            (checked EXACTLY with GMP for every divisor tested)
   Enumeration: a odd, delta odd, c' odd 7!|c', P1 | M. Loop termination uses the P1=1 instance of the exact
   inequality, which is monotone decreasing in a, delta, c' once 64 x^4 > T^4 (x = c_o delta^2): R99 review §Comp 4.1.
   M factored by smallest-prime-factor table (M < SPFMAX) or trial division by primes (M < 2^62).
   For every divisor P1 of M passing the exact inequality: N = 7^a (M/P1) u^2 + 1; require 16 c' P1 | N and
   N/(16 c' P1) = X^2, X odd, 7 !| X. Prints "SOL L u a c' delta P1 X regime" where regime is computed
   (j, lambda, sigma) for case B, or "A" for case A.
   Usage: review_typei6_vsearch L b      or   review_typei6_vsearch L 0 U1 U2 ...  (arbitrary odd u's; relaxed control) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <gmp.h>
typedef unsigned long long u64;
#define SPFMAX (1u<<27)
static uint32_t *spf; static uint32_t *pr; static long npr;
static int L; static u64 T; static mpz_t U, U2, T4, lhs, rhs, tmp, N, Pz, Xz, cz;
static long ntriples = 0, ndiv = 0, npass = 0, nsol = 0;

static int factor(u64 M, u64 *p, int *e) {
  int k = 0;
  if (M < SPFMAX) { while (M > 1) { u64 q = spf[M]; int c = 0; while (M % q == 0) { M /= q; c++; } p[k] = q; e[k++] = c; } return k; }
  for (long i = 0; i < npr; i++) { u64 q = pr[i]; if (q * q > M) break; if (M % q == 0) { int c = 0; while (M % q == 0) { M /= q; c++; } p[k] = q; e[k++] = c; } }
  if (M > 1) { if (M > (u64)pr[npr-1] * pr[npr-1]) { fprintf(stderr, "trial division range exceeded\n"); exit(3); } p[k] = M; e[k++] = 1; }
  return k;
}
/* exact test of P*(64 c_o^4 delta^8 - T^4) < u^2 * c_o*M * T^4 */
static int bound_ok(u64 co_hi_7a, u64 cp, u64 de, u64 M, u64 P) {
  mpz_set_ui(tmp, co_hi_7a); mpz_mul_ui(tmp, tmp, cp); mpz_mul_ui(tmp, tmp, de); mpz_mul_ui(tmp, tmp, de); /* x = c_o de^2 */
  mpz_pow_ui(lhs, tmp, 4); mpz_mul_ui(lhs, lhs, 64); mpz_sub(lhs, lhs, T4); mpz_mul_ui(lhs, lhs, cp); mpz_mul_ui(lhs, lhs, P / cp);
  mpz_set_ui(rhs, co_hi_7a); mpz_mul_ui(rhs, rhs, cp); mpz_mul_ui(rhs, rhs, M); mpz_mul(rhs, rhs, U2); mpz_mul(rhs, rhs, T4);
  return mpz_cmp(lhs, rhs) < 0;
}
static void report(u64 p7a, int a, u64 cp, u64 de, u64 P1) {
  /* regime classification from scratch: y = c' g delta, g = 4 P1 X - 7^a u delta, j = T u/2 - y */
  mpz_t g, y, j, m, rho, lam, sig, t2; mpz_inits(g, y, j, m, rho, lam, sig, t2, NULL);
  mpz_mul_ui(g, Xz, 4 * P1); mpz_mul_ui(t2, U, p7a); mpz_mul_ui(t2, t2, de); mpz_sub(g, g, t2);
  mpz_mul_ui(y, g, cp * de); mpz_mul_ui(j, U, T / 2); mpz_sub(j, j, y);
  gmp_printf("SOL L=%d u=%Zd a=%d c'=%llu delta=%llu P1=%llu X=%Zd ", L, U, a, cp, de, P1, Xz);
  if (mpz_sgn(j) < 0) printf("caseA\n");
  else {
    mpz_set_ui(m, cp * de * de);
    mpz_mul_ui(rho, U, T / 2); mpz_add(rho, rho, j); if (!mpz_divisible_ui_p(rho, P1)) printf("[rho non-integral!] "); mpz_divexact_ui(rho, rho, P1);
    mpz_mul(lam, rho, j); mpz_sub(lam, lam, m); if (!mpz_divisible_p(lam, U)) printf("[lambda non-integral!] "); mpz_divexact(lam, lam, U);
    /* sigma = 8 7^a m j + 4 T j - T^2 u */
    mpz_mul(sig, m, j); mpz_mul_ui(sig, sig, 8 * p7a); mpz_mul_ui(t2, j, 4 * T); mpz_add(sig, sig, t2);
    mpz_mul_ui(t2, U, T * T); mpz_sub(sig, sig, t2);
    gmp_printf("j=%Zd lambda=%Zd sigma=%Zd regime=%s\n", j, lam, sig,
      mpz_sgn(lam) < 0 ? "ii" : mpz_sgn(sig) < 0 ? "iii" : mpz_sgn(sig) == 0 ? "iv" : "v");
  }
  fflush(stdout); mpz_clears(g, y, j, m, rho, lam, sig, t2, NULL);
}
static void try_div(u64 p7a, int a, u64 cp, u64 de, u64 M, u64 P1) {
  ndiv++;
  u64 P = cp * P1;  /* < 2^63 guaranteed by caller */
  if (!bound_ok(p7a, cp, de, M, P)) return;
  npass++;
  mpz_set_ui(N, p7a); mpz_mul_ui(N, N, M / P1); mpz_mul(N, N, U2); mpz_add_ui(N, N, 1);
  mpz_set_ui(Pz, P); mpz_mul_ui(Pz, Pz, 16);
  if (!mpz_divisible_p(N, Pz)) return;
  mpz_divexact(N, N, Pz);
  if (!mpz_perfect_square_p(N)) return;
  mpz_sqrt(Xz, N);
  if (mpz_even_p(Xz) || mpz_divisible_ui_p(Xz, 7)) return;
  nsol++; report(p7a, a, cp, de, P1);
}
static void divs(u64 p7a, int a, u64 cp, u64 de, u64 M, u64 *p, int *e, int k, int i, u64 cur) {
  if (i == k) { try_div(p7a, a, cp, de, M, cur); return; }
  u64 q = 1; for (int t = 0; t <= e[i]; t++) { divs(p7a, a, cp, de, M, p, e, k, i + 1, cur * q); q *= p[i]; }
}
/* P1 = 1 instance, used for loop termination (monotone, see header) */
static int alive(u64 p7a, u64 cp, u64 de) {
  if ((unsigned __int128)p7a * cp * de * de + T >= ((unsigned __int128)1 << 62)) { fprintf(stderr, "overflow guard alive\n"); exit(4); }
  return bound_ok(p7a, cp, de, p7a * cp * de * de + T, cp); }
static int vacuous(u64 p7a, u64 cp, u64 de) { /* 64 x^4 <= T^4 */
  long double x = (long double)p7a * cp * de * de; return 64.0L * x * x * x * x <= (long double)T * T * T * T * 1.0000001L; }
int main(int argc, char **argv) {
  L = atoi(argv[1]); int b = atoi(argv[2]); T = 1ULL << (L - 4);
  mpz_inits(U, U2, T4, lhs, rhs, tmp, N, Pz, Xz, cz, NULL);
  mpz_ui_pow_ui(T4, T, 4);
  spf = calloc(SPFMAX, 4);
  for (u64 i = 2; i < SPFMAX; i++) if (!spf[i]) for (u64 j = i; j < SPFMAX; j += i) if (!spf[j]) spf[j] = i;
  pr = malloc(sizeof(uint32_t) * 8000000); npr = 0;
  for (u64 i = 3; i < SPFMAX && npr < 8000000; i++) if (spf[i] == i) pr[npr++] = i;
  for (int arg = 3; arg < (argc > 3 ? argc : 4); arg++) {
  if (argc > 3) mpz_set_str(U, argv[arg], 10); else mpz_ui_pow_ui(U, 7, b);
  mpz_mul(U2, U, U); ntriples = ndiv = npass = nsol = 0;
  u64 pf[64]; int pe[64];
  u64 p7a = 7;
  for (int a = 1;; a += 2, p7a *= 49) {
    if (p7a > (1ULL << 56)) { fprintf(stderr, "a too large guard\n"); exit(5); }
    if (!vacuous(p7a, 1, 1) && !alive(p7a, 1, 1)) break;
    for (u64 de = 1;; de += 2) {
      if (!vacuous(p7a, 1, de) && !alive(p7a, 1, de)) break;
      for (u64 cp = 1;; cp += 2) {
        if (cp % 7 == 0) continue;
        int vac = vacuous(p7a, cp, de);
        if (!vac && !alive(p7a, cp, de)) break;
        u64 M = p7a * cp * de * de + T;
        if (M >= (1ULL << 62) / 1 || (double)cp * M > 4e18) { fprintf(stderr, "overflow guard M\n"); exit(4); }
        ntriples++;
        int k = factor(M, pf, pe);
        divs(p7a, a, cp, de, M, pf, pe, k, 0, 1);
      }
    }
  }
  gmp_fprintf(stderr, "L=%d u=%Zd: triples=%ld divisors=%ld pass-bound=%ld solutions=%ld\n", L, U, ntriples, ndiv, npass, nsol);
  }
  return 0;
}
