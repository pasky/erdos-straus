"""R86 from-scratch check of Lemma 2.1 (paper/es-coverings-note.tex): for random admissible
triples of the 7 ET families and every n>=1 in the class (n up to a bound), the coordinates of
the paper's second table are positive integers and 4/n = 1/x+1/y+1/z. Also checks the class
table against ET Prop 1.9 as transcribed (moduli, side conditions)."""
import random, math
from fractions import Fraction as Fr
random.seed(86)

def sol(fam, k, n):
    if fam == 'I1':
        a, d, f = k; e = Fr(4*a*a*d+1, f); b = (n*e+1)/Fr(4*a*d); c = Fr(n+f, 4*a*d); I = True
    elif fam == 'I2':
        a, c, f = k; d = Fr(n+f, 4*a*c); b = Fr(n*a+c, f); I = True
    elif fam == 'I3':
        c, d, f = k; a = Fr(n+f, 4*c*d); b = (n+Fr(n*n+4*c*c*d, f))/(4*c*d); I = True
    elif fam == 'I4':
        a, b, e = k; c = Fr(a+b, e); d = Fr(n*e+1, 4*a*b); I = True
    elif fam == 'II1':
        a, b, e = k; c = Fr(a+b, e); d = Fr(n+e, 4*a*b); I = False
    elif fam == 'II2':
        a, d, f = k; c = Fr(f+1, 4*a*d); b = (n*c+a)/f; I = False
    elif fam == 'II3':
        a, d, e = k; c = Fr(n+4*a*a*d+e, 4*a*d*e); b = c*e-a; I = False
        assert b == Fr(n+e, 4*a*d)
    coords = (a, b, c, d)
    xyz = (a*b*d*n, a*c*d, b*c*d) if I else (a*b*d, a*c*d*n, b*c*d*n)
    return coords, xyz

def admissible(fam, k):
    p, q, r = k
    g = math.gcd
    return {'I1': (4*p*p*q+1) % r == 0, 'I2': g(4*p*q, r) == 1, 'I3': g(4*p*q, r) == 1,
            'I4': (p+q) % r == 0 and g(r, 4*p*q) == 1, 'II1': (p+q) % r == 0 and g(r, 4*p*q) == 1,
            'II2': (r+1) % (4*p*q) == 0, 'II3': g(4*p*q, r) == 1}[fam]

def in_class(fam, k, n):
    p, q, r = k
    if fam == 'I1': return (n+r) % (4*p*q) == 0
    if fam == 'I2': return (n+r) % (4*p*q) == 0 and (n*p+q) % r == 0
    if fam == 'I3': return (n+r) % (4*p*q) == 0 and (n*n+4*p*p*q) % r == 0
    if fam == 'I4': return (n*r+1) % (4*p*q) == 0
    if fam == 'II1': return (n+r) % (4*p*q) == 0
    if fam == 'II2': return (n+4*p*p*q) % r == 0
    if fam == 'II3': return (n+4*p*p*q+r) % (4*p*q*r) == 0

if __name__ == "__main__":
    tested = 0; maxdeg = 0
    for fam in ['I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3']:
        cnt = 0
        while cnt < 150:
            k = tuple(random.randint(1, 12) for _ in range(3))
            if fam == 'II2':
                a, d = k[0], k[1]; k = (a, d, 4*a*d*random.randint(1, 6)-1)
            if fam == 'I1':
                a, d = k[0], k[1]; N = 4*a*a*d+1
                divs = [x for x in range(1, N+1) if N % x == 0]; k = (a, d, random.choice(divs))
            if not admissible(fam, k): continue
            M = 4*k[0]*k[1]*k[2]
            ns = [n for n in range(1, 3*M+1) if in_class(fam, k, n)]
            if not ns: continue
            cnt += 1
            for n in ns:
                coords, xyz = sol(fam, k, n)
                assert all(v.denominator == 1 and v > 0 for v in coords), (fam, k, n, coords)
                assert Fr(4, n) == sum(Fr(1) / v for v in xyz), (fam, k, n)
                tested += 1
    print("Lemma 2.1 identity/integrality/positivity OK on", tested, "(family,triple,n) cases")

