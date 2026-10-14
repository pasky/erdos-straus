// R224 from-scratch check of CONJECTURE 3SQ via Thm A criterion (i):
// w = (t,u,v) in X_n (tuv-u-v=n) is Z^3-embeddable  <=>  (-A/l) = +1 for every odd prime l with v_l(n) odd, A = tu-1.
// For each odd n <= N: E(n) = [every word embeddable]. 3SQ: E(n) <=> n square. Prints exceptions + stats.
// Also: for every non-square n, records whether an "elementary" word (A = 1 or 2) already fails, and the max
// over n of the least u (u <= v enumeration) needed to find a failing word. All loops bounded.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static long long pw(long long a, long long e, long long m) { long long r = 1; a %= m; if (a < 0) a += m; while (e) { if (e & 1) r = r * a % m; a = a * a % m; e >>= 1; } return r; }
static int leg(long long a, long long p) { a %= p; if (a < 0) a += p; if (!a) return 0; return pw(a, (p - 1) / 2, p) == 1 ? 1 : -1; }
int main(int argc, char **argv) {
    long long N = atoll(argv[1]);
    long long M = 2 * N + 10;
    int *spf = calloc(M + 1, sizeof(int));
    for (long long i = 2; i <= M; i++) if (!spf[i]) for (long long j = i; j <= M; j += i) if (!spf[j]) spf[j] = i;
    long long divs[8192];
    long long exc = 0, sqfail = 0, nonsq = 0, elem = 0, resid = 0, nwords105 = 0;
    for (long long n = 1; n <= N; n += 2) {
        long long r = (long long)llround(sqrt((double)n)); int sq = (r * r == n);
        long long L[32]; int nl = 0, m = n;   // odd-exponent primes of n
        { long long x = n; while (x > 1) { long long q = spf[x]; int e = 0; while (x % q == 0) { x /= q; e++; } if (e & 1) L[nl++] = q; } }
        int all_ok = 1; long long cnt = 0, bad = 0;
        for (long long u = 1; (u - 2) * u <= n; u++) {
            long long mm = n + u; int nd = 1; divs[0] = 1;
            while (mm > 1) { long long q = spf[mm]; int e = 0; while (mm % q == 0) { mm /= q; e++; } int cur = nd; long long pk = 1; for (int k = 1; k <= e; k++) { pk *= q; for (int i = 0; i < cur; i++) divs[nd++] = divs[i] * pk; } }
            for (int i = 0; i < nd; i++) {
                long long v = divs[i];
                if (v < u || (n + u + v) % (u * v)) continue;
                long long t = (n + u + v) / (u * v), A = t * u - 1;
                int ok = 1;
                for (int j = 0; j < nl; j++) if (leg(-A, L[j]) != 1) { ok = 0; break; }
                cnt += (u == v) ? 1 : 2; if (!ok) { bad += (u == v) ? 1 : 2; all_ok = 0; }
                if (n == 105 || n == 525) {
                    printf("  n=%lld word (%lld,%lld,%lld) A=%lld embeddable=%d legs:", n, t, u, v, A, ok);
                    for (int j = 0; j < nl; j++) printf(" (-A/%lld)=%d", L[j], leg(-A, L[j])); printf("\n");
                }
            }
            if (!all_ok && !sq && n != 105 && n != 525) goto done;   // early exit for non-squares
        }
    done:
        if (n == 105 || n == 525) printf("n=%lld ordered words %lld, non-embeddable %lld\n", n, cnt, bad);
        if (sq) { if (!all_ok) { sqfail++; printf("SQUARE FAIL %lld\n", n); } }
        else {
            nonsq++;
            if (all_ok) { exc++; printf("EXCEPTION %lld\n", n); }
            int e = 0; for (int j = 0; j < nl; j++) if (leg(-1, L[j]) != 1 || leg(-2, L[j]) != 1) e = 1;
            if (e) elem++; else resid++;
        }
    }
    printf("N=%lld odd non-squares %lld, exceptions %lld, squares failing %lld; elementary (A=1/2) %lld, residual (all odd-exp primes = 1 mod 8) %lld\n", N, nonsq, exc, sqfail, elem, resid);
    return 0;
}
