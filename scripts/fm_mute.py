"""FF_MUTE (O195): solve ES_q^{(s)}(A,P) by the mute shot (Prop 2.1) for every irreducible P of degree <= N,
and verify every solution exactly.

usage: fm_mute.py p A s N [maxd] [nmin]
  p prime, A and s as digit strings high->low (e.g. A=100 is T^2, s=11 is T+1).
For each P: search moduli f (monic irreducible, f = -1 mod A, f not s, f != P) by increasing degree d <= maxd;
for each, test whether -P/A lies in <s^2> mod f (discrete log by enumeration of the orbit). Records the least d,
whether s is a primitive root mod f, the least j, and whether the shot is already an ES_q solution (Cor 2.2).
The solution is then built with j lifted so that deg(A s^{2j}) > n + d, and verified:
  A X Y Zn == P (Y Zn + X Zn + Q^2 X Y), X,Y,Zn monic, z = Zn/Q^2: v_s(z) even if negative, NC degrees, Type II at P.
Prints a summary line; failures (if any) listed.
"""
import sys
from fm_poly import Fp, parse, show

p = int(sys.argv[1]); F = Fp(p)
A = parse(sys.argv[2]); s = parse(sys.argv[3]); N = int(sys.argv[4])
maxd = int(sys.argv[5]) if len(sys.argv) > 5 else 8
nmin = int(sys.argv[6]) if len(sys.argv) > 6 else None  # default: max(1, deg A)
k = len(A) - 1
minus1 = F.mod((p - 1,), A) if k >= 1 else ()
assert F.mod(A, s), "s | A"

fcache = {}


def moduli(d):
    if d not in fcache:
        L = []
        for f in F.irreducibles(d):
            if f == s or F.mod(f, A) != minus1 or not F.mod(A, f):
                continue
            # orbit of s^2 mod f
            s2 = F.mulmod(s, s, f)
            orb = {}
            x = (1,); j = 0
            while x not in orb:
                orb[x] = j
                x = F.mulmod(x, s2, f); j += 1
            ords = len(orb)  # order of s^2
            # order of s itself (R195 M4: 2*ord(s^2) = q^d-1 does not imply s primitive)
            x = s1 = F.mod(s, f); os_ = 1
            while x != (1,):
                x = F.mulmod(x, s1, f); os_ += 1
            prim = (os_ == p ** d - 1)
            L.append((f, orb, ords, prim))
        fcache[d] = L
    return fcache[d]


def solve(P):
    n = len(P) - 1
    for d in range(1, maxd + 1):
        for f, orb, ords, prim in moduli(d):
            if f == P:
                continue
            Pm = F.mod(P, f)
            if not Pm:
                continue
            t = F.mod(F.neg(F.mul(Pm, F.egcd_inv(A, f))), f)
            if t in orb:
                return d, f, orb[t], ords, prim
    return None


def build_verify(P, f, j0, ords):
    n = len(P) - 1; d = len(f) - 1; h = len(s) - 1
    j = j0
    while j < 1 or k + 2 * j * h <= n + d:
        j += ords
    Q = (1,)
    for _ in range(j):
        Q = F.mul(Q, s)
    Q2 = F.mul(Q, Q)
    num = F.add(P, F.mul(A, Q2))
    E, r = F.divmod(num, f); assert not r
    X, r = F.divmod(F.add(P, E), A); assert not r
    f1 = F.add(f, (1,))
    Y, r = F.divmod(F.mul(P, f1), A); assert not r
    Zn, r = F.divmod(F.mul(F.mul(P, X), f1), A); assert not r
    ok = True
    lhs = F.mul(F.mul(F.mul(A, X), Y), Zn)
    rhs = F.mul(P, F.add(F.add(F.mul(Y, Zn), F.mul(X, Zn)), F.mul(Q2, F.mul(X, Y))))
    ok &= lhs == rhs
    ok &= X[-1] == 1 and Y[-1] == 1 and Zn[-1] == 1
    vz = F.val(Zn, s) - 2 * j
    ok &= (vz >= 0) or (vz % 2 == 0)
    degs = (len(X) - 1, len(Y) - 1, len(Zn) - 1 - 2 * j * h)
    ok &= min(degs) >= n - k and sorted(degs)[0] == n - k
    ok &= bool(F.mod(X, P)) and not F.mod(Y, P) and not F.mod(Zn, P)
    esint = vz >= 0
    return ok, esint, j


def main():
    tot = 0; bad = []; hist = {}; nprim = 0; nes = 0; maxj = 0; nq1 = 0
    for n in range(nmin if nmin is not None else max(1, k), N + 1):
        for P in F.irreducibles(n):
            if not F.mod(A, P) or P == s:
                continue
            tot += 1
            r = solve(P)
            if r is None:
                bad.append(show(P)); continue
            d, f, j0, ords, prim = r
            hist[d] = hist.get(d, 0) + 1
            nprim += prim
            nq1 += (j0 == 0)
            maxj = max(maxj, j0)
            ok, esint, j = build_verify(P, f, j0, ords)
            if not ok:
                bad.append('VERIFYFAIL ' + show(P))
    print(f"q={p} A={show(A)} s={show(s)} n<={N}: P={tot} unsolved/badverify={len(bad)} "
          f"min-d histogram={dict(sorted(hist.items()))} s-primitive-at-chosen-f={nprim} j0=0(ES shot P+A)={nq1} max j0={maxj}")
    if bad:
        print("BAD:", ' '.join(bad[:50]))


main()
