"""review_fz_brute.py (R220, from scratch): exact enumeration of Case B tuples over F_p and test of FF_STERILE_SMALL §1.
Enumeration (independent of bsE_famcount): (B) with T || w, T || C, T not| m' forces v = T^2 v1, v1(0) != 0, deg v < s,
and m'w1C1 = T^{s-2} + v1 =: F. So: for every v1 (deg e <= s-3, v1(0) != 0, lc(v1) in {1, 2} = lc(w+C)), factor F,
run over all ordered monic factorisations F = m' w1 C1, keep those with w1 + C1 = T g' v1, g' monic, T not| g'.
Checks per tuple: Lemma 1.1 (Euclidean division by every monic D | F with deg D > deg v1 returns v1 and the cofactor;
D = larger of w1, C1 always qualifies), Lemma 1.3 (v1 = -T^{s-2} mod every monic D | F).
Checks per pattern (a <= b): exact count <= EVERY route of review_fz_bounds (each route separately).
usage: uv run --with python-flint python scripts/review_fz_brute.py p SMAX"""
import sys
from itertools import product
from collections import Counter, defaultdict
import flint
sys.path.insert(0, 'scripts')
from review_fz_bounds import make_fz

p, SMAX = int(sys.argv[1]), int(sys.argv[2])
P = lambda c: flint.nmod_poly(c, p)
T = P([0, 1])
one = P([1])
R = make_fz(p)


def divisors(F):
    """all monic divisors of the monic polynomial F."""
    c, fac = F.factor()
    divs = [one]
    for (g, k) in fac:
        new = []
        for d in divs:
            x = d
            for i in range(k + 1):
                new.append(x)
                x = x * g
        divs = new
    return divs


def monic(f):
    return f.degree() >= 0 and int(f.coeffs()[-1]) == 1


viol, worst, ntup, nl11 = 0, defaultdict(float), 0, 0
for s in range(3, SMAX + 1):
    Ts2 = T**(s - 2)
    cnt = Counter()
    for e in range(0, s - 2):
        for low in product(range(p), repeat=e):
            if e > 0 and low[0] == 0:
                continue
            for lc in (1, 2):
                c = list(low) + [lc]
                if c[0] == 0:
                    continue
                v1 = P(c)
                F = Ts2 + v1
                Tv1 = T * v1
                Ds = divisors(F)
                # Lemma 1.3 / 1.1 for all monic divisors of F (properties of F and v1 alone)
                for D in Ds:
                    qq, rr = divmod(Ts2, D)
                    assert (v1 + rr) % D == 0 if D.degree() > 0 else True
                    if D.degree() > e:
                        assert rr == -v1 and qq * D == F, (s, c)
                        nl11 += 1
                for w1 in Ds:
                    G = F // w1
                    for C1 in divisors(G):
                        g, rem = divmod(w1 + C1, Tv1)
                        if rem != 0 or not monic(g) or int(g.coeffs()[0]) == 0:
                            continue
                        m = G // C1
                        a, b, z, y, t = w1.degree() + 1, C1.degree() + 1, m.degree(), g.degree(), e + 2
                        assert y + t == max(a, b) and a + b + z == s
                        # Lemma 1.1 with D = larger cofactor (deg > t-2 always)
                        Dl = w1 if a >= b else C1
                        assert Dl.degree() > e and -(Ts2 % Dl) == v1
                        ntup += 1
                        if a <= b:
                            cnt[(a, z, y, t)] += 1
    for (a, z, y, t), n in cnt.items():
        for name, bd in R['routes'](s, a, z, y, t).items():
            if bd == 0:
                print("ZERO-BOUND (degenerate args)", s, (a, z, y, t), name, n)
            if n > bd:
                viol += 1
                print("VIOLATION", p, s, (a, z, y, t), name, n, bd, flush=True)
            worst[name] = max(worst[name], n / bd)
    print(f"p={p} s={s}: tuples(a<=b)={sum(cnt.values())} patterns={len(cnt)}", flush=True)
print(f"p={p} SMAX={SMAX}: total tuples(all orders)={ntup}, Lemma 1.1 division checks={nl11}, route violations={viol}")
print("max count/route per route:", {k: round(v, 3) for k, v in sorted(worst.items())})
