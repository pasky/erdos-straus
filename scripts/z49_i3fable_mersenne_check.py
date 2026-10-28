"""z49_i3fable_mersenne_check.py — independent brute-force check of the exponential-family coverings (Thm 5.5):
for each family and its pair list, report the k in [1, KMAX] with no interior word among the listed pairs, and
compare with the full I3 count (all words) for small k.  Usage: uv run python scripts/z49_i3fable_mersenne_check.py
"""
import sys; sys.path.insert(0, 'scripts')
from z49_i3fable_cells import words
FAM = {
    "2^k-1": (lambda k: 2**k - 1, [(3, 3), (3, 5), (3, 6), (4, 5), (3, 9), (4, 13), (3, 18), (26, 37)]),
    "2^k+1": (lambda k: 2**k + 1, [(3, 3), (3, 4), (3, 6), (3, 9), (3, 18), (9, 21)]),
    "2^k+3": (lambda k: 2**k + 3, [(3, 5), (4, 5), (3, 7), (5, 6), (4, 9), (4, 13)]),
    "2^k-3": (lambda k: 2**k - 3, [(3, 4), (3, 8)]),
    "7*2^k-1": (lambda k: 7 * 2**k - 1, [(3, 3), (3, 6), (4, 5), (3, 11), (5, 10), (4, 13), (5, 12), (8, 9), (5, 15), (5, 20), (8, 65), (15, 65)]),
    # the two families the first search missed (gcd(c, w) > 1 pairs); certificates from the cross-model review and from the repaired search
    "5*2^k-1 (reviewer)": (lambda k: 5 * 2**k - 1, [(5, 6), (3, 3), (3, 6), (6, 15)]),
    "3*2^k+1 (reviewer, L=360)": (lambda k: 3 * 2**k + 1, [(3, 14), (7, 8), (3, 5), (5, 6), (5, 27), (6, 17), (9, 38), (5, 5), (4, 11), (5, 10), (5, 15), (5, 195)]),
    "3*2^k+1 (repaired search, L=60)": (lambda k: 3 * 2**k + 1, [(3, 5), (3, 11), (3, 14), (4, 11), (5, 10), (7, 8), (5, 15), (3, 26), (5, 27), (5, 195)]),
}
KMAX = 2000
for name, (f, pairs) in FAM.items():
    bad = []
    for k in range(1, KMAX + 1):
        n = f(k)
        if n < 3: bad.append(k); continue
        if not any((n + u + v) % (u * v) == 0 and (n + u + v) // (u * v) >= 3 for (u, v) in pairs): bad.append(k)
    small = [(k, len(words(f(k)))) for k in range(1, 15) if f(k) >= 3]
    print(f"{name}: pairs {pairs}; k <= {KMAX} without a listed interior word: {bad}; full I3 for small k: {small}")
