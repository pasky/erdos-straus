"""R260 from-scratch check of ASTRA_BRIDGE Thm 3.1(a)-(d), Thm 3.4, Prop 3.2 (EXPONENT_CAP conventions).

Independent enumerations (do not use the theorem's parametrisation):
 (S) all shot data (Q, g): g = 3 (4) <= G, 1 <= Q <= QM, gcd(Q,p)=1, g | p+4Q^2 (composite g incl.);
     solution per EXPONENT_CAP Sec.1: m=(p+4Q^2)/g, x=(p+m)/4, y=p(g+1)/4, z=p x (g+1)/(4Q^2).
     Q0 = gcd(Q,(g+1)/4), Q1 = Q/Q0, k = (g+1)/(4 Q0).
 (L) all lattice points (2k, Y): k | h, 1 <= Y <= YM, gcd(Y,2k)=1, Y = 2k rho (mod g) for SOME root rho of
     rho^2 = -p (mod g); mapped to Q = (h/k) Y.
 (A) all Astra sources (q, m): q = 3 (4) <= G, 1 <= m <= MM, q | p m^2 + 1, s = (pm^2+1)/q, h=(q+1)/4.
Usage: review_r260_lattice.py P G QM MM
"""
import sys
from fractions import Fraction as F
from math import gcd
from sympy import primerange, factorint


def rad(n):
    return 1 if n == 1 else __import__('math').prod(factorint(n))


def in_esye(pt, p):
    """Return (is integral ES, cap or None) per EXPONENT_CAP Def 1.1 (x,y ints, z rational) for ordered (x,y,z)."""
    x, y, z = pt
    if x.denominator != 1 or y.denominator != 1:
        return None
    d = z.denominator
    if d == 1:
        return 0
    r = int(round(d ** 0.5))
    while r * r > d:
        r -= 1
    while (r + 1) ** 2 <= d:
        r += 1
    if r * r != d or r % 2 == 0 or gcd(r, p) != 1 or int(y) % rad(r) != 0:
        return None
    return max(factorint(r).values())


def main():
    P, G, QM, MM = map(int, sys.argv[1:5])
    st = dict(shots=0, odd=0, even=0, even_sq=0, es=0, lat=0, src=0, even_src=0, ready=0, gen_ready=0,
              slices=0, slice_es=0)
    for p in primerange(5, P + 1):
        if p % 4 != 1:
            continue
        for g in range(3, G + 1, 4):
            if gcd(g, p) != 1:
                continue
            h = (g + 1) // 4
            roots = [r for r in range(g) if (r * r + p) % g == 0]
            if not roots:
                continue
            # (S) shots
            S_odd = {}
            ES_m = set(); ready_m = set()
            for Q in range(1, QM + 1):
                if gcd(Q, p) != 1 or (p + 4 * Q * Q) % g:
                    continue
                m = (p + 4 * Q * Q) // g
                assert (p + m) % 4 == 0
                x = F(p + m, 4); y = F(p * (g + 1), 4); z = p * x * (g + 1) / (4 * Q * Q)
                assert 1 / x + 1 / y + 1 / z == F(4, p)
                st['shots'] += 1
                Q0 = gcd(Q, h); Q1 = Q // Q0; k = h // Q0
                rho = (2 * Q) % g
                if Q1 % 2:
                    st['odd'] += 1
                    assert z.denominator == Q1 * Q1, (p, g, Q)
                    assert (Q1 - rho * 2 * k) % g == 0 and gcd(Q1, 2 * k) == 1
                    # Prop 1.3 D and congruence
                    D = (4 * k * k * p + Q1 * Q1) // g
                    assert D * g == 4 * k * k * p + Q1 * Q1 and (D + Q1 * Q1) % (4 * k) == 0
                    # Thm 3.4(b) ES^{(y,e)} criterion vs definition
                    cap = in_esye((x, y, z), p)
                    crit = (h % rad(Q1) == 0)
                    assert (cap is not None) == crit, (p, g, Q)
                    if crit and Q1 > 1:
                        assert cap == max(factorint(Q1).values())
                    if Q1 == 1:
                        st['es'] += 1
                        assert z.denominator == 1
                        ES_m.add(2 * k)  # Thm 3.1(c) converse: source (g, 2k)
                    S_odd[Q] = (2 * k, Q1, rho)
                else:
                    st['even'] += 1
                    d = z.denominator
                    r = int(round(d ** 0.5))
                    if r * r == d:
                        st['even_sq'] += 1
                    assert r * r == d and r == Q1, (p, g, Q, d, Q1)  # den z = Q1^2 also for even overflow?
            # (L) lattice points, any root
            L = {}
            for k in [d for d in range(1, h + 1) if h % d == 0]:
                for Y in range(1, QM + 1):
                    if gcd(Y, 2 * k) != 1:
                        continue
                    for rho in roots:
                        if (Y - 2 * k * rho) % g == 0:
                            Q = (h // k) * Y
                            if Q <= QM and gcd(Q, p) == 1:
                                assert (2 * Q - rho) % g == 0  # shot is in branch rho
                                L[Q] = (2 * k, Y, rho)
            assert set(L) == set(S_odd), (p, g, set(L) ^ set(S_odd))
            for Q in L:
                assert L[Q] == S_odd[Q]
            st['lat'] += len(L)
            # Prop 3.2: ES at slice y = ph by brute force over divisors d | (ph)^2
            ph = p * h
            fac = factorint(ph)
            ds = [1]
            for qq, a in fac.items():
                ds = [d * qq ** i for d in ds for i in range(2 * a + 1)]
            slice_es = any((d + ph) % g == 0 for d in ds)
            st['slices'] += 1
            st['slice_es'] += slice_es
            # (A) sources
            for mm in range(1, MM + 1):
                if (p * mm * mm + 1) % g:
                    continue
                s = (p * mm * mm + 1) // g
                A = s * h
                assert F(mm * mm, A) + F(1, p * A) + F(1, p * h) == F(4, p)
                assert 4 * A - p * mm * mm == s + 1
                assert any((1 - r * mm) % g == 0 for r in roots)  # (m,1) in L_rho
                # -ph = Q^2 (mod g) for Q = (2m)^-1  (Prop 3.2)
                Qr = pow(2 * mm, -1, g)
                assert (ph + Qr * Qr) % g == 0
                st['src'] += 1
                genuine = gcd(mm, h) == 1
                if mm % 2 == 0:
                    st['even_src'] += 1
                    ready = (s + 1) % (2 * mm) == 0
                    assert ready == ((2 * h) % mm == 0) == ((g + 1) % (2 * mm) == 0)
                    if ready:
                        st['ready'] += 1
                        if gcd(h // (mm // 2), p) == 1:
                            ready_m.add(mm)
                        k = mm // 2; Q0 = h // k
                        assert slice_es or gcd(Q0, p) != 1
                        if gcd(Q0, p) == 1:
                            assert (p + 4 * Q0 * Q0) % g == 0
                            mw = (p + 4 * Q0 * Q0) // g
                            x = F(p + mw, 4); y = F(p * h); z = p * x * 4 * h / (4 * Q0 * Q0)
                            assert z.denominator == 1 and 1 / x + 1 / y + 1 / z == F(4, p)
                            # Prop 1.3 D equals Astra s
                            jj = (mw + p) // Q0
                            assert k * jj - 1 == s
                        if genuine:
                            st['gen_ready'] += 1
                            assert mm == 2
            # ES shots (Q1=1, Q=h/k<=QM) <-> ES-ready sources (m=2k<=MM), compared on common range
            lo = lambda mm_: mm_ <= MM and (2 * h) // mm_ <= QM
            assert {x_ for x_ in ES_m if lo(x_)} == {x_ for x_ in ready_m if lo(x_)}, (p, g, ES_m, ready_m)
    print(st)


if __name__ == "__main__":
    main()
