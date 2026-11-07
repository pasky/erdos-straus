"""Verify: S_p={(a,c): ac | p+a+c}, N_p={(a,D): a|D+1, D|p+a}, L_p={(g,D): g|D+1, D|pg+1};
 K:(a,c)->(a,(p+a)/c) bijection S_p->N_p; J:(a,D)->((D+1)/a, D) bijection N_p->L_p;
 iota:(g,D)->(g,(pg+1)/D) involution on L_p with unique fixed point (p+2,p+1);
 J K swap K J = iota.  Also Jacobi: for 4|g elements of U_II: (ga-1 / p) = -1 ; for U_I: (g/4 / p) = -1."""
import sys
sys.path.insert(0,'scripts')
from sympy import primerange, legendre_symbol
from z62_parityf_universal import U_II, U_I

def Sp(p):
    return {(a,c) for a in range(1,p+3) for c in range(1,2*p+3) if (p+a+c) % (a*c) == 0}
def Np(p):
    return {(a,D) for D in range(1,2*p+3) for a in range(1,D+2) if (D+1) % a == 0 and (p+a) % D == 0}
def Lp(p):
    return {(g,D) for D in range(1,p*(p+3)) for g in range(1,p+3) if (D+1) % g == 0 and (p*g+1) % D == 0}

for p in primerange(5, 60):
    if p % 4 != 1: continue
    S, N, L = Sp(p), Np(p), Lp(p)
    K = {(a,c): (a,(p+a)//c) for (a,c) in S}
    assert set(K.values()) == N and len(K) == len(S), p
    J = {(a,D): ((D+1)//a, D) for (a,D) in N}
    assert set(J.values()) == L and len(J) == len(N), p
    iota = {(g,D): (g,(p*g+1)//D) for (g,D) in L}
    assert set(iota.values()) == L
    fix = [x for x in L if iota[x] == x]
    assert fix == [(p+2,p+1)], (p, fix)
    # composite J K swap K^-1 J^-1 == iota ? (K,J are bijections; K^-1 = K on N->S? K is its own inverse as map on pairs)
    Kinv = {v:k for k,v in K.items()}; Jinv = {v:k for k,v in J.items()}
    for (g,D) in L:
        (a,Dn) = Jinv[(g,D)]; (a2,c) = Kinv[(a,Dn)]; (c2,a3) = (c,a2)  # swap
        img = J[K[(c2,a3)]]
        assert img == iota[(g,D)], (p, (g,D), img, iota[(g,D)])
    assert len(S) % 2 == 1
    # Jacobi
    for (g,a,b,c) in U_II(p):
        if g % 4 == 0:
            assert legendre_symbol((g*a*c-1) % p, p) == -1 and legendre_symbol((g*b*c-1) % p, p) == -1, (p,g,a,b,c)
    for (g,a,b,c) in U_I(p):
        if g % 4 == 0:
            assert legendre_symbol((g//4) % p, p) == -1, (p,g,a,b,c)
    print(p, "ok |S|=%d" % len(S))
