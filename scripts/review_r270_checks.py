"""R270 from-scratch checks for B1_LINE.md (O259). Does not import any z29_* code.
usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_r270_checks.py <part>
parts: brute (Lemma 1.1/3.1 vs raw ES brute force, p < 400), genus (Lemma 1.2 / Cor 1.3 / Prop 1.4, p < 2e4),
       freeze (Prop 4.1 on p = 1 mod M_sigma), dickson (Thm 4.2 examples), chi (Sec. 5), records, mainterm, nb
"""
import sys, math, random
from fractions import Fraction
from sympy import isprime, factorint, divisors, jacobi_symbol, primerange, totient

def b1_pairs(p):
    """all unordered pairs {s,t} (s<t) with s*t | p+s+t and 4 | s*t (literal definition, s <= 1+sqrt(p+1))."""
    out = []
    B = 1 + math.isqrt(p + 1)
    for s in range(1, B + 1):
        for t in divisors(p + s):
            if t <= s:
                continue
            if (s * t) % 4 == 0 and (p + s + t) % (s * t) == 0:
                out.append((s, t))
    # pairs with t < s were found at shift t; pairs with both > B impossible
    return out

def star_pairs(p):
    """(★): unordered {x,y}, x<=y, 4xy | p+x+y."""
    out = []
    B = (1 + math.isqrt(4 * p + 1)) // 4 + 1
    for x in range(1, B + 1):
        for y in divisors(p + x):
            if y < x:
                continue
            if (p + x + y) % (4 * x * y) == 0:
                out.append((x, y))
    return out

def pair_to_solution(p, s, t):
    D, g = (s, t) if s % 4 == 0 else (t, s)
    assert D % 4 == 0 and g % 2 == 1
    d = D // 4
    c = (p + s + t) // (s * t)
    w = 4 * c * d - 1
    assert (c * p + 1) % w == 0
    a = (c * p + 1) // w
    return a, c, d, (a * d, a * c * d * p, c * d * p)

def is_typeA(tr):
    import itertools
    for X, Y, Z in itertools.permutations(tr):
        if (X * Y) % Z == 0:
            d = X * Y // Z
            if d >= 1 and X % d == 0 and Y % d == 0 and d * (X // d) * (Y // d) == Z:
                return True
    return False

def brute():
    bad = 0
    for p in primerange(5, 400):
        if p % 4 != 1:
            continue
        sols = set()
        # all x<=y<=z with 4/p = 1/x+1/y+1/z
        for x in range(p // 4 + 1, 3 * p // 4 + 2):
            r1 = Fraction(4, p) - Fraction(1, x)
            if r1 <= 0:
                continue
            ylo = max(x, math.floor(1 / r1) + 1)
            yhi = math.floor(2 / r1)
            for y in range(ylo, yhi + 1):
                r2 = r1 - Fraction(1, y)
                if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                    sols.add((x, y, r2.denominator))
        A = {s for s in sols if is_typeA(s)}
        P = b1_pairs(p)
        inc = sum(1 for d in range(1, (p + 3) // 8 + 1) for c in range(1, p + 1)
                  if 4 * c * d - 1 <= p + 4 * d and (p + 4 * d) % (4 * c * d - 1) == 0)
        fromP = {tuple(sorted(pair_to_solution(p, s, t)[3])) for s, t in P}
        if not (len(A) == len(P) == inc == len(fromP) and fromP == A):
            bad += 1
            print("MISMATCH", p, len(A), len(P), inc, len(fromP))
    print("brute: primes p=1(4) < 400 checked; mismatches:", bad)

def genus(N=20000):
    nb = ns = ov = viol = 0
    free = {}
    for p in primerange(5, N):
        if p % 4 != 1:
            continue
        two = jacobi_symbol(2, p)
        P = b1_pairs(p); S = star_pairs(p)
        nb += len(P); ns += len(S)
        ov += len({tuple(sorted(x)) for x in P} & {tuple(sorted(x)) for x in S})
        for (s, t) in P:
            S_, T = (s, t) if s % 4 == 0 else (t, s)
            k = (S_ & -S_).bit_length() - 1
            Sp = S_ >> k
            if T % 4 != 3 or math.gcd(S_, T) != 1: viol += 1
            if jacobi_symbol(S_ * T % p, p) != -1: viol += 1
            j = jacobi_symbol(Sp * T % p, p)
            if j != -(two ** k): viol += 1
            if j == 1: free[('b1', p % 8, k % 2)] = free.get(('b1', p % 8, k % 2), 0) + 1
        for (x, y) in S:
            if x % 2 == 1 and y % 2 == 1: viol += 1; continue
            if x % 2 == 0 and y % 2 == 0: viol += 1; continue
            X, Y = (x, y) if x % 2 == 0 else (y, x)
            k = (X & -X).bit_length() - 1
            Xp = X >> k
            if jacobi_symbol(X * Y % p, p) != -1: viol += 1
            j = jacobi_symbol(Xp * Y % p, p)
            if j != -(two ** k): viol += 1
            if j == 1: free[('star', p % 8, k % 2)] = free.get(('star', p % 8, k % 2), 0) + 1
        # Prop 1.4
        if p % 24 != 1 and not P: viol += 1; print("Prop1.4 b1 FAIL", p)
        if p % 8 == 5 and not S: viol += 1; print("Prop1.4 star FAIL", p)
    print(f"genus N={N}: b1 pairs {nb}, star pairs {ns}, overlaps {ov}, violations {viol}, free {free}")
    if 181 < N: print("181 star pairs:", star_pairs(181))

def M(sig):
    m = 1
    for l in primerange(2, sig + 2):
        e = 1
        while l ** e <= sig + 1: e += 1
        m *= l ** e  # e = floor(log_l(sig+1)) + 1
    return m

def freeze(LIM=2 * 10 ** 9):
    for sig in (3, 5, 7, 11):
        print("M_%d =" % sig, M(sig))
    for sig in (7, 11):
        Ms = M(sig); np_ = npairs = nprime = bad = 0
        for k in range(1, LIM // Ms + 1):
            p = 1 + Ms * k
            if not isprime(p): continue
            np_ += 1
            for s in range(1, sig + 1):
                n = p + s
                actual = sorted(t for t in divisors(n) if t > s and (s * t) % 4 == 0 and (p + s + t) % (s * t) == 0)
                if s >= 3:
                    assert n % (1 + s) == 0
                    Q = n // (1 + s)
                    if Q % s != 1 % s or min(factorint(Q)) <= sig + 1: bad += 1
                    pred = sorted(t for t in divisors(n) if t > s and t % s == s - 1 and (s * t) % 4 == 0)
                    if pred != actual: bad += 1
                    if isprime(Q):
                        nprime += 1
                        if actual: bad += 1
                elif actual: bad += 1
                npairs += len(actual)
                for t in actual:
                    if Ms % (s * t) == 0: bad += 1  # (a)
        print(f"freeze sigma={sig} M={Ms}: primes {np_}, shift<=sigma pairs {npairs}, Q_s prime cases {nprime}, bad {bad}")

if __name__ == "__main__":
    globals()[sys.argv[1]](*[int(float(a)) for a in sys.argv[2:]])
