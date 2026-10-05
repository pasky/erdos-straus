"""R44a from-scratch check of POINTWISE_OMEGA11 §2 (graded quarantine).

Independent of the author's scripts. For a given T and c:
  * enumerate atoms (M,D), M<=T, M=3 mod 4, D | A^2, A=(M+1)/4;
  * run Lemma 2.2 (atomic masses; batch raising, which is covered by the cost
    proof because the majorant of w_l is Q-uniform);
  * check: P(E)<=s'(M,D)=(g/M)prod l/(l-1) for every surviving atom at every stage,
    every raise satisfies w_l(Q_i)<=sum_{v_l(M)>=a+1} s', final LLL quantity <= c,
    log Q <= 9 + (L/c) sum s' h(M), h(M)<=log2 tau(M);
  * property (I) by sampling n=1 (Q): every n with W(n)<=T has an occurring surviving
    event; every n with no occurring surviving event has W(n)>T.
Usage: review_o11a_graded.py T c [nsamples]
"""
import math, random, sys
from collections import defaultdict


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds


def atoms(T):
    out = []
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        fA = factor(A)
        fA2 = {p: 2 * e for p, e in fA.items()}
        fM = factor(M)
        for D in divisors_from(fA2):
            out.append((M, D, fM))
    return out


def fibre_prob(l, v, a, r):
    """P(X = r mod l^v) for X uniform on {x mod l^f: x=1 mod l^a} (units if a=0), v>a."""
    if a == 0:
        return 0.0 if r % l == 0 else 1.0 / (l ** (v - 1) * (l - 1))
    assert (r - 1) % (l ** a) == 0, "inconsistent with fibre"
    return float(l) ** (-(v - a))


def run(T, c, nsamp):
    L = math.log(T)
    At = atoms(T)
    f = {}
    for (M, D, fM) in At:
        for l in fM:
            f[l] = int(math.floor(L / math.log(l) + 1e-12))
            while l ** (f[l] + 1) <= T:
                f[l] += 1
            while l ** f[l] > T:
                f[l] -= 1
    a = defaultdict(int)
    for l in (3, 5, 7):
        a[l] = 1
    # Q-uniform majorant s' and h
    sp, hM = [], []
    for (M, D, fM) in At:
        g = math.gcd(M, 4 * D + 1)
        s = g / M
        for l in fM:
            s *= l / (l - 1)
        sp.append(s)
        hM.append(sum(sum(1.0 / i for i in range(1, v + 1)) for v in fM.values()))
    # majorant tail: maj[(l,a)] = sum_{v_l(M)>=a+1} s'
    maj = defaultdict(float)
    for (M, D, fM), s in zip(At, sp):
        for l, v in fM.items():
            for aa in range(v):
                maj[(l, aa)] += s

    def state():
        w = defaultdict(float)
        ev = []
        for idx, (M, D, fM) in enumerate(At):
            ok = True
            supp = []
            for l, v in fM.items():
                m = l ** min(v, a[l])
                if (4 * D + 1) % m:
                    ok = False
                    break
                if v > a[l]:
                    supp.append((l, v))
            if not ok or not supp:
                continue
            P = 1.0
            for l, v in supp:
                P *= fibre_prob(l, v, a[l], (-4 * D) % l ** v)
            assert P <= sp[idx] * (1 + 1e-12), (M, D, P, sp[idx])
            for l, v in supp:
                w[l] += P
            ev.append((idx, P, supp))
        return w, ev

    rounds = 0
    while True:
        w, ev = state()
        raise_ = [l for l in w if a[l] < f[l] and w[l] > c * (a[l] + 1) * math.log(l) / L]
        if not raise_:
            break
        for l in raise_:
            assert w[l] <= maj[(l, a[l])] * (1 + 1e-12)
            a[l] += 1
        rounds += 1
    lll = max((sum(w[l] for l, v in supp) for idx, P, supp in ev), default=0.0)
    logQ = math.log(8) + sum(a[l] * math.log(l) for l in a)
    bound = 9 + (L / c) * sum(s * h for s, h in zip(sp, hM))
    hmax = max(hM)
    l2tau = max(math.log2(math.prod(v + 1 for v in fM.values())) for (M, D, fM) in At)
    Stot = sum(P for idx, P, supp in ev)
    print(f"T={T} c={c} atoms={len(At)} rounds={rounds} events={len(ev)} Stot={Stot:.3f} "
          f"S'={sum(sp):.2f} maxLLL={lll:.4f} logQ={logQ:.1f} bound={bound:.1f} "
          f"hmax={hmax:.3f} max log2tau={l2tau:.3f} primesInQ={sum(1 for l in a if a[l])} "
          f"maxexp={max(a.values())}")
    assert lll <= c + 1e-12 and logQ <= bound and hmax <= l2tau + 1e-12
    # property (I) by sampling
    Q = 8 * math.prod(l ** a[l] for l in a)
    R = {}
    for (M, D, fM) in At:
        R.setdefault(M, set()).add((-4 * D) % M)
    byM = defaultdict(list)
    for idx, P, supp in ev:
        byM[At[idx][0]].append(idx)
    rng = random.Random(1)
    nfree = 0
    for _ in range(nsamp):
        n = 1 + Q * rng.randrange(1, 10 ** 30)
        hard = any(n % M in R[M] for M in R)  # W(n)<=T
        occ = any((n + 4 * At[idx][1]) % At[idx][0] == 0 for M in byM for idx in byM[M])
        assert hard == occ, n  # (I) and its converse
        nfree += not occ
    print(f"  (I) checked on {nsamp} samples n=1 (Q); {nfree} with W(n)>T")


if __name__ == "__main__":
    T = int(sys.argv[1]); c = float(sys.argv[2])
    ns = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
    run(T, c, ns)
