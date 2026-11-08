/* z64 SDEEP KS0: exact decision of conjecture (S) at individual n (n == 1 mod 4, n < 9e13).
   A word of n: n + u = d*v with d = tu-1 == -1 (mod u), d >= 2u-1, v >= u (one per reversal pair), 2u(u-1) <= n.
   Sign = Jacobi (d/n).  (S)(n) holds iff some word has sign -1.
   Modes (per input line "n tag"):
     E  early exit: scan u = 2,3,... (factoring n+u by trial division to 2^16 + Pollard rho) up to u <= UE;
        if no -1 word found, fall back to the full segmented-sieve enumeration (mode F).
     F  full: enumerate every word (segmented sieve of n+u, u <= sqrt(n/2), primes <= 1e7) and count.
   Output: n tag mode has_word Npairs Nneg_pairs min_u_neg first_u_word
   gcc -O2 -o /tmp/z64d scripts/z64_sdeep_decide.c -lm ;  echo "n tag" lines | /tmp/z64d E|F  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned __int128 u128;
typedef uint64_t u64;
static u64 mulmod(u64 a, u64 b, u64 m) { return (u64)((u128)a * b % m); }
static u64 powmod(u64 a, u64 e, u64 m) { u64 r = 1; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; } return r; }
static int isprime(u64 n) {
  if (n < 2) return 0;
  static const u64 sp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
  for (int i = 0; i < 12; i++) { if (n % sp[i] == 0) return n == sp[i]; }
  u64 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
  static const u64 B[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};
  for (int i = 0; i < 7; i++) {
    u64 a = B[i] % n; if (!a) continue;
    u64 x = powmod(a, d, n); if (x == 1 || x == n - 1) continue;
    int ok = 0; for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } }
    if (!ok) return 0;
  }
  return 1;
}
static u64 gcdu(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static u64 rho(u64 n) {
  if (n % 2 == 0) return 2;
  for (u64 c = 1;; c++) {
    u64 x = 2, y = 2, d = 1, q = 1, ys = 2; u64 r = 1;
    do {
      x = y;
      for (u64 i = 0; i < r; i++) y = (mulmod(y, y, n) + c) % n;
      u64 k = 0;
      do {
        ys = y;
        for (u64 i = 0; i < 128 && i < r - k; i++) { y = (mulmod(y, y, n) + c) % n; q = mulmod(q, x > y ? x - y : y - x, n); }
        d = gcdu(q, n); k += 128;
      } while (k < r && d == 1);
      r *= 2;
    } while (d == 1);
    if (d == n) { do { ys = (mulmod(ys, ys, n) + c) % n; d = gcdu(x > ys ? x - ys : ys - x, n); } while (d == 1); }
    if (d != n) return d;
  }
}
static u64 fp[64]; static int fe[64]; static int nf;
static void addf(u64 p) { for (int i = 0; i < nf; i++) if (fp[i] == p) { fe[i]++; return; } fp[nf] = p; fe[nf++] = 1; }
static void factrec(u64 n) { if (n == 1) return; if (isprime(n)) { addf(n); return; } u64 d = rho(n); factrec(d); factrec(n / d); }
static void factor(u64 n) {
  nf = 0;
  for (u64 p = 2; p < 65536 && p * p <= n; p += (p == 2 ? 1 : 2)) { while (n % p == 0) { addf(p); n /= p; } }
  if (n > 1) factrec(n);
}
static int jac(u64 a, u64 n) {
  int s = 1; a %= n;
  while (a) {
    while (!(a & 1)) { a >>= 1; u64 r = n & 7; if (r == 3 || r == 5) s = -s; }
    u64 t = a; a = n; n = t;
    if ((a & 3) == 3 && (n & 3) == 3) s = -s;
    a %= n;
  }
  return n == 1 ? s : 0;
}
static u64 divs[1 << 16];
static int gendivs(void) {
  int k = 1; divs[0] = 1;
  for (int i = 0; i < nf; i++) { int k0 = k; u64 pw = 1; for (int j = 1; j <= fe[i]; j++) { pw *= fp[i]; for (int a = 0; a < k0; a++) divs[k++] = divs[a] * pw; } }
  return k;
}
/* process one u given factorisation of n+u in fp/fe; update counters; return 1 if a -1 word found */
static long Npairs, Nneg; static u64 minuneg, firstu;
static int process_u(u64 n, u64 u) {
  u64 m = n + u; int k = gendivs(); int found = 0;
  for (int i = 0; i < k; i++) {
    u64 d = divs[i];
    if (d < 2 * u - 1 || (d + 1) % u) continue;
    u64 v = m / d; if (v < u) continue;
    u64 t = (d + 1) / u;
    if ((u128)t * u * v - u - v != n) { fprintf(stderr, "BUG n=%lu u=%lu\n", n, u); exit(1); }
    Npairs++; if (!firstu) firstu = u;
    if (jac(d, n) == -1) { Nneg++; if (!minuneg) minuneg = u; found = 1; }
  }
  return found;
}
static uint32_t *primes; static long np;
#define BLK (1 << 18)
static u64 rem_[BLK]; static uint32_t fl[BLK][16]; static uint8_t fc[BLK];
static void full(u64 n, int stop_at_neg) {
  u64 U = 2; while (2 * (U + 1) * U <= n) U++;  /* max u */
  for (u64 lo = 2; lo <= U; lo += BLK) {
    u64 hi = lo + BLK; if (hi > U + 1) hi = U + 1; long B = hi - lo;
    for (long i = 0; i < B; i++) { rem_[i] = n + lo + i; fc[i] = 0; }
    u64 top = (u64)sqrt((double)(n + hi)) + 2;
    for (long j = 0; j < np && primes[j] <= top; j++) {
      u64 q = primes[j]; u64 o = (q - (n + lo) % q) % q;
      for (u64 i = o; i < (u64)B; i += q) { fl[i][fc[i]++] = q; do rem_[i] /= q; while (rem_[i] % q == 0); }
    }
    for (long i = 0; i < B; i++) {
      u64 m = n + lo + i; nf = 0;
      for (int a = 0; a < fc[i]; a++) { u64 q = fl[i][a]; int e = 0; while (m % q == 0) { m /= q; e++; } fp[nf] = q; fe[nf++] = e; }
      if (m > 1) { fp[nf] = m; fe[nf++] = 1; }
      if (process_u(n, lo + i) && stop_at_neg) return;
    }
  }
}
int main(int argc, char **argv) {
  char mode = argv[1][0]; u64 UE = argc > 2 ? strtoull(argv[2], 0, 10) : 3000;
  long PL = 10000000; char *comp = calloc(PL + 1, 1); primes = malloc(sizeof(uint32_t) * 700000); np = 0;
  for (long i = 2; i <= PL; i++) if (!comp[i]) { primes[np++] = i; for (long j = i * i; j <= PL; j += i) comp[j] = 1; }
  free(comp);
  char line[256];
  while (fgets(line, sizeof line, stdin)) {
    u64 n; char tag[128] = "-";
    if (sscanf(line, "%lu %127s", &n, tag) < 1) continue;
    if (n % 4 != 1 || n > 90000000000000ULL) { printf("%lu %s SKIP\n", n, tag); continue; }
    Npairs = Nneg = 0; minuneg = firstu = 0; char used = mode;
    if (mode == 'E') {
      int got = 0;
      for (u64 u = 2; u <= UE && 2 * u * (u - 1) <= n; u++) { factor(n + u); if (process_u(n, u)) { got = 1; break; } }
      if (!got) { used = 'F'; Npairs = Nneg = 0; minuneg = firstu = 0; full(n, 0); }
    } else full(n, 0);
    printf("%lu %s %c %d %ld %ld %lu %lu\n", n, tag, used, Npairs > 0, Npairs, Nneg, minuneg, firstu);
    fflush(stdout);
  }
  return 0;
}
