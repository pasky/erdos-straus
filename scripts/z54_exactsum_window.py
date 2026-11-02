# z54 EXACTSUM: window reconciliation arithmetic (exact rationals).
# Constraints on (a0,a1,b,g) = (alpha0, alpha1, beta, gamma):
#   Thm U (Z53_GENUSLVAL): (C1) g < 1-a1, (C2) b > tau(1+a1)+4eps, (C3) a0 > tau^2(1+a1)+3eps, tau = (r+1)/(4r)+r*eps
#   Thm X (Z53_GENUSX) with (C4) replaced by (C4'): (C2*) b > 2a1+tau+4eps, (C4') (1/2-eps)(b-a1) >= a1+eps/2
#   Lemma E exponent condition (E): kappa + (lam-kappa)(1-b) < a0(1+kappa)   [worst box: U = p^a0, K = p^(1-b)]
# Prints, per exponent pair: the threshold a0 > kappa/(1+2kappa-lam) (at 1-b -> a0), whether 2kappa+lam<1,
# the best-possible reach exponent (1-2kappa-lam)/(4(1+kappa)) at a0 -> 1/4, and checks an explicit window.
from fractions import Fraction as Fr
def A(k, l): return (k / (2 * k + 2), (k + l + 1) / (2 * k + 2))
def B(k, l): return (l - Fr(1, 2), k + Fr(1, 2))
pairs = {}
k, l = B(Fr(0), Fr(1)); pairs['B(0,1)=(1/2,1/2)'] = (k, l)
for n in range(1, 7):
    k, l = A(k, l); pairs['A^%dB(0,1)' % n] = (k, l)
pairs['Huxley-Watt (9/56,37/56)'] = (Fr(9, 56), Fr(37, 56))
pairs['Huxley 2005 (32/205,269/410)'] = (Fr(32, 205), Fr(269, 410))
pairs['Bourgain (13/84,55/84)'] = (Fr(13, 84), Fr(55, 84))
pairs['EPC (0,1/2)'] = (Fr(0), Fr(1, 2))
print('pair  kappa  lambda  2k+l<1  a0-threshold k/(1+2k-l)  best reach (1-2k-l)/(4(1+k))  C-range bound (1-2k-l)/(4(l-k))')
for name, (k, l) in pairs.items():
    den = 1 + 2 * k - l
    thr = k / den if den > 0 else None
    reach = (1 - 2 * k - l) / (4 * (1 + k))
    crange = (1 - 2 * k - l) / (4 * (l - k)) if l > k else None
    print(f'{name:30s} {float(k):.5f} {float(l):.5f} {2*k+l<1!s:5s} {float(thr) if thr is not None else float("nan"):.5f} {float(reach):.5f} {float(crange) if crange is not None else float("nan"):.5f}')

def check(a0, a1, b, g, kap, lam, r=100, eps=Fr(1, 10**5)):
    tau = Fr(r + 1, 4 * r) + r * eps
    c = {'C1 g<1-a1': g < 1 - a1, 'C2 b>tau(1+a1)+4eps': b > tau * (1 + a1) + 4 * eps,
         'C3 a0>tau^2(1+a1)+3eps': a0 > tau ** 2 * (1 + a1) + 3 * eps, 'C2* b>2a1+tau+4eps': b > 2 * a1 + tau + 4 * eps,
         "C4' (1/2-eps)(b-a1)>=a1+eps/2": (Fr(1, 2) - eps) * (b - a1) >= a1 + eps / 2, 'b<g': b < g, 'a0<a1': a0 < a1,
         'E': kap + (lam - kap) * (1 - b) < a0 * (1 + kap)}
    margin = (a0 * (1 + kap) - kap - (lam - kap) * (1 - b)) / (1 + kap)
    return c, margin, tau
for name, (a0, a1, b, g) in {'W1 (A^3B)': (Fr(200, 1000), Fr(204, 1000), Fr(7925, 10000), Fr(7955, 10000))}.items():
    kap, lam = pairs['A^3B(0,1)']
    c, m, tau = check(a0, a1, b, g, kap, lam)
    print(name, (float(a0), float(a1), float(b), float(g)), 'tau_r =', float(tau))
    for kk, v in c.items(): print('   ', kk, v)
    print('    reach exponent log_p(U_min/E) =', float(m), '  C-range exponent 1-b-a0 =', float(1 - b - a0),
          '  window constant c = (8/pi^4)(g-b)(a1-a0) =', float(8 / 97.40909103400242 * (g - b) * (a1 - a0)))
