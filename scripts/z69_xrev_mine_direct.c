/* Independent literal U7 checker; no divisor sieve or complementary scan.
 * gcc -O2 scripts/z69_xrev_mine_direct.c -o /tmp/xrev_MINE/direct
 * stdin: n full (full=1 counts every f <= 2n+1; full=0 stops at first witness).
 * stdout: n count first_f. Bound: f>n implies r=f-n divides n+1.
 */
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
int main(void) {
    uint64_t n;
    int full;
    while (scanf("%" SCNu64 " %d", &n, &full) == 2) {
        if (!n || !(n & 1) || n > UINT64_C(1000000000000)) return 2;
        uint64_t count = 0, first = 0;
        for (uint64_t f = 7; f <= 2*n+1; f += 8) {
            uint64_t r = (f - n%f)%f;
            if (r && (f+1)%r == 0) {
                ++count;
                if (!first) first = f;
                if (!full) break;
            }
        }
        printf("%" PRIu64 " %" PRIu64 " %" PRIu64 "\n", n, count, first);
    }
    return ferror(stdin) || ferror(stdout);
}
