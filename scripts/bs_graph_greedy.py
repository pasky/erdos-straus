"""Deterministic Egyptian-fraction algorithms on 4/p and the offset-greedy family.

For primes p = 1 (mod 24) up to PMAX:
  * greedy (Fibonacci-Sylvester), Engel, Golomb/Farey-predecessor: does the algorithm give <= 3 terms?
  * offset greedy G_J: x = ceil(p/4)+j, j < J, then any 2-term completion of 4/p - 1/x.
    J(p) := least j that works (j = (e-3)/4 with e = 4x - p: the e-slice / window frame).
Usage: python bs_graph_greedy.py PMAX
"""
import sys
from fractions import Fraction
from collections import Counter
from sympy import primerange, divisors


def greedy(fr, kmax=3):
    t = 0
    while fr > 0 and t <= kmax:
        x = -(-fr.denominator // fr.numerator)
        fr -= Fraction(1, x); t += 1
    return t if fr == 0 else 99


def engel(fr, kmax=3):
    # fr = 1/q1 + 1/(q1q2) + ...
    t = 0
    while fr > 0 and t <= kmax:
        q = -(-fr.denominator // fr.numerator)  # ceil(1/fr)
        fr = fr * q - 1; t += 1
    return t if fr == 0 else 99


def golomb(fr, kmax=3):
    # a/b = a'/b' + 1/(b b'), a'/b' the Farey predecessor (b' < b, a b' - a' b = 1)
    t = 0
    while fr > 0 and t <= kmax:
        a, b = fr.numerator, fr.denominator
        if a == 1:
            return t + 1
        bp = pow(a, -1, b)  # a*bp = 1 mod b
        ap = (a * bp - 1) // b
        fr = Fraction(ap, bp); t += 1
    return t if fr == 0 else 99


def two_term(a, b):
    """a/b = 1/y+1/z (y<=z) solvable?"""
    from math import gcd
    g = gcd(a, b); a //= g; b //= g
    for u in divisors(b * b):
        if u > b:
            break
        if (b + u) % a == 0 and (b + b * b // u) % a == 0:
            return True
    return False


def J_of(p, jmax=400):
    x0 = (p + 3) // 4
    for j in range(jmax):
        x = x0 + j
        if two_term(4 * x - p, p * x):
            return j
    return None


if __name__ == '__main__':
    PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    alg = Counter(); Js = Counter(); worst = []
    for p in primerange(5, PMAX):
        if p % 24 != 1:
            continue
        fr = Fraction(4, p)
        alg['greedy<=3'] += greedy(fr) <= 3
        alg['engel<=3'] += engel(fr) <= 3
        alg['golomb<=3'] += golomb(fr) <= 3
        alg['total'] += 1
        J = J_of(p)
        Js[J] += 1
        worst.append((J, p))
    print(dict(alg))
    print('J(p) distribution:', sorted(Js.items()))
    print('largest J:', sorted(worst)[-5:])
