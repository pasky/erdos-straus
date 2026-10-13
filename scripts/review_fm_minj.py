"""R195: independent check of FF_MUTE §6 'least shot height' (EVIDENCE). For each irreducible P (prime q only),
least j >= 0 such that P + A s^{2j} has a monic divisor f = -1 (mod A), deg f >= 1, in a valid degree regime
(deg A s^{2j} > n + deg f, or deg A s^{2j} < n); factorisation by sympy (independent of the author's code path),
the resulting solution verified exactly by review_fm_search.Searcher.verify.
Default: accept every (j, f) whose Prop 2.1 tuple verifies exactly (any degree regime);
--strict: only Prop 2.1's stated regime deg AQ^2 > n + d or the remark's deg AQ^2 < n.
Usage: review_fm_minj.py q Acoeffs scoeffs nmin nmax [--strict]"""
import sys
from collections import Counter
import sympy
from sympy.abc import x
from review_fm_ff import GF
from review_fm_search import Searcher, parse


def to_sym(P, p):
    return sympy.Poly(list(reversed(P)), x, modulus=p)


def from_sym(S, p):
    c = [int(a) % p for a in reversed(S.all_coeffs())]
    while c and c[-1] == 0:
        c.pop()
    return tuple(c)


STRICT = '--strict' in sys.argv
if STRICT:
    sys.argv.remove('--strict')


def main():
    q = int(sys.argv[1]); A = parse(sys.argv[2]); s = parse(sys.argv[3]); nmin, nmax = int(sys.argv[4]), int(sys.argv[5])
    F = GF(q)
    assert F.r == 1
    S = Searcher(F, A, s, 60, 0)
    k = len(A) - 1
    for n in range(nmin, nmax + 1):
        hist = Counter()
        regimes = Counter()
        for P in F.irreds(n):
            if P == s or F.pmod(A, P) == ():
                continue
            found = None
            for j in range(61):
                Q, AQ2 = S.Q2A[j]
                m = len(AQ2) - 1
                if m == n and STRICT:
                    continue
                N = F.padd(P, AQ2)
                _, fl = sympy.factor_list(to_sym(N, q))
                fl = [(from_sym(g, q), e) for g, e in fl]
                divs = [(1,)]
                for g, e in fl:
                    g = F.pscale(F.inv[g[-1]], g)
                    new = []
                    for dv in divs:
                        y = dv
                        for _ in range(e + 1):
                            new.append(y)
                            y = F.pmul(y, g)
                    divs = new
                for f in divs:
                    d = len(f) - 1
                    if d < 1 or F.pmod(F.padd(f, (1,)), A) != ():
                        continue
                    strict = (m > n + d) or (m < n)
                    ok = S.verify(P, j, f)
                    if strict:
                        assert ok
                    if ok and (strict or not STRICT):
                        assert m != n + d, "deg E = n cannot be valid"
                        regimes[('>n+d' if m > n + d else '<n' if m < n else '=n' if m == n else 'n..n+d')] += 1
                        found = j
                        break
                if found is not None:
                    break
            hist[found] += 1
        tot = sum(hist.values())
        mx = max(j for j in hist if j is not None) if any(j is not None for j in hist) else None
        mean = sum(j * c for j, c in hist.items() if j is not None) / tot
        print(f"q={q} A={A} s={s} n={n}: {tot} P, least-j max {mx}, mean {mean:.2f}, j=0 share {hist[0]/tot:.2f}, "
              f"none<=60: {hist[None]}; regimes of the least shots {dict(regimes)}", flush=True)


if __name__ == "__main__":
    main()
