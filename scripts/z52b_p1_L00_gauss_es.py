"""z52b pass1 L00 item Z2822: ES over Z[i]: search 4/pi = 1/xi + 1/eta + 1/zeta with xi, eta, zeta in Z[i], pi a Gaussian prime.
Box search: |xi|, |eta| <= R (ordered pairs), zeta = pi*xi*eta / (4*xi*eta - pi*(xi+eta)) must lie in Z[i].
Exact integer arithmetic (int64; components stay < 1e9 for R <= 60, norms <= 200).
Usage: python3 scripts/z52b_p1_L00_gauss_es.py R
Memory: pair arrays are processed in chunks over xi (bounded by ~ chunk*#pts complex pairs)."""
import sys, json
import numpy as np

R = int(sys.argv[1]) if len(sys.argv) > 1 else 25
CONE = len(sys.argv) > 2 and sys.argv[2] == "cone"   # Bradford-Ionascu cone: Re, Im of each denominator of equal sign
OUT = "data/z52b/pass1/L00/gauss_es_R%d%s.json" % (R, "_cone" if CONE else "")

def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def gaussian_primes_upto(normmax):
    """Gaussian primes up to associates (one per associate class), as (a,b) with norm a^2+b^2 <= normmax."""
    out = []
    for a in range(0, int(normmax ** 0.5) + 1):
        for b in range(1, int(normmax ** 0.5) + 1):
            n = a * a + b * b
            if n > normmax or n < 2: continue
            if a == 0 and b == 1: continue
            if (a == 1 and b == 1):
                out.append((a, b)); continue
            if is_prime(n) and n % 4 == 1:
                out.append((a, b))
            elif a == 0 and is_prime(b) and b % 4 == 3:
                out.append((a, b))  # rational inert prime q = b (norm q^2)
    return out

pts = [(a, b) for a in range(-R, R + 1) for b in range(-R, R + 1) if (a, b) != (0, 0) and a * a + b * b <= R * R]
if CONE:
    pts = [(a, b) for (a, b) in pts if a * b > 0]   # denominators in the open cone {Re*Im > 0}
P = np.array(pts, dtype=np.int64)
XR, XI = P[:, 0], P[:, 1]

def mul(ar, ai, br, bi):
    return ar * br - ai * bi, ar * bi + ai * br

results = []
for (pa, pb) in gaussian_primes_upto(200):
    # pi = pa + pb i  (also consider conjugate: separate run)
    for (qa, qb) in ([(pa, pb), (pa, -pb)] if pb != 0 and pa != 0 else [(pa, pb)]):
        hits = 0; example = None
        for k in range(len(pts)):
            xr, xi = XR[k], XI[k]
            # eta over all pts
            pr, pi_ = mul(np.full_like(XR, xr), np.full_like(XR, xi), XR, XI)       # P = xi*eta
            sr, si = xr + XR, xi + XI                                                  # S = xi+eta
            ps_r, ps_i = mul(np.full_like(XR, qa), np.full_like(XR, qb), sr, si)     # pi*S
            dr, di = 4 * pr - ps_r, 4 * pi_ - ps_i                                     # D = 4P - pi*S
            nr, ni = mul(np.full_like(XR, qa), np.full_like(XR, qb), pr, pi_)        # num = pi*P
            nn = dr * dr + di * di
            ok = nn != 0
            # zeta = num * conj(D) / |D|^2
            zr, zi = mul(nr, ni, dr, -di)
            safe = np.where(ok, nn, 1)
            integral = ok & (zr % safe == 0) & (zi % safe == 0)
            if CONE:
                zq = np.where(integral, zr // safe, 0), np.where(integral, zi // safe, 0)
                integral = integral & (zq[0] * zq[1] > 0)
            if integral.any():
                idx = np.nonzero(integral)[0]
                hits += len(idx)
                if example is None:
                    j = idx[0]
                    example = {"xi": [int(xr), int(xi)], "eta": [int(XR[j]), int(XI[j])],
                               "zeta": [int(zr[j] // nn[j]), int(zi[j] // nn[j])]}
        results.append({"pi": [qa, qb], "norm": qa * qa + qb * qb, "hits_ordered": int(hits), "example": example})
        print(results[-1], flush=True) if False else None

# Comparison over Z (same kind of box, signs allowed, no positivity): 4/p = 1/x + 1/y + 1/z with |x|,|y| <= R,
# z = p*x*y/(4xy - p(x+y)) in Z.  Rational primes p <= 200 (all, not up to associates).
from fractions import Fraction
zres = []
for p in [q for q in range(2, 201) if is_prime(q)]:
    hit = 0
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            if x == 0 or y == 0: continue
            if CONE and (x < 0 or y < 0): continue   # positive ES over Z: all denominators > 0
            D = 4 * x * y - p * (x + y)
            if D == 0: continue
            num = p * x * y
            if num % D == 0 and num // D != 0 and (not CONE or num // D > 0):
                hit += 1
    zres.append({"p": p, "hits_ordered": hit})
gz = sum(1 for r in zres if r["hits_ordered"] > 0)
gi = sum(1 for r in results if r["hits_ordered"] > 0)
summary = {"R": R, "gaussian_primes_tested": len(results), "gaussian_with_hit": gi,
           "Z_primes_tested": len(zres), "Z_with_hit": gz}
summary["cone"] = CONE
json.dump({"summary": summary, "gaussian": results, "Z": zres}, open(OUT, "w"), indent=1)
print("wrote", OUT, summary)
