"""fs_lemma_check.py (O216): brute-force test of FF_STERILE_PUSH Lemmas 1.4 (Lenstra) and 1.5 (Coppersmith) over F_p.
For random highly factorable F and random moduli Q, enumerate all monic divisors of F, group them by
(degree, residue mod Q), and compare the largest group with the lemma bounds (class must be a unit mod Q;
the cofactor version needs gcd(F, Q) = 1)."""
import random, sys, itertools
from sympy import Poly, symbols, GF, factor_list
T = symbols('T')

def cop_count(n, D, rho, mmax=60, kmax=200):
    if D < rho: return 1
    X = D - rho; best = 0
    for m in range(1, mmax + 1):
        for k in range(0, kmax + 1):
            det = n*m*(m+1)//2 + X*(m*(m+1)//2 + k*m + k*(k+1)//2)
            if det < (m+k+1)*m*D:
                if not best or m+k < best: best = m+k
                break
            if X*(m+k+1) >= m*D: break
    return best

def bound(n, d, rho, both):
    if d < rho: return 1
    if both and n - d < rho: return 1
    best = 0
    if 3*rho > n: best = 2
    for c in ([cop_count(n, d, rho)] + ([cop_count(n, n-d, rho)] if both else [])):
        if c and (not best or c < best): best = c
    return best

def divisors(F, p):
    fl = factor_list(F.as_expr(), modulus=p)[1]
    facs = [(Poly(f, T, modulus=p), e) for f, e in fl]
    out = []
    for es in itertools.product(*[range(e+1) for _, e in facs]):
        D = Poly(1, T, modulus=p)
        for (f, _), e in zip(facs, es): D = D * f**e
        out.append(D.monic())
    return out

def run(p, trials, seed):
    random.seed(seed)
    lin = [Poly(T - c, T, modulus=p) for c in range(p)]
    irr2 = [Poly(T**2 + a*T + b, T, modulus=p) for a in range(p) for b in range(p)
            if Poly(T**2 + a*T + b, T, modulus=p).is_irreducible]
    tested = viol = 0; tight = 0
    for _ in range(trials):
        F = Poly(1, T, modulus=p)
        for _ in range(random.randint(4, 9)): F = F * random.choice(lin + irr2)
        n = F.degree()
        divs = divisors(F, p)
        for _ in range(3):
            rho = random.randint(1, max(1, n//2))
            Q = Poly([1] + [random.randrange(p) for _ in range(rho)], T, modulus=p)
            both = Q.gcd(F).degree() == 0
            groups = {}
            for Dv in divs:
                r = Dv.rem(Q)
                if Q.gcd(r).degree() != 0 or r.is_zero: continue      # class must be a unit
                key = (Dv.degree(), tuple(r.all_coeffs()))
                groups[key] = groups.get(key, 0) + 1
            for (d, _), c in groups.items():
                b = bound(n, d, rho, both)
                if b:
                    tested += 1
                    if c > b: viol += 1; print("VIOL", p, F, Q, d, c, b)
                    if c == b: tight += 1
    print(f"p={p}: tested {tested} (class, degree) groups with a lemma bound; violations {viol}; tight {tight}")
    return viol

if __name__ == '__main__':
    bad = 0
    for p in [int(x) for x in sys.argv[1].split(',')]:
        bad += run(p, int(sys.argv[2]), 1)
    sys.exit(1 if bad else 0)
