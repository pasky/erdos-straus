"""R81: check the de la Vallee Poussin kernel facts in the proof of Thm 2.1.
v = 2 k_{2d} - k_d, k_d(x) = d (sin(pi d x)/(pi d x))^2.
 (i) |v(x)| <= 5 d min(1, (pi d x)^-2)
 (ii) sum_m v(m) e(-m theta) = 1 for ||theta|| <= d  (d <= 1/4)
 (iii) sum_m |v(m)| 1_A(r+m) <= 12 d M(L), L = ceil(1/d), for adversarial A
       (A = union of blocks placed to maximise sum |v| over A, worst case).
"""
import numpy as np


def k(x, d):
    y = np.pi * d * x
    s = np.where(y == 0, 1.0, np.sin(y) / np.where(y == 0, 1, y))
    return d * s * s


def v(x, d):
    return 2 * k(x, 2 * d) - k(x, d)


worst_i = 0
worst_ii = 0
worst_iii = 0
for d in [1 / 4, 1 / 5, 1 / 7.3, 1 / 10, 1 / 33, 1 / 100]:
    x = np.linspace(-2000 / d, 2000 / d, 2_000_001)
    env = 5 * d * np.minimum(1, (np.pi * d * np.where(x == 0, 1e-9, x)) ** -2.0)
    worst_i = max(worst_i, np.max(np.abs(v(x, d)) / env))
    L = int(np.ceil(1 / d))
    nb = 4000
    m = np.arange(-nb * L, nb * L)
    vm = v(m.astype(float), d)
    for th in np.linspace(-d, d, 41):
        S = np.sum(vm * np.cos(2 * np.pi * m * th))  # v even, so real
        worst_ii = max(worst_ii, abs(S - 1))
    # (iii) the worst set for sum |v(m)| 1_A(m) given block budget M(L)=c:
    # each block I_j = [jL,(j+1)L) contributes at most the c largest |v| in it.
    av = np.sort(np.abs(vm).reshape(2 * nb, L), axis=1)[:, ::-1]
    for c in [1, max(1, L // 3), L]:
        tot = av[:, :c].sum()
        worst_iii = max(worst_iii, tot / (12 * d * c))
print(f"(i) max |v|/(5d min(1,(pi d x)^-2)) = {worst_i:.4f}  (<=1 required)")
print(f"(ii) max |sum v(m)e(-m th) - 1| over ||th||<=d = {worst_ii:.2e} (truncation error only)")
print(f"(iii) max [sum_blocks top-M(L) |v|] / (12 d M(L)) = {worst_iii:.4f}  (<=1 required)")
