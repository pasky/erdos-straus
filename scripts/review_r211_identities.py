"""R211 from-scratch checks for O213 TRANSPORT_LAW.md (SHARP 1, 2, 3; item (a)).

Independent of scripts/y5_*.  Usage: PYTHONPATH=scripts uv run python scripts/review_r211_identities.py
"""
import random, math, sys
from math import gcd

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

def v2split(x):
    v = 0
    while x % 2 == 0: x //= 2; v += 1
    return v, x

def hilbert2(a, b):
    """2-adic Hilbert symbol (a,b)_2, a,b nonzero integers (Serre, Cours d'arithmétique III.1.2)."""
    al, u = v2split(a); be, w = v2split(b)
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    e = (eps(u) * eps(w) + al * om(w) + be * om(u)) % 2
    return -1 if e else 1

def hilbert_inf(a, b):
    return -1 if (a < 0 and b < 0) else 1

def continuants(word):
    K = [1]; Km = 0
    for a in word:
        K.append(a * K[-1] - Km); Km = K[-2]
    return K  # K[0]=1, ..., K[r]

# ---------- SHARP 1: Ptolemy relations + transport law, all formal words, odd N <= X
def sharp1(X):
    nw = bad = 0; cls = {}
    for c in range(1, X + 2):
        for m in range(1, X + 3):
            g = c * m - 1
            if g == 0: continue
            if g - c > X: break
            for s in range(1, (X + c) // g + 1):
                N = g * s - c
                if N >= 1 and N % 2 == 1:
                    h, hp = c * m - 1, m * s - 1
                    q = [hp, c, m, s, h]
                    # exact Ptolemy relations (P)
                    assert q[0]*q[1] == N + q[3] and q[1]*q[2] == 1 + q[4] and q[2]*q[3] == 1 + q[0]
                    assert q[3]*q[4] == N + q[1] and q[4]*q[0] == 1 + N*q[2]
                    ev = [i for i in range(5) if q[i] % 2 == 0]
                    assert len(ev) == 2 and (ev[1] - ev[0]) % 5 in (1, 4), (c, m, s)
                    i = ev[0] if (ev[1] - ev[0]) % 5 == 1 else ev[1]   # edge {q_i, q_{i+1}}
                    o = q[(i + 3) % 5]
                    eps = 0 if i in (1, 2) else 1        # edges {c,m},{m,s}: ee' = 1 + o
                    ee = q[i] * q[(i + 1) % 5]
                    assert ee % 4 == 0 and (o + N**eps) % 4 == 0
                    assert (ee % 8 == 0) == ((o + N**eps) % 8 == 0)
                    chi = jacobi(hp % N, N) if N > 1 else 1
                    pred = -jacobi(-1 % N, N) * jacobi(2, o) * jacobi(2, N)**eps if N > 1 else None
                    thm12 = jacobi(-1 % N, N) * (-1 if ee % 8 == 0 else 1) if N > 1 else None
                    if N > 1 and (chi != pred or chi != thm12): bad += 1
                    if N % 8 == 1:
                        assert o % 4 == 3
                        cert = any(x % 4 == 0 for x in q)
                        assert cert == (o % 8 == 7) and (N == 1 or cert == (chi == -1))
                    cls[N % 8] = cls.get(N % 8, 0) + 1
                    nw += 1
    print(f"SHARP1: X={X} words={nw} by N mod 8={dict(sorted(cls.items()))} failures={bad}")

# ---------- SHARP 2: general-r Jacobi law
def sharp2(trials, seed=1):
    rnd = random.Random(seed); tested = bad = 0; edge = {"K=±1": 0, "even K_i": 0, "neg": 0, "letters 0/1": 0}
    while tested < trials:
        r = rnd.randint(1, 10)
        mode = rnd.random()
        if mode < 0.4: w = [rnd.randint(2, 9) for _ in range(r)]
        elif mode < 0.7: w = [rnd.randint(-6, 6) for _ in range(r)]
        else: w = [rnd.choice([-2, -1, 0, 1, 2, 3, 4, 8, 16, rnd.randint(-50, 50)]) for _ in range(r)]
        K = continuants(w); N = K[r]
        if N <= 0 or N % 2 == 0 or any(k == 0 for k in K[1:r]): continue
        lhs = jacobi(K[r-1] % N, N)
        rhs = 1; inf = 1
        for i in range(1, r):
            rhs *= hilbert2(K[i], -K[i+1]); inf *= hilbert_inf(K[i], -K[i+1])
        cnt = sum(1 for i in range(1, r) if K[i] < 0 < K[i+1])
        assert inf == (-1)**cnt
        if lhs != rhs * inf: bad += 1; print("FAIL", w, K)
        tested += 1
        if any(abs(k) == 1 for k in K[1:r]): edge["K=±1"] += 1
        if any(k % 2 == 0 for k in K[1:r]): edge["even K_i"] += 1
        if any(k < 0 for k in K[1:r]): edge["neg"] += 1
        if any(a in (0, 1) for a in w): edge["letters 0/1"] += 1
    print(f"SHARP2: tested={tested} failures={bad} edge-case coverage={edge}")

# ---------- SHARP 3: narrow/wide Prop 1 (bijection + sign) for small N
def sharp3(X):
    bad = 0; nneg_missing = []
    for N in range(3, X + 1, 2):
        anyneg = False
        for m in range(1, 40):
            M = 1 + N * m
            pos = set(); neg = set()
            for a in range(1, M + 1):
                if M % a: continue
                b = M // a
                if (a + 1) % m == 0 and (b + 1) % m == 0: pos.add(((a + 1)//m, (b + 1)//m))
                if a > 1 and b > 1 and (a - 1) % m == 0 and (b - 1) % m == 0: neg.add(((1 - a)//m, (1 - b)//m))
            # compare with direct word enumeration
            for (c, s) in pos:
                if not (c >= 1 and s >= 1 and c*m*s - c - s == N): bad += 1
            for (c, s) in neg:
                if not (c <= -1 and s <= -1 and c*m*s - c - s == N): bad += 1
                K = continuants([c, m, s])
                l = jacobi(K[2] % N, N)
                s2 = hilbert2(K[1], -K[2]) * hilbert2(K[2], -K[3])
                if l != -s2: bad += 1
                anyneg = True
        if not anyneg: nneg_missing.append(N)
    print(f"SHARP3: odd N<= {X}: failures={bad}; N with no negative-pair word (m<40): {nneg_missing[:10]}")

# ---------- item (a): C(o) in Jacobi non-residues; P_h bijection
def item_a(omax, Xn):
    bad = 0
    for o in range(7, omax + 1, 8):
        C = {(-c) % o for c in range(2, o + 2, 2) if (o + 1) % c == 0 and ((o + 1)//c) % 2 == 0}
        for x in C:
            if gcd(x, o) != 1 or jacobi(x, o) != -1: bad += 1
        assert len(C) == sum(1 for d in range(1, (o+1)//4 + 1) if ((o+1)//4) % d == 0)
    # P_h words at N (formal, c,m even, h=o) vs C(o)
    for N in range(1, Xn, 8):
        for o in range(7, N + 200, 8):
            C = {(-c) % o: c for c in range(2, o + 2, 2) if (o + 1) % c == 0 and ((o + 1)//c) % 2 == 0}
            words = [(c, (o+1)//c, (N + c)//o) for c in range(2, o+2, 2)
                     if (o+1) % c == 0 and ((o+1)//c) % 2 == 0 and (N + c) % o == 0 and (N + c)//o >= 1]
            pred = 1 if (N % o) in C and (N + C[N % o]) // o >= 1 else 0
            if len(words) != pred: bad += 1
    print(f"item(a): o<= {omax}, N<{Xn}: failures={bad}")

if __name__ == "__main__":
    sharp1(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
    sharp2(200000)
    sharp3(301)
    item_a(4000, 2000)

# ---------- R211 extra: s_2 product depends only on the word mod 8 (N odd), as claimed in memo y5_general_r_jacobi
def s2_of(w):
    K = continuants(w); r = len(w)
    if K[r] % 2 == 0 or any(k == 0 for k in K[1:r + 1]): return None
    p = 1
    for i in range(1, r): p *= hilbert2(K[i], -K[i + 1])
    return p

def mod8_invariance(trials, seed=7):
    rnd = random.Random(seed); t = bad = 0
    while t < trials:
        r = rnd.randint(2, 8); w = [rnd.randint(-20, 20) for _ in range(r)]
        a = s2_of(w)
        if a is None: continue
        w2 = [x + 8 * rnd.randint(-5, 5) for x in w]
        b = s2_of(w2)
        if b is None: continue
        t += 1
        # s_inf may differ between w and w2 (signs of K_i): compare s_2 * (-1/N)^? -> compare s_2 only
        if a != b: bad += 1
    print(f"mod8-invariance of s_2 (N odd): {t} pairs, {bad} differences")

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[2] == "mod8":
    mod8_invariance(100000)
