"""Numerics for EXCEPTIONAL_BALANCED.md §3 (route 8): the REAL Case-B forced-class
system  R(M) = {-4D mod M : D | ((M+1)/4)^2},  M = 3 (mod 4),  M <= X.  EVIDENCE only.

Moduli classified by P = P(M), P2 = P(M/P):
  dom   : P >= M^(2/3)                       (dominant, C = 1/2)
  gap   : not dom, P >= P2^(1+eta)           (eta-gapped, includes balanced gapped)
  twin  : P < P2^(1+eta)                     (eta-twin; contains P^2 | M)
(also flag bal = P <= sqrt(M)).

Part (i):  sequential histories with singleton windows (primes in increasing
order; at prime p the residue n mod p^e is uniform among residues completing no
condition with top prime p).  This is Q_seq of ET §2.6 with one prime per window.
Records p_p(h) = |F_p(h)|/p^e, split by class type, for every p, plus the uniform
masses M_p = sum_{P(M)=p} |R(M)|/M and an adversarial greedy search for large
p_l(h) over reachable histories.

Run:  uv run python scripts/balanced_numerics.py i [X] [samples] [eta]
"""
import math
import random
import sys
from collections import defaultdict

import numpy as np


def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == 0:
            s = spf[p * p::p]
            s[s == 0] = p
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx
    return spf


def factor(n, spf):
    f = {}
    while n > 1:
        p = int(spf[n])
        f[p] = f.get(p, 0) + 1
        n //= p
    return f


def divisors_of_square(fa):
    ds = [1]
    for p, e in fa.items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return ds


def build_system(X, eta):
    """Return dict top prime p -> list of (q, c mod q, c mod p^v, v, type, M)."""
    spf = spf_sieve(X + 1)
    for n in range(2, X + 1):
        pass
    sysd = defaultdict(list)
    maxexp = defaultdict(int)
    stats = defaultdict(float)
    for M in range(3, X + 1, 4):
        fM = factor(M, spf)
        for p, e in fM.items():
            maxexp[p] = max(maxexp[p], e)
        P = max(fM)
        q = M // P ** fM[P]
        rest = M // P
        P2 = max(factor(rest, spf)) if rest > 1 else 1
        if P >= M ** (2 / 3):
            t = "dom"
        elif P >= P2 ** (1 + eta):
            t = "gapB" if P * P <= M else "gapM"
        else:
            t = "twin"
        A = (M + 1) // 4
        cls = sorted({(-4 * D) % M for D in divisors_of_square(factor(A, spf))})
        pv = P ** fM[P]
        for c in cls:
            sysd[P].append((q, c % q, c % pv, fM[P], t, M))
        stats[t] += len(cls) / M
    return sysd, maxexp, stats


def sample_history(sysd, primes, maxexp, rng, record):
    """One Q_seq sample with singleton windows; record(p, pe, F, Ftype) per prime."""
    n, L = 0, 1
    for p in primes:
        e = maxexp[p]
        pe = p ** e
        forb = set()
        ftype = defaultdict(set)
        qcache = {}
        for (q, cq, cv, v, t, M) in sysd.get(p, ()):
            r = qcache.get(q)
            if r is None:
                r = n % q
                qcache[q] = r
            if r == cq:
                step = p ** v
                for r2 in range(cv, pe, step):
                    forb.add(r2)
                    ftype[t].add(r2)
        record(p, pe, forb, ftype)
        allowed = pe - len(forb)
        assert allowed > 0, ("dead end", p)
        while True:
            r = rng.randrange(pe)
            if r not in forb:
                break
        # CRT: n mod L, r mod pe
        inv = pow(L, -1, pe)
        n = n + L * (((r - n) * inv) % pe)
        L *= pe
    return n


TYPES = ("dom", "gapM", "gapB", "twin")


def factor_small(q):
    f = {}
    d = 2
    while d * d <= q:
        while q % d == 0:
            f[d] = f.get(d, 0) + 1
            q //= d
        d += 1
    if q > 1:
        f[q] = f.get(q, 0) + 1
    return f


def part_i(X=100000, samples=200, eta=0.25, seed=1, steer_tries=3):
    rng = random.Random(seed)
    sysd, maxexp, stats = build_system(X, eta)
    primes = sorted(maxexp)
    Mu = defaultdict(lambda: defaultdict(float))
    for p, lst in sysd.items():
        for (q, cq, cv, v, t, M) in lst:
            Mu[p][t] += 1.0 / M
    acc = defaultdict(lambda: defaultdict(list))

    def record(p, pe, forb, ftype):
        acc[p]["all"].append(len(forb) / pe)
        for t in TYPES:
            acc[p][t].append(len(ftype.get(t, ())) / pe)

    for _ in range(samples):
        sample_history(sysd, primes, maxexp, rng, record)
    out = [f"# part (i)  X={X} samples={samples} eta={eta}",
           "# uniform total mass by type: " +
           " ".join(f"{t}={stats[t]:.3f}" for t in TYPES),
           "# band [a,b) of top primes p > 30 | type | sum Mu | sum E_seq p | K=ratio |"
           " max_p max_h p(h) | max_p max_h p(h)*sqrt(p) | frac(p(h)>1/4)"]
    lo = 32
    while lo <= X:
        band = [p for p in primes if lo <= p < 2 * lo and acc[p]["all"]]
        for t in TYPES + ("all",):
            mu = sum(sum(Mu[p].values()) if t == "all" else Mu[p][t] for p in band)
            if mu == 0:
                continue
            ep = sum(np.mean(acc[p][t]) for p in band)
            mx = max(max(acc[p][t]) for p in band)
            mxs = max(max(acc[p][t]) * p ** 0.5 for p in band)
            hv = np.mean([x > 0.25 for p in band for x in acc[p][t]])
            out.append(f"[{lo},{2*lo}) {t:5s} | {mu:.3e} | {ep:.3e} | {ep/mu:5.2f} |"
                       f" {mx:.3e} | {mxs:.3f} | {hv:.3f}")
        lo *= 2
    # adversarial steered histories at primes carrying twin/gapB mass
    cand = sorted((p for p in primes if p > 30 and Mu[p]["twin"] + Mu[p]["gapB"] > 0),
                  key=lambda p: -(Mu[p]["twin"] + Mu[p]["gapB"]))[:8]
    out.append("# steered (adversarial, valid) histories: p | Mu_p(all) | "
               "mean seq p(h) | best steered p(h) over tries | p^-1/2")
    for p in sorted(cand):
        best = max(steered_history(sysd, maxexp, p, rng) for _ in range(steer_tries))
        out.append(f"{p:6d} | {sum(Mu[p].values()):.3e} | {np.mean(acc[p]['all']):.3e} |"
                   f" {best:.3e} | {p**-0.5:.3e}")
    return out


def steered_history(sysd, maxexp, ell, rng):
    """Adversarial but VALID history: Q_seq-support path (each residue avoids all
    conditions with that top prime) steered to keep as many distinct target values
    at ell alive as possible.  Returns |F_ell(h)|/ell^e for the final history."""
    primes = sorted(p for p in maxexp if p < ell)
    target = list(sysd.get(ell, []))
    alive = target[:]
    n, L = 0, 1
    for p in primes:
        e = maxexp[p]
        pe = p ** e
        # forbidden residues at p (conditions with top prime p)
        forb = set()
        qcache = {}
        for (q, cq, cv, v, t, M) in sysd.get(p, ()):
            r = qcache.get(q)
            if r is None:
                r = qcache[q] = n % q
            if r == cq:
                forb.update(range(cv, pe, p ** v))
        inv = [(c, factor_small(c[0]).get(p, 0)) for c in alive]
        vmax = max([k for _, k in inv] + [0])
        if vmax == 0:
            while True:
                r = rng.randrange(pe)
                if r not in forb:
                    break
        else:
            pv = p ** vmax
            score = defaultdict(set)
            free_vals = set(c[2] % ell for c, k in inv if k == 0)
            for r0 in range(pv):
                score[r0] = set(free_vals)
            for c, k in inv:
                if k:
                    need = c[1] % p ** k
                    for r0 in range(need, pv, p ** k):
                        score[r0].add(c[2] % ell)
            ranked = sorted(range(pv), key=lambda r0: -len(score[r0]))
            r = None
            for r0 in ranked:
                lifts = [x for x in range(r0, pe, pv) if x not in forb]
                if lifts:
                    r = rng.choice(lifts)
                    break
            assert r is not None, "dead end"
        n = n + L * (((r - n) * pow(L, -1, pe)) % pe)
        L *= pe
        alive = [c for c in alive if (n - c[1]) % math.gcd(c[0], L) == 0]
    vals = {c[2] % ell for c in target if n % c[0] == c[1]}
    return len(vals) / ell


if __name__ == "__main__" and False:
    part = sys.argv[1] if len(sys.argv) > 1 else "i"
    if part == "i":
        X = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
        S = int(sys.argv[3]) if len(sys.argv) > 3 else 200
        eta = float(sys.argv[4]) if len(sys.argv) > 4 else 0.25
        print("\n".join(part_i(X, S, eta)))


# ---------------------------------------------------------------- part (ii)
def window_system(S):
    """Exact CRT space Z/Q, Q = prod(S) (S distinct odd primes).  Returns
    residues table, list of conditions (U, M, classes) for squarefree M | Q,
    M = 3 mod 4, classes R(M)."""
    from itertools import combinations
    S = sorted(S)
    Q = math.prod(S)
    idx = np.arange(Q, dtype=np.int64)
    # point index i <-> integer n = i (CRT is a bijection Z/Q -> prod Z/p)
    res = {p: idx % p for p in S}
    conds = []
    for r in range(1, len(S) + 1):
        for U in combinations(S, r):
            M = math.prod(U)
            if M % 4 != 3:
                continue
            A = (M + 1) // 4
            fa = factor_small(A)
            cls = sorted({(-4 * D) % M for D in divisors_of_square(fa)})
            conds.append((U, M, cls))
    return S, Q, idx, res, conds


def avoid_mask(Q, idx, conds, which):
    ok = np.ones(Q, dtype=bool)
    for (U, M, cls) in conds:
        if not which(U):
            continue
        r = idx % M
        ok &= ~np.isin(r, cls)
    return ok


def lp_saving(S, Q, res, A, m):
    """max sigma(A) over probability sigma on Z/Q with uniform marginals on every
    m-subset of S (= min mean of level-m majorant, by LP duality)."""
    from itertools import combinations
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    if m >= len(S):
        return -math.log(A.mean())
    rows, cols = [], []
    b = []
    r0 = 0
    for T in combinations(S, m):
        key = np.zeros(Q, dtype=np.int64)
        size = 1
        for p in T:
            key = key * p + res[p]
            size *= p
        rows.append(r0 + key)
        cols.append(np.arange(Q))
        b.extend([1.0 / size] * size)
        r0 += size
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    Aeq = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(r0, Q)).tocsr()
    c = -A.astype(float)
    sol = linprog(c, A_eq=Aeq, b_eq=np.array(b), bounds=(0, None), method="highs")
    assert sol.status == 0, sol.message
    return -math.log(-sol.fun)


def rankin(S, conds, which, m):
    lam = sum(sorted(math.log(p) for p in S)[-m:])
    terms = [(len(cls) / M, math.log(M)) for (U, M, cls) in conds if which(U)]
    best = float("inf")
    for a in np.linspace(0, 3, 601):
        best = min(best, a * lam + sum(w * math.exp(-a * s) for w, s in terms))
    return best


def part_ii(S, mmax):
    S, Q, idx, res, conds = window_system(S)
    fams = {"D(single primes)": lambda U: len(U) == 1,
            "D+B(all)": lambda U: True}
    out = [f"# part (ii) window S={S} Q={Q}; conditions: " +
           ", ".join(f"{M}:{len(c)}" for U, M, c in conds)]
    for name, w in fams.items():
        A = avoid_mask(Q, idx, conds, w)
        mass = sum(len(c) / M for U, M, c in conds if w(U))
        line = [f"{name:18s} mass={mass:.3f} void={-math.log(A.mean()):.3f}"]
        for m in range(1, mmax + 1):
            s = lp_saving(S, Q, res, A, m)
            line.append(f"m={m}: LP={s:.3f} Rankin={rankin(S, conds, w, m):.3f}")
        out.append(" | ".join(line))
    return out


if __name__ == "__main__":
    part = sys.argv[1]
    if part == "i":
        X = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
        S_ = int(sys.argv[3]) if len(sys.argv) > 3 else 200
        eta = float(sys.argv[4]) if len(sys.argv) > 4 else 0.25
        print("\n".join(part_i(X, S_, eta)))
    elif part == "ii":
        S = [int(x) for x in sys.argv[2].split(",")]
        mmax = int(sys.argv[3]) if len(sys.argv) > 3 else 3
        print("\n".join(part_ii(S, mmax)))


def part_steer(X, plist, tries, eta=0.25, seed=3):
    rng = random.Random(seed)
    sysd, maxexp, stats = build_system(X, eta)
    out = [f"# steered histories X={X} tries={tries}: p | Mu_p by type (dom,gapM,gapB,twin) |"
           " best p(h) | best p(h)*sqrt(p)"]
    for p in plist:
        mu = defaultdict(float)
        for (q, cq, cv, v, t, M) in sysd.get(p, ()):
            mu[t] += 1.0 / M
        best = max(steered_history(sysd, maxexp, p, rng) for _ in range(tries))
        out.append(f"{p:6d} | " + " ".join(f"{mu[t]:.2e}" for t in TYPES) +
                   f" | {best:.3e} | {best * p ** 0.5:.3f}")
    return out


if __name__ == "__main__" and sys.argv[1] == "steer":
    print("\n".join(part_steer(int(sys.argv[2]), [int(x) for x in sys.argv[3].split(",")],
                               int(sys.argv[4]))))
