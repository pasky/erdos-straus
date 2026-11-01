"""Sharpness check for Theorem B(b,c): best mean of a frequency certificate, by linear programming.

For a block with modulus set Qset = {4uB}, a certificate of degree H is a real even trigonometric polynomial
G(x) = c_0 + 2 sum_{h=1}^H c_h cos(2 pi h x) with G(0) <= 1 and G(r/q) <= 0 for every q in Qset and r/q not in Z.
Theorem B(b): if H < q_max/2 then c_0 <= 0.  Theorem B(c): positive c_0 is possible from H ~ q_max/2 on.
We maximise c_0 by LP (scipy) for small blocks and report max c_0 and G(0) at the optimum, as a function of H.
(Even G suffices: symmetrising G(x) -> (G(x)+G(-x))/2 preserves the constraints, since T is symmetric, and the mean.)
NOTE (review F19): coefficients are box-bounded |c_h| <= 10 (an artificial bound, hit for H >= q_max where T is too
sparse to constrain G); floating-point HiGHS LP: this is EVIDENCE, not an exact certified optimum.
Usage: uv run --with numpy --with scipy python scripts/z53_hypkloost_certificate_lp.py
"""
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction

def block_moduli(U, V):
    return sorted({4 * u * B for u in range(U + 1, 2 * U + 1) for B in range(V + 1, 2 * V + 1)})

def best_mean(Qs, H):
    pts = sorted({Fraction(r, q) for q in Qs for r in range(1, q)})
    xs = np.array([float(f) for f in pts])
    h = np.arange(1, H + 1)
    # rows: G(x) = c0 + sum 2 c_h cos(2 pi h x) <= 0 at x in T ; G(0) <= 1
    A = np.hstack([np.ones((len(xs), 1)), 2 * np.cos(2 * np.pi * np.outer(xs, h))])
    A0 = np.hstack([[1.0], 2 * np.ones(H)])[None, :]
    A_ub = np.vstack([A, A0]); b_ub = np.concatenate([np.zeros(len(xs)), [1.0]])
    cobj = np.zeros(H + 1); cobj[0] = -1.0
    bounds = [(-10, 10)] * (H + 1)
    res = linprog(cobj, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    if res.status != 0:
        return None, None
    c = res.x
    return c[0], c[0] + 2 * c[1:].sum()

if __name__ == "__main__":
    for (U, V) in [(2, 2), (2, 3), (3, 3)]:
        Qs = block_moduli(U, V)
        qmin, qmax = min(Qs), max(Qs)
        print(f"block U={U} V={V}: q_min={qmin} q_max={qmax} q_max/2={qmax//2}")
        for H in sorted({qmin - 1, qmax // 2 - 2, qmax // 2 - 1, qmax // 2, qmax // 2 + 1, qmax // 2 + 4, qmax}):
            m, g0 = best_mean(Qs, H)
            print(f"   H={H:4d}: max mean c0 = {m:+.6f}   G(0) = {g0:+.4f}")
