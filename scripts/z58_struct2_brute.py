#!/usr/bin/env python3
"""z58 STRUCT2: independent brute force for N_II(n) = #{(a,b,c,d) in N^4 : 4abcd = a+b+nc}.
Bounds (PROVED in Z58_STRUCT2.md §3, Lemma C): every positive solution has 4abd - n in [1, n] (so abd <= n/2) and
c = (a+b)/(4abd - n).  So enumerate (a,b,d) with abd <= n/2 and test integrality of c.  Independent of the (a,b,e) loop.
Usage: uv run python scripts/z58_struct2_brute.py n [n2 ...]     (prints n, count, first solutions);
       uv run python scripts/z58_struct2_brute.py --cmp NMAX       (compare with z58_struct2_bm.positive_points)"""
import sys
sys.path.insert(0, 'scripts')

def brute(n, K=4):
    sols = []
    h = n // 2 if K == 4 else n          # for K = 8 use the weaker bound abd <= n
    for a in range(1, h + 1):
        for b in range(1, h // a + 1):
            for d in range(1, h // (a * b) + 1):
                den = K * a * b * d - n
                if den >= 1 and (a + b) % den == 0:
                    c = (a + b) // den
                    assert K * a * b * c * d == a + b + n * c
                    sols.append((a, b, c, d))
    return sols

if __name__ == '__main__':
    if sys.argv[1] == '--cmp':
        from z58_struct2_bm import positive_points
        N = int(sys.argv[2]); bad = 0
        for n in range(1, N + 1, 2):
            if sorted(brute(n)) != sorted(positive_points(n, 4)):
                bad += 1; print('MISMATCH', n)
        print('compare n <=', N, 'odd: mismatches', bad); sys.exit(1 if bad else 0)
    for s in sys.argv[1:]:
        n = int(s); S = brute(n)
        print(n, 'N_II =', len(S), S[:5])
