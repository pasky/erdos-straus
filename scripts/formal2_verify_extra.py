"""Certificate invariants not covered by formal2_verify.py (FORMAL_CLOSURE.md §3.2, items 6-9).

uv run --with python-flint python scripts/formal2_verify_extra.py LAMFILE DUMP.json.gz

Independently of the generator's metadata:
 6. entry flags: the polynomials occurring in vertex entries are exactly those flagged `entry`;
 7. connectivity: the 7883 formal vertices form one component (shared formal denominators)
    containing the seed;
 8. for every non-dead denominator Z: all irreducible factors of 4Z-P lie in S (aux coverage),
    every prime of the constant c_r of r lies in LAM, and the precision
    needE_ell = v_ell(c_r) + v_ell(prod_{g in s} C_g^{2 e_g}) is recomputed and compared
    with the dump;
 9. E_ell = max(1 + max_g v_ell(g(qt)), needE_ell) and log10 M.
"""
import gzip
import json
import math
import sys
from fractions import Fraction
from math import gcd

import flint

sys.set_int_max_str_digits(0)
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import formal2  # noqa: E402


def main():
    LF = json.load(open(sys.argv[1]))
    st = json.load(gzip.open(sys.argv[2], "rt"))
    res = {int(l): tuple(v) for l, v in LF["residues"].items()}
    lam = sorted(res)
    qt = formal2.build_qt(res, LF.get("seed", 1))
    assert qt == int(st["qt"])
    S, flags = {}, {}
    maxval = {}
    for key, C, isaux, isentry in st["S"]:
        key = tuple(key)
        v = int(flint.fmpz_poly(list(key))(qt))
        CC = 1
        for ell in lam:
            k = 0
            while v % ell == 0:
                v //= ell
                k += 1
            if k:
                CC *= ell**k
                maxval[ell] = max(maxval.get(ell, 0), k)
        assert CC == C
        S[key] = (flint.fmpz_poly(list(key)), C)
        flags[key] = (bool(isaux), bool(isentry))
    P, X = (1, 24), (0, 1)
    V = [tuple(sorted((z[0], tuple(sorted((tuple(k), e) for k, e in z[1]))) for z in v)) for v in st["vertices"]]
    # 6. entry flags
    used = {k for v in V for z in v for k, e in z[1]}
    assert used == {k for k, f in flags.items() if f[1]}, "entry flags"
    # 7. connectivity
    par = list(range(len(V)))

    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]
            i = par[i]
        return i
    first = {}
    for i, v in enumerate(V):
        for z in v:
            if z in first:
                par[find(i)] = find(first[z])
            else:
                first[z] = i
    roots = {find(i) for i in range(len(V))}
    seed = tuple(sorted([(6, ((X, 1),)), (-12, tuple(sorted([(X, 1), (P, 1)]))), (-12, tuple(sorted([(X, 1), (P, 1)])))]))
    assert len(roots) == 1 and seed in V, "not one component"

    def polyq(z):
        c, ex = z
        num, den = flint.fmpz_poly([c]), 1
        for k, e in ex:
            num *= S[k][0] ** e
            den *= S[k][1] ** e
        return num, den

    def dead(z):
        c, ex = z
        if any(k == P for k, e in ex):
            return False
        if c < 0:
            return True
        d = sum((len(k) - 1) * e for k, e in ex)
        if d == 0:
            return False
        if d >= 2:
            return True
        num, den = polyq(z)
        a1, a0 = Fraction(int(num.coeffs()[1]), den), Fraction(int(num.coeffs()[0]), den)
        return a1 > 12 or (a1 == 12 and a0 > 0)

    need = {}
    naux = set()
    nZ = 0
    for Z in first:
        if dead(Z):
            continue
        nZ += 1
        zn, zd = polyq(Z)
        Nn = 4 * zn - flint.fmpz_poly([1, 24]) * zd
        cont, facs = Nn.factor()
        cont = int(cont)
        ex = {}
        Cp = 1
        for h, e in facs:
            if h.coeffs()[-1] < 0:
                h = -h
                if e % 2:
                    cont = -cont
            k = tuple(int(a) for a in h.coeffs())
            assert k in S, ("aux factor not in S", k)
            naux.add(k)
            ex[k] = ex.get(k, 0) + e
            Cp *= S[k][1] ** e
        cN = Fraction(cont * Cp, zd)
        assert cN.denominator == 1
        cN = int(cN)
        zc, zex = Z
        pz = dict(zex)
        pz[P] = pz.get(P, 0) + 1
        g = gcd(cN, zc)
        cr = cN // g
        sex = {k: e - min(e, ex.get(k, 0)) for k, e in pz.items()}
        rest = abs(cr)
        for ell in lam:
            while rest % ell == 0:
                rest //= ell
        assert rest == 1, ("prime of c_r outside LAM", Z)
        sden = 1
        for k, e in sex.items():
            sden *= S[k][1] ** (2 * e)
        for ell in lam:
            if cr % ell == 0:
                v = formal2.vval(cr, ell) + formal2.vval(sden, ell)
                need[ell] = max(need.get(ell, 0), v)
    dneed = {int(l): v for l, v in st["needE"].items()}
    assert need == dneed, ("needE mismatch", {l: (need.get(l), dneed.get(l)) for l in set(need) | set(dneed) if need.get(l) != dneed.get(l)})
    assert naux <= {k for k, f in flags.items() if f[0]}, "aux flags"
    E = {ell: max(maxval.get(ell, 0) + 1, need.get(ell, 0)) for ell in lam}
    print(json.dumps({"entry_flags_ok": True, "one_component": True, "nondead_Z": nZ,
                      "aux_factors_in_S": len(naux), "c_r_primes_in_LAM": True, "needE_recomputed_equal": True,
                      "E_max": max(E.values()), "log10_M": round(sum(e * math.log10(l) for l, e in E.items()), 1),
                      "OK": True}))


if __name__ == "__main__":
    main()
