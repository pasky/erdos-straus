"""R205 symbolic checks (sympy) of LENGTH_THREE Thm 2.1 table, Thm 3.1, Thm 4.1, Cor 4.2, §6 Ptolemy/identity, torus.

Usage: uv run --with sympy python scripts/review_l3_symbolic.py
"""
import sympy as sp

c, m, s, mu, d, j, p, Q, n, al = sp.symbols('c m s mu d j p Q n alpha', positive=True)
N = m * c * s - c - s
h, hp = c * m - 1, m * s - 1
ok = lambda e: sp.simplify(sp.together(e)) == 0

# Thm 2.1 table, as printed
tab = [
    (hp / N, 1 / c + 1 / (c * h) + 1 / (h * N)),
    (c / N, 1 / hp + 1 / (m * hp * N) + 1 / (m * N)),
    (m / N, 1 / (c * s) + 1 / (c * N) + 1 / (s * N)),
    (s / N, 1 / h + 1 / (m * h * N) + 1 / (m * N)),
    (h / N, 1 / s + 1 / (s * hp) + 1 / (hp * N)),
]
print("Thm 2.1 table:", [ok(l - r) for l, r in tab])
# DK Thm 4.5 / Cor 1.2 triples: slice variable = 4w, compare with the vertex identity / w
w = sp.symbols('w', positive=True)
# V1, 4|h'=A: DK Cor 1.2 Type I: 1/(b d p) + 1/(c d) + 1/(b c d), c=v=c, d=A/4, b=(p+v)/u
b = (N + c) / s
print("V1 b = h:", ok(b - h))
# V2 (4|v=c): DK 4/n = 1/(w'f') + 1/(t n w') + 1/(t n w' f'), f'=tu-1=h', t=m
print("V2 = DK 4|v:", ok(tab[1][1] - (1 / hp + 1 / (m * N) + 1 / (m * N * hp))))
# V4 (4|u=s): DK f = tv-1 = h
print("V4 = DK 4|u:", ok(tab[3][1] - (1 / h + 1 / (m * N) + 1 / (m * N * h))))

# Thm 3.1
r2 = N / m
print("Thm3.1 cs - r^2 = (c+s)/m:", ok(c * s - r2 - (c + s) / m))
z = sp.symbols('z')
K = lambda x, zz: (x * zz - r2) / (zz + x)
print("K_c(s) = 1/m:", ok(K(c, s) - 1 / m))
print("K_c o K_s = K_{1/m} (as maps):", ok(sp.together(K(c, K(s, z)) - K(1 / m, z))))
# Type II r^2
print("Type II r^2 = p/(4d):", ok((p * j) / (4 * d * j) - p / (4 * d)))

# Thm 4.1
norm = lambda X, Y: X**2 - mu * X * Y + r2 * Y**2
print("Thm4.1 m^2 Norm = hh' - m mu:", ok(m**2 * norm(1 / m, 1) - (h * hp - m * mu)))
print("  at mu_c:", ok((m**2 * norm(1 / m, 1)).subs(mu, N + c) + h), " at mu_s:", ok((m**2 * norm(1 / m, 1)).subs(mu, N + s) + hp))
# Cor 4.2: omega = 2 d z, with z^2 + mu z + r^2 = 0 and r^2 = p/(4d)
om = sp.symbols('omega')
zz = om / (2 * d)
print("Cor4.2 omega relation:", ok(sp.expand((zz**2 + mu * zz + p / (4 * d)) * 4 * d**2 - (om**2 + 2 * d * mu * om + p * d))))

# §6: pentagon with sides (Q^2,1,1,1,n), lam24=4; parametrise by h
hh = sp.symbols('h', positive=True)
cc = (hh + Q**2) / 4
hhp = (4 * n + Q**2) / hh
ss = (n + cc) / hh
rels = [4 * cc - (Q**2 + hh), hh * ss - (n + cc), 4 * ss - (hhp + 1), hh * hhp - (Q**2 + 4 * n), cc * hhp - (Q**2 * ss + n)]
print("§6 Ptolemy:", [ok(e) for e in rels])
print("§6 identity:", ok(4 / n - (1 / (ss * n) + 1 / (ss * cc) + Q**2 / (cc * n))))
# §6 generic V3 fan with arbitrary sides
L12, L23, L34, L45, L51 = sp.symbols('L12 L23 L34 L45 L51', positive=True)

# torus element f = (a, 1/a, a, 1/a, a): lam_ik -> f_i f_k lam_ik
f = [al, 1 / al, al, 1 / al, al]
sides = [f[0] * f[1], f[1] * f[2], f[2] * f[3], f[3] * f[4], f[4] * f[0]]
diag = {"c(13)": f[0] * f[2], "m(24)": f[1] * f[3], "s(35)": f[2] * f[4], "h(14)": f[0] * f[3], "h'(25)": f[1] * f[4]}
print("torus sides:", sides, "diag factors:", diag)
# torus making Q^2 side tangent
f1, f2 = sp.symbols('f1 f2', positive=True)
sol = {f1: 1 / (f2 * Q**2)}
F_ = [1 / (f2 * Q**2), f2, 1 / f2, f2, 1 / f2]
print("torus Q-side: sides", [sp.simplify(x) for x in [F_[0] * F_[1] * Q**2, F_[1] * F_[2], F_[2] * F_[3], F_[3] * F_[4]]],
      " lam14 factor", sp.simplify(F_[0] * F_[3]), " N factor", sp.simplify(F_[4] * F_[0]),
      " = f1^2 Q^2:", sp.simplify(F_[4] * F_[0] - F_[0]**2 * Q**2) == 0)
