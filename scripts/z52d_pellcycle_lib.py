"""z52d PELLCYCLE: shared library — continued-fraction cycle data of sqrt(p) and (1+sqrt(p))/2 as roots
in the word forest F_p (vertices 1..p+2, u~v iff uv | p+u+v; colour chi_p(v) = (v/p)).

Facts used (LOWER_TAIL_ASTRA Lemma 2.1; Z52D_PELLCYCLE.md Lemma 1.2):
  * v>1 has at most one smaller neighbour r_v = (-p mod v); it is a neighbour iff r_v>0 and r_v | p+v (gcd(v,p)=1).
  * u has a larger neighbour v only if v | p+u and u | p+v; then w=(p+u)/v == -1 (mod u), so u^2-1 <= p+u.
    Hence children of u are found among divisors of p+u, and vertices with u^2-1 > p+u are leaves.
"""
import math
from sympy import factorint, legendre_symbol

# ---------- continued fractions ----------

def cf_cycle(D, P0, Q0):
    """Continued fraction of x0=(P0+sqrt(D))/Q0, Q0 | D-P0^2, D non-square.
    Returns (pre, cyc): lists of (P_k, Q_k, a_k); 'cyc' is one full period of the purely periodic part
    (detected by first repeat of (P,Q)), 'pre' the pre-period."""
    assert (D - P0 * P0) % Q0 == 0
    s = math.isqrt(D)
    P, Q = P0, Q0
    seen = {}
    seq = []
    while (P, Q) not in seen:
        seen[(P, Q)] = len(seq)
        # a = floor((P+sqrt D)/Q), exact for Q>0 or Q<0
        if Q > 0:
            a = (P + s) // Q
        else:
            a = (P + s + 1) // Q  # floor for negative denominator (sqrt D irrational)
            # verify
        seq.append((P, Q, a))
        P2 = a * Q - P
        Q2 = (D - P2 * P2) // Q
        P, Q = P2, Q2
    i = seen[(P, Q)]
    return seq[:i], seq[i:]


def convergents_until(pre_a, cyc_a, bound):
    """numerators A_k and denominators B_k of [pre_a; cyc_a, cyc_a, ...] (periodic tail), generated until
    B_k > bound (then A_k > B_k > bound too, as all partial quotients after a_0 are >= 1 and a_0 >= 1) and all
    later convergents are larger; returns all (A_k, B_k) produced."""
    def seq():
        for a in pre_a:
            yield a
        while True:
            for a in cyc_a:
                yield a
    it = seq()
    a0 = next(it)
    A1, A0 = 1, a0
    B1, B0 = 0, 1
    out = [(A0, B0)]
    while not (B0 > bound and A0 > bound):
        a = next(it)
        A1, A0 = A0, a * A0 + A1
        B1, B0 = B0, a * B0 + B1
        out.append((A0, B0))
    return out


def cycle_data(p):
    """Return dict of root families for prime p ≡ 1 (mod 4).
    S  : sqrt(p)  = (0+sqrt(4p))/2 ... we use D=p with P0=0,Q0=1 on sqrt(p) directly.
    W  : omega=(1+sqrt p)/2  -> (P0,Q0)=(1,2) on sqrt(p)."""
    out = {}
    for name, P0, Q0 in (("S", 0, 1), ("W", 1, 2)):
        pre, cyc = cf_cycle(p, P0, Q0)
        allrows = pre + cyc
        P = {r[0] for r in allrows}
        Q = {abs(r[1]) for r in allrows}
        A = {r[2] for r in allrows}
        # all convergents until both A_k, B_k exceed p+2 (A_k, B_k are increasing from k = 1 on)
        conv = convergents_until([r[2] for r in pre], [r[2] for r in cyc], p + 2)
        num = {x for x, _ in conv}
        den = {y for _, y in conv}
        out[name] = dict(pre=pre, cyc=cyc, P=P, Q=Q, a=A, num=num, den=den, period=len(cyc))
    return out


def root_sets(p):
    """Nested definitions (Z52D_PELLCYCLE.md Def 1.2), all intersected with [1, p+2], 0 and p removed.
    R0: P_k, Q_k of the sqrt(p) cycle (whole period incl. k=0)
    R1: R0 + partial quotients a_k of sqrt(p)
    R2: R1 + P_k, Q_k, a_k of the omega=(1+sqrt p)/2 cycle
    R3: R2 + convergent numerators/denominators <= p+2 of sqrt(p) and omega."""
    cd = cycle_data(p)
    S, W = cd["S"], cd["W"]
    lim = p + 2
    ok = lambda s: {x for x in s if 0 < x <= lim and x != p}
    R0 = ok(S["P"] | S["Q"])
    R1 = R0 | ok(S["a"])
    R2 = R1 | ok(W["P"] | W["Q"] | W["a"])
    R3 = R2 | ok(S["num"] | S["den"] | W["num"] | W["den"])
    return dict(R0=R0, R1=R1, R2=R2, R3=R3, periodS=S["period"], periodW=W["period"], cd=cd)


# ---------- forest ----------

_fcache = {}

def divisors_of(n):
    f = factorint(n)
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds


def chi(p, v):  # Euler criterion, returns +1/-1/0
    if v % p == 0:
        return 0
    return 1 if pow(v % p, (p - 1) // 2, p) == 1 else -1


def parent(p, v):
    if v <= 1:
        return None
    r = (-p) % v
    if r > 0 and (p + v + r) % (v * r) == 0:
        return r
    return None


def children(p, u):
    """larger neighbours v>u (v <= p+2)."""
    if u * u - 1 > p + u:
        return []
    out = []
    for v in divisors_of(p + u):
        if v > u and v <= p + 2 and (p + u + v) % (u * v) == 0:
            out.append(v)
    return out


_nbcache = {"p": None, "d": {}}


def neighbours(p, u):
    if _nbcache["p"] != p:
        _nbcache["p"] = p
        _nbcache["d"] = {}
    d = _nbcache["d"]
    if u in d:
        return d[u]
    nb = children(p, u)
    r = parent(p, u)
    if r is not None:
        nb.append(r)
    d[u] = nb
    return nb


def explore(p, u, depth=None, cap=200000):
    """BFS from u. depth=None: full component. Returns (status, nverts, bichrom_edge or None, maxdist).
    status: 'hit' (bichromatic edge found among explored edges), 'mono' (exhausted, none), 'censored' (cap)."""
    if u % p == 0:
        return ("nonunit", 1, None, 0)
    dist = {u: 0}
    frontier = [u]
    d = 0
    while frontier:
        if depth is not None and d >= depth:
            break
        nxt = []
        for x in frontier:
            cx = chi(p, x)
            for y in neighbours(p, x):
                if y % p == 0:
                    continue
                if chi(p, y) != cx:
                    return ("hit", len(dist), (x, y), d + 1)
                if y not in dist:
                    dist[y] = d + 1
                    nxt.append(y)
                    if len(dist) > cap:
                        return ("censored", len(dist), None, d + 1)
        frontier = nxt
        d += 1
    if depth is not None and frontier:
        return ("mono_ball", len(dist), None, d)
    return ("mono", len(dist), None, d)
