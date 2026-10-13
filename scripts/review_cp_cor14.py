"""R203: explicit counterexample to the literal wording of COMPOSITION_ES Cor 1.4(a).
p = 11, mu = 18: j = 1, t = 7, D = 4tj - 1 = 27 does not divide 18, yet eps_mu = u * alpha^3 with alpha a V_11
point at mu = 18 (D = 3) and u a unit of O' = Z[2 sqrt f], f = 313.  Exact integer arithmetic.
"""
from math import isqrt, gcd

n, mu = 11, 18
f = mu * mu - n
j, t = (mu - 1) // n, (mu - 1) % n + 1
D = 4 * t * j - 1
eps = (1 - 2 * j * mu, 2 * j)  # 1 - 2 j etabar = (1 - 2 j mu) + 2 j sqrt f
mul = lambda a, b: (a[0] * b[0] + f * a[1] * b[1], a[0] * b[1] + a[1] * b[0])
nrm = lambda a: a[0] ** 2 - f * a[1] ** 2
print("f =", f, "j,t =", j, t, "D =", D, "N(eps) =", nrm(eps), "D | mu ?", mu % D == 0)
# V_n points at mu with D = 3, small A
pts = []
for A in range(2, 400, 2):
    for B in range(1, 2 * mu * A, 2):
        if 2 * mu * A * B - n * A * A - B * B == 3 and gcd(A, B) == 1:
            pts.append((A, B))
print("V_11 points at mu=18 with D=3 (A<400):", pts[:4])
for (A, B) in pts[:2]:
    for conj in (1, -1):
        al = (B - mu * A, conj * A)
        a3 = mul(mul(al, al), al)
        # u = eps / a3 = eps * conj(a3) / N(a3)
        num = mul(eps, (a3[0], -a3[1])); den = nrm(a3)
        if num[0] % den == 0 and num[1] % den == 0:
            u = (num[0] // den, num[1] // den)
            print(f"alpha = {al} (A,B)=({A},{B}), N(alpha) = {nrm(al)}; eps = u*alpha^3 with u = {u}, N(u) = {nrm(u)},"
                  f" u in O' (even sqrt f coeff): {u[1] % 2 == 0}; check: {mul(u, a3) == eps}")

# generator of norm -3 from the CF of sqrt(4f) (Lagrange), exact
N = 4 * f; a0 = isqrt(N); m, Q, a = 0, 1, a0
p0, p1, q0, q1 = 1, a0, 0, 1
gens = []
while True:
    if abs(p1 * p1 - N * q1 * q1) == 3:
        gens.append((p1, q1))
    m = Q * a - m; Q = (N - m * m) // Q; a = (a0 + m) // Q
    p0, p1 = p1, a * p1 + p0; q0, q1 = q1, a * q1 + q0
    if Q == 1:
        break
print("convergents with |norm| = 3 in one period:", [(x, y, x * x - N * y * y) for x, y in gens][:2])
for (x, y) in gens[:1]:
    for s in (1, -1):
        al = (x, 2 * y * s)  # x +- y sqrt N = x +- 2y sqrt f
        A, B = abs(al[1]), (al[0] if al[1] > 0 else -al[0]) + mu * abs(al[1])
        assert n * A * A + B * B + 3 == 2 * mu * A * B and gcd(A, B) == 1 and B % 2 == 1
        a3 = mul(mul(al, al), al)
        num = mul(eps, (a3[0], -a3[1])); den = nrm(a3)
        ok = num[0] % den == 0 and num[1] % den == 0
        if ok:
            u = (num[0] // den, num[1] // den)
            print(f"V_11 point (A,B,D,mu) = ({A},{B},3,18); eps_18 = u*alpha^3, u = {u}, N(u) = {nrm(u)}, "
                  f"u in O': {u[1] % 2 == 0}, exact: {mul(u, a3) == eps}")
