# z52d pass2 NC1 (Z1394): compare run-length of consecutive primes ≡1 mod 24 with no C≤2 witness against
# (a) i.i.d. Bernoulli with the global failure rate, (b) independent Bernoulli with per-class (p mod 840) failure rates.
# input: /tmp/list_c2_1e9.txt  lines "p C" (C=0 means no witness with C≤2), produced by z52d_p2_NC1_cmin.c list mode.
import numpy as np, sys, json
ps, cs = [], []
with open(sys.argv[1]) as f:
    for line in f:
        a, b = line.split(); ps.append(int(a)); cs.append(int(b))
p = np.array(ps, dtype=np.int64); fail = (np.array(cs) == 0).astype(np.int8)
N = len(p); cls = p % 840
q_glob = fail.mean()
uniq, inv = np.unique(cls, return_inverse=True)
q_cls = np.bincount(inv, weights=fail) / np.bincount(inv)
qi = q_cls[inv]
def observed(f):
    # maximal runs of failures
    d = np.diff(np.concatenate(([0], f, [0])))
    starts = np.where(d == 1)[0]; ends = np.where(d == -1)[0]
    L = ends - starts
    return np.bincount(L, minlength=40)
obs = observed(fail)
def expected_iid(q, k):
    return N * q ** k * (1 - q) ** 2
def expected_class(k):
    # sum over starting positions i: prod_{j=i}^{i+k-1} q_j * (1-q_{i-1})(1-q_{i+k}) (approximate boundary treatment)
    lq = np.log(np.maximum(qi, 1e-12))
    cs_ = np.concatenate(([0.0], np.cumsum(lq)))
    tot = 0.0
    for i in range(1, N - k - 1):
        tot += 0.0
    # vectorised
    idx = np.arange(1, N - k - 1)
    logprod = cs_[idx + k] - cs_[idx]
    bnd = (1 - qi[idx - 1]) * (1 - qi[idx + k])
    return float(np.sum(np.exp(logprod) * bnd))
out = {"N_primes": int(N), "q_global_fail": float(q_glob), "n_classes": int(len(uniq))}
rows = []
for k in range(1, 9):
    rows.append({"k": k, "observed_exact_len": int(obs[k]) if k < len(obs) else 0,
                 "iid_global": round(expected_iid(q_glob, k), 1),
                 "iid_class_indep": round(expected_class(k), 1)})
out["table"] = rows
print(json.dumps(out, indent=1))
