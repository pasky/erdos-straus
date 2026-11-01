"""z52d avenue Q11 (Z2652/Z2851): the 3-vertex (triangle multigraph) rung of the sandpile-pairing ladder.
Triangle with edge multiplicities a (1–2), b (2–3), c (1–3), sink 3: reduced Laplacian [[a+c, −a], [−a, a+b]],
τ = ab + bc + ca, self-pairing of vertex 1 = (a+b)/τ. Claim (PROVED in out_Q11 Z2652): every prime p ≡ 1 (4) has
a, b, c ≥ 1 with ab+bc+ca = p and ((a+b)/p) = −1 (take a prime q ≡ 3 (4) with (q/p) = −1, a ≡ √(−p) mod q, a < q,
b = q − a, c = (a²+p)/q − a); at odd squares n = m² no such triple exists. Checked here for p < 3·10⁴ and m² < 3·10⁴.
Run: timeout 60 python3 scripts/z52d_avenue_Q11_triangle_rung.py"""
def leg(a, p):
    r = pow(a % p, (p - 1) // 2, p); return -1 if r == p - 1 else r
def jac(a, n):  # Jacobi symbol (a/n), n odd positive
    a %= n; s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: s = -s
        a %= n
    return s if n == 1 else 0
def has_triple(n, sym):
    # a, b ≥ 1 with d = a+b dividing a²+n, c = (a²+n)/d − a ≥ 1, symbol of d mod n = −1
    a = 1
    while a * a < n:
        N = a * a + n
        for d in range(a + 1, N // a + 1):
            if N % d == 0 and N // d - a >= 1 and sym(d, n) == -1: return (a, d - a, N // d - a)
        a += 1
    return None
isp = lambda n: n > 1 and all(n % k for k in range(2, int(n ** .5) + 1))
ps = [p for p in range(5, 30000, 4) if isp(p)]
bad = [p for p in ps if has_triple(p, leg) is None]
print(f'primes p ≡ 1 (4) < 3·10⁴: {len(ps)}, without a non-square triangle: {bad}')
sq = [m * m for m in range(3, 174, 2)]
hits = [n for n in sq if has_triple(n, jac)]
print(f'odd squares 9..{sq[-1]}: with a triple of Jacobi symbol −1: {hits}')
