"""R197 from-scratch cell computation for MODEL_SPECIFIC Thm 3.1 (relative to the cell formula, Lemma 3.0').

chi(t,u,v) = (-1/n)*(A/n), with 2(A/n) == n+1-n(t+u+v-9)-A-A* (mod 8), (-1/n) = +1 iff n == 1 (mod 4).
Also: brute-force completeness check of the word enumerator of review_ms_words.py for small n,
and checks of the explicit example words of Thm 3.1(b),(c).
"""
from math import gcd
from fractions import Fraction as F
import itertools
import sys

sys.path.insert(0, "scripts")
from review_ms_words import jacobi, words, slice_solutions  # noqa: E402


def chi_cell(t, u, v):
    n = (t * u * v - u - v) % 8
    if n % 2 == 0:
        return None
    A, As = t * u - 1, t * v - 1
    r = (n + 1 - n * (t + u + v - 9) - A - As) % 8
    assert r in (2, 6), (t, u, v, r)
    jA = 1 if r == 2 else -1
    return jA * (1 if n % 4 == 1 else -1)


def inS(m, t, u, v):
    return (t * u - 1) % m == 0 or (t * v - 1) % m == 0 or t % m == 0 or u % m == 0 or v % m == 0


def main():
    # brute-force completeness of words() for n <= 81
    for n in range(3, 82, 2):
        bf = sorted((t, u, v) for t in range(1, n + 3) for u in range(1, n + 3) for v in range(1, n + 3)
                    if t * u * v - u - v == n and t * u - 1 >= 1)
        assert bf == sorted(words(n)), n
    print("words(): brute force agrees for odd n <= 81")
    for m in range(4, 25):
        L = 8 * m // gcd(8, m)
        c = {1: [0, 0], -1: [0, 0]}
        for t, u, v in itertools.product(range(L), repeat=3):
            ch = chi_cell(t, u, v)
            if ch is None:
                continue
            c[ch][0] += 1
            if inS(m, t, u, v):
                c[ch][1] += 1
        print("m=%2d L=%3d chi=-1 cells %6d in S_m %6d (%.3f) | chi=+1 cells %6d in S_m %6d (%.3f)" % (
            m, L, c[-1][0], c[-1][1], c[-1][1] / c[-1][0], c[1][0], c[1][1], c[1][1] / c[1][0]))
    # example words
    def info(t, u, v):
        n = t * u * v - u - v
        A = t * u - 1
        return n, A, jacobi(-A % n, n)
    print("(4,1,2):", info(4, 1, 2), [inS(m, 4, 1, 2) for m in range(4, 13)])
    bad = 0
    for m in range(5, 2000):
        if m % 4 == 0:
            n, A, ch = info(m, 1, 2)
            if not (inS(m, m, 1, 2) and ch == -1 and gcd(A, n) == 1):
                bad += 1
            continue
        w = {1: (2, 3), 5: (2, 3), 2: (1, 2), 6: (1, 2), 3: (1, 1), 7: (1, 1)}[m % 8]
        n, A, ch = info(m, *w)
        nm = (3, 1, 2) if m >= 6 else (3, 1, 6)
        n2, A2, ch2 = info(*nm)
        ok = ch == 1 and gcd(A, n) == 1 and n >= 3 and n % 2 == 1 and slice_solutions(m, m, *w, n) \
            and ch2 == 1 and not inS(m, *nm)
        if not ok:
            bad += 1
            print("bad example m=", m, w, n, A, ch)
    print("Thm 3.1(b),(c) example words checked for 5 <= m < 2000: bad =", bad)


if __name__ == "__main__":
    main()
