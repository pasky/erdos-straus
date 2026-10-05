"""R32 from-scratch check of POINTWISE_XWIN Lemma 1.1 (half-set lemma).

Rat_a(x) = { u/v mod a : u*v | x, gcd(u,v)=1 }  (POINTWISE_SIZE §8.1), computed by
full enumeration of exponent vectors (u gets r^i, v gets r^j, i*j=0, i+j<=v_r(x)).
Check: whenever -1 not in Rat_a(x), C(x) (classes of prime factors of x) lies in some
S_sigma, i.e. in every Klein orbit {g,g^-1,-g,-g^-1} C meets only one of the halves
{g,g^-1},{-g,-g^-1}, and -1 not in C.  Also checks |S_sigma|=phi/2 and the beta formula.
"""
import sys, random
from math import gcd

def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def rat(x, a, fx):
    vals = {1}
    for r, e in fx.items():
        rm = r % a
        rinv = pow(rm, -1, a)
        mults = [1]
        for i in range(1, e + 1):
            mults.append(pow(rm, i, a))
            mults.append(pow(rinv, i, a))
        vals = {(v * m) % a for v in vals for m in mults}
    return vals

def orbits(a):
    G = [g for g in range(1, a) if gcd(g, a) == 1]
    seen, orbs = set(), []
    for g in G:
        if g in seen:
            continue
        gi = pow(g, -1, a)
        h1 = frozenset({g, gi})
        h2 = frozenset({(-g) % a, (-gi) % a})
        assert not (h1 & h2), (a, g)
        seen |= h1 | h2
        orbs.append((h1, h2))
    return G, orbs

def omega(n):
    return len(factor(n))

FCACHE = {}

def check_a(a, xs):
    G, orbs = orbits(a)
    phi = len(G)
    nfixed = [o for o in orbs if len(o[0]) == 1]
    beta_formula = (phi - 2 ** omega(a)) // 4 + 2 ** (omega(a) - 1) - 1
    assert len(orbs) - 1 == beta_formula, (a, len(orbs), beta_formula)
    assert sum(len(h1) for h1, h2 in orbs) == phi // 2
    assert len(nfixed) == 2 ** (omega(a) - 1), a
    fails = 0
    for x in xs:
        if gcd(x, a) != 1:
            continue
        fx = FCACHE.get(x)
        if fx is None:
            fx = FCACHE[x] = factor(x)
        R = rat(x, a, fx)
        if (a - 1) in R:
            continue
        fails += 1
        C = {r % a for r in fx}
        assert (a - 1) not in C
        for h1, h2 in orbs:
            if (C & h1) and (C & h2):
                print("COUNTEREXAMPLE", a, x, sorted(C), sorted(h1), sorted(h2))
                return None
    return fails

if __name__ == "__main__":
    amax = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    xmax = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    random.seed(1)
    big = [random.randrange(10**8, 10**12) for _ in range(2000)]
    tot = 0
    for a in range(3, amax + 1, 4):
        f = check_a(a, list(range(1, xmax + 1)) + big)
        if f is None:
            sys.exit(1)
        tot += f
    print("OK: a<=%d, x<=%d plus 2000 random x in [1e8,1e12]; failing (a,x) pairs checked: %d" % (amax, xmax, tot))
