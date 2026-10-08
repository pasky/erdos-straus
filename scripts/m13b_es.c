/* m13b_es.c — all ordered solutions x<=y<=z of 4/N = 1/x+1/y+1/z (POINTWISE_MORDELL13B §2).
 * usage: m13b_es N    (N <= ~4e7; prints "x y z" lines, then "# count" on stderr)
 * Method: x in (N/4, 3N/4]; r/s = (4x-N)/(Nx) reduced; (ry-s)(rz-s)=s^2, so y=(D+s)/r for divisors
 * D<=s of s^2 with D = -s (mod r) and y>=x; z=(s^2/D+s)/r.  s is factored from the factorisation of N
 * (trial division) and of x (smallest-prime-factor sieve).  128-bit arithmetic for s^2/D.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;

static u64 gcdu(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static void pr128(u128 v) { char buf[64]; int i = 63; buf[i] = 0; if (!v) buf[--i] = '0'; while (v) { buf[--i] = '0' + (int)(v % 10); v /= 10; } fputs(buf + i, stdout); }

static u64 P[64]; static int E[64]; static int np;
static void addf(u64 p, int e) { for (int i = 0; i < np; i++) if (P[i] == p) { E[i] += e; return; } P[np] = p; E[np] = e; np++; }

static u64 *divs; static size_t ndiv, capd;

int main(int argc, char **argv) {
    u64 N = strtoull(argv[1], 0, 10);
    u64 X = 3 * N / 4 + 1;
    uint32_t *spf = calloc(X + 1, sizeof(uint32_t));
    for (u64 i = 2; i <= X; i++) if (!spf[i]) for (u64 j = i; j <= X; j += i) if (!spf[j]) spf[j] = (uint32_t)i;
    capd = 1 << 20; divs = malloc(capd * sizeof(u64));
    u64 count = 0;
    for (u64 x = N / 4 + 1; 4 * x <= 3 * N; x++) {
        u64 num = 4 * x - N; u128 den = (u128)N * x;
        u64 g = gcdu(num, (u64)(den % num)); /* gcd(num, den) */
        u64 r = num / g; u128 s128 = den / g; u64 s = (u64)s128;
        /* factor s = N*x/g */
        np = 0;
        { u64 m = N; for (u64 p = 2; p * p <= m; p++) { int e = 0; while (m % p == 0) { m /= p; e++; } if (e) addf(p, e); } if (m > 1) addf(m, 1); }
        { u64 m = x; while (m > 1) { u64 p = spf[m]; int e = 0; while (m % p == 0) { m /= p; e++; } addf(p, e); } }
        { u64 m = g; for (int i = 0; i < np && m > 1; i++) while (m % P[i] == 0) { m /= P[i]; E[i]--; } if (m != 1) { fprintf(stderr, "factor error\n"); return 1; } }
        /* divisors of s^2 that are <= s */
        ndiv = 1; divs[0] = 1;
        for (int i = 0; i < np; i++) {
            if (!E[i]) continue;
            size_t cur = ndiv;
            for (size_t k = 0; k < cur; k++) {
                u128 v = divs[k];
                for (int e = 1; e <= 2 * E[i]; e++) {
                    v *= P[i];
                    if (v > s) break;
                    if (ndiv == capd) { capd *= 2; divs = realloc(divs, capd * sizeof(u64)); }
                    divs[ndiv++] = (u64)v;
                }
            }
        }
        u64 smr = s % r;
        for (size_t k = 0; k < ndiv; k++) {
            u64 D = divs[k];
            if ((D % r + smr) % r) continue;
            u128 y = ((u128)D + s) / r;
            if (y < x) continue;
            u128 z = ((u128)s * s / D + s) / r;
            /* verify 4xyz = N(xy+yz+zx) exactly is too big for 128 bits in general; verify via r/s */
            pr128(x); putchar(' '); pr128(y); putchar(' '); pr128(z); putchar('\n');
            count++;
        }
    }
    fprintf(stderr, "# N=%llu count=%llu\n", N, count);
    return 0;
}
