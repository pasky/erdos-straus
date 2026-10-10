"""R123: independent numerical check of Props 3.1/3.2 (areas, widths, point-in-wedge <=> Type I).
Areas: brute 2D midpoint quadrature of the indicator in (x, t = log y), measure dx dy / y^2 = e^{-t} dx dt.
Widths: numeric minimisation of the hyperbolic distance d(z,w) = arccosh(1 + |z-w|^2/(2 Im z Im w))
from points on one edge to the other edge.
"""
import numpy as np
from math import log, sqrt, acosh, gcd


def area_indicator(ind, xlo, xhi, ylo, yhi, nx=4000, nt=4000):
    t = np.linspace(log(ylo), log(yhi), nt + 1); t = (t[1:] + t[:-1]) / 2; dt = (log(yhi) - log(ylo)) / nt
    tot = 0.0
    for tt in t:
        y = np.exp(tt)
        # x-window adapted per row is NOT used (to stay independent): fixed global box
        x = np.linspace(xlo, xhi, nx + 1); x = (x[1:] + x[:-1]) / 2; dx = (xhi - xlo) / nx
        tot += ind(x, y).sum() * dx * np.exp(-tt) * dt
    return tot


def hdist(z, w):
    return acosh(1 + abs(z - w) ** 2 / (2 * z.imag * w.imag))


rng = np.random.default_rng(1)
print("Prop 3.1 (A): area of R_c, y in [sqrt(d)/2p, sqrt(d)]  vs  log(2p)/(c sqrt d)")
for (p, c, d) in [(101, 1, 1), (101, 2, 3), (1009, 3, 2), (257, 5, 7)]:
    sd = sqrt(d)
    ind = lambda x, y: np.abs(2 * c * sd * x - sd - p * y) < y
    # box: x in [1/2c, 1/2c + (p+1) sqrt(d)/(2 c sqrt d)] generous
    xlo, xhi = 1 / (2 * c) - 0.01, 1 / (2 * c) + (p + 1) * sd / (2 * c * sd) * 1.0 + 0.01
    # split the y-range into dyadic slabs with tight x boxes to keep resolution (box still independent of formula)
    tot = 0.0
    ys = np.geomspace(sd / (2 * p), sd, 25)
    for y1, y2 in zip(ys[:-1], ys[1:]):
        bx = (p + 2) * y2 / (2 * c * sd)
        tot += area_indicator(ind, 1 / (2 * c) - 1e-9, 1 / (2 * c) + bx, y1, y2, nx=3000, nt=200)
    print(f"  p={p} c={c} d={d}: numeric {tot:.6f}  formula {log(2*p)/(c*sd):.6f}")

print("Prop 3.2 (B): area of R'_a, y' in [sqrt(d)/2, p sqrt(d)]  vs  log(2p)/(a sqrt d p)")
for (p, a, d) in [(101, 1, 1), (101, 2, 3), (1009, 1, 2), (257, 3, 5)]:
    sd = sqrt(d)
    ind = lambda x, y: np.abs(2 * a * sd * x + sd + y) < y / p
    tot = 0.0
    ys = np.geomspace(sd / 2, p * sd, 25)
    for y1, y2 in zip(ys[:-1], ys[1:]):
        cx = -(sd + y2) / (2 * a * sd); bx = (sd + y2) / (2 * a * sd) * 0.0 + (y2 - y1 + 2 * y2 / p) / (2 * a * sd)
        lo = -(sd + y2 * (1 + 1 / p)) / (2 * a * sd) - 1e-9
        hi = -(sd + y1 * (1 - 1 / p)) / (2 * a * sd) + 1e-9
        tot += area_indicator(ind, lo, hi, y1, y2, nx=6000, nt=200)
    print(f"  p={p} a={a} d={d}: numeric {tot:.6f}  formula {log(2*p)/(a*sd*p):.6f}")

print("Widths: min hyperbolic distance from a point on the inner edge to the outer edge, times p")
from scipy.optimize import minimize_scalar


def edge_dist(z, slope_dx_dy):          # outer edge: x = slope * s, y = s (through the origin)
    g = lambda u: hdist(z, complex(slope_dx_dy * np.exp(u), np.exp(u)))
    r = minimize_scalar(g, bracket=(-1, 0, 1), tol=1e-14)
    return r.fun


for (p, K) in [(1009, 2.0), (1009, 20.0), (1009, 200.0), (1009, 2000.0), (100003, 2.0)]:
    z = complex((p - 1) / K, 1.0)                     # A: edges x - x0 = (p -+ 1) y / K, K = 2c sqrt d
    w = edge_dist(z, (p + 1) / K)
    print(f"  A: p={p} K={K}: width*p = {w*p:.5f}   arcsinh-difference*p = {(np.arcsinh((p+1)/K)-np.arcsinh((p-1)/K))*p:.5f}")
for (p, K) in [(1009, 2.0), (1009, 20.0), (1009, 200.0)]:
    z = complex(-(1 - 1 / p) / K, 1.0)                # B: edges x + x0 = -(1 -+ 1/p) y / K, K = 2a sqrt d
    w = edge_dist(z, -(1 + 1 / p) / K)
    print(f"  B: p={p} K={K}: width*p = {w*p:.5f}  (2/sqrt(1+K^2) = {2/np.sqrt(1+K*K):.5f})")

print("Point-in-wedge <=> quadruple (Formulation A), floating test vs integer test, p <= 400")
bad = 0; hits = 0
for p in [q for q in range(5, 401) if all(q % r for r in range(2, int(q ** .5) + 1))]:
    for d in range(1, 60):
        sd = sqrt(d)
        for a in range(1, 60):
            F = 4 * a * a * d + 1
            for f in range(1, 2 * p + 1):
                if F % f:
                    continue
                z = complex(2 * a * d / f, sd / f)
                for c in range(1, 60):
                    inreg = abs(2 * c * sd * z.real - sd - p * z.imag) < z.imag * (1 - 1e-9)
                    isq = (4 * a * c * d - f == p)
                    bad += inreg != isq; hits += isq
print("  mismatches", bad, "hits", hits)
