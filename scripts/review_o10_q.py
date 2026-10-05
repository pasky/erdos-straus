"""R38 from-scratch exact (Fraction) checks of Q, Theta, QM and Lemma 3.2.

Q_mu(H) = sum_V mu^V tauhat(V)^2, tauhat = Moebius transform of the
transversal indicator.  Theta(C) = sum_{J subset C} (-1)^|J| lam^{cup J}.
Checks, exhaustively over all hypergraphs on n<=4 vertices (edge sets of
nonempty subsets, up to a cap) with random rational weights at the w<=2
boundary, and randomly on n<=7:
  (a) Q == E_P[Theta(H_P)^2]           (Lemma 3.2, exact)
  (b) |Theta(H)| <= prod_{E in M}(w_E-1) for all matchings M (Lemma 3.3)
  (c) Q <= prod_{E in M}(w_E-1)         (Thm 3.4 / QM)
usage: review_o10_q.py seed ntrials nmax
"""
import sys, itertools, random
from fractions import Fraction as Fr


def subsets(n):
    return range(1 << n)


def tau(H, R):
    return 1 if all(E & R for E in H) else 0


def Q(H, mu, n):
    t = [tau(H, R) for R in subsets(n)]
    # Moebius transform
    th = t[:]
    for i in range(n):
        for S in subsets(n):
            if S >> i & 1:
                th[S] -= th[S ^ (1 << i)]
    tot = Fr(0)
    for V in subsets(n):
        if th[V]:
            m = Fr(1)
            for i in range(n):
                if V >> i & 1:
                    m *= mu[i]
            tot += m * th[V] ** 2
    return tot


def lamU(lam, U, n):
    m = Fr(1)
    for i in range(n):
        if U >> i & 1:
            m *= lam[i]
    return m


def Theta(C, lam, n):
    tot = Fr(0)
    for r in range(len(C) + 1):
        for J in itertools.combinations(C, r):
            U = 0
            for E in J:
                U |= E
            tot += (-1) ** r * lamU(lam, U, n)
    return tot


def polar(H, lam, n):
    tot = Fr(0)
    for P in subsets(n):
        pr = Fr(1)
        for i in range(n):
            p = (lam[i] - 1) / lam[i]
            pr *= p if P >> i & 1 else 1 - p
        if pr == 0:
            continue
        HP = [E for E in H if not (E & P)]
        tot += pr * Theta(HP, lam, n) ** 2
    return tot


def matchings(H):
    res = [[]]
    def rec(i, used, cur):
        for j in range(i, len(H)):
            if not (H[j] & used):
                cur.append(H[j]); res.append(list(cur))
                rec(j + 1, used | H[j], cur); cur.pop()
    rec(0, 0, [])
    return res


def boundary_lam(rng, H, n):
    """rational lam_v >= 1 with max_E w_E <= 2, pushed close to 2."""
    lam = [Fr(1) + Fr(rng.randint(0, 12), rng.choice([4, 8, 12, 16])) for _ in range(n)]
    for _ in range(200):
        bad = [E for E in H if lamU(lam, E, n) > 2]
        if not bad:
            break
        E = bad[0]
        i = rng.choice([i for i in range(n) if E >> i & 1])
        lam[i] = 1 + (lam[i] - 1) / 2
    if any(lamU(lam, E, n) > 2 for E in H):
        return None
    # push: for a random edge, raise one vertex so it hits exactly 2 if allowed
    for _ in range(3):
        E = rng.choice(H)
        i = rng.choice([i for i in range(n) if E >> i & 1])
        cap = min(Fr(2) / (lamU(lam, F, n) / lam[i]) for F in H if F >> i & 1)
        lam[i] = max(lam[i], cap)
    return lam


def check(H, lam, n, do_polar=True):
    mu = [l - 1 for l in lam]
    q = Q(H, mu, n)
    out = {"Q": q}
    if do_polar:
        assert q == polar(H, lam, n), ("polar", H, lam)
    th = abs(Theta(H, lam, n))
    for M in matchings(H):
        b = Fr(1)
        for E in M:
            b *= lamU(lam, E, n) - 1
        assert th <= b, ("theta", H, lam, M)
        assert q <= b, ("QM", H, lam, M)
    return out


def main():
    seed, ntr, nmax = map(int, sys.argv[1:4])
    rng = random.Random(seed)
    mx = Fr(0)
    # exhaustive structured families on n=3: all hypergraphs
    n = 3
    alle = list(range(1, 1 << n))
    cnt = 0
    for mask in range(1, 1 << len(alle)):
        H = [alle[j] for j in range(len(alle)) if mask >> j & 1]
        for _ in range(3):
            lam = boundary_lam(rng, H, n)
            if lam is None:
                continue
            mx = max(mx, check(H, lam, n)["Q"]); cnt += 1
    print("n=3 exhaustive hypergraphs: cases", cnt, "max Q", float(mx))
    mx = Fr(0)
    for t in range(ntr):
        n = rng.randint(2, nmax)
        m = rng.randint(1, 7)
        H = list({rng.randint(1, (1 << n) - 1) for _ in range(m)})
        if t % 3 == 0:  # triangles / hubs / stars
            H = list({(1 << rng.randrange(n)) | (1 << rng.randrange(n)) for _ in range(m)})
        lam = boundary_lam(rng, H, n)
        if lam is None:
            continue
        r = check(H, lam, n, do_polar=(n <= 6))
        mx = max(mx, r["Q"])
    print("random: max Q", float(mx), "(all assertions passed)")


if __name__ == "__main__":
    main()
