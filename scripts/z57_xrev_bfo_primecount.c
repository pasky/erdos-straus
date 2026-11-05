/* Independent AP-only segmented prime count for the four BFO intervals.
 * gcc -O2 scripts/z57_xrev_bfo_primecount.c -o /tmp/bfo_primecount
 * Memory: <2 MiB; no solution engine or original sieve code is reused.
 */
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#define SEG (1 << 20)
static unsigned char composite[150001], live[SEG];
static int primes[20000], np;
int main(void) {
    for (int n = 2; n <= 150000; ++n) {
        if (composite[n]) continue;
        primes[np++] = n;
        for (int64_t m = (int64_t)n*n; m <= 150000; m += n)
            composite[m] = 1;
    }
    int64_t total = 0;
    for (int k = 0; k < 4; ++k) {
        int64_t a = 10000000001LL + k*2500000000LL;
        int64_t b = 10000000000LL + (k+1)*2500000000LL, count = 0;
        for (int64_t lo = a; lo <= b; lo += 4LL*SEG) {
            int len = (b-lo)/4 + 1 < SEG ? (int)((b-lo)/4 + 1) : SEG;
            int64_t hi = lo + 4LL*(len-1);
            memset(live, 1, (size_t)len);
            for (int j = 1; j < np; ++j) {
                int64_t q = primes[j];
                if (q*q > hi) break;
                int64_t start = ((lo+q-1)/q)*q;
                while (start%4 != 1) start += q;
                if (start < q*q) start = q*q;
                for (int64_t i = (start-lo)/4; i < len; i += q) live[i] = 0;
            }
            for (int i = 0; i < len; ++i) count += live[i];
        }
        total += count;
        printf("[%lld,%lld] %lld\n", (long long)a, (long long)b, (long long)count);
        fflush(stdout);
    }
    printf("total %lld\n", (long long)total);
}
