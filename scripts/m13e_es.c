/* m13e_es.c — all ordered solutions x<=y<=z of 4/N = 1/x+1/y+1/z, N up to ~1e11 (POINTWISE_MORDELL13E §1).
 * usage: m13e_es N [xlo xhi]   (x range (N/4,3N/4] by default; xlo..xhi inclusive, clipped to it)
 * prints "x y" lines (z = 1/(4/N-1/x-1/y) is recomputed exactly by the reader, m13e_inv.py); "# N=.. xlo=.. xhi=.. count=.." on stdout at the end (completion marker).
 * Same method as m13b_es.c (validated): r/s = (4x-N)/(Nx) reduced; y=(D+s)/r, z=(s^2/D+s)/r for divisors
 * D<=s of s^2 with D = -s (mod r) and y>=x.  Differences: segmented sieve (factorisation of x in blocks,
 * sieving primes <= sqrt(xhi)), 128-bit s and D, and the congruence D = -s (mod r) solved by meet-in-the-middle
 * over a split of the primes of s (residues tracked multiplicatively, hash table with a bitmap prefilter;
 * brute force when n1*n2 <= 64).
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;

static u64 gcdu(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static void pr128(u128 v, char *buf) { char t[64]; int i = 63; t[i] = 0; if (!v) t[--i] = '0'; while (v) { t[--i] = '0' + (int)(v % 10); v /= 10; } strcpy(buf, t + i); }

#define BL (1 << 16)
#define MAXF 16
static uint32_t fp[BL][MAXF]; static uint8_t fe[BL][MAXF], fn[BL]; static u64 rem_[BL];
static u64 P[40]; static int E[40]; static int np;
#define DMAX (1 << 22)
static u128 dv[DMAX], ev[DMAX]; static u64 dr[DMAX], er[DMAX];
typedef struct { u64 res; uint32_t st, idx; } HE; static HE ht[1 << 24]; static u64 bm[64]; static uint32_t stamp; static double S1, S2, S3, SX;
static double rinv; /* 1.0/r of the current x; mulmod valid for a, b < m < 2^50 (q off by at most 1) */
static inline u64 mulmod(u64 a, u64 b, u64 m) {
    u64 q = (u64)((double)a * (double)b * rinv); long long t = (long long)(a * b - q * m);
    while (t < 0) t += (long long)m; while (t >= (long long)m) t -= (long long)m; return (u64)t; }
static u64 invmod(u64 a, u64 m) { /* a invertible mod m */
    if (m == 1) return 0; long long t = 0, nt = 1; u64 rr = m, nr = a;
    while (nr) { u64 q = rr / nr; long long tt = t - (long long)q * nt; t = nt; nt = tt; u64 r2 = rr - q * nr; rr = nr; nr = r2; }
    if (rr != 1) { fprintf(stderr, "invmod fail\n"); exit(1); } return (u64)(t < 0 ? t + (long long)m : t); }

int main(int argc, char **argv) {
    u64 N = strtoull(argv[1], 0, 10);
    u64 xlo = N / 4 + 1, xhi = 3 * N / 4;
    if (argc > 3) { u64 a = strtoull(argv[2], 0, 10), b = strtoull(argv[3], 0, 10); if (a > xlo) xlo = a; if (b < xhi) xhi = b; }
    /* factor N */
    u64 NP[16]; int NE[16], nn = 0;
    { u64 m = N; for (u64 p = 2; p * p <= m; p++) { int e = 0; while (m % p == 0) { m /= p; e++; } if (e) { NP[nn] = p; NE[nn++] = e; } } if (m > 1) { NP[nn] = m; NE[nn++] = 1; } }
    /* sieving primes */
    u64 sq = (u64)sqrtl((long double)xhi) + 2;
    char *comp = calloc(sq + 1, 1); uint32_t *pr = malloc(sizeof(uint32_t) * (sq + 1)); int npr = 0;
    for (u64 i = 2; i <= sq; i++) if (!comp[i]) { pr[npr++] = (uint32_t)i; for (u64 j = i * i; j <= sq; j += i) comp[j] = 1; }
    u64 count = 0; char b1[48], b2[48];
    for (u64 lo = xlo; lo <= xhi; lo += BL) {
        u64 hi = lo + BL - 1; if (hi > xhi) hi = xhi; u64 L = hi - lo + 1;
        for (u64 k = 0; k < L; k++) { rem_[k] = lo + k; fn[k] = 0; }
        for (int t = 0; t < npr; t++) {
            u64 p = pr[t]; if (p * p > hi) break;
            u64 st = (lo + p - 1) / p * p;
            for (u64 v = st; v <= hi; v += p) {
                u64 k = v - lo; int e = 0; while (rem_[k] % p == 0) { rem_[k] /= p; e++; }
                fp[k][fn[k]] = (uint32_t)p; fe[k][fn[k]++] = (uint8_t)e;
            }
        }
        for (u64 k = 0; k < L; k++) {
            u64 x = lo + k;
            u64 num = 4 * x - N; u64 g = gcdu(num, (u64)(((u128)(N % num) * (x % num)) % num));
            u64 r = num / g; u128 s = (u128)N * x / g; rinv = 1.0 / (double)r;
            if (r >= (1ull << 50)) { fprintf(stderr, "r too large\n"); return 1; }
            /* factorisation of s */
            np = 0;
            for (int i = 0; i < nn; i++) { P[np] = NP[i]; E[np++] = NE[i]; }
            for (int i = 0; i < fn[k]; i++) { u64 p = fp[k][i]; int j; for (j = 0; j < np; j++) if (P[j] == p) break; if (j == np) { P[np] = p; E[np++] = 0; } E[j] += fe[k][i]; }
            if (rem_[k] > 1) { u64 p = rem_[k]; int j; for (j = 0; j < np; j++) if (P[j] == p) break; if (j == np) { P[np] = p; E[np++] = 0; } E[j] += 1; }
            { u64 m = g; for (int i = 0; i < np && m > 1; i++) while (m % P[i] == 0) { m /= P[i]; E[i]--; } if (m != 1) { fprintf(stderr, "factor error x=%llu\n", x); return 1; } }
            /* meet in the middle: D = d1*d2 (d1 over primes of group 1, d2 over group 2), D | s^2, D <= s,
             * D = -s (mod r).  gcd(D, r) = 1 since gcd(r, s) = 1, so d2 is invertible mod r and the condition
             * reads d1 = -s * d2^{-1} (mod r): hash d1 residues, scan d2. */
            int grp[40]; u64 w1 = 1, w2 = 1;
            { int ord[40]; for (int i = 0; i < np; i++) ord[i] = i;
              for (int i = 0; i < np; i++) for (int j = i + 1; j < np; j++) if (E[ord[j]] > E[ord[i]]) { int t = ord[i]; ord[i] = ord[j]; ord[j] = t; }
              for (int ii = 0; ii < np; ii++) { int i = ord[ii]; if (!E[i]) { grp[i] = 0; continue; } if (w1 <= w2) { grp[i] = 1; w1 *= 2 * E[i] + 1; } else { grp[i] = 2; w2 *= 2 * E[i] + 1; } } }
            size_t n1 = 1; dv[0] = 1; dr[0] = 1 % r;
            for (int i = 0; i < np; i++) {
                if (grp[i] != 1) continue;
                size_t cur = n1; u64 pm = P[i] % r;
                for (size_t q = 0; q < cur; q++) {
                    u128 v = dv[q]; u64 vr = dr[q];
                    for (int e = 1; e <= 2 * E[i]; e++) {
                        v *= P[i]; if (v > s) break;
                        vr = mulmod(vr, pm, r);
                        if (n1 == DMAX) { fprintf(stderr, "divisor overflow x=%llu\n", x); return 1; }
                        dv[n1] = v; dr[n1++] = vr;
                    }
                }
            }
            u64 smr = (u64)(s % r); u64 need = (r - smr) % r;
            size_t n2 = 1; ev[0] = 1; er[0] = need;
            /* batch inversion of the group-2 primes mod r (one extended gcd) */
            u64 pinvs[40]; { int idx[40], k2 = 0; u64 pre[41]; pre[0] = 1 % r;
              for (int i = 0; i < np; i++) if (grp[i] == 2) { idx[k2] = i; pre[k2 + 1] = mulmod(pre[k2], P[i] % r, r); k2++; }
              u64 inv = k2 ? invmod(pre[k2], r) : 0;
              for (int t = k2 - 1; t >= 0; t--) { pinvs[idx[t]] = mulmod(inv, pre[t], r); inv = mulmod(inv, P[idx[t]] % r, r); } }
            for (int i = 0; i < np; i++) {
                if (grp[i] != 2) continue;
                size_t cur = n2; u64 pinv = pinvs[i];
                for (size_t q = 0; q < cur; q++) {
                    u128 v = ev[q]; u64 vr = er[q];
                    for (int e = 1; e <= 2 * E[i]; e++) {
                        v *= P[i]; if (v > s) break;
                        vr = mulmod(vr, pinv, r);
                        if (n2 == DMAX) { fprintf(stderr, "divisor overflow x=%llu\n", x); return 1; }
                        ev[n2] = v; er[n2++] = vr;
                    }
                }
            }
#ifdef STATS
            S1 += n1; S2 += n2; SX++; S3 += np;
#endif
            /* hash group-1 residues */
            if (n1 * n2 <= 64) {
                for (size_t q2 = 0; q2 < n2; q2++) for (size_t q = 0; q < n1; q++) if (dr[q] == er[q2]) {
                    if (dv[q] > s / ev[q2]) continue;
                    u128 D = dv[q] * ev[q2]; u128 y = (D + s) / r;
                    if (y < x) continue;
                    pr128(x, b1); pr128(y, b2); printf("%s %s\n", b1, b2);
                    count++;
                }
                continue;
            }
            unsigned hb = 4; while ((1u << hb) < 2 * n1) hb++; u64 hm = (1ull << hb) - 1; stamp++;
            memset(bm, 0, sizeof bm);
            for (size_t q = 0; q < n1; q++) { u64 hh = dr[q] * 0x9E3779B97F4A7C15ull; bm[hh >> 58] |= 1ull << ((hh >> 52) & 63); u64 h = hh >> (64 - hb); while (ht[h].st == stamp) h = (h + 1) & hm; ht[h].st = stamp; ht[h].idx = (uint32_t)q; ht[h].res = dr[q]; }
            for (size_t q2 = 0; q2 < n2; q2++) {
                u64 hh = er[q2] * 0x9E3779B97F4A7C15ull;
                if (!((bm[hh >> 58] >> ((hh >> 52) & 63)) & 1)) continue;   /* bitmap prefilter (no false negatives) */
                u64 h = hh >> (64 - hb);
                for (; ht[h].st == stamp; h = (h + 1) & hm) {
                    if (ht[h].res != er[q2]) continue;
                    size_t q = ht[h].idx;
                    if (dv[q] > s / ev[q2]) continue;
                    u128 D = dv[q] * ev[q2]; u128 y = (D + s) / r;
                    if (y < x) continue;
                    pr128(x, b1); pr128(y, b2); printf("%s %s\n", b1, b2);
                    count++;
                }
            }
        }
    }
#ifdef STATS
    fprintf(stderr, "avg n1 %.1f n2 %.1f np %.2f\n", S1 / SX, S2 / SX, S3/SX);
#endif
    printf("# N=%llu xlo=%llu xhi=%llu count=%llu\n", N, xlo, xhi, count);
    return 0;
}
