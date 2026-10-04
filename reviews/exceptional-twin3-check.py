"""Independent checks for the review of EXCEPTIONAL_TWIN3.md (commit 2bbe184).

Part A (Lemma 3.2): for v,t,u <= Y prime to j compute
  r(c)  = sum_{v^2 t = c (j)} 1/(vt),  r1(rho) = sum_{(u,v)=1, u = rho v (j)} 1/(uv),
their diagonal/off-diagonal second moments, and the *sup tails* that the proof
bounds by box counting:
  T(c)  = sum_{v^2 t = c, v^2 t > j} 1/(vt),
  T1(r) = sum_{u = r v, (u,v)=1, max(u,v) >= sqrt(j/2)} 1/(uv),
against the explicit box bounds of the proof.
Part B (inequality (2.1) and TW2-D5): random (x,y,z) test.
Usage: PYTHONPATH=scripts uv run --with numpy python reviews/exceptional-twin3-check.py A Y j1 j2 ...
       ... B
"""
import sys, math
import numpy as np


def box_bound_r(j, Y):
    L2 = math.log2(Y)
    s = 2 * (2 + L2) ** 2 / j
    i = 0
    while 2 ** i <= Y:
        if 2 ** i > (j / 8) ** (1 / 3):
            s += (4 * i + 4) / 2 ** i
        i += 1
    return s


def box_bound_r1(j, Y):
    L2 = math.log2(Y)
    s = (2 + L2) ** 2 / j
    i = 0
    while 2 ** i <= Y:
        if 2 ** i >= (j / 8) ** 0.5:
            s += (2 * i + 2) / 2 ** i
        i += 1
    return s


def partA(Y, j):
    v = np.arange(1, Y + 1, dtype=np.int64)
    v = v[v % j != 0]
    w = 1.0 / v
    inv = np.zeros(j, dtype=np.int64)
    for x in range(1, j):
        inv[x] = pow(x, -1, j)
    r = np.zeros(j); T = np.zeros(j); diag = {}
    r1 = np.zeros(j); T1 = np.zeros(j); d1 = 0.0
    h = math.sqrt(j / 2)
    for vv, wv in zip(v, w):
        N = vv * vv * v  # t = v array
        c = N % j
        r += np.bincount(c, weights=wv * w, minlength=j)
        big = N > j
        T += np.bincount(c[big], weights=wv * w[big], minlength=j)
        for NN, ww in zip(N.tolist(), (wv * w).tolist()):
            diag[NN] = diag.get(NN, 0.0) + ww
        # r1 with u = vv, v = array
        cop = np.gcd(vv, v) == 1
        vin = v[cop]; win = w[cop]
        rho = (vv % j) * inv[vin % j] % j
        r1 += np.bincount(rho, weights=wv * win, minlength=j)
        d1 += float(np.sum((wv * win) ** 2))
        hi = np.maximum(vv, vin) >= h
        T1 += np.bincount(rho[hi], weights=wv * win[hi], minlength=j)
    dg = sum(x * x for x in diag.values())
    S, S1 = r.sum(), r1.sum()
    tot, tot1 = (r * r).sum(), (r1 * r1).sum()
    z2, z3 = math.pi ** 2 / 6, 1.2020569031595942
    br, br1 = box_bound_r(j, Y), box_bound_r1(j, Y)
    print(f"j={j} Y={Y}")
    print(f"  r : sum={S:.2f} tot2={tot:.4f} diag={dg:.4f} (<= {z2*z2*z3*z3:.4f}) off={tot-dg:.4f}"
          f" <= 2*sum*supT={2*S*T.max():.3f};  supT={T.max():.4f} vs box bound {br:.4f}  [{'OK' if T.max()<=br else 'VIOLATION'}]")
    print(f"  r1: sum={S1:.2f} tot2={tot1:.4f} diag={d1:.4f} (<= {z2*z2:.4f}) off={tot1-d1:.4f}"
          f" <= 2*sum*supT1={2*S1*T1.max():.3f};  supT1={T1.max():.4f} vs box bound {br1:.4f}  [{'OK' if T1.max()<=br1 else 'VIOLATION'}]")
    ok = (dg <= z2 * z2 * z3 * z3 and d1 <= z2 * z2 and tot - dg <= 2 * S * T.max() + 1e-9
          and tot1 - d1 <= 2 * S1 * T1.max() + 1e-9 and T.max() <= br and T1.max() <= br1)
    print("  all Lemma 3.2 inequalities:", "OK" if ok else "VIOLATION")


def partB(n=10 ** 6, seed=1):
    rng = np.random.default_rng(seed)
    x = rng.exponential(1.0, n) * rng.choice([0, 0.01, 0.5, 1, 3], n)
    z = rng.exponential(1.0, n) * rng.choice([0, 0.01, 0.5, 1, 3], n)
    lhs = np.minimum(x + z, 1) ** 2
    rhs = 2 * x + 2 * z ** 2
    rhs_d5 = np.minimum(x, 1) ** 2 + 3 * z
    print("(2.1) pointwise: max lhs-rhs =", float((lhs - rhs).max()),
          "| D5: max lhs-rhs =", float((lhs - rhs_d5).max()))
    print("(2.1) tightness: min rhs/lhs over lhs>0 =", float((rhs[lhs > 0] / lhs[lhs > 0]).min()))


# ---------------- Part C: Lemma 3.1 structure on the real system (toy) ----------------
def partC(j=11, k=1, C0=5, Mmax=3_000_000, nsample=1500, seed=2):
    import random
    from math import gcd, log
    kj = k * j
    lo = kj ** C0
    Amax = (kj * Mmax + 1) // 4
    spf = np.zeros(Amax + 1, dtype=np.int32)
    for p in range(2, int(Amax ** 0.5) + 1):
        if spf[p] == 0:
            blk = spf[p * p::p]
            blk[blk == 0] = p
    isp = np.ones(Mmax + 1, dtype=bool); isp[:2] = False
    for p in range(2, int(Mmax ** 0.5) + 1):
        if isp[p]:
            isp[p * p::p] = False
    P = np.nonzero(isp)[0]
    P = P[(P > lo) & ((kj * P) % 4 == 3) & (P != j)]
    print(f"Part C: j={j} k={k} C0={C0} m in ({lo},{Mmax}]: {len(P)} primes")

    def fac(n):
        f = {}
        while n > 1:
            p = int(spf[n]) or n
            f[p] = f.get(p, 0) + 1
            n //= p
        return f

    def phi(n):
        r = n
        for p in fac(n) if n <= Amax else []:
            r -= r // p
        return r

    keys = {}  # (case, short pair) -> list of m
    bad_res = 0; ntrip = 0
    for m in P.tolist():
        A = (kj * m + 1) // 4
        f = list(fac(A).items())
        # enumerate (u,v) coprime with uv | A
        pairs = [(1, 1)]
        for p, e in f:
            new = []
            for (u, v) in pairs:
                new.append((u, v))
                pe = 1
                for _ in range(e):
                    pe *= p
                    new.append((u * pe, v)); new.append((u, v * pe))
            pairs = new
        for (u, v) in pairs:
            t = A // (u * v); ntrip += 1
            D = u * u * t
            a = (-4 * D) % j
            if a != (-u * pow(v, -1, j)) % j or a != (-pow(4 * v * v * t, -1, j)) % j:
                bad_res += 1
            if t >= u and t >= v:
                key = ('t', u, v)
            elif u >= v:
                key = ('u', v, t)
            else:
                key = ('v', u, t)
            keys.setdefault(key, []).append(m)
    print(f"  triples={ntrip}, residue-identity (3.1) failures={bad_res}, keys={len(keys)}")
    # every (key, m) satisfies the predicted class/size conditions; injectivity
    bad_cond = 0; bad_inj = 0; bad_M1 = 0; bad_bt = 0; worst = 0.0
    for key, ms in keys.items():
        c, x, y = key
        q = 4 * x * y
        mx = max(x, y)
        M1 = max(lo, (q * mx - 1) / kj)
        if M1 < q * kj / 8 - 1e-9:
            bad_M1 += 1
        if len(set(ms)) != len(ms):
            bad_inj += 1
        for m in ms:
            if (kj * m + 1) % q != 0 or (kj * m + 1) // 4 < x * y * mx:
                bad_cond += 1
        # MV-shaped bound on dyadic blocks starting at y0 = M1 (requires y0 > q)
        if M1 > q:
            s = 0.0; yb = M1
            while yb < Mmax:
                s += 1.0 / log(yb / q); yb *= 2
            bound = 2.0 / phi(q) * s
            act = sum(1.0 / m for m in ms)
            worst = max(worst, act / bound)
            if act > bound:
                bad_bt += 1
    print(f"  cond failures={bad_cond}, injectivity failures={bad_inj}, M1<q*kj/8: {bad_M1}, "
          f"BT-shaped bound failures={bad_bt}, worst actual/bound={worst:.3f}")
    # equality (t-case) / containment (u,v-cases) on a random sample of keys:
    rng = random.Random(seed)
    sample = rng.sample(list(keys), min(nsample, len(keys)))
    neq = 0; nsub = 0
    for key in sample:
        c, x, y = key
        q = 4 * x * y; mx = max(x, y)
        if gcd(q, kj) != 1:
            neq += 1; continue
        s = (-pow(kj, -1, q)) % q
        pred = P[(P % q == s) & ((kj * P + 1) // 4 >= x * y * mx)]
        act = set(keys[key])
        if not act <= set(pred.tolist()):
            nsub += 1
        if c == 't':
            # t-case: predicted m must give exactly this triple (u,v,t) with (u,v)=1
            if len(act) != len(pred):
                neq += 1
    print(f"  sample {len(sample)} keys: containment failures={nsub}, t-case equality failures={neq}")


if __name__ == "__main__":
    if sys.argv[1] == "C":
        partC()
    elif sys.argv[1] == "A":
        Y = int(float(sys.argv[2]))
        for j in sys.argv[3:]:
            partA(Y, int(j))
    else:
        partB()
