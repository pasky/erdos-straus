"""R56 from-scratch check of Lemma 2.1 (atoms) and Lemma 2.2 (Jacobi) in es-subexp-note v4."""
import sys
from sympy import factorint, divisors
from sympy.ntheory import jacobi_symbol, legendre_symbol

def atoms_check(Mmax):
    for M in range(3, Mmax+1, 4):
        A = (M+1)//4
        R = {(-4*D) % M for D in divisors(A*A)}
        S = set()
        for u in divisors(A):
            for v in divisors(A//u):
                S.add((-u*pow(v, -1, M)) % M)
        assert R == S, M
    print("atoms lemma ok up to", Mmax)

def jacobi_check(Mmax):
    natoms = 0
    for M in range(3, Mmax+1, 4):
        A = (M+1)//4
        fM = factorint(M)
        for D in divisors(A*A):
            natoms += 1
            x = (-4*D) % M
            assert jacobi_symbol(x, M) == -1, (M, D)
            fD = factorint(D)
            d = 1
            for q, e in fD.items():
                if e % 2: d *= q
            for l in fM:
                assert (2*D) % l != 0
                if l > 2:
                    assert legendre_symbol((-4*D) % l, l) == legendre_symbol((-d) % l, l)
    print("jacobi lemma ok up to", Mmax, "atoms", natoms)

if __name__ == "__main__":
    atoms_check(int(sys.argv[1]))
    jacobi_check(int(sys.argv[2]))
