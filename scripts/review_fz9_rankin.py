"""R221 (from scratch): check fz_tail.c's linearised Lemma 4.1 constants (Lemma 5.1).
For each rho = k/24 and n0 in {S/2, S, 2S, 4S}: true fractional knapsack value V(n0) and right derivative lam_true over ALL
items (P, e), P monic irreducible != T (I'(j) of degree j), weight j, gain log(S_e(rho^j)/S_{e-1}(rho^j)); items of degree
j > J are bounded by ratio <= min(rho^j, log 2)/j and J is chosen so that this is < lam_true / 2 (checked).
Line c + lam*n dominates V on [0, inf) iff c >= V(n0) - lam_true*n0 and lam >= lam_true (V concave, V(0)=0).
Also brute-force: for q = 3, n <= 10 and q = 9, n <= 5, all factorisation types (multisets of (deg, exp) with available primes),
max_d #div(deg d)/exp(-d' log rho + lam n + c) over all (rho, n0) used by fz_tail must be <= 1.
usage: review_fz9_rankin.py dumpfile q S"""
import sys, math
from itertools import combinations_with_replacement
dump, q, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
def mob(n):
    m, r, p = n, 1, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r
def nirr(j):
    v = sum(mob(i) * q ** (j // i) for i in range(1, j + 1) if j % i == 0) // j
    return v - 1 if j == 1 else v
def items(rho, J):
    it = []
    for j in range(1, J + 1):
        y = rho ** j
        if y == 0: break
        cnt = min(nirr(j), 10 ** 6)          # capacity <= 4S < 10^6: more copies are never used
        Sp, e = 1.0, 1
        while e * j <= 4 * S + j:            # chains beyond capacity never used
            Se = Sp + y ** e; g = math.log(Se / Sp); Sp = Se
            if g <= 0: break
            it.append((g / j, j, cnt)); e += 1
    it.sort(reverse=True); return it
def fill(it, n0):
    need, val = n0, 0.0
    for i, (r, j, cnt) in enumerate(it):
        cap = cnt * j
        if cap > need: return val + need * r, r
        val += cap * r; need -= cap
        if need == 0: return val, it[i + 1][0]      # exactly at a boundary: right derivative = next ratio
    raise RuntimeError('list exhausted')
bad = 0; consts = []
for line in open(dump):
    k, n0, lr, lam, c = line.split(); k, n0 = int(k), int(n0); lam, c = float(lam), float(c); rho = k / 24
    J = 50
    while True:
        it = items(rho, J); V, lt = fill(it, n0)
        tailr = min(rho ** (J + 1), math.log(2)) / (J + 1)
        if tailr < lt / 2: break
        J *= 2
    # items cut by e*j > 4S + j have ratio <= min(1/(e j), rho^(e j)/j) <= min(1/(4S), rho^(4S)); they must lie below lt
    if not min(1 / (4 * S), rho ** (4 * S)) < lt: bad += 1; print('E-CUT NOT JUSTIFIED', k, n0, lt)
    ok = (c >= V - lt * n0 - 1e-12) and (lam >= lt)
    if not ok: bad += 1; print('VIOLATION', k, n0, 'V', V, 'lt', lt, 'their lam', lam, 'c', c, 'need c>=', V - lt * n0)
    consts.append((float(lr), lam, c))
print(f'q={q} S={S}: {len(consts)} (rho, n0) pairs, violations {bad}')
# brute force over factorisation types
def types(n, q):
    # multisets of (deg, exp) with at most I'(deg) primes per degree, total degree n
    parts = [(j, e) for j in range(1, n + 1) for e in range(1, n // j + 1)]
    out = []
    def rec(i, rem, cur, used):
        if rem == 0: out.append(list(cur)); return
        if i == len(parts): return
        j, e = parts[i]
        rec(i + 1, rem, cur, used)
        if j * e <= rem and used.get(j, 0) < nirr(j):
            used[j] = used.get(j, 0) + 1; cur.append((j, e)); rec(i, rem - j * e, cur, used); cur.pop(); used[j] -= 1
    rec(0, n, [], {}); return out
def ndiv(tp, d):
    poly = [1]
    for j, e in tp:
        new = [0] * (len(poly) + j * e)
        for i, c in enumerate(poly):
            for k in range(e + 1): new[i + j * k] += c
        poly = new
    return poly[d] if d < len(poly) else 0
for qq, nmax in ((q, 10 if q == 3 else 5),):
    worst = 0
    for n in range(1, nmax + 1):
        for tp in types(n, qq):
            for d in range(n + 1):
                cnt = ndiv(tp, d); dp = min(d, n - d)
                b = min(math.exp(lr * dp + lam * n + max(c, 0)) for lr, lam, c in consts)
                worst = max(worst, cnt / b)
    print(f'brute force q={qq} n<={nmax}: max count/linearised bound = {worst:.4f}', 'OK' if worst <= 1 else 'VIOLATION')
