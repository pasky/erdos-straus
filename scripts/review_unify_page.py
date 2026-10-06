"""R60 from-scratch check of the Page-term identity used in CEILINGS_UNIFIED Thm 2.1:
for chi1 a real primitive character mod q1 and (a,q)=1,
  (unit-Haar mass of chi1 on {n = a mod q}) = chi1(a)/phi(q) if q1 | q, else 0.
Computed exactly as the average of chi1(n mod q1) over units n mod lcm(q,q1)
with n = a (q)."""
from math import gcd
from fractions import Fraction
from sympy import totient, factorint
from sympy.ntheory import jacobi_symbol


def kronecker(d, n):
    # Kronecker symbol (d/n) for n>0
    if n == 1:
        return 1
    res = 1
    f = factorint(n)
    for p, e in f.items():
        if p == 2:
            if d % 2 == 0:
                return 0
            v = 1 if d % 8 in (1, 7) else -1
        else:
            v = jacobi_symbol(d % p, p)
        res *= v ** e
    return res


def fundamental_discriminants(B):
    out = []
    for d in range(-B, B + 1):
        if d in (0, 1):
            continue
        if d % 4 == 1:
            m = d
            ok = all(e == 1 for p, e in factorint(abs(m)).items())
        elif d % 4 == 0:
            m = d // 4
            ok = (m % 4 in (2, 3)) and all(e == 1 for p, e in factorint(abs(m)).items())
        else:
            ok = False
        if ok:
            out.append(d)
    return out


def main(Bq1=200, Bq=120):
    checked = 0
    for d in fundamental_discriminants(Bq1):
        q1 = abs(d)
        chi = [kronecker(d, n) if gcd(n, q1) == 1 else 0 for n in range(q1)]
        for q in range(1, Bq + 1):
            Lc = q * q1 // gcd(q, q1)
            phiq = int(totient(q))
            for a in range(q):
                if gcd(a, q) != 1:
                    continue
                s = Fraction(0); cnt = 0
                for n in range(a, Lc, q):
                    if gcd(n, Lc) == 1:
                        s += chi[n % q1]; cnt += 1
                assert cnt * phiq == int(totient(Lc))
                mass = s / int(totient(Lc))  # Haar mass of chi on the class
                pred = Fraction(chi[a % q1], phiq) if q % q1 == 0 else Fraction(0)
                assert mass == pred, (d, q, a, mass, pred)
                checked += 1
    print(f"Page-term Haar identity verified on {checked} (chi1,q,a) cases")


if __name__ == "__main__":
    main()
