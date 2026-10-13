"""R174: from-scratch check of bsA_wu_rokhlin_sign Thm W.
For an HJ word [[b1..br]] (b_i >= 2), G = tridiag(b_i; -1), n = det G = K(b1..br), A = K(b2..br).
Characteristic vector w = sum eps_i e_i with (G eps)_i == b_i (mod 2) (unique mod 2 since n odd).
Claim: (A/n) = +1 <=> eps^T G eps == n + r - 1 (mod 8); and eps^T G eps - n - r + 1 in {0,4} mod 8 always.
Checks: exhaustive letters 2..9 for r <= 5 (all residues mod 8), and random words r <= 10, letters <= 200 (no use of
DK Cor 4.1).  Also tests the Rokhlin sanity case L(p,1)."""
import itertools, random

def jac(a, n):
    a %= n; s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: s = -s
        a %= n
    return s if n == 1 else 0

def K(bs):
    p0, p1 = 1, 0      # K() = 1, K(b1) = b1, K(b1..bk) = bk K(..b_{k-1}) - K(..b_{k-2})
    for b in bs: p0, p1 = b * p0 - p1, p0
    return p0

def check(bs):
    r = len(bs); n = K(bs); A = K(bs[1:])
    if n % 2 == 0: return None
    sol = []
    for eps in itertools.product((0, 1), repeat=r):
        ok = all(((bs[i] * eps[i] - (eps[i-1] if i else 0) - (eps[i+1] if i < r-1 else 0)) - bs[i]) % 2 == 0 for i in range(r))
        if ok: sol.append(eps)
    assert len(sol) == 1, (bs, sol)
    e = sol[0]
    ww = sum(bs[i] * e[i] for i in range(r)) - 2 * sum(e[i] * e[i+1] for i in range(r - 1))
    d = (ww - n - r + 1) % 8
    j = jac(A, n)
    assert d in (0, 4), (bs, d)
    return (j == 1) == (d == 0)

bad = tot = 0
for r in range(1, 6):
    for bs in itertools.product(range(2, 10), repeat=r):
        c = check(bs)
        if c is None: continue
        tot += 1; bad += (not c)
print("exhaustive letters 2..9, r<=5:", tot, "odd words,", bad, "failures")
random.seed(174); bad = tot = 0
for _ in range(60000):
    r = random.randint(1, 10); bs = [random.randint(2, 200) for _ in range(r)]
    c = check(bs)
    if c is None: continue
    tot += 1; bad += (not c)
print("random r<=10, letters<=200:", tot, "odd words,", bad, "failures")
# W2: squares
bad = 0; cnt = 0
for m in range(3, 60, 2):
    n = m * m
    for A in range(1, n):
        if __import__('math').gcd(A, n) != 1: continue
        # HJ expansion of n/A
        bs = []; x, y = n, A
        while y:
            b = -(-x // y); bs.append(b); x, y = y, b * y - x
        if len(bs) > 9: continue
        e = None
        cnt += 1
        if not check(bs): bad += 1
print("odd squares m<60, all A with r<=9:", cnt, "words,", bad, "failures (W2 is the case (A/n)=+1)")
