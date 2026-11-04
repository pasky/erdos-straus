// z56 PRIMET1: exact (★) count at single odd n (prime p up to ~1e14):
//   R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n}   (and, with flag g, R*(n) = same with gcd(u,B) = 1).
// Decomposition by the smallest coordinate (ordered triples, u <-> B symmetric):
//   A1 = #{C <= u, C <= B}: for each C, divisor pairs d*e = 4Cn+1 with d = 4uC-1, e = 4BC-1, d,e ≡ -1 (4C), d,e >= 4C^2-1;
//   A2 = #{u < C, u <= B}:   for each u, divisors m | n+u, m = 4uC-1 ≡ -1 (4u), C > u, B = (n+u)/m >= u;
//   A3 = #{B < C, B < u} = #{u < C, u < B} (swap u,B): same loop with B > u.
// R = A1 + A2 + A3. The numbers n+u (u <= S) and 4Cn+1 (C <= S) are factored by a sieve over primes <= 65536 plus
// Miller-Rabin / Pollard-rho on the cofactor.
// Usage: echo n1 n2 ... | z56_primet1_rone [g]     output: "n R A1 A2 A3"
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulm(u64 a, u64 b, u64 m) { return (u128)a * b % m; }
static u64 powm(u64 b, u64 e, u64 m) { u64 r = 1; b %= m; while (e) { if (e & 1) r = mulm(r, b, m); b = mulm(b, b, m); e >>= 1; } return r; }
static int isprime(u64 n) {
  if (n < 2) return 0;
  static const u64 sp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
  for (int i = 0; i < 12; i++) { if (n % sp[i] == 0) return n == sp[i]; }
  u64 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
  for (int i = 0; i < 12; i++) {
    u64 x = powm(sp[i], d, n); if (x == 1 || x == n - 1) continue;
    int ok = 0; for (int r = 1; r < s; r++) { x = mulm(x, x, n); if (x == n - 1) { ok = 1; break; } }
    if (!ok) return 0;
  }
  return 1;
}
static u64 gcdu(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static u64 rho(u64 n) {
  if (n % 2 == 0) return 2;
  for (u64 c = 1;; c++) {
    u64 y = 2, x, g = 1, q = 1, ys = 2; u64 r = 1, m = 128;
    do { x = y; for (u64 i = 0; i < r; i++) y = (mulm(y, y, n) + c) % n;
      u64 k = 0;
      do { ys = y; for (u64 i = 0; i < m && i < r - k; i++) { y = (mulm(y, y, n) + c) % n; q = mulm(q, x > y ? x - y : y - x, n); }
        g = gcdu(q, n); k += m; } while (k < r && g == 1);
      r <<= 1; } while (g == 1);
    if (g == n) { do { ys = (mulm(ys, ys, n) + c) % n; g = gcdu(x > ys ? x - ys : ys - x, n); } while (g == 1); }
    if (g != n) return g;
  }
}
#define MAXF 64
typedef struct { int k; u64 p[MAXF]; int e[MAXF]; } fac_t;
static void addf(fac_t *f, u64 q) { for (int i = 0; i < f->k; i++) if (f->p[i] == q) { f->e[i]++; return; } f->p[f->k] = q; f->e[f->k] = 1; f->k++; }
static void factor_big(fac_t *f, u64 n) { // n has no prime factor <= 65536
  if (n == 1) return;
  if (isprime(n)) { addf(f, n); return; }
  u64 d = rho(n); factor_big(f, d); factor_big(f, n / d);
}
static int NP; static u64 PR[7000];
static u64 *divs; static size_t divcap;
static size_t gen_divs(fac_t *f) {
  size_t cnt = 1; divs[0] = 1;
  for (int i = 0; i < f->k; i++) {
    size_t cur = cnt; u64 pw = 1;
    for (int e = 1; e <= f->e[i]; e++) {
      pw *= f->p[i];
      if (cnt + cur > divcap) { divcap = 2 * (cnt + cur); divs = realloc(divs, divcap * sizeof(u64)); }
      for (size_t j = 0; j < cur; j++) divs[cnt++] = divs[j] * pw;
    }
  }
  return cnt;
}
static u64 inv_mod(u64 a, u64 m) { // m prime
  return powm(a % m, m - 2, m);
}
int main(int argc, char **argv) {
  int gflag = argc > 1 && argv[1][0] == 'g';
  // primes <= 65536
  { char *s = calloc(65537, 1); for (int i = 2; i <= 65536; i++) if (!s[i]) { PR[NP++] = i; for (int j = 2 * i; j <= 65536; j += i) s[j] = 1; } free(s); }
  divcap = 1 << 16; divs = malloc(divcap * sizeof(u64));
  u64 n;
  while (scanf("%llu", &n) == 1) {
    u64 S = 1; while (4 * (S + 1) * (S + 1) * (S + 1) <= n + 4 * (S + 1)) S++;
    S += 2;
    fac_t *F1 = calloc(S + 1, sizeof(fac_t)), *F2 = calloc(S + 1, sizeof(fac_t));
    u64 *c1 = malloc((S + 1) * sizeof(u64)), *c2 = malloc((S + 1) * sizeof(u64));
    for (u64 i = 1; i <= S; i++) { c1[i] = 4 * i * n + 1; c2[i] = n + i; }
    for (int t = 0; t < NP; t++) {
      u64 q = PR[t];
      // 4Cn+1 ≡ 0 (q): q odd, q ∤ n:  C ≡ -(4n)^{-1}
      if (q != 2 && n % q) {
        u64 c0 = (q - inv_mod(4 * (n % q) % q, q)) % q; if (c0 == 0) c0 = q;
        for (u64 C = c0; C <= S; C += q) { while (c1[C] % q == 0) { c1[C] /= q; addf(&F1[C], q); } }
      }
      // n+u ≡ 0 (q): u ≡ -n
      { u64 u0 = (q - n % q) % q; if (u0 == 0) u0 = q;
        for (u64 u = u0; u <= S; u += q) { while (c2[u] % q == 0) { c2[u] /= q; addf(&F2[u], q); } } }
    }
    u64 A1 = 0, A2 = 0, A3 = 0;
    for (u64 C = 1; C <= S && 4 * C * C * C <= n + 2 * C; C++) {
      factor_big(&F1[C], c1[C]);
      u64 N = 4 * C * n + 1, mod = 4 * C, lo = 4 * C * C - 1;
      size_t nd = gen_divs(&F1[C]);
      for (size_t j = 0; j < nd; j++) { u64 d = divs[j]; if (d % mod != mod - 1 || d < lo) continue; u64 e = N / d; if (e < lo) continue;
        if (gflag) { u64 u = (d + 1) / mod, B = (e + 1) / mod; if (gcdu(u, B) != 1) continue; }
        A1++; }
    }
    for (u64 u = 1; u <= S && 4 * u * u * (u + 1) <= n + 2 * u; u++) {
      factor_big(&F2[u], c2[u]);
      u64 N = n + u, mod = 4 * u, lo = 4 * u * u - 1;
      size_t nd = gen_divs(&F2[u]);
      for (size_t j = 0; j < nd; j++) { u64 m = divs[j]; if (m % mod != mod - 1 || m <= lo) continue; u64 B = N / m; if (B < u) continue;
        if (gflag && gcdu(u, B) != 1) continue;
        A2++; if (B > u) A3++; }
    }
    printf("%llu %llu %llu %llu %llu\n", n, A1 + A2 + A3, A1, A2, A3); fflush(stdout);
    free(F1); free(F2); free(c1); free(c2);
  }
  return 0;
}
