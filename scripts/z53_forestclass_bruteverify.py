"""z53 FORESTCLASS: independent brute-force re-implementation of z53_forestclass_forest.c's per-n line,
for small odd n.  Edges by direct AP enumeration (v ≡ -n mod u, test uv | n+u+v), components by BFS,
root-set membership by exhaustive square search mod a.  Prints lines in the same format; compare with diff.
Usage: uv run python scripts/z53_forestclass_bruteverify.py < list_of_n
"""
import sys
from math import isqrt, log10


def jac(a, n):
    a %= n
    t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def issq(x, a):
    x %= a
    return any((b * b - x) % a == 0 for b in range(a))


def line(n):
    lim = n + 2
    adj = {}
    E = []
    for u in range(1, lim + 1):
        if u * (u - 1) > n + 1:
            break
        r = (-n) % u
        v = r if r > u else r + u * ((u - r) // u + 1) if r <= u else r
        # all v > u with v ≡ -n (mod u)
        v = r
        while v <= u:
            v += u
        while v <= lim:
            if (n + u + v) % (u * v) == 0:
                E.append((u, v))
            v += u
    col = {}
    def c(x):
        if x not in col:
            col[x] = jac(x, n)
        return col[x]
    bi = []
    for u, v in E:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
        bi.append(c(u) * c(v) == -1)
    # depth: multi-source BFS
    dep = {}
    from collections import deque
    dq = deque()
    for (u, v), b in zip(E, bi):
        if b:
            for x in (u, v):
                if x not in dep:
                    dep[x] = 1
                    dq.append(x)
    while dq:
        x = dq.popleft()
        for y in adj.get(x, []):
            if y not in dep:
                dep[y] = dep[x] + 1
                dq.append(y)
    Us = isqrt(n) + 2
    R = isqrt(n) + 1
    names = ["ALL", "SM", "SP", "NR", "SMN", "SQ"]
    st = {k: [0] * 8 for k in names}
    for a in range(1, R + 1):
        ca = c(a)
        if ca == 0:
            continue
        sm = issq(-n, a)
        sp = issq(n, a)
        sq = isqrt(a) ** 2 == a
        ins = {"ALL": True, "SM": sm, "SP": sp, "NR": ca == -1, "SMN": sm and ca == -1, "SQ": sq}
        d = dep.get(a, None)
        for k in names:
            if not ins[k]:
                continue
            s = st[k]
            s[0] += 1
            if d is not None:
                s[1] += 1
                if d <= 1:
                    s[2] += 1
                if d <= 2:
                    s[3] += 1
                if not s[4]:
                    s[4], s[5] = a, s[0]
                if a > 100 and not s[6]:
                    s[6], s[7] = a, s[0]
    out = f"n={n} ndig={int(log10(n))+1} edges={len(E)} bi={sum(bi)} Us={Us}"
    for k in names:
        s = st[k]
        out += f" {k}={s[0]}/{s[1]}/{s[2]}/{s[3]} f={s[4]}@{s[5]} f100={s[6]}@{s[7]}"
    return out


for tok in sys.stdin.read().split():
    n = int(tok)
    if n >= 5 and n % 2:
        print(line(n))
