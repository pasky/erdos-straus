/* O69 (POINTWISE_TYPEI2.md §2.1-2.2): enumerate ALL certificates at {2,7}-generic points
   (x*_q = 1 for q != 2,7) with Lambda = 2^(2+al+2ga) 7^(a+2b) <= LMAX, via Lemma 2.4:
     c' J J' - u = Lambda,  u | J+J',  k' = (J+J')/u,  c'k' prime to 14,  F = c'k' J - 1, (F,14)=1.
   Output lines:  al ga a b c' k' J J' F  M2 r2 M7 r7
   where the box is x_2 = r2 (mod M2=2^(2+al+ga)), x_7 = r7 (mod M7=7^(a+b)), r = -F.
   Enumeration over ordered (J,J') (both F and its cofactor are listed).
   Usage: typei2_s27 LMAX */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
typedef unsigned long long ull;

static void emit(int al, int ga, int a, int b, ll cp, ll J, ll Jp, ll u) {
  if ((J + Jp) % u) return;
  ll kp = (J + Jp) / u;
  if (cp % 2 == 0 || cp % 7 == 0 || kp % 2 == 0 || kp % 7 == 0) return;
  ll m = cp * kp;
  ll F = m * J - 1;
  if (F <= 0 || F % 2 == 0 || F % 7 == 0) return;
  ll M2 = 1LL << (2 + al + ga);
  ll M7 = 1; for (int i = 0; i < a + b; i++) M7 *= 7;
  ll r2 = ((-F) % M2 + M2) % M2, r7 = ((-F) % M7 + M7) % M7;
  printf("%d %d %d %d %lld %lld %lld %lld %lld %lld %lld %lld %lld\n", al, ga, a, b, cp, kp, J, Jp, F, M2, r2, M7, r7);
}

int main(int argc, char **argv) {
  ll LMAX = atoll(argv[1]);
  for (int a = 1; ; a += 2) {
    ll p7a = 1; for (int i = 0; i < a; i++) p7a *= 7;
    if (4 * p7a > LMAX) break;
    for (int b = 0; ; b++) {
      ll p7 = p7a; for (int i = 0; i < 2 * b; i++) p7 *= 7;
      if (4 * p7 > LMAX) break;
      for (int al = 0; ; al++) {
        if ((4LL << al) * p7 > LMAX) break;
        for (int ga = 0; ; ga++) {
          if ((4LL << (al + 2 * ga)) * p7 > LMAX) break;
          ll L = (4LL << (al + 2 * ga)) * p7;
          /* all (c',J,J',u): c' J J' = L + u, 1 <= u <= J+J' (necessary).  Enumerate J <= J'
             and emit both orders. */
          for (ll cp = 1; cp <= L + 4; cp++) {
            for (ll J = 1; ; J++) {
              ll g = cp * J;
              if (g == 1) {
                /* J'= L+u, u | L+1 */
                for (ll u = 1; u <= L + 1; u++) if ((L + 1) % u == 0) {
                  ll Jp = L + u;
                  emit(al, ga, a, b, cp, J, Jp, u);
                  if (Jp != J) emit(al, ga, a, b, cp, Jp, J, u);
                }
                continue;
              }
              /* need J' >= J and g J' - L in [1, J+J'] -> J' in (L/g, (L+J)/(g-1)] */
              ll lo = L / g + 1; if (lo < J) lo = J;
              ll hi = (L + J) / (g - 1);
              if (g * J > L + 2 * J && lo > hi) break; /* J too large for J' >= J */
              for (ll Jp = lo; Jp <= hi; Jp++) {
                ll u = g * Jp - L;
                if (u < 1 || u > J + Jp) continue;
                emit(al, ga, a, b, cp, J, Jp, u);
                if (Jp != J) emit(al, ga, a, b, cp, Jp, J, u);
              }
              if (g * J > L + 2 * J) break;
            }
          }
        }
      }
    }
  }
  return 0;
}
