"""review_fz1_prop61.py (R226): brute-force test of FF_STERILE_SMALL Prop 6.1 FROM THE DEFINITION of a linear family
(FUNCTIONFIELD_ES §6.2), k = 1, A = T: every family with j = v_T(lcm(a0, b0)) = 0 that is valid at some slice point x_u
(x = 1 off T, x = u mod T^oo) has u0 = u(0) = -E(0) in {-1, -2}.
For each (E, a0, b0, types) with T not dividing a0 b0 we build a concrete monic P of large degree with P = 1 mod (E_monic * L)
and P(0) = u0 = -E(0), i.e. P = x_u mod W_F (Lemma 6.2: validity depends only on P mod W_F = T E L for deg P >= n_F),
and test the definition: T a0 | P + E, T b0 | P + E, s = a + b != 0, E | s, lc(s) = lc(E).
(If T | E then T | P + E forces T | P, impossible as u0 != 0: such E are never valid; they are skipped.)
E ranges over ALL nonzero polys of degree <= dE (every leading coefficient) with L | E + 1 (necessary: P = 1 mod L and
a0, b0 | X = (P+E)/T give L | 1 + E); a0, b0 monic T-free of degree <= dA, ordered; all 16 type pairs.
usage: review_fz1_prop61.py q dA dE"""
import sys, itertools
sys.path.insert(0, 'scripts')
from review_fz1_ff import GF

def main():
    q, dA, dE = map(int, sys.argv[1:4])
    F = GF(q)
    monics = [f for d in range(dA + 1) for f in F.polys(d, monic=True, Tfree=True)]
    cnt = 0; valid = {}; examples = {}
    for a0 in monics:
        for b0 in monics:
            g = F.pgcd(a0, b0); L = F.pdivmod(F.pmul(a0, b0), g)[0]
            dL = F.deg(L)
            # E = -1 + L h, deg E <= dE, E != 0
            hs = [()] + [h for d in range(0, dE - dL + 1) for h in F.polys(d, monic=False)]
            for h in hs:
                E = F.padd(F.pmul(L, h), F.const(F.neg[1]))
                if not E or E[0] == 0: continue
                u0 = F.neg[E[0]]
                M = F.pmul(F.monic(E), L)
                extra = F.deg(a0) + F.deg(b0) + 3
                h0 = F.mul[F.add[u0][F.neg[1]]][F.inv[M[0]]]
                hh = F.padd(F.T(extra), F.const(h0))
                P = F.padd(F.const(1), F.pmul(M, hh))
                assert P[0] == u0 and P[-1] == 1 and not F.pdivmod(F.psub(P, F.const(1)), M)[1]
                PE = F.padd(P, E)
                X, rem = F.pdivmod(PE, F.T(1)); assert not rem
                ok_a = F.pdivides(a0, X); ok_b = F.pdivides(b0, X)
                if not (ok_a and ok_b): continue
                Xa = F.pdivmod(X, a0)[0]; Xb = F.pdivmod(X, b0)[0]
                A4 = [a0, F.pmul(P, a0), Xa, F.pmul(P, Xa)]
                B4 = [b0, F.pmul(P, b0), Xb, F.pmul(P, Xb)]
                for ta in range(4):
                    for tb in range(4):
                        cnt += 1
                        s = F.padd(A4[ta], B4[tb])
                        if not s: continue
                        if F.lc(s) != F.lc(E): continue
                        if F.pdivmod(s, E)[1]: continue
                        valid[u0] = valid.get(u0, 0) + 1
                        key = (u0, F.deg(E) > 0)
                        if key not in examples: examples[key] = (E, a0, b0, ta, tb)
    allowed = {F.neg[1], F.neg[2 % q if q != 2 else 0]} if q > 2 else {1}
    allowed = {F.neg[1], F.neg[F.add[1][1]]}
    print(f"q={q} dA={dA} dE={dE}: {cnt} (family, type) tests; valid j=0 families per u0: {dict(sorted(valid.items()))}")
    print(f"  allowed u0 = {{-1, -2}} = {sorted(allowed)}; examples: " + "; ".join(f"u0={k[0]} nonconstE={k[1]}: E={v[0]} a0={v[1]} b0={v[2]} t=({v[3]},{v[4]})" for k, v in sorted(examples.items())))
    bad = [u for u in valid if u not in allowed]
    print("  VIOLATIONS:", bad if bad else "none")
    sys.exit(1 if bad else 0)

main()
