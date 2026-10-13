"""FF_MUTE (O195): minimal mute shot height.  For every irreducible P of degree n (n1..n2), P coprime to sA, find the
least j >= 0 such that P + A s^{2j} has a monic divisor f (prime or composite) = -1 (mod A), deg f >= 1, giving a VALID solution of Prop 2.1's
formulas (X, Y, Zn monic, identity, parity, NC), checked exactly.  Factorisation by sympy (independent of fm_poly's
orbit/discrete-log search in fm_mute.py).  Reports per n: #P, #(j=0), max least j, mean least j, #unsolved (j<=jmax).

usage: fm_minq.py p A s n1 n2 [jmax]
"""
import sys
from sympy import Poly, symbols
from fm_poly import Fp, parse, show

T = symbols('T')
p = int(sys.argv[1]); F = Fp(p)
A = parse(sys.argv[2]); s = parse(sys.argv[3]); n1, n2 = int(sys.argv[4]), int(sys.argv[5])
jmax = int(sys.argv[6]) if len(sys.argv) > 6 else 200
k = len(A) - 1; h = len(s) - 1
minus1 = F.mod((p - 1,), A)


def to_sym(a):
    return Poly(list(reversed(a)), T, modulus=p)


def from_sym(P):
    c = [int(x) % p for x in P.all_coeffs()]
    return F.trim(list(reversed(c)))


def valid(P, f, j):
    n = len(P) - 1
    Q2 = (1,)
    for _ in range(2 * j):
        Q2 = F.mul(Q2, s)
    E, r = F.divmod(F.add(P, F.mul(A, Q2)), f)
    if r or not E:
        return False
    X, r = F.divmod(F.add(P, E), A)
    if r or not X:
        return False
    f1 = F.add(f, (1,))
    Y, r = F.divmod(F.mul(P, f1), A)
    if r:
        return False
    Zn, r = F.divmod(F.mul(F.mul(P, X), f1), A)
    if r:
        return False
    if not (X[-1] == Y[-1] == Zn[-1] == 1):
        return False
    lhs = F.mul(F.mul(F.mul(A, X), Y), Zn)
    rhs = F.mul(P, F.add(F.add(F.mul(Y, Zn), F.mul(X, Zn)), F.mul(Q2, F.mul(X, Y))))
    vz = F.val(Zn, s) - 2 * j
    degs = (len(X) - 1, len(Y) - 1, len(Zn) - 1 - 2 * j * h)
    return lhs == rhs and (vz >= 0 or vz % 2 == 0) and min(degs) >= n - k


for n in range(n1, n2 + 1):
    cnt = j0 = mx = tot = uns = esint = 0
    for P in F.irreducibles(n):
        if not F.mod(A, P) or P == s:
            continue
        cnt += 1
        found = None
        Q2 = (1,)
        for j in range(jmax + 1):
            shot = F.add(P, F.mul(A, Q2))
            facs = [(from_sym(fc.monic()), e) for fc, e in to_sym(shot).factor_list()[1]]
            divs = [(1,)]
            for g, e in facs:  # all monic divisors (R195 M3: composite moduli are allowed by Prop 2.1)
                new = []
                for dv in divs:
                    x = dv
                    for _ in range(e + 1):
                        new.append(x); x = F.mul(x, g)
                divs = new
            for f in sorted(divs, key=len):
                if len(f) > 1 and F.mod(f, A) == minus1 and valid(P, f, j):
                    found = (j, f); break
            if found:
                break
            Q2 = F.mul(F.mul(Q2, s), s)
        if not found:
            uns += 1; continue
        j, f = found
        j0 += (j == 0); mx = max(mx, j); tot += j
        sj = (1,)
        for _ in range(j):
            sj = F.mul(sj, s)
        esint += not F.mod(F.add(f, (1,)), F.mul(A, sj))
    print(f"q={p} A={show(A)} s={show(s)} n={n}: P={cnt} least-j=0: {j0}  max least j={mx}  mean={tot / max(cnt - uns, 1):.2f}"
          f"  ES-integral minimal shots={esint}  unsolved(j<={jmax})={uns}", flush=True)
