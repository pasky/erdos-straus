"""R50 from-scratch check of Thm 7.1 (filtration bound) and Remark 7.3 of paper/energy-dnf-note.tex.
Usage: PYTHONPATH=scripts uv run python scripts/review_r50_filt.py SEED NCASES
"""
import math, random, sys
from fractions import Fraction as Fr
from review_r50_core import es_energies, _prod

LAMS = [Fr(1), Fr(21, 20), Fr(11, 10), Fr(9, 8), Fr(6, 5), Fr(5, 4), Fr(4, 3), Fr(7, 5), Fr(3, 2)]


def run(rng, mode):
    L = rng.randint(1, 2)
    base = [rng.choice([2, 3]) for _ in range(L)]
    i0 = [rng.randint(0, 1) for _ in range(L)]
    f = [i0[l] + rng.randint(1, 2 if L == 2 else 3) for l in range(L)]
    digs = [(l, i) for l in range(L) for i in range(i0[l], f[l])]
    if len(digs) > 4:
        return None
    qs = [base[l] for l, i in digs]
    pis = []
    for q in qs:
        w = [rng.randint(0, 6) for _ in range(q)]
        if sum(w) == 0:
            w[0] = 1
        pis.append([Fr(a, sum(w)) for a in w])
    events = []
    for _ in range(rng.randint(1, 6)):
        v = [rng.randint(0, f[l]) for l in range(L)]
        ev = {}
        for d, (l, i) in enumerate(digs):
            if i < v[l]:
                ev[d] = rng.randrange(base[l])
        events.append((v, ev))
    lam = [rng.choice(LAMS) for _ in range(L)]
    def ok(lam):
        for v, _ in events:
            if mode == "thm":
                if _prod(lam[l] ** (2 * v[l]) for l in range(L)) > 2:
                    return False
            else:  # Remark 7.3 hypothesis sum (lam^v - 1) <= ln 2 (float check of hypothesis only)
                if sum(float(lam[l] ** v[l]) - 1 for l in range(L)) > math.log(2) - 1e-12:
                    return False
        return True
    while not ok(lam):
        l = rng.randrange(L)
        lam[l] = LAMS[max(0, LAMS.index(lam[l]) - 1)]
    import itertools
    pts = list(itertools.product(*[range(q) for q in qs]))
    F = {x: Fr(int(not any(all(x[d] == s for d, s in ev.items()) for _, ev in events))) for x in pts}
    en, _, _ = es_energies(qs, pis, F)
    tot = Fr(0)
    for U, e in en.items():
        w = Fr(1)
        for l in range(L):
            Ul = [digs[d][1] for d in U if digs[d][0] == l]
            if Ul:
                w *= lam[l] ** (1 + max(Ul))
        tot += w * e
    assert tot <= 1, (tot, mode, events, lam, i0, f)
    return tot


if __name__ == "__main__":
    seed, n = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    for mode in ("thm", "rem"):
        mx, c = Fr(0), 0
        while c < n:
            r = run(rng, mode)
            if r is None:
                continue
            c += 1; mx = max(mx, r)
        print(f"{mode}: {n} random digit-prefix systems OK, max weighted energy = {float(mx):.10f}")
