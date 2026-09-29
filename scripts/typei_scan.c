// Exact interval scan of a Type I p-divisible bucket (SIGNED_REFACTOR.md §4,§5).
// For a in [lo,hi] test e=(4a-1)h-a != 0 and e | (t+a)^2.  Pure divisibility
// test, no factorization.  Called from pointwise_fibres_big.py via ctypes.
// Build: gcc -O3 -shared -fPIC scripts/typei_scan.c -o /tmp/typei_scan.so
// Arguments are passed as (hi,lo) 64-bit halves of signed 128-bit integers.
// Requires |t| <= 2^62 and |h| < 2^100 (checked by the caller); products that
// cannot divide x^2 are skipped before any overflow can occur.
#include <stdint.h>

typedef __int128 i128;
static i128 mk(int64_t hi, uint64_t lo) {
    // assemble in unsigned arithmetic (no signed left shift), then convert
    unsigned __int128 u = ((unsigned __int128)(uint64_t)hi << 64) | (unsigned __int128)lo;
    return (i128)u;  // two's complement conversion (GCC/Clang-defined)
}
static i128 ab(i128 v) { return v < 0 ? -v : v; }

// returns number of hits written to out (capacity cap), or -1 on overflow of cap
long typei_scan(int64_t t_hi, uint64_t t_lo, int64_t h_hi, uint64_t h_lo,
                int64_t lo, int64_t hi, int64_t* out, long cap) {
    i128 t = mk(t_hi, t_lo), h = mk(h_hi, h_lo);
    i128 H = 4 * h - 1, aH = ab(H);
    long n = 0;
    for (int64_t a = lo; a <= hi; ++a) {
        i128 x = t + a;
        if (x == 0) continue;
        i128 x2 = x * x;              // |x| <= 2t+|lo| < 2^63
        // |e| <= |a*H| + |h|; if |a|*|H| > 2*x^2 then |e| > x^2 and e cannot divide.
        i128 aa = a < 0 ? -(i128)a : (i128)a;
        if (aa != 0 && aH > (2 * x2) / aa + 1) continue;
        i128 e = (i128)a * H - h;
        if (e == 0) continue;
        if (ab(e) > x2) continue;
        if (x2 % e == 0) {
            if (n >= cap) return -1;
            out[n++] = a;
        }
    }
    return n;
}
