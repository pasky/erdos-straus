/* z52_bank_pencil.c — positive integer points on the pencil S_{n,k}: 4xyz - n(xy+yz+zx) = k.
 *
 * Complete method (for n >= 9 and k in {-4} or 1 <= k <= 319): order x <= y <= z; then n/4 < x <= floor(3n/4)+1 (Z52_BANKED.md §1(a)).
 * For fixed x put m = 4x - n >= 1; the equation is (m y - n x)(m z - n x) = N_x := (n x)^2 + k m.
 * So every solution comes from a factorisation N_x = D D' (D, D' of either common sign) with D, D' == -n x (mod m),
 * y = (D + n x)/m, z = (D' + n x)/m.  We enumerate ALL x in the range and ALL divisors D (both signs), keeping y,z >= 1
 * (not forcing y >= x, so solutions may be found more than once in "count" mode we divide by symmetry instead:
 * count mode counts ordered pairs (y,z) with x = min and y,z >= x, i.e. unordered-x-minimal triples with y <= z).
 *
 * usage: z52_bank_pencil MODE k nlo nhi [mod res]
 *   MODE = first : for each n print n and first solution found, or "n FAIL" after the complete range
 *   MODE = count : print n and #{(x,y,z): x<=y<=z} (complete)
 * Only n with n % mod == res are processed (default mod=1).
 */
#include "z52_bank_fac.h"
#include <string.h>

static u128 dbuf[1 << 20];

static int verify(i128 n, i128 k, i128 x, i128 y, i128 z) {
  return 4 * x * y * z - n * (x * y + y * z + z * x) == k;
}

/* returns number of solutions with x fixed, y<=z, y>=x (count mode) or 1/0 for first */
static long solve_x(long n, long k, long x, int mode, long *oy, long *oz) {
  i128 m = 4 * (i128)x - n;
  if (m <= 0) return 0;
  i128 nx = (i128)n * x;
  i128 N = nx * nx + (i128)k * m;
  if (N == 0) return 0; /* not reached for |k| small, n>=9 */
  u128 aN = N > 0 ? (u128)N : (u128)(-N);
  fac_t F; factor128(aN, &F);
  int nd = divisors128(&F, dbuf, 1 << 20);
  if (nd < 0) { fprintf(stderr, "too many divisors n=%ld x=%ld\n", n, x); exit(3); }
  long cnt = 0;
  i128 r = ((-nx) % m + m) % m;
  for (int i = 0; i < nd; i++) {
    for (int sg = -1; sg <= 1; sg += 2) {
      i128 D = sg * (i128)dbuf[i];
      i128 Dp = N / D; /* exact */
      if (((D % m) + m) % m != r) continue;
      if (((Dp % m) + m) % m != r) continue;
      i128 y = (D + nx) / m, z = (Dp + nx) / m;
      if (y < 1 || z < 1) continue;
      if (!verify(n, k, x, y, z)) { fprintf(stderr, "VERIFY FAIL n=%ld k=%ld\n", n, k); exit(4); }
      if (mode == 0) { *oy = (long)y; *oz = (long)z; return 1; }
      if (y >= x && z >= y) cnt++;
    }
  }
  return cnt;
}

int main(int argc, char **argv) {
  if (argc < 5) { fprintf(stderr, "usage\n"); return 1; }
  int mode = strcmp(argv[1], "first") == 0 ? 0 : 1;
  long k = atol(argv[2]), nlo = atol(argv[3]), nhi = atol(argv[4]);
  long mod = argc > 6 ? atol(argv[5]) : 1, res = argc > 6 ? atol(argv[6]) : 0;
  if (nlo < 9) { fprintf(stderr, "need n>=9 for the bounds\n"); return 1; }
  for (long n = nlo; n <= nhi; n++) {
    if (n % mod != res) continue;
    long xlo = n / 4 + 1, xhi = (3 * n) / 4 + 1; /* generous: x <= 3n/4 (+1 slack, harmless) */
    if (mode == 0) {
      long y = 0, z = 0, found = 0;
      for (long x = xlo; x <= xhi && !found; x++) if (solve_x(n, k, x, 0, &y, &z)) { printf("%ld %ld %ld %ld\n", n, x, y, z); found = 1; }
      if (!found) printf("%ld FAIL\n", n);
    } else {
      long c = 0, y, z;
      for (long x = xlo; x <= xhi; x++) c += solve_x(n, k, x, 1, &y, &z);
      printf("%ld %ld\n", n, c);
    }
    fflush(stdout);
  }
  return 0;
}
