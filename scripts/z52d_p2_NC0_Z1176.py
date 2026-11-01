"""Z1176: SAT encoding of bounded ES search, p = 13 (G4, NC0).
Instance: x,y,z in [1, 2^B - 1] (B bits each, value = bit-vector), constraint 4xyz = p(xy+yz+zx) (exact integers).
Boolean circuit with EXPLICIT carries: shift-add multipliers and ripple-carry adders (full adders as Tseitin
clauses), equality by bitwise equivalence, x,y,z != 0 by clauses. Models are enumerated with blocking clauses
using minisat (system binary). Decoded models are compared with direct enumeration (all ordered triples with
entries <= 2^B - 1 from the exact sorted-solution enumerator, permutations included)."""
import sys, math, subprocess, os, itertools
from fractions import Fraction

P = int(sys.argv[1]) if len(sys.argv) > 1 else 13
B = int(sys.argv[2]) if len(sys.argv) > 2 else 10
OUT = "data/z52b/pass2/NC0/sub"
os.makedirs("/tmp/z52d_big/G4", exist_ok=True)


class CNF:
    def __init__(self):
        self.n = 0; self.cl = []
        self.TRUE = self.new(); self.cl.append([self.TRUE])
        self.FALSE = -self.TRUE
    def new(self):
        self.n += 1; return self.n
    def AND(self, a, b):
        c = self.new()
        self.cl += [[-c, a], [-c, b], [c, -a, -b]]
        return c
    def OR(self, a, b):
        c = self.new()
        self.cl += [[c, -a], [c, -b], [-c, a, b]]
        return c
    def XOR(self, a, b):
        c = self.new()
        self.cl += [[-c, a, b], [-c, -a, -b], [c, -a, b], [c, a, -b]]
        return c
    def full_add(self, a, b, cin):
        t = self.XOR(a, b)
        s = self.XOR(t, cin)
        c1 = self.AND(a, b); c2 = self.AND(t, cin)
        return s, self.OR(c1, c2)
    def add(self, u, v):
        W = max(len(u), len(v))
        u = u + [self.FALSE] * (W - len(u)); v = v + [self.FALSE] * (W - len(v))
        out = []; c = self.FALSE
        for i in range(W):
            s, c = self.full_add(u[i], v[i], c)
            out.append(s)
        return out + [c]
    def mul(self, u, v):
        acc = [self.FALSE] * (len(u) + len(v))
        for j, vj in enumerate(v):
            pp = [self.AND(ui, vj) for ui in u]
            shifted = [self.FALSE] * j + pp
            acc = self.add(acc, shifted)[:len(u) + len(v)]
        return acc
    def const(self, val, W):
        return [self.TRUE if (val >> i) & 1 else self.FALSE for i in range(W)]
    def equal(self, u, v):
        W = max(len(u), len(v))
        u = u + [self.FALSE] * (W - len(u)); v = v + [self.FALSE] * (W - len(v))
        for a, b in zip(u, v):
            self.cl += [[-a, b], [a, -b]]
    def dimacs(self, extra):
        lines = [f"p cnf {self.n} {len(self.cl) + len(extra)}"]
        for c in self.cl + extra:
            lines.append(" ".join(map(str, c)) + " 0")
        return "\n".join(lines) + "\n"


def build():
    cnf = CNF()
    xs = [cnf.new() for _ in range(B)]; ys = [cnf.new() for _ in range(B)]; zs = [cnf.new() for _ in range(B)]
    for v in (xs, ys, zs):
        cnf.cl.append(list(v))  # nonzero (at least one bit set)
    xy = cnf.mul(xs, ys); yz = cnf.mul(ys, zs); zx = cnf.mul(zs, xs)
    s = cnf.add(cnf.add(xy, yz), zx)
    lhs = cnf.mul(cnf.mul(xs, ys), zs)  # xyz
    lhs4 = cnf.add(lhs, lhs); lhs4 = cnf.add(lhs4, lhs4)  # 4xyz
    W = max(len(lhs4), len(s)) + 1
    rhs = cnf.mul(cnf.const(P, W), s)  # p*(xy+yz+zx)
    cnf.equal(lhs4, rhs)
    return cnf, xs, ys, zs


def solve_all(cnf, xs, ys, zs, limit=10000):
    models = []
    extra = []
    while len(models) < limit:
        open(f"/tmp/z52d_big/G4/z1176_{P}_{B}.cnf", "w").write(cnf.dimacs(extra))
        r = subprocess.run(["timeout", "900", "minisat", f"/tmp/z52d_big/G4/z1176_{P}_{B}.cnf",
                            f"/tmp/z52d_big/G4/z1176_{P}_{B}.out"], capture_output=True, text=True)
        out = open(f"/tmp/z52d_big/G4/z1176_{P}_{B}.out").read().split()
        if not out or out[0] != "SAT":
            break
        vals = {int(t) for t in out[1:] if int(t) > 0}
        def bit(v): return 1 if v in vals else 0
        dec = lambda vs: sum((1 << i) * bit(v) for i, v in enumerate(vs))
        x, y, z = dec(xs), dec(ys), dec(zs)
        models.append((x, y, z))
        extra.append([-v if bit(v) else v for v in xs + ys + zs])  # block this assignment
    return models


cnf, xs, ys, zs = build()
print(f"p={P}, B={B} bits per variable (values 1..{2**B-1}); CNF vars {cnf.n}, clauses {len(cnf.cl)}")
models = solve_all(cnf, xs, ys, zs)
print("SAT models decoded:", len(models))
# direct enumeration: exact sorted solutions (x<=y<=z), all permutations, entries < 2^B
def sorted_solutions(p):
    S = []
    for x in range(math.ceil(p / 4), (3 * p) // 4 + 1):
        r = Fraction(4, p) - Fraction(1, x)
        if r <= 0: continue
        for y in range(x, math.floor(2 / r) + 1):
            r2 = r - Fraction(1, y)
            if r2 > 0 and r2.numerator == 1:
                S.append((x, y, r2.denominator))
    return S
bound = 2 ** B - 1
direct = set()
for t in sorted_solutions(P):
    if max(t) <= bound:
        for perm in itertools.permutations(t):
            direct.add(perm)
print("direct enumeration (ordered, entries <= %d): %d" % (bound, len(direct)))
print("SAT model set == direct set:", set(models) == direct and len(models) == len(set(models)))
print("sorted solutions found by SAT:", sorted({tuple(sorted(m)) for m in models}))
# verify each decoded model exactly
assert all(4 * x * y * z == P * (x * y + y * z + z * x) for x, y, z in models)
print("all decoded models verified exactly in integers")
