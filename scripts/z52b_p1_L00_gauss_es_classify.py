"""z52b pass1 L00 Z2822 follow-up: classify the Z[i] box hits of gauss_es search (R given) by degeneracy.
Counts ordered hits (xi,eta) with zeta in Z[i]; flags: xi==eta, zeta in {xi,eta}, pi | zeta, pi | xi or pi | eta.
Usage: python3 scripts/z52b_p1_L00_gauss_es_classify.py R"""
import sys, json
from fractions import Fraction
R = int(sys.argv[1]) if len(sys.argv) > 1 else 16
d = json.load(open("data/z52b/pass1/L00/gauss_es_R%d.json" % R))
def mul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def div_int(a, b):
    """a/b in Z[i] ? return quotient or None (b != 0)."""
    n = b[0]*b[0]+b[1]*b[1]
    c = mul(a, (b[0], -b[1]))
    if c[0] % n or c[1] % n: return None
    return (c[0]//n, c[1]//n)
pts = [(a, b) for a in range(-R, R+1) for b in range(-R, R+1) if (a, b) != (0, 0) and a*a+b*b <= R*R]
stats = {"hits": 0, "xi_eq_eta": 0, "zeta_in_xi_eta": 0, "pi_divides_zeta": 0, "pi_divides_xi_or_eta": 0, "any_degenerate": 0}
per_pi = []
for rec in d["gaussian"]:
    pi = tuple(rec["pi"]); h = 0; deg = 0
    for xi in pts:
        for eta in pts:
            P = mul(xi, eta)
            S = (xi[0]+eta[0], xi[1]+eta[1])
            pS = mul(pi, S)
            D = (4*P[0]-pS[0], 4*P[1]-pS[1])
            if D == (0, 0): continue
            num = mul(pi, P)
            z = div_int(num, D)
            if z is None or z == (0, 0): continue
            h += 1
            flags = [xi == eta, z in (xi, eta), div_int(z, pi) is not None,
                     div_int(xi, pi) is not None or div_int(eta, pi) is not None]
            stats["xi_eq_eta"] += flags[0]; stats["zeta_in_xi_eta"] += flags[1]
            stats["pi_divides_zeta"] += flags[2]; stats["pi_divides_xi_or_eta"] += flags[3]
            if any(flags): deg += 1
    stats["hits"] += h; stats["any_degenerate"] += deg
    per_pi.append({"pi": pi, "hits": h, "degenerate": deg})
out = {"R": R, "totals": stats, "per_pi_sample": per_pi[:10]}
json.dump(out, open("data/z52b/pass1/L00/gauss_es_classify_R%d.json" % R, "w"), indent=1)
print(json.dumps(stats))
