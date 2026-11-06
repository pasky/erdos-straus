/* z60 RAYCLASS: per-integer counts of (★) and of its single-field (t0 = 1, field Q(sqrt(-n))) sub-families.
 *
 * For each odd n in the requested list/range (n ≡ 1 mod 4) prints
 *   n R Sq_u Sq_C S1 Sq_uC
 * R    = #{(u,B,C) : 4uBC - u - B = n}   via the (MS) d-form: d ≡ 3 (4), 3 ≤ d ≤ (4n+1)/3, r = (-n mod d) | (d+1)/4
 *        (u = r, C = (d+1)/(4r), B = (n+r)/d);  r = 0 (d | n) is skipped (no solution).
 * Sq_u = # of those with u a perfect square   (ideal divisors of s + sqrt(-n), field Q(sqrt(-n)))
 * Sq_C = # of those with C a perfect square   (ideal divisors of 1 + 2s sqrt(-n), field Q(sqrt(-n)))
 * Sq_uC = # of those with BOTH u and C perfect squares (the overlap of the two slices)
 * S1   = # Type II solutions with d = 1, i.e. (a,b,c) with 4abc = a + b + nc  (the "shot family";
 *        ideal divisors of 1 + 2c sqrt(-n) with norm ≡ -1 mod 4c, equivalently of 2a + sqrt(-n) with norm ≡ -1 mod 4a).
 *        Enumerated as pairs (a, g): g | n + 4a^2, g ≡ -n (mod 4a), 1 ≤ a ≤ (n+3)/3  (f = (n+4a^2)/g ≡ -1 mod 4a).
 *        For gcd(n, 4a) = 1 this is exact; for gcd > 1 we fall back to testing f directly (see code).
 * Mode: ./fam range LO HI      (all primes p ≡ 1 mod 4 in [LO,HI])
 *       ./fam list FILE        (integers from FILE, '#' lines ignored)
 *       ./fam s1zeros LO HI    (primes p ≡ 1 mod 4 in [LO,HI] with S1(p) = 0; early exit per prime)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

typedef unsigned long long u64;
typedef __uint128_t u128;

static int is_square(u64 x) { u64 s = (u64)sqrtl((long double)x); while (s * s > x) s--; while ((s + 1) * (s + 1) <= x) s++; return s * s == x; }

static int is_prime(u64 n) {
  if (n < 2) return 0;
  for (u64 q = 2; q * q <= n; q++) if (n % q == 0) return 0;
  return 1;
}

static void rcount(u64 n, long *R, long *Su, long *SC, long *SB) {
  *R = *Su = *SC = *SB = 0;
  u64 dmax = (4 * n + 1) / 3;
  for (u64 d = 3; d <= dmax; d += 4) {
    u64 r = (d - n % d) % d;
    if (r == 0) continue;
    u64 q = (d + 1) / 4;
    if (q % r) continue;
    (*R)++;
    u64 C = q / r;
    int a = is_square(r), b = is_square(C);
    if (a) (*Su)++;
    if (b) (*SC)++;
    if (a && b) (*SB)++;
  }
}

/* S1: solutions (a,b,c) of 4abc = a + b + n c.  If stop1, return as soon as one is found. */
static long s1count(u64 n, int stop1) {
  long cnt = 0;
  u64 amax = (n + 3) / 3 + 1;
  for (u64 a = 1; a <= amax; a++) {
    u64 m = 4 * a;
    u128 N = (u128)n + (u128)4 * a * a;
    /* f*g = N, f ≡ -1 (mod m), f ≥ m - 1  ⇔  g ≤ N/(m-1).  Enumerate g directly when gcd(n, m) = 1. */
    u64 gmax = (u64)(N / (m - 1));
    u64 nm = n % m;
    if (nm % 2 == 0) { /* n odd so never */ }
    /* gcd(n, m) */
    u64 x = n, y = m; while (y) { u64 t = x % y; x = y; y = t; }
    if (x == 1) {
      u64 g0 = (m - nm) % m; if (g0 == 0) g0 = m;
      for (u64 g = g0; g <= gmax; g += m) {
        if ((u64)(N % g) == 0) {
          u64 f = (u64)(N / g);
          if (f % m == m - 1) { cnt++; if (stop1) return cnt; }
        }
      }
    } else {
      /* fall back: enumerate f ≡ -1 (mod m), f ≤ N, f | N   (rare: only when gcd(n, a) > 1) */
      for (u128 f = m - 1; f <= N; f += m) {
        if (N % f == 0) { cnt++; if (stop1) return cnt; }
      }
    }
  }
  return cnt;
}

int main(int argc, char **argv) {
  const char *use = "usage: fam range LO HI | fam list FILE | fam s1zeros LO HI\n";
  if (argc < 3) { fprintf(stderr, "%s", use); return 1; }
  if ((!strcmp(argv[1], "range") || !strcmp(argv[1], "s1zeros")) && argc < 4) { fprintf(stderr, "%s", use); return 1; }
  if (!strcmp(argv[1], "range")) {
    u64 lo = strtoull(argv[2], 0, 10), hi = strtoull(argv[3], 0, 10);
    for (u64 p = lo | 1; p <= hi; p += 2) {
      if (p % 4 != 1 || !is_prime(p)) continue;
      long R, Su, SC, SB; rcount(p, &R, &Su, &SC, &SB);
      long S1 = s1count(p, 0);
      printf("%llu %ld %ld %ld %ld %ld\n", p, R, Su, SC, S1, SB);
    }
  } else if (!strcmp(argv[1], "list")) {
    FILE *F = fopen(argv[2], "r"); char line[256];
    if (!F) { perror(argv[2]); return 1; }
    while (fgets(line, sizeof line, F)) {
      if (line[0] == '#' || line[0] == '\n') continue;
      u64 n = strtoull(line, 0, 10); if (!n) continue;
      long R, Su, SC, SB; rcount(n, &R, &Su, &SC, &SB);
      long S1 = s1count(n, 0);
      printf("%llu %ld %ld %ld %ld %ld\n", n, R, Su, SC, S1, SB);
    }
  } else if (!strcmp(argv[1], "s1zeros")) {
    u64 lo = strtoull(argv[2], 0, 10), hi = strtoull(argv[3], 0, 10);
    for (u64 p = lo | 1; p <= hi; p += 2) {
      if (p % 4 != 1 || !is_prime(p)) continue;
      if (s1count(p, 1) == 0) { printf("%llu\n", p); fflush(stdout); }
    }
  } else { fprintf(stderr, "%s", use); return 1; }
  return 0;
}
