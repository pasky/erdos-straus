"""R286 from-scratch checks of the symmetric re-indexings (1.3), (2.2), (2.3), (2.5) of LOWER_TAIL_FABLE.

Count-level comparison (p < P, complete bounds) against the Type I / Type II certificates obtained by
mapping ALL brute-force solutions (review_r286_canon.cert_of):
  * (2.2) II: pairs (u,c) with r = least positive residue of -p mod 4uc, r | u+c.     [bound u,c <= p/2]
  * (2.3) II: triples (u,k,e) with 4ku | p+e, e | p+4ku^2                               [enumerate via p+e = 4ku*v]
  * (2.2) I : pairs (u,c), r = least positive residue of -p^{-1} mod 4uc, r | u+c         [window]
And existence-level for (2.5): p = e^2 k^2 - y^2 - e, e = 3 (4), and the 'equivalently p in W - squares,
W = {X^2 - e : e | X}' reading, including odd squares as T1 control.
"""
import sys
from collections import Counter
from review_r286_canon import isprime, solutions, cert_of, divisors


def certs(p):
    cs = set()
    for s in solutions(p):
        for c in cert_of(p, s):
            cs.add(c)
    return cs


def form22_II(p):
    out = set()
    for u in range(1, p // 2 + 1):
        for c in range(1, p // (2 * u) + 1):   # x = u c w <= p/2 forces u c <= p/2
            M = 4 * u * c
            r = (-p) % M
            if r and (u + c) % r == 0:
                out.add((u, c))
    return out


def form23_II(p):
    out = set()
    for e in range(1, 3 * p):            # e = 4x - p <= p (x <= p/2), generous
        for K in divisors(p + e):
            if K % 4:
                continue
            ku = K // 4
            for u in divisors(ku):
                k = ku // u
                if (p + 4 * k * u * u) % e == 0:
                    out.add((u, k, e))
    return out


def form22_I(p, B):
    out = set()
    for u in range(1, B):
        for c in range(1, B):
            M = 4 * u * c
            if M % p == 0:
                continue
            r = (-pow(p, -1, M)) % M
            if r and (u + c) % r == 0:
                out.add((u, c))
    return out


def form25(n, E):
    """p + e + y^2 = (e k)^2 with e = 3 mod 4: enumerate e, then factor n+e = (ek-y)(ek+y)"""
    hits = []
    for e in range(3, E, 4):
        N = n + e
        for a in divisors(N):
            b = N // a
            if a <= b and (a + b) % 2 == 0:
                X, y = (a + b) // 2, (b - a) // 2
                if X % e == 0:
                    hits.append((e, X // e, y))
    return hits


def W_minus_sq(n, E):
    """n = X^2 - e - y^2 with e | X, ANY e >= 1 (the 'equivalently' reading)"""
    for e in range(1, E):
        N = n + e
        for a in divisors(N):
            b = N // a
            if a <= b and (a + b) % 2 == 0 and ((a + b) // 2) % e == 0:
                return (e, (a + b) // 2, (b - a) // 2)
    return None


if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    st = Counter()
    for p in range(5, P, 4):
        if not isprime(p):
            continue
        cs = certs(p)
        nII = sum(1 for c in cs if c[0] == "II")
        nI = sum(1 for c in cs if c[0] == "I")
        f2 = form22_II(p)
        f3 = form23_II(p)
        st["primes"] += 1
        st["(2.2)II count == #II certs"] += (len(f2) == nII)
        st["(2.3)II count == #II certs"] += (len(f3) == nII)
        # Type I: (2.2) witness set vs certificate (u,c)-projections in a window
        B = 40
        g = form22_I(p, B)
        st["(2.2)I nonempty"] += bool(g)
        st["(2.5) nonempty"] += bool(form25(p, 4 * p))
        # which certs have w = 1 or w a square (the only ones (2.5) visibly encodes)
        sqw = any(c[0] == "II" and int(c[3] ** 0.5) ** 2 == c[3] for c in cs)
        st["has II cert with square w"] += sqw
        if not sqw:
            print("p", p, ": every Type II certificate has non-square level w")
    for m in range(3, 80, 2):
        n = m * m
        st["odd squares"] += 1
        st["squares with (2.5) witness"] += bool(form25(n, 4 * n))
        st["squares in W - sq (any e)"] += W_minus_sq(n, 10) is not None
    for p in range(5, P, 4):
        if isprime(p):
            st["primes in W - sq via e=2"] += W_minus_sq(p, 3) is not None and W_minus_sq(p, 3)[0] <= 2
    for k, v in sorted(st.items()):
        print(k, v)
