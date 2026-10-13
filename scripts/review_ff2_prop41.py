"""R166: from-scratch exhaustive check of O140 Prop 4.1 (as used in O166 Prop 1.1) for small data:
no linear family (E; t_a, a0; t_b, b0) is valid at a monic P = 1 (mod W_F), W_F = A*monic(E)*lcm(a0,b0),
deg P > n_F. Validity = A|P+E, a0|X, b0|X, s=a+b != 0, E | s, lc(s) = lc(E) (FUNCTIONFIELD_ES §6.2).
Uses P = 1 + W_F*T^m (validity is a congruence condition for n >= n_F; irreducibility is not needed).
usage: review_ff2_prop41.py p A(low-first) maxdeg_a0b0 maxdegE"""
import sys
from review_ff2_poly import *

p = int(sys.argv[1]); setp(p)
A = tr([int(x) for x in sys.argv[2].split(',')])
ma, me = int(sys.argv[3]), int(sys.argv[4])
k = deg(A)
mons = list(monics_upto(ma))
nfam = nvalid = 0
viol = []
for dE in monics_upto(me):
    for lam in range(1, p):
        E = scal(lam, dE)
        for i, a0 in enumerate(mons):
            for b0 in mons[i:]:
                g = egcd(a0, b0)[0]
                L = dm(mul(a0, b0), g)[0]
                W = mul(mul(A, dE), L)
                nF = 1 + max(k + deg(a0) + deg(b0), deg(E))
                for extra in (0, 1):
                    m = max(nF - deg(W), 0) + 1 + extra
                    P = add((1,), mul(W, Tpow(m)))
                    X, r = dm(add(P, E), A)
                    if r or not divides(a0, X) or not divides(b0, X):
                        continue
                    def term(t, c):
                        return [c, mul(P, c), dm(X, c)[0], mul(P, dm(X, c)[0])][t]
                    for ta in range(4):
                        for tb in range(4):
                            nfam += 1
                            s = add(term(ta, a0), term(tb, b0))
                            if s and s[-1] == E[-1] and divides(E, s):
                                nvalid += 1
                                viol.append((E, ta, a0, tb, b0, deg(P)))
print("p", p, "A", A, "family-instances tested", nfam, "valid at P=1 mod W_F:", nvalid)
for v in viol[:20]:
    print(v)
