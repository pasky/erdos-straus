"""R269 from-scratch spot-checks of BALANCED_LATTICE §6 (EVIDENCE).
mode nu  y QLO QHI NS SEED : random primes q = 3 (8) in [QLO,QHI]; exact D_min over all psi != 1 of U_q (integer arithmetic),
         nu = D_min N^{1/k}, order of a minimiser (ties: all minimisers reported via 'any minimiser has order N'), P+(N) | ord;
         same for a uniform random vector a mod N (random-lattice model). Quantiles of nu; order stats conditioned on D_min > 0.
mode eq  y X OUT            : all primes q = 3 (8), q <= X, q not | P. Writes per-q flags (class mod 8P, nu, flags) to OUT.
mode an  OUT NPERM          : chi^2 over reduced classes a = 3 (8) mod 8P of (i) existential Bad1 (some psi with
         D < t N^{-1/k} and ord > N^{1/k}/t), (ii) full set (some psi != 1 with D < t N^{-1/k}); permutation p-values;
         per-class max nu.
"""
import sys, math, random
import numpy as np
from sympy import isprime, primerange, primitive_root, factorint

TS = (0.3, 0.5, 0.7)


def logs(q, S):
    N = (q - 1) // 2
    g = pow(primitive_root(q), 2, q)
    tab = np.empty(q, dtype=np.int64); x = 1
    for i in range(N):
        tab[x] = i; x = x * g % q
    return N, np.array([tab[s * s % q] for s in S], dtype=np.int64)


def scan(N, a):
    j = np.arange(1, N, dtype=np.int64)
    tot = np.zeros(N - 1, dtype=np.int64)
    for s in a:
        r = (j * s) % N; tot += np.minimum(r, N - r)
    order = N // np.gcd(j, N)
    return tot, order


def mode_nu(y, qlo, qhi, ns, seed):
    S = list(primerange(3, y + 1)); k = len(S); rnd = random.Random(seed); nrng = np.random.default_rng(seed)
    out = {'true': [], 'rand': []}
    while len(out['true']) < ns:
        q = rnd.randrange(qlo, qhi)
        if q % 8 != 3 or not isprime(q) or q <= y: continue
        N, a = logs(q, S)
        Pp = max(factorint(N))
        for lab, vec in (('true', a), ('rand', nrng.integers(0, N, size=k))):
            tot, order = scan(N, vec)
            m = int(tot.min()); mins = order[tot == m]
            o = int(mins.max())  # order of a minimiser (largest among ties)
            out[lab].append((m / N * N ** (1 / k), m == 0, o, N, Pp, bool(o % Pp == 0), bool((mins == N).any()), int(mins.min())))
    print(f"y={y} k={k} q in [{qlo},{qhi}] n={ns}")
    for lab in ('true', 'rand'):
        R = out[lab]
        nu = np.array([r[0] for r in R]); deg = np.array([r[1] for r in R])
        nd = [r for r in R if not r[1]]
        o = np.array([r[2] for r in nd], dtype=float); N = np.array([r[3] for r in nd], dtype=float)
        o_min = np.array([r[7] for r in nd], dtype=float)
        print(f" {lab}: nu quantiles 1/10/50/90% = " + "/".join(f"{np.quantile(nu, p):.3f}" for p in (.01, .1, .5, .9)) +
              f"; degenerate {deg.sum()}/{len(R)}")
        print(f"   cond. D>0 (n={len(nd)}): ord=N {np.mean([r[6] for r in nd]):.3f} (some minimiser), "
              f"ord>=N^0.9 {np.mean(o >= N ** 0.9):.3f}, ord<=N^0.5 {np.mean(o_min <= N ** 0.5):.4f} (smallest-order minimiser), "
              f"ord<=N^(3/(2k+4)) {np.mean(o_min <= N ** (3 / (2 * k + 4))):.4f}, P+(N)|ord {np.mean([r[5] for r in nd]):.4f}")


def mode_eq(y, X, outp, qlo=0):
    S = list(primerange(3, y + 1)); k = len(S); P = math.prod(S); M = 8 * P
    with open(outp, 'w') as f:
        f.write(f"# y={y} k={k} 8P={M}\n")
        for q in primerange(max(y + 1, qlo), X + 1):
            if q % 8 != 3: continue
            N, a = logs(q, S)
            tot, order = scan(N, a)
            nu = tot.min() / N * N ** (1 / k)
            fl = []
            for t in TS:
                small = tot < t * N ** ((k - 1) / k)        # D < t N^{-1/k}
                fl.append(int(small.any()))
                fl.append(int((small & (order > N ** (1 / k) / t)).any()))
            f.write(f"{q} {q % M} {nu:.5f} " + " ".join(map(str, fl)) + "\n")


def mode_cls(y, qlo, X, c, outp):
    S = list(primerange(3, y + 1)); k = len(S); P = math.prod(S); M = 8 * P
    with open(outp, 'w') as f:
        f.write(f"# y={y} k={k} 8P={M} class={c}\n")
        q0 = qlo - (qlo % M) + c
        for q in range(q0, X + 1, M):
            if not isprime(q): continue
            N, a = logs(q, S)
            tot, order = scan(N, a)
            nu = tot.min() / N * N ** (1 / k)
            fl = []
            for t in TS:
                small = tot < t * N ** ((k - 1) / k)
                fl.append(int(small.any())); fl.append(int((small & (order > N ** (1 / k) / t)).any()))
            f.write(f"{q} {q % M} {nu:.5f} " + " ".join(map(str, fl)) + "\n"); f.flush()


def mode_an(inp, nperm, qmin=0, qmax=10**18):
    rows = [l.split() for l in open(inp) if not l.startswith('#')]
    rows = [r for r in rows if qmin <= int(r[0]) <= qmax]
    hdr = open(inp).readline()
    M = int(hdr.split('8P=')[1])
    cls = np.array([int(r[1]) for r in rows]); nu = np.array([float(r[2]) for r in rows])
    F = np.array([[int(x) for x in r[3:]] for r in rows])
    classes = sorted(set(cls)); idx = {c: i for i, c in enumerate(classes)}; li = np.array([idx[c] for c in cls])
    sizes = np.bincount(li); rng = np.random.default_rng(0)
    print(hdr.strip(), f"#q={len(rows)} #classes={len(classes)} (expected reduced classes = 3 mod 8: {len(classes)})")
    def chi(flag):
        exp = sizes * flag.sum() / len(flag)
        return float((((np.bincount(li[flag], minlength=len(classes)) - exp) ** 2) / exp).sum())
    for ti, t in enumerate(TS):
        for name, col in (('full', 2 * ti), ('Bad1', 2 * ti + 1)):
            flag = F[:, col].astype(bool)
            c0 = chi(flag); null = [chi(rng.permutation(flag)) for _ in range(nperm)]
            pv = (1 + sum(c >= c0 for c in null)) / (nperm + 1)
            print(f" t={t} {name}: #={flag.sum()}  chi2={c0:.1f} (df {len(classes) - 1})  perm p={pv:.3f}  max/class={np.bincount(li[flag], minlength=len(classes)).max()}")
    best = np.array([nu[li == i].max() for i in range(len(classes))])
    worst = np.array([nu[li == i].min() for i in range(len(classes))])
    print(f" per-class best nu: min {best.min():.3f} median {np.median(best):.3f}; classes with worst nu = 0: {(worst == 0).sum()}")


if __name__ == '__main__':
    m = sys.argv[1]
    if m == 'nu': mode_nu(*map(int, sys.argv[2:7]))
    elif m == 'cls': mode_cls(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6])
    elif m == 'eq': mode_eq(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], *map(int, sys.argv[5:]))
    else: mode_an(sys.argv[2], *map(int, sys.argv[3:]))
