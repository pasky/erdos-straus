"""R278 from-scratch check of QUESTION_R Thm 1.5.

(a) numerically verify the theta transformation law theta(gz) = s(g) (cz+d)^{1/2} theta(z) on Gamma_1(4)
    (principal branch), and read off s(g) for general g (also c<0 or d<0) -> compare with Jacobi conventions;
(b) multiplicativity of sigma = (c/d) on random products of non-negative Gamma_1(4) matrices;
(c) the archimedean cocycle w on products leaving the cone; check sigma(g1 g2) = sigma sigma w with w from
    principal square roots, and count failures of naive multiplicativity;
(d) non-extension: [[5,2],[12,5]] word in T, U=L^4; T, U generate Gamma_1(4) (free) -- checked by reduction.
"""
import cmath, math, random, sys

def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def kron(c, d):
    """Kronecker (c/d) for d odd positive; (0/1)=1."""
    return jacobi(c, d)

def theta(z, M=None):
    y = z.imag
    if M is None: M = int(math.sqrt(12.0 / y)) + 3   # exp(-2 pi m^2 y) < e^-75
    s = 1 + 0j
    for m in range(1, M + 1):
        s += 2 * cmath.exp(2j * math.pi * m * m * z)
    return s

def mul(A, B):
    return (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])

def act(g, z):
    a, b, c, d = g
    return (a*z + b) / (c*z + d)

def mult_factor(g):
    a, b, c, d = g
    if c == 0:
        z = 0.3 + 0.7j
    else:
        z = complex(-d / c + 0.37 / abs(c), 1.0 / abs(c))
    v = theta(act(g, z)) / (theta(z) * cmath.sqrt(c*z + d))
    return v

T = (1, 1, 0, 1); Ti = (1, -1, 0, 1); U = (1, 0, 4, 1); Ui = (1, 0, -4, 1)

def rand_word(L, gens):
    g = (1, 0, 0, 1)
    for _ in range(L):
        g = mul(g, random.choice(gens))
    return g

def nonneg(g): return all(x >= 0 for x in g)

def main():
    random.seed(278)
    # (a) theta law on Gamma_1(4), general elements (c, d of any sign)
    bad = 0; tested = 0; table = {}
    for _ in range(400):
        g = rand_word(random.randint(1, 7), [T, Ti, U, Ui])
        a, b, c, d = g
        if abs(c) > 3000: continue
        v = mult_factor(g)
        s = round(v.real)
        if abs(v - s) > 1e-6 or s not in (1, -1):
            bad += 1; print("non +-1 factor", g, v); continue
        tested += 1
        key = (c > 0, c < 0, d > 0)
        # Shimura convention: (c/d) for d<0 := (c/|d|) * (-1 if c<0 else 1)
        if c == 0:
            pred = 1 if d > 0 else None
        else:
            j = jacobi(c, abs(d))
            pred = j if d > 0 else (j if c > 0 else -j)
        if pred is not None and pred != s:
            table.setdefault(key, [0, 0])[0] += 1
        table.setdefault(key, [0, 0])[1] += 1
    print("(a) theta law tested", tested, "non+-1:", bad, "mismatch vs Shimura conv by (c>0,c<0,d>0):", table)
    # (b) non-negative products
    pos = []
    while len(pos) < 3000:
        g = rand_word(random.randint(1, 12), [T, Ti, U, Ui])
        if nonneg(g): pos.append(g)
    # also enlarge: products of non-negative elements
    fail_mult = fail_ab = 0; N = 0
    for _ in range(20000):
        g1, g2 = random.choice(pos), random.choice(pos)
        g3 = mul(g1, g2)
        N += 1
        s1, s2, s3 = (kron(g[2], g[3]) for g in (g1, g2, g3))
        if s3 != s1 * s2: fail_mult += 1
        a, b, c, d = g3
        if b > 0 and b % 2 == 1 and jacobi(a, b) != s3: fail_ab += 1
    print("(b) non-neg products", N, "mult failures", fail_mult, "(a/b)!=(c/d) failures (b odd)", fail_ab,
          "#pos with sigma=-1:", sum(kron(g[2], g[3]) == -1 for g in pos))
    # (c) products leaving the cone: g1,g2 with d>0 and c>=0 but negative b's allowed; compute w
    stats = {"w=1,mult ok": 0, "w=-1,mult fails": 0, "inconsistent": 0}
    cnt = 0
    while cnt < 5000:
        g1 = rand_word(random.randint(1, 6), [T, Ti, U, Ui]); g2 = rand_word(random.randint(1, 6), [T, Ti, U, Ui])
        g3 = mul(g1, g2)
        if not all(g[3] > 0 and g[2] >= 0 for g in (g1, g2, g3)): continue
        cnt += 1
        z = 0.123 + 0.456j
        w = cmath.sqrt(g1[2]*act(g2, z) + g1[3]) * cmath.sqrt(g2[2]*z + g2[3]) / cmath.sqrt(g3[2]*z + g3[3])
        wr = round(w.real)
        s1, s2, s3 = (kron(g[2], g[3]) for g in (g1, g2, g3))
        if wr == 1 and s3 == s1*s2: stats["w=1,mult ok"] += 1
        elif wr == -1 and s3 == -s1*s2: stats["w=-1,mult fails"] += 1
        else: stats["inconsistent"] += 1
    print("(c) c>=0,d>0 pairs (entries may be negative):", stats)
    # (d) non-extension witness
    g = mul(mul(mul(mul(U, Ti), U), Ti), U)
    print("(d) U T^-1 U T^-1 U =", g, "sigma =", kron(g[2], g[3]))

if __name__ == "__main__":
    main()

def shimura(c, d):
    if c == 0: return 1 if d > 0 else -1 if d < 0 else 0
    j = jacobi(c, abs(d))
    return j if d > 0 or c > 0 else -j

def broader():
    """w = 1 whenever d2 > 0 and d3 > 0 (any signs of c's and of d1): test with Shimura's symbol."""
    random.seed(2780); ok = bad = 0; neg_d2 = [0, 0]
    for _ in range(20000):
        g1 = rand_word(random.randint(1, 6), [T, Ti, U, Ui]); g2 = rand_word(random.randint(1, 6), [T, Ti, U, Ui])
        g3 = mul(g1, g2)
        m = shimura(g3[2], g3[3]) == shimura(g1[2], g1[3]) * shimura(g2[2], g2[3])
        if g2[3] > 0 and g3[3] > 0:
            ok += m; bad += (not m)
        else:
            neg_d2[0] += (not m); neg_d2[1] += 1
    print("broader: d2,d3>0: mult holds", ok, "fails", bad, "| otherwise: fails", neg_d2[0], "of", neg_d2[1])

if __name__ == "__main__":
    broader()
