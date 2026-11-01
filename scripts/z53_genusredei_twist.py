# Theorem P census (Z53_GENUSREDEI §5.5): at a fixed prime p, for the (★) levels C <= X (N_C = 4Cp+1, t = 4C),
# classify each level where the event E_C = [-1 in Sigma(N_C) mod t] holds:
#   B1   : -1 in Sigma(s) ∪ Sigma(s)*g  (s = N_C / product of twistable primes; twistable = prime > X dividing N_C exactly once;
#          g = class of the twistable part)  -> event visible from smooth part + product law alone;
#   P2   : not B1, k >= 2 twistable primes and (2^k - 2)|Sigma(s)| < |G^2|   -> event NOT determined by any quadratic data;
#   Podd : not B1, not P2, k >= 2 and (2^k - 2)|Sigma(s)| < |G_odd|          -> not determined by any 2-power-character data;
#   P2x  : not B1/P2/Podd, but an exhaustive search finds a product-1 twist by squares killing the event (protected);
#   Q    : exhaustive search: EVERY product-1 twist by squares keeps the event (event determined by quadratic data);
#   U    : search too large (not classified).
# Reports per prime: #event levels by class, and whether some event level is B1 or U (i.e. possibly decidable from
# 2-power character data + product law + smooth part).
import sys, random
from sympy import factorint, isprime
from math import gcd
def units(t): return [x for x in range(1, t) if gcd(x, t) == 1]
def sigma(fac, t):
    S = {1}
    for q, e in fac:
        c = q % t; new = set(S); cur = set(S)
        for _ in range(e):
            cur = {x * c % t for x in cur}; new |= cur
        S = new
    return S
def odd_part(n):
    while n % 2 == 0: n //= 2
    return n
Gsq_cache = {}
def gsq(t):
    if t not in Gsq_cache: Gsq_cache[t] = len({x * x % t for x in units(t)})
    return Gsq_cache[t]
def phi(t): return len(units(t))
def exact_twist(t, Ss, cls, cap=200000):
    """True if some (h_i) in (G^2)^k with prod h_i = 1 gives -1 not in Ss*Sigma(cls*h); False if none; None if too big."""
    import itertools
    H = sorted({x * x % t for x in units(t)}); k = len(cls)
    if len(H) ** (k - 1) > cap: return None
    inv = {x: y for x in units(t) for y in units(t) if x * y % t == 1}
    for hs in itertools.product(H, repeat=k - 1):
        prod = 1
        for h in hs: prod = prod * h % t
        hh = list(hs) + [inv[prod]]
        a = [c * h % t for c, h in zip(cls, hh)]
        S = {1}
        for x in a: S = S | {y * x % t for y in S}
        if not any((y * z) % t == t - 1 for y in Ss for z in S): return True
    return False
def classify(p, X):
    out = {"B1": 0, "P2": 0, "Podd": 0, "P2x": 0, "Q": 0, "U": 0, "none": 0}
    for C in range(1, X + 1):
        t = 4 * C; N = 4 * C * p + 1; f = factorint(N)
        tw = [q for q, e in f.items() if q > X and e == 1]
        sm = [(q, e) for q, e in f.items() if not (q > X and e == 1)]
        ev = (t - 1) in sigma(list(f.items()), t)
        if not ev: out["none"] += 1; continue
        Ss = sigma(sm, t); g = 1
        for q in tw: g = g * q % t
        if (t - 1) in Ss or (t - 1) in {x * g % t for x in Ss}: out["B1"] += 1; continue
        k = len(tw); bound = (2 ** k - 2) * len(Ss)
        if k >= 2 and bound < gsq(t): out["P2"] += 1
        elif k >= 2 and bound < odd_part(phi(t)): out["Podd"] += 1
        else:
            # exact search for a twist by squares (H = G^2) with product 1 that kills the event
            r = exact_twist(t, Ss, [q % t for q in tw])
            out["U" if r is None else ("P2x" if r else "Q")] = out.get("U" if r is None else ("P2x" if r else "Q"), 0) + 1
    return out
if __name__ == "__main__":
    X = int(sys.argv[1]); mode = sys.argv[2]
    if mode == "list": ps = [int(x) for x in sys.argv[3].split(",")]
    else:
        lo, cnt = int(sys.argv[3]), int(sys.argv[4]); random.seed(53); ps = []
        while len(ps) < cnt:
            q = random.randrange(lo, 2 * lo) | 1
            if q % 4 == 1 and isprime(q): ps.append(q)
    print("# X =", X, " p\tevents\tB1\tP2\tPodd\tP2x\tQ\tU\tpossibly-decidable(B1+Q+U>0)")
    tot = 0; dec = 0
    for p in ps:
        o = classify(p, X); e = o["B1"] + o["P2"] + o["Podd"] + o["P2x"] + o["Q"] + o["U"]; d = int(o["B1"] + o["Q"] + o["U"] > 0)
        tot += 1; dec += d
        print(p, e, o["B1"], o["P2"], o["Podd"], o["P2x"], o["Q"], o["U"], d, sep="\t")
    print("# primes with some level decidable from smooth part + product + 2-power data:", dec, "/", tot)

def range_scan(X, lo, hi):
    """All primes p ≡ 1 (4) in [lo, hi): how many have NO B1-visible event level C <= X, and among those the classes."""
    from sympy import primerange
    n = 0; noB1 = 0; agg = {"P2": 0, "Podd": 0, "P2x": 0, "Q": 0, "U": 0}; onlyP = 0; noev = 0; rows = []
    for p in primerange(lo, hi):
        if p % 4 != 1: continue
        n += 1; o = classify(p, X)
        if o["B1"] == 0:
            noB1 += 1
            for k in agg: agg[k] += o[k]
            if o["P2"] + o["Podd"] + o.get("P2x", 0) + o.get("Q", 0) + o["U"] == 0: noev += 1
            elif o["U"] == 0 and o.get("Q", 0) == 0: onlyP += 1
            rows.append((p, o))
    return n, noB1, agg, onlyP, noev, rows
