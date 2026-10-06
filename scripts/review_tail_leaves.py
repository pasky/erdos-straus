"""R76 from-scratch check of POINTWISE_TAIL Lemma 3.1 (leaf calculus) on toy square-class processes.
Process: start Q=8, r=1 (8); forced a=0 steps at 3,5,7; then a state-dependent rule (pseudo-random hash
of the revealed digits) picks a step (l,a) among eligible primes {11,13} (levels < cap) or stops.
a=0 step: uniform over the (l-1)/2 nonzero squares mod l; a>=1: uniform over the l lifts.
Checks: (1) every a>=1 lift is a square mod l^(a+1); (2) sum P_proc = 1;
(3) P_proc(L) == 4*2^{k_L}/phi(Q_L), k_L = #odd primes of Q_L; (4) fibres pairwise disjoint and their
union is exactly {n unit mod N : n=1 (8), n square mod every odd prime of Q_L} (enumerated mod N)."""
from fractions import Fraction as Fr
import hashlib, sys, numpy as np
from sympy import totient
CAP = {11: 2, 13: 1}
N = 8 * 3 * 5 * 7 * 11**2 * 13
def sq(l): return sorted({x * x % l for x in range(1, l)})
def rule(state, seed):
    elig = [(l, state.get(l, (0, 0))[0]) for l in CAP if state.get(l, (0, 0))[0] < CAP[l]]
    h = int(hashlib.sha256((repr(sorted(state.items())) + str(seed)).encode()).hexdigest(), 16)
    if not elig or h % 3 == 0: return None
    return elig[h % len(elig)]
def leaves(seed):
    out = []
    def rec(state, prob, forced):
        if forced:
            l = forced[0]; nxt = (l, 0)
        else:
            nxt = rule(state, seed)
        if nxt is None:
            out.append((dict(state), prob)); return
        l, a = nxt
        if a == 0:
            ch = sq(l); p = Fr(1, len(ch)); new = [(1, x) for x in ch]
        else:
            r = state[l][1]; m = l**a
            new = [(a + 1, r + j * m) for j in range(l)]; p = Fr(1, l)
            for _, x in new:  # (1) lifts are squares mod l^(a+1)
                assert any(y * y % (l**(a + 1)) == x for y in range(l**(a + 1))), (l, a, x)
        for st in new:
            s2 = dict(state); s2[l] = st
            rec(s2, prob * p, forced[1:] if forced else forced)
    rec({}, Fr(1), [3, 5, 7])
    return out
def check(seed):
    L = leaves(seed)
    assert sum(p for _, p in L) == 1
    cover = np.zeros(N, dtype=np.int32); n = np.arange(N); unit = np.gcd(n, N) == 1
    for st, p in L:
        Q = 8; mask = (n % 8 == 1) & unit
        for l, (a, r) in st.items():
            Q *= l**a; mask &= (n % l**a == r)
        k = len(st)
        assert p == Fr(4 * 2**k, int(totient(Q))), (st, p)
        cover += mask
    assert cover.max() <= 1
    # expected union: n=1(8), units, square mod each prime that is stepped in the leaf containing n
    # union = units n=1 (8) that are squares mod 3,5,7 (forced) -- Haar mass 1/4 * 2^-3
    expect = unit & (n % 8 == 1)
    for l in (3, 5, 7): expect &= np.isin(n % l, sq(l))
    assert not (cover.astype(bool) & ~expect).any()
    for m in np.nonzero(expect)[0]:   # follow n's own path; covered iff never hits a non-square
        m = int(m); state = {l: (1, m % l) for l in (3, 5, 7)}; lost = False
        while True:
            nxt = rule(state, seed)
            if nxt is None: break
            l, a = nxt
            if a == 0 and (m % l) not in sq(l): lost = True; break
            state[l] = (a + 1, m % l**(a + 1))
        assert cover[m] == (0 if lost else 1), m
    # mass check: Haar mass of union = sum 1/phi(Q_L)
    tot = sum(Fr(1, int(totient(8 * np.prod([l**a for l, (a, r) in st.items()])))) for st, _ in L)
    assert Fr(int(cover.sum()), int(totient(N))) == tot
    return len(L), max(len(st) for st, _ in L)
for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 6):
    print("seed", seed, "leaves, max k:", check(seed), "OK")
