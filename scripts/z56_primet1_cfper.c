// z56 PRIMET1: period length of the continued fraction of sqrt(p) (p not a square), for each p on stdin.
// Standard recurrence m' = d a - m, d' = (p - m'^2)/d, a' = floor((a0 + m')/d'); the period ends when a = 2 a0.
// Usage: z56_primet1_cfper < primes.txt   output "p len"
#include <stdio.h>
#include <math.h>
typedef unsigned long long u64; typedef long long ll;
int main(void) {
  u64 p;
  while (scanf("%llu", &p) == 1) {
    ll a0 = (ll)sqrtl((long double)p); while ((u64)(a0 + 1) * (a0 + 1) <= p) a0++; while ((u64)a0 * a0 > p) a0--;
    ll m = 0, d = 1, a = a0; u64 len = 0;
    if ((u64)a0 * a0 == p) { printf("%llu 0\n", p); continue; }
    do { m = d * a - m; d = (ll)((p - (u64)(m * m)) / (u64)d); a = (a0 + m) / d; len++; } while (a != 2 * a0);
    printf("%llu %llu\n", p, len);
  }
  return 0;
}
