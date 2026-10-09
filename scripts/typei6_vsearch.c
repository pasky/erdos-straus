/* O99 (POINTWISE_TYPEI6.md, Comp 4.1): complete search for regime-(v) fibre certificates at level L with
   v_7(k) = b, via the necessary size condition of Lemma 3.1(b):
       Q u^2 + 1 = 16 P X^2 > 64 c_o^4 delta^8 / T^4   (u = 7^b, Q = d/P)
   i.e.  P (64 c_o^4 delta^8 - T^4) < u^2 d T^4.
   Enumerates a odd, delta odd, c' odd (7 !| c'), P1 | M = c_o delta^2 + T with P1 <= P1max; tests
   16 P | Q u^2 + 1 and (Q u^2 + 1)/(16 P) = X^2 (X odd, 7 !| X) exactly (GMP).
   Divisors: M is factored by a sieve along c' (M = A c' + T is an arithmetic progression) while P1max >= SMALL;
   otherwise P1 runs over odd numbers <= P1max.
   Output: one line per solution "L b a c' delta P1 X" (every solution of (1.1) with the size condition, regime
   (v) or not); stderr: counts.
   Usage: typei6_vsearch L b [u]   (u: test an arbitrary odd u instead of 7^b; regression only)   */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <gmp.h>
typedef unsigned long long u64; typedef __int128 i128; typedef unsigned __int128 u128;
typedef long double ld;
#define SMALL 64
#define BLK (1<<18)
#define MAXF 20
static int L, b; static u64 T, UU = 0; /* UU: optional odd u replacing 7^b (relaxed regression) */ static mpz_t U2, N, Qz, X;
static long nsol = 0, ncand = 0, nmod = 0;
static u64 mulmod(u64 a, u64 c, u64 m) { return (u64)((u128)a * c % m); }
static u64 u2mod(u64 m) { /* u^2 mod m */ if (UU) return mulmod(UU % m, UU % m, m); u64 r = 1 % m, p = 49 % m; int e = b; while (e) { if (e & 1) r = mulmod(r, p, m); p = mulmod(p, p, m); e >>= 1; } return r; }
static u64 *primes; static long np;
static void test(int a, u64 p7a, u64 cp, u64 dl, u64 M, u64 P1) {
  ncand++;
  u64 Q1 = M / P1; u128 P = (u128)cp * P1;
  if (P > ((u128)1 << 58)) { /* fall back to GMP for the divisibility test */ }
  else {
    u64 m = (u64)(16 * P);
    u64 q = mulmod(p7a % m, Q1 % m, m);
    if ((mulmod(q, u2mod(m), m) + 1) % m) return;
  }
  nmod++;
  mpz_set_ui(Qz, Q1); mpz_mul_ui(Qz, Qz, p7a); mpz_mul(N, Qz, U2); mpz_add_ui(N, N, 1);
  mpz_t Pz; mpz_init(Pz); mpz_set_ui(Pz, cp); mpz_mul_ui(Pz, Pz, P1); mpz_mul_ui(Pz, Pz, 16);
  if (!mpz_divisible_p(N, Pz)) { mpz_clear(Pz); return; }
  mpz_divexact(N, N, Pz); mpz_clear(Pz);
  if (!mpz_perfect_square_p(N)) return;
  mpz_sqrt(X, N);
  if (mpz_even_p(X) || mpz_divisible_ui_p(X, 7)) return;
  printf("%d %d %d %llu %llu %llu ", L, b, a, cp, dl, P1); mpz_out_str(stdout, 10, X); printf("\n"); fflush(stdout);
  nsol++;
}
/* P1max from P (64 c_o^4 d^8 - T^4) < u^2 d T^4 ; returns huge if vacuous */
static ld p1max(u64 p7a, u64 cp, u64 dl) {
  ld co = (ld)p7a * cp, D = (ld)dl, Tl = (ld)T;
  ld lhs = 64 * powl(co, 4) * powl(D, 8) - powl(Tl, 4);
  ld d = co * (co * D * D + Tl);
  ld u2 = UU ? (ld)UU * UU : powl(7.0L, 2 * b);
  if (lhs <= 0) return 1e30L;
  return u2 * d * powl(Tl, 4) / (lhs * cp) * (1 + 1e-9L);
}
static void divisors_test(int a, u64 p7a, u64 cp, u64 dl, u64 M, u64 *pf, int *pe, int nf, u64 lim) {
  static u64 dv[1 << 16]; int nd = 1; dv[0] = 1;
  for (int i = 0; i < nf; i++) { int n0 = nd; u64 pw = 1;
    for (int k = 1; k <= pe[i]; k++) { pw *= pf[i]; for (int t = 0; t < n0; t++) { if (nd >= (1 << 16)) { fprintf(stderr, "divisor overflow\n"); exit(2); } dv[nd++] = dv[t] * pw; } } }
  for (int t = 0; t < nd; t++) if (dv[t] <= lim) test(a, p7a, cp, dl, M, dv[t]);
}
int main(int argc, char **argv) {
  L = atoi(argv[1]); b = atoi(argv[2]); T = 1ULL << (L - 4);
  mpz_init(U2); mpz_init(N); mpz_init(Qz); mpz_init(X); if (argc > 3) UU = strtoull(argv[3], 0, 10);
  if (UU) mpz_set_ui(U2, UU), mpz_mul(U2, U2, U2); else mpz_ui_pow_ui(U2, 7, 2 * b);
  /* primes up to 2^32 sqrt bound needed: M < 2^63 -> sqrt < 3.04e9; we sieve primes up to PMAX and require M <= PMAX^2 */
  u64 PMAX = 1ULL << 25; char *isc = calloc(PMAX + 1, 1); primes = malloc(sizeof(u64) * 2200000); np = 0;
  for (u64 i = 2; i <= PMAX; i++) if (!isc[i]) { primes[np++] = i; for (u64 j = i * i; j <= PMAX; j += i) isc[j] = 1; }
  free(isc);
  u64 p7a = 7;
  for (int a = 1;; a += 2, p7a *= 49) {
    if (p1max(p7a, 1, 1) < 1) break;
    for (u64 dl = 1;; dl += 2) {
      if (p1max(p7a, 1, dl) < 1) break;
      u64 A = p7a * dl * dl;
      /* largest c' with p1max >= 1 (p1max is decreasing in c' once lhs>0 dominates; scan geometric) */
      u64 cmax = 1; while (p1max(p7a, cmax * 2 + 1, dl) >= 1 || 64.0L * powl((ld)p7a * cmax * 2, 4) * powl(dl, 8) < 2 * powl((ld)T, 4)) cmax = cmax * 2 + 1;
      cmax = cmax * 2 + 1;
      /* sieve region: c' with p1max >= SMALL */
      u64 csieve = 1; while (csieve < cmax && p1max(p7a, csieve, dl) >= SMALL) csieve += 2;
      if ((ld)A * csieve + T > (ld)PMAX * PMAX) { fprintf(stderr, "M too large for sieve (a=%d dl=%llu)\n", a, dl); exit(3); }
      /* sieved part: odd c' in [1, csieve) */
      static u64 rem[BLK]; static u64 pf[BLK][MAXF]; static int pe[BLK][MAXF]; static int nfac[BLK];
      for (u64 c0 = 1; c0 < csieve; c0 += 2 * (u64)BLK) {
        u64 cnt = (csieve - c0 + 1) / 2; if (cnt > BLK) cnt = BLK;
        for (u64 i = 0; i < cnt; i++) { rem[i] = A * (c0 + 2 * i) + T; nfac[i] = 0; }
        u64 Mhi = A * (c0 + 2 * (cnt - 1)) + T;
        for (long k = 1; k < np && primes[k] * primes[k] <= Mhi; k++) { u64 p = primes[k];
          if (A % p == 0) continue;
          /* solve A (c0 + 2 i) + T == 0 mod p for i */
          u64 s = (2 * (A % p)) % p; u64 rhs = (p - (mulmod(A % p, c0 % p, p) + T % p) % p) % p;
          /* inverse of s mod p */
          long long t0 = 0, t1 = 1; long long r0 = p, r1 = s; while (r1) { long long q = r0 / r1, tt = t0 - q * t1; t0 = t1; t1 = tt; tt = r0 - q * r1; r0 = r1; r1 = tt; }
          u64 inv = (u64)((t0 % (long long)p + p) % p);
          for (u64 i = mulmod(rhs, inv, p); i < cnt; i += p) { int e = 0; while (rem[i] % p == 0) { rem[i] /= p; e++; }
            if (nfac[i] >= MAXF) { fprintf(stderr, "MAXF\n"); exit(4); } pf[i][nfac[i]] = p; pe[i][nfac[i]] = e; nfac[i]++; }
        }
        for (u64 i = 0; i < cnt; i++) { u64 cp = c0 + 2 * i; if (cp % 7 == 0) continue;
          if (rem[i] > 1) { pf[i][nfac[i]] = rem[i]; pe[i][nfac[i]] = 1; nfac[i]++; }
          ld lim = p1max(p7a, cp, dl); u64 M = A * cp + T;
          divisors_test(a, p7a, cp, dl, M, pf[i], pe[i], nfac[i], lim > 1.8e19L ? ~0ULL : (u64)lim);
        }
      }
      /* small part: odd c' >= csieve, P1 odd <= p1max < SMALL */
      for (u64 cp = csieve | 1; cp <= cmax; cp += 2) { if (cp % 7 == 0) continue;
        ld lim = p1max(p7a, cp, dl); if (lim < 1) continue; u64 M = A * cp + T;
        for (u64 P1 = 1; P1 <= (u64)lim; P1 += 2) if (M % P1 == 0) test(a, p7a, cp, dl, M, P1);
      }
    }
  }
  fprintf(stderr, "L=%d b=%d: %ld candidates, %ld pass mod 16P, %ld solutions\n", L, b, ncand, nmod, nsol);
  return 0;
}
