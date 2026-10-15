"""R234 from-scratch re-run of the z9_order3_fano TES chi_3 test (no tf_core / tw_eis / z9_* code).
O = Z[w], w^2 = -1 - w. Type II words: c_i*pi + c_j*v + c_k*u = T*u*v, T != 0, for each choice of i (c_i in {w, w^2, 2}),
(j, k) the remaining two in fixed order. chi_3 = cubic residue class at pi of the tame symbol of
alpha = (-u1/u3, -u2/u3), u = (x/w, y/w^2, z/2), (x, y, z) = denominators attached to (w, w^2, 2):
x_i = u*v, x_j = pi*u, x_k = pi*v. Calibrated on genuine TES solutions (9 | T, (T/9) x_m 2-primary)."""
import sys, math
from collections import Counter
import sympy

def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)

def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x): return (-x[0], -x[1])
def conj(x): return (x[0] - x[1], -x[1])
def norm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]

def div(x, y):
    """x / y if in O else None"""
    n = norm(y); z = mul(x, conj(y))
    if z[0] % n or z[1] % n:
        return None
    return (z[0] // n, z[1] // n)

W = (0, 1); W2 = (-1, -1); TWO = (2, 0); ONE = (1, 0); LAM = (1, -1); NINE = (9, 0)
UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]
assert mul(W, W) == W2 and mul(W, W2) == ONE and norm(LAM) == 3

def two_primary(x): return x[0] % 2 == 1 and x[1] % 2 == 0

def elements_of_norm(n):
    out = []
    B = int(2 * math.isqrt(n // 3 + 1)) + 2
    for b in range(-B, B + 1):
        # a^2 - a b + b^2 - n = 0
        D = b * b - 4 * (b * b - n)
        if D < 0: continue
        s = math.isqrt(D)
        if s * s != D: continue
        for a2 in {b + s, b - s}:
            if a2 % 2 == 0:
                out.append((a2 // 2, b))
    return list(set(out))

_div_cache = {}
def divisors_O(R):
    out = []
    for n in sympy.divisors(norm(R)):
        if n not in _div_cache:
            _div_cache[n] = elements_of_norm(n)
        for d in _div_cache[n]:
            if div(R, d) is not None:
                out.append(d)
    return out

def val(x, p):
    k = 0
    while True:
        q = div(x, p)
        if q is None: return k, x
        x = q; k += 1

def small_elements(bound_norm):
    out = []
    for n in range(1, int(bound_norm) + 1):
        out += elements_of_norm(n)
    return out

class Res:
    """O/pi = F_N via w -> r."""
    def __init__(self, pi):
        self.N = norm(pi); self.pi = pi
        rs = [r for r in range(self.N) if (r * r + r + 1) % self.N == 0]
        self.r = next(r for r in rs if (pi[0] + pi[1] * r) % self.N == 0)
    def red(self, x): return (x[0] + x[1] * self.r) % self.N
    def chi3(self, s):
        e = pow(s, (self.N - 1) // 3, self.N)
        for k in range(3):
            if e == pow(self.r, k, self.N): return k
        raise ValueError

def tame_chi3(R, a, b):
    """cubic class of the tame symbol at pi of (a, b), a, b given as (num, den) pairs of O elements."""
    pi = R.pi
    def vu(f):
        vn, un = val(f[0], pi); vd, ud = val(f[1], pi)
        return vn - vd, R.red(un) * pow(R.red(ud), -1, R.N) % R.N
    va, ua = vu(a); vb, ub = vu(b)
    s = pow(-1, va * vb, R.N) * pow(ua, vb, R.N) * pow(pow(ub, -1, R.N), va, R.N) % R.N if vb >= 0 and va >= 0 else None
    if s is None:
        s = (-1) ** ((va * vb) % 2) * pow(ua, vb % (R.N - 1), R.N) * pow(ub, (-va) % (R.N - 1), R.N) % R.N
    return R.chi3(s)

C = [W, W2, TWO]
CN = [1, 1, 2]  # |c|^2 ... use |c| = 1, 1, 2

def words(pi):
    """set of (i, T, u, v)"""
    N = norm(pi); out = set()
    for i in range(3):
        j, k = [m for m in range(3) if m != i]
        absc = [1, 1, 2][i]
        m = (3 + math.sqrt(9 + 4 * absc * math.sqrt(N))) / 2
        for s in small_elements(m * m + 1e-9):
            # branch u = s small: v (T u - c_j) = c_i pi + c_k u
            for (cs, cother, small_is_u) in ((C[k], C[j], True), (C[j], C[k], False)):
                Rr = add(mul(C[i], pi), mul(cs, s))
                if Rr == (0, 0): continue
                for d in divisors_O(Rr):
                    T = div(add(d, cother), s)
                    if T is None or T == (0, 0): continue
                    o = div(Rr, d)
                    u, v = (s, o) if small_is_u else (o, s)
                    # verify
                    lhs = add(add(mul(C[i], pi), mul(C[j], v)), mul(C[k], u))
                    assert lhs == mul(T, mul(u, v))
                    out.add((i, T, u, v))
    return out

def analyse(pi):
    R = Res(pi); ws = words(pi)
    rows = []
    for (i, T, u, v) in ws:
        j, k = [m for m in range(3) if m != i]
        den = [None] * 3
        den[i] = mul(u, v); den[j] = mul(pi, u); den[k] = mul(pi, v)
        x, y, z = den
        # u1 = x/w = x w^2, u2 = y/w^2 = y w, u3 = z/2 ; -u1/u3 = -2 x w^2 / z ; -u2/u3 = -2 y w / z
        a = (neg(mul(TWO, mul(x, W2))), z); b = (neg(mul(TWO, mul(y, W))), z)
        ch = tame_chi3(R, a, b)
        vl, _ = val(T, LAM)
        sol = False
        T9 = div(T, NINE)
        if T9 is not None:
            sol = all(two_primary(mul(T9, d)) for d in den)
            if sol:  # exact check of 9/pi = sum c/X
                X = [mul(T9, d) for d in den]
                lhs = mul(NINE, mul(X[0], mul(X[1], X[2])))
                rhs = mul(pi, add(add(mul(C[0], mul(X[1], X[2])), mul(C[1], mul(X[0], X[2]))), mul(C[2], mul(X[0], X[1]))))
                assert lhs == rhs
        rows.append((ch, vl, sol))
    return rows

def two_primary_pi(N):
    for a in range(-N, N + 1):
        pass

def prime_above(N):
    for e in elements_of_norm(N):
        for u in UNITS:
            x = mul(u, e)
            if two_primary(x): return x

FAIL = {7, 13, 19, 61, 79, 97, 103, 151, 193, 211, 367, 409, 769}
if __name__ == '__main__':
    bound = int(sys.argv[1])
    agg = Counter(); solch = Counter(); solvable = 0; nsplit = 0
    for N in sympy.primerange(7, bound + 1):
        if N % 3 != 1: continue
        nsplit += 1
        pi = prime_above(N)
        rows = analyse(pi)
        for ch, vl, so in rows:
            for kk in range(5):
                if vl >= kk: agg[(ch, kk)] += 1
            if so: solch[ch] += 1
        nsol = sum(1 for r in rows if r[2])
        solvable += nsol > 0
        h = Counter(r[0] for r in rows)
        t4 = Counter(r[0] for r in rows if r[1] >= 4)
        print(N, 'F' if N in FAIL else '.', 'words', len(rows), 'by chi3', dict(h), 'lam4 by chi3', dict(t4), 'TypeII sols', nsol, flush=True)
    print('split primes', nsplit, 'with a Type II word-solution', solvable, 'chi3 of solutions', dict(solch))
    for ch in range(3):
        print('chi3', ch, [round(agg[(ch, kk)] / agg[(ch, 0)], 4) for kk in range(5)])
