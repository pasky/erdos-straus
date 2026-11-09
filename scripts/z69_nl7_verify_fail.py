"""Independent re-verification of the explicit rule failures (different code path from z69_nl7_lib letter tests):
for each candidate letter L and each position, solve the word equation directly from divisors.
  x = L:  n + L = z*(L*y - 1)      -> for each divisor z of n+L: y = ((n+L)/z + 1)/L
  z = L:  n + L = x*(y*L - 1)      -> for each divisor x of n+L: y = ((n+L)/x + 1)/L
  y = L:  L*n + 1 = (xL-1)(zL-1)   -> for each divisor F of Ln+1: x = (F+1)/L, z = ((Ln+1)/F + 1)/L
A U7 word (either orientation) is a positive solution with 8 | x*y or 8 | z*y.
usage: verify_fail.py FAMILY RULE file_with_FAIL_lines
"""
import sys
sys.path.insert(0, 'scripts')
from sympy import divisors, isprime
from z69_nl7_polyrule import RULES

def any_word_with_letter(n, L):
    found = []
    for z in divisors(n + L):
        q = (n + L) // z
        if (q + 1) % L == 0:
            y = (q + 1) // L
            for (x_, y_, z_) in ((L, y, z), (z, y, L)):   # letter as x, and (reading z as x) letter as z
                assert x_ * y_ * z_ - x_ - z_ == n
                if (x_ * y_) % 8 == 0 or (z_ * y_) % 8 == 0:
                    found.append((x_, y_, z_))
    N = L * n + 1
    for F in divisors(N):
        G = N // F
        if (F + 1) % L == 0 and (G + 1) % L == 0:
            x, z = (F + 1) // L, (G + 1) // L
            assert x * L * z - x - z == n
            if (x * L) % 8 == 0 or (z * L) % 8 == 0:
                found.append((x, L, z))
    return found

fam, rule, fn = sys.argv[1], sys.argv[2], sys.argv[3]
B = 1 if fam == 't2p1' else int(fam.split(':')[1])
for line in open(fn):
    if not line.startswith('FAIL'):
        continue
    t, p = int(line.split()[1]), int(line.split()[2])
    assert p == t * t + B * B and isprime(p) and p % 8 == 1
    letters = set()
    for e in RULES[rule](t, B):
        if e > 0:
            letters |= set(divisors(e))
    bad = {L: any_word_with_letter(p, L) for L in sorted(letters) if any_word_with_letter(p, L)}
    # and exhibit a U7 word with some other letter, to show p is not a U7 zero
    other = None
    for L in range(1, 200):
        w = any_word_with_letter(p, L)
        if w:
            other = (L, w[0]); break
    print(f"t={t} p={p} p%840={p%840} candidate letters={sorted(letters)}\n   words with a candidate letter: {bad if bad else 'NONE (rule fails, re-verified)'};  least letter of any U7 word: {other}")
