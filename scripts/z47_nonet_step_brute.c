/* Independent complete three-unit-fraction enumerator, audit only.
 * n <= 10000, k >= 4: products here fit uint64_t. No factoring or ratio gate.
 */
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
    if (argc != 3) return 2;
    uint64_t k = strtoull(argv[1], 0, 10), n = strtoull(argv[2], 0, 10);
    if (k < 4 || n < 2 || n > 10000) return 2;
    for (uint64_t x = n/k+1; x <= 3*n/k; ++x) {
        uint64_t A = k*x-n, B = n*x, lo = B/A+1, hi = 2*B/A;
        if (lo < x) lo = x;
        for (uint64_t y = lo; y <= hi; ++y) {
            uint64_t d = A*y-B;
            if (B*y % d == 0) {
                uint64_t z = B*y/d;
                if (z >= y) printf("%" PRIu64 " %" PRIu64 " %" PRIu64 "\n",x,y,z);
            }
        }
    }
    return 0;
}
