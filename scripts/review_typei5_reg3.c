/* R92 from-scratch complete enumeration of regime (iii) of TYPEI5 Prop 3.3 (lambda>0, 0<Delta<2Tj) with u = 7^b.
   Own derivation: s = 2Tj - Delta >= 1, kappa = 8 W lambda (W = 7^a, a odd), g = 2T^3 - s kappa > 0,
   u (g j - s T^2) = N(j) = 4 kappa j^3 + (2Tj - s)(4Tj + s),  e := g j - s T^2 > 0 divides
   R = g^3 N(sT^2/g) = kappa s^3 (4T^3 - s kappa)^2  (polynomial division with integral quotient, sympy-checked).
   For every divisor e of R with e = -sT^2 (mod g) and j = (e+sT^2)/g odd, test N(j)/e in {7^b} modulo two
   61-bit primes (a genuine solution always passes); survivors are printed for exact verification.
   Usage: review_typei5_reg3 L [control_u] */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef long long ll;
static const u64 P1 = 2305843009213693951ULL; /* 2^61-1 */
static const u64 P2 = 2305843009213693921ULL; /* not nec. prime; only used as a modulus with tables */
#define BMAX 400
static u64 pw1[BMAX + 1], pw2[BMAX + 1];
static u64 mulm(u64 a, u64 b, u64 p) { return (u64)((u128)a * b % p); }
static u64 powm(u64 a, u64 e, u64 p) { u64 r = 1; a %= p; while (e) { if (e & 1) r = mulm(r, a, p); a = mulm(a, a, p); e >>= 1; } return r; }
static int *spf; static int NS;
static int pr[64], ex[64], np;
static void addf(ll n, int mult) { while (n > 1) { int p = spf[n], e = 0; while (n % p == 0) { n /= p; e++; }
    int i; for (i = 0; i < np; i++) if (pr[i] == p) break; if (i == np) { pr[np] = p; ex[np] = 0; np++; } ex[i] += e * mult; } }
static ll T, kap, s, g; static int L, a; static ll lam; static long ndiv = 0, ncand = 0, nmatch = 0; static u128 sT2;
static u64 inv1(u64 x) { return powm(x, P1 - 2, P1); }
static int in_tab(u64 t, u64 *tab) { for (int b = 0; b <= BMAX; b++) if (tab[b] == t) return 1; return 0; }
static void test(u128 e) {
  ndiv++;
  if ((e + sT2) % (u128)g) return;
  u128 j = (e + sT2) / (u128)g; if (!(j & 1)) return;
  ncand++;
  long double jl = (long double)j; long double Nl = 4.0L * kap * jl * jl * jl + 8.0L * T * T * jl * jl;
  if (logl(Nl) / logl(7.0L) > BMAX - 2) { fprintf(stderr, "BMAX too small L=%d a=%d lam=%lld s=%lld\n", L, a, lam, s); exit(1); }
  /* N(j) mod p, e mod p */
  u64 jm = (u64)(j % P1), em = (u64)(e % P1);
  u64 N1 = (mulm(mulm(4 * (u64)kap % P1, jm, P1), mulm(jm, jm, P1), P1)
           + mulm((mulm(2 * (u64)T, jm, P1) + P1 - (u64)s % P1) % P1, (mulm(4 * (u64)T, jm, P1) + (u64)s) % P1, P1)) % P1;
  if (em == 0) { nmatch++; goto out; }
  u64 t1 = mulm(N1, inv1(em), P1);
  if (!in_tab(t1, pw1)) return;
  {
    u64 jm2 = (u64)(j % P2), em2 = (u64)(e % P2);
    u64 N2 = (mulm(mulm(4 * (u64)kap % P2, jm2, P2), mulm(jm2, jm2, P2), P2)
             + mulm((mulm(2 * (u64)T, jm2, P2) + P2 - (u64)s % P2) % P2, (mulm(4 * (u64)T, jm2, P2) + (u64)s) % P2, P2)) % P2;
    int ok = 0; for (int b = 0; b <= BMAX; b++) if (mulm(pw2[b], em2, P2) == N2) { ok = 1; break; }
    if (!ok) return;
  }
  nmatch++;
out:;
  char buf[64]; int k = 63; buf[k] = 0; u128 x = j; do { buf[--k] = '0' + (int)(x % 10); x /= 10; } while (x);
  printf("%d %d %lld %lld %s\n", L, a, lam, s, buf + k);
}
static void gen(int i, u128 e) { if (i == np) { test(e); return; } u128 f = 1; for (int k = 0; k <= ex[i]; k++) { gen(i + 1, e * f); f *= pr[i]; } }
int main(int argc, char **argv) {
  L = atoi(argv[1]); T = 1LL << (L - 4); NS = (int)(4 * T * T * T + 16);
  spf = calloc(NS + 1, sizeof(int)); for (int i = 2; i <= NS; i++) if (!spf[i]) for (ll k = i; k <= NS; k += i) if (!spf[k]) spf[k] = i;
  for (int b = 0; b <= BMAX; b++) { pw1[b] = powm(7, b, P1); pw2[b] = powm(7, b, P2); }
  if (argc > 2) { u64 cu = strtoull(argv[2], 0, 10); for (int b = 0; b <= BMAX; b++) { pw1[b] = cu % P1; pw2[b] = cu % P2; } } /* positive control: look for u = argv[2] instead of 7-powers */
  long ncase = 0;
  for (ll W = 7; 4 * W < T * T * T; W *= 49) { a = 0; for (ll w = W; w > 1; w /= 7) a++;
    for (lam = 1; 4 * W * lam < T * T * T; lam++)
      for (s = 1; 4 * W * lam * s < T * T * T; s++) {
        kap = 8 * W * lam; g = 2 * T * T * T - s * kap; if (g <= 0) continue; /* cannot happen given the loop bound */
        ll w4 = 4 * T * T * T - s * kap; sT2 = (u128)s * T * T; ncase++;
        np = 0; addf(kap, 1); addf(s, 3); addf(w4, 2); gen(0, 1);
      }
  }
  fprintf(stderr, "L=%d: %ld (a,lam,s) cases, %ld divisors, %ld j-candidates, %ld 7-power matches\n", L, ncase, ndiv, ncand, nmatch);
  return 0;
}
