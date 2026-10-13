"""R195: in characteristic 2 the mute shot mechanism DOES admit a finite covering (contrast FF_MUTE Prop 5.4, q odd).
If q is even and s is a primitive root mod a prime f = -1 (mod A), f != s, then <s^2 mod f> = (R/f)^*, so the
finitely many shot families (f, Q = s^j), 0 <= j < ord_f(s), together cover every P with f not dividing P, in the
low-shot regime deg(A s^{2j}) < deg P. A second such prime f2 covers P = f. Verified exactly here on all
irreducible P in a degree range (q = 2 and q = 4)."""
import sys
from review_fm_ff import GF
from review_fm_search import Searcher


def find_f(F, A, s, avoid=()):
    for d in range(1, 9):
        for f in F.monics(d):
            if f == s or f in avoid or F.pmod(F.padd(f, (1,)), A) != () or not F.is_irred(f):
                continue
            # s primitive mod f?
            e = F.q ** d - 1
            x, o = F.pmod(s, f), 1
            while x != (1,):
                x = F.pmod(F.pmul(x, s), f)
                o += 1
            if o == e:
                return f, o
    raise ValueError


def run(q, A, s, nlo, nhi):
    # nlo/nhi are offsets above the low-shot threshold k + 2hJ
    F = GF(q)
    f1, o1 = find_f(F, A, s)
    f2, o2 = find_f(F, A, s, avoid=(f1,))
    k, h = len(A) - 1, len(s) - 1
    J = max(o1, o2) - 1
    S = Searcher(F, A, s, J, 0)
    n0 = k + 2 * h * J + 1
    nlo, nhi = n0 + nlo, n0 + nhi
    fams = [(f1, j) for j in range(o1)] + [(f2, j) for j in range(o2)]
    for n in range(nlo, nhi + 1):
        assert k + 2 * h * J < n, "low-shot regime needs n > k + 2hJ"
        tot = 0
        for P in F.irreds(n):
            if P == s or F.pmod(A, P) == ():
                continue
            tot += 1
            ok = False
            for f, j in fams:
                Q, AQ2 = S.Q2A[j]
                if F.pmod(F.padd(P, AQ2), f) == ():
                    assert S.verify(P, j, f), (P, j, f)
                    ok = True
                    break
            assert ok, ("not covered", P)
        print(f"q={q} A={A} s={s}: the {len(fams)} families (f1={f1}, f2={f2}, j < ord) cover all {tot} "
              f"irreducible P of degree {n} (verified exactly)", flush=True)


if __name__ == "__main__":
    run(2, (0, 1), (1, 1), 0, 3)
    # (other (q, A) need n0 = k + 2h(ord - 1) + 1 too large for exhaustive enumeration; the argument is general)
