"""s7_certified_cap: congruence-certified caps on a least-non-residue line lnr(p) = r.
For a prime window q ≡ 3 (4) with (q/p) = -1, K = (p+q)/4 has (i) the forced primes F = {l <= L : l | K}
(l | K iff p ≡ -q mod l; for l = 2 iff p ≡ -q mod 8), each with exponent b_l >= 1 unknown, and (ii) a prime s that is
a non-residue mod q with odd exponent (reciprocity). Guaranteed Lemma-1.1 offsets: F-primes l^{-1,0,1};
s^{G_e}, G_e = {-1,0,1,3,5,...,2e+1} (valid for every odd b_s; c_s even beyond 2b_s). The certified cap at q is the
least e with -1 ∈ <F>^{[-1,1]} * s^{G_e}, worst case over s (s an unknown prime in any non-residue class, or s = l ∈ F
non-residue, then l is removed from F). This depends only on p mod (8 * prod_{l<=L} l * q): a PROVED cap on the class.
Usage: python s7_certified_cap.py N r [QMAX] [L]
"""
import sys, collections

def legendre(a, p):
    t = pow(a % p, (p - 1) // 2, p)
    return -1 if t == p - 1 else t

def reach(F, q):
    S = {1}
    for l in F:
        r = l % q; ri = pow(r, -1, q)
        S = {x * y % q for x in S for y in (1, r, ri)}
    return S

def cert_cap(p, q, SP, emax):
    F = [l for l in SP if l != q and (((p + q) % 8 == 0) if l == 2 else ((p + q) % l == 0))]
    nonres = [a for a in range(1, q) if legendre(a, q) == -1]
    cases = [(F, a) for a in nonres] + [([x for x in F if x != l], l % q) for l in F if legendre(l, q) == -1]
    worst = 0
    cache = {}
    for Fc, a in cases:
        key = tuple(Fc)
        if key not in cache:
            cache[key] = reach(Fc, q)
        S = cache[key]
        ai = pow(a, -1, q)
        best = None
        for e in range(emax + 1):
            G = [ai, 1, a] + [pow(a, j, q) for j in range(3, 2 * e + 2, 2)]
            if any((q - 1) * pow(g, -1, q) % q in S for g in G):
                best = e; break
        if best is None:
            return None
        worst = max(worst, best)
    return worst

if __name__ == "__main__":
    N = int(sys.argv[1]); r = int(sys.argv[2])
    QMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    L = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = bytearray(len(isp[i * i::i]))
    SP = [l for l in range(2, L + 1) if isp[l]]
    small = [l for l in SP if l < r]
    windows = [q for q in range(3, QMAX + 1, 4) if isp[q]]
    tab = collections.Counter(); n = 0; firstq = collections.Counter()
    for p in range(9, N + 1, 8):  # p ≡ 1 (8) is forced by (2/p) = 1
        if p <= r or not isp[p] or legendre(p, r) != -1 or any(legendre(p, l) != 1 for l in small if l > 2):
            continue
        n += 1
        best = None
        for q in windows:
            if legendre(q, p) != -1:
                continue
            c = cert_cap(p, q, SP, (q - 3) // 4)
            if c is not None and (best is None or c < best):
                best = c
                if c == 0:
                    break
        tab[best] += 1
    print("line lnr(p) = %d, primes <= %d: %d; windows q <= %d, forced primes <= %d" % (r, N, n, QMAX, L))
    for k in sorted(tab, key=lambda t: (t is None, t)):
        print("  certified cap", k, ":", tab[k], "(%.3f)" % (tab[k] / n))

def haar_mc(r, QMAX, L, samples, seed=1):
    """Haar (profinite) density on the line lnr = r: random residues p mod l for every prime l <= max(QMAX, L),
    QR for l < r, QNR for l = r, uniform non-zero for l > r, p ≡ 1 (8). Returns Counter of certified caps."""
    import random
    rng = random.Random(seed)
    P = [l for l in range(3, max(QMAX, L) + 1) if all(l % d for d in range(2, int(l ** 0.5) + 1))]
    SP = [2] + [l for l in P if l <= L]
    windows = [q for q in P if q % 4 == 3 and q <= QMAX]
    out = collections.Counter()
    for _ in range(samples):
        res = {}
        for l in P:
            while True:
                a = rng.randrange(1, l)
                sym = legendre(a, l)
                if (l < r and sym == 1) or (l == r and sym == -1) or l > r:
                    break
            res[l] = a
        # emulate p via CRT-free predicates: l | K_q iff res[l] ≡ -q (mod l); 2 | K_q iff q ≡ 7 (8) (p ≡ 1 (8))
        best = None
        for q in windows:
            F = [2] if q % 8 == 7 else []
            F += [l for l in SP if l != 2 and l != q and (res[l] + q) % l == 0]
            if legendre(res[q], q) != -1:  # unforced window: only F-data (an ET class) can certify, at cap 0
                if (q - 1) in reach(F, q):
                    best = 0; break
                continue
            c = cert_cap_F(F, q, (q - 3) // 4)
            if c is not None and (best is None or c < best):
                best = c
                if c == 0:
                    break
        out[best] += 1
    return out

def cert_cap_F(F, q, emax):
    nonres = [a for a in range(1, q) if legendre(a, q) == -1]
    cases = [(F, a) for a in nonres] + [([x for x in F if x != l], l % q) for l in F if legendre(l, q) == -1]
    worst = 0; cache = {}
    for Fc, a in cases:
        key = tuple(Fc)
        if key not in cache:
            cache[key] = reach(Fc, q)
        S = cache[key]; ai = pow(a, -1, q); best = None
        for e in range(emax + 1):
            G = [ai, 1, a] + [pow(a, j, q) for j in range(3, 2 * e + 2, 2)]
            if any((q - 1) * pow(g, -1, q) % q in S for g in G):
                best = e; break
        if best is None:
            return None
        worst = max(worst, best)
    return worst
