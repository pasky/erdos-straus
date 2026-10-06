"""Review R67b: from-scratch toy check of LS5 Prop 2.1 (tilted fibre law).

Sequential law Q' on prod Z/l (squarefree coordinates) for a random rough family
of classes (b mod G), with TRUNCATED forbidding: at step l the forbidden set is
the first floor(delta*l) elements (in increasing residue order) of the activated
set F_l; x_l ~ U(Z/l minus Ftilde_l).  ptilde_l = |Ftilde_l|/l, Y = sum w_l ptilde_l.

Checks, exactly (Fractions) for the rational tilt Phi = 1_A / prod(1+2 w ptilde)
and in 60-digit mpmath for the exponential tilt Phi = 1_A exp(-2Y):
  (1) E_T R_2(sigma_T) = E_{sigma x sigma} prod(1 + w h)   (direct pair sum)
  (2) E_T R_2 <= Z^{-2}
  (3) Z >= Q'(A) exp(-2 E Y / Q'(A))          (exp tilt)
  (4) if Q'(A) >= 3/4:  log E_T R_2 <= 6 E Y + 1
  (5) eta_l <= ptilde/(1-ptilde) along every pair path (via 1+eta = l sum k k')
Also prints the leak P(x not in A) against E sum (p - ptilde) (LS5 Setting 2.0).
"""
import itertools, random, sys
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 60


def run(primes, ncls, seed, delta=Fr(1, 2), wmode="rand"):
    rnd = random.Random(seed)
    # random family: moduli = random nonempty subsets of primes; residues random
    fam = []
    for _ in range(ncls):
        k = rnd.randint(1, min(3, len(primes)))
        Gs = tuple(sorted(rnd.sample(primes, k)))
        fam.append((Gs, {p: rnd.randrange(p) for p in Gs}))
    w = {p: (Fr(rnd.randint(1, 10), 10) if wmode == "rand" else Fr(1)) for p in primes}
    # enumerate the law
    law = {}  # x -> (prob, ptilde dict, p dict, avoider flag)

    def rec(i, x, prob, pt, pp, avoid):
        if i == len(primes):
            law[tuple(x)] = (prob, dict(pt), dict(pp), avoid)
            return
        l = primes[i]
        F = set()
        for Gs, b in fam:
            if Gs[-1] == l and all(x[primes.index(q)] == b[q] for q in Gs[:-1]):
                F.add(b[l])
        Fs = sorted(F)
        cap = int(delta * l)
        Ft = set(Fs[:cap])
        pt[l] = Fr(len(Ft), l); pp[l] = Fr(len(F), l)
        allowed = [a for a in range(l) if a not in Ft]
        for a in allowed:
            rec(i + 1, x + [a], prob / len(allowed), pt, pp, avoid and a not in F)
    rec(0, [], Fr(1), {}, {}, True)
    pts = list(law)
    QA = sum(law[x][0] for x in pts if law[x][3])
    EY = sum(law[x][0] * sum(w[l] * law[x][1][l] for l in primes) for x in pts)
    leak = 1 - QA
    Eexcess = sum(law[x][0] * sum(law[x][2][l] - law[x][1][l] for l in primes) for x in pts)
    out = {}
    assert leak <= 2 * Eexcess  # (p-pt)/(1-pt) <= 2(p-pt)
    if QA == 0:
        return QA, EY, leak, Eexcess, None
    for mode in ("rat", "exp"):
        if mode == "rat":
            phi = {x: (Fr(1) / mp_prod([1 + 2 * w[l] * law[x][1][l] for l in primes])) if law[x][3] else Fr(0) for x in pts}
        else:
            phi = {x: mp.e ** (-2 * mpq(sum(w[l] * law[x][1][l] for l in primes))) if law[x][3] else mp.mpf(0) for x in pts}
        conv = (lambda v: v) if mode == "rat" else mpq
        Z = sum(conv(law[x][0]) * phi[x] for x in pts)
        sig = {x: conv(law[x][0]) * phi[x] / Z for x in pts if phi[x] != 0}
        S = list(sig)
        # (1) direct pair sum of prod(1+w h)
        direct = 0
        for x in S:
            for y in S:
                f = 1
                for i, l in enumerate(primes):
                    h = (l if x[i] == y[i] else 0) - 1
                    f *= 1 + conv(w[l]) * h
                direct += sig[x] * sig[y] * f
        # E_T R_2(sigma_T) via T-decomposition
        ET = 0
        for T in itertools.product([0, 1], repeat=len(primes)):
            wt = 1; MT = 1
            for i, l in enumerate(primes):
                wt *= conv(w[l]) if T[i] else 1 - conv(w[l])
                if T[i]:
                    MT *= l
            marg = {}
            for x in S:
                key = tuple(x[i] for i in range(len(primes)) if T[i])
                marg[key] = marg.get(key, 0) + sig[x]
            ET += wt * MT * sum(v * v for v in marg.values())
        assert abs(ET - direct) <= (0 if mode == "rat" else mp.mpf(10) ** -40), (ET, direct)
        assert ET <= 1 / Z ** 2, (mode, ET, 1 / Z ** 2)
        out[mode] = (ET, 1 / Z ** 2)
        if mode == "exp":
            lb = mpq(QA) * mp.e ** (-2 * mpq(EY) / mpq(QA))
            assert Z >= lb
            if QA >= Fr(3, 4):
                assert mp.log(ET) <= 6 * mpq(EY) + 1
    return QA, EY, leak, Eexcess, out


def mpq(f):
    return mp.mpf(f.numerator) / f.denominator


def mp_prod(v):
    r = Fr(1)
    for t in v:
        r *= t
    return r


def eta_check(primes, ncls, seed, delta=Fr(1, 2)):
    """(5): for every pair of pasts, 1+eta = l*sum_a k(a)k'(a) <= 1/(1-ptilde(x))."""
    rnd = random.Random(seed)
    # direct per-step check with random activated sets
    for _ in range(2000):
        l = rnd.choice(primes)
        F = set(rnd.sample(range(l), rnd.randint(0, l - 1)))
        F2 = set(rnd.sample(range(l), rnd.randint(0, l - 1)))
        cap = int(delta * l)
        Ft, Ft2 = set(sorted(F)[:cap]), set(sorted(F2)[:cap])
        k = [Fr(0) if a in Ft else Fr(1, l - len(Ft)) for a in range(l)]
        k2 = [Fr(0) if a in Ft2 else Fr(1, l - len(Ft2)) for a in range(l)]
        eta = l * sum(k[a] * k2[a] for a in range(l)) - 1
        pt = Fr(len(Ft), l)
        assert eta <= pt / (1 - pt) <= 2 * pt


if __name__ == "__main__":
    eta_check([3, 5, 7, 11, 13], 0, 1)
    print("[5] eta <= ptilde/(1-ptilde) <= 2 ptilde: OK (2000 random steps)")
    cases = [([3, 5, 7], 6), ([3, 5, 7], 14), ([2, 3, 5, 7], 10), ([3, 5, 7], 25), ([2, 3, 5, 7], 30)]
    worst = 0; nleak = 0
    for primes, nc in cases:
        for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 6):
            for wm in ("rand", "one"):
                QA, EY, leak, Eex, out = run(primes, nc, seed, wmode=wm)
                if out is None:
                    print(f"P={primes} n={nc} s={seed}: empty avoider set, skipped"); continue
                nleak += leak > Eex
                r = float(out["exp"][0] / out["exp"][1])
                worst = max(worst, r)
                print(f"P={primes} n={nc} s={seed} w={wm}: Q'(A)={float(QA):.3f} EY={float(EY):.3f} "
                      f"ET/Z^-2 rat={float(out['rat'][0]/out['rat'][1]):.3f} exp={r:.3f} "
                      f"leak={float(leak):.3f} Esum(p-pt)={float(Eex):.3f}")
    print(f"leak > E sum(p - ptilde) in {nleak} cases (LS5 Setting 2.0 leak bound misses 1/(1-ptilde)); leak <= 2 E sum(p-ptilde) always")
    print(f"[1-4] all asserts passed; max E_T R_2 / Z^-2 = {worst:.4f}")
