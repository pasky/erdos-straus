"""Independent brute-force check of V_I(n) u V_II(n) emptiness (small n), cf. bs_corr_vempty.c.
Enumerates a<=b, d, e directly from 4abd = n e + 1 (I) or n + e (II), e | a+b."""
import sys
def nonempty(n):
    # Type II: e = 4abd - n >= 1, e <= a+b  => 4abd <= n + a + b <= n + 2b  => 4ad <= n/b + 2
    for a in range(1, n + 2):
        for d in range(1, n + 2):
            if 4 * a * d - 2 > n / a: break
            for b in range(a, 10 * n + 10):
                e = 4 * a * b * d - n
                if e > a + b: break
                if e >= 1 and (a + b) % e == 0: return 'II', (a, b, (a + b) // e, d, e)
    # Type I: 4abd = n e + 1, e | a+b, e <= a+b
    for a in range(1, 2 * n + 2):
        for d in range(1, 2 * n + 2):
            if 4 * a * d > 2 * n + 2: break
            for b in range(a, 10 * n * n + 10):
                if (4 * a * b * d - 1) % n: continue
                e = (4 * a * b * d - 1) // n
                if e > a + b: break
                if e >= 1 and (a + b) % e == 0: return 'I', (a, b, (a + b) // e, d, e)
    return None
if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for n in range(lo, hi + 1):
        r = nonempty(n)
        if r is None: print('EMPTY', n)
