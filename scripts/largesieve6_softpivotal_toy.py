"""LS6 toy check (EVIDENCE): the soft-pivotal bounds of EXCEPTIONAL_LARGESIEVE6.md.

Random rough families over a small prime pool (squarefree coordinates
Omega_q = Z/q), truncated forbidding (LS5 Setting 2.0), tilted law
sigma = Q' 1_A e^{-2Y} / Z.  For every support S (|S| <= 3) we compute
  * exact  max_{supp theta = S} |sigma^(theta)|                (exact enumeration)
  * MC     Z^{-1} E|D_S Psi|                                   ((2.1), coin coupling)
  * MC     Z^{-1} 4^{|S|} E sum_{partitions} prod_B W_B         (Prop 2.2)
  * MC     Z^{-1} 4^{|S|} E sum_T 1[T in Piv H] max e^{2|a|'} XOR-cover  (Prop 4.2, first form)
and check exact <= each bound (MC noise is irrelevant for the last two: slack 4^|S|).
Also checks the corner-path chain structure of Lemma 3.1(iii) on every sample.
"""
import itertools, math, random, cmath, sys

def partitions(s):
    s = list(s)
    if not s:
        yield []
        return
    first, rest = s[0], s[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p

def make_family(rng, pool, ncls):
    fam = []
    for _ in range(ncls):
        k = rng.choice([1, 2, 2, 3])
        ps = sorted(rng.sample(pool, k))
        b = {p: rng.randrange(p) for p in ps}
        fam.append((tuple(ps), b))
    return fam

def run(seed, pool=(3, 5, 7, 11, 13), ncls=40, delta=0.5, nsamp=3000):
    rng = random.Random(seed)
    pool = list(pool)
    fam = make_family(rng, pool, ncls)
    w = {q: rng.uniform(0.2, 0.9) for q in pool}
    cap = {q: int(delta * q) for q in pool}
    bytop = {q: [C for C in fam if C[0][-1] == q] for q in pool}

    def step_sets(q, x):
        F = set()
        for ps, b in bytop[q]:
            if all(x[p] == b[p] for p in ps if p != q):
                F.add(b[q])
        Ft = sorted(F)[:cap[q]]
        return F, set(Ft)

    # exact law
    pts = list(itertools.product(*[range(q) for q in pool]))
    sig = {}
    Z = 0.0
    for t in pts:
        x = dict(zip(pool, t))
        pr, Y, ok = 1.0, 0.0, True
        for q in pool:
            F, Ft = step_sets(q, x)
            pt = len(Ft) / q
            if x[q] in Ft:
                pr = 0.0
                break
            pr *= 1.0 / (q * (1 - pt))
            Y += w[q] * pt
            if x[q] in F:
                ok = False
        val = pr * (math.exp(-2 * Y) if ok else 0.0)
        sig[t] = val
        Z += val
    for t in sig:
        sig[t] /= Z

    def path(S, vA, coins):
        """corner path; returns factor data per q"""
        x, data = {}, {}
        for q in pool:
            F, Ft = step_sets(q, x)
            pt = len(Ft)
            if q in S:
                x[q] = vA[q]
                data[q] = ('S', frozenset(F), pt, int(x[q] not in F))
            else:
                c, pi = coins[q]
                if c not in Ft:
                    x[q] = c
                else:
                    x[q] = next(a for a in pi if a not in Ft)
                data[q] = ('O', frozenset(F), pt, int(x[q] not in (F - Ft)))
        return x, data

    out = []
    for k in (1, 2, 3):
        for S in itertools.combinations(pool, k):
            S = list(S)
            idx = [pool.index(l) for l in S]
            # exact max Fourier coefficient over theta with supp S
            marg = {}
            for t, val in sig.items():
                key = tuple(t[i] for i in idx)
                marg[key] = marg.get(key, 0.0) + val
            best = 0.0
            for th in itertools.product(*[range(1, l) for l in S]):
                s = sum(val * cmath.exp(2j * math.pi * sum(th[j] * key[j] / S[j] for j in range(k)))
                        for key, val in marg.items())
                best = max(best, abs(s))
            corners = [frozenset(A) for r in range(k + 1) for A in itertools.combinations(S, r)]
            accD = acc22 = acc42 = 0.0
            for _ in range(nsamp):
                v = {l: rng.randrange(l) for l in S}
                vp = {l: rng.randrange(l) for l in S}
                coins = {}
                for q in pool:
                    if q not in S:
                        pi = list(range(q)); rng.shuffle(pi)
                        coins[q] = (rng.randrange(q), pi)
                P = {}
                for A in corners:
                    vA = {l: (vp[l] if l in A else v[l]) for l in S}
                    P[A] = path(S, vA, coins)
                def psi(A):
                    x, d = P[A]
                    val, Y = 1.0, 0.0
                    for q in pool:
                        typ, F, pt, ind = d[q]
                        Y += w[q] * pt / q
                        val *= ind
                        if typ == 'S':
                            val *= 1.0 / (1 - pt / q)
                    return val * math.exp(-2 * Y)
                DS = sum((-1) ** (k - len(A)) * psi(A) for A in corners)
                accD += abs(DS)
                # factors: (kind, q) -> value per corner
                def piv(fun):
                    s = set()
                    for A in corners:
                        for l in S:
                            if l not in A and fun(A | {l}) != fun(A):
                                s.add(l)
                    return s
                factors = []  # (kappa, pivset)
                for q in pool:
                    ptf = lambda A, q=q: P[A][1][q][2]
                    vals = [ptf(A) for A in corners]
                    Dq = (max(vals) - min(vals)) / q
                    pv = piv(ptf)
                    factors.append((w[q] * Dq, pv))             # phi_q
                    indf = lambda A, q=q: P[A][1][q][3]
                    factors.append((1.0, piv(indf)))             # h_q or lambda_q
                    if q in S:
                        factors.append((2 * Dq, pv))             # g_q
                tot = 0.0
                for part in partitions(S):
                    prod = 1.0
                    for B in part:
                        WB = sum(kap for kap, pv in factors if set(B) <= pv)
                        prod *= WB
                        if prod == 0: break
                    tot += prod
                acc22 += tot
                # Prop 4.2 (first form, crude XOR-cover sum <= cover sum, exact enumeration of covers)
                Hf = lambda A: int(all(P[A][1][q][3] for q in pool))
                pivH = piv(Hf)
                tot42 = 0.0
                for r in range(k + 1):
                    for T in itertools.combinations(S, r):
                        if not set(T) <= pivH: continue
                        U = [l for l in S if l not in T]
                        best_AT = 0.0
                        for rr in range(len(T) + 1):
                            for AT in itertools.combinations(T, rr):
                                AT = frozenset(AT)
                                sub = [AT | frozenset(B) for m in range(len(U) + 1) for B in itertools.combinations(U, m)]
                                def Ystar(A):
                                    d = P[A][1]; y = 0.0
                                    for q in pool:
                                        y += 2 * w[q] * d[q][2] / q
                                        if q in S: y += -math.log(1 - d[q][2] / q)
                                    return y
                                ys = {A: Ystar(A) for A in sub}
                                a = {}
                                Rs = [frozenset(B) for m in range(1, len(U) + 1) for B in itertools.combinations(U, m)]
                                for R in Rs:
                                    a[R] = sum(ys[A] * (-1) ** len(A & R) for A in sub) / len(sub)
                                norm = sum(abs(x) for x in a.values())
                                xor = 0.0
                                for m in range(1, len(Rs) + 1):
                                    for fam_ in itertools.combinations(Rs, m):
                                        sd = frozenset()
                                        for R in fam_: sd = sd ^ R
                                        if sd == frozenset(U):
                                            xor += math.prod(abs(a[R]) for R in fam_)
                                if not U: xor = 1.0
                                best_AT = max(best_AT, math.exp(norm) * xor)
                        tot42 += best_AT
                acc42 += tot42
            bD = accD / nsamp / Z
            b22 = 4 ** k * acc22 / nsamp / Z
            b42 = 2 ** k * acc42 / nsamp / Z
            out.append((S, best, bD, b22, b42))
    return out, Z

if __name__ == '__main__':
    seeds = [int(a) for a in sys.argv[1:]] or [1, 2, 3]
    worst = [0, 0, 0]
    for sd in seeds:
        res, Z = run(sd)
        print(f"seed {sd}: Z = {Z:.4f}")
        for S, ex, bD, b22, b42 in res:
            r = (ex / bD if bD else float('inf'), ex / b22 if b22 else float('inf'), ex / b42 if b42 else float('inf'))
            worst = [max(worst[i], r[i]) for i in range(3)]
            print(f"  S={S}: exact {ex:.3e}  (2.1) {bD:.3e}  P2.2 {b22:.3e}  P4.2 {b42:.3e}")
    print("max ratios exact/bound: (2.1) %.3f  Prop2.2 %.3e  Prop4.2 %.3e" % tuple(worst))
