"""R216 from-scratch checks over F_{h^2} = F_h[i] (h ≡ 3 mod 4 prime), m | h+1:
 (1) pure Gauss sum of a character chi of exact order m:  g(chi) = (-1)^{(h+1)/m} h   (BEW Thm 11.6.3, t = gamma = 1)
 (2) cyclotomic numbers (a,b)_m = #{x in C_a : x + 1 in C_b}; residues of m^2 (a,b) mod h (author: {1, 1-m, 1-3m})
     and the PATTERN: which (a,b) get which residue.
 (3) prod_{zeta in mu_c, zeta != 1} (1 - zeta) = c in F_{h^2}.
 (4) scaling collapse: #{x in C_a : x + u in C_b} independent of u in F_h^*.
Complex arithmetic only for Gauss sums (additive character psi(x) = exp(2 pi i Tr(x)/h)).
"""
import cmath, sys
from sympy import primerange, divisors

def mul(x, y, h):  # (a + b i)(c + d i), i^2 = -1
    return ((x[0] * y[0] - x[1] * y[1]) % h, (x[0] * y[1] + x[1] * y[0]) % h)

def gen(h):
    q1 = h * h - 1
    fs = [f for f in divisors(q1) if f > 1 and all(f % e or e == f for e in [f])]
    from sympy import primefactors
    pf = primefactors(q1)
    for a in range(h):
        for b in range(1, h):
            g = (a, b)
            if all(pw(g, q1 // r, h) != (1, 0) for r in pf):
                return g

def pw(x, e, h):
    r = (1, 0)
    while e:
        if e & 1:
            r = mul(r, x, h)
        x = mul(x, x, h)
        e >>= 1
    return r

def main(H):
    bad = 0; resid_pattern = {}
    for h in primerange(7, H):
        if h % 4 != 3:
            continue
        q1 = h * h - 1
        g = gen(h)
        log = {}
        x = (1, 0)
        for k in range(q1):
            log[x] = k
            x = mul(x, g, h)
        for m in divisors(h + 1):
            if m < 3:
                continue
            # (1) Gauss sum, chi(g) = exp(2 pi i / m)
            S = 0
            for xx, k in log.items():
                tr = (2 * xx[0]) % h
                S += cmath.exp(2j * cmath.pi * k / m) * cmath.exp(2j * cmath.pi * tr / h)
            want = (-1) ** ((h + 1) // m) * h
            if abs(S - want) > 1e-6 * h:
                bad += 1; print("gauss fail", h, m, S)
            # (2) cyclotomic numbers
            cyc = [[0] * m for _ in range(m)]
            for xx, k in log.items():
                y = ((xx[0] + 1) % h, xx[1])
                if y in log:
                    cyc[k % m][log[y] % m] += 1
            for a in range(m):
                for b in range(m):
                    r = (m * m * cyc[a][b]) % h
                    typ = "00" if a == b == 0 else ("0i/i0/ii" if (a == 0 or b == 0 or a == b) else "other")
                    rr = [rv for rv in (1, 1 - m, 1 - 3 * m) if (rv - r) % h == 0]
                    resid_pattern.setdefault((typ, tuple(rr)), 0)
                    resid_pattern[(typ, tuple(rr))] += 1
                    if not rr:
                        bad += 1; print("cyc residue fail", h, m, a, b)
            # (4) scaling collapse for u in F_h^*
            for u in range(2, h):
                cu = [[0] * m for _ in range(m)]
                for xx, k in log.items():
                    y = ((xx[0] + u) % h, xx[1])
                    if y in log:
                        cu[k % m][log[y] % m] += 1
                if cu != cyc:
                    bad += 1; print("scaling fail", h, m, u); break
            # (3)
            for c in divisors(h + 1):
                if c < 2: continue
                z = pw(g, q1 // c, h)
                P = (1, 0); zz = z
                for _ in range(c - 1):
                    P = mul(P, ((1 - zz[0]) % h, (-zz[1]) % h), h)
                    zz = mul(zz, z, h)
                if P != (c % h, 0):
                    bad += 1; print("prod fail", h, c)
    print("failures:", bad)
    for k, v in sorted(resid_pattern.items()):
        print(k, v)

if __name__ == "__main__":
    main(int(sys.argv[1]))
