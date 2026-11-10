# z70 CLASS — core objects for the good-class sets G_d(n) in the form class group of discriminant -4dn.
# Type II (d fixed):  4abd = n + e,  ce = a + b  (a,b,c,e >= 1).  For a solution put A = 4acd - 1, N_a = n + 4a^2 d = A e.
#   good class (z69 TWIST §9.1):  g = class of the form [A, 4ad, de]  <->  ideal  (A, 2ad + sqrt(-dn)).
#   e-ideal:  E = (e, 2ad + sqrt(-dn)) <-> form [e, 4ad, dA];  [A,4ad,de]*[e,4ad,dA] = T_d := class [d,0,n]  (Lemma CS identity),
#   hence G_d(n) = T_d + X,  X := { +-[E] : E an e-ideal of a solution }   (checked in selftest()).
# Each e-ideal factors as a product of split prime ideals: E = prod_q Q_q^{k_q}, Q_q = (q, 2ad mod q + sqrt(-dn)).
# Writing Q_q = (q, r_q + sqrt(-dn)) or its conjugate (r_q = least root of x^2 = -dn mod q):  [E] = sum_q eps_q k_q [Q_q].
# FLIP NULL: [E]_s := sum_q s_q eps_q k_q [Q_q] with s_q = +-1 iid per prime q.  s = +1 is the real set.  The map E -> E_s is
# multiplicative on ideals, preserves norms and every ideal-level product identity (in particular Lemma DL pairs), and
# randomises class-level coincidences that are not ideal identities.
import sys, math
sys.path.insert(0, 'scripts')
from z69_twist_i17 import reduce
from z69_twist_i17b import Grp

def spf_table(N):
    import numpy as np
    s = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, int(N**0.5) + 1):
        if s[i] == 0:
            blk = s[i*i::i]
            blk[blk == 0] = i
    out = s.tolist()
    for i in range(2, N + 1):
        if out[i] == 0: out[i] = i
    return out

class Fact:
    def __init__(self, N):
        self.N = N; self.spf = spf_table(N) if N >= 2 else [0, 0]
    def factor(self, m):
        f = {}
        if m <= self.N:
            while m > 1:
                q = self.spf[m]; f[q] = f.get(q, 0) + 1; m //= q
            return f
        q = 2
        while q * q <= m:
            while m % q == 0: f[q] = f.get(q, 0) + 1; m //= q
            q += 1
        if m > 1: f[m] = f.get(m, 0) + 1
        return f
    def divisors(self, m):
        ds = [1]
        for q, k in self.factor(m).items():
            ds = [x * q**j for x in ds for j in range(k + 1)]
        return ds

def solutions(n, d, F):
    """all (a,b,c,e) with 4abd = n+e, e | a+b (Type II, fixed d); exhaustive (e <= (n+4d)/(4d-1))."""
    out = []; emax = (n + 4*d) // (4*d - 1)
    e = (-n) % (4*d)
    if e == 0: e = 4*d
    while e <= emax:
        if e >= 2:
            M = (n + e) // (4*d)
            for a in F.divisors(M):
                b = M // a
                if (a + b) % e == 0: out.append((a, b, (a + b)//e, e))
        e += 4*d
    return out

def sqrt_mod_prime(x, q):
    x %= q
    if x == 0: return 0
    if q == 2: return x
    if pow(x, (q-1)//2, q) != 1: return None
    if q % 4 == 3: return pow(x, (q+1)//4, q)
    # Tonelli-Shanks
    Q, S = q - 1, 0
    while Q % 2 == 0: Q //= 2; S += 1
    z = 2
    while pow(z, (q-1)//2, q) != q - 1: z += 1
    M, c, t, R = S, pow(z, Q, q), pow(x, Q, q), pow(x, (Q+1)//2, q)
    while t != 1:
        i, tt = 0, t
        while tt != 1: tt = tt*tt % q; i += 1
        b = pow(c, 1 << (M - i - 1), q); M, c, t, R = i, b*b % q, t*b*b % q, R*b % q
    return R

class ClassData:
    """class group of disc -4dn with prime-ideal classes on demand"""
    def __init__(self, n, d):
        self.n, self.d, self.D = n, d, -4*d*n
        self.G = Grp(self.D)
        self.pcache = {}
        self.Td = self.G.coords[reduce(d, 0, n)]
    def prime_class(self, q):
        """(r_q, coords of Q_q = (q, r_q + sqrt(-dn)))"""
        if q not in self.pcache:
            dn = self.d * self.n
            r = sqrt_mod_prime(-dn, q); assert r is not None and r != 0, (q, self.n, self.d)
            r = min(r, q - r)
            self.pcache[q] = (r, self.G.coords[reduce(q, 2*r, (r*r + dn)//q)])
        return self.pcache[q]
    def ideal_vector(self, e, rho, F):
        """e-ideal (e, rho + sqrt(-dn)) as list of (q, signed exponent eps*k)"""
        vec = []
        for q, k in sorted(F.factor(e).items()):
            r, _ = self.prime_class(q)
            rr = rho % q
            if rr == r: vec.append((q, k))
            else:
                assert rr == q - r, (e, rho, q); vec.append((q, -k))
        return vec
    def vec_class(self, vec, s=None):
        G = self.G; x = G.one
        for q, k in vec:
            _, c = self.prime_class(q)
            kk = k if (s is None or s[q] > 0) else -k
            cc = c if kk > 0 else G.negd[c]
            for _ in range(abs(kk)): x = G.add(x, cc)
        return x

def good_ideals(n, d, F, sols=None):
    """distinct e-ideals (e, rho) of the solutions, rho = 2ad mod e; dict (e,rho) -> list of solutions"""
    if sols is None: sols = solutions(n, d, F)
    out = {}
    for (a, b, c, e) in sols:
        out.setdefault((e, (2*a*d) % e), []).append((a, b, c, e))
    return out

def selftest(n, d, F):
    """check G_d(n) (z69 definition, classes of [A,4ad,de]) == T_d + {+-[E]} and the factorisation formula"""
    C = ClassData(n, d); G = C.G
    sols = solutions(n, d, F)
    Gz = set(G.coords[reduce(4*a*c*d - 1, 4*a*d, d*e)] for (a, b, c, e) in sols)
    X = set(); bad = 0
    for (e, rho), sl in good_ideals(n, d, F, sols).items():
        a, b, c, _ = sl[0]
        direct = G.coords[reduce(e, 4*a*d, d*(4*a*c*d - 1))]
        viav = C.vec_class(C.ideal_vector(e, rho, F))
        if viav != direct: bad += 1
        X.add(viav); X.add(G.negd[viav])
    GX = set(G.add(C.Td, x) for x in X)
    return dict(n=n, d=d, nsol=len(sols), G=len(Gz), X=len(X), equal=(GX == Gz), badvec=bad)

if __name__ == "__main__":
    F = Fact(2*10**6)
    for (n, d) in [(20113, 1), (20113, 3), (20113, 5), (20113, 2), (20113, 7), (200017, 1), (1000033, 1), (409, 1), (4545, 1), (21841, 3)]:
        print(selftest(n, d, F), flush=True)
