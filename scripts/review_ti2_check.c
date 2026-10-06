/* R69 from-scratch checker for certificates at the sign point
 *   xhat = (w at 2; -1 at r; +1 at every other prime).
 * A certificate (c,k,F) with v_r(c) odd holds at xhat iff
 *   F | N := 1+4ck^2   and   F == -xhat (mod h), h = 4ck.
 * Since N == 1 (mod h), the cofactor N/F == -xhat^{-1} (mod h).
 * min(F,N/F) <= sqrt(N) < h, so it suffices to test the least positive
 * residues  A = -xhat mod h  and  B = -xhat^{-1} mod h  (each a single
 * candidate) for A^2<=N, A|N  resp.  B^2<=N, B|N.
 * Independent of the author's code: xhat mod h is built by explicit CRT
 * with extended Euclid; 2-adic inverse by Hensel/Newton.
 * usage: review_ti2_check r w X [cmin cmax]   (prints certificates found)
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef __int128 i128;
typedef uint64_t u64; typedef int64_t i64;

static i128 egcd_inv(i128 a, i128 m) { /* inverse of a mod m, m>=1 */
  if (m == 1) return 0;
  i128 g = m, x = 0, g1 = ((a % m) + m) % m, x1 = 1;
  while (g1) { i128 q = g / g1, t = g - q * g1; g = g1; g1 = t; t = x - q * x1; x = x1; x1 = t; }
  if (g != 1) { fprintf(stderr, "noninvertible\n"); exit(2); }
  return ((x % m) + m) % m;
}
/* x == a1 mod m1, x == a2 mod m2 (coprime) */
static i128 crt(i128 a1, i128 m1, i128 a2, i128 m2) {
  i128 t = ((a2 - a1) % m2 + m2) % m2;
  t = (t * egcd_inv(m1 % m2, m2)) % m2;
  return a1 + m1 * t;
}
static u128 isqrt128(u128 n) { u128 x = (u128)__builtin_sqrtl((long double)n); while (x * x > n) x--; while ((x + 1) * (x + 1) <= n) x++; return x; }

int main(int argc, char **argv) {
  if (argc < 4) return 1;
  i64 r = atoll(argv[1]); i64 w = atoll(argv[2]); u64 X = strtoull(argv[3], 0, 10);
  u64 slices = 0, certs = 0;
  for (u64 c = r; c <= X; c += r) {
    u64 cc = c; int a = 0; while (cc % r == 0) { cc /= r; a++; }
    if (!(a & 1)) continue;
    for (u64 k = 1; c * k <= X; k++) {
      slices++;
      u64 h = 4 * c * k;
      /* split h = 2^t * r^v * m */
      u64 m = h; int t = 0; while (!(m & 1)) { m >>= 1; t++; }
      u64 rv = 1; while (m % r == 0) { m /= r; rv *= r; }
      u64 two = (u64)1 << t;
      i128 wmod = ((i128)w % two + two) % two;           /* w is odd */
      i128 winv = egcd_inv(wmod, two);
      /* xhat mod h and xhat^{-1} mod h */
      i128 x1 = crt(crt(wmod, two, rv - 1, rv), (i128)two * rv, 1 % m, m);
      i128 x2 = crt(crt(winv, two, rv - 1, rv), (i128)two * rv, 1 % m, m);
      i128 H = h;
      u128 A = (u128)((H - x1 % H) % H), B = (u128)((H - x2 % H) % H);
      u128 N = (u128)1 + (u128)4 * c * (u128)k * k;
      u128 sq = isqrt128(N);
      u128 cand[2] = {A, B};
      for (int i = 0; i < 2; i++) {
        u128 D = cand[i];
        if (D == 0 || D > sq) continue;
        if (i == 1 && D * D == N) continue; /* square: already counted */
        if (N % D == 0) {
          u128 F = (i == 0) ? D : N / D;
          certs++;
          printf("CERT c=%llu k=%llu F=%llu ck=%llu\n", (unsigned long long)c, (unsigned long long)k,
                 (unsigned long long)F, (unsigned long long)(c * k));
        }
      }
    }
  }
  printf("r=%lld w=%lld X=%llu slices=%llu certs=%llu\n", (long long)r, (long long)w,
         (unsigned long long)X, (unsigned long long)slices, (unsigned long long)certs);
  return 0;
}
