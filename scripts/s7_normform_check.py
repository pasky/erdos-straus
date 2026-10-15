"""s7_normform_check: symbolic checks of the rearrangements used in SYNTHESIS_SPARKS7 Thms 1.1/1.2 (sympy), plus a
random-coefficient search for Type II/I families with deg <= 2 parameters on Q = u^2 + v^2 solving the ET equations
modulo nothing (exact polynomial identity) that are NOT in Q[Q] (expected: none).
"""
import sympy as sp, itertools, random
u, v = sp.symbols('u v'); Q = u**2 + v**2
A, B, C, D, E, k, kp, EA, EB = sp.symbols('A B C D E k kp EA EB')
chk = []
# II (b2): with A = (Q+E)/(4BD): C*(4BDA - Q) - (A+B) == 0  <=>  Q + 4B^2 D == E*(4BDC - 1) (times 1/(4BD))
Aexpr = (Q + E) / (4 * B * D)
lhs = sp.expand((C * (4 * B * D * Aexpr - Q) - (Aexpr + B)) * 4 * B * D)
chk.append(sp.simplify(lhs - (E * (4 * B * D * C - 1) - Q - 4 * B**2 * D)) == 0)
# I (c1, B quadratic): B = (Q+E)/(4CD); A(4BCD - Q) = QB + C  <=>  4CD*A*E = Q(Q+E) + 4C^2 D
Bexpr = (Q + E) / (4 * C * D)
chk.append(sp.simplify(sp.expand(4 * C * D * (Q * Bexpr + C)) - sp.expand(Q * (Q + E) + 4 * C**2 * D)) == 0)
# I (c1, C quadratic): C = Q/(4BD) + E: 4ABCD - Q(A+B) - C == 4ABD*E - (B + 1/(4BD))Q - E
Cexpr = Q / (4 * B * D) + E
chk.append(sp.simplify(4 * A * B * Cexpr * D - Q * (A + B) - Cexpr - (4 * A * B * D * E - (B + 1 / (4 * B * D)) * Q - E)) == 0)
# I (c2, mu=2): A = kQ+EA, B = kpQ+EB, C, D const: 4CDAB - Q(A+B) - C == (4CDk kp - k - kp)Q^2 + Q*G + 4CD EA EB - C
Ae, Be = k * Q + EA, kp * Q + EB
G = (4 * C * D * k - 1) * EB + (4 * C * D * kp - 1) * EA
chk.append(sp.expand(4 * C * D * Ae * Be - Q * (Ae + Be) - C - ((4 * C * D * k * kp - k - kp) * Q**2 + Q * G + 4 * C * D * EA * EB - C)) == 0)
print("symbolic rearrangement checks:", chk)
# random search: parameters A,B,C,D of degree <= 2 with integer coefficients in [-2,2] satisfying Type II or Type I exactly
mons = [1, u, v, u**2, u * v, v**2]
def rp(rng, deg):
    ms = [m for m in mons if sp.Poly(m, u, v).total_degree() <= deg]
    if rng.random() < 0.3:  # constants often, as positive controls (they must give hits)
        ms = [1]
    return sum(rng.randint(-2, 2) * m for m in ms)
rng = random.Random(7); hits = 0; nonQ = 0; trials = 0
# Solve for the last parameter instead of guessing it: Type II: A = (B + C Q)/(4BCD - 1) must be a polynomial
for _ in range(20000):
    Bp, Cp, Dp = rp(rng, 1), rp(rng, 1), rp(rng, 2)
    if 0 in (Bp, Cp, Dp): continue
    trials += 1
    num, den = sp.expand(Bp + Cp * Q), sp.expand(4 * Bp * Cp * Dp - 1)
    if den == 0: continue
    q, r = sp.div(sp.Poly(num, u, v, domain='QQ'), sp.Poly(den, u, v, domain='QQ'))
    if r.is_zero and not q.is_zero:
        hits += 1
        inQ = all(sp.Poly(x, u, v).total_degree() == 0 for x in (Bp, Cp, Dp))
        nonQ += (not inQ)
print("Type II random trials:", trials, "polynomial solutions (positive controls: all-constant B,C,D):", hits, "with a non-constant B/C/D (must be 0):", nonQ)
