/* O273 item (3): interior five-slice union R_III^int(n) (= DEDEKIND_ES Thm 4.5 set N_-) and its
 * T1-exact Brauer–Manin-type main term, per n.  EVIDENCE tool.
 *
 * Interior pairs: ordered (u,v), u,v >= 2, gcd(u,v) = 1, 2uv - u - v <= n  (t := (n+u+v)/(uv) >= 2 at hits).
 * Hit: uv | n+u+v.  R = #hits with Jacobi (uv/n) = -1 (= five-slice union for n = 1 mod 4, Thm 4.5).
 * Main term (n = 1 mod 4), uv = 2^k w, w odd, a = -(u+v):
 *   eps(n) := (2/n)^k (a/w)  [value of (uv/n) forced at a hit];  active := 2^k | n+u+v and eps = -1;
 *   term := [active] [gcd(n,uv)=1] * ( w non-square: (1 - (uv/n))/phi(w) ;  w square: 1/phi(w) ).
 *   principal (p-free given n mod 2^k):  [active]/phi(w).
 * Usage: z42_five_slice n1 [n2 ...]   (prints one line per n)
 *        z42_five_slice -r lo hi step  (all primes = 1 mod 4 in [lo,hi), every step-th)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int *phi; static int NMAX;
static signed char *J; /* J[x] = (x/n) for current n */

static int jacobi(long a, long n) { /* n odd > 0 */
    int s = 1; a %= n; if (a < 0) a += n;
    while (a) {
        while (!(a & 1)) { a >>= 1; long r = n & 7; if (r == 3 || r == 5) s = -s; }
        long t = a; a = n; n = t;
        if ((a & 3) == 3 && (n & 3) == 3) s = -s;
        a %= n;
    }
    return n == 1 ? s : 0;
}
static long gcdl(long a, long b) { while (b) { long t = a % b; a = b; b = t; } return a; }
static int issq(long w) { long r = (long)llround(sqrt((double)w)); while (r*r > w) r--; while ((r+1)*(r+1) <= w) r++; return r*r == w; }
static int isprime(long n) { if (n < 2) return 0; for (long d = 2; d*d <= n; d++) if (n % d == 0) return 0; return 1; }

static void run(long n) {
    for (long x = 0; x < n; x++) J[x] = (signed char)jacobi(x, n);
    int two = ((n & 7) == 1 || (n & 7) == 7) ? 1 : -1;
    /* sectors: 0 odd-odd, 1 k=1, 2 k=2, 3 k>=3 */
    double M = 0, M0[4] = {0}, Mcls[4] = {0};
    long R[4] = {0}, hits = 0, viol45 = 0, violeps = 0, eight = 0, sqterms = 0, autoviol = 0, U = 0;
    for (long u = 2; 2*u*u - 2*u <= n; u++) {
        long vmax = (n + u) / (2*u - 1);
        for (long v = u + 1; v <= vmax; v++) {
            if (gcdl(u, v) != 1) continue;
            int c = J[u % n] * J[v % n];
            if (c == 0) continue;            /* gcd(n, uv) > 1 */
            long uv = u * v; int k = 0; long w = uv; while (!(w & 1)) { w >>= 1; k++; }
            int sec = k == 0 ? 0 : (k == 1 ? 1 : (k == 2 ? 2 : 3));
            int twoad = ((n + u + v) % (1L << k)) == 0;
            if (twoad) {
                int eps = ((k & 1) ? two : 1) * jacobi(-(u + v), w);
                if (k >= 2 && (n & 3) == 1 && eps != -1) autoviol++;  /* claim: k>=2 + 2-adic => active */
                if (eps == -1) {
                    int sq = issq(w);
                    double term = sq ? 1.0 / phi[w] : (1.0 - c) / phi[w];
                    if (sq) sqterms++;
                    M += 2 * term; M0[sec] += 2.0 / phi[w];
                }
            }
            if ((n + u + v) % uv == 0) {
                hits += 2; long t = (n + u + v) / uv;
                int five = ((t*u - 1) % 4 == 0) || ((t*v - 1) % 4 == 0) || (t % 4 == 0) || (u % 4 == 0) || (v % 4 == 0);
                if ((n & 3) == 1 && (five != (c == -1))) viol45++;
                if (five) U += 2;
                int eps = ((k & 1) ? two : 1) * jacobi(-(u + v), w);
                if ((n & 3) == 1 && eps != c) violeps++;
                if (c == -1) {
                    R[sec] += 2;
                    int e8 = (t % 8 == 0) || (u % 8 == 0) || (v % 8 == 0) || ((t*u - 1) % 8 == 0) || ((t*v - 1) % 8 == 0);
                    if (e8) eight += 2;
                }
            }
        }
    }
    double L = log((double)n);
    long Rt = R[0] + R[1] + R[2] + R[3];
    double M0t = M0[0] + M0[1] + M0[2] + M0[3];
    (void)Mcls;
    printf("n=%ld mod8=%ld L2=%.2f R=%ld [oo %ld k1 %ld k2 %ld k3+ %ld] M=%.3f M0=%.3f [oo %.3f k1 %.3f k2 %.3f k3+ %.3f] "
           "hits=%ld U5=%ld viol45=%ld violeps=%ld autoviol=%ld eight=%ld sqterms=%ld R/L2=%.4f M/L2=%.4f M0/L2=%.4f\n",
           n, n & 7, L*L, Rt, R[0], R[1], R[2], R[3], M, M0t, M0[0], M0[1], M0[2], M0[3],
           hits, U, viol45, violeps, autoviol, eight, sqterms, Rt/(L*L), M/(L*L), M0t/(L*L));
    fflush(stdout);
}

int main(int argc, char **argv) {
    long lo = 0, hi = 0, step = 1; int ranged = argc >= 5 && !strcmp(argv[1], "-r");
    long nmax = 0;
    if (ranged) { lo = atol(argv[2]); hi = atol(argv[3]); step = atol(argv[4]); nmax = hi; }
    else for (int i = 1; i < argc; i++) if (atol(argv[i]) > nmax) nmax = atol(argv[i]);
    NMAX = (int)nmax + 2;
    phi = malloc(sizeof(int) * (NMAX + 1)); J = malloc(NMAX + 1);
    for (int i = 0; i <= NMAX; i++) phi[i] = i;
    for (int i = 2; i <= NMAX; i++) if (phi[i] == i) for (int j = i; j <= NMAX; j += i) phi[j] -= phi[j] / i;
    if (ranged) { long cnt = 0; for (long n = lo; n < hi; n++) if ((n & 3) == 1 && isprime(n)) { if (cnt++ % step == 0) run(n); } }
    else for (int i = 1; i < argc; i++) run(atol(argv[i]));
    return 0;
}
