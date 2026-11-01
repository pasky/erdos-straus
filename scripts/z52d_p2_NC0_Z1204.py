#!/usr/bin/env python3
"""Z1204: straight-line circuit size vs expanded polynomial size for verified identities.

Families (each is a 3-term identity 4/n = 1/P1 + 1/P2 + 1/P3 that holds identically in n;
integrality is on residue classes, not relevant for circuit size):
  F1 (n = 3 mod 4):  P = ((n+1)/2, (n+1)/2, n(n+1)/4)
  F2 (n = 2 mod 4):  P = ((n+2)/4, n(n+2)/4, n(n+2)/4)
  F3 (n = 3 mod 4):  P = ((n+1)/4, n(n+1)/2, n(n+1)/2)
  (F1 and F3 are the two-term n = 3 mod 4 identity with one term duplicated; F2 the n = 2 mod 4 one.)
For each family: the identity check N(n) = n(P2P3+P1P3+P1P2) - 4P1P2P3 (must be 0) is built
   (a) as an expression tree and turned into a straight-line program with sympy.cse (CSE),
       counting multiplication gates (Mul with k args = k-1 gates) and additions;
   (b) expanded: number of monomials (nonzero coefficients) and the multiplication count of the
       naive monomial-by-monomial evaluation (Horner-free), i.e. the cost of the expanded form.
Measured values are in the output; the numerator N is verified to be identically 0.
"""
import json
import sympy as sp

n = sp.symbols('n')

def count_gates(expr):
    """multiplications and additions in an expression tree (no sharing)"""
    mul = add = 0
    for node in sp.preorder_traversal(expr):
        if isinstance(node, sp.Mul):
            mul += len(node.args) - 1
        elif isinstance(node, sp.Add):
            add += len(node.args) - 1
        elif isinstance(node, sp.Pow) and node.exp.is_Integer and node.exp > 1:
            mul += int(node.exp) - 1
    return mul, add

def cse_gates(expr):
    reps, red = sp.cse(expr, optimizations=None)
    mul = add = 0
    for _, e in reps:
        m, a = count_gates(e); mul += m; add += a
    m, a = count_gates(red[0]); mul += m; add += a
    return mul, add, len(reps)

families = {
    "F1_n3mod4": [(n + 1) / 2, (n + 1) / 2, n * (n + 1) / 4],
    "F2_n2mod4":       [(n + 2) / 4, n * (n + 2) / 4, n * (n + 2) / 4],
    "F3_n3mod4_dup":   [(n + 1) / 4, n * (n + 1) / 2, n * (n + 1) / 2],
}

out = {}
for name, (P1, P2, P3) in families.items():
    lhs = 4 / n
    identity_ok = sp.simplify(lhs - (1 / P1 + 1 / P2 + 1 / P3)) == 0
    # numerator polynomial of the identity (denominators cleared): must vanish identically
    Num = sp.expand(n * (P2 * P3 + P1 * P3 + P1 * P2) - 4 * P1 * P2 * P3)
    assert Num == 0, name
    # expression as written (tree) and after CSE (straight-line program)
    expr_tree = n * (P2 * P3 + P1 * P3 + P1 * P2) - 4 * P1 * P2 * P3
    tm, ta = count_gates(expr_tree)
    cm, ca, nrep = cse_gates(expr_tree)
    # expanded form of the three denominators' product and the sum numerator (before cancellation)
    prod_expanded = sp.Poly(sp.expand(P1 * P2 * P3 * 16), n)   # clears /4 and /2 factors
    terms_expanded = len(prod_expanded.terms())
    # naive monomial evaluation cost of the expanded product: sum over monomials of deg (muls)
    naive_mul = sum(max(sum(m) - 1, 0) + 1 for m, c in prod_expanded.terms())
    out[name] = {"identity_checked": bool(identity_ok), "numerator_identically_zero": True,
                 "tree_mul": tm, "tree_add": ta, "cse_mul": cm, "cse_add": ca, "cse_temps": nrep,
                 "expanded_product_monomials": terms_expanded, "naive_expanded_mul": naive_mul}
    print(name, out[name])

json.dump(out, open("data/z52b/pass2/NC0/sub/Z1204_circuits.json", "w"), indent=1)
