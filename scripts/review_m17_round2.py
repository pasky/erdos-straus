"""R83 round 2: from-scratch checks of POINTWISE_MORDELL17 §5-6.

Uses the reviewer's own enumerations (review_m17_enum.c output in DIR: S{k}, U{k}, P{K}) and
independent brute force for the §6 reformulations.
usage: review_m17_round2.py DIR
"""
import sys, statistics
from math import gcd

D = sys.argv[1]
p = 17
LMAX_QU, KMAX_P = 7, 9


def v17(x):
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v


def cell_ok(r):
    return r % p in (5, 7)


# ---------- load data ----------
Q = {}   # k -> list of (a, m, d, j)
for k in range(1, LMAX_QU + 1):
    F = p**k
    Q[k] = []
    for l in open(f"{D}/S{k}.txt"):
        _, a, m, d = l.split(); a, m, d = int(a), int(m), int(d)
        f = 4 * a * d * m - 1; g = f // F; j = (a + m) // g
        assert (a + m) % g == 0
        Q[k].append((a, m, d, j))
U = {}
for k in range(1, LMAX_QU + 1):
    U[k] = []
    for l in open(f"{D}/U{k}.txt"):
        _, e, a, b, i = l.split(); U[k].append(tuple(map(int, (e, a, b, i))))
P = {}   # K -> list of ET (a,b,c,d) = (i,j,a',d'), a<=b
for K in range(1, KMAX_P + 1):
    N = p**K
    P[K] = []
    for l in open(f"{D}/P{K}.txt"):
        w = l.split(); f, ap, dp = int(w[1]), int(w[3]), int(w[4])
        i = (f + 1) // (4 * ap * dp); j = (i + N * ap) // (4 * ap * dp * i - 1)
        assert 4 * i * j * ap * dp == i + j + N * ap
        P[K].append((i, j, ap, dp))

# ---------- Lemma 5.1 ----------
bad = 0; c17 = 0
for k, L in Q.items():
    F = p**k
    for a, m, d, j in L:
        for x, y in ((a, m), (m, a)):
            if (-4 * x * x * d - (-x * pow(y, -1, F))) % F:
                bad += 1
        if j % p == 0:
            c17 += 1
print(f"5.1(i): Q boxes == -a/b mod 17^k for all Q data: {bad == 0} (bad {bad}); Q data with 17|c: {c17}")
bad = 0; inc = 0; nonprim_incell = 0; nonprim = 0
for K, L in P.items():
    N = p**K
    for a, b, c, d in L:
        f, fs = 4 * a * c * d - 1, 4 * b * c * d - 1
        if a % p == 0 or b % p == 0:
            nonprim += 1
            assert a % p == 0 and b % p == 0  # 17|a <=> 17|b
            if cell_ok(-f) or cell_ok(-fs):
                nonprim_incell += 1
            continue
        if (-f + a * pow(b, -1, N)) % N or (-fs + b * pow(a, -1, N)) % N:
            bad += 1
        inc += 1
print(f"5.1(ii): P boxes == -a/b mod 17^K for 17!|ab: {bad == 0} ({inc} data); "
      f"data with 17|a,b: {nonprim}, of which in-cell: {nonprim_incell}")

# Q == Q^{-1} as box sets
for k in (1, 3, 5, 7):
    F = p**k
    Qs = {(-4 * x * x * d) % F for a, m, d, j in Q[k] for x in (a, m)}
    Qi = {(-y * pow(x, -1, F)) % F for a, m, d, j in Q[k] for x, y in ((a, m), (m, a))}
    print(f"level {k}: Q == Q^-1 as sets: {Qs == Qi} ({len(Qs)} boxes)")

# ---------- P boxes by level (max box, level ceil(K/2)) ----------
Pbox = {}  # level -> set of residues
for K, L in P.items():
    lv = (K + 1) // 2
    for a, b, c, d in L:
        for f in (4 * a * c * d - 1, 4 * b * c * d - 1):
            Pbox.setdefault(lv, set()).add((-f) % p**lv)


def in_P_below(r, k):
    """levels l<k (resp. <=k) with r mod 17^l a P box"""
    return [l for l in range(1, k + 1) if l in Pbox and r % p**l in Pbox[l]]


# ---------- Lemma 5.2 ----------
tot = incell = strict = same = 0; i17 = []; parity_bad = 0; centre_bad = 0; allk = {}
for k, L in U.items():
    F = p**k
    for e, a, b, i in L:
        allk[k] = allk.get(k, 0) + 1
        tot += 1
        r = (-e) % F
        if i % p == 0:
            i17.append((k, r % p))
        if not cell_ok(r):
            continue
        incell += 1
        al, be = v17(a), v17(b)
        if al < be:
            a, b, al, be = b, a, be, al
        assert al > be, "alpha == beta in-cell U datum"
        if (al - be) % 2 == 0:
            parity_bad += 1
        # the proof's P-datum (A,B,C,D) = (b', c', a', i) at N' = 17^(al-be)
        ap, bp = a // p**al, b // p**be
        c = (a + b) // e; cp = c // p**be
        Np = p**(al - be)
        assert 4 * bp * cp * ap * i == bp + cp + Np * ap and ap % p and i % p
        lv = (al - be + 1) // 2
        if (r - (-bp * pow(cp, -1, p**lv))) % p**lv:
            centre_bad += 1
        ls = in_P_below(r, k)
        if any(l < k for l in ls):
            strict += 1
        elif ls:
            same += 1
print(f"5.2: U data {tot} (per level {allk}); in-cell {incell}; inside a P box of strictly lower level: {strict};"
      f" only same level: {same}; centre mismatches: {centre_bad}; alpha-beta even: {parity_bad}")
print(f"5.2: U data with 17|i: {len(i17)}, their box mod 17: {sorted(set(x for _, x in i17))}")

# ---------- new-box counts in C_5 ----------
allbox = {}  # level -> {r: set(types)}
for k in Q:
    F = p**k
    for a, m, d, j in Q[k]:
        for x in (a, m):
            allbox.setdefault(k, {}).setdefault((-4 * x * x * d) % F, set()).add("Q")
    for e, a, b, i in U[k]:
        allbox.setdefault(k, {}).setdefault((-e) % F, set()).add("U")
        allbox.setdefault(k, {}).setdefault((-pow(e, -1, F)) % F, set()).add("U")
for lv, S in Pbox.items():
    for r in S:
        allbox.setdefault(lv, {}).setdefault(r, set()).add("P")
for k in sorted(allbox):
    new = {}
    for r, ts in allbox[k].items():
        if r % p != 5:
            continue
        if any(l in allbox and r % p**l in allbox[l] for l in range(1, k)):
            continue
        for t in ts:
            new[t] = new.get(t, 0) + 1
    print(f"new boxes in C_5 at level {k}: {new}" + (" (P incomplete)" if k > 5 else ""))

# ---------- digit-set ratio t ----------
for k in (3, 4, 5, 7):
    F = p**k
    ts = []
    for r in allbox.get(k, {}):
        if r % p not in (5,) or any(l in allbox and r % p**l in allbox[l] for l in range(1, k)):
            continue
        z1, z2 = (-r) % F, (-pow(r, -1, F)) % F
        ts.append(min(z1, z2) / F)
    if ts:
        print(f"level {k}: new in-cell(5) boxes {len(ts)}: t median {statistics.median(ts):.3f} max {max(ts):.3f}")

# ---------- §6 (a,b)-reformulation, brute force for K <= 7 ----------
for K in (1, 3, 5):
    N = p**K
    found = set()
    for a in range(1, int((N / 2) ** 0.5) + 2):
        for b in range(a, N // (2 * a) + 1):
            m4 = 4 * a * b
            e = (-N) % m4
            if e == 0 or (a + b) % e:
                continue
            d = (N + e) // m4; c = (a + b) // e
            if c % p == 0 or d % p == 0:
                continue
            assert 4 * a * b * c * d == a + b + N * c
            found.add((a, b, c, d))
    print(f"K={K}: (a,b)-criterion count {len(found)} vs enumerated D_P {len(P[K])}: equal sets {found == set(P[K])}")

# ---------- §6 (a,s,t)-reformulation, brute force for K <= 5 ----------
for K in (1, 3, 5):
    N = p**K
    found = set()
    # b >= a  =>  sN + 2a >= 4a^2 s t  =>  4a^2 t <= N + 2a;  f | sN+a  =>  f | N + 4a^2 t
    for a in range(1, N + 1):
        if 4 * a * a > N + 2 * a:
            break
        for t in range(1, N + 1):
            if 4 * a * a * t > N + 2 * a:
                break
            for s in range(1, 4 * N):
                f = 4 * a * s * t - 1
                if f > N + 4 * a * a * t:
                    break
                if (s * N + a) % f:
                    continue
                b = (s * N + a) // f
                if b < a or s % p == 0 or t % p == 0:
                    continue
                assert (a + b) % s == 0 and 4 * a * b * s * t == s * N + a + b
                found.add((a, b, s, t))
    print(f"K={K}: (a,s,t)-criterion count {len(found)}; equal to D_P set: {found == set(P[K])}")

# ---------- periodicity of admissible K for fixed (a,b) ----------
def ordmod(x, m):
    o, y = 1, x % m
    while y != 1:
        y = y * x % m; o += 1
    return o

viol = 0; tested = 0
pairs = sorted({(a, b) for K in P for (a, b, c, d) in P[K] if a % p and b % p})[:300]
for a, b in pairs:
    m4 = 4 * a * b; o = ordmod(17, m4)
    adm = []
    for K in range(1, 120):
        N = p**K; e = (-N) % m4
        ok = e and (a + b) % e == 0 and N + e >= m4 and ((a + b) // e) % p and ((N + e) // m4) % p
        adm.append(bool(ok))
    K0 = next(K for K in range(1, 120) if adm[K - 1])
    for K in range(K0, 120 - o):
        tested += 1
        if adm[K - 1] != adm[K - 1 + o]:
            viol += 1
print(f"periodicity mod ord_4ab(17) beyond K0: {tested} checks, {viol} violations ({len(pairs)} pairs)")

# ---------- heuristic K^3 vs data ----------
print("D_P(K) vs K^3:", [(K, len(P[K]), K**3) for K in (1, 3, 5, 7, 9)])
