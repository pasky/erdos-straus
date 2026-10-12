"""R162 from-scratch check of INVOLUTION_ES2 Lemma 4.1(c,d)/Lemma 5.1 => Thm 5.3 mechanism on cylinders,
and of Remark 3 ({t=u}: q, 12q+1, 24q+1 prime => E(p) ∩ {t=u} = ∅).

For p = 24q+1 prime, p <= PMAX: enumerate E(p) by brute force; for each cylinder W, compute R_W(p) directly
(R_f(n) = n^{deg_T f} f(-1/n,-n); t-cylinders R1*R2), the QR property "every prime l != p of R_W(p) is a
square mod p", and check QR => E(p) ∩ W = ∅.  Usage: ... review_inv2_cyl.py PMAX
"""
import sys
from fractions import Fraction
from sympy import isprime, factorint, legendre_symbol
from review_inv2_lemmas import E

# cylinders: (name, kind, membership test, R(n) as python function)
def Rf(f, degT):
    return lambda n: int(Fraction(n) ** degT * f(Fraction(-1, n), Fraction(-n)))

CYL = [
    ("t=u", lambda t, u, v: t == u, Rf(lambda T, U: T - U, 1)),
    ("t=3", lambda t, u, v: t == 3, Rf(lambda T, U: T - 3, 1)),
    ("t=7", lambda t, u, v: t == 7, Rf(lambda T, U: T - 7, 1)),
    ("u=3", lambda t, u, v: u == 3, Rf(lambda T, U: U - 3, 0)),
    ("u=t^2+2", lambda t, u, v: u == t * t + 2, Rf(lambda T, U: U - T * T - 2, 2)),
    ("u=3t+2", lambda t, u, v: u == 3 * t + 2, Rf(lambda T, U: U - 3 * T - 2, 1)),
    ("tu=u+2t+... (u(t-1)=2t+5)", lambda t, u, v: u * (t - 1) == 2 * t + 5, Rf(lambda T, U: U * (T - 1) - 2 * T - 5, 1)),
    ("v=2t+1 (B-side)", lambda t, u, v: v == 2 * t + 1, Rf(lambda T, U: U - 2 * T - 1, 1)),
    ("v=5", lambda t, u, v: v == 5, lambda n: (5 + n) * 5),    # g=V-5: R1=g(0,-n)=-n-5, R2=g(-n,0)=-5
    ("v=u+6", lambda t, u, v: v == u + 6, lambda n: (n - 6) * (n + 6)),  # g=V-U-6: R1=-n-6, R2=n-6
    ("uv=3u+4v", lambda t, u, v: u * v == 3 * u + 4 * v, lambda n: (4 * n) * (3 * n)),  # g=UV-3U-4V: R1=4n, R2=3n
]

def qr(Rv, p):
    if Rv == 0:
        return None
    for l in factorint(abs(Rv)):
        if l != p and l != 2 and legendre_symbol(l % p, p) != 1:
            return False
    return True

def main(PMAX):
    stats = {c[0]: [0, 0, 0] for c in CYL}  # [#QR, #QR&nonempty, #nonempty]
    nprimes = 0; rem3 = [0, 0]
    for q in range(1, (PMAX - 1) // 24 + 1):
        p = 24 * q + 1
        if not isprime(p):
            continue
        nprimes += 1
        Ep = E(p)
        for name, mem, R in CYL:
            hit = any(mem(*x) for x in Ep)
            Q = qr(R(p), p)
            st = stats[name]
            st[0] += bool(Q); st[1] += bool(Q and hit); st[2] += hit
            if Q and hit:
                print("COUNTEREXAMPLE", name, p, [x for x in Ep if mem(*x)])
        if isprime(q) and isprime(12 * q + 1):
            rem3[0] += 1
            rem3[1] += any(x[0] == x[1] for x in Ep)
    print(f"{nprimes} primes p=24q+1 <= {PMAX}")
    for name, st in stats.items():
        print(f"  {name:28s} QR at {st[0]:4d}, QR&nonempty {st[1]}, nonempty {st[2]}")
    print(f"Remark 3: {rem3[0]} q with q,12q+1,24q+1 prime; E∩{{t=u}} nonempty at {rem3[1]} of them")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 10000)
