"""R62 from-scratch checks for EXCEPTIONAL_LARGESIEVE4 (review; EVIDENCE only).

Toy Setting 4.0: coordinates Z/l^E (prime powers allowed), classes = {l: (b, v)} meaning
x_l = b mod l^v for every l in the class; increasing-order sequential law with caps delta_l
(light: uniform off F_l; heavy: uniform), Q' its law (exact Fractions).
Checks
 [L1.1] identity sum_S w_S P_S = E_T R_2(sigma_T) and inequality R_{2+2b} <= E_T R_2(sigma_T)
        whenever (A_w) holds (w chosen minimal-uniform so that (A_w) holds, and random-direction).
 [P4.1] E_T R_2((sigma_B)_T) <= e^{2B}/Q'(G_B)^2 for sigma_B = Q'(.|G_B).
 [L5.1] |sigma_hat(theta)| <= Q'(G)^{-1} prod_{l in S} 4U(Res_l)/(1-delta_l) for G = G_B and G = avoider.
 [L2.1] E_{sig x sig} prod(1+w h) = E_Q prod(1+w eta) (tilted pair process, by recursion) and the
        inflation bound P_Q(x_l=a|past) <= U(a)/((1-p)(1-p')(1+w eta)).
"""
import itertools, math, random, sys
from fractions import Fraction as Fr
import numpy as np

def make_law(coords, classes, delta):
    """coords: list of (l, E) increasing in l. Returns dict path->Fraction (Q'), and per-path data."""
    paths = {(): (Fr(1), Fr(0), [])}   # path -> (prob, unused, list of (p_tilde))
    out = {(): Fr(1)}
    ptil = {(): []}
    for i, (l, E) in enumerate(coords):
        mod = l ** E
        tops = [C for C in classes if max(C) == l]
        new, newp = {}, {}
        for pre, pr in out.items():
            F = set()
            for C in tops:
                ok = all((pre[j] - C[q][0]) % (q ** C[q][1]) == 0
                         for j, (q, _) in enumerate(coords[:i]) if q in C)
                if ok:
                    b, v = C[l]
                    F |= {a for a in range(mod) if (a - b) % (l ** v) == 0}
            p = Fr(len(F), mod)
            light = p <= delta[l]
            free = [a for a in range(mod) if not (light and a in F)]
            for a in free:
                new[pre + (a,)] = pr / len(free)
                newp[pre + (a,)] = ptil[pre] + [(p if light else Fr(0), frozenset(F) if light else frozenset())]
        out, ptil = new, newp
    return out, ptil

def in_avoider(x, coords, classes):
    for C in classes:
        if all((x[j] - C[q][0]) % (q ** C[q][1]) == 0 for j, (q, _) in enumerate(coords) if q in C):
            return False
    return True

def fourier_abs(coords, sig):
    arr = np.zeros(tuple(l ** E for l, E in coords))
    for k, v in sig.items():
        arr[k] = float(v)
    return np.abs(np.fft.fftn(arr))

def ET_R2(coords, sig, w):
    n = len(coords); tot = 0.0
    for mask in itertools.product([0, 1], repeat=n):
        pT = 1.0
        for i, m in enumerate(mask):
            pT *= w[i] if m else 1 - w[i]
        if pT == 0: continue
        T = [i for i in range(n) if mask[i]]
        marg = {}
        for x, v in sig.items():
            k = tuple(x[i] for i in T); marg[k] = marg.get(k, 0.0) + float(v)
        MT = math.prod(coords[i][0] ** coords[i][1] for i in T)
        tot += pT * MT * sum(u * u for u in marg.values())
    return tot

def supp(idx):
    return [i for i, a in enumerate(idx) if a]

def sum_wS_PS(coords, A, w):
    tot = 0.0
    for idx in np.ndindex(A.shape):
        tot += math.prod(w[i] for i in supp(idx)) * A[idx] ** 2
    return tot

def Rp(A, beta):
    return float((A ** (2 + 2 * beta)).sum())

def check_L11(coords, sig, beta, rng, tag):
    A = fourier_abs(coords, sig); n = len(coords)
    worst = 0.0
    for trial in range(4):
        r = [1.0] * n if trial == 0 else [rng.uniform(0.3, 1.0) for _ in range(n)]
        # minimal t with (A_w): |s|^{2b} <= prod_{S} min(1, t r_l)
        lo, hi = 0.0, 1e6
        def ok(t):
            ww = [min(1.0, t * x) for x in r]
            for idx in np.ndindex(A.shape):
                S = supp(idx)
                if S and A[idx] ** (2 * beta) > math.prod(ww[i] for i in S) * (1 + 1e-12) + 1e-15:
                    return False
            return True
        for _ in range(60):
            mid = (lo + hi) / 2
            (hi := mid) if ok(mid) else (lo := mid)
        w = [min(1.0, hi * x) for x in r]
        lhs = Rp(A, beta); mid_ = sum_wS_PS(coords, A, w); rhs = ET_R2(coords, sig, w)
        assert abs(mid_ - rhs) < 1e-9 * rhs, (mid_, rhs)
        assert lhs <= rhs * (1 + 1e-9), (lhs, rhs)
        worst = max(worst, lhs / rhs)
    print(f"[L1.1 {tag}] identity ok, inequality ok, max R_p'/E_T R2 = {worst:.4f}")

def tilted_identity(coords, sig_pathlaw, w):
    """E_{sig x sig} prod(1+w h) vs E_Q prod(1+w eta) via recursion on prefix pairs. sig_pathlaw: step laws
    given by full-path probabilities (sequential law); compute step kernels from prefix marginals."""
    n = len(coords)
    pref = [dict() for _ in range(n + 1)]
    for x, v in sig_pathlaw.items():
        for i in range(n + 1):
            pref[i][x[:i]] = pref[i].get(x[:i], Fr(0)) + v
    def kern(pre):
        i = len(pre); mod = coords[i][0] ** coords[i][1]
        tot = pref[i][pre]
        return {a: pref[i + 1].get(pre + (a,), Fr(0)) / tot for a in range(mod)}
    # V(pre,pre') = E_Q[prod_{k>=i}(1+w eta_k) | prefixes]; direct = E[prod_{k>=i}(1+w h)| prefixes]
    memo = {}
    maxinfl = 0.0
    def rec(pre, prp):
        nonlocal maxinfl
        i = len(pre)
        if i == n: return (Fr(1), Fr(1))
        key = (pre, prp)
        if key in memo: return memo[key]
        l, E = coords[i]; mod = l ** E; wl = w[i]
        k, kp = kern(pre), kern(prp)
        eta = mod * sum(k[a] * kp[a] for a in range(mod)) - 1
        Z = 1 + wl * eta
        vq, vd = Fr(0), Fr(0)
        p = 1 - Fr(sum(1 for a in range(mod) if k[a] > 0), mod)
        pp = 1 - Fr(sum(1 for a in range(mod) if kp[a] > 0), mod)
        margx = {}
        for a in range(mod):
            if k[a] == 0: continue
            for b in range(mod):
                if kp[b] == 0: continue
                h = (mod if a == b else 0) - 1
                fac = 1 + wl * h
                sq, sd = rec(pre + (a,), prp + (b,))
                vd += k[a] * kp[b] * fac * sd
                if Z > 0:
                    q = k[a] * kp[b] * fac / Z
                    vq += q * sq
                    margx[a] = margx.get(a, 0) + q
        if Z > 0:
            for a, q in margx.items():
                bound = Fr(1, mod) / ((1 - p) * (1 - pp) * Z)
                assert q <= bound, (q, bound)
                maxinfl = max(maxinfl, float(q / bound))
        res = (Z * vq, vd)
        memo[key] = res
        return res
    vq, vd = rec((), ())
    return vq, vd, maxinfl

def main(seed):
    rng = random.Random(seed)
    coords = [(3, 2), (5, 1), (7, 1), (11, 1)] if seed % 2 else [(5, 1), (7, 1), (11, 1), (13, 1)]
    primes = [l for l, _ in coords]; Emap = dict(coords)
    delta = {l: Fr(rng.choice([1, 2, 3]), 2 * 3) if rng.random() < 0.5 else Fr(1, 2) for l in primes}
    delta = {l: min(d, Fr(1, 2)) for l, d in delta.items()}
    classes = []
    sparse = rng.random() < 0.5
    resid = {l: rng.randrange(l ** Emap[l]) for l in primes}
    for _ in range(rng.randrange(8, 30)):
        k = rng.choice([1, 2, 2, 3])
        S = rng.sample(primes, k)
        C = {}
        for q in S:
            v = rng.randint(1, Emap[q])
            b = resid[q] if sparse else rng.randrange(q ** Emap[q])
            C[q] = (b % (q ** v), v)
        classes.append(C)
    Qp, ptil = make_law(coords, classes, delta)
    beta = rng.choice([0.25, 0.5, 0.1])
    w = [rng.uniform(0.0, 1.0) for _ in coords]
    # avoider and G_B
    av = {x for x in Qp if in_avoider(x, coords, classes)}
    QG = sum(Qp[x] for x in av)
    if QG == 0:
        print("empty avoider; skip"); return
    damped = {x: sum(w[i] * float(ptil[x][i][0]) for i in range(len(coords))) for x in Qp}
    vals = sorted(damped[x] for x in av)
    B = vals[len(vals) // 2]
    GB = {x for x in av if damped[x] <= B + 1e-15}
    QGB = sum(Qp[x] for x in GB)
    sigB = {x: Qp[x] / QGB for x in GB}
    sigA = {x: Qp[x] / QG for x in av}
    tag = f"seed{seed}{' sparse' if sparse else ''}"
    # L1.1 on sigma_B and on sigma_avoider
    check_L11(coords, sigB, beta, rng, tag + " sigB")
    check_L11(coords, sigA, beta, rng, tag + " sigAv")
    # P4.1
    lhs = ET_R2(coords, sigB, w); rhs = math.exp(2 * B) / float(QGB) ** 2
    assert lhs <= rhs * (1 + 1e-12), (lhs, rhs)
    print(f"[P4.1 {tag}] E_T R2(sigB) = {lhs:.4f} <= e^2B/Q(G)^2 = {rhs:.4f}")
    # L5.1
    Res = []
    for i, (l, E) in enumerate(coords):
        R = set()
        for C in classes:
            if l in C:
                b, v = C[l]; R |= {a for a in range(l ** E) if (a - b) % (l ** v) == 0}
        Res.append(Fr(len(R), l ** E))
    for name, sig, QGv in [("G_B", sigB, QGB), ("avoider", sigA, QG)]:
        A = fourier_abs(coords, sig); worst = 0.0
        for idx in np.ndindex(A.shape):
            S = supp(idx)
            if not S: continue
            bd = math.prod(4 * float(Res[i]) / (1 - float(delta[coords[i][0]])) for i in S) / float(QGv)
            if A[idx] > bd * (1 + 1e-9) + 1e-12:
                raise AssertionError(f"L5.1 FAIL {tag} {name} idx={idx} |s|={A[idx]} bd={bd}")
            if bd < 1: worst = max(worst, A[idx] / bd)
        print(f"[L5.1 {tag} {name}] ok; max ratio over nontrivial bounds = {worst:.3f}")
    # L2.1 tilted identity on the *always-forbid* law (delta=1) restricted to 3 coords (cost)
    c3 = coords[:3]
    cl3 = [C for C in classes if all(q in dict(c3) for q in C)]
    law3, _ = make_law(c3, cl3, {l: Fr(1) for l, _ in c3})
    if sum(law3.values()) != 1:
        print(f"[L2.1 {tag}] some p_l = 1 (Lemma 2.1 excludes it); skip"); return
    vq, vd, mi = tilted_identity(c3, law3, [Fr(round(x * 100), 100) for x in w[:3]])
    assert vq == vd, (vq, vd)
    print(f"[L2.1 {tag}] tilted identity exact ({float(vq):.5f}); max inflation ratio {mi:.3f}")

if __name__ == "__main__":
    for s in range(int(sys.argv[1]) if len(sys.argv) > 1 else 6):
        main(s)
