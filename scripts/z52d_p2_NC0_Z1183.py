#!/usr/bin/env python3
"""Z1183: arc consistency (GAC) on factor domains for the 2-equation divisor model.

Setting. For prime p = 1 mod 4 and x >= ceil(p/4), put r = 4x - p, M = p x, and
  y = (e+M)/r, z = (f+M)/r  with  e*f = M^2,  e = r y - M,  f = r z - M.
So 4/p = 1/x+1/y+1/z has a solution with this x iff some divisor e of M^2 satisfies
  (A) e = prod q^{i_q}  = -M (mod r)     and   (B) f = prod q^{2a_q - i_q} = -M (mod r),
where M^2 = prod q^{2a_q}. The variables are the exponents i_q in [0, 2a_q], one per prime
q | M. Constraints A, B are global multiplicative congruences mod r.

Propagation. GAC for a global product constraint over monoid Z_r: value v of variable q is
supported iff -M is attainable (mod r) by the product of the other variables with q^v.
Attainable sets are computed by prefix/suffix DPs over residue sets (no divisor listing).
AC iterated to fixpoint over A and B.

Checks. (1) soundness: every exhaustive solution e survives propagation; (2) pruning amount;
(3) how often propagation alone refutes a window (empty domain) without any enumeration.
Exhaustive enumeration is used only as ground truth for the check, not by the propagator.
"""
import sys, time, json
import numpy as np

def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]

def attain_mul(S, c, r):
    """residues {s*c mod r : s in S}"""
    idx = np.nonzero(S)[0]
    out = np.zeros(r, bool)
    out[(idx * c) % r] = True
    return out

def gac_product(qs, doms, pw, r, target):
    """Generalized arc consistency for constraint prod_q q^{v_q} == target (mod r).
    qs: list of primes; doms: list of boolean arrays over exponents; pw[k][j] = q_k^j mod r.
    Returns True if consistent (no empty domain), updates doms in place (returns status)."""
    K = len(qs)
    # value image of exponent j of variable k: pw[k][j]
    # prefix sets: pre[k] = attainable residues from variables < k
    pre = [None] * (K + 1)
    suf = [None] * (K + 1)
    changed = True
    while changed:
        changed = False
        pre[0] = np.zeros(r, bool); pre[0][1 % r] = True
        for k in range(K):
            new = np.zeros(r, bool)
            for j in np.nonzero(doms[k])[0]:
                new |= attain_mul(pre[k], pw[k][j], r)
            pre[k + 1] = new
        suf[K] = np.zeros(r, bool); suf[K][1 % r] = True
        for k in range(K - 1, -1, -1):
            new = np.zeros(r, bool)
            for j in np.nonzero(doms[k])[0]:
                new |= attain_mul(suf[k + 1], pw[k][j], r)
            suf[k] = new
        if not pre[K][target % r]:
            return False
        for k in range(K):
            # residues attainable by the others: combine pre[k] and suf[k+1]
            others = np.zeros(r, bool)
            for s in np.nonzero(pre[k])[0]:
                others |= attain_mul(suf[k + 1], s, r)
            need = target % r
            for j in np.nonzero(doms[k])[0]:
                # value j supported iff some residue o of the others gives o * q^j == target (mod r)
                if not attain_mul(others, pw[k][j], r)[need]:
                    doms[k][j] = False
                    changed = True
            if not doms[k].any():
                return False
    return True

def exhaustive_solutions(p, x, qs, es, r, M):
    """ground truth: all exponent vectors (divisors e of M^2) with e = -M and f = -M mod r"""
    sols = []
    ranges = [range(2 * a + 1) for a in es]
    import itertools
    for iv in itertools.product(*ranges):
        e = 1
        f = 1
        for q, a, i in zip(qs, es, iv):
            e *= q ** i; f *= q ** (2 * a - i)
        if (e + M) % r == 0 and (f + M) % r == 0:
            sols.append(iv)
    return sols

def run(pmax=2000, K=40):
    primes = [int(q) for q in primes_upto(pmax) if q % 4 == 1 and q >= 5]
    stats = dict(windows=0, refuted_by_gac=0, windows_with_solution=0, soundness_violations=0,
                 values_total=0, values_removed=0, gac_refuted_but_solvable=0, prime_pass=0)
    per_p = []
    t0 = time.time()
    for p in primes:
        x0 = -(-p // 4)
        p_refuted = 0; p_solvable_x = []
        for x in range(x0, x0 + K):
            r = 4 * x - p
            if r <= 0:
                continue
            M = p * x
            fM = factor(M)
            fM2 = {q: 2 * a for q, a in fM.items()}
            qs = sorted(fM2)
            es = [fM2[q] // 2 for q in qs]          # exponent in M, so M^2 has 2*es
            # variables: exponent of q in e is i in [0, 2*es]
            ks = [2 * a for a in es]
            # prime q may divide r: then powers mod r are not invertible: handled by gac_product
            pw = []
            for q, kmax in zip(qs, ks):
                row = np.zeros(kmax + 1, dtype=np.int64)
                v = 1 % r
                for j in range(kmax + 1):
                    row[j] = v; v = (v * q) % r
                pw.append(row)
            doms = [np.ones(kmax + 1, bool) for kmax in ks]
            total_vals = sum(len(d) for d in doms)
            # baseline: root-level test only (is -M attainable by the full product, for A and for B)?
            # (full domains: the B-side root test is the same set as the A-side one, since divisor
            #  sets are closed under e -> M^2/e; we still run both for transparency)
            root_A = gac_product(qs, [d.copy() for d in doms], pw, r, (-M) % r)
            root_B = gac_product(qs, [d[::-1].copy() for d in doms], [row[::-1].copy() for row in pw], r, (-M) % r)
            root_ok = root_A and root_B
            if not root_ok:
                stats["refuted_at_root_no_pruning"] = stats.get("refuted_at_root_no_pruning", 0) + 1
            stats["windows"] += 1
            stats["values_total"] += total_vals
            # constraint A: prod q^{i} == -M ; constraint B: prod q^{2a-i} == -M (mod r)
            # B is expressed with exponent j' = 2a - i: reverse the per-variable domain/power rows.
            pwA = pw
            pwB = [row[::-1].copy() for row in pw]
            domsA = [d for d in doms]
            ok = True
            # iterate A and B to a joint fixpoint over one shared domain set
            changed = True
            while changed and ok:
                before = sum(int(d.sum()) for d in doms)
                ok_a = gac_product(qs, [d for d in doms], pwA, r, (-M) % r)
                if not ok_a:
                    ok = False; break
                # B on reversed domains (exponent of f): map back
                rev = [d[::-1].copy() for d in doms]
                ok_b = gac_product(qs, rev, pwB, r, (-M) % r)
                if not ok_b:
                    ok = False; break
                for k in range(len(doms)):
                    doms[k] &= rev[k][::-1]
                after = sum(int(d.sum()) for d in doms)
                changed = after != before
            if ok:
                removed = total_vals - sum(int(d.sum()) for d in doms)
                stats["values_removed"] += removed
            if not ok:
                stats["refuted_by_gac"] += 1
                if root_ok:
                    stats["refuted_only_by_pruning"] = stats.get("refuted_only_by_pruning", 0) + 1
                p_refuted += 1
            # ground truth (small instances only to stay within budget)
            ntot = 1
            for kmax in ks:
                ntot *= (kmax + 1)
            if ntot <= 200000:
                stats["ground_truth_windows"] = stats.get("ground_truth_windows", 0) + 1
                sols = exhaustive_solutions(p, x, qs, es, r, M)
                if not sols and ok:
                    stats["survivor_but_unsolvable"] = stats.get("survivor_but_unsolvable", 0) + 1
                if sols:
                    stats["windows_with_solution"] += 1
                    p_solvable_x.append(x)
                    for k, i in enumerate(qs):
                        pass
                    for iv in sols:
                        for k, ii in enumerate(iv):
                            if not doms[k][ii]:
                                stats["soundness_violations"] += 1
                    if not ok:
                        stats["gac_refuted_but_solvable"] += 1
        if p_refuted == K and not p_solvable_x:
            stats["prime_pass"] += 1
        per_p.append((p, p_refuted, len(p_solvable_x)))
    stats["seconds"] = round(time.time() - t0, 1)
    return stats, per_p

if __name__ == "__main__":
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    stats, per_p = run(pmax, K)
    print(json.dumps(stats, indent=1))
    refuted_p = sum(1 for p, rf, s in per_p if rf == K)
    sol_p = sum(1 for p, rf, s in per_p if s > 0)
    print("primes:", len(per_p), "primes with every window GAC-refuted:", refuted_p,
          "primes with an exhaustive-solvable window:", sol_p)
    unsolved = [p for p, rf, s in per_p if s == 0]
    print("primes with no solvable window in the scanned x-range:", unsolved[:30])
    json.dump({"stats": stats, "per_p": per_p, "pmax": pmax, "K": K},
              open(f"data/z52b/pass2/NC0/sub/Z1183_gac_{pmax}_{K}.json", "w"))
