"""R198 from-scratch: move groupoid (reversal, rotation^{+-1}, scaling up/down by any a>=2) on the box
B = {(t,u,v): 1 <= letters <= L, 1 <= K <= NMAX}. Union-find; report #components and the odd numerators n having
two words of opposite chi=(-A/n) in one component. Option 'odd': only words with odd K are nodes.
Usage: python review_cf_groupoid.py L NMAX [odd]"""
import sys
from sympy import jacobi_symbol as J
L, NMAX = int(sys.argv[1]), int(sys.argv[2]); ODD = len(sys.argv) > 3
K = lambda t, u, v: t * u * v - u - v
inbox = lambda w: all(1 <= x <= L for x in w) and 1 <= K(*w) <= NMAX and (not ODD or K(*w) % 2)
nodes = [(t, u, v) for t in range(1, L + 1) for u in range(1, L + 1) for v in range(1, L + 1) if inbox((t, u, v))]
idx = {w: i for i, w in enumerate(nodes)}
par = list(range(len(nodes)))
def f(i):
    while par[i] != i:
        par[i] = par[par[i]]; i = par[i]
    return i
def un(a, b):
    a, b = f(a), f(b)
    if a != b: par[a] = b
for w in nodes:
    t, u, v = w
    nb = [(t, v, u), (u, v, t), (v, t, u)]
    for a in range(2, L + 1):
        if u % a == 0 and v % a == 0: nb.append((a * t, u // a, v // a))
        if t % a == 0: nb.append((t // a, a * u, a * v))
    for w2 in nb:
        if w2 in idx: un(idx[w], idx[w2])
comps = {}
for i, w in enumerate(nodes):
    n = K(*w)
    if n % 2:
        comps.setdefault((f(i), n), set()).add(J(1 - w[0] * w[1], n))
print(f"L={L} NMAX={NMAX} odd={ODD}: nodes {len(nodes)}, components {len({f(i) for i in range(len(nodes))})}")
print("flip numerators:", sorted({n for (c, n), s in comps.items() if len(s) == 2}))
