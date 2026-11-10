# z70 LOOSE I6: one high-precision (mpmath, 34 digits) check of Theorem F for the d = 1 fibre (M, alpha, beta) = (4, 3, 3).
import mpmath as mp, sys
# usage: z70_loose_i6mp.py [M al be dps small z0re z0im]   (default: the d = 1 point below, 34 digits)
args = sys.argv[1:]
M, al, be = (int(args[0]), int(args[1]), int(args[2])) if args else (4, 3, 3)
mp.mp.dps = int(args[3]) if len(args) > 3 else 34
SMALL = float(args[4]) if len(args) > 4 else 3e-3
a = mp.mpf(al) / M; b = mp.mpf(be) / M
def e(x): return mp.expj(2 * mp.pi * x)
def Ldirect(z):
    tot = 0; A = al
    while True:
        t = e(A * be * z) / (1 - e(A * M * z)); tot += t
        if abs(e(A * be * z)) < mp.mpf(10)**-(mp.mp.dps + 6): break
        A += M
    return tot
LI = {}
def Li(k, x):
    key = (k, x)
    if key not in LI: LI[key] = mp.polylog(-k, x)
    return LI[key]
def Lstar(w, u, v):
    if abs(w) < SMALL:
        eu, ev = e(u), e(v); s = 0; term_fac = 1
        for k in range(0, 61):
            s += (2j * mp.pi * w)**k / mp.factorial(k) * Li(k, eu) * Li(k, ev)
        return s
    tot = 0; m = 1
    while True:
        q = e(v + m * w); t = e(m * u) * q / (1 - q); tot += t
        if abs(q) < mp.mpf(10)**-(mp.mp.dps + 4): break
        m += 1
    return tot
def Ef(z):
    return (1j / (2 * mp.pi * M * M * z)) * (-mp.euler - mp.log(-2j * mp.pi * M * M * z) - mp.digamma(a) - mp.digamma(b)) + (mp.mpf(1)/2 - a) * (mp.mpf(1)/2 - b)
def Psi(z):
    w = -1 / (M * M * z); th = mp.arg(w) / 2; rot = mp.expj(-th)
    def f(s):
        t = s * rot; tw = t * w
        S1 = Lstar(tw, a, b) + Lstar(tw, -a, -b); S2 = Lstar(tw, a, -b) + Lstar(tw, -a, b)
        return (S1 * t / (t - 1) - S2 * t / (1 + t)) * rot
    smax = 90 / (2 * mp.pi * abs(w) * mp.sin(mp.arg(w) - th))
    pts = [0] + [smax * mp.mpf(2)**(-j) for j in range(30, -1, -1)]
    return (1j / (2 * mp.pi * M * M * z)) * mp.quad(f, pts)
z = (mp.mpc(args[5], args[6]) if len(args) > 6 else mp.mpc(0.05, 0.15)) * mp.mpf(16) / (10 * al * be)
lhs = Ldirect(z); w = -1 / (M * M * z)
rhs = Lstar(w, a, b) / (M * M * z) + Ef(z) + Psi(z)
print('z =', z); print('L(z)   =', lhs); print('law    =', rhs); print('|diff| =', mp.nstr(abs(lhs - rhs), 5), ' rel =', mp.nstr(abs(lhs - rhs) / abs(lhs), 5))
