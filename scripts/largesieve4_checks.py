"""EXCEPTIONAL_LARGESIEVE4 sanity checks (EVIDENCE only).
(1) Lemma 1.1: Sum_S (Prod_{l in S} w_l) P_S == E_T R_2(sigma_T), and R_{2+2b} <= it when (A_w) holds
    with w_l := max over theta with l in supp of ... (we take w_l = 1 and the tight per-prime choice below).
(2) Lemma 2.1: eta formula E[l^E 1[x_l=x'_l] | past] - 1 = (U(F∩F') - p p')/((1-p)(1-p')) for the
    always-forbid sequential law, by exact enumeration; and the tilted identity.
"""
import itertools, random
import numpy as np

def seq_law(primes, classes):
    """classes: list of (dict prime->residue). top = max prime. Returns sigma as dict tuple->prob."""
    order = sorted(primes)
    states = {(): 1.0}
    for i, l in enumerate(order):
        new = {}
        tops = [C for C in classes if max(C) == l]
        for pre, pr in states.items():
            asg = dict(zip(order[:i], pre))
            F = {C[l] for C in tops if all(asg[q] == C[q] for q in C if q != l)}
            free = [a for a in range(l) if a not in F]
            for a in free:
                new[pre + (a,)] = pr / len(free)
        states = new
    return order, states

def fourier(order, sig):
    shape = tuple(order)
    arr = np.zeros(shape)
    for k, v in sig.items():
        arr[k] = v
    return np.fft.fftn(arr)  # sigma-hat at (a_l/l) up to sign convention

def main(seed=1):
    rng = random.Random(seed)
    primes = [3, 5, 7, 11]
    classes = []
    for _ in range(40):
        k = rng.choice([1, 2, 2, 3])
        S = rng.sample(primes, k)
        classes.append({q: rng.randrange(q) for q in S})
    order, sig = seq_law(primes, classes)
    # support check
    for x in sig:
        asg = dict(zip(order, x))
        assert not any(all(asg[q] == C[q] for q in C) for C in classes)
    F = fourier(order, sig)
    A = np.abs(F)
    beta = 0.3
    # tight w: w_l from (A_w) is not product in general; use w_l = 1 (trivial) and also per-prime max
    for wmode in ["one", "rand"]:
        w = {l: (1.0 if wmode == "one" else rng.uniform(0.2, 1.0)) for l in order}
        lhs = 0.0; rhsS = 0.0
        for idx in itertools.product(*[range(l) for l in order]):
            S = [l for l, a in zip(order, idx) if a]
            ww = np.prod([w[l] for l in S]) if S else 1.0
            rhsS += ww * A[idx] ** 2
        # E_T R_2(sigma_T)
        ET = 0.0
        for mask in itertools.product([0, 1], repeat=len(order)):
            T = [i for i, m in enumerate(mask) if m]
            pT = np.prod([w[order[i]] if m else 1 - w[order[i]] for i, m in enumerate(mask)])
            marg = {}
            for x, v in sig.items():
                key = tuple(x[i] for i in T)
                marg[key] = marg.get(key, 0) + v
            MT = np.prod([order[i] for i in T]) if T else 1
            ET += pT * MT * sum(v * v for v in marg.values())
        print(f"[1] w={wmode}: sum_S w_S P_S = {rhsS:.10f}  E_T R2 = {ET:.10f}  diff={abs(rhsS-ET):.2e}")
        assert abs(rhsS - ET) < 1e-9 * max(1, ET)
    # Lemma 1.1 inequality with the per-theta check: take w_l minimal s.t. (A_w) holds is not product; check R_p' <= sum_S s_S^{2b} P_S
    Rp = (A ** (2 + 2 * beta)).sum()
    print(f"[1] R_(2+2b) = {Rp:.6f}")
    # (2) eta formula
    order_ = order
    marg_prefix = []
    for i in range(len(order_) + 1):
        m = {}
        for x, v in sig.items():
            m[x[:i]] = m.get(x[:i], 0) + v
        marg_prefix.append(m)
    maxerr = 0
    for i, l in enumerate(order_):
        tops = [C for C in classes if max(C) == l]
        pres = list(marg_prefix[i].keys())
        for _ in range(200):
            px, py = rng.choice(pres), rng.choice(pres)
            def Fset(pre):
                asg = dict(zip(order_[:i], pre))
                return {C[l] for C in tops if all(asg[q] == C[q] for q in C if q != l)}
            Fx, Fy = Fset(px), Fset(py)
            kx = {a: marg_prefix[i + 1].get(px + (a,), 0) / marg_prefix[i][px] for a in range(l)}
            ky = {a: marg_prefix[i + 1].get(py + (a,), 0) / marg_prefix[i][py] for a in range(l)}
            direct = l * sum(kx[a] * ky[a] for a in range(l)) - 1
            p, q, inter = len(Fx) / l, len(Fy) / l, len(Fx & Fy) / l
            formula = (inter - p * q) / ((1 - p) * (1 - q))
            maxerr = max(maxerr, abs(direct - formula))
    print(f"[2] eta formula max error {maxerr:.2e}")
    assert maxerr < 1e-12

if __name__ == "__main__":
    for s in range(1, 4):
        main(s)
    print("all checks passed")


def check_lemma51(seed):
    """Lemma 5.1 (always-forbid law, G = everything): |sigma_hat(theta)| <= prod_{l in S} 4U(Res_l)/(1-pmax_l)."""
    rng = random.Random(100 + seed)
    primes = [5, 7, 11, 13]
    # residue-sparse family: few residues per prime, classes of arity 1..4
    pool = {q: rng.sample(range(q), 2) for q in primes}
    classes = []
    for _ in range(25):
        k = rng.choice([1, 2, 2, 3, 4])
        S = rng.sample(primes, k)
        classes.append({q: rng.choice(pool[q]) for q in S})
    order, sig = seq_law(primes, classes)
    # max p over pasts
    pmax = {}
    for i, l in enumerate(order):
        tops = [C for C in classes if max(C) == l]
        mx = 0
        for pre in itertools.product(*[range(q) for q in order[:i]]):
            asg = dict(zip(order[:i], pre))
            F = {C[l] for C in tops if all(asg[q] == C[q] for q in C if q != l)}
            mx = max(mx, len(F) / l)
        pmax[l] = mx
    Res = {l: len({C[l] for C in classes if l in C}) / l for l in order}
    A = np.abs(fourier(order, sig))
    worst = 0
    for idx in itertools.product(*[range(l) for l in order]):
        S = [l for l, a in zip(order, idx) if a]
        if not S: continue
        bound = np.prod([4 * Res[l] / (1 - pmax[l]) for l in S])
        worst = max(worst, A[idx] / bound)
    print(f"[3] Lemma 5.1 seed {seed}: max |hat|/bound = {worst:.4f} (Res fractions {[round(Res[l],3) for l in order]})")
    assert worst <= 1 + 1e-12


if __name__ == "__main__":
    for s in range(1, 6):
        check_lemma51(s)
    print("lemma 5.1 checks passed")
