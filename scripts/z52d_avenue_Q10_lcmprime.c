/* z52d avenue Q10 (Z0686): R(p) = #{(u,C): (4uC-1) | p+u} (trial form, PARITY_AUDIT Lemma 2.1) and the b = 1 line
   count L1(p) = #{d >= 1, s | p+4d, s ≡ -1 (mod 4d)} for p = lcm(1..k)+1 and a few nearby control primes.
   Build: cc -O2 -o /tmp/lcmprime scripts/z52d_avenue_Q10_lcmprime.c ; run: timeout 60 /tmp/lcmprime <p> ... */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
int main(int argc, char **argv) {
  for (int a = 1; a < argc; a++) {
    u64 p = strtoull(argv[a], 0, 10), R = 0;
    for (u64 u = 1; 4 * u - 1 <= p + u; u++)
      for (u64 m = 4 * u - 1; m <= p + u; m += 4 * u)
        if ((p + u) % m == 0) R++;
    printf("p=%llu R=%llu\n", p, R);
  }
  return 0;
}
