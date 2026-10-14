// R224 from-scratch sign census for primes p = 1 (4) < N.
// Ordered words (t,u,v), t u v - u - v = p  <=>  u v | p + u + v, t = (p+u+v)/(uv).
// chi = (-(tu-1)/p) = ((tu-1)/p) (p = 1 mod 4). Output: p N Nminus lnr
// usage: review_r224_census N [S]   (terminates: all loops bounded by N)
// with a 2nd arg: also output S, Sm = # words (ordered) with A or A* (lnr-1)-smooth ("forced +") and their chi=-1 count
#include <stdio.h>
#include <stdlib.h>
static long long pw(long long a, long long e, long long m) { long long r = 1; a %= m; while (e) { if (e & 1) r = r * a % m; a = a * a % m; e >>= 1; } return r; }
static int smooth(long long a, long long B) { for (long long r = 2; r < B; r++) while (a % r == 0) a /= r; return a == 1; }
static int leg(long long a, long long p) { a %= p; if (a < 0) a += p; if (!a) return 0; return pw(a, (p - 1) / 2, p) == 1 ? 1 : -1; }
int main(int argc, char **argv) {
    long long N = atoll(argv[1]);
    long long M = N + 3000;
    int *spf = calloc(M + 1, sizeof(int));
    for (long long i = 2; i <= M; i++) if (!spf[i]) for (long long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    long long divs[4096]; int wantS = argc > 2;
    for (long long p = 5; p < N; p += 4) {
        if (spf[p] != p) continue;
        long long Nw = 0, Nm = 0, S = 0, Sm = 0;
        long long q = 2; while (leg(q, p) == 1) q++;
        for (long long u = 1; (u - 2) * u <= p; u++) {
            long long m = p + u;               // v | p+u
            int nd = 1; divs[0] = 1;
            while (m > 1) {
                long long r = spf[m]; int e = 0; while (m % r == 0) { m /= r; e++; }
                int cur = nd; long long pk = 1;
                for (int k = 1; k <= e; k++) { pk *= r; for (int i = 0; i < cur; i++) divs[nd++] = divs[i] * pk; }
            }
            for (int i = 0; i < nd; i++) {
                long long v = divs[i];
                if (v < u) continue;
                if ((p + u + v) % (u * v)) continue;
                long long t = (p + u + v) / (u * v);
                int c = leg(t * u - 1, p);
                int mult = (u == v) ? 1 : 2;   // (t,u,v) and (t,v,u) have the same chi (A A* = tp+1 = 1 mod p)
                Nw += mult; if (c == -1) Nm += mult;
                if (wantS && (smooth(t * u - 1, q) || smooth(t * v - 1, q))) { S += mult; if (c == -1) Sm += mult; }
                if (c == 0) { fprintf(stderr, "chi=0?? %lld\n", p); return 1; }
            }
        }
        if (wantS) printf("%lld %lld %lld %lld %lld %lld\n", p, Nw, Nm, q, S, Sm);
        else printf("%lld %lld %lld %lld\n", p, Nw, Nm, q);
    }
    return 0;
}
