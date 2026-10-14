"""O211 (a): semi-primitive cyclotomy over F_{h^2}, h = 3 mod 4 prime, m | h+1.
Checks: (1) Stickelberger pure Gauss sum g(chi_m) = (-1)^{(h+1)/m} h  (so for m = 4cd: sign (-1)^j);
(2) F_h^* lies in the class C_0 of every order m | h+1 (scaling collapse, Lemma 1.1);
(3) cyclotomic numbers (a,b)_m over F_{h^2}: m^2 (a,b) mod h depends only on (m, eta, a, b-type), not on h's
    other data -> the residue information is a rational function of the integer m (the box);
(4) c = prod_{zeta in mu_c, zeta != 1} (1 - zeta) in F_{h^2} (the additive bridge transports the integer c).
Usage: PYTHONPATH=scripts uv run python scripts/y3_gauss.py"""
import cmath, itertools

def field(h):  # F_{h^2} = F_h[i], elements (a,b) = a + b i
    def mul(x, y): return ((x[0]*y[0] - x[1]*y[1]) % h, (x[0]*y[1] + x[1]*y[0]) % h)
    els = [(a, b) for a in range(h) for b in range(h) if (a, b) != (0, 0)]
    q1 = h*h - 1
    fac = [r for r in range(2, q1+1) if q1 % r == 0 and all(r % s for s in range(2, int(r**.5)+1))]
    def pw(x, e):
        r = (1, 0)
        while e:
            if e & 1: r = mul(r, x)
            x = mul(x, x); e >>= 1
        return r
    g = next(x for x in els if all(pw(x, q1//r) != (1, 0) for r in fac))
    log = {}; x = (1, 0)
    for e in range(q1): log[x] = e; x = mul(x, g)
    return mul, pw, g, log

def run(h):
    mul, pw, g, log = field(h); q1 = h*h - 1; bad = 0
    for m in [m for m in range(3, h+2) if (h+1) % m == 0]:
        # (2) F_h^* in C_0
        if any(log[(a, 0)] % m for a in range(1, h)): bad += 1
        # (1) pure Gauss sum with psi(x) = e(Tr(x)/h), Tr(a+bi) = 2a
        G = sum(cmath.exp(2j*cmath.pi*e*1/m) * cmath.exp(2j*cmath.pi*(2*x[0])/h) for x, e in log.items())
        if abs(G - (-1)**((h+1)//m) * h) > 1e-6: bad += 1
        # (4) prod (1 - zeta)
        zs = [pw(g, (q1//m)*t) for t in range(1, m)]
        P = (1, 0)
        for z in zs: P = mul(P, ((1 - z[0]) % h, (-z[1]) % h))
        if P != (m % h, 0): bad += 1
    return bad

def cyclo(h, m):
    mul, pw, g, log = field(h)
    N = [[0]*m for _ in range(m)]
    for x, e in log.items():
        y = ((x[0]+1) % h, x[1])
        if y != (0, 0): N[e % m][log[y] % m] += 1
    return N

if __name__ == "__main__":
    tot = 0
    for h in [7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83]:
        b = run(h); tot += b
    print("checks (1),(2),(4) over h in {7..83}: failures =", tot)
    # (3): m^2 * cyclotomic numbers mod h, compared across h for the same m and parity eta
    for m in [4, 8, 12]:
        rows = []
        for h in [x for x in [7, 11, 23, 31, 47, 59, 71, 79, 83, 103, 107, 127] if (x+1) % m == 0]:
            N = cyclo(h, m); eta = (-1)**((h+1)//m)
            vals = sorted(set(N[a][b] for a in range(m) for b in range(m)))
            rows.append((h, eta, vals, sorted(set((m*m*v) % h for v in vals))))
        for r in rows: print("m=%d h=%d eta=%+d distinct (a,b)=%s  m^2(a,b) mod h=%s" % (m, *r))

def mixed_check(h, ochi, opsi):
    """g(lambda), lambda = (chi o N) * psi, chi of order ochi on F_h^*, psi of order opsi | h+1 on F_{h^2}^*,
    vs 1/2 g_{F_h}(chi^2) sum_{eps} chi(N gamma)^eps sum_{u in T} psi(u gamma^eps) conj(chi^2)(Tr(u gamma^eps))."""
    mul, pw, g, log = field(h); q1 = h*h - 1
    E = lambda t: cmath.exp(2j*cmath.pi*t)
    gh = next(a for a in range(2, h) if all(pow(a, (h-1)//r, h) != 1 for r in range(2, h) if (h-1) % r == 0 and all(r % s for s in range(2, r))))
    lg = {pow(gh, e, h): e for e in range(h-1)}
    chi = lambda a: E(lg[a % h]/ochi) if a % h else 0
    N = lambda x: (x[0]*x[0] + x[1]*x[1]) % h
    lam = lambda x: chi(N(x)) * E(log[x]/opsi)
    G = sum(lam(x)*E(2*x[0]/h) for x in log)
    gF = sum(chi(a)**2 * E(a/h) for a in range(1, h))
    T = [x for x in log if N(x) == 1]
    gam = next(x for x in log if pow(N(x), (h-1)//2, h) == h-1)
    S = 0
    for eps in (0, 1):
        for u in T:
            v = mul(u, gam) if eps else u; tr = 2*v[0] % h
            S += chi(N(gam))**eps * E(log[v]/opsi) * (chi(tr)**2).conjugate() if tr else 0
    return abs(G - 0.5*gF*S)

if __name__ == "__main__":
    errs = [mixed_check(h, oc, op) for h, oc, op in [(11, 5, 4), (19, 9, 4), (23, 11, 8), (31, 5, 8), (43, 7, 4), (47, 23, 12)]]
    print("mixed Gauss sum decomposition, max error:", max(errs))
