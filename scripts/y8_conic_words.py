# y8 (goal c): conic point of a chi=+1 word. For w with chi=+1, find primitive z in Z^3, |z|^2 = tp, with z^perp ~ T_w
# (proper or improper; reduced binary forms compared), then l(w) = z mod p in C(F_p): x^2+y^2+z^2 = 0, up to the 48
# signed permutations and scalars. Also h(l) = min of L_l = min{|y|^2/p : y = lambda l mod p, y != 0 mod p}.
import sys
from math import gcd, isqrt
from itertools import permutations, product
from sympy import legendre_symbol as L
def words(p):
    for t in range(1, p+3):
        umax = p+2 if t == 1 else (p+1)//(t-1)
        for u in range(1, umax+1):
            A = t*u-1
            if A > 0 and (p+u) % A == 0: yield t, u, (p+u)//A
def vecs(n):
    r = isqrt(n)
    for a in range(0, r+1):
        m = n-a*a; s = isqrt(m)
        for b in range(-s, s+1):
            c2 = m-b*b; c = isqrt(c2)
            if c*c == c2:
                for cc in {c, -c}: yield (a, b, cc)
def red2(a, b, c):  # reduce binary form a x^2 + 2b xy + c y^2 (Gram [[a,b],[b,c]]) up to GL2(Z)
    while True:
        if c < a: a, c = c, a
        k = round(b/a) if a else 0
        if k == 0:
            return (a, abs(b), c)
        c = c - 2*k*b + k*k*a; b = b - k*a
def perp_gram(z):
    # basis of z^perp in Z^3 via two short integer vectors (lattice kernel by brute small search + gcd reduction)
    x, y, w = z
    import sympy
    M = sympy.Matrix([[x, y, w]]); ns = M.nullspace()
    # integer basis of kernel lattice: use Hermite normal form via sympy
    from sympy.matrices.normalforms import hermite_normal_form
    B = sympy.Matrix.hstack(*[v*sympy.ilcm(*[q.q for q in v]) for v in ns]).T  # 2x3 rational->integer, maybe not saturated
    # saturate: kernel lattice of z is {v : v.z = 0}; compute via extended gcd construction
    g = gcd(x, y)
    if g == 0:
        v1, v2 = (1, 0, 0), (0, 1, 0)
    else:
        # v1 = (y/g, -x/g, 0); v2 completes: need v with v.z = 0 and det condition; solve a*x + b*y = g
        a0, b0 = egcd(x, y)
        v1 = (y//g, -x//g, 0)
        v2 = (a0*w, b0*w, -g)  # (a0 x + b0 y) w - g w = 0
        v2 = tuple(c//gcd(gcd(*v2[:2]), v2[2]) for c in v2) if False else v2
    G = [[sum(p*q for p, q in zip(u, v)) for v in (v1, v2)] for u in (v1, v2)]
    return G
def egcd(a, b):
    if b == 0: return (1 if a >= 0 else -1, 0)
    q, r = divmod(a, b); s, t = egcd(b, r); return (t, s - q*t)
def cross(x, y): return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0])
def canon(l, p):
    best = None
    for perm in permutations(range(3)):
        for sg in product((1, -1), repeat=3):
            v = [sg[i]*l[perm[i]] % p for i in range(3)]
            i0 = next(i for i in range(3) if v[i])
            inv = pow(v[i0], -1, p); v = tuple(c*inv % p for c in v)
            best = v if best is None or v < best else best
    return best
def height(l, p, H):
    for h in range(1, H+1):
        for y in vecs(h*p):
            if gcd(gcd(*y[:2]), y[2]) and any(y[i] % p for i in range(3)):
                # y proportional to l mod p?
                if all((y[i]*l[j]-y[j]*l[i]) % p == 0 for i in range(3) for j in range(3)): return h
    return None
p = int(sys.argv[1]); TMAX = int(sys.argv[2])
from collections import Counter
orb = Counter(); rows = []
for t, u, v in words(p):
    A, As = t*u-1, t*v-1
    if L(A % p, p) != 1 or t > TMAX or u > v: continue
    # R-O217 repair: use a COMPATIBLE embedding (TWO_FIBRES Thm A(iii)): x, y with |x|^2 = A*, |y|^2 = A, x.y = 1
    # and z = x × y = x + y (mod t); an arbitrary z with z^perp ~ T_w need not come from p*G_w (counterexample p=61, (63,1,1)).
    found = None
    VY = list(vecs(A)); VY += [tuple(-c for c in y) for y in VY]
    for x in vecs(As):
        for y in VY:
            if x[0]*y[0]+x[1]*y[1]+x[2]*y[2] != 1: continue
            z = cross(x, y)
            if all((z[i]-x[i]-y[i]) % t == 0 for i in range(3)): found = z; break
        if found: break
    l = canon(found, p) if found else None
    h = height(found, p, t) if found else None
    orb[l] += 1; rows.append((t, u, v, l, h))
for r in rows: print("t,u,v", r[:3], "orbit", r[3], "height(l)", r[4])
print("p", p, "chi=+1 words (u<=v, t<=%d):" % TMAX, len(rows), "distinct conic orbits:", len(orb), "~(p+1)/24 =", (p+1)/24)
