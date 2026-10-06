"""O68 / POINTWISE_OMEGA17 §5: toy support-aware LP vs diffuse LP (EVIDENCE).

Toy sieve: primes l in PS, each with a random set Omega_l of omega_l nonzero residues; bit
z_l(n) = 1[n mod l in Omega_l]; avoider = all bits 0. True measure: primes p <= x, p > max PS.
Information: the EXACT prime counts in every bit-cell {z_I = beta}, |I| <= k (k-juntas), and N_x.
By Lemma 5.1 (aggregation), a support-aware fake on S is a vector M_sigma (sigma in {0,1}^n)
with 0 <= M_sigma <= cap_sigma := #{n in S: z(n) = sigma}; the diffuse fake drops the caps.
We report min M_0 (fake mass on the avoider configuration) for both; a certificate exists iff
min M_0 > 0.  Supports: S1 = max(PS)-rough integers (slack ~1.6), S2 = integers coprime to
prod(PS) (slack ~5).
Usage: uv run --with scipy python scripts/omega17_toylp.py [seed] [x] [frac]
"""
import itertools
import sys

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


def primes_upto(N):
    s = np.ones(N + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def run(seed=1, x=10 ** 6, PS=(17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71),
        frac=0.3, ks=(0, 1, 2, 3)):
    rng = np.random.default_rng(seed)
    n = len(PS)
    ns = np.arange(1, x + 1, dtype=np.int64)
    sig = np.zeros(x, dtype=np.int64)
    probs = []
    for b, l in enumerate(PS):
        om = max(1, int(round(frac * l)))
        Om = rng.choice(np.arange(1, l), size=om, replace=False)
        mem = np.zeros(l, dtype=bool)
        mem[Om] = True
        sig |= mem[ns % l].astype(np.int64) << b
        probs.append(om / (l - 1))
    pr = primes_upto(x)
    pr = pr[pr > max(PS)]
    small = primes_upto(max(PS))
    cop = np.ones(x, dtype=bool)
    for l in PS:
        cop &= ns % l != 0
    rough = cop.copy()
    for q in small:
        rough &= ns % q != 0
    rough[0] = False
    cop[0] = False
    nconf = 1 << n
    truth = np.bincount(sig[pr - 1], minlength=nconf).astype(float)
    caps = {}
    sj = cop.copy()
    for j, q in enumerate([1] + [int(t) for t in small if t < min(PS)]):
        if q > 1:
            sj &= ns % q != 0
        caps[f"slack{sj.sum() / len(pr):.2f}"] = np.bincount(sig[sj], minlength=nconf).astype(float)
    caps["S1(rough)"] = np.bincount(sig[rough], minlength=nconf).astype(float)
    caps["S2(coprime)"] = np.bincount(sig[cop], minlength=nconf).astype(float)
    Nx = truth.sum()
    R = sum(p / (1 - p) for p in probs)
    print(f"seed={seed} x={x} nbits={n} R(odds)={R:.2f} N_x={int(Nx)} prime avoiders={int(truth[0])} "
          f"|S1|={int(caps['S1(rough)'].sum())} |S2|={int(caps['S2(coprime)'].sum())}", flush=True)
    confs = np.arange(nconf)
    out = []
    for k in ks:
        rows, cols, rhs = [], [], []
        r = 0
        for s in range(k + 1):
            for I in itertools.combinations(range(n), s):
                mask = sum(1 << b for b in I)
                key = confs & mask
                tkey = np.bincount(key, weights=truth, minlength=nconf)
                for beta in np.unique(key):
                    idx = np.nonzero(key == beta)[0]
                    rows.append(np.full(len(idx), r))
                    cols.append(idx)
                    rhs.append(tkey[beta])
                    r += 1
        A = sp.csr_matrix((np.ones(sum(len(c) for c in cols)), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(r, nconf))
        b = np.array(rhs)
        c = np.zeros(nconf)
        c[0] = 1.0
        res = {}
        for name, ub in [("diffuse", None)] + list(caps.items()):
            bounds = np.column_stack([np.zeros(nconf), ub if ub is not None else np.full(nconf, np.inf)])
            sol = linprog(c, A_eq=A, b_eq=b, bounds=bounds, method="highs")
            assert sol.status == 0, (name, sol.message)
            res[name] = sol.fun
        line = f"  k={k}: rows={r}  min fake avoider mass: " + "  ".join(f"{a}={v:.3f}" for a, v in res.items())
        print(line, flush=True)
        out.append((k, res))
    return out


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    x = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 6
    frac = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3
    run(seed, x, frac=frac)
