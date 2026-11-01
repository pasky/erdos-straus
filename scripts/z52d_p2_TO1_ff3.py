# z52d pass2 TO1 (Z0322): brute-force FF Erdos-Straus test over F_3[T]: is A/P = 1/X + 1/Y + 1/Z solvable with X,Y,Z monic,
# for numerators A in {T^2, T^2+1, T^2+T+2} and monic P of degree 1..dmaxP. Bounded search: deg X, deg Y <= deg P + deg A + 1,
# Z determined as the reciprocal of A/P - 1/X - 1/Y (must be a monic polynomial). Exact over F_3. Not the bs_ff_es.py procedure
# (that one requires char >= 5).  usage: python3 scripts/z52d_p2_TO1_ff3.py dmaxP
import sys, itertools, json
Q = 3
def trim(a):
    a = list(a)
    while a and a[-1] % Q == 0: a.pop()
    return [x % Q for x in a]
def add(a, b):
    n = max(len(a), len(b)); return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])
def neg(a): return trim([-x for x in a])
def mul(a, b):
    if not a or not b: return []
    r = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] = (r[i+j] + x*y) % Q
    return trim(r)
def divmod_(a, b):
    a = trim(a); b = trim(b); q = [0]*max(0, len(a)-len(b)+1)
    inv = pow(b[-1], Q-2, Q)
    while len(a) >= len(b) and a:
        c = (a[-1]*inv) % Q; k = len(a)-len(b); q[k] = c
        a = trim([ (a[i] if i < len(a) else 0) - (c*b[i-k] if 0 <= i-k < len(b) else 0) for i in range(max(len(a), k+len(b)))])
    return trim(q), a
def gcd(a, b):
    a = trim(a); b = trim(b)
    while b: a, b = b, divmod_(a, b)[1]
    if not a: return []
    inv = pow(a[-1], Q-2, Q); return [(x*inv) % Q for x in a]
def frac_sub(n1, d1, n2, d2):   # n1/d1 - n2/d2
    return add(mul(n1, d2), neg(mul(n2, d1))), mul(d1, d2)
def reduce_frac(n, d):
    g = gcd(n, d)
    if not g or len(g) == 1: return trim(n), trim(d)
    return divmod_(n, g)[0], divmod_(d, g)[0]
def monic_polys(maxdeg):
    for k in range(0, maxdeg+1):
        for coeffs in itertools.product(range(Q), repeat=k):
            yield list(coeffs) + [1]
def solvable(A, P, dX):
    n_sol = 0; ex = None
    Xs = [X for X in monic_polys(dX) if X]
    for X in Xs:
        n1, d1 = frac_sub(A, P, [1], X)              # A/P - 1/X
        for Y in Xs:
            n2, d2 = frac_sub(n1, d1, [1], Y)
            n2, d2 = reduce_frac(n2, d2)
            if not n2: continue
            # need 1/Z = n2/d2 with Z monic polynomial: numerator must be a nonzero constant c, Z = d2/c monic
            if len(n2) != 1: continue
            c = n2[0]; Z = [(x*pow(c, Q-2, Q)) % Q for x in d2]
            if Z and Z[-1] == 1:
                n_sol += 1
                if ex is None: ex = (X, Y, Z)
    return n_sol, ex
dmaxP = int(sys.argv[1]) if len(sys.argv) > 1 else 4
res = {}
As = {'T^2': [0,0,1], 'T^2+1': [1,0,1], 'T^2+T+2': [2,1,1]}
for name, A in As.items():
    rows = []
    for dP in range(1, dmaxP+1):
        for Pc in monic_polys(0) if False else [list(c)+[1] for c in itertools.product(range(Q), repeat=dP)]:
            if Pc[0] == 0: continue  # skip T | P (keeps the search about units at T)
            dX = dP + len(A) - 1 + 1
            n_sol, ex = solvable(A, Pc, min(dX, dP+2))
            rows.append((dP, Pc, n_sol > 0))
    unsolved = [r[1] for r in rows if not r[2]]
    res[name] = dict(n_P=len(rows), unsolved_count=len(unsolved), unsolved_first=[ ''.join(str(x) for x in P) for P in unsolved[:12]])
print(json.dumps(res, indent=1))
