"""R77 from-scratch checks for Lemma 12.4 (leaves) and the elementary inequalities of Lemma 12.5.

(1) Lemma 12.4: for an ARBITRARY deterministic stopping/step rule on square-class quarantines
    (here: pseudo-random hash of the current state), enumerate the full decision tree and check
    (a) leaf probabilities sum to 1, (b) P(L) = 4*2^{k_L}/phi(Q_L), (c) leaf fibres are disjoint
    and their Haar masses sum to <= 1/4 (= mass of the class 1 mod 8), and the residue r_L is a
    square mod every odd prime of Q_L.
(2) y <= (1+loglogY) t^y, t = 1+1/loglogY, and log rad <= logY * rad^{1/logY} (y <= e^{sy}/(es)).
"""
import hashlib, math, itertools
from fractions import Fraction
from sympy import totient, factorint

PRIMES = [3, 5, 7, 11, 13]
FMAX = {3: 2, 5: 2, 7: 1, 11: 1, 13: 1}


def h(state, salt):
    return int(hashlib.sha256((repr(state) + salt).encode()).hexdigest(), 16)


def enumerate_tree(salt):
    leaves = []

    def rec(Q, r, a, prob, forced):
        if forced:
            l = forced[0]
            choices = [l]
        else:
            # deterministic rule: stop or pick a prime with a_l < f_l (depends only on (Q,r))
            cand = [l for l in PRIMES if a[l] < FMAX[l]]
            hv = h((Q, r), salt)
            if not cand or hv % 3 == 0:
                leaves.append((Q, r, prob))
                return
            choices = [cand[hv % len(cand)]]
        l = choices[0]
        al = a[l]
        Qn = Q * l
        if al == 0:
            sq = sorted({(x * x) % l for x in range(1, l)})
            opts = []
            for s in sq:
                # CRT lift r mod Q, s mod l
                for y in range(Qn):
                    if y % Q == r and y % l == s:
                        opts.append(y); break
            p = Fraction(1, len(opts))
        else:
            opts = [y for y in range(r, Qn, Q)]  # all lifts of r mod Q to mod Q*l
            p = Fraction(1, len(opts))
        a2 = dict(a); a2[l] = al + 1
        for y in opts:
            rec(Qn, y, a2, prob * p, forced[1:] if forced else forced)

    rec(8, 1, {l: 0 for l in PRIMES}, Fraction(1), [3, 5, 7])
    return leaves


def check_leaves(salt):
    leaves = enumerate_tree(salt)
    tot = sum(p for _, _, p in leaves)
    assert tot == 1, tot
    haar = Fraction(0)
    for Q, r, p in leaves:
        k = sum(1 for q in factorint(Q) if q != 2)
        assert p == Fraction(4 * 2 ** k, int(totient(Q))), (Q, r, p)
        for q in factorint(Q):
            if q != 2:
                assert pow(r, (q - 1) // 2, q) == 1
        assert r % 8 == 1
        haar += Fraction(1, int(totient(Q)))
    # disjointness: pairwise incompatibility of classes
    for (Q1, r1, _), (Q2, r2, _) in itertools.combinations(leaves, 2):
        g = math.gcd(Q1, Q2)
        assert r1 % g != r2 % g, (Q1, r1, Q2, r2)
    assert haar <= Fraction(1, 4)
    return len(leaves), haar


def check_ineq():
    for Y in [10, 100, 1e4, 1e8, 1e20]:
        LL = math.log(math.log(Y)); t = 1 + 1 / LL
        for y in range(0, 400):
            assert y <= (1 + LL) * t ** y + 1e-9
        s = 1 / math.log(Y)
        for z in [0.0, 0.5, 1, 5, 50, 300]:
            assert z <= math.log(Y) * math.exp(s * z) + 1e-9
        for l in [2, 3, 5, 7, 11, Y]:
            if l <= Y:
                assert l ** s - 1 <= (math.e - 1) * s * math.log(l) + 1e-12


if __name__ == "__main__":
    for salt in ["a", "b", "c", "d"]:
        print("salt", salt, "leaves, haar mass:", check_leaves(salt))
    check_ineq()
    print("inequalities OK")
