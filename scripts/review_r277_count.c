/* R277 from-scratch engine (independent of z30_rgen.c).
   For odd n in a list: enumerate coprime (u,B), u+B odd, 4uB-u-B <= n, and compute
     R    = #{4uB | n+u+B}
     M0   = sum 1/phi(q)                       (only if flag m0=1; all coprime opposite-parity pairs)
     M2   = sum 4/phi(q) * 1[n = a mod 8]
     Mgen = sum s(q)/phi(q) * 1[n a in squares mod q]
     MQ   = sum 1[n = a mod g] 1[n a in sq mod q] * s(q) phi(g) / (s(g) phi(q)),  g = gcd(q, Q), Q = 720720
   q = 4uB, a = -(u+B).  Usage: review_r277_count NMAX m0flag < list_of_n
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

static int *spf; static int64_t *phiv;
static int64_t QQ = 720720; /* 2^4 3^2 5 7 11 13; optional argv[3] overrides */

static int jacobi(int64_t a, int64_t m) { /* m odd > 0 */
  a %= m; if (a < 0) a += m; int t = 1;
  while (a) {
    while (!(a & 1)) { a >>= 1; int64_t r = m & 7; if (r == 3 || r == 5) t = -t; }
    int64_t tmp = a; a = m; m = tmp;
    if ((a & 3) == 3 && (m & 3) == 3) t = -t;
    a %= m;
  }
  return m == 1 ? t : 0;
}
static int64_t gcdl(int64_t a, int64_t b) { while (b) { int64_t t = a % b; a = b; b = t; } return a; }
static int64_t phi_big(int64_t x) { /* x small enough to factor by trial (only used for g | Q) */
  int64_t r = x; for (int64_t l = 2; l * l <= x; l++) if (x % l == 0) { r = r / l * (l - 1); while (x % l == 0) x /= l; }
  if (x > 1) r = r / x * (x - 1); return r; }
static int s_of(int64_t g) { /* |G/G^2| for (Z/g)^x */
  int s = 1; int k = 0; while (!(g & 1)) { g >>= 1; k++; }
  if (k == 2) s = 2; else if (k >= 3) s = 4;
  for (int64_t l = 3; l * l <= g; l += 2) if (g % l == 0) { s *= 2; while (g % l == 0) g /= l; }
  if (g > 1) s *= 2; return s; }

/* does n*a lie in squares at all odd primes of x?  (a = -(u+B)); also returns omega_odd */
static int oddsq(int64_t n, int64_t x, int64_t a, int *om) {
  int ok = 1; *om = 0;
  while (x > 1) {
    int l = spf[x]; while (x % l == 0) x /= l;
    if (l == 2) continue;
    (*om)++;
    int64_t v = ((n % l) * (((a % l) + l) % l)) % l;
    if (jacobi(v, l) != 1) ok = 0;
  }
  return ok;
}

int main(int argc, char **argv) {
  int NMAX = atoi(argv[1]); int m0 = atoi(argv[2]); if (argc > 3) QQ = atol(argv[3]);
  spf = calloc(NMAX + 2, sizeof(int)); phiv = calloc(NMAX + 2, sizeof(int64_t));
  for (int i = 2; i <= NMAX; i++) if (!spf[i]) for (int j = i; j <= NMAX; j += i) if (!spf[j]) spf[j] = i;
  phiv[1] = 1;
  for (int i = 2; i <= NMAX; i++) { int l = spf[i], m = i / l; phiv[i] = (m % l == 0) ? phiv[m] * l : phiv[m] * (l - 1); }
  int64_t n;
  while (scanf("%ld", &n) == 1) {
    long R = 0; double M0 = 0, M2 = 0, Mg = 0, MQ = 0;
    for (int64_t u = 1; 3 * u - 1 <= n; u++) {
      int64_t Bmax = (n + u) / (4 * u - 1);
      int64_t b0 = 1;
      if (m0) {
        for (int64_t B = 1; B <= Bmax; B++) {
          if (!((u + B) & 1)) continue;
          if (gcdl(u, B) != 1) continue;
          M0 += 1.0 / (4.0 * phiv[u] * phiv[B]);
        }
      }
      /* B = -(n+u) mod 8 */
      int64_t r = ((-(n + u)) % 8 + 8) % 8; b0 = r ? r : 8;
      for (int64_t B = b0; B <= Bmax; B += 8) {
        if (gcdl(u, B) != 1) continue;  /* u+B odd automatic: n odd, n+u+B = 0 mod 8 */
        int64_t q = 4 * u * B, a = -(u + B);
        double ph = 4.0 * phiv[u] * phiv[B];
        M2 += 4.0 / ph;
        if (n % q == ((a % q) + q) % q) R++;
        int o1, o2;
        int ok = oddsq(n, u, a, &o1); ok &= oddsq(n, B, a, &o2);
        if (!ok) continue;
        int s = 4 << (o1 + o2);
        Mg += s / ph;
        int64_t g = gcdl(q, QQ);
        if (((n - a) % g + g) % g == 0) MQ += (double)s * phi_big(g) / ((double)s_of(g) * ph);
      }
    }
    printf("%ld %ld %.6f %.6f %.6f %.6f\n", n, R, M0, M2, Mg, MQ);
    fflush(stdout);
  }
  return 0;
}
