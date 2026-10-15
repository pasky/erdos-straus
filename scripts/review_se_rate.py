"""R222: from-scratch continuum check of STERILE_EXPLICIT §0 (I3) / Prop 2.1 (grid EVIDENCE claim):
theta*(eta) = max over normalised P-boxes (alpha, gamma, delta, eps), alpha+gamma+delta+eps = 1, 2 alpha + delta <= 1,
of min over routes of the route exponent, with Cor 1.4 class-divisor counts (no tau except the tau_3 route, loss eta).
Claimed: theta* = 0.400 for eta <= 0.3; 0.417 (0.35), 0.450 (0.4), 0.500 (0.5); binding at ET's point (1/5,1/5,1/5,2/5).
Route exponents re-derived by the reviewer from Table 2 (sizes: b = N^beta, beta = 1-alpha-delta = gamma+eps; f = N^{1-eps}).
Usage: uv run python scripts/review_se_rate.py [grid]"""
import sys, itertools

def cls(nsz, ssz, dsz):
    """log_N of #divisors of size N^dsz of an integer of size N^nsz in a unit class mod N^ssz (Cor 1.4 + trivial)."""
    if nsz <= 0: return 0.0
    triv = max(0.0, dsz - ssz)
    b, r = dsz / nsz, ssz / nsz
    interp = nsz * max(0.0, b * (1 - b) - r) if 0 < b < 1 else 0.0
    return min(triv, interp)

def routes(al, ga, de, ep, eta):
    be = 1 - al - de; ph = 1 - ep
    R = {}
    R['H'] = al + ga + de
    R['A'] = max(ep, al + de)
    R['C'] = al + de + cls(1.0, al + de, ph)
    R['D'] = ga + de + cls(1 + 2 * ga + de, ga + de, ph)
    R['E'] = al + ga + cls(1 + ga, al + ga, ph)
    R['F'] = max(ep, al) + min(cls(1 - al, ep, be), cls(1 - al, ep, de))
    R['G'] = max(ep, de) + min(cls(1 - de, ep, al), cls(1 - de, ep, be))
    R['tau3'] = ep + eta
    R['I'] = ga + max(ep, al)
    R['J'] = ga + max(ep, de)
    return R

def theta(eta, n):
    best = (-1, None)
    for i, j, k in itertools.product(range(n + 1), repeat=3):
        al, ga, de = i / n, j / n, k / n
        ep = 1 - al - ga - de
        if ep < -1e-12 or 2 * al + de > 1 + 1e-12: continue
        R = routes(al, ga, de, max(ep, 0.0), eta)
        v = min(R.values())
        if v > best[0]: best = (v, (al, ga, de, ep), min(R, key=R.get))
    return best

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    for eta in (0.0, 0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5):
        v, pt, k = theta(eta, n)
        print(f"eta={eta:.2f}: theta* = {v:.4f} at (a,c,d,e) = {tuple(round(x, 3) for x in pt)} binding {k}")
    R = routes(.2, .2, .2, .4, 0.3); print("ET point (1/5,1/5,1/5,2/5):", {k: round(v, 4) for k, v in R.items()})
    # drop-one-route robustness
    for drop in ['A', 'C', 'D', 'E', 'F', 'G', 'tau3', 'I']:
        old = routes
        def routes(al, ga, de, ep, eta, _o=old, _d=drop):
            R = _o(al, ga, de, ep, eta); R.pop(_d); return R
        v, pt, k = theta(0.3, n // 2)
        print(f"  without {drop}: theta*(0.3) = {v:.4f} at {tuple(round(x, 3) for x in pt)}")
        routes = old
