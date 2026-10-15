"""s7_window_excess: least cap-0 window m0(n) = min{4x - n : ES solution with gcd(x,n)=1, n | y, n | z}
(= least m ≡ -n (4) with -K ∈ {d mod m : d | K^2}, K=(n+m)/4; CAP_DOWN Lemma 1.1 at cap 0).
Usage: python s7_window_excess.py N [MMAX]
Outputs tiny statistics: histogram, records, Mordell-hard split, correlation with q1(p), lnr(p),
empirical per-window failure rates and an independence-model prediction of P(m0 > M).
"""
import sys, math, collections

def spf_sieve(L):
    spf = list(range(L + 1))
    for i in range(2, int(L ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, L + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def factor(k, spf):
    f = {}
    while k > 1:
        s = spf[k]; e = 0
        while k % s == 0:
            k //= s; e += 1
        f[s] = e
    return f

def fires(K, m, spf):
    """True iff some d | K^2 has d ≡ -K (mod m)."""
    if m == 1:
        return True
    target = (-K) % m
    S = {1 % m}
    for s, b in factor(K, spf).items():
        r = s % m
        pw = [1]
        for _ in range(2 * b):
            pw.append(pw[-1] * r % m)
        S = {x * y % m for x in S for y in set(pw)}
        if target in S:
            return True
    return target in S

def m0(n, spf, MMAX):
    m = (-n) % 4
    if m == 0:
        m = 4
    while m <= MMAX:
        if math.gcd(m, n) == 1 and fires((n + m) // 4, m, spf):
            return m
        m += 4
    return None

def sigkey(p, m):
    ls = sorted(factor_small(m))
    return (m, p % 8) + tuple(legendre(p, l) for l in ls)

def factor_small(m):
    out = set(); l = 2
    while l * l <= m:
        while m % l == 0:
            out.add(l); m //= l
        l += 1
    if m > 1: out.add(m)
    return out

def legendre(a, p):
    t = pow(a % p, (p - 1) // 2, p)
    return -1 if t == p - 1 else t

if __name__ == "__main__":
    N = int(sys.argv[1]); MMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
    spf = spf_sieve(N // 4 + MMAX + 10)
    isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = bytearray(len(isp[i * i::i]))
    primes = [p for p in range(5, N + 1, 4) if isp[p]]
    hist = collections.Counter(); rec = []; best = 0
    MH = {1, 121, 169, 289, 361, 529}
    agg = collections.defaultdict(list)
    fail = collections.defaultdict(lambda: [0, 0])  # (m, sign) -> [fails, total]
    data = []
    for p in primes:
        v = m0(p, spf, MMAX)
        hist[v] += 1
        if v is None or v > best:
            best = v if v else best; rec.append((p, v))
        q1 = next(q for q in range(3, p, 4) if isp[q] and legendre(q, p) == -1)
        lnr = next(q for q in range(2, p) if isp[q] and legendre(q, p) == -1)
        agg[('MH' if p % 840 in MH else 'easy')].append(v)
        agg[('q1', min(q1, 31))].append(v)
        data.append((p, v, q1, lnr))
        for m in range(3, 200, 4):
            if math.gcd(m, p) == 1:
                key = sigkey(p, m)
                fail[key][1] += 1
                if not fires((p + m) // 4, m, spf):
                    fail[key][0] += 1
    print("primes p≡1(4) ≤", N, ":", len(primes))
    print("histogram m0:", sorted(hist.items(), key=lambda t: (t[0] is None, t[0])))
    print("records:", rec[-8:])
    for k in sorted(agg, key=str):
        vs = [x for x in agg[k] if x is not None]
        print("group", k, "count", len(agg[k]), "mean m0 %.2f" % (sum(vs) / len(vs)), "max", max(vs))
    # independence model: P(m0 > M) predicted by product of per-(m,sign) fail rates, averaged over primes
    for M in (3, 7, 11, 19, 27, 35, 47):
        pred = 0.0; act = 0
        for p, v, q1, lnr in data:
            pr = 1.0
            for m in range(3, M + 1, 4):
                if math.gcd(m, p) == 1:
                    f, t = fail[sigkey(p, m)]
                    pr *= f / t
            pred += pr
            act += (v is None or v > M)
        print("M=%d  actual #(m0>M)=%d  independence-model=%.1f" % (M, act, pred))
    print("fail rates (m, (p/m)):", [(k, round(f / t, 3)) for k, (f, t) in sorted(fail.items()) if k[0] < 24])
