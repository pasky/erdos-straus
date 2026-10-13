"""review_fsp_cyclo.py (R179): independent re-run of the cyclotomic (r = r0 constant) search of FF_STERILE_PROOF §4.
Own factorisation (review_fsp_poly: squarefree + DDF + Cantor–Zassenhaus, each factor re-tested irreducible and the
product re-multiplied), own split enumeration: every exponent split of T^K + r0 = H H' L'' (all monic),
test (I) H + H' = r0 T g', g' monic with g'(0) != 0 (r constant => r = r0), re-verify (II) by multiplication,
and record z = v_T(H g' L'' + c) vs N0 = ceil(K/2) + 1 (covers x*_c iff z >= N0).
Odd K are also run (Lemma 2.1 predicts no solutions there).
usage: PYTHONPATH=scripts uv run python scripts/review_fsp_cyclo.py KMIN KMAX CAP"""
import sys, itertools
from review_fsp_poly import F

R = F(3)

def splits(K, r0, cap):
    f = R.add(R.T(K), (r0,))
    fac = R.factor(f)
    chk = (1,)
    for g, m in fac.items():
        assert R.is_irred(g)
        for _ in range(m):
            chk = R.mul(chk, g)
    assert chk == f
    items = list(fac.items())
    tot = 1
    for g, m in items:
        tot *= (m + 1) * (m + 2) // 2
    if tot > cap:
        return None, tot
    pw = []
    for g, m in items:
        p = [(1,)]
        for _ in range(m):
            p.append(R.mul(p[-1], g))
        pw.append(p)
    sols = []
    ranges = [[(i, j) for i in range(m + 1) for j in range(m + 1 - i)] for g, m in items]
    for combo in itertools.product(*ranges):
        H, Hp, L = (1,), (1,), (1,)
        for idx, (i, j) in enumerate(combo):
            m = items[idx][1]
            H = R.mul(H, pw[idx][i]); Hp = R.mul(Hp, pw[idx][j]); L = R.mul(L, pw[idx][m - i - j])
        S = R.add(H, Hp)
        if not S or S[0] != 0:
            continue
        gp = R.scal(r0, S[1:])          # r0^{-1} = r0 in F_3
        if gp[-1] != 1 or gp[0] == 0:
            continue
        assert R.mul(R.mul(H, Hp), L) == f
        assert R.add(H, Hp) == R.mul(R.T(), R.scal(r0, gp))
        sols.append((R.deg(H), R.deg(Hp), R.mul(H, R.mul(gp, L))))
    return sols, tot

def main():
    K0, K1, cap = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    for K in range(K0, K1 + 1):
        N0 = -(-K // 2) + 1
        out = []
        for r0 in (1, 2):
            sols, tot = splits(K, r0, cap)
            if sols is None:
                out.append("r0=%d:SKIP(%d splits)" % (r0, tot)); continue
            zb = []
            for c in (1, 2):
                zs = [R.vT(R.add(X, (c,))) for (_, _, X) in sols]
                zb.append(max(zs) if zs else -1)
                for (a, b, X), z in zip(sols, zs):
                    if z >= N0:
                        print("HIT x*_%d K=%d r0=%d a=%d b=%d" % (c, K, r0, a, b), flush=True)
            out.append("r0=%d:n=%d zbest=(%d,%d)" % (r0, len(sols), zb[0], zb[1]))
        print(K, "N0", N0, " ".join(out), flush=True)

if __name__ == '__main__':
    main()
