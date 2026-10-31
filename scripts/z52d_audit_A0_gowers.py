# z52d audit A0, item Z2591: Gowers/Nikolov–Pyber criterion |A||B||C| > |G|^3/m for ES5 letter sets mod q,
# and the actual image size of {S(a)S(b)S(c)} in SL2(F_q), S(a) = [[a,-1],[1,0]] (minus-CF letters).
def mul(X, Y, q):
    return ((X[0]*Y[0]+X[1]*Y[2]) % q, (X[0]*Y[1]+X[1]*Y[3]) % q, (X[2]*Y[0]+X[3]*Y[2]) % q, (X[2]*Y[1]+X[3]*Y[3]) % q)
for q in [p for p in range(3, 50) if all(p % d for d in range(2, p))]:
    G = q*(q*q-1); m = (q-1)//2 if q > 3 else 1
    S = [(a, q-1, 1, 0) for a in range(q)]           # |A| = |B| = |C| = q (reduction of any integer letter range)
    img = {mul(mul(x, y, q), z, q) for x in S for y in S for z in S}
    traces = {(t[0]+t[3]) % q for t in img}
    lhs, rhs = q**3, G**3/m
    print(f"q={q:2d} |G|={G:6d} |A||B||C|={lhs:7d} |G|^3/m={rhs:.3g} ratio={lhs/rhs:.2e} |ABC|={len(img)} "
          f"missing={G-len(img)} (pred q(q-2)={q*(q-2)}) all_traces={len(traces)==q}")
