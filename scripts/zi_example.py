"""zi_example.py (O244): explicit ET-I4 analogue solutions over F_3[T], A = T^2, and their E_FF = A*X_min - P."""
import sys
from zi_lib import *
p = 3; A = T(2)
found = 0
for da in range(0, 2):
    for db in range(da + 1, 3):
        for a in monics(da, p):
            for b in monics(db, p):
                s = add(a, b, p)
                for de in range(1, deg(s) + 1):
                    for E in monics(de, p):
                        c = exact(s, E, p)
                        if c is None or len(gcd(E, mul(T(1), mul(a, b, p), p), p)) != 1: continue
                        M = mul(A, mul(a, b, p), p)
                        # find irreducible P, deg 6, with M | P*E + 1
                        for P in monics(6, p):
                            if mod(add(mul(P, E, p), [1], p), M, p) or not is_irred(P, p): continue
                            d = exact(add(mul(P, E, p), [1], p), M, p)
                            X1 = mul(mul(a, b, p), mul(d, P, p), p); X2 = mul(a, mul(c, d, p), p); X3 = mul(b, mul(c, d, p), p)
                            # identity A*X1*X2*X3 == P*(X1X2+X2X3+X3X1)
                            lhs = mul(A, mul(X1, mul(X2, X3, p), p), p)
                            rhs = mul(P, add(add(mul(X1, X2, p), mul(X2, X3, p), p), mul(X3, X1, p), p), p)
                            ok = lhs == rhs
                            mon = [lc(x) for x in (X1, X2, X3)]
                            Xmin = min((X1, X2, X3), key=deg)
                            EFF = sub(mul(A, Xmin, p), P, p)
                            print(f"a={show(a)} b={show(b)} E={show(E)} P={show(P)} ok={ok} lcs={mon} degs={[deg(x) for x in (X1,X2,X3)]} E_FF={show(EFF)} degE_FF={deg(EFF)}")
                            found += 1
                            break
                        if found >= 12: sys.exit()
