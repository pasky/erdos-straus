/* z52_bank_fac.h — factorisation of integers < 2^126 (practically < 2^70) for the z52 bank scripts.
 * Trial division by small primes, deterministic Miller–Rabin (first 13 prime bases: exact below 3.3e24),
 * Pollard–Brent rho. mulmod for moduli >= 2^64 uses a 60-bit split (needs modulus < 2^67).
 */
#ifndef Z52_BANK_FAC_H
#define Z52_BANK_FAC_H
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
typedef unsigned __int128 u128;
typedef __int128 i128;
typedef uint64_t u64;

static inline u128 mulmod128(u128 a, u128 b, u128 m) {
  if (m >> 64 == 0) { return (u128)((u64)a) * (u64)b % m; }
  /* m < 2^67, a,b < m */
  if (m >> 67) { fprintf(stderr, "mulmod128: modulus too large\n"); exit(2); }
  const u128 mask = (((u128)1) << 60) - 1;
  u128 hi = (a * (b >> 60)) % m;       /* a < 2^67, b>>60 < 2^7 */
  u128 r = (hi << 60) + a * (b & mask); /* < 2^127 + 2^127 */
  return r % m;
}
static inline u128 powmod128(u128 a, u128 e, u128 m) {
  u128 r = 1 % m; a %= m;
  while (e) { if (e & 1) r = mulmod128(r, a, m); a = mulmod128(a, a, m); e >>= 1; }
  return r;
}
static int isprime128(u128 n) {
  static const u64 sp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41};
  if (n < 2) return 0;
  for (int i = 0; i < 13; i++) { if (n == sp[i]) return 1; if (n % sp[i] == 0) return 0; }
  u128 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
  for (int i = 0; i < 13; i++) {
    u128 x = powmod128(sp[i], d, n);
    if (x == 1 || x == n - 1) continue;
    int ok = 0;
    for (int r = 1; r < s; r++) { x = mulmod128(x, x, n); if (x == n - 1) { ok = 1; break; } }
    if (!ok) return 0;
  }
  return 1;
}
static u128 gcd128(u128 a, u128 b) { while (b) { u128 t = a % b; a = b; b = t; } return a; }
static u128 rho128(u128 n) {
  if (!(n & 1)) return 2;
  for (u128 c = 1;; c++) {
    u128 y = 2, x, g = 1, q = 1, ys = 2; u64 r = 1, m = 128;
    do {
      x = y;
      for (u64 i = 0; i < r; i++) y = (mulmod128(y, y, n) + c) % n;
      u64 k = 0;
      do {
        ys = y;
        for (u64 i = 0; i < m && i < r - k; i++) {
          y = (mulmod128(y, y, n) + c) % n;
          q = mulmod128(q, x > y ? x - y : y - x, n);
        }
        g = gcd128(q, n); k += m;
      } while (k < r && g == 1);
      r <<= 1;
    } while (g == 1);
    if (g == n) {
      do { ys = (mulmod128(ys, ys, n) + c) % n; g = gcd128(x > ys ? x - ys : ys - x, n); } while (g == 1);
    }
    if (g != n) return g;
  }
}
#define MAXPF 40
typedef struct { int nf; u128 p[MAXPF]; int e[MAXPF]; } fac_t;
static void fac_add(fac_t *F, u128 p, int e) {
  for (int i = 0; i < F->nf; i++) if (F->p[i] == p) { F->e[i] += e; return; }
  if (F->nf >= MAXPF) { fprintf(stderr, "MAXPF\n"); exit(2); }
  F->p[F->nf] = p; F->e[F->nf] = e; F->nf++;
}
static void fac_rec(fac_t *F, u128 n) {
  if (n == 1) return;
  if (isprime128(n)) { fac_add(F, n, 1); return; }
  u128 d = rho128(n);
  fac_rec(F, d); fac_rec(F, n / d);
}
static void factor128(u128 n, fac_t *F) {
  F->nf = 0;
  if (n <= 1) return;
  static const u64 tp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
  for (int i = 0; i < 25; i++) { int e = 0; while (n % tp[i] == 0) { n /= tp[i]; e++; } if (e) fac_add(F, tp[i], e); }
  fac_rec(F, n);
}
/* enumerate all positive divisors into buf (returns count, -1 if > cap) */
static int divisors128(const fac_t *F, u128 *buf, int cap) {
  int nd = 1; buf[0] = 1;
  for (int i = 0; i < F->nf; i++) {
    int cur = nd; u128 v = 1;
    for (int e = 1; e <= F->e[i]; e++) {
      v *= F->p[i];
      for (int j = 0; j < cur; j++) { if (nd >= cap) return -1; buf[nd++] = buf[j] * v; }
    }
  }
  return nd;
}
#endif
