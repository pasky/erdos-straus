"""Choose residues rho_ell for the r-primes of a formal2.py dump (FORMAL_CLOSURE.md §1).

uv run --with python-flint python scripts/formal2_rho.py DUMP.json.gz [OUT.json]

For every r-prime ell (prime of some c_r outside LAM):
  * counting certificate if budget[ell] + sum_deg(S) < ell - 1;
  * otherwise (ell must be in the dump's explicit list): the covered set = roots mod ell
    of all g in S and of all recorded fragile witness polynomials at ell; report a free
    residue rho (preferring 24 rho+1 a nonzero square) or FAIL.
"""
import gzip, json, sys
from collections import defaultdict
import numpy as np
import flint


def roots(coeffs, ell):
    c = [a % ell for a in coeffs]
    while c and c[-1] == 0:
        c.pop()
    if len(c) <= 1:
        return []
    if len(c) == 2:
        return [(-c[0] * pow(c[1], -1, ell)) % ell]
    return [int(r) for r, _ in flint.nmod_poly(c, ell).roots()]


def main():
    st = json.load(gzip.open(sys.argv[1], "rt"))
    S = [k for k, C, a, e in st["S"]]
    sdeg = sum(len(k) - 1 for k in S)
    explicit = set(st["explicit"])
    budget = {int(l): b for l, b in st["budget"].items()}
    lam_max = st["B"]
    frag = defaultdict(list)
    for ell, co in st["fragile"]:
        frag[ell].append(co)
    res = {"counting": [], "explicit_ok": {}, "fail": [], "sum_deg": sdeg}
    for ell in sorted(set(st["rprimes"])):
        if ell <= lam_max:
            continue
        if ell not in explicit:
            assert budget.get(ell, 0) + sdeg < ell - 1, ("counting fails at non-explicit", ell)
            res["counting"].append(ell)
            continue
        cov = np.zeros(ell, dtype=bool)
        for k in S:
            for r in roots(k, ell):
                cov[r] = True
        nS = int(cov.sum())
        for co in frag.get(ell, []):
            for r in roots(co, ell):
                cov[r] = True
        free = np.flatnonzero(~cov)
        if len(free) == 0:
            res["fail"].append([ell, nS, len(frag.get(ell, []))])
            continue
        qr = [int(x) for x in free[:2000] if pow((24 * int(x) + 1) % ell, (ell - 1) // 2, ell) == 1]
        rho = qr[0] if qr else int(free[0])
        res["explicit_ok"][str(ell)] = {"rho": rho, "free": int(len(free)), "S_cov": nS,
                                        "nfrag": len(frag.get(ell, [])), "rho_QR": bool(qr)}
    print(json.dumps({"counting": len(res["counting"]), "explicit_ok": len(res["explicit_ok"]),
                      "fail": res["fail"][:50], "nfail": len(res["fail"]),
                      "min_free": min((v["free"] for v in res["explicit_ok"].values()), default=None),
                      "nonQR_rho": sum(1 for v in res["explicit_ok"].values() if not v["rho_QR"])}))
    if len(sys.argv) > 2:
        json.dump(res, open(sys.argv[2], "w"))


if __name__ == "__main__":
    main()
