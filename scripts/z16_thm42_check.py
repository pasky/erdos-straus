"""z16_thm42_check.py (O241): checks STERILE_DIOPHANTINE Thm 4.2 on the census (bsE_famcount 3 2 SMAX print):
for every Case B tuple (s, w = T w1, C = T C1, E) and every rational rho = P/Q (height <= H, T ∤ Q) agreeing with -E to
order D := delta(-E, rho) (capped at s - 1): if rho != -w1/C1 then H_tau >= min(N+1, D) - H(rho), where N = ceil(s/2) and
H_tau = max(deg w1, deg C1).  Also checks delta(-E, -w1/C1) >= s - 1 (Lemma 1.1).  Prints #pairs and #violations."""
import sys, re, itertools
P3 = 3; cen, H = sys.argv[1], int(sys.argv[2])
def trim(a):
    a = [x % 3 for x in a]
    while a and a[-1] == 0: a.pop()
    return a
def mul(a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return trim(r)
def sub(a, b):
    n = max(len(a), len(b)); return trim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)])
def val(a):  # T-adic valuation of a polynomial, inf for 0
    for i, x in enumerate(a):
        if x: return i
    return 10 ** 9
def deg(a): return len(a) - 1
def pmod(a, b):
    a = a[:]; inv = 1 if b[-1] == 1 else 2
    while a and len(a) >= len(b):
        f = a[-1] * inv % 3; sh = len(a) - len(b)
        for i, x in enumerate(b): a[sh + i] = (a[sh + i] - f * x) % 3
        a = trim(a)
    return a
def pgcd(a, b):
    while b: a, b = b, pmod(a, b)
    return a
rats = []  # (R248 repair D7) reduced representatives only: gcd(P, Q) = 1, Q monic-normalised by Q(0) = 1
for h in range(0, H + 1):
    for Pp in itertools.product(range(3), repeat=h + 1):
        for Q in itertools.product(range(3), repeat=h + 1):
            Pp_, Q_ = trim(list(Pp)), trim(list(Q))
            if not Q_ or Q_[0] == 0 or not Pp_: continue
            if max(deg(Pp_), deg(Q_)) != h or Q_[0] != 1 or deg(pgcd(Pp_, Q_)) > 0: continue
            rats.append((Pp_, Q_, h))
pairs = viol = lem = exact = 0
for line in open(cen):
    m = re.match(r"s=(\d+) a=.* w=\[([0-9,]*)\] C=\[([0-9,]*)\] .* E=\[([0-9,]*)\]", line)
    if not m: continue
    s = int(m.group(1)); w = [int(x) for x in m.group(2).split(",")]; C = [int(x) for x in m.group(3).split(",")]
    E = [int(x) for x in m.group(4).split(",")]
    w1, C1 = trim(w[1:]), trim(C[1:]); N = (s + 1) // 2; Ht = max(deg(w1), deg(C1))
    mE = trim([-x for x in E])
    # delta(-E, -w1/C1) = v(-E*C1 + w1)
    if min(val(sub(mul(mE, C1), [-x for x in w1])), s - 1) < s - 1: lem += 1
    for (Pp, Q, h) in rats:
        D = min(val(sub(mul(mE, Q), Pp)), s - 1)     # delta(-E, P/Q), capped
        if D < N + 1: continue
        pairs += 1
        if not sub(mul(Pp, C1), mul([-x for x in w1], Q)): exact += 1; continue   # rho == -w1/C1
        if Ht < min(N + 1, D) - h: viol += 1
print(f"Lemma 1.1 depth failures: {lem}; (tuple, rational) pairs with rho in the tuple ball: {pairs} (of which exact rho = rho_tau: {exact}); Thm 4.2 violations: {viol}")
