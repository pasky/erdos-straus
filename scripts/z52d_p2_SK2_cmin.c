/* Pass-2 SK2: C-form census. For each prime p = 1 (mod 4), p <= PMAX, output "p Cmin"
   where Cmin = least C <= CAP such that 4Cp+1 has a divisor d = -1 (mod 4C) (0 if none <= CAP).
   Usage: z52d_p2_SK2_cmin PMAX CAP NPROC K   (processes primes with index % NPROC == K)
   Memory: sieve bit array only. Divisors enumerated from full factorisation of N = 4Cp+1. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static u64 *sp; static long nsp = 0;
static int divs_check(u64 N, u64 m) { /* does N have divisor d with d = m-1 mod m ? (m=4C) */
  u64 ps[64]; int es[64]; int k = 0; u64 M = N;
  for (long i = 0; i < nsp && sp[i] * sp[i] <= M; i++) {
    if (M % sp[i] == 0) { int e = 0; while (M % sp[i] == 0) { M /= sp[i]; e++; } ps[k] = sp[i]; es[k] = e; k++; }
  }
  if (M > 1) { ps[k] = M; es[k] = 1; k++; }
  /* enumerate divisors mod m: residues reachable as products of subsets of prime powers */
  u64 cap = 1; for (int i = 0; i < k; i++) cap *= (es[i] + 1);
  /* DFS over exponents, track residue mod m; only need residue m-1 */
  static u64 stack_r[4096]; static int stack_i[4096], stack_e[4096];
  int top = 0; stack_r[top] = 1 % m; stack_i[top] = 0; stack_e[top] = 0; top++;
  /* simple recursive-free enumeration */
  u64 res_list_n = 0; (void)res_list_n; (void)cap;
  int found = 0;
  /* iterate over all exponent vectors via odometer */
  int ex[64]; memset(ex, 0, sizeof(ex));
  while (1) {
    u64 r = 1 % m;
    for (int i = 0; i < k; i++) for (int e = 0; e < ex[i]; e++) r = (r * (ps[i] % m)) % m;
    if (r == m - 1) { found = 1; break; }
    int i = 0;
    while (i < k) { ex[i]++; if (ex[i] <= es[i]) break; ex[i] = 0; i++; }
    if (i == k) break;
  }
  return found;
}
int main(int argc, char **argv) {
  long PMAX = atol(argv[1]); long CAP = atol(argv[2]); long NP = atol(argv[3]); long K = atol(argv[4]);
  long SQ = 1 + (long)sqrt(4.0 * (double)CAP * (double)PMAX + 1.0);
  char *isc = calloc(SQ + 1, 1);
  sp = malloc(sizeof(u64) * (SQ / 2 + 10));
  for (long i = 2; i <= SQ; i++) if (!isc[i]) { sp[nsp++] = (u64)i; for (long j = i * i; j <= SQ; j += i) isc[j] = 1; }
  char *cs = calloc(PMAX + 1, 1); long idx = 0;
  for (long i = 2; i <= PMAX; i++) if (!cs[i]) { for (long j = i * i; j <= PMAX; j += i) cs[j] = 1; }
  for (long p = 5; p <= PMAX; p++) {
    if (cs[p] || (p % 4) != 1) continue;
    idx++; if (idx % NP != K) continue;
    long found = 0;
    for (long C = 1; C <= CAP && !found; C++) {
      u64 N = 4ULL * C * (u64)p + 1, m = 4ULL * C;
      if (divs_check(N, m)) found = C;
    }
    printf("%ld %ld\n", p, found);
  }
  return 0;
}
