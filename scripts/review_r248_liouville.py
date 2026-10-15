"""review_r248_liouville.py (R248, from scratch): checks of STERILE_DIOPHANTINE §4 on the Case B tuples s <= 17
(FULL output of review_r248_caseB.c).
 (a) Lemma 4.1 on all pairs of distinct rationals of height <= HMAX: v_T(r1 - r2) <= H1 + H2 (and sharpness count).
 (b) Lemma 1.1 agreement: v_T(E - w1/C1) >= s - 1 for every tuple.
 (c) Thm 4.2 at rational points: every rational rho of height <= HMAX inside the tuple ball (depth N+1, N = ceil(s/2)),
     rho != rho_tau, satisfies H_tau >= N + 1 - H(rho), H_tau = max(a-1, b-1); also at random u in the ball with all
     rationals rho: H_tau >= min(N+1, v(u - rho)) - H(rho).  Reports min slack.
usage: python3 scripts/review_r248_liouville.py FULLFILE HMAX"""
import sys, itertools, random
p = 3; PREC = 40
def trim(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    return a
def mul(a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % p
    return trim(r)
def divmod_(a, b):
    a = list(a); q = [0] * max(0, len(a) - len(b) + 1); il = 1 if b[-1] == 1 else 2
    while len(a) >= len(b) and a:
        sh = len(a) - len(b); f = a[-1] * il % p; q[sh] = f
        for i, y in enumerate(b): a[i + sh] = (a[i + sh] - f * y) % p
        a = trim(a)
    return trim(q), a
def gcd(a, b):
    while b: a, b = b, divmod_(a, b)[1]
    return a
def series(P, Q, n=PREC):          # power series P/Q mod T^n, Q(0) != 0
    inv0 = 1 if Q[0] == 1 else 2; out = []; r = list(P) + [0] * n
    for i in range(n):
        c = r[i] * inv0 % p; out.append(c)
        for j, y in enumerate(Q):
            if i + j < len(r): r[i + j] = (r[i + j] - c * y) % p
    return out
def val(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]: return i
    return min(len(x), len(y))
def rationals(H):
    seen = {}
    for dq in range(H + 1):
        for qc in itertools.product(range(p), repeat=dq):
            Q = trim(list(qc) + [1])
            if Q[0] == 0: continue
            for dp in range(-1, H + 1):
                for pc in itertools.product(range(p), repeat=dp + 1):
                    P = trim(list(pc))
                    if dp >= 0 and (not P or len(P) - 1 != dp): continue
                    if P and len(gcd(P, Q)) > 1: continue
                    s = tuple(series(P, Q))
                    h = max(len(P) - 1, len(Q) - 1)
                    if s not in seen or seen[s] > h: seen[s] = h
    return seen       # series -> height
def neg(a): return [(-x) % p for x in a]
if __name__ == "__main__":
    fn, H = sys.argv[1], int(sys.argv[2]); R = rationals(H); Rl = list(R.items())
    print("rationals of height <=", H, ":", len(R))
    viol = sharp = 0
    for i in range(len(Rl)):
        for j in range(i + 1, len(Rl)):
            d = val(Rl[i][0], Rl[j][0])
            if d > Rl[i][1] + Rl[j][1]: viol += 1
            if d == Rl[i][1] + Rl[j][1]: sharp += 1
    print("(a) Lemma 4.1 pairs:", len(Rl) * (len(Rl) - 1) // 2, "violations", viol, "equality cases", sharp)
    bad_b = 0; pairs = 0; viol_c = 0; minsl = 99; viol_r = 0; minsl_r = 99; exact = 0
    random.seed(1)
    for line in open(fn):
        t = line.split(); s = int(t[0]); kv = dict(x.split("=") for x in t[3:])
        a, b = int(kv["a"]), int(kv["b"]); E = [int(c) for c in kv["E"]]; w1 = [int(c) for c in kv["w1"]]; C1 = [int(c) for c in kv["C1"]]
        Es = (E + [0] * PREC)[:PREC]; rho_t = series(neg(w1), C1)
        if val(neg(Es), rho_t) < s - 1: bad_b += 1
        N = (s + 1) // 2; Ht = max(a - 1, b - 1)
        if N + 1 > s - 1: continue
        ctr = neg(Es)
        for ser, h in Rl:
            if val(list(ser), ctr) >= N + 1:
                if list(ser) == rho_t[:PREC]: exact += 1; continue
                pairs += 1; sl = Ht - (N + 1 - h); minsl = min(minsl, sl)
                if sl < 0: viol_c += 1
        for _ in range(20):
            u = ctr[:N + 1] + [random.randrange(p) for _ in range(PREC - N - 1)]
            for ser, h in Rl:
                if list(ser) == rho_t: continue
                sl = Ht - (min(N + 1, val(u, list(ser))) - h); minsl_r = min(minsl_r, sl)
                if sl < 0: viol_r += 1
    print("(b) tuples with v(-E - rho_tau) < s-1:", bad_b)
    print("(c) rational-in-ball pairs:", pairs, "violations", viol_c, "min slack", minsl, "exact (rho = rho_tau) cases", exact)
    print("(c') random u in ball x all rationals: violations", viol_r, "min slack", minsl_r)
