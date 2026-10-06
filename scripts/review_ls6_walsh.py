"""R71 from-scratch checks of LS6 Lemma 2.1 (cube Leibniz) and Lemma 4.1 (Walsh/XOR cover).

Cube: corners A subset of U={0..n-1} as bitmasks.  D_T f(A) = sum_{B<=T} (-1)^{|T\\B|} f(A|B).
Lemma 4.1: Y*>=0, a_R = 2^-n sum_A Y*(A) chi_R(A).
  |D_U e^{-Y*}(0)| <= 2^n e^{||a||'} sum_{XOR-families T, xor = U} prod |a_R|        (first)
                   <= 2^n e^{2||a||'} prod_l sum_{R ni l} beta_R,  beta_R=max(|a|,|a|^{1/|R|}).
  XOR-family sum computed exactly by DP over subsets of the 2^n-1 nonempty R (product
  over R of (1 + |a_R| x^R) in the group algebra of (Z/2)^n).
Lemma 2.1(b),(c): random 0/1 and Lipschitz factors psi_i=F(u_i); check
  ||D_S prod psi|| <= sum_{f:S->I} prod_i ||D_{f^-1(i)} psi_i||  and (c)'s bounds.
"""
import itertools, math, random, sys

def pc(x): return bin(x).count("1")

def D(f, T, A):
    s = 0.0; B = T
    while True:
        s += (-1) ** pc(T & ~B) * f[A | B]
        if B == 0: break
        B = (B - 1) & T
    return s

def normD(f, T, n):
    full = (1 << n) - 1
    return max(abs(D(f, T, A)) for A in range(1 << n) if A & T == 0)

def piv(f, n):
    P = 0
    for l in range(n):
        if any(f[A | 1 << l] != f[A] for A in range(1 << n) if not A >> l & 1):
            P |= 1 << l
    return P

def lemma41(rng, n):
    # structured random Y*: sparse sums of indicator-type pieces + noise, >= 0
    Y = [0.0] * (1 << n)
    for _ in range(rng.randint(1, 4)):
        B = rng.randrange(1, 1 << n); c = rng.uniform(0, 3)
        kind = rng.random()
        for A in range(1 << n):
            if kind < 0.5: Y[A] += c * ((A & B) != B)
            else: Y[A] += c * ((A & B) != 0)
    if rng.random() < 0.5:
        Y = [y + rng.uniform(0, 0.5) for y in Y]
    N = 1 << n
    a = [sum(Y[A] * (-1) ** pc(A & R) for A in range(N)) / N for R in range(N)]
    an = sum(abs(a[R]) for R in range(1, N))
    f = [math.exp(-y) for y in Y]
    lhs = abs(D(f, N - 1, 0))
    # XOR-family DP
    dp = [0.0] * N; dp[0] = 1.0
    for R in range(1, N):
        nd = dp[:]
        for X in range(N):
            nd[X ^ R] += dp[X] * abs(a[R])
        dp = nd
    first = 2 ** n * math.exp(an) * dp[N - 1]
    beta = [0.0] + [max(abs(a[R]), abs(a[R]) ** (1 / pc(R))) for R in range(1, N)]
    second = 2 ** n * math.exp(2 * an) * math.prod(
        sum(beta[R] for R in range(1, N) if R >> l & 1) for l in range(n))
    assert lhs <= first * (1 + 1e-9) + 1e-12, (lhs, first)
    assert first <= second * (1 + 1e-9) + 1e-12, (first, second)
    # coefficient facts
    P = piv(Y, n); dl = max(Y) - min(Y)
    for R in range(1, N):
        if R & ~P: assert abs(a[R]) < 1e-9
        assert abs(a[R]) <= dl / 2 + 1e-9
    return lhs / first if first else 0, first / second if second else 0

def lemma21(rng, n, k):
    N = 1 << n
    facs = []
    for _ in range(k):
        # u depends on a random subset of coordinates
        dep = rng.randrange(0, N)
        tab = {}
        u = []
        for A in range(N):
            key = A & dep
            if key not in tab: tab[key] = rng.uniform(0, 0.5)
            u.append(tab[key])
        if rng.random() < 0.5:
            th = rng.uniform(0, 0.5); psi = [1.0 * (x < th) for x in u]; typ = ("01",)
        else:
            L = rng.uniform(0, 4); psi = [math.exp(-L * x / 2) * 2 for x in u]  # Lipschitz <= L
            typ = ("lip", L, max(u) - min(u), piv(u, n))
        facs.append((psi, typ))
    prod = [math.prod(p[A] for p, _ in facs) for A in range(N)]
    S = N - 1
    lhs = normD(prod, S, n)
    rhs = 0.0
    for f in itertools.product(range(k), repeat=n):
        pre = [0] * k
        for l, i in enumerate(f): pre[i] |= 1 << l
        rhs += math.prod(normD(facs[i][0], pre[i], n) for i in range(k))
    assert lhs <= rhs * (1 + 1e-9) + 1e-12
    for psi, typ in facs:
        for T in range(1, N):
            d = normD(psi, T, n)
            if T & ~piv(psi, n): assert d < 1e-12
            if typ[0] == "01": assert d <= 2 ** (pc(T) - 1) + 1e-12
            else:
                _, L, dl, pu = typ
                bound = 2 ** (pc(T) - 1) * L * dl * (1 if T & ~pu == 0 else 0)
                assert d <= bound + 1e-9, (d, bound)
    return lhs / rhs if rhs else 0

if __name__ == "__main__":
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
    w1 = w2 = w3 = 0
    for t in range(400):
        r1, r2 = lemma41(rng, rng.randint(1, 5)); w1 = max(w1, r1); w2 = max(w2, r2)
    for t in range(150):
        w3 = max(w3, lemma21(rng, rng.randint(1, 4), rng.randint(1, 3)))
    print("Lemma 4.1 ok: max lhs/first %.3f, first/second %.3f" % (w1, w2))
    print("Lemma 2.1 ok: max lhs/rhs %.3f" % w3)
