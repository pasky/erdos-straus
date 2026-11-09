"""Self-test of the letter tests against brute force, small n."""
import sys
sys.path.insert(0, 'scripts')
from z69_nl7_lib import *
bad = 0
for n in range(3, 1500, 2):
    W = set(words_brute(n))
    letters = set()
    for (x, y, z) in W:
        letters |= {x, y, z}
    # every letter L found by brute force must be found by letter tests and vice versa
    W2 = set()
    for L in range(1, n + 3):
        for w in words_with_letter(n, L):
            x, y, z = w
            assert x*y*z - x - z == n and (x*y) % 8 == 0 and min(w) >= 1, (n, w)
            W2.add(w)
    if W != W2:
        bad += 1
        if bad <= 5: print("MISMATCH", n, W ^ W2)
    if W:
        assert max(max(w) for w in W) <= n + 2
print("selftest done, mismatches:", bad)
# T1: odd squares have no U7 word
for m in range(1, 60, 2):
    assert not words_brute(m*m), m
print("T1 ok for m<60")
print("U7 zeros (odd nonsquare) < 1500:", [n for n in range(3,1500,2) if isqrt(n)**2 != n and not words_brute(n)])
