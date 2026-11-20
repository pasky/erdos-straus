# Round-2 hostile review checks for notes/z78/F3_CONJ.md §§6-7 (fresh code, F_3[T]).
# Polynomials: lists of ints mod 3, low degree first, no trailing zeros.
import sys, itertools
from collections import Counter

def nrm(a):
    a = [x % 3 for x in a]
    while a and a[-1] == 0: a.pop()
    return a
def add(*ps):
    n = max((len(p) for p in ps), default=0); o = [0]*n
    for p in ps:
        for i, x in enumerate(p): o[i] += x
    return nrm(o)
def neg(a): return nrm([-x for x in a])
def sub(a, b): return add(a, neg(b))
def sc(k, a): return nrm([k*x for x in a])
def mul(*ps):
    r = [1]
    for b in ps:
        if not r or not b: return []
        o = [0]*(len(r)+len(b)-1)
        for i, x in enumerate(r):
            if x:
                for j, y in enumerate(b): o[i+j] += x*y
        r = nrm(o)
    return r
def dvm(a, b):
    a = a[:]; q = [0]*max(0, len(a)-len(b)+1); il = 1 if b[-1] == 1 else 2
    while a and len(a) >= len(b):
        s = len(a)-len(b); f = (a[-1]*il) % 3; q[s] = f
        for i, y in enumerate(b): a[i+s] = (a[i+s]-f*y) % 3
        a = nrm(a)
    return nrm(q), a
def exq(a, b):
    q, r = dvm(a, b)
    return q if not r else None
def Tp(k): return [0]*k+[1]
def deg(a): return len(a)-1 if a else -10**9
def val(a):
    if not a: return 10**9
    i = 0
    while a[i] == 0: i += 1
    return i
def lc(a): return a[-1]
def der(a): return nrm([i*a[i] for i in range(1, len(a))])
def gcd(a, b):
    while b: a, b = b, dvm(a, b)[1]
    return sc(1 if a[-1] == 1 else 2, a) if a else a
def trunc(a, k): return nrm(a[:k])
def inv_ser(a, k):  # power series inverse mod T^k, a(0)!=0
    a0inv = 1 if a[0] == 1 else 2; r = [0]*k
    for i in range(k):
        s = (1 if i == 0 else 0) - sum(a[j]*r[i-j] for j in range(1, min(i, len(a)-1)+1))
        r[i] = (s*a0inv) % 3
    return nrm(r)
def degR3(A, B):
    # F=A/B; R3(F)F'/F has denominator R3; deg R3 = deg rad-part = deg(AB/gcd(A'B-AB',AB)) computed as reduced denom of F'/F
    num = sub(mul(der(A), B), mul(A, der(B)))
    if not num: return None
    AB = mul(A, B); return deg(AB)-deg(gcd(num, AB))

def monic_tunits(d):
    if d == 0: yield [1]; return
    for low in itertools.product(range(3), repeat=d):
        if low[0] == 0: continue
        yield list(low)+[1]

# ---------- (a) independent tuple enumeration for small n ----------
def enum_tuples(n):
    out = []
    Tn = Tp(n)
    for z in range(0, n+1):
        for a1 in range(0, n-z+1):
            b1 = n-z-a1
            Ms = list(monic_tunits(z)); Ws = list(monic_tunits(a1)); Cs = list(monic_tunits(b1))
            for m in Ms:
                for w in Ws:
                    mw = mul(m, w)
                    for C in Cs:
                        if (w[0]+C[0]) % 3: continue
                        V = sub(mul(mw, C), Tn)
                        if not V or V[0] == 0: continue
                        s_ = add(w, C)
                        TV = mul(Tp(1), V)
                        g = exq(s_, TV)
                        if g is None or not g or g[-1] != 1 or g[0] == 0: continue
                        out.append((m, w, C, g, V))
    return out

def P2s(p): return ''.join(str(x) for x in p) if p else '0'

def part_a(nmax):
    res = {}
    allt = {}
    for n in range(1, nmax+1):
        T = enum_tuples(n); allt[n] = T
        s = n+2; Nmin = -(-s//2)
        mx = {}
        for c in (1, 2):
            u = [1, c]
            deps = [val(add(t[1], mul(u, t[2]))) for t in T]
            mx[c] = max(deps) if deps else None
            cover = [t for t, d in zip(T, deps) if d >= Nmin+1]
            res[(n, c)] = (len(T), mx[c], Nmin+1, len(cover))
    return res, allt

# ---------- (b) identity checks at self-points u := -w/C mod T^K ----------
def ident_check(t, n, K, orient, stats, cu=None):
    m, w, C, g, V = t
    if cu is None:
        u = trunc(mul(neg(w), inv_ser(C, K)), K)   # polynomial of deg < K, u(0)=1
    else:
        u = cu
    if not u or u[0] != 1: return
    if orient == 'A': X, B, p, q = w, C, [1], u
    else:            X, B, p, q = C, w, u, [1]
    N = K-1; b = n-K; dl = N-b
    if b < 0 or dl < 1: return
    M = mul(m, X)
    kap = exq(sub(q, p), Tp(1))
    if kap is None: stats['kap_nonint'] += 1; return
    H = exq(add(mul(p, X), mul(q, B)), Tp(K))
    if H is None: stats['cover_fail'] += 1; return
    J = exq(add(mul(p, M, X), mul(q, V)), Tp(K))
    S = exq(add(mul(p, M, g), kap), Tp(N))
    if J is None or S is None: stats['JS_fail'] += 1; return
    ok = lambda nm, c: stats.__setitem__(nm+(':ok' if c else ':FAIL'), stats[nm+(':ok' if c else ':FAIL')]+1)
    ok('MH', mul(M, H) == add(mul(q, Tp(b)), J))
    ok('VS', mul(V, S) == add(mul(p, Tp(b)), J))
    Wn = add(mul(Tp(dl), S, J), mul(kap, q))
    W = exq(Wn, M)
    ok('W_int', W is not None)
    if W is None: return
    ok('VW', mul(V, W) == sub(mul(Tp(dl), H, J), mul(kap, p, X)))
    ok('pXS', mul(p, X, S) == sub(mul(Tp(b+1), W), mul(q, H)))
    ok('TdSH-W=ug', sub(mul(Tp(dl), S, H), W) == mul(p, q, g))
    ok('pgJ', mul(p, g, J) == sub(mul(Tp(b), W), mul(kap, H)))
    lhs = add(mul(p, M, W), mul(Tp(dl), q, m, H, H))
    rhs = add(mul(kap, u), mul(Tp(N), sub(mul(Tp(1), m, H, W), mul(u, S))))
    ok('(6.1)', lhs == rhs)
    # degree formula of second term (needs deg qB > deg pX for deg H = L+Q-K)
    z, r, L = deg(m), deg(X), deg(B); d = z+r; Q = deg(q)
    if L+Q > r+deg(p):
        ok('deg2nd', deg(mul(Tp(dl), q, m, H, H)) == N+b+3*Q-d-r)
    # second-contact square identity, general u, char 3
    A0 = sub(mul(q, B), mul(p, X))
    if 2*K-n >= 0:
        D = sub(mul(m, Tp(2*K-n), H, H), u)
        ok('square', add(mul(m, A0, A0), mul(u, V)) == mul(Tp(n), D))
        # §7 L0 congruence: L0 = T^(1-n) C G'/G, C = m A0 u V, G = m A0^2/(uV)
        Cc = mul(m, A0, u, V)
        # C*G'/G = m' A0 u V + 2 m A0' u V - m A0 (uV)'
        CGG = add(mul(der(m), A0, u, V), sc(2, mul(m, der(A0), u, V)), neg(mul(m, A0, der(mul(u, V)))))
        if CGG and val(CGG) >= n-1:
            L0 = CGG[n-1:]
            e = min(dl, 2*K-n, K)   # precision of the claimed congruence
            if e >= 1:
                # RHS: (kap u^2 / W) [ n - T(p'/p - W'/W + X'/X) ] mod T^e
                Wi = inv_ser(W, e+1); pi = inv_ser(p, e+1); Xi = inv_ser(X, e+1)
                ki = inv_ser(kap, e+1)
                lg = add(mul(der(p), pi), mul(der(kap), ki), neg(mul(der(W), Wi)), mul(der(X), Xi))  # kappa'/kappa term vanishes at x* (constant kappa)
                br = sub([n % 3], mul(Tp(1), trunc(lg, e)))
                R = trunc(mul(kap, u, u, Wi, br), e)
                ok('L0form', trunc(L0, e) == R)
                ok('L0const', (L0[0] if L0 else 0) == (mul([n % 3], kap, inv_ser(W, 1))[:1] or [0])[0])

def part_b(allt, census):
    stats = Counter()
    tl = [(n, t) for n, T in allt.items() for t in T] + census
    for n, t in tl:
        for K in range(2, n+1):
            if K > n+1: break  # K <= s-1 = n+1; identities need K<=n
            for o in ('A', 'B'):
                ident_check(t, n, K, o, stats)
    return stats

# ---------- (c) second contact at x*_c on deep (non-covering) tuples ----------
def part_c(tl):
    st = Counter(); viol = []
    for n, t in tl:
        m, w, C, g, V = t
        for c in (1, 2):
            u = [1, c]; K = val(add(w, mul(u, C)))
            if 2*K < n or K > n: continue
            for o in ('A', 'B'):
                if o == 'A': X, B, p, q = w, C, [1], u
                else:        X, B, p, q = C, w, u, [1]
                L, r, z, v = deg(B), deg(X), deg(m), deg(V); Q = deg(q)
                if not (L+Q > r+deg(p)): continue
                H = exq(add(mul(p, X), mul(q, B)), Tp(K))
                A0 = sub(mul(q, B), mul(p, X))
                G_num = mul(m, A0, A0); G_den = mul(u, V)
                R = degR3(G_num, G_den)
                st['cases'] += 1
                if R is None: st['Gcube'] += 1; continue
                if R < n: viol.append(('R3G<n', n, c, o, R)); continue
                st['R3G>=n'] += 1
                if v < r-Q-1: viol.append(('v<r-Q-1', n, c, o, v, r, Q))
                else: st['v>=r-Q-1'] += 1
    return st, viol

# ---------- (d) endpoint system brute force ----------
def part_d(dmax):
    # B, c=1, delta=3, H=1, p=u=1+T, q=1, kappa=-1, M=T^d+J, M=mX, X=TWJ+1, uS=TmW-1, MW=T^3 S J -1, W monic deg 2 W(0)!=0
    u = [1, 1]; found = []; relaxed = 0
    Ws = [W for W in monic_tunits(2)]
    for d in range(1, dmax+1):
        for j in range(0, d):
            for Jl in itertools.product(range(3), repeat=j):
                for J0 in (1,):   # lc J = lc p = 1
                    J = nrm(list(Jl)+[1])
                    if not J: continue
                    M = add(Tp(d), J)
                    if M[0] == 0: continue
                    for W in Ws:
                        X = add(mul(Tp(1), W, J), [1])
                        m = exq(M, X)
                        if m is None: continue
                        S = exq(sub(mul(Tp(1), m, W), [1]), u)
                        if S is None: continue
                        relaxed += 1
                        if mul(M, W) == sub(mul(Tp(3), S, J), [1]):
                            found.append((d, J, W))
    return relaxed, found

def load_census(fn):
    out = []
    seen = set()
    for line in open(fn):
        f = dict(x.split('=') for x in line.split())
        key = (f['m'], f['w'], f['C'])
        if key in seen: continue
        seen.add(key)
        P_ = lambda s: nrm([int(ch) for ch in s])
        out.append((int(f['n']), (P_(f['m']), P_(f['w']), P_(f['C']), P_(f['g']), P_(f['V']))))
    return out

if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    res, allt = part_a(nmax)
    print('== (a) independent enumeration n<=%d: (n,c): #tuples, max dep, needed N(s)+1, #covering' % nmax)
    for k in sorted(res): print(k, res[k])
    census = load_census('census_s4_17.txt')
    cn = Counter(n for n, _ in census)
    print('census tuples by n:', dict(sorted(cn.items())))
    for n in range(1, nmax+1):
        mine = sorted((P2s(t[0]), P2s(t[1]), P2s(t[2])) for t in allt[n])
        theirs = sorted((P2s(t[0]), P2s(t[1]), P2s(t[2])) for nn, t in census if nn == n)
        print('n=%d mine=%d census=%d equal=%s' % (n, len(mine), len(theirs), mine == theirs))
    st = part_b(allt, [x for x in census if x[0] > nmax])
    print('== (b) identities at self-points:', dict(sorted(st.items())))
    tl = [(n, t) for n, T in allt.items() for t in T] + [x for x in census if x[0] > nmax]
    extra = []
    try:
        for line in open('tuples_lop_n25_28.txt'):
            f = dict(x.split('=') for x in line.split())
            P_ = lambda s: nrm([int(ch) for ch in s])
            extra.append((int(f['n']), (P_(f['m']), P_(f['w']), P_(f['C']), P_(f['g']), P_(f['V']))))
    except FileNotFoundError: pass
    st2, viol = part_c(tl+extra)
    print('== (c) second contact at x*_c, 2K>=n:', dict(st2), 'violations:', viol[:10])
    rel, found = part_d(int(sys.argv[2]) if len(sys.argv) > 2 else 7)
    print('== (d) endpoint: relaxed solutions (all but MW eq):', rel, 'full solutions:', found)
