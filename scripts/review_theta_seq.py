"""Exact-LP test of Theorem 2.7 (sequential windows, shared large primes).

Reviewer's own code.  Small CRT systems with Q0 = 4, slice primes {5,7,11,13}
split into windows W1 = {5,7}, W2 = {11,13}.  Conditions at a W2 prime may
also fix a residue modulo a W1 prime (shared large primes) and modulo q | Q0.

Checks the rigorous intermediate of the proof of Theorem 2.7, with the
exact Boolean window LP W_j(h) in place of Proposition 2.4:
    E nu  >=  (1/Q0) sum_{c in R} W_1(c) * exp( E_Qseq[ log W_2(H_{<2}) | c ] )
          >=  (|R|/Q0) exp( avg_c [ log W_1(c) + E_Qseq[log W_2 | c] ] )
against the exact CRT LP optimum.  Also checks Lemma 2.8's bound on
E_Qseq p_l(H) and reports the final Theorem 2.7 bound (2.6).

Run: PYTHONPATH=scripts uv run --with scipy python scripts/review_theta_seq.py
"""
import itertools
import math
import random

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog

from review_theta_lp import bool_lp, best_rhs

Q0 = 4
R = [1, 3]
W1 = [5, 7]
W2 = [11, 13]
P = W1 + W2
QT = Q0 * math.prod(P)


def avoid_mask(conds):
    n = np.arange(QT)
    ok = np.isin(n % Q0, R)
    for (q, a, req) in conds:
        hit = (n % q) == a
        for l, b in req.items():
            hit &= (n % l) == b
        ok &= ~hit
    return ok


def crt_lp(avoid, lam):
    n = np.arange(QT)
    allowed = [T for k in range(len(P) + 1) for T in itertools.combinations(P, k)
               if sum(math.log(l) for l in T) <= lam + 1e-12]
    maximal = [T for T in allowed if not any(set(T) < set(U) for U in allowed)]
    cols, obj, off = [], [], 0
    for T in maximal:
        m = Q0 * math.prod(T)
        cols.append((off, m)); obj += [1.0 / m] * m; off += m
    rows = np.concatenate([n for _ in cols])
    colidx = np.concatenate([o + n % m for (o, m) in cols])
    A = sp.csr_matrix((np.ones(len(rows)), (rows, colidx)), shape=(QT, off))
    b = np.where(avoid, -1.0, 0.0)
    for meth in ("highs-ds", "highs-ipm"):
        res = linprog(np.array(obj), A_ub=-A, b_ub=b, bounds=[(None, None)] * off, method=meth)
        if res.status == 0:
            return res.fun
    return None


def F_sets(conds, c, hist):
    """Forbidden residues at each prime given c and W1-residues hist (dict) or None."""
    out = {l: set() for l in P}
    for (q, a, req) in conds:
        if c % q != a:
            continue
        lastw = W2 if any(l in W2 for l in req) else W1
        lc = [l for l in req if l in lastw]
        assert len(lc) == 1  # (U)
        lc = lc[0]
        if lastw is W1:
            out[lc].add(req[lc])
        elif hist is not None:
            if all(hist[l] == b for l, b in req.items() if l != lc):
                out[lc].add(req[lc])
    return out


def gen(rng):
    while True:
        conds = []
        for l in W1:
            for _ in range(rng.randint(0, 2)):
                q = rng.choice([1, 2, 4]); conds.append((q, rng.randrange(q), {l: rng.randrange(l)}))
        for l in W2:
            for _ in range(rng.randint(1, 7)):
                q = rng.choice([1, 2, 4])
                req = {l: rng.randrange(l)}
                for lp in W1:
                    if rng.random() < 0.6:
                        req[lp] = rng.randrange(lp)
                conds.append((q, rng.randrange(q), req))
        # hypothesis p <= 1/4 on Qseq support (all reachable histories)
        ok = True
        for c in R:
            F1 = F_sets(conds, c, None)
            if any(len(F1[l]) > l / 4 for l in W1):
                ok = False
            for hv in itertools.product(*[range(l) for l in W1]):
                hist = dict(zip(W1, hv))
                if any(hist[l] in F1[l] for l in W1):
                    continue
                F2 = F_sets(conds, c, hist)
                if any(len(F2[l]) > l / 4 for l in W2):
                    ok = False
        if ok:
            return conds


def chain(conds, lam):
    s = {l: math.log(l) for l in P}
    tot_tight, avg_log, phi_sum = 0.0, 0.0, 0.0
    lemma28_ok = True
    for c in R:
        F1 = F_sets(conds, c, None)
        p1 = [len(F1[l]) / l for l in W1]
        Wc1 = bool_lp(p1, [s[l] for l in W1], lam)
        Elog2, Ephi2 = 0.0, 0.0
        Ep2 = {l: 0.0 for l in W2}
        for hv in itertools.product(*[range(l) for l in W1]):
            hist = dict(zip(W1, hv))
            if any(hist[l] in F1[l] for l in W1):
                continue
            pr = math.prod(1.0 / (l - len(F1[l])) for l in W1)
            F2 = F_sets(conds, c, hist)
            p2 = [len(F2[l]) / l for l in W2]
            Elog2 += pr * math.log(bool_lp(p2, [s[l] for l in W2], lam))
            for l, pl in zip(W2, p2):
                Ep2[l] += pr * pl
        tot_tight += Wc1 * math.exp(Elog2) / Q0
        avg_log += (math.log(Wc1) + Elog2) / len(R)
        # Lemma 2.8 bound, for this c (P(c = a mod q | c) is 0/1 here)
        pstar = {l: max(len(F_sets(conds, cc, None)[l]) / l for cc in R) for l in W1}
        for l in W2:
            bnd = 0.0
            for (q, a, req) in conds:
                if l in req and c % q == a:
                    bnd += (1 / l) * math.prod(1 / (lp * (1 - pstar[lp])) for lp in req if lp != l)
            if Ep2[l] > bnd + 1e-12:
                lemma28_ok = False
    return tot_tight, len(R) / Q0 * math.exp(avg_log), lemma28_ok


if __name__ == "__main__":
    rng = random.Random(5)
    for trial in range(8):
        conds = gen(rng)
        avoid = avoid_mask(conds)
        for lam in [math.log(7), math.log(13), math.log(77), math.log(143)]:
            W = crt_lp(avoid, lam)
            if W is None:
                print("  solver failure; skipped"); continue
            tight, jens, l28 = chain(conds, lam)
            ok = W >= tight * (1 - 1e-9) and tight >= jens * (1 - 1e-9) and l28
            print(f"trial {trial} #conds={len(conds)} lam=e^{math.exp(lam):.0f}: -log W_CRT={-math.log(W):.4f} "
                  f"chain={-math.log(tight):.4f} chain+Jensen={-math.log(jens):.4f} void={-math.log(avoid.mean()):.4f} "
                  f"Lemma2.8={'ok' if l28 else 'FAIL'} {'ok' if ok else 'FAIL'}", flush=True)
            assert ok
