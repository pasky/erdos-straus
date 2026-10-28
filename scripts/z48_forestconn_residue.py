"""z48 forestconn: residue-level check of the reciprocity proof of the slot lemma.

Proof formula (u = 2^a u', v = 2^b v', ab = 0, u', v' odd, n == 1 mod 4, gcd(uv,n) = 1):
    (uv/n) = (2/n)^(a+b) (2/v')^a (2/u')^b (-1/u')(-1/v') (-1)^((u'-1)(v'-1)/4).
Everything on the right depends on a, b, u' mod 8, v' mod 8 and n mod 8, and n mod 8 is a
polynomial in (t,u,v) mod 8. We enumerate all cells (a or b in 0..5, where 5 stands for
"any a >= 3 of odd parity" and 4 for "a >= 3 of even parity"; u is 0 mod 8 when a >= 3)
and check: formula == -1  <=>  slot.  Second check: the formula itself against direct
Jacobi symbols on random/real integer triples, and an independent sympy divisor-based edge
enumeration for small primes.
"""
import random
import sys
from math import isqrt

from sympy import divisors, jacobi_symbol, isprime, legendre_symbol


def chi2(m):  # (2/m) for odd m
    return 1 if m % 8 in (1, 7) else -1


def chim1(m):  # (-1/m)
    return 1 if m % 4 == 1 else -1


def formula(a, b, up, vp, n8):
    s = chi2(n8) ** (a + b) * chi2(vp) ** a * chi2(up) ** b * chim1(up) * chim1(vp)
    if up % 4 == 3 and vp % 4 == 3:
        s = -s
    return s


def slot(t, u, v):
    return t % 4 == 0 or u % 4 == 0 or v % 4 == 0 or (t * u - 1) % 4 == 0 or (t * v - 1) % 4 == 0


def residue_enumeration():
    cells = neg = 0
    # exponent classes: 0,1,2 literal; 3 = "a>=3, odd" ; 4 = "a>=3, even"
    expo = {0: (0, 1), 1: (1, 2), 2: (2, 4), 3: (3, 0), 4: (4, 0)}  # (parity exponent, 2^a mod 8)
    for ea in range(5):
        for eb in range(5):
            if ea and eb:
                continue
            for up in (1, 3, 5, 7):
                for vp in (1, 3, 5, 7):
                    u8 = expo[ea][1] * up % 8
                    v8 = expo[eb][1] * vp % 8
                    for t8 in range(8):
                        n8 = (t8 * u8 * v8 - u8 - v8) % 8
                        if n8 % 4 != 1:
                            continue
                        f = formula(expo[ea][0], expo[eb][0], up, vp, n8)
                        s = slot(t8, u8, v8)
                        cells += 1
                        neg += f == -1
                        assert (f == -1) == s, (ea, eb, up, vp, t8)
    return cells, neg


def formula_vs_jacobi(trials=200000, seed=48):
    rng = random.Random(seed)
    done = 0
    while done < trials:
        t = rng.randint(1, 10**4)
        u = rng.randint(1, 10**6)
        v = rng.randint(1, 10**6)
        n = t * u * v - u - v
        if n <= 0 or n % 4 != 1:
            continue
        if jacobi_symbol(u * v % n, n) == 0:
            continue
        a = (u & -u).bit_length() - 1
        b = (v & -v).bit_length() - 1
        up, vp = u >> a, v >> b
        assert a == 0 or b == 0
        assert formula(a, b, up, vp, n % 8) == jacobi_symbol(u * v % n, n)
        assert (jacobi_symbol(u * v % n, n) == -1) == slot(t, u, v)
        done += 1
    return done


def sympy_edges(limit=20000):
    primes = edges = 0
    for p in range(5, limit, 4):
        if not isprime(p):
            continue
        primes += 1
        # u < v and tuv-u-v = p force (u-1)^2 < (u-1)(v-1) <= p+1
        for u in range(1, isqrt(p + 1) + 3):
            # v > u with v | p+u and u | p+v
            for v in divisors(p + u):
                if v <= u or (p + v) % u:
                    continue
                t, rem = divmod(p + u + v, u * v)
                assert rem == 0
                s = legendre_symbol(u % p, p) * legendre_symbol(v % p, p)
                assert (s == -1) == slot(t, u, v), (p, u, v, t)
                edges += 1
    return primes, edges


if __name__ == "__main__":
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    c, n = residue_enumeration()
    print(f"residue cells (n==1 mod 4): {c}, formula -1 cells: {n}, all agree with slot predicate")
    print(f"random integer triples, formula == Jacobi == slot: {formula_vs_jacobi()}")
    pr, ed = sympy_edges(lim)
    print(f"sympy divisor-enumerated edges, primes p==1 mod 4 below {lim}: {pr} primes, {ed} edges, 0 failures")
