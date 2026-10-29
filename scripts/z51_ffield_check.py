# z51_ffield_check.py — independent check of the U_q engine (z51_ffield_enum.c) and of §3 claims.
# Independent re-implementation (Python, own arithmetic): enumerates all words of all shapes and records per f the shapes present.
# Also: n=3 closed formula for W_{(1,1,1)}, and the fraction of f with NO word of any shape except (n,0,0).
import sys, itertools
from collections import Counter

def polymul(a, b, p):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return r

def monics(d, p):
    for c in itertools.product(range(p), repeat=d):
        yield list(c) + [1]

def key(f):
    return tuple(f)

def all_words(n, p):
    """dict f -> Counter of shapes having words (all non-degenerate shapes)."""
    res = {}
    for s in range(n + 1):
        for b in range(n + 1 - s):
            a = n - s - b
            if s + b == 0 or s + a == 0:
                continue
            for t in monics(s, p):
                for v in monics(b, p):
                    tv = polymul(t, v, p)
                    for u in monics(a, p):
                        f = polymul(tv, u, p)
                        f = f[:]  # length n+1
                        for i, x in enumerate(u): f[i] = (f[i] - x) % p
                        for i, x in enumerate(v): f[i] = (f[i] - x) % p
                        assert f[n] == 1
                        res.setdefault(key(f), Counter())[(s, a, b)] += 1
    return res

def isU(s, a, b):
    return a >= 1 and (s % 2 == 1 or b % 2 == 1)

def chi(x, p):
    x %= p
    if x == 0: return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1

if __name__ == "__main__":
    for p, n in [(7, 3), (11, 3), (7, 4), (11, 4), (3, 6)]:
        W = all_words(n, p)
        tot = p ** n
        failU = 0; nowords = 0
        for f in itertools.product(range(p), repeat=n):
            F = tuple(list(f) + [1])
            C = W.get(F, Counter())
            wu = sum(c for sh, c in C.items() if isU(*sh))
            if wu == 0: failU += 1
            if sum(c for sh, c in C.items() if sh != (n, 0, 0)) == 0: nowords += 1
            if n == 3:
                c0, c1, c2 = f
                w111 = sum(1 + chi(-3 * x * x - 2 * c2 * x + c2 * c2 - 4 * c1 - 8, p)
                           for x in range(p) if (x ** 3 + c2 * x * x + c1 * x + c0 + 3 * x + c2) % p == 0)
                assert w111 == C.get((1, 1, 1), 0), (f, w111, C)
        print(f"p={p} n={n}: U-fail (incl squares) {failU} = {failU/tot:.4f}; no word at all {nowords} = {nowords/tot:.4f}"
              + ("; n=3 closed formula for W_(1,1,1) verified on all f" if n == 3 else ""))
