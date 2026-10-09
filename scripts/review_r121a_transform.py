"""R121A: shape/uniformity check of the transform ledger (ttl3_lemma81_effective.md §2.2 (a),(d),(e)).
Uses a generic smooth bump Psi on [11/12,17/12] (uniformity in Y and the r/t/sigma-shape is what is tested;
B = 2^2048 is far above any value seen)."""
import mpmath as mp
mp.mp.dps = 40
a, b = mp.mpf(11) / 12, mp.mpf(17) / 12
c0, hw = (a + b) / 2, (b - a) / 2
def Psi(u):
    z = (u - c0) / hw
    return mp.e ** (-1 / (1 - z * z)) if abs(z) < 1 else mp.mpf(0)
def phihat_t(r, t, Y):  # pi i/(2 sinh pi r) int [J_{2ir}-J_{-2ir}](x) x^{it} Psi(Yx) dx/x , x=u/Y
    k = lambda u: mp.besselj(2j * r, u / Y) - mp.besselj(-2j * r, u / Y)
    I = mp.quad(lambda u: k(u) * (u / Y) ** (1j * t) * Psi(u) / u, [a, c0, b])
    return mp.pi * 1j / (2 * mp.sinh(mp.pi * r)) * I
def phihat_exc(s, t, Y):  # kernel pi/(2 sin pi s)[J_{-2s}-J_{2s}]
    k = lambda u: mp.besselj(-2 * s, u / Y) - mp.besselj(2 * s, u / Y)
    I = mp.quad(lambda u: k(u) * (u / Y) ** (1j * t) * Psi(u) / u, [a, c0, b])
    return mp.pi / (2 * mp.sin(mp.pi * s)) * I
print("(a) normalised |phihat_t(r)| (1+r)^4 / ((1+|t|)^4 L_Y):")
for Y in [mp.mpf(2) ** 32, mp.mpf(2) ** 64, mp.mpf(2) ** 128]:
    LY = 1 + mp.log(Y)
    row = []
    for r in [mp.mpf('1e-8'), mp.mpf('0.5'), 2, 8]:
        for t in [0, 3]:
            v = abs(phihat_t(mp.mpf(r), t, Y)) * (1 + r) ** 4 / ((1 + abs(t)) ** 4 * LY)
            row.append(mp.nstr(v, 3))
    print("  log2 Y=%d:" % int(mp.log(Y, 2)), row)
print("(d) |phihat_t(-i s)| / (Y^{2s} L_Y), s small:")
for Y in [mp.mpf(2) ** 32, mp.mpf(2) ** 128]:
    LY = 1 + mp.log(Y)
    print("  log2 Y=%d:" % int(mp.log(Y, 2)),
          [mp.nstr(abs(phihat_exc(mp.mpf(s), t, Y)) / (Y ** (2 * s) * LY), 3) for s in [mp.mpf('1e-9'), mp.mpf('1e-4'), mp.mpf('0.01')] for t in [0, 5]])
print("(e) |phihat_t(-i s) - main| * s, e<s<=1/4 (should be bounded uniformly):")
for Y in [mp.mpf(2) ** 32, mp.mpf(2) ** 128]:
    out = []
    for s in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.25')]:
        for t in [0, 5]:
            phistar = mp.quad(lambda u: Psi(u) * (u / Y) ** (-2 * s + 1j * t) / u, [a, c0, b])
            main = mp.pi * 4 ** s / (2 * mp.sin(mp.pi * s) * mp.gamma(1 - 2 * s)) * phistar
            out.append(mp.nstr(abs(phihat_exc(s, t, Y) - main) * s, 3))
    print("  log2 Y=%d:" % int(mp.log(Y, 2)), out)
