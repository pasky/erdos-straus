"""R126 from-scratch symbolic checks for GEOMETRY_ES §2 (toric model, lines) and §3 (fibrations).
Independent of scripts/geo_*.py."""
import sympy as sp

n, t, lam = sp.symbols('n t lam', nonzero=True)
X1, X2, X3 = sp.symbols('X1 X2 X3')
x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3')
u1, u2, u3 = sp.symbols('u1 u2 u3')
S = lambda a, b, c, d: sp.expand(4*b*c*d - n*a*(b*c + b*d + c*d))

# (A) Prop 2.1 via the cubic linear system: phi(X) = (4X1X2X3 : n s X2X3 : n s X1X3 : n s X1X2), s = X1+X2+X3
s = X1 + X2 + X3
phi = (4*X1*X2*X3, n*s*X2*X3, n*s*X1*X3, n*s*X1*X2)
print('(A) phi lands in S_n:', sp.simplify(S(*phi)) == 0)
# affine: u_i = x_i/x0 = n s/(4 X_i), i.e. 1/u_i = 4X_i/(n s) =: s_i, sum s_i = 4/n
print('    sum 1/u_i = 4/n:', sp.simplify(sum(phi[0]/p for p in phi[1:]) - 4/n) == 0)
# base locus of the linear system: common zeros of the 4 cubics
sols = sp.solve([p for p in phi], [X1, X2, X3], dict=True)
print('    base locus (affine cone sols):', sols)
# multiplicity of each base point: min order of vanishing of a general member
def mult(pt):
    # translate pt to origin in an affine chart and compute min total degree among the 4 cubics' lowest terms
    i = [k for k in range(3) if pt[k] != 0][0]
    Xs = [X1, X2, X3]
    y, z = sp.symbols('y z')
    others = [k for k in range(3) if k != i]
    sub = {Xs[i]: 1, Xs[others[0]]: pt[others[0]]/pt[i] + y, Xs[others[1]]: pt[others[1]]/pt[i] + z}
    m = 99
    for p in phi:
        q = sp.Poly(sp.expand(p.subs(sub)), y, z)
        m = min(m, min(sum(mon) for mon in q.monoms()) if not q.is_zero else 99)
    return m
for pt in [(1,0,0),(0,1,0),(0,0,1),(0,1,-1),(1,0,-1),(1,-1,0)]:
    print('    base pt', pt, 'mult', mult(pt))
# each of the 4 lines X_i=0 and s=0 contains exactly 3 base points -> 4 (-2)-curves -> 4 nodes
# image of the line s=0 is the point (1:0:0:0) = P
print('    image of s=0:', [sp.factor(p.subs(X3, -X1-X2)) for p in phi])

# (B) the nine lines lie on S_n
T1, T2 = sp.symbols('T1 T2')
lines = {}
for (i, j) in [(1,2),(1,3),(2,3),(0,1),(0,2),(0,3)]:
    v = [T1, T1, T1, T1]; v[i] = 0; v[j] = 0
    k = [m for m in range(4) if m not in (i, j)]
    v[k[0]] = T1; v[k[1]] = T2
    lines[f'edge{i}{j}'] = v
for k in (1, 2, 3):
    i, j = [m for m in (1, 2, 3) if m != k]
    v = [0]*4; v[0] = 4*T1; v[k] = n*T1; v[i] = T2; v[j] = -T2
    lines[f'M{k}'] = v
print('(B) nine lines on S_n:', all(sp.expand(S(*v)) == 0 for v in lines.values()))
# u_i = -u_j with u1u2u3 != 0 forces u_k = n/4
print('    u1=-u2 =>', sp.factor(S(1, u1, -u1, u3)))

# (C) (F1): u1 = t, X=(4t-n)u2-nt, Y=(4t-n)u3-nt => XY=(nt)^2 on the fibre
eq = S(1, t, u2, u3)
XY = sp.expand(((4*t-n)*u2 - n*t)*((4*t-n)*u3 - n*t) - (n*t)**2)
print('(C) F1: XY-(nt)^2 = (4t-n)*eq/?', sp.simplify(XY/eq))
# (F2): u1 = lam u2, Z=4 lam u2 - n(lam+1), W = 4 lam u3 - n lam, ZW = n^2 lam (lam+1)
eq2 = sp.expand(S(1, lam*u2, u2, u3)/u2)
ZW = sp.expand((4*lam*u2 - n*(lam+1))*(4*lam*u3 - n*lam) - n**2*lam*(lam+1))
print('    F2: ZW-N over residual eq:', sp.simplify(ZW/eq2))
# (F3): 4u1-n = lam(u2+u3): residual conic and its points at infinity
U1 = (n + lam*(u2+u3))/4
eq3 = sp.factor(S(1, U1, u2, u3))
print('    F3 restricted eq:', eq3)
