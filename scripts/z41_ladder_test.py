"""O272 goal 1: is the order-2^j class of a forced prime l | tn+1 modulo t determined by n (i.e. by t mod l)?

Family: t = 4q, q prime, q = 1 (mod m), with t = -1/n (mod l)  (so l | tn + 1).
For the Dirichlet character of order m mod q, the canonical (choice-free) invariant is
    e(l, q) := discrete-log class of l in F_q^* / F_q^{*m}, i.e. l^{(q-1)/m} mod q  (an m-th root of unity mod q),
reported as the exponent k with l^{(q-1)/m} = g^{k(q-1)/m}, g = least primitive root mod q.
The quadratic part e mod 2 is forced by quadratic reciprocity; the test: is e itself (or e given e mod 2) constant
on the forced progression, or on q mod 16*l*l?  Then: is e a function of the Gaussian / Eisenstein lift of q mod l?
Tiny output.
"""
import sys
from collections import Counter, defaultdict
from sympy import primerange, primitive_root, isprime


def dlog_class(x, q, m, g):
    """k in Z/m with x^{(q-1)/m} = g^{k(q-1)/m} mod q."""
    h = pow(g, (q - 1) // m, q)
    y = pow(x, (q - 1) // m, q)
    z = 1
    for k in range(m):
        if z == y:
            return k
        z = z * h % q
    raise ValueError


def gauss_lift(q):
    """primary pi = a + bi, a odd, b even, with a + b = 1 (mod 4); q = a^2 + b^2."""
    import math
    for b in range(0, math.isqrt(q) + 1, 2):
        a2 = q - b * b
        a = math.isqrt(a2)
        if a * a == a2:
            for A in (a, -a):
                for B in (b, -b):
                    if (A + B) % 4 == 1 and A % 2 == 1:
                        return A, B
    raise ValueError


def run(n, l, m, Q, extra_mod=1):
    ninv = pow(n, -1, l)
    tcls = (-ninv) % l
    rows = []
    for q in primerange(3, Q):
        if q % m != 1 or q == l:
            continue
        if (4 * q) % l != tcls:
            continue
        assert (4 * q * n + 1) % l == 0
        g = primitive_root(q)
        rows.append((q, dlog_class(l, q, m, g)))
    # standard Dirichlet m-character needs a coherent choice of generator; dlog_class with the least primitive
    # root is not coherent across q, but the multiset of e mod 2 and the event "e = 0" (l an m-th power) ARE canonical.
    par = Counter(e % 2 for _, e in rows)
    mth = Counter((e == 0) for _, e in rows)
    # conditional on the quadratic part being trivial (e even): how often is l an m-th power?
    even = [e for _, e in rows if e % 2 == 0]
    zero_given_even = sum(1 for e in even if e == 0)
    return len(rows), dict(par), zero_given_even, len(even)


def gaussian_function_test(l, Q):
    """m = 4: is [l is a quartic residue mod q] a function of the Gaussian lift (a, b) mod l (up to units)?"""
    table = defaultdict(set)
    for q in primerange(5, Q):
        if q % 4 != 1 or q == l:
            continue
        g = primitive_root(q)
        e = dlog_class(l, q, 4, g)
        a, b = gauss_lift(q)
        # value of the quartic symbol depends on pi mod l; record the ratio class x/y in F_l (l = 1 mod 4) or
        # pi^{l-1} in F_{l^2} (l = 3 mod 4) -- simpler: key on (a mod l, b mod l) directly
        table[(a % l, b % l, a % 8, b % 8)].add(e == 0)
    clash = sum(1 for v in table.values() if len(v) > 1)
    return len(table), clash


if __name__ == "__main__":
    Q = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
    print(f"# forced progression t=4q = -1/n (mod l); q prime = 1 (mod m), q < {Q}")
    print("# n l m : #q | parity counts (quadratic part, forced) | #(l m-th power)/#(quadratic part trivial)")
    for (n, l) in [(7, 3), (7, 5), (13, 5), (13, 7), (73, 3), (73, 7), (101, 3), (131, 3), (241, 7), (9, 5), (25, 3), (49, 3)]:
        for m in (4, 8):
            N, par, z, ev = run(n, l, m, Q)
            print(f"{n:4d} {l:3d} {m}: {N:5d} | {par} | {z}/{ev}")
    print("# Gaussian-lift functionality (m=4): #classes (a,b) mod l, #classes with both values")
    for l in (3, 5, 7, 11, 13):
        print(l, gaussian_function_test(l, Q))
