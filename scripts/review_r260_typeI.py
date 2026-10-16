"""R260 from-scratch check of ASTRA_BRIDGE Thm 2.1, Cor 2.2, Prop 3.3(b).

Thm 2.1: for p, level e = 3 (4) (composite allowed), H = (pe+1)/4, twist n:
  side (a): r | H^2, e | n^2+4r, gcd(r,n)=1  (Astra STR (28)-(30))
  side (b): rational points 4/p = 1/x + 1/v + 1/(pH), v integer, den x = n^2 exactly.
Side (b) is enumerated independently of the theorem: with t = e v - H > 0,
  x = H v / t, and gcd(Hv, t) | H^2 (gcd(v,t)=gcd(v,H), gcd(H,t)=gcd(H,v) as gcd(H,e)=1),
  so den x = n^2 forces t | n^2 H^2.  We enumerate divisors t of n^2 H^2.
Cor 2.2: prime e; alive (some n <= 3e, brute force) <=> H has a prime factor s with
  Kronecker (s/p) = -1; least twist < e.
Prop 3.3(b): odd squares a^2 in place of p, all e = 3 (4) (composite) up to bound, n <= bound: no state.
Usage: review_r260_typeI.py P E NMAX
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import factorint, primerange, isprime, jacobi_symbol


def divisors_from_fac(fac):
    ds = [1]
    for q, a in fac.items():
        ds = [d * q**i for d in ds for i in range(a + 1)]
    return ds


def kron(s, p):  # Kronecker (s/p), p odd prime
    if s == 2:
        return 1 if p % 8 in (1, 7) else -1
    return jacobi_symbol(s, p)


def side_a(p, e, H, n, Hdiv2):
    out = set()
    for r in Hdiv2:
        if (n * n + 4 * r) % e == 0 and gcd(r, n) == 1:
            U = (n * n * H + r) // e
            assert (n * n * H + r) % e == 0
            assert (H * U) % r == 0
            v = H * U // r
            out.add((F(U, n * n), v))
    return out


def side_b(p, e, H, n, facH):
    fac = {q: 2 * a for q, a in facH.items()}
    for q, a in factorint(n).items():
        fac[q] = fac.get(q, 0) + 2 * a
    out = set()
    for t in divisors_from_fac(fac):
        if (t + H) % e:
            continue
        v = (t + H) // e
        x = F(H * v, t)
        if x.denominator == n * n:
            out.add((x, v))
    return out


def main():
    P, E, NM = map(int, sys.argv[1:4])
    npairs = nstates = nes = 0
    for p in primerange(5, P + 1):
        if p % 4 != 1:
            continue
        for e in range(3, E + 1, 4):
            H = (p * e + 1) // 4
            facH = factorint(H)
            Hd2 = divisors_from_fac({q: 2 * a for q, a in facH.items()})
            npairs += 1
            for n in range(1, NM + 1):
                A = side_a(p, e, H, n, Hd2) if gcd(n, e) == 1 else set()
                B = side_b(p, e, H, n, facH)
                assert A == B, (p, e, n, A ^ B)
                for (x, v) in A:
                    assert F(1) / x + F(1, v) + F(1, p * H) == F(4, p)
                nstates += len(A)
                if n == 1:
                    nes += len(A)
    print(f"Thm2.1: {npairs} (p,e) pairs (composite e incl.), n<= {NM}: side(a)==side(b) always; {nstates} states, {nes} at n=1")
    # Cor 2.2 for prime e
    nal = ndead = 0
    maxtw = 0
    for p in primerange(5, P + 1):
        if p % 4 != 1:
            continue
        for e in primerange(3, E + 1):
            if e % 4 != 3:
                continue
            H = (p * e + 1) // 4
            facH = factorint(H)
            Hd2 = divisors_from_fac({q: 2 * a for q, a in facH.items()})
            least = None
            for n in range(1, 3 * e + 1):
                if gcd(n, e) == 1 and side_a(p, e, H, n, Hd2):
                    least = n
                    break
            pred = any(kron(s, p) == -1 for s in facH)
            pred_e = any(kron(s, e) == -1 for s in facH)
            assert pred == pred_e, (p, e)
            assert (least is not None) == pred, (p, e, least, facH)
            if least is not None:
                assert least < e
                maxtw = max(maxtw, least)
                nal += 1
            else:
                ndead += 1
            # parity claim: number of p-nonresidue prime factors (with mult.) even
            assert sum(a for s, a in facH.items() if kron(s, p) == -1) % 2 == 0
    print(f"Cor2.2: prime e<= {E}: alive {nal}, dead {ndead}; brute force (n<=3e) == criterion; max least twist {maxtw}")
    # Prop 3.3(b): odd squares
    cnt = 0
    for a in range(3, int(P ** 0.5) + 1, 2):
        N = a * a
        for e in range(3, E + 1, 4):
            if gcd(e, a) != 1:
                continue
            H = (N * e + 1) // 4
            facH = factorint(H)
            Hd2 = divisors_from_fac({q: 2 * b for q, b in facH.items()})
            for n in range(1, NM + 1):
                if gcd(n, e) == 1:
                    assert not side_a(N, e, H, n, Hd2), (N, e, n)
                assert not side_b(N, e, H, n, facH), (N, e, n)
            cnt += 1
    print(f"Prop3.3(b): {cnt} (a^2, e) pairs, n<= {NM}: no state on either side")


if __name__ == "__main__":
    main()
