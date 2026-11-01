# z52d P2 TO8 Z2984: totally positive solutions of (★)-form 4uBC-u-B=p over O_K=Z[√2], u,B in a coefficient box; C in O_K tot.pos.
# Count solutions, split rational (b=0 for u,B,C) vs non-rational; parity of non-rational count.
import sys
p = int(sys.argv[1]); M = int(sys.argv[2])
def mul(x, y): return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def norm(x): return x[0]*x[0] - 2*x[1]*x[1]
def tp(x): return x[0] + x[1]*2**0.5 > 0 and x[0] - x[1]*2**0.5 > 0
def divides_check(num, den):
    # returns C=num/den in O_K if integral else None
    n = norm(den)
    if n == 0: return None
    conj = (den[0], -den[1])
    t = mul(num, conj)
    if t[0] % n or t[1] % n: return None
    return (t[0] // n, t[1] // n)
elems = [(a, b) for a in range(-M, M+1) for b in range(-M, M+1)]
elems = [x for x in elems if tp(x) and x != (0, 0)]
rat = nonrat = 0; sols = []
for u in elems:
    for B in elems:
        num = (p + u[0] + B[0], u[1] + B[1])
        den = mul((4, 0), mul(u, B))
        C = divides_check(num, den)
        if C is None or not tp(C): continue
        if u[1] == 0 and B[1] == 0 and C[1] == 0:
            rat += 1
        else:
            nonrat += 1; sols.append((u, B, C))
print(f"p={p} box M={M}: |elements|={len(elems)} rational sols={rat} non-rational sols={nonrat} parity={nonrat%2}")
for s in sols[:5]: print("  e.g.", s)
