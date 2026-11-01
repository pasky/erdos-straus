"""Z0323: k=4 monic FF Egyptian: T/P = 1/X1+1/X2+1/X3+1/X4 over F_5[T] (A=T), vs the 3-term engine.
Search (sufficient, not complete): X1<=X2 monic of degree <= DEG (default n-1); remainder R = T/P-1/X1-1/X2 = N/D with
D = P X1 X2, N = T X1 X2 - P(X1+X2); then 2-term completion (complete for that pair) by divisors of D^2 (as in Z0047).
Reports: for each irreducible P (T∤P) of degree n: 3-term engine verdict and 4-term verdict; the 3-term failures and whether 4 terms fix them.
Usage: python3 scripts/z52d_p2_NC0_Z0323.py NMAX [DEG-offset]"""
import sys, itertools, time
sys.path.insert(0, 'scripts')
import bs_ff_es as E
E.Q = 5
Q = 5
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
A = (0, 1)
sys.argv_saved = sys.argv
import z52d_p2_NC0_Z0047 as Z47   # reuse solve_two_term (Z0047 module; its __main__ block is not executed)
E.Q = Q  # Z0047 import sets E.Q=3; restore
Z47.E = E; Z47.Q = Q

def monic_upto(d):
    out = []
    for k in range(0, d + 1):
        out += [tuple(low) + (1,) for low in itertools.product(range(Q), repeat=k)]
    return out

def four_term(P, deg):
    n = len(P) - 1
    cands = monic_upto(deg)
    for i, X1 in enumerate(cands):
        for X2 in cands[i:]:
            N = E.sub(E.mul(A, E.mul(X1, X2)), E.mul(P, E.add(X1, X2)))
            if not N:
                continue
            D = E.mul(P, E.mul(X1, X2))
            for Y, Z in Z47.solve_two_term(N, D):
                lhs = E.mul(A, E.mul(X1, E.mul(X2, E.mul(Y, Z))))
                rhs = E.mul(P, E.add(E.add(E.mul(X1, X2), E.mul(X1, Y)), E.add(E.mul(X1, Z), E.mul(X2, Y)))) 
                # identity check for 4 terms: T/P = sum 1/X_i  <=> T*prod(X) = P*(sum of triple products)
                e4 = E.add(E.add(E.mul(X1, E.mul(X2, Y)), E.mul(X1, E.mul(X2, Z))), E.add(E.mul(X1, E.mul(Y, Z)), E.mul(X2, E.mul(Y, Z))))
                assert E.mul(A, E.mul(X1, E.mul(X2, E.mul(Y, Z)))) == E.mul(P, e4)
                return (X1, X2, Y, Z)
    return None

t0 = time.time()
for n in range(2, NMAX + 1):
    irr = [p for p in E.irreducibles(n) if E.divmod_(p, A)[1]]
    f3 = [p for p in irr if next(E.es_solutions(A, p), None) is None]
    deg = n - 1
    res = []
    for p in f3:
        s4 = four_term(p, deg)
        res.append((p, s4))
    fixed = sum(1 for _, s in res if s is not None)
    print(f"n={n}: irreducible={len(irr)} 3-term failures={len(f3)} ; 4-term (X1,X2 deg<={deg}) solves {fixed} of them  t={time.time()-t0:.1f}s", flush=True)
    for p, s in res:
        print("   3-term-fail P=", list(p), " 4-term witness (X1,X2,Y,Z)=", s, flush=True)
