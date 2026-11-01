"""Z0292: elliptic (cone-point) terms of the Selberg trace formula for triangle orbifolds S^2(x,y,z) and the heat invariants.
(1) per-cone-point constant heat coefficient (m^2-1)/(12m): checked on the round football S^2/Z_m (exact spectrum:
    Z_m-invariant spherical harmonics), a_1 = chi_orb/6 + 2(m^2-1)/(12m), chi_orb = 2/m;
(2) the same constant from the hyperbolic elliptic orbital integral (Iwaniec, Spectral Methods Thm 10.2 normalisation):
    sum_{k=1}^{m-1} (1/(2m sin th_k)) * int h(r) cosh((pi-2 th_k) r)/cosh(pi r) dr, th_k = pi k/m, as t -> 0 for
    h(r) = exp(-t(1/4+r^2)) -> the r-integral -> 1/sin th_k, i.e. sum 1/(2m sin^2 th_k) = (m^2-1)/(6m); compared with (1);
(3) ES side: for n <= N, all ES triples x<=y<=z (4/n = 1/x+1/y+1/z, hyperbolic for n >= 5) have the same a_0 = Area/4pi;
    check whether a_1 = chi/6 + sum (x_i^2-1)/(12 x_i) separates the triples of the same n (collisions listed).
Usage: python z52d_p2_ZF1_Z0292_heat.py N out.json
"""
import sys, json, math
from fractions import Fraction as Fr
import numpy as np


def football_a1(m, ts=(1e-3, 5e-4, 2.5e-4)):
    # heat trace of S^2/Z_m (rotation about an axis): multiplicity of l = #{|j|<=l : m | j}
    vals = []
    for t in ts:
        L = int(math.sqrt(40 / t)) + 10
        l = np.arange(L)
        mult = 2 * (l // m) + 1
        Th = (mult * np.exp(-l * (l + 1) * t)).sum()
        vals.append(Th - 1 / (m * t))     # area 4pi/m -> leading term 1/(m t)
    # Richardson in t (expansion a_1 + a_2 t + ...)
    a = np.polyfit(ts, vals, 2)
    return a[-1]


def elliptic_const(m):
    return sum(1 / (2 * m * math.sin(math.pi * k / m) ** 2) for k in range(1, m))


def elliptic_integral_check(m, t=1e-3):
    # numerical r-integral for small t vs its limit 1/sin(theta)
    out = []
    r = np.linspace(-200, 200, 400001)
    for k in range(1, m):
        th = math.pi * k / m
        f = np.exp(-t * (0.25 + r * r)) * np.cosh((math.pi - 2 * th) * r) / np.cosh(math.pi * r)
        out.append((np.trapezoid(f, r), 1 / math.sin(th)))
    return out


def es_triples(n):
    res = []
    q = Fr(4, n)
    for x in range(n // 4 + 1, 3 * n // 4 + 2):
        r1 = q - Fr(1, x)
        if r1 <= 0:
            continue
        ylo = max(x, math.floor(1 / r1) + 1)
        for y in range(ylo, math.floor(2 / r1) + 1):
            r2 = r1 - Fr(1, y)
            if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                res.append((x, y, r2.denominator))
    return res


def a1(tr):
    chi = -1 + sum(Fr(1, m) for m in tr)
    return chi / 6 + sum(Fr(m * m - 1, 12 * m) for m in tr)


def main():
    N = int(sys.argv[1]); out = {}
    out['football'] = {m: dict(numeric=float(football_a1(m)), predicted=float(Fr(1, 3 * m) + Fr(m * m - 1, 6 * m)))
                       for m in (1, 2, 3, 5)}
    out['elliptic_sum_vs_cone_constant'] = {m: dict(iwaniec_sum=elliptic_const(m), two_x_cone=(m * m - 1) / (6 * m))
                                           for m in (2, 3, 4, 7, 20)}
    out['elliptic_integral_small_t'] = {m: elliptic_integral_check(m) for m in (3, 7)}
    coll = []; ntrip = 0; nmulti = 0; zero = []
    for n in range(5, N + 1):
        T = es_triples(n)
        if not T:
            zero.append(n)
        ntrip += len(T)
        if len(T) > 1:
            nmulti += 1
        seen = {}
        for tr in T:
            k = a1(tr)
            if k in seen:
                coll.append((n, seen[k], tr))
            seen[k] = tr
    def isp(k):
        return k > 1 and all(k % d for d in range(2, math.isqrt(k) + 1))
    prime_coll = [c for c in coll if isp(c[0])]
    out['es_prime_collisions'] = dict(count=len(prime_coll), first=prime_coll[:10])
    out['es'] = dict(N=N, n_without_triple=zero, total_triples=ntrip, n_with_several=nmulti,
                     a1_collisions=coll[:30], n_collisions=len(coll))
    print(json.dumps(out, indent=1, default=str))
    json.dump(out, open(sys.argv[2], 'w'), indent=1, default=str)


if __name__ == '__main__':
    main()
