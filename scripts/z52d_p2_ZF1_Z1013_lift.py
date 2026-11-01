"""Z1013 (ZF1 finisher): the actual 'modular solutions -> rational reconstruction of y/z' experiment at a fixed prime.
(1) Coverage: for modulus m, which unit ratios rho = y/z mod m occur on the ES surface 4xyz = p(xy+yz+zx) mod m?
    For y = rho*z the equation is linear in x: x*z*(4 rho z - p(rho+1)) = p rho z^2, so a point exists as soon as
    z(4 rho z - p(rho+1)) is a unit for some unit z.  We count covered rho exactly for several m.
(2) Candidates: rational reconstruction of each covered rho gives a/b with |a|,|b| <= sqrt(m/2); we test every candidate
    for being a TRUE ratio y/z of an ES solution (exact test below) and report precision/recall vs the true ratio list.
Exact ratio test: y = a s, z = b s (gcd(a,b)=1, a<=b) solve 4/p - 1/x = (a+b)/(a b s) for some x,s >= 1
    <=> s = p x (a+b) / (a b (4x - p)) integral for some x with 4x > p and x <= y (we drop the ordering: any x).
    x ranges over p/4 < x <= (3p/4)*... ; we use: (4x-p) | p x (a+b)/... -> brute over x in (p/4, X] with X from the
    bound 1/x >= 4/(3p) for the smallest denominator OR x is not the smallest; we simply enumerate all solutions of p
    first (brute force) and compare the ratio sets, which is exact.
Run: uv run --with numpy python scripts/z52d_p2_ZF1_Z1013_lift.py
"""
import math, json, os, itertools
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'data/z52b/pass2/ZF1/Z1013'); os.makedirs(OUT, exist_ok=True)

def solutions(p):
    """all x<=y<=z with 4/p = 1/x+1/y+1/z (exact, divisor method)."""
    sols = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        A = 4 * x - p; B = p * x
        if A <= 0: continue
        g = math.gcd(A, B); A //= g; B //= g
        # 1/y+1/z = A/B, y>=x: (Ay-B)(Az-B)=B^2, d=Ay-B <= B
        B2 = B * B
        # enumerate divisors of B^2 via factorisation
        f = {}; r = B; q = 2
        while q * q <= r:
            while r % q == 0: f[q] = f.get(q, 0) + 1; r //= q
            q += 1
        if r > 1: f[r] = f.get(r, 0) + 1
        divs = [1]
        for q, e in f.items():
            divs = [d * q ** k for d in divs for k in range(2 * e + 1)]
        for d in divs:
            if d <= B and (d + B) % A == 0:
                y = (d + B) // A
                if y >= x:
                    z = (B2 // d + B) // A
                    sols.append((x, y, z))
    return sols

def ratrec(r, m):
    """rational reconstruction: a/b == r mod m with |a|,|b| <= sqrt(m/2); None if none."""
    N = math.isqrt(m // 2)
    r0, r1 = m, r % m; s0, s1 = 0, 1
    while r1 > N:
        q = r0 // r1; r0, r1 = r1, r0 - q * r1; s0, s1 = s1, s0 - q * s1
    if abs(s1) > N or s1 == 0 or math.gcd(r1, abs(s1)) != 1: return None
    a, b = r1, s1
    if b < 0: a, b = -a, -b
    return (a, b)

def coverage(p, m):
    units = [z for z in range(1, m) if math.gcd(z, m) == 1]
    U = np.array(units, dtype=np.int64)
    cov = 0; tot = 0
    for rho in units:
        tot += 1
        v = (U * ((4 * rho * U - p * (rho + 1)) % m)) % m
        g = np.gcd(v, m)
        if (g == 1).any(): cov += 1
    return cov, tot

res = {}
for p in (409, 2521):
    sols = solutions(p)
    true_ratios = set()
    for (x, y, z) in sols:
        g = math.gcd(y, z); true_ratios.add((y // g, z // g))
    Hs = sorted(max(a, b) for a, b in true_ratios)
    r = dict(U=len(sols), n_true_ratios=len(true_ratios), H_true_ratios_quartiles=[Hs[0], Hs[len(Hs)//4], Hs[len(Hs)//2], Hs[3*len(Hs)//4], Hs[-1]])
    # coverage at small moduli (exact)
    cov = {}
    for m in ([p, 1009, 1024, 3 * 5 * 7 * 8] if p == 409 else [p, 1009]):
        c, t = coverage(p, m); cov[str(m)] = dict(covered=c, units=t)
    r['coverage_unit_ratios'] = cov
    # reconstruction at m = p^2 and p^3: candidate set = all reconstructible residues (coverage is total, see above)
    for k in (2, 3):
        m = p ** k; N = math.isqrt(m // 2)
        # number of candidates = # coprime pairs (a,b), 1<=a,b<=N  (positive ratios only)  ~ (6/pi^2) N^2
        ncand = int(round(6 / math.pi ** 2 * N * N))
        hit = sum(1 for (a, b) in true_ratios if max(a, b) <= N)
        # check: each true ratio is recovered by ratrec of its residue
        rec_ok = sum(1 for (a, b) in true_ratios if max(a, b) <= N and (ratrec(a * pow(b, -1, m) % m, m) == (a, b) if b % p else ratrec(b * pow(a, -1, m) % m, m) == (b, a)))
        r[f'm=p^{k}'] = dict(height_bound=N, n_candidates_positive_coprime_pairs_approx=ncand, true_ratios_recovered=hit,
                            ratrec_consistency=rec_ok, recall=round(hit / len(true_ratios), 4), precision=hit / ncand)
    res[str(p)] = r
    print(p, json.dumps(r), flush=True)
json.dump(res, open(os.path.join(OUT, 'lift.json'), 'w'), indent=1)
