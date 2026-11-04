// z56 PRIMET1: continued fraction of sqrt(p) (p not a square), for each p on stdin. Output "p len a1 amax":
//   len  = period length;
//   a1   = first partial quotient after a0;
//   amax = max{a_{i+1} : i >= 1, q_i <= 1000} (q_i convergent denominators: q_0 = 1, q_1 = a1, q_{i} = a_i q_{i-1} + q_{i-2}),
//          i.e. the largest partial quotient that follows a convergent with denominator <= 1000 (G17, Amendment 1);
//          0 if no such i (cannot happen for p > 10^6 unless the period ends first; then the scan wraps within the period).
// Recurrence m' = d a - m, d' = (p - m'^2)/d, a' = floor((a0 + m')/d'); the period ends when a = 2 a0.
#include <stdio.h>
#include <math.h>
typedef unsigned long long u64; typedef long long ll;
int main(void) {
  u64 p;
  while (scanf("%llu", &p) == 1) {
    ll a0 = (ll)sqrtl((long double)p); while ((u64)(a0 + 1) * (a0 + 1) <= p) a0++; while ((u64)a0 * a0 > p) a0--;
    if ((u64)a0 * a0 == p) { printf("%llu 0 0 0\n", p); continue; }
    ll m = 0, d = 1, a = a0; u64 len = 0;
    double qm2 = 0, qm1 = 1; // q_{-1} = 0, q_0 = 1
    ll a1 = 0, amax = 0; int scanning = 1;
    do {
      m = d * a - m; d = (ll)((p - (u64)(m * m)) / (u64)d); a = (a0 + m) / d; len++;
      // a is a_len
      if (len == 1) a1 = a;
      if (scanning) {
        if (len >= 2) { if (qm1 <= 1000.0) { if (a > amax) amax = a; } else scanning = 0; }
        double qn = (double)a * qm1 + qm2; qm2 = qm1; qm1 = qn; // q_len
      }
    } while (a != 2 * a0);
    printf("%llu %llu %lld %lld\n", p, len, a1, amax);
  }
  return 0;
}
