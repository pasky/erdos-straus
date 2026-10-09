"""Complete witness search at a node (task O100): all ET classes whose modulus divides L (no size cap).

witness_all(x, L, fams=None) -> list of (fam, P) of classes with modulus M | L that contain the whole
progression x + L*Z (i.e. x mod M is a class residue).  Complete by the following reductions
(POINTWISE_MORDELL13C §2):
  pairs (a,d) with 4ad | L, K = L/(4ad), Kc = part of K coprime to 4ad;
  I1 (a,d,f), f | N=4a^2d+1, f = -x (4ad):  f = (-x mod 4ad) or N/g with g = (-1/x mod 4ad)
     (if f > 4ad then g = N/f <= a < 4ad);
  II1/I4 (a,b,e): e | a+b < 4ab, so e = (-x mod 4ab) resp. (-1/x mod 4ab);
  II3 (a,d,e): e | gcd(Kc, x+4a^2d), e = -x (4ad);   I2 (a,c,f): f | gcd(Kc, a x + c), f = -x (4ac);
  I3 (c,d,f): f | gcd(Kc, x^2+4c^2d), f = -x (4cd);
  II2 (a,d,f): f | L odd, f = 3 (4), a | A=(f+1)/4, d = -x/(4a^2) mod f (d <= A/a < f), d | A/a.
"""
from math import gcd
from sympy import factorint


def divs_from_fac(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds


def divs(n):
    return divs_from_fac(factorint(n)) if n > 1 else [1]


def coprime_part(K, m):
    g = gcd(K, m)
    while g > 1:
        K //= g
        g = gcd(K, m)
    return K


def witness_all(x, L, fams=None, first=True):
    out = []
    def add(fam, P):
        out.append((fam, P))
        return first
    F = factorint(L)
    if F.get(2, 0) < 2:
        return out
    F4 = dict(F); F4[2] -= 2
    Q = L // 4
    DQ = sorted(divs_from_fac(F4))
    want = (lambda f: True) if fams is None else (lambda f: f in fams)
    for a in DQ:
        for d in DQ:
            if (Q // a) % d:
                continue
            m = 4 * a * d
            K = L // m
            xm = x % m
            if gcd(xm, m) != 1:
                continue
            ix = pow(xm, -1, m)
            # I1 (a,d,f)
            if want('I1'):
                N = 4 * a * a * d + 1
                f0 = (-xm) % m
                if N % f0 == 0 and add('I1', (a, d, f0)):
                    return out
                g0 = (-ix) % m
                if N % g0 == 0 and add('I1', (a, d, N // g0)):
                    return out
            # II1 / I4 (a,b=d,e)
            for fam, e in (('II1', (-xm) % m), ('I4', (-ix) % m)):
                if want(fam) and (a + d) % e == 0 and gcd(e, m) == 1 and add(fam, (a, d, e)):
                    return out
            Kc = coprime_part(K, m)
            for fam, val in (('II3', x + 4 * a * a * d), ('I2', a * x + d), ('I3', x * x + 4 * a * a * d)):
                if not want(fam):
                    continue
                G = gcd(Kc, val)
                for f in divs(G):
                    if (f + xm) % m == 0 and add(fam, (a, d, f)):
                        return out
    if want('II2'):
        Fo = {p: e for p, e in F.items() if p != 2}
        for f in divs_from_fac(Fo):
            if f % 4 != 3:
                continue
            A = (f + 1) // 4
            xf = x % f
            for a in divs(A):
                if gcd(a, f) != 1:
                    continue
                d = (-xf * pow(4 * a * a, -1, f)) % f
                if d and (A // a) % d == 0 and add('II2', (a, d, f)):
                    return out
    return out


if __name__ == '__main__':
    import sys
    x, L = int(sys.argv[1]), int(sys.argv[2])
    print(witness_all(x, L, first=False))
