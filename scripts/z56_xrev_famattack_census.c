/* Independent census: mark values 4uBC-u-B, without factoring n+u.
 * Build: cc -O2 -o /tmp/famattack-census this-file.c
 * Run: /tmp/famattack-census 7999801 > /tmp/census.txt
 * Memory: N+1 bytes. Time: O(N log^2 N); use external timeout/ulimit.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <errno.h>
int main(int argc, char **argv) {
    if (argc != 2) return 2;
    char *end;
    errno = 0;
    long long N = strtoll(argv[1], &end, 10);
    if (errno || *end || N < 5 || N > 100000000) return 2;
    unsigned char *hit = calloc((size_t)N + 1, 1);
    if (!hit) return 3;
    uint64_t triples = 0;
    /* Odd n implies u+B odd and u != B; enumerate the u<B half. */
    for (long long u = 1; 4*u*(u+1)-2*u-1 <= N; ++u) {
        for (long long B = u+1; 4*u*B-u-B <= N; B += 2) {
            long long q = 4*u*B;
            for (long long n = q-u-B; n <= N; n += q) {
                hit[n] = 1;
                ++triples;
            }
        }
    }
    long long zeros = 0;
    for (long long n = 5; n <= N; n += 4) {
        if (!hit[n]) { printf("%lld 0\n", n); ++zeros; }
    }
    fprintf(stderr, "N=%lld unordered odd-n hits=%llu zeros(1 mod 4)=%lld\n",
            N, (unsigned long long)triples, zeros);
    free(hit);
    return 0;
}
