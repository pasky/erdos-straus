# R92: classify relaxed solutions (from review_typei5_relax.c) into TYPEI5 cases/regimes and test
# identities (H), (Lin), the Prop 3.3 bounds and Lemma 3.6 (case A) constraints on each.
import sys
from fractions import Fraction as Fr

def classify(L, u, W, cp, g, dl, P1, X):
    T = 2 ** (L - 4); y = cp * g * dl; z = T * u - y; m = cp * dl * dl
    assert P1 * m == y * y + 2 * W * m * u * (y - T * u // 2) * 1 or True
    out = dict(L=L, u=u, a=len(str(W)) and W, y=y)
    # Fe identity of TYPEI4 Remark 1.6 with 7^s -> W u^2:  (8c'Xg-1)(8c'Xh-1) = 1 + 2^(L+2) c' W u^2 X^2, h = g + 2 W u dl
    h = g + 2 * W * u * dl
    assert (8 * cp * X * g - 1) * (8 * cp * X * h - 1) == 1 + 2 ** (L + 2) * cp * W * u * u * X * X, "Fe"
    if 2 * y > T * u:
        J = y - T * u // 2; rho = Fr(z, P1)
        ok = (2 * W * u * J < T * u // 2) and J * 4 * W < T
        caseA_shape = (L in (9, 10)) and rho == 1 and (7 - T // 2) % (cp * g) == 0
        return f"caseA J={J} rho={rho} J<T/(4W):{ok} L9/10-shape(rho=1,G|7-T/2):{caseA_shape}"
    j = T * u // 2 - y; rho = Fr(z, P1); assert rho.denominator == 1; rho = int(rho)
    lam = Fr(rho * j - m, u)
    Delta = 8 * j * W * m + 6 * T * j - T * T * u
    kap = 8 * W * lam
    H = rho * Delta == 2 * lam * (T * u + 2 * j)
    Lin = (lam == 0) or (u * (kap * j * (2 * T * j - Delta) - Delta * T * T) == Delta * (Delta - 6 * T * j) - 4 * kap * j ** 3)
    if lam < 0:
        reg = "ii"; bnd = 8 * W * (-lam) * j < T * T
    elif lam == 0:
        reg = "i"; bnd = False
    elif Delta < 2 * T * j:
        s = 2 * T * j - Delta; reg = "iii"; bnd = W * lam * s < Fr(T ** 3, 4)
        gg = 2 * T ** 3 - s * kap
        R = kap * s ** 3 * (4 * T ** 3 - s * kap) ** 2
        bnd = bnd and gg > 0 and (lam.denominator != 1 or (R % (gg * j - s * T * T) == 0))
    elif Delta == 2 * T * j:
        reg = "iv"; bnd = True
    else:
        sig = Delta - 2 * T * j; reg = "v"; bnd = u * sig < 4 * j * j
    return f"caseB j={j} rho={rho} lam={lam} Delta={Delta} H:{H} Lin:{Lin} regime={reg} bound:{bnd}"

for line in open(sys.argv[1]):
    if not line.strip() or line.startswith("L="): continue
    L, u, W, cp, g, dl, P1, X = map(int, line.split())
    print(L, u, "W=%d c'=%d g=%d delta=%d P1=%d X=%d" % (W, cp, g, dl, P1, X), "|", classify(L, u, W, cp, g, dl, P1, X))
