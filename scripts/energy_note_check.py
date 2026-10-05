"""Exact-arithmetic checks for paper/energy-dnf-note.tex.

All quantities are computed with fractions.Fraction (exact rationals), except
where a statement involves an irrational number; there the comparison is
reduced to an exact rational one (e.g. W^k <= 2^{-(t+1)} c^k instead of
W <= c 2^{-(t+1)/k}).

Usage:  PYTHONPATH=scripts uv run python scripts/energy_note_check.py [seed] [scale]
  scale multiplies the number of random cases (default 1; ~1-3 min).
Sections:
  A  Theorem 1.1 (G_F <= 1) and Lemma 3.1 (cover bound), random systems on
     prod_v [q_v] with random rational product measures and rational weights.
  B  Lemma 4.1 (polarization identity, exact), Lemma 4.2 / Theorem 4.3
     (matching bounds for Theta and Q), random weighted hypergraphs.
  C  Corollary 1.3, exhaustive: every Boolean function on 4 bits, uniform
     measure, with its minimal DNF width k: W^{>t} <= 4p(2-p) 2^{-(t+1)/k}
     for all t, sum 2^{|S|/k} g^(S)^2 <= 1+4p and I[g] <= (4k/ln2)p at the
     endpoint (exact for k=1, float with 1e-12 slack otherwise), and
     G_F(lambda) <= 1 for a rational lambda <= 2^{1/k}.
  D  Corollary 1.3 for random DNFs under biased product measures, and q-ary
     DNFs with set-valued literals.
  E  Theorem 7.1 (filtration energy bound), random digit-prefix systems with
     random offsets i_0 in {0,1} and random digit distributions.
  F  Proposition 6.1 (sharpness family, exact level polynomial),
     Example 6.2 (parity formula; the rates (max_s En)^(1/j) are only printed),
     Example 6.3 (adding an event increases G; exact sign on [8]^2, 50-digit on [5]^3).
"""
import itertools
import random
import sys
from fractions import Fraction as Fr
from math import comb

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


# ---------------------------------------------------------------- product spaces
class Space:
    """Finite product space prod_v [q_v] with product measure probs[v][a]."""

    def __init__(self, qs, probs):
        self.qs = list(qs)
        self.n = len(qs)
        self.probs = probs
        self.points = list(itertools.product(*[range(q) for q in qs]))
        self.index = {x: i for i, x in enumerate(self.points)}
        self.weight = []
        for x in self.points:
            w = Fr(1)
            for v, a in enumerate(x):
                w *= probs[v][a]
            self.weight.append(w)

    def E_v(self, f, v):
        """Average over coordinate v."""
        out = [Fr(0)] * len(f)
        pv = self.probs[v]
        for i, x in enumerate(self.points):
            s = Fr(0)
            for a in range(self.qs[v]):
                y = x[:v] + (a,) + x[v + 1:]
                s += pv[a] * f[self.index[y]]
            out[i] = s
        return out

    def norm2(self, f):
        return sum(w * a * a for w, a in zip(self.weight, f))

    def L_norms(self, f):
        """dict mask -> ||L_V f||^2 for all V (bitmask)."""
        n = self.n
        Lf = {0: list(f)}
        for mask in range(1, 1 << n):
            v = (mask & -mask).bit_length() - 1
            g = Lf[mask & ~(1 << v)]
            e = self.E_v(g, v)
            Lf[mask] = [a - b for a, b in zip(g, e)]
        return {m: self.norm2(g) for m, g in Lf.items()}


def components_from_L(Ln, n):
    """||f^{=U}||^2 = sum_{V >= U} (-1)^{|V-U|} ||L_V f||^2."""
    comp = {}
    full = (1 << n) - 1
    for U in range(1 << n):
        s = Fr(0)
        rest = full & ~U
        sub = rest
        while True:
            s += (-1) ** bin(sub).count("1") * Ln[U | sub]
            if sub == 0:
                break
            sub = (sub - 1) & rest
        comp[U] = s
    return comp


def prod_over(mask, vals):
    r = Fr(1)
    v = 0
    while mask:
        if mask & 1:
            r *= vals[v]
        mask >>= 1
        v += 1
    return r


def G_from_comp(comp, lam):
    return sum(prod_over(U, lam) * c for U, c in comp.items())


def rand_probs(rng, q):
    ws = [rng.randint(1, 6) for _ in range(q)]
    s = sum(ws)
    return [Fr(w, s) for w in ws]


LAMS = [Fr(1), Fr(9, 8), Fr(6, 5), Fr(5, 4), Fr(4, 3), Fr(7, 5), Fr(3, 2), Fr(2)]


# ---------------------------------------------------------------- hypergraphs
def N_of(H, V):
    """Signed cover count N_H(V) = sum_{R <= V} (-1)^{|R|} tau_H(R)."""
    s = 0
    sub = V
    while True:
        if all(J & sub for J in H):
            s += (-1) ** bin(sub).count("1")
        if sub == 0:
            break
        sub = (sub - 1) & V
    return s


def N_def(H, V):
    """N_H(V) from the definition (subfamilies whose traces cover V)."""
    H = list(H)
    s = 0
    for r in range(len(H) + 1):
        for J in itertools.combinations(H, r):
            u = 0
            for e in J:
                u |= e & V
            if u == V:
                s += (-1) ** r
    return s


def Q_of(H, mu, n):
    return sum(prod_over(V, mu) * N_of(H, V) ** 2 for V in range(1 << n))


def Theta(C, lam):
    C = list(C)
    s = Fr(0)
    for r in range(len(C) + 1):
        for J in itertools.combinations(C, r):
            u = 0
            for e in J:
                u |= e
            s += (-1) ** r * prod_over(u, lam)
    return s


def matchings(H):
    H = list(H)
    out = [[]]

    def rec(i, used, cur):
        for k in range(i, len(H)):
            if H[k] & used == 0:
                out.append(cur + [H[k]])
                rec(k + 1, used | H[k], cur + [H[k]])

    rec(0, 0, [])
    return out


# ---------------------------------------------------------------- systems
def avoidance(space, events):
    """events: list of (mask, dict v->value). Returns F as list."""
    F = []
    for x in space.points:
        F.append(Fr(0) if any(all(x[v] == a for v, a in val.items()) for _, val in events) else Fr(1))
    return F


def holds(x, val):
    return all(x[v] == a for v, a in val.items())


def section_A(rng, cases):
    worst = Fr(0)
    for _ in range(cases):
        n = rng.randint(1, 4)
        qs = [rng.randint(2, 3) for _ in range(n)]
        if n <= 2:
            qs = [rng.randint(2, 5) for _ in range(n)]
        probs = [rand_probs(rng, q) for q in qs]
        S = Space(qs, probs)
        lam = [rng.choice(LAMS) for _ in range(n)]
        events = []
        for _ in range(rng.randint(1, 7)):
            mask = rng.randint(1, (1 << n) - 1)
            if prod_over(mask, lam) > 2:
                continue
            val = {v: rng.randrange(qs[v]) for v in range(n) if mask >> v & 1}
            events.append((mask, val))
        F = avoidance(S, events)
        Ln = S.L_norms(F)
        comp = components_from_L(Ln, n)
        mu = [l - 1 for l in lam]
        G1 = G_from_comp(comp, lam)
        G2 = sum(prod_over(V, mu) * Ln[V] for V in range(1 << n))
        check(G1 == G2, "Lemma 2.2(a) identity")
        check(G1 <= 1, f"Theorem 1.1: G={G1} qs={qs} lam={lam} ev={events}")
        # cover bound, every V
        Hx = []
        for x in S.points:
            Hx.append(frozenset(m for m, val in events if holds(x, val)))
        for V in range(1 << n):
            rhs = sum(w * N_of(H, V) ** 2 for w, H in zip(S.weight, Hx))
            check(Ln[V] <= rhs, f"Lemma 3.1 V={V}")
        if events:
            worst = max(worst, G1)
    print(f"A: {cases} systems: Theorem 1.1 and Lemma 3.1 hold; max G_F over nonempty systems = {float(worst):.6f}")


def section_B(rng, cases):
    nmatch = 0
    for _ in range(cases):
        n = rng.randint(1, 5)
        lam = [rng.choice(LAMS[1:]) for _ in range(n)]
        mu = [l - 1 for l in lam]
        H = set()
        for _ in range(rng.randint(0, 6)):
            H.add(rng.randint(0, (1 << n) - 1))
        H = frozenset(H)
        # N: two formulas
        for V in range(1 << n):
            check(N_of(H, V) == N_def(H, V), "N formula")
        Q = Q_of(H, mu, n)
        # polarization (no weight condition needed)
        EP = Fr(0)
        for P in range(1 << n):
            pr = Fr(1)
            for v in range(n):
                pr *= (mu[v] / lam[v]) if P >> v & 1 else (1 / lam[v])
            HP = [J for J in H if J & P == 0]
            EP += pr * Theta(HP, lam) ** 2
        check(Q == EP, f"Lemma 4.1 polarization H={sorted(H)} lam={lam}")
        # matching bounds under the weight condition
        Hg = [J for J in H if prod_over(J, lam) <= 2]
        th = Theta(Hg, lam)
        Qg = Q_of(Hg, mu, n)
        for M in matchings(Hg):
            b = Fr(1)
            for J in M:
                b *= prod_over(J, lam) - 1
            check(abs(th) <= b, "Lemma 4.2")
            check(Qg <= b, "Theorem 4.3")
            nmatch += 1
        if len(Hg) > 0 and all(a & b == 0 for a, b in itertools.combinations(Hg, 2)):
            b = Fr(1)
            for J in Hg:
                b *= prod_over(J, lam) - 1
            check(Qg == b, "Theorem 4.3 equality for matchings")
    print(f"B: {cases} hypergraphs: polarization exact; {nmatch} (hypergraph, matching) bounds hold")


def walsh(tt, n):
    """Unnormalised Walsh-Hadamard: returns 2^n * hat g(S), S as bitmask."""
    a = list(tt)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def lam_for_k(k):
    """Largest lambda in a fixed rational grid with lambda^k <= 2."""
    best = Fr(1)
    for num in range(100, 201):
        l = Fr(num, 100)
        if l ** k <= 2:
            best = l
    return best


def section_C():
    n = 4
    N = 1 << n
    # subcubes: (mask of fixed vars, values)
    cubes = []
    for fixed in range(N):
        for vals in range(N):
            if vals & ~fixed:
                continue
            pts = [x for x in range(N) if (x & fixed) == vals]
            cubes.append((bin(fixed).count("1"), pts))
    lamk = {k: lam_for_k(k) for k in range(1, n + 1)}
    maxratio = 0.0
    count = 0
    for code in range(1 << N):
        true = [x for x in range(N) if code >> x & 1]
        if not true:
            continue
        tset = set(true)
        width = 0
        for x in true:
            width = max(width, min(c for c, pts in cubes if x in pts and all(y in tset for y in pts)))
        if width == 0:
            continue  # g constant True
        k = width
        g = [(-1 if code >> x & 1 else 1) for x in range(N)]
        co = walsh(g, n)
        W = [Fr(0)] * (n + 2)
        for S_, c in enumerate(co):
            W[bin(S_).count("1")] += Fr(c * c, N * N)
        p = Fr(len(true), N)
        c0 = 4 * p * (2 - p)
        for t in range(0, n + 1):
            Wt = sum(W[t + 1:])
            # W^{>t} <= c0 2^{-(t+1)/k}  <=>  Wt^k 2^{t+1} <= c0^k
            check(Wt ** k * 2 ** (t + 1) <= c0 ** k, f"Cor 1.3 code={code} t={t}")
            if Wt > 0:
                maxratio = max(maxratio, float(Wt) * 2 ** ((t + 1) / k) / float(c0))
        # endpoint lambda = 2^{1/k}: sum 2^{|S|/k} g^(S)^2 <= 1+4p (exact if k=1, else float)
        if k == 1:
            ws = sum(2 ** bin(S_).count("1") * Fr(c * c, N * N) for S_, c in enumerate(co))
            check(ws <= 1 + 4 * p, f"Cor 1.3 weighted sum code={code}")
        else:
            ws = sum(2 ** (bin(S_).count("1") / k) * (c * c) / (N * N) for S_, c in enumerate(co))
            check(ws <= float(1 + 4 * p) + 1e-12, f"Cor 1.3 weighted sum (float) code={code}")
        infl = sum(bin(S_).count("1") * (c * c) / (N * N) for S_, c in enumerate(co))
        check(infl <= 4 * k / 0.6931471805599453 * float(p) + 1e-12, f"Cor 1.3 influence code={code}")
        # G_F <= 1 with F = (1+g)/2, lambda <= 2^{1/k}
        lam = lamk[k]
        G = sum(lam ** bin(S_).count("1") * Fr(c * c, N * N) for S_, c in enumerate(co) if S_) / 4
        G += ((1 + Fr(co[0], N)) / 2) ** 2
        check(G <= 1, f"Thm 1.1 Boolean code={code}")
        count += 1
    print(f"C: all {count} nonconstant-True Boolean functions on 4 bits: Cor 1.3 holds for all t;"
          f" max W^(>t) 2^((t+1)/k) / (4p(2-p)) = {maxratio:.4f}")


def section_D(rng, cases):
    worst = 0.0
    for case in range(cases):
        boolean = case % 2 == 0
        n = rng.randint(2, 5)
        qs = [2] * n if boolean else [rng.randint(2, 3) for _ in range(n)]
        probs = [rand_probs(rng, q) for q in qs]
        S = Space(qs, probs)
        k = rng.randint(1, min(3, n))
        events = []
        for _ in range(rng.randint(1, 5)):
            vs = rng.sample(range(n), rng.randint(1, k))
            mask = sum(1 << v for v in vs)
            # set-valued literal x_v in S_v, split into single-value cylinders
            choices = [rng.sample(range(qs[v]), rng.randint(1, qs[v] - 1)) for v in vs]
            for vals in itertools.product(*choices):
                events.append((mask, dict(zip(vs, vals))))
        F = avoidance(S, events)
        comp = components_from_L(S.L_norms(F), n)
        a = 1 - sum(w * f for w, f in zip(S.weight, F))  # P(F=0)
        for t in range(n + 1):
            En = sum(c for U, c in comp.items() if bin(U).count("1") > t)
            Wt = 4 * En
            c0 = 4 * a * (2 - a)
            check(Wt ** k * 2 ** (t + 1) <= c0 ** k, f"Cor 1.3 biased/q-ary case {case} t={t}")
            if En > 0:
                worst = max(worst, float(Wt) * 2 ** ((t + 1) / k) / float(c0))
        lam = [lam_for_k(k)] * n
        check(G_from_comp(comp, lam) <= 1, f"Thm 1.1 DNF case {case}")
        # endpoint lambda = 2^{1/k} (float): weighted sum of g = 2F-1 and influence
        ws = sum(2 ** (bin(U).count("1") / k) * float(c) * (4 if U else 1) for U, c in comp.items() if U)
        ws += float(1 - 2 * a) ** 2
        check(ws <= float(1 + 4 * a) + 1e-12, f"Cor 1.3 weighted sum (float) case {case}")
        infl = sum(4 * bin(U).count("1") * float(c) for U, c in comp.items())
        check(infl <= 4 * k / 0.6931471805599453 * float(a) + 1e-12, f"Cor 1.3 influence case {case}")
    print(f"D: {cases} random DNFs (biased Boolean / q-ary set-valued): Cor 1.3 holds;"
          f" max normalised tail {worst:.4f}")


def section_E(rng, cases):
    worst = Fr(0)
    for _ in range(cases):
        # primes (radix) and digit counts; digit 0 may have a smaller alphabet
        ells = rng.sample([2, 3], rng.randint(1, 2))
        digits = []  # (ell, i, alphabet size)
        i0 = {ell: rng.randint(0, 1) for ell in ells}
        for ell in ells:
            f = rng.randint(1, 3 if ell == 2 else 2)
            for i in range(i0[ell], i0[ell] + f):
                digits.append((ell, i, ell))
        if len(digits) > 5:
            digits = digits[:5]
        n = len(digits)
        qs = [d[2] for d in digits]
        probs = [rand_probs(rng, q) for q in qs]
        S = Space(qs, probs)
        lamell = {ell: rng.choice([Fr(1), Fr(21, 20), Fr(11, 10), Fr(6, 5), Fr(5, 4)]) for ell in ells}
        nd = {ell: sum(1 for d in digits if d[0] == ell) for ell in ells}
        events = []
        for _ in range(rng.randint(1, 6)):
            # v_ell(E) in [0, f_ell]; v <= i0 fixes no digit of X_ell
            v = {ell: rng.randint(0, i0[ell] + nd[ell]) for ell in ells}
            if all(x <= i0[ell] for ell, x in v.items()):
                continue
            w = Fr(1)
            for ell in ells:
                w *= lamell[ell] ** (2 * v[ell])
            if w > 2:
                continue
            val = {}
            mask = 0
            for idx, (ell, i, q) in enumerate(digits):
                if i0[ell] <= i < v[ell]:
                    val[idx] = rng.randrange(q)
                    mask |= 1 << idx
            events.append((mask, val))
        F = avoidance(S, events)
        comp = components_from_L(S.L_norms(F), n)
        tot = Fr(0)
        for U, c in comp.items():
            wt = Fr(1)
            for ell in ells:
                idx = [digits[j][1] for j in range(n) if U >> j & 1 and digits[j][0] == ell]
                if idx:
                    wt *= lamell[ell] ** (1 + max(idx))
            tot += wt * c
        check(tot <= 1, f"Theorem 7.1: {tot} digits={digits} i0={i0} lam={lamell} ev={events}")
        if events:
            worst = max(worst, tot)
    print(f"E: {cases} digit-prefix systems: Theorem 7.1 holds; max weighted sum (nonempty systems) = {float(worst):.6f}")


def poly_mul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def poly_pow(a, m):
    res = [Fr(1)]
    base = a
    while m:
        if m & 1:
            res = poly_mul(res, base)
        m >>= 1
        if m:
            base = poly_mul(base, base)
    return res


def section_F():
    # Proposition 6.1: disjoint events, level polynomial B(z)^m; brute-force check first.
    p = Fr(1, 3)
    S = Space([3, 3, 3, 3], [[p, Fr(1, 3), Fr(1, 3)]] * 4)
    events = [(0b0011, {0: 0, 1: 0}), (0b1100, {2: 0, 3: 0})]
    comp = components_from_L(S.L_norms(avoidance(S, events)), 4)
    lev = [sum(c for U, c in comp.items() if bin(U).count("1") == d) for d in range(5)]
    k, m = 2, 2
    pi = p ** k
    blk = [(1 - pi) ** 2] + [comb(k, d) * (p * (1 - p)) ** d * (p * p) ** (k - d) for d in range(1, k + 1)]
    check(poly_pow(blk, m) == lev, "Prop 6.1 level polynomial")
    print("F1: level polynomial of disjoint events matches brute force")
    for k, p in ((1, Fr(1, 40)), (2, Fr(1, 6))):
        pi = p ** k
        blk = [(1 - pi) ** 2] + [comb(k, d) * (p * (1 - p)) ** d * (p * p) ** (k - d) for d in range(1, k + 1)]
        for j in (2, 4, 6):
            best, bm = Fr(0), 0
            step = max(1, int(1 / pi) // 8)
            for m in range(1, int(2 * j / pi) + 1, step):
                if k == 1:  # binomial closed form
                    lev = [comb(m, i) * ((1 - p) ** 2) ** (m - i) * (p * (1 - p)) ** i for i in range(m + 1)]
                else:
                    lev = poly_pow(blk, m)
                En = sum(lev[j * k:])
                a = 1 - (1 - pi) ** m
                # Corollary 1.2: En(jk-1) <= 2^{-j} a(2-a)
                check(En * 2 ** j <= a * (2 - a), f"Cor 1.2 on Prop 6.1 family k={k} j={j} m={m}")
                if En > best:
                    best, bm = En, m
            print(f"F2: k={k} p={p} j={j}: max_m En(jk-1) 2^j = {float(best) * 2 ** j:.4f} (m={bm});"
                  f" p->0 limit is >= 1/(e sqrt j) = {1 / (2.718281828 * j ** 0.5):.4f}")
    # Example 6.2: OR of s disjoint k-parities, brute force for k=2, s=2 then formula.
    n = 4
    g = []
    for x in range(1 << n):
        b = [(x >> v) & 1 for v in range(n)]
        par1, par2 = b[0] ^ b[1], b[2] ^ b[3]
        g.append(-1 if (par1 or par2) else 1)
    co = walsh(g, n)
    F_lev = [Fr(0)] * (n + 1)
    for S_, c in enumerate(co):
        if S_:
            F_lev[bin(S_).count("1")] += Fr(c * c, 4 * 256)
    for j in (1, 2):
        En = sum(F_lev[2 * j:])
        check(En == Fr(sum(comb(2, i) for i in range(j, 3)), 16), "Example 6.2 formula")
    rates = []
    for j in (10, 20, 40):
        best = max(Fr(sum(comb(s, i) for i in range(j, s + 1)), 4 ** s) for s in range(j, 4 * j))
        rates.append((j, float(best) ** (1 / j)))
    print("F3: parity example formula verified; (max_s En(jk-1))^(1/j):",
          ", ".join(f"j={j}: {r:.4f}" for j, r in rates), "(-> 1/3)")
    # Example 6.3: [8]^2 uniform, events {x=(a,b)}, a,b != 0; A = {x=(0,0)}.
    q = 8
    S = Space([q, q], [[Fr(1, q)] * q] * 2)
    ev = [(3, {0: a, 1: b}) for a in range(1, q) for b in range(1, q)]
    c1 = components_from_L(S.L_norms(avoidance(S, ev)), 2)
    c2 = components_from_L(S.L_norms(avoidance(S, ev + [(3, {0: 0, 1: 0})])), 2)
    # G = c[0] + sqrt2 (c[1]+c[2]) + 2 c[3]; difference x + y sqrt2 with x, y rational
    x = (c2[0] - c1[0]) + 2 * (c2[3] - c1[3])
    y = (c2[1] + c2[2]) - (c1[1] + c1[2])
    pos = (x > 0 and y >= 0) or (y > 0 and x >= 0) or (x > 0 > y and x * x > 2 * y * y) or (y > 0 > x and 2 * y * y > x * x)
    check(pos, "Example 6.3: G increases")
    G1 = float(c1[0]) + 2 ** 0.5 * float(c1[1] + c1[2]) + 2 * float(c1[3])
    G2 = float(c2[0]) + 2 ** 0.5 * float(c2[1] + c2[2]) + 2 * float(c2[3])
    print(f"F4: Example 6.3 (exact sign): G before = {G1:.5f}, after adding A = {G2:.5f}")
    # Example 6.3, second instance: [5]^3, lambda = 2^{1/3}, points with exactly two nonzero
    # coordinates, A = {x=(0,0,0)}.  G = sum_U alpha^{|U|} c_U with exact rational c_U;
    # the sign of the difference is evaluated with 50-digit decimal arithmetic.
    from decimal import Decimal, getcontext
    getcontext().prec = 50
    q = 5
    S = Space([q] * 3, [[Fr(1, q)] * q] * 3)
    ev = [(7, {0: x[0], 1: x[1], 2: x[2]}) for x in S.points if sum(1 for a in x if a) == 2]
    check(len(ev) == 48, "Example 6.3 [5]^3 event count")
    c1 = components_from_L(S.L_norms(avoidance(S, ev)), 3)
    c2 = components_from_L(S.L_norms(avoidance(S, ev + [(7, {0: 0, 1: 0, 2: 0})])), 3)
    alpha = Decimal(2) ** (Decimal(1) / Decimal(3))

    def Gd(c):
        return sum(alpha ** bin(U).count("1") * (Decimal(v.numerator) / Decimal(v.denominator)) for U, v in c.items())

    g1, g2 = Gd(c1), Gd(c2)
    check(g2 - g1 > Decimal(10) ** -30, "Example 6.3 [5]^3: G increases")
    print(f"F5: Example 6.3 on [5]^3 (50-digit): G before = {float(g1):.5f}, after adding A = {float(g2):.5f}")


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    scale = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    rng = random.Random(seed)
    section_A(rng, 150 * scale)
    section_B(rng, 300 * scale)
    section_C()
    section_D(rng, 150 * scale)
    section_E(rng, 150 * scale)
    section_F()
    print("ALL CHECKS PASSED" if not FAIL else f"{len(FAIL)} FAILURES")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
