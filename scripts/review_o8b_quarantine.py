"""R30b from-scratch checks (reviewer 2 of OMEGA8): definition chain and Haar-side inputs.

Independent of the author's scripts.  Checks
 (a) R(M) := {-4D mod M : D | A^2} equals the multiplier-witness set
     {-u v^{-1} mod M : uvw = A} of blind51 (B1.1), and 1 notin R(M)  (Fact 1.1);
 (b) O2 Lemma 11.2 iterated quarantine from {l<=z} with c0 = 1/(64k):
     final max w_l <= c0, |B| <= k S*/c0, S_tot(Pi) <= S* <= Lemma 11.1 majorant;
 (c) O2 Lemma 4.3 (I) for the iterated-quarantine Pi: for integers n = 1 (Q_Pi),
     built by actual CRT, "no surviving event occurs" <=> W(n) > T
     (both directions; forced survivors + unconditioned samples);
 (d) LLL premise sum_{E'~E} 2P(E') <= 2k c0 and delta >= prod(1-2P(E)).
Usage: review_o8b_quarantine.py T z nsurv nrand seed [c0]
"""
import sys, math, random
from math import gcd

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds

def phi_f(f):
    r = 1
    for p, e in f.items(): r *= (p - 1) * p ** (e - 1)
    return r

def Rset(M):
    A = (M + 1) // 4
    fa = factor(A); fa2 = {p: 2 * e for p, e in fa.items()}
    return {(-4 * D) % M for D in divisors_from(fa2)}

def Rset_uvw(M):
    A = (M + 1) // 4; out = set()
    for u in divisors_from(factor(A)):
        for v in divisors_from(factor(A // u)):
            out.add((-u * pow(v, -1, M)) % M)
    return out

def main():
    T, z, nsurv, nrand, seed = (int(a) for a in sys.argv[1:6])
    rng = random.Random(seed)
    L = math.log(T)
    # (a)
    bad = 0
    for M in range(3, min(T, 2000) + 1, 4):
        R = Rset(M)
        if R != Rset_uvw(M) or 1 in R: bad += 1
    print(f"(a) R(M) == uvw-set and 1 notin R(M) for all M<=min(T,2000), M=3(4): failures={bad}")
    P = primes_upto(T)
    e = {l: int(math.floor(math.log(T) / math.log(l) + 1e-12)) for l in P}
    for l in P:
        while l ** (e[l] + 1) <= T: e[l] += 1
        while l ** e[l] > T: e[l] -= 1
    k = int(L // math.log(z))
    c0 = 1.0 / (64 * k) if len(sys.argv) < 7 else float(sys.argv[6])  # optional override for non-degenerate toy
    atoms = []  # (M, fM, D)
    for M in range(3, T + 1, 4):
        fM = factor(M); A = (M + 1) // 4
        fa2 = {p: 2 * x for p, x in factor(A).items()}
        for D in divisors_from(fa2):
            atoms.append((M, fM, D))
    # S* : per atom max over all Pi of 1[survive]/phi(r_Pi)
    Sstar = 0.0
    for M, fM, D in atoms:
        best = 0.0; items = list(fM.items())
        for mask in range(2 ** len(items)):
            m = 1; rf = {}
            for i, (p, x) in enumerate(items):
                if mask >> i & 1: m *= p ** x
                else: rf[p] = x
            if m < M and (4 * D + 1) % m == 0:
                best = max(best, 1.0 / phi_f(rf))
        Sstar += best
    def tau(n): return len(divisors_from(factor(n)))
    X = (T + 1) / 4
    inner = sum(tau(4 * s * r * r + 1) / (s * r) for r in range(1, int(T ** 0.5) + 1)
                for s in range(1, T // (r * r) + 1) if all(s % (q * q) for q in range(2, int(s ** 0.5) + 1)))
    maj11 = 2 * (3 + math.log(X)) / 3 * inner  # Lemma 11.1 shape without the C loglog T factor
    def events_for(Pi):
        ev = {}
        for M, fM, D in atoms:
            m = 1; rf = {}
            for p, x in fM.items():
                if p in Pi: m *= p ** x
                else: rf[p] = x
            if not rf or (4 * D + 1) % m: continue
            key = tuple(sorted((p, x, (-4 * D) % p ** x) for p, x in rf.items()))
            ev[key] = 1.0 / phi_f(rf)
        return ev
    Pi = set(l for l in P if l <= z); B = set(); rounds = 0
    while True:
        ev = events_for(Pi)
        w = {}
        for key, pr in ev.items():
            for p, x, a in key: w[p] = w.get(p, 0.0) + pr
        add = {p for p, v in w.items() if v > c0 and p > z and p not in Pi}
        if not add: break
        Pi |= add; B |= add; rounds += 1
    Stot = sum(ev.values()); wmax = max(w.values()) if w else 0
    print(f"(b) T={T} z={z} k={k} c0={c0:.5f} rounds={rounds} |B|={len(B)} kS*/c0={k*Sstar/c0:.1f} "
          f"final max w={wmax:.5f} (<=c0: {wmax<=c0}) S_tot(Pi)={Stot:.3f} S*={Sstar:.3f} "
          f"Lemma11.1 majorant (no loglog factor)={maj11:.1f}")
    print(f"    |B|<=kS*/c0: {len(B) <= k*Sstar/c0};  S_tot<=S*: {Stot<=Sstar+1e-9};  "
          f"max support={max((len(kk) for kk in ev), default=0)} (<=k: {max((len(kk) for kk in ev), default=0)<=k})")
    # (d) LLL premise
    nb = max((sum(2 * w[p] for p, x, a in key) for key in ev), default=0)
    lll = sum(math.log1p(-2 * pr) for pr in ev.values())
    print(f"(d) max neighbourhood sum 2*sum_w <= {nb:.4f} (2kc0={2*k*c0:.4f}); log prod(1-2P) = {lll:.3f}, -2.07*S = {-2.07*Stot:.3f}")
    # (c) (I) by actual CRT integers
    free = [l for l in P if l not in Pi]
    mods = [(8, 1)] + [(l ** e[l], 1) for l in P if l in Pi and l != 2]
    Q = 1
    for mm, _ in mods: Q *= mm
    print(f"    log Q_Pi = {math.log(Q):.1f}; 840|Q: {Q % 840 == 0}; Q>T: {Q > T}")
    by_max = {}
    for key in ev:
        by_max.setdefault(max(p for p, x, a in key), []).append(key)
    Rs = {M: Rset(M) for M in range(3, T + 1, 4)}
    def crt_n(Xs):
        n, mod = 0, 1
        for mm, a in mods + [(l ** e[l], Xs[l]) for l in free]:
            t = ((a - n) * pow(mod, -1, mm)) % mm
            n += mod * t; mod *= mm
        return n
    def occurs(Xs):
        return any(all(Xs[p] % p ** x == a for p, x, a in key) for key in ev)
    def W_gt_T(n):
        return all((n % M) not in Rs[M] for M in Rs)
    def unit(l):
        q = l ** e[l]
        while True:
            a = rng.randrange(1, q)
            if a % l: return a
    mism = 0; nsurv_ok = 0
    for _ in range(nsurv):
        while True:
            Xs = {}; ok = True
            for l in free:
                q = l ** e[l]; forb = set()
                for key in by_max.get(l, []):
                    if all(Xs[p] % p ** x == a for p, x, a in key if p != l):
                        x_l, a_l = [(x, a) for p, x, a in key if p == l][0]
                        for t in range(a_l, q, l ** x_l): forb.add(t)
                if len(forb) >= q - q // l: ok = False; break
                while True:
                    a = unit(l)
                    if a not in forb: break
                Xs[l] = a
            if ok: break
        assert not occurs(Xs)
        n = crt_n(Xs)
        if W_gt_T(n): nsurv_ok += 1
        else: mism += 1
    print(f"(c) forced survivors: {nsurv}, with W(n)>T: {nsurv_ok}, mismatches: {mism}")
    agree = 0; occ = 0
    for _ in range(nrand):
        Xs = {l: unit(l) for l in free}
        o = occurs(Xs); occ += o
        n = crt_n(Xs)
        agree += (W_gt_T(n) == (not o))
    print(f"    random n=1(Q): {nrand}, events occurred in {occ}, [no event] == [W>T] in {agree}/{nrand}")

if __name__ == "__main__":
    main()
