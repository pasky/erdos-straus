"""review_fsp_enum.py (R179): independent enumeration of slice Case B solutions (q = 3, A = T^2) through the
ONE-SIDED route of FF_STERILE_PROOF Lemma 1.1 (different from the author's H,H' route):
  pick monic H', g', L'' (nonzero constant terms), E' := T H' g' L'' - 1, require E' | T^K + H'^2 L'',
  r := quotient, H := T g' r - H' monic with H(0) != 0; then (I),(II) are re-verified directly.
When a >= b, deg r = K - 1 - (b + deg g' + lambda) >= 0 bounds the search: b + deg g' + lambda <= K - 1;
solutions with a < b are obtained as H <-> H' swaps (a < b solutions met directly are skipped to avoid double counting).
Checks on every solution: Lemma 2.1 parities, D = E E' = 1 + T^{K+2} g'^2 L'', Lemma 1.2 (u-cylinder),
and whether it covers x*_c (v_T(H L' + c) >= ceil(K/2) + 1).
usage: PYTHONPATH=scripts uv run python scripts/review_fsp_enum.py KMAX [outfile]"""
import sys
from review_fsp_poly import F, s

R = F(3)
T = R.T()

def main():
    KMAX = int(sys.argv[1])
    out = open(sys.argv[2], 'w') if len(sys.argv) > 2 else None
    sols = []
    for m in range(0, KMAX):            # m = b + deg g' + lambda
        for b in range(0, m + 1):
            for dg in range(0, m - b + 1):
                lam = m - b - dg
                for Hp in R.monics(b):
                    for gp in R.monics(dg):
                        for Lpp in R.monics(lam):
                            Lp = R.mul(gp, Lpp)
                            Ep = R.sub(R.mul(T, R.mul(Hp, Lp)), (1,))
                            H2L = R.mul(R.mul(Hp, Hp), Lpp)
                            for K in range(m + 1, KMAX + 1):
                                num = R.add(R.T(K), H2L)
                                r, z = R.divmod(num, Ep)
                                if z or not r or R.deg(r) >= K:
                                    continue
                                H = R.sub(R.mul(T, R.mul(gp, r)), Hp)
                                if not H or H[-1] != 1 or H[0] == 0:
                                    continue
                                # direct re-verification of (I), (II)
                                if R.deg(H) < b:
                                    continue        # obtained (once) as the swap of an a > b solution
                                assert R.add(H, Hp) == R.mul(T, R.mul(gp, r))
                                assert R.mul(R.mul(H, Hp), Lpp) == R.add(R.T(K), r)
                                sols.append((K, H, Hp, gp, Lpp, r))
                                # this route finds exactly the solutions with a >= b (deg(T^K + H'^2 L'') = K);
                                # the a < b ones are the H <-> H' swaps (Lemma 1.1 is symmetric)
                                if R.deg(H) > b:
                                    sols.append((K, Hp, H, gp, Lpp, r))
    bad = 0
    classes = {}
    covers = []
    for (K, H, Hp, gp, Lpp, r) in sols:
        a, bb, lam = R.deg(H), R.deg(Hp), R.deg(Lpp)
        Lp = R.mul(gp, Lpp)
        E = R.sub(R.mul(T, R.mul(H, Lp)), (1,))
        Ep = R.sub(R.mul(T, R.mul(Hp, Lp)), (1,))
        D = R.add((1,), R.mul(R.T(K + 2), R.mul(gp, Lp)))
        assert R.mul(E, Ep) == D
        ok = (R.deg(E) % 2 == 0 and R.deg(Ep) % 2 == 0 and lam % 2 == K % 2 and R.deg(r) % 2 == K % 2)
        if not ok:
            bad += 1
            print("PARITY VIOLATION", K, s(H), s(Hp), s(gp), s(Lpp), s(r))
        key = (a % 2, bb % 2, lam % 2, K % 2)
        classes[key] = classes.get(key, 0) + 1
        N0 = max(2, -(-K // 2) + 1)
        # Lemma 1.2: H'(1 - T H L') == -H - T^{K+1} g'
        lhs = R.mul(Hp, R.sub((1,), R.mul(T, R.mul(H, Lp))))
        rhs = R.neg(R.add(H, R.mul(R.T(K + 1), gp)))
        assert lhs == rhs
        for c in (1, 2):
            if R.vT(R.add(R.mul(H, Lp), (c,))) >= N0:
                covers.append((K, c, s(H), s(Hp), s(gp), s(Lpp), s(r)))
        if out:
            out.write("%d %d %d %s %s %s %s %s\n" % (K, a, bb, s(H), s(Hp), s(gp), s(Lpp), s(r)))
    perK = {}
    for t in sols:
        perK[t[0]] = perK.get(t[0], 0) + 1
    print("KMAX", KMAX, "solutions", len(sols), "per K", sorted(perK.items()))
    print("parity classes (a,b,lam,K mod 2):", sorted(classes.items()), "violations", bad)
    print("covers of x*_c (N0 = max(2, ceil(K/2)+1)):", covers)

if __name__ == '__main__':
    main()
