"""O181 DRINFELD_ES §3: twisted ES over F_p[T]:  A/P = c1/X + c2/Y + c3/Z, X, Y, Z monic, all degrees >= n - deg A.
(c = (1,1,1) is ES_q.) Enumerates ALL solutions: the minimal degree is exactly n - deg A (leading-term argument), so
for each position i and each monic X_i of degree n - deg A, the other two are found from the factorisation
(E Y - c2 N)(E Z - c3 N) = c2 c3 N^2 (N = P X_i, E = A X_i - c_i P), U running over unit multiples of monic
divisors of N^2. Then evaluates the BL class alpha = (-u1/u3, -u2/u3)_zeta on u_i = X_i / c_i (order m) and reports
the local invariants at Q (P = Q^e) and at infinity.
usage: bsH_twisted.py p gen m A n c1 c2 c3 [pow e]"""
import sys
from collections import Counter
from bsH_ff import FF
import bsH_bl_classes as BL  # reuse tame symbols (module reads argv; we patch below)

p, gen, m = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
Adig, n = sys.argv[4], int(sys.argv[5])
cs = [int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8])]
powe = int(sys.argv[10]) if len(sys.argv) > 10 and sys.argv[9] == 'pow' else 1
F = FF(p)
A = tuple(int(c) for c in reversed(Adig))
kA = len(A) - 1
inv = lambda x: pow(x, p - 2, p)


def solutions(P):
    sols = set()
    perms = [(0, 1, 2), (1, 0, 2), (2, 0, 1)]
    for i, j, l in perms:
        ci, cj, cl = cs[i], cs[j], cs[l]
        for X in F.monics(n - kA):
            E = F.sub(F.mul(A, X), F.scal(ci, P))
            if not E:
                continue
            N = F.mul(P, X)
            N2c = F.scal(cj * cl % p, F.mul(N, N))
            for dv in F.monic_divisors(F.mul(N, N)):
                for u in range(1, p):
                    U = F.scal(u, dv)
                    Ynum = F.add(U, F.scal(cj, N))
                    Y, r = F.divmod(Ynum, E) if Ynum else ((), ())
                    if r or not Y or Y[-1] != 1:
                        continue
                    V, r2 = F.divmod(N2c, U)
                    assert not r2
                    Z, r3 = F.divmod(F.add(V, F.scal(cl, N)), E)
                    if r3 or not Z or Z[-1] != 1:
                        continue
                    if min(len(Y), len(Z)) - 1 < n - kA:
                        continue
                    trip = [None] * 3
                    trip[i], trip[j], trip[l] = X, Y, Z
                    t = tuple(trip)
                    # verify A*XYZ = P*(c1 YZ + c2 XZ + c3 XY)
                    X1, Y1, Z1 = t
                    lhs = F.mul(A, F.mul(X1, F.mul(Y1, Z1)))
                    rhs = F.mul(P, F.add(F.add(F.scal(cs[0], F.mul(Y1, Z1)), F.scal(cs[1], F.mul(X1, Z1))),
                                         F.scal(cs[2], F.mul(X1, Y1))))
                    assert lhs == rhs, t
                    sols.add(t)
    return sols


STAT = Counter()


def invariants(t, Qs):
    # u_i = X_i / c_i ; a = -u1/u3 = -(c3/c1) X1/X3 ; b = -(c3/c2) X2/X3  as (num, den)
    X1, X2, X3 = t
    a = (F.scal((-cs[2] * inv(cs[0])) % p, X1), X3)
    b = (F.scal((-cs[2] * inv(cs[1])) % p, X2), X3)
    out = {}
    tot = 0
    for l in BL.primes_of(X1, X2, X3):
        s = BL.sym_at(a, b, l)
        tot += s
        out[l] = s
    si = BL.sym_inf(a, b)
    tot += si
    # Lemma 3.2 prediction (odd part): rotate so that u1 has degree > n - kA (cyclic shifts preserve alpha)
    degs = [len(X) - 1 for X in t]
    for r in range(3):
        i1, i2, i3 = r, (r + 1) % 3, (r + 2) % 3
        if degs[i1] > n - kA:
            break
    else:
        i1 = None
    if i1 is not None and m % 2 == 1:
        c1, c2, c3 = cs[i1], cs[i2], cs[i3]
        val_ = pow(c1, (degs[i2] - degs[i3]) % (p - 1), p) * pow(c3 * inv(c2) % p, (kA + degs[i1] - n) % (p - 1), p) % p
        pred = BL.LOG[pow(val_, (p - 1) // m, p)]
        STAT['pred_ok' if pred == si else 'pred_bad'] += 1
    iQ = sum(out.get(Q, 0) for Q in Qs) % m
    other = sum(v for l, v in out.items() if l not in Qs) % m
    vs = []
    for Xi in t:
        v = 0
        for Q in Qs:
            v, _ = BL.val(Xi, Q)
        vs.append(min(v, powe))
    shape = 'II' if sorted(vs) == [0, powe, powe] else ('I' if sorted(vs) == [0, 0, powe] else 'other')
    return shape, iQ, si, other, tot % m


def run():
    BL.p, BL.F, BL.m = p, F, m
    w = pow(gen, (p - 1) // m, p)
    BL.LOG = {pow(w, j, p): j for j in range(m)}
    res = {}
    for Q in F.irreds(n // powe):
        if not F.mod(Q, A) and False:
            continue
        P = (1,)
        for _ in range(powe):
            P = F.mul(P, Q)
        if not F.mod(P, A):
            continue
        sols = solutions(P)
        c = Counter()
        for t in sols:
            shape, iQ, si, other, tot = invariants(t, [Q])
            c[(shape, iQ, si)] += 1
            assert other == 0 and tot == 0
        res[P] = (len(sols), c)
    nP = len(res); nzero = sum(1 for v in res.values() if v[0] == 0)
    agg = Counter()
    for v in res.values():
        agg.update(v[1])
    print(f"q={p} m={m} A={Adig} n={n} c={cs} P=Q^{powe}: #P={nP} #P_no_solution={nzero} "
          f"#sol={sum(v[0] for v in res.values())} Lemma3.2 check={dict(STAT)} (shape, inv_Q, inv_inf) dist [inv_other = 0, total = 0 asserted]={sorted(agg.items())}")


if __name__ == '__main__':
    run()
