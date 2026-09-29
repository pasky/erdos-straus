"""Consistency certificate for a stabilized formal seed component (DEPTH3 §6).

uv run python scripts/formal_consistency.py DUMP.json.gz

The formal model fixes the class of q* only at primes ell<=B. A stabilized
closure yields a genuine H-conditional theorem only if the following hold:

 (a) every prime needed for the character argument, or occurring in a formal
     constant, lies in a set Lambda on which q* can be fixed consistently:
       * primes of vertex constants,
       * primes of C_g and of the leading coefficients,
       * primes of H_g = 24^deg g(-1/24), for g != 24X+1.
     For such ell > B the model assumed v_ell(g(q*)) = 0 for every g. So we
     need a residue q mod ell with q != 0, 24q+1 a nonzero square, and no g in
     S vanishing ("QR-feasible").
 (b) for every other prime ell <= sum deg g, Hypothesis H needs no fixed prime
     divisor: some residue q mod ell must avoid all roots of all g in S.

The script reports the primes where (a) or (b) fails. None failing means the
model is consistent: extend q* by the found residues.
"""
from __future__ import annotations

import gzip
import json
import sys
from math import prod

from sympy import factorint, primerange
from sympy.ntheory import sqrt_mod


def main():
    st = json.load(gzip.open(sys.argv[1], "rt"))
    B = st["B"]
    SMALL = set(primerange(2, B + 1)) | set(st.get("extra_small", []))
    S = [(tuple(c), C) for c, C in st["primes"]]
    degs = [len(c) - 1 for c, _ in S]
    sdeg = sum(degs)
    need = {}

    def add(n, why):
        for ell in factorint(abs(int(n))):
            need.setdefault(ell, set()).add(why)

    aux = {tuple(c) for c in st.get("aux_only", [])}
    for c, C in S:
        add(C, "C_g")
        add(c[0], "lc")
        if c != (24, 1) and c not in aux:  # H_g only matters for denominators
            d = len(c) - 1
            H = sum(a * 24 ** (d - i) * (-1) ** i for i, a in enumerate(c))
            assert H != 0
            add(H, "H_g")
    for v in st["vertices"]:
        for const, _ in v:
            add(const, "const")
    big_need = sorted(ell for ell in need if ell not in SMALL)
    print(json.dumps({"formal_primes": len(S), "sum_deg": sdeg, "vertices": len(st["vertices"]),
                      "stabilized": st["stabilized"], "B": B, "aux_only": len(aux),
                      "Lambda_primes_above_B": len(big_need), "max_needed_prime": max(need)}))

    def roots_one(c, ell):
        cm = [a % ell for a in c]
        while cm and cm[0] == 0:
            cm = cm[1:]
        if not cm:
            return None
        if len(cm) == 1:
            return set()
        if len(cm) == 2:
            return {(-cm[1] * pow(cm[0], -1, ell)) % ell}
        if len(cm) == 3 and ell > 2:
            a, b, cc = cm
            disc = (b * b - 4 * a * cc) % ell
            inv = pow(2 * a, -1, ell)
            if disc == 0:
                return {(-b * inv) % ell}
            rts = sqrt_mod(disc, ell, all_roots=True) or []
            return {((-b + r) * inv) % ell for r in rts}
        out = set()
        for q in range(ell):
            v = 0
            for a in cm:
                v = (v * q + a) % ell
            if v == 0:
                out.add(q)
        return out

    def roots_mod(ell):
        bad = set()
        for c, _ in S:
            r = roots_one(c, ell)
            if r is None:
                return None
            bad |= r
        return bad

    fail_a, fail_b = [], []
    for ell in big_need:
        bad = roots_mod(ell)
        ok = bad is not None and any(
            q % ell and pow((24 * q + 1) % ell, (ell - 1) // 2, ell) == 1 and q not in bad
            for q in range(1, ell))
        if not ok:
            fail_a.append(ell)
    for ell in primerange(B + 1, sdeg + 2):
        if ell in need or ell in SMALL:
            continue
        bad = roots_mod(ell)
        if bad is None or len(bad) >= ell:
            fail_b.append(ell)
    # (c) primes of const(r) above B: q* = qt there. Need: no S-rval divisible by ell,
    #     no accidental flag, and 24qt+1 a residue if ell is also a character prime.
    qt = int(st["qt"])
    rp = [int(l) for l in st.get("r_primes", [])]
    fail_c = []
    RB = {int(l): b for l, b in st.get("r_root_budget", {}).items()}
    for ell in rp:
        if ell in SMALL:
            continue
        # generic residue: q* mod ell chosen QR-feasible avoiding all roots of S and of
        # every candidate D+s in fibres with ell | const(r); counting bound suffices
        if sdeg + RB.get(ell, 10**30) < (ell - 3) // 2:
            continue
        bad = any((sum(a * pow(qt, len(c) - 1 - i, ell) for i, a in enumerate(c)) % ell) == 0
                  and (C % ell) for c, C in S)
        if ell in need and pow((24 * qt + 1) % ell, (ell - 1) // 2, ell) != 1:
            bad = True
        if bad:
            fail_c.append(ell)
    # (primes of const(r) passing the counting bound are chosen generically; others are listed in fail_c)
    print(json.dumps({"r_primes_above_B": len(rp), "fail_c": fail_c[:50], "n_fail_c": len(fail_c),
                      "accidental_flags": len(st.get("flags", []))}))
    print(json.dumps({"QR_infeasible_needed_primes": fail_a[:50], "n_fail_a": len(fail_a),
                      "fixed_divisor_primes": fail_b[:50], "n_fail_b": len(fail_b)}))


if __name__ == "__main__":
    main()
