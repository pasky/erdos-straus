# z70 GEN — core engine: good sets G_d(n) by the small-fibre method, full class group of D = -4dn as a dict
# reduced form -> exponent vector, genus characters / target coset, natural ideal representatives.
# Type II: 4abd = n + e, ce = a + b.  A = 4acd - 1, N_a = n + 4a^2 d = A e.  good class g = [A, 4ad, de].
# G_d(n) = {[A,4ad,de] : a >= 1, A | N_a, A = -1 mod 4ad}; every solution has min(a,b) <= a_max (see Z70_GEN.md §1).
import math, itertools
import cypari2
pari = cypari2.Pari()
pari.allocatemem(400 * 10**6, silent=True) if hasattr(pari, 'allocatemem') else None

def red(a, b, c):
    f = pari.qfbred(pari.Qfb(a, b, c))
    return (int(f[0]), int(f[1]), int(f[2]))

def divisors(m):
    return [int(x) for x in pari.divisors(m)]

def solutions(n, d):
    """all Type II solutions (a,b,c,e) at fixed d (both orientations), exact."""
    emax = (n + 4*d) // (4*d - 1)
    amax = math.isqrt((n + emax) // (4*d)) + 1
    sols = set()
    for a in range(1, amax + 1):
        Na = n + 4*a*a*d
        m = 4*a*d
        for A in divisors(Na):
            if A % m == m - 1:
                e = Na // A
                if (n + e) % m: raise AssertionError('b not integral')
                b = (n + e) // m; c = (A + 1) // m
                assert c * e == a + b
                sols.add((a, b, c, e)); sols.add((b, a, c, e))
    return sols

def good_class(n, d, s):
    a, b, c, e = s
    A = 4*a*c*d - 1
    return red(A, 4*a*d, d*e)

def natural_reps(n, d, s):
    """the three natural ideals of the class of s (as (N, r mod N)): A-ideal, conj B-ideal, d*conj(e-ideal)."""
    a, b, c, e = s
    A = 4*a*c*d - 1; B = 4*b*c*d - 1
    out = [(A, (2*a*d) % A), (B, (-2*b*d) % B)]
    # (de, r): r = 0 mod d, r = -2ad mod e   (gcd(d,e)=1 needed)
    if math.gcd(d, e) == 1:
        r = int(pari.chinese(pari.Mod(0, d), pari.Mod(-2*a*d, e)).lift()) if d > 1 else (-2*a*d) % e
        out.append((d*e, r % (d*e)))
    return out

def ideal_form(n, d, N, r):
    D4 = d*n
    assert (r*r + D4) % N == 0, (N, r)
    return red(N, 2*r, (r*r + D4) // N)

class ClassGroup:
    """full enumeration of Cl(-4dn) (group structure CONDITIONAL on GRH via quadclassunit; h cross-checkable)."""
    def __init__(self, n, d, maxh=400000):
        self.n, self.d = n, d
        self.D = -4*d*n
        q = pari.quadclassunit(self.D)
        self.h = int(q[0]); self.cyc = [int(x) for x in q[1]]
        if self.h > maxh: raise ValueError('h too large %d' % self.h)
        self.gens = [pari.qfbred(g) for g in q[2]]
        self.elts = {}   # reduced tuple -> exponent tuple
        self.byvec = {}
        # enumerate
        cur = [(pari.qfbred(pari.Qfb(1, 0, d*n)), ())]
        for g, m in zip(self.gens, self.cyc):
            nxt = []
            for f, v in cur:
                x = f
                for k in range(m):
                    nxt.append((x, v + (k,)))
                    x = pari.qfbcomp(x, g)
            cur = nxt
        for f, v in cur:
            t = (int(f[0]), int(f[1]), int(f[2]))
            if t in self.elts: raise AssertionError('duplicate class: structure wrong')
            self.elts[t] = v; self.byvec[v] = t
        assert len(self.elts) == self.h
    def vec(self, t):
        return self.elts[t]
    def add(self, u, v):
        return tuple((x + y) % m for x, y, m in zip(u, v, self.cyc))
    def neg(self, u):
        return tuple((-x) % m for x, m in zip(u, self.cyc))
    def mul(self, k, u):
        return tuple((k * x) % m for x, m in zip(u, self.cyc))
    def is2tors(self, u):
        return all((2*x) % m == 0 for x, m in zip(u, self.cyc))
    def is2power(self, u):
        # order a power of 2  <=>  x is a multiple of the odd part of m in each factor
        for x, m in zip(u, self.cyc):
            o = m
            while o % 2 == 0: o //= 2
            if x % o: return False
        return True
    def sqclass(self, u):
        """image in Cl/Cl^2: parities of the even factors."""
        return tuple(x % 2 for x, m in zip(u, self.cyc) if m % 2 == 0)

def kron(a, b):
    return int(pari.kronecker(a, b))

def represented(t, n, d, k=3):
    """k distinct integers m coprime to 2dn represented by the form t."""
    a, b, c = t; out = []
    for x in range(0, 40):
        for y in range(-40, 41):
            if x == 0 and y <= 0: continue
            m = a*x*x + b*x*y + c*y*y
            if m > 0 and math.gcd(m, 2*d*n) == 1 and m not in out:
                out.append(m)
                if len(out) >= k: return out
    return out

def char_list(n, d):
    """candidate genus characters: Legendre at odd primes of dn, delta, eps, delta*eps."""
    ps = [int(q) for q in pari.factor(d*n)[0] if int(q) % 2 == 1]
    ch = [('q', q) for q in ps]
    # 2-adic assigned characters for D = -4N, N = dn (Cox, Primes of the form x^2+ny^2, Thm 3.15 / Table)
    N = d*n
    if N % 4 == 1: ch.append(('delta', 0))
    elif N % 8 == 2: ch.append(('de', 0))
    elif N % 8 == 6: ch.append(('eps', 0))
    elif N % 8 == 4: ch.append(('delta', 0))
    elif N % 8 == 0: ch += [('delta', 0), ('eps', 0)]
    return ch

def chval(ch, m):
    k, q = ch
    if k == 'q': return kron(m, q)
    dl = 1 if m % 4 == 1 else -1
    ep = 1 if m % 8 in (1, 7) else -1
    return dl if k == 'delta' else ep if k == 'eps' else dl * ep

class Genus:
    """genus characters that are class invariants (checked on generators with several representations)."""
    def __init__(self, CG):
        n, d = CG.n, CG.d
        self.CG = CG
        cands = char_list(n, d)
        valid = []
        for ch in cands:
            ok = True
            for g in CG.gens:
                t = (int(g[0]), int(g[1]), int(g[2]))
                vals = {chval(ch, m) for m in represented(t, n, d, 12)}
                if len(vals) > 1: raise AssertionError('assigned character not invariant %r' % (ch,))
            # also check on the principal form (must be +1)
            if ok and any(chval(ch, m) != 1 for m in represented((1, 0, d*n), n, d, 4)): ok = False
            if ok: valid.append(ch)
        self.chars = valid
        self.genval = []
        for g in CG.gens:
            t = (int(g[0]), int(g[1]), int(g[2])); m = represented(t, n, d, 1)[0]
            self.genval.append(tuple(chval(ch, m) for ch in valid))
        # target: values on m = -1 mod 4d with (m/n) = -1 for the n-character
        tg = []
        for ch in valid:
            k, q = ch
            if k == 'q':
                tg.append(kron(n, q) * 0 - 1 if (n % q == 0) else kron(-1, q))
            else:
                tg.append(chval(ch, 8*d*n - 1))  # m = -1 mod 8d: 2-adic values of -1 (only valid chars kept)
        self.target = tuple(tg)
    def of(self, u):
        out = [1] * len(self.chars)
        for gv, x in zip(self.genval, u):
            if x % 2:
                out = [o * v for o, v in zip(out, gv)]
        return tuple(out)

def split_primes(n, d, upto):
    out = []
    for q in pari.primes([3, upto]):
        q = int(q)
        if (d*n) % q == 0: continue
        if kron(-d*n, q) == 1:
            r = int(pari.Mod(-d*n, q).sqrt().lift()); r = min(r, q - r)
            out.append((q, r))
    return out

def prime_ideal_classes(n, d, upto):
    return [(q, r, ideal_form(n, d, q, r)) for q, r in split_primes(n, d, upto)]
