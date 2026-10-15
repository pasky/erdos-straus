"""R237 from-scratch check of CAP_INTERPOLATION Prop 5.1 (both directions) + T1.
Def 1.1 (EXPONENT_CAP): 4/n = 1/x+1/y+1/z, x,y in Z>0, z in Q>0, every prime l with v_l(z)<0 has
l !| 2n, l | y, v_l(z) even, v_l(z) >= -2e.
Usage: review_r237_dict.py MMAX  (part A exhaustive D<M + structured D; part B converse over all x)."""
import sys
from fractions import Fraction
from math import gcd
from sympy import factorint, isprime, nextprime, jacobi_symbol

def def11(n, x, y, z, e):
    if x <= 0 or y <= 0 or z <= 0: return False
    if Fraction(4, n) != Fraction(1, x) + Fraction(1, y) + 1 / z: return False
    for l, a in factorint(z.denominator).items():
        if l == 2 or n % l == 0 or y % l or a % 2 or a > 2 * e: return False
    return True

def vp(n, s):
    c = 0
    while n % s == 0: n //= s; c += 1
    return c

def inDe(D, M, e):
    A = (M + 1) // 4
    for s, t in factorint(D).items():
        sg = vp(A, s)
        if sg == 0: return False
        if t <= 2 * sg: continue
        if s == 2 or t % 2 or t > 2 * sg + 2 * e: return False
    return True

def primes_for(M, D, k=2):
    out, r = [], (-4 * D) % M
    p = r if r > 1 else r + M
    while len(out) < k:
        if isprime(p) and D % p and M % p: out.append(p)
        p += M
    return out

def sol(p, M, D):
    A = (M + 1) // 4
    E, rem = divmod(p + 4 * D, M); assert rem == 0
    x, r4 = divmod(p + E, 4); assert r4 == 0
    return x, p * A, Fraction(p * x * A, D)

def structured(M, e):
    A = (M + 1) // 4
    fa = factorint(A)
    # add one foreign prime (smallest prime not dividing A*M)
    f = 2
    while A % f == 0 or M % f == 0: f = nextprime(f)
    ps = list(fa.items()) + [(f, 0)]
    Ds = [1]
    for s, sg in ps:
        Ds = [d * s**t for d in Ds for t in range(0, 2 * sg + 2 * e + 3) if d * s**t <= 10**12]
    return Ds

def partA(MMAX):
    agree = dis = 0; tests = 0; ins = 0
    for M in range(3, MMAX, 4):
        Ds = set(D for D in range(1, M) if gcd(D, M) == 1) | set(structured(M, 3))
        for D in sorted(Ds):
            if gcd(D, M) != 1: continue
            ps = primes_for(M, D)
            sols = [sol(p, M, D) for p in ps]
            for e in (0, 1, 2, 3):
                pred = inDe(D, M, e)
                for p, (x, y, z) in zip(ps, sols):
                    tests += 1
                    ok = def11(p, x, y, z, e)
                    if ok == pred: agree += 1
                    else:
                        dis += 1
                        if dis < 10: print("DISAGREE", M, D, p, e, pred, ok)
                ins += pred
    print(f"partA M<{MMAX}: tests={tests} agree={agree} disagree={dis} (in-family (D,e) pairs={ins})")

def partB(PMAX, AMAX, XMULT):
    """Converse: every ES^(y,e) solution with y = pA (any x, p !| x) has D = xM - pA in D_e(M), p = -4D mod M."""
    n_sol = n_px = n_pM = bad = 0
    p = 3
    while p < PMAX:
        for A in range(1, AMAX):
            M = 4 * A - 1; y = p * A
            x = p // 4 + 1
            while x <= XMULT * p * A:
                w = Fraction(4, p) - Fraction(1, x) - Fraction(1, y)
                if w > 0:
                    z = 1 / w
                    for e in (0, 1, 2):
                        if def11(p, x, y, z, e):
                            if x % p == 0: n_px += 1; continue
                            if M % p == 0:
                                n_pM += 1
                                if n_pM <= 3: print("  out-of-scope p|M solution:", p, "A=", A, "x=", x, "y=", y, "z=", z, "e=", e)
                                continue
                            n_sol += 1
                            D = x * M - p * A
                            if not (D > 0 and (p + 4 * D) % M == 0 and D % p and inDe(D, M, e)
                                    and sol(p, M, D) == (x, y, z)):
                                bad += 1; print("CONVERSE FAIL", p, A, x, e, D)
                x += 1
        p = nextprime(p)
    print(f"partB p<{PMAX}, A<{AMAX}, x<={XMULT}pA: (solution,e) pairs with p!|x: {n_sol}, failures {bad}; with p|x: {n_px}; with p|M=4A-1: {n_pM} (both outside Prop 5.1's hypothesis p !| DM)")

def t1(MMAX, e):
    cnt = bad = 0
    for M in range(3, MMAX, 4):
        for D in structured(M, e):
            if D * 4 >= M or not inDe(D, M, e): continue
            cnt += 1
            if jacobi_symbol((-D) % M, M) != -1: bad += 1
            # brute: is -4D a square mod M?
            r = (-4 * D) % M
            if any((k * k - r) % M == 0 for k in range(M)): bad += 1; print("SQUARE", M, D)
    print(f"T1 M<{MMAX} e={e}: classes {cnt}, failures {bad}")

if __name__ == "__main__":
    MMAX = int(sys.argv[1])
    partA(MMAX)
    partB(60, 40, 3)
    t1(1500, 3)
