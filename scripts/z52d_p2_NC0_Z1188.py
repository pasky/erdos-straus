#!/usr/bin/env python3
"""Z1188: heuristic discovery separated from the Lean kernel, for the C-form family.

Discovery (untrusted, this script): for each n in [2, NMAX], search C >= 1 with 4C <= n+2
(cform_C_bound) and a divisor a of 4Cn+1 with 4C | a+1 (CForm n C a, Basic.lean:81). Output:
one certificate (n, C, a) per n where found.
Kernel (trusted, Lean): lean/ES/ES/Basic.lean `cform_ES` turns any CForm certificate into the
explicit solution x = Cuv, y = nCv, z = nCu of 4xyz = n(xy+yz+zx). This script only writes
a Lean file that applies `cform_ES` to each certificate with the side condition discharged by
`decide`; the Lean build (run separately in a /tmp copy of lean/ES) is the check.
Not trusted: the Python search itself; its output is re-checked by Lean.
"""
import sys

def find_cform(n):
    for C in range(1, (n + 2) // 4 + 1):
        N = 4 * C * n + 1
        # divisors a of N with 4C | a+1, a <= N
        a = 4 * C - 1          # candidates a = 4C*k - 1
        while a <= N:
            if N % a == 0 and (a + 1) % (4 * C) == 0:
                return C, a
            a += 4 * C
    return None

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    certs = []
    for n in range(2, NMAX + 1):
        c = find_cform(n)
        if c:
            certs.append((n, c[0], c[1]))
    print("n with C-form certificate found:", len(certs), "of", NMAX - 1)
    print("first:", certs[:8])
    # Lean kernel input
    lines = ["import ES.Basic", "", "namespace ES", ""]
    for n, C, a in certs:
        lines.append(f"example : ESProp {n} := cform_ES (show CForm {n} {C} {a} by unfold CForm; decide)")
    lines += ["", "end ES", ""]
    open("data/z52b/pass2/NC0/sub/Z1188_certs.lean", "w").write("\n".join(lines))
    open("data/z52b/pass2/NC0/sub/Z1188_certs.txt", "w").write("\n".join(f"{n} {C} {a}" for n, C, a in certs) + "\n")
