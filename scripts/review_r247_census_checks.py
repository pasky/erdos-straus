"""R247: checks on the brute-force census (review_r247_census output): Lemma 1.2, Lemma 3.1, Cor 3.2 (generalised to
depth), Prop 1.4 sign condition, parity laws; and covering sets at polynomial points per level for k = 2, 3, written to a
file for comparison with review_r247_search full mode.  usage: census_checks.py census.txt smax covers_out.txt"""
import itertools, sys
P = 3
def norm(a):
    a = [x % P for x in a]
    while a and a[-1] == 0: a.pop()
    return a
def add(a, b, sg=1):
    n = max(len(a), len(b)); return norm([(a[i] if i < len(a) else 0) + sg * (b[i] if i < len(b) else 0) for i in range(n)])
def mul(a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i + j] += x * y
    return norm(r)
def val(a):
    if not a: return 10 ** 9
    i = 0
    while a[i] == 0: i += 1
    return i
def deg(a): return len(a) - 1
T = [0, 1]
def tp(e): return [0] * e + [1]

census, smax, outp = sys.argv[1], int(sys.argv[2]), sys.argv[3]
tups = []
for l in open(census):
    s, m, g, w, C, v = l.split()
    f = lambda x: norm([int(c) for c in x])
    tups.append((int(s), f(m), f(g), f(w), f(C), f(v)))
tups = [t for t in tups if t[0] <= smax]
print('tuples', len(tups))

pts = []
for h in range(1, 5):
    for mid in itertools.product(range(3), repeat=h - 1):
        for lc in (1, 2): pts.append([1] + list(mid) + [lc])

viol = {'L12': 0, 'L31': 0, 'C32a': 0, 'C32b': 0, 'parity': 0, 'exact_lc': 0}
nexact = 0
covers = []
for (s, m, g, w1, C1, v1) in tups:
    a, b, z, y, t = deg(w1) + 1, deg(C1) + 1, deg(m), deg(g), deg(v1) + 2
    assert a + b + z == s and y + t == max(a, b)
    L = mul(g, m)
    E = add(mul(mul(L, T), w1), [1], -1)
    Ep = add(mul(mul(L, T), C1), [1], -1)
    D = add([1], mul(mul(tp(s), L), g))
    assert mul(E, Ep) == D
    if not (z % 2 == t % 2 == s % 2 and deg(E) % 2 == 0 and deg(Ep) % 2 == 0): viol['parity'] += 1
    for u in pts:
        h = deg(u)
        dep = val(add(E, u))                       # E ≡ -u mod T^dep
        x = add(w1, mul(u, C1))
        if not x:
            nexact += 1
            if u[-1] != 2: viol['exact_lc'] += 1
        m_ = min(dep, s - 1)
        if x and m_ > max(a - 1, b - 1 + h): viol['L12'] += 1
        d2 = min(val(add(mul(m, mul(w1, w1)), mul(u, v1))), s - 2)
        d3 = min(val(add(mul(u, mul(m, mul(C1, C1))), v1)), s - 2)
        if not (min(dep, s - 2) == d2 == d3): viol['L31'] += 1
        if h == 1:   # Cor 3.2 generalised: depth m <= s-2 forces the two degree inequalities (non-exact forms)
            mm = min(dep, s - 2)
            if add(mul(m, mul(w1, w1)), mul(u, v1)) and mm > max(z + 2 * a - 2, t - 1): viol['C32a'] += 1
            if add(mul(u, mul(m, mul(C1, C1))), v1) and mm > max(z + 2 * b - 1, t - 2): viol['C32b'] += 1
        if len(u) >= 2 and u[1] != 0:
            for k in (2, 3):
                N = -(-(s + k - 2) // 2)
                if dep >= N + 1: covers.append((k, ''.join(map(str, u)), N, s, m, g, w1, C1))
print('violations', viol, 'exact (tuple,u) pairs', nexact)
with open(outp, 'w') as f:
    for k, u, N, s, m, g, w1, C1 in covers:
        S = lambda p: ''.join(map(str, p))
        f.write(f"{k} {u} {N} {s} {S(m)} {S(g)} {S(w1)} {S(C1)}\n")
print('covering (k,u,tuple) records', len(covers))
