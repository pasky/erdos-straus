#!/usr/bin/env python3
"""POINTWISE_OMEGA3 §3 (EVIDENCE): brute-force check of the two-level composition.

Random small product spaces (coordinates l with alphabets [m_l], uniform), a random
"level-2" family (singles and edges) and a random "level-3" family (events on 2..3
coordinates).  B_3 := B_{L3} - 4^{L3+1} G_{L3+1} (O2 Lemma 1.2) for level 3, expanded
into cells; for each cell the cell-conditioned level-2 system (induced singles,
killed cells) and beta_i, alpha_i := B_{L2} -/+ 4^{L2+1} G_{L2+1}; then
  B := sum_{c_i>0} c_i beta_i 1_{C_i} - sum_{c_i<0} |c_i| alpha_i 1_{C_i}.
Checks, for every outcome x:  B(x) <= F2(x) F3(x)  (Thm 3.2 item 1), and
beta_i <= F2^{(i)} <= alpha_i on each cell; reports the mean deficit E[F2F3 - B].
All functions are dicts {cell: coeff}, a cell being a frozenset of (coord, value).

usage: omega3_compose_check.py trials seed [neg]
  neg: negative control (beta used also for negative coefficients; violations expected)
"""
import itertools
import random
import sys
from math import comb

NEG = False


def consistent_union(cells):
    d = {}
    for c in cells:
        for l, v in c:
            if d.get(l, v) != v:
                return None
            d[l] = v
    return frozenset(d.items())


def supp(c):
    return frozenset(l for l, _ in c)


def BL_cells(events, L):
    """cell expansion of B_L = sum_{F subset A, |supp F|<=L} (-1)^|F| (O2 Lemma 1.3(2))."""
    out = {}
    for F in powerset_small(events, L):
        u = consistent_union(F)
        if u is None or len(supp(u)) > L:
            continue
        out[u] = out.get(u, 0) + (-1) ** len(F)
    return {c: v for c, v in out.items() if v}


def powerset_small(events, L):
    # all subfamilies whose support union has size <= L (events have support >=1)
    n = len(events)
    res = [()]
    def rec(start, cur, s):
        for i in range(start, n):
            s2 = s | supp(events[i])
            if len(s2) <= L:
                nxt = cur + (events[i],)
                res.append(nxt)
                rec(i + 1, nxt, s2)
    rec(0, (), frozenset())
    return res


def G_cells(events, coords, L1):
    """e_{L1}(a), a_l = #{occurring events containing l}, as a +combination of cells."""
    out = {}
    by = {l: [e for e in events if l in supp(e)] for l in coords}
    for P in itertools.combinations(coords, L1):
        for choice in itertools.product(*[by[l] for l in P]):
            u = consistent_union(choice)
            if u is not None:
                out[u] = out.get(u, 0) + 1
    return out


def evaluate(fn, x):
    return sum(v for c, v in fn.items() if all(x[l] == val for l, val in c))


def occurs(e, x):
    return all(x[l] == v for l, v in e)


def condition(events, cell):
    """cell-conditioned system: returns (killed, new_events)."""
    fixed = dict(cell)
    new = []
    for e in events:
        rest, ok = [], True
        for l, v in e:
            if l in fixed:
                if fixed[l] != v:
                    ok = False
                    break
            else:
                rest.append((l, v))
        if not ok:
            continue
        if not rest:
            return True, None
        new.append(frozenset(rest))
    return False, list(set(new))


def trial(rng):
    k = rng.randint(3, 5)
    coords = list(range(k))
    m = {l: rng.randint(2, 3) for l in coords}
    def rand_event(size):
        ls = rng.sample(coords, size)
        return frozenset((l, rng.randrange(m[l])) for l in ls)
    lev2 = list({rand_event(rng.choice([1, 2])) for _ in range(rng.randint(0, 4))})
    lev3 = list({rand_event(rng.choice([2, 3])) for _ in range(rng.randint(1, 4))})
    L3, L2 = rng.randint(0, 3), rng.randint(0, 3)
    B3 = BL_cells(lev3, L3)
    for c, v in G_cells(lev3, coords, L3 + 1).items():
        B3[c] = B3.get(c, 0) - 4 ** (L3 + 1) * v
    B = {}
    checks = []
    for C, ci in B3.items():
        if ci == 0:
            continue
        killed, sys2 = condition(lev2, C)
        if killed:
            continue
        rest = [l for l in coords if l not in supp(C)]
        Bl = BL_cells(sys2, L2)
        G = G_cells(sys2, rest, L2 + 1)
        sign = 1 if ci > 0 else -1
        part = dict(Bl)
        for c, v in G.items():
            part[c] = part.get(c, 0) - (1 if NEG else sign) * 4 ** (L2 + 1) * v
        checks.append((C, sys2, part, sign))
        for c, v in part.items():
            u = consistent_union([c, C])
            B[u] = B.get(u, 0) + ci * v
    bad = 0
    deficit = 0.0
    outcomes = list(itertools.product(*[range(m[l]) for l in coords]))
    for xs in outcomes:
        x = dict(zip(coords, xs))
        F2 = 0 if any(occurs(e, x) for e in lev2) else 1
        F3 = 0 if any(occurs(e, x) for e in lev3) else 1
        b = evaluate(B, x)
        if b > F2 * F3 + 1e-9:
            bad += 1
        deficit += F2 * F3 - b
        for C, sys2, part, sign in checks:
            if occurs(C, x):
                f = 0 if any(occurs(e, x) for e in sys2) else 1
                v = evaluate(part, x)
                if not NEG and ((sign > 0 and v > f + 1e-9) or (sign < 0 and v < f - 1e-9)):
                    bad += 1
    return bad, deficit / len(outcomes), len(B)


def main():
    global NEG
    trials, seed = int(sys.argv[1]), int(sys.argv[2])
    NEG = len(sys.argv) > 3 and sys.argv[3] == 'neg'
    rng = random.Random(seed)
    tot_bad, n_cells = 0, 0
    for _ in range(trials):
        bad, d, nc = trial(rng)
        tot_bad += bad
        n_cells += nc
    print(f"trials={trials} seed={seed}: violations={tot_bad} (total composite cells {n_cells})")


if __name__ == "__main__":
    main()
