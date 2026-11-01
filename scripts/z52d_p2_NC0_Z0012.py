"""Z0012: ES over the coordinate ring A = F_5[E minus O] of E: y^2 = x^3 + x + 1 (smooth over F_5), numerator 4.
Elements u + v*y (u,v in F_5[x]); y^2 = f(x). Pole order at O: ord = max(2 deg u, 2 deg v + 3). A^* = F_5^*.
Norm N(u+vy) = u^2 - v^2 f in F_5[x]; deg N = ord. Principal prime (heuristic test, documented): pi with N(pi) irreducible
(then (pi) is prime; we also require pi nonunit). Only these principal primes are enumerated (inert-type primes with N = g^2 are missed).
ES search: 4/P = 1/X + 1/Y + 1/Z with X,Y,Z in A\{0}, all with ord <= MX.  Enumerate X,Y (all, including scalars), solve Z exactly:
Z = P X Y / (4XY - P(X+Y)), tested for membership in A by norm division.
Usage: python3 scripts/z52d_p2_NC0_Z0012.py MP MX"""
import sys, itertools, time, collections
sys.path.insert(0, 'scripts')
import bs_ff_es as E
Q = 5
E.Q = Q
F = (1, 1, 0, 1)  # f(x) = x^3 + x + 1 (low->high)
MP = int(sys.argv[1]) if len(sys.argv) > 1 else 3
MX = int(sys.argv[2]) if len(sys.argv) > 2 else 4

def pad(p): return E.trim(p)
def emul(a, b):
    u, v = a; c, d = b
    return (E.trim(E.add(E.mul(u, c), E.mul(E.mul(v, d), F))), E.trim(E.add(E.mul(u, d), E.mul(v, c))))
def eadd(a, b): return (E.add(a[0], b[0]), E.add(a[1], b[1]))
def esc(k, a): return (E.trim([(k * x) % Q for x in a[0]]), E.trim([(k * x) % Q for x in a[1]]))
def enorm(a): return E.sub(E.mul(a[0], a[0]), E.mul(E.mul(a[1], a[1]), F))
def eord(a):
    o = 0
    if a[0]: o = max(o, 2 * (len(a[0]) - 1))
    if a[1]: o = max(o, 2 * (len(a[1]) - 1) + 3)
    return o
def is_zero(a): return not a[0] and not a[1]
def lead(a):
    """leading coefficient at the pole order: from u if 2deg u > 2deg v + 3, else from v."""
    if not a[0] and not a[1]: return 0
    du = 2 * (len(a[0]) - 1) if a[0] else -1
    dv = 2 * (len(a[1]) - 1) + 3 if a[1] else -1
    return a[0][-1] if du > dv else a[1][-1]
def normal(a): return lead(a) == 1
def divides_A(D, N):
    """return quotient N/D in A if it lies in A, else None. D != 0."""
    Dn = enorm(D)
    if not Dn: return None
    conjD = (D[0], E.trim([(-x) % Q for x in D[1]]))
    m = emul(N, conjD)
    q0, r0 = E.divmod_(m[0], Dn)
    q1, r1 = E.divmod_(m[1], Dn)
    if r0 or r1: return None
    return (q0, q1)
def all_elems(M):
    """all nonzero elements with ord <= M (not up to scalar)."""
    out = []
    polys_u = [p for d in range(0, M // 2 + 1) for p in [tuple(l) + (1,) for l in itertools.product(range(Q), repeat=d)]] + [()]
    polys_v = [p for d in range(0, max(0, (M - 3) // 2) + 1) for p in [tuple(l) + (1,) for l in itertools.product(range(Q), repeat=d)]] + [()]
    for u in polys_u:
        for v in polys_v:
            # scalars handled by including all leading coefficients
            pass
    # all coefficient vectors (not just monic): enumerate by degree bound
    ulist = [tuple(l) for d in range(0, M // 2 + 1) for l in itertools.product(range(Q), repeat=d + 1)]
    ulist = [E.trim(l) for l in ulist]
    vlist = [tuple(l) for d in range(0, max(0, (M - 3) // 2) + 1) for l in itertools.product(range(Q), repeat=d + 1)] if M >= 3 else [()]
    vlist = [E.trim(l) for l in vlist]
    ulist = list(dict.fromkeys(ulist)); vlist = list(dict.fromkeys(vlist))
    for u in ulist:
        for v in vlist:
            a = (u, v)
            if is_zero(a): continue
            if eord(a) <= M: out.append(a)
    return out

def irreducible_poly(g):
    d = len(g) - 1
    if d <= 0: return False
    return E.is_irred(g)

def principal_primes(M):
    """pi (up to F_5^* scalars, leading coefficient normalised) with N(pi) irreducible and ord <= M."""
    out = []
    seen = set()
    for a in all_elems(M):
        n = enorm(a)
        if len(n) - 1 < 1 or not irreducible_poly(n): continue
        # normalise by scalar: make norm monic-ish: scale so that a's last nonzero coeff of the top-order part is 1
        key = None
        for k in range(1, Q):
            b = esc(k, a)
            if b[0] and len(b[0]) - 1 == len(a[0]) - 1 and b[0][-1] == 1: key = b
        cand = a
        # canonical form: scale so that norm is monic
        canon = esc(pow(lead(a), Q - 2, Q), a)   # canonical generator: leading coefficient 1 (4/P depends on the generator)
        if canon in seen or lead(canon) != 1: continue
        seen.add(canon); out.append(canon)
    return out

def es_for(P, MX):
    """search X,Y (ord<=MX, all scalars) and solve Z; return first witness (X,Y,Z) or None."""
    fourP = esc(4, ((1,), ()))  # element 4 (constant)
    cands = [a for a in all_elems(MX) if normal(a)]   # sign/unit normalisation: lead coefficient 1
    ordered = cands
    for i, X in enumerate(ordered):
        PX = emul(P, X)
        for Y in ordered[i:]:
            # D = 4XY - P(X+Y);  N = P X Y ;  Z = N/D
            XY = emul(X, Y)
            D = eadd(esc(4, XY), esc(Q - 1, emul(P, eadd(X, Y))))
            if is_zero(D): continue
            N = emul(P, XY)
            Z = divides_A(D, N)
            if Z is None or is_zero(Z) or not normal(Z): continue
            return (X, Y, Z)
    return None

if __name__ == "__main__":
    t0 = time.time()
    PP = principal_primes(MP)
    print(f"principal primes (N irreducible, ord<={MP}, up to F_5^* scalars): {len(PP)}  time={time.time()-t0:.1f}s", flush=True)
    cnt = collections.Counter(eord(P) for P in PP)
    print("  by degree (= pole order):", dict(cnt), flush=True)
    fails = []
    for P in PP:
        w = es_for(P, MX)
        if w is None: fails.append(P)
        else:
            X, Y, Z = w
            # verify 4/P = 1/X+1/Y+1/Z  <=>  4XYZ = P(XY+YZ+ZX) in A
            lhs = esc(4, emul(emul(X, Y), Z)); rhs = emul(P, eadd(eadd(emul(X, Y), emul(Y, Z)), emul(X, Z)))
            assert lhs == rhs
    print(f"ES search with ord(X),ord(Y)<=MX={MX}: failing principal primes = {len(fails)} of {len(PP)}  time={time.time()-t0:.1f}s", flush=True)
    for P in fails[:10]:
        print("  fail P=", P, "ord", eord(P), "N(P)=", enorm(P), flush=True)
