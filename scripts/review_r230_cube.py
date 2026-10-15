"""R230 from-scratch check of CAP_GROWING Prop 1.3 (overflow cube) and the class-count claims of Thm 1.4.

(a) symbolic: identity 4/p = 1/x + 1/y + 1/z with x=(p+E)/4, E=(p+4c^2 d R^2)/l, l=4cdj-1, y=p c d j, z=p x j/(c R^2).
(b) brute force: every prime l = 3 mod 4 up to LMAX, every factorisation K = c0 d0 j (c0, d0 ANY, not nec. squarefree),
    every R with rad R | c0 and v_s(c0)=v_s(K) for s|R, a few primes p in the class -4 c0^2 d0 R^2 mod l, p not | R:
    check x,y integers, z exact denominator R^2, rad R | y, ES^{(y,e)} conditions with e = max v_s(R).
    Also a NEGATIVE control: drop the hypothesis v_s(c0)=v_s(K) and record whether den z = R^2 still holds.
(c) injectivity / distinctness of classes for Thm 1.4's triples.
"""
import sys, random
from fractions import Fraction
from math import gcd
import sympy as sp
from sympy import factorint, isprime, divisors, nextprime

def symbolic():
    p, c, d, j, R = sp.symbols('p c d j R', positive=True)
    l = 4*c*d*j - 1
    E = (p + 4*c**2*d*R**2)/l
    x = (p + E)/4
    y = p*c*d*j
    z = p*x*j/(c*R**2)
    expr = sp.simplify(4/p - 1/x - 1/y - 1/z)
    print("symbolic residual:", expr)
    assert expr == 0

def rad(n):
    r = 1
    for q in factorint(n):
        r *= q
    return r

def vp(n, q):
    v = 0
    while n % q == 0:
        n //= q; v += 1
    return v

def Rs_for(c0, K, emax):
    """all R >= 1 with rad R | c0, v_s(R) <= emax; flag whether hypothesis v_s(c0)=v_s(K) holds"""
    primes = list(factorint(c0)) if c0 > 1 else []
    out = [1]
    for q in primes:
        out = [r * q**a for r in out for a in range(emax + 1)]
    return out

def check_solution(p, c0, d0, j, R, l):
    M = c0*c0*d0*R*R
    assert (p + 4*M) % l == 0
    E = (p + 4*M)//l
    assert (p + E) % 4 == 0, "x not integer"
    x = (p + E)//4
    y = p*c0*d0*j
    z = Fraction(p*x*j, c0*R*R)
    assert Fraction(4, p) == Fraction(1, x) + Fraction(1, y) + 1/z
    assert x > 0 and z > 0
    den = z.denominator
    return den, y

def brute(LMAX, emax, per=3, seed=1):
    rng = random.Random(seed)
    n_ok = n_hyp = n_neg = n_neg_fail = 0
    neg_examples = []
    for l in sp.primerange(7, LMAX):
        if l % 4 != 3: continue
        K = (l + 1)//4
        for c0 in divisors(K):
            for d0 in divisors(K//c0):
                j = K//(c0*d0)
                for R in Rs_for(c0, K, emax):
                    if R % 2 == 0: continue  # Prop 1.3 assumes R odd
                    if R == 1 and c0 > 1 and rng.random() < 0.7:  # thin out R=1 (that's just the cube lemma)
                        continue
                    hyp = all(vp(c0, s) == vp(K, s) for s in factorint(R))
                    M = c0*c0*d0*R*R
                    r = (-4*M) % l
                    if r == 0: continue
                    # primes p = r mod l, p > l, p not | R
                    cnt = 0
                    t = rng.randrange(1, 50)
                    while cnt < per:
                        p = r + l*t; t += rng.randrange(1, 7)
                        if p > 2 and isprime(p) and R % p != 0:
                            den, y = check_solution(p, c0, d0, j, R, l)
                            if hyp:
                                n_hyp += 1
                                assert den == R*R, (l, c0, d0, j, R, p, den)
                                assert y % rad(R) == 0
                                for s in factorint(R):  # ES^{(y,e)} conditions prime by prime
                                    assert s % 2 == 1 and p % s != 0 and y % s == 0
                            else:
                                n_neg += 1
                                if den != R*R:
                                    n_neg_fail += 1
                                    if len(neg_examples) < 3: neg_examples.append((l, c0, d0, j, R, p, den))
                            cnt += 1
    print(f"LMAX={LMAX} emax={emax}: hypothesis cases {n_hyp} all den=R^2 ok; "
          f"cases violating v_s(c0)=v_s(K): {n_neg}, of which den != R^2: {n_neg_fail}; e.g. {neg_examples}")

def classes_thm14(LMAX, e):
    """Thm 1.4 triples: c0,d0 odd squarefree coprime, c0 d0 | K, rad R | c0, v_s(R)<=e, s^2 nmid K for s|R, 4M<l.
    check injectivity of M=c0^2 d0 R^2 and that -4M is a QNR mod l."""
    worst = 0
    for l in sp.primerange(7, LMAX):
        if l % 4 != 3: continue
        K = (l + 1)//4
        seen = {}
        for c0 in divisors(K):
            if c0 % 2 == 0 or not sp.ntheory.factor_.core(c0) == c0: continue
            for d0 in divisors(K//c0):
                if d0 % 2 == 0 or sp.ntheory.factor_.core(d0) != d0 or gcd(c0, d0) != 1: continue
                for R in Rs_for(c0, K, e):
                    if any(K % (s*s) == 0 for s in factorint(R)): continue
                    M = c0*c0*d0*R*R
                    if 4*M >= l: continue
                    cls = (-4*M) % l
                    assert cls not in seen, (l, seen.get(cls), (c0, d0, R))
                    seen[cls] = (c0, d0, R)
                    assert sp.legendre_symbol(cls, l) == -1
        worst = max(worst, len(seen))
    print(f"Thm1.4 triples e={e}, l<{LMAX}: classes distinct, all QNR; max omega'={worst}")

if __name__ == "__main__":
    LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    symbolic()
    for emax in (1, 2, 3):
        brute(LMAX, emax)
    for e in (0, 1, 2, 3):
        classes_thm14(LMAX * 10, e)
