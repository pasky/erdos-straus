"""cf_groupoid: BFS on positive words under reversal, rotation (both ways), scaling up/down
(K(av,t,au) = a K(v,at,u)), with letters <= L and numerators <= NMAX. Reports pairs of words
of the same odd numerator in one component with different chi = (-A/n)."""
import sys
from cf_lib import chi
from collections import defaultdict
L = int(sys.argv[1]); NMAX = int(sys.argv[2]); ODD = len(sys.argv) > 3
def K(w):
    t, u, v = w
    return t * u * v - u - v
def nbrs(w):
    t, u, v = w
    out = [(t, v, u), (u, v, t), (v, t, u)]  # reversal, rotation, inverse rotation
    # scaling down: a | u, a | v -> (a t, u/a, v/a); scaling up: a | t -> (t/a, a u, a v)
    from math import gcd
    g = gcd(u, v)
    for a in range(2, g + 1):
        if g % a == 0:
            out.append((a * t, u // a, v // a))
    for a in range(2, t + 1):
        if t % a == 0:
            out.append((t // a, a * u, a * v))
    return [x for x in out if min(x) >= 1 and max(x) <= L and 1 <= K(x) <= NMAX and (not ODD or K(x) % 2 == 1)]
seen = {}
comp = 0
flips = 0
for t in range(1, L + 1):
    for u in range(1, L + 1):
        for v in range(1, L + 1):
            w = (t, u, v)
            if w in seen or not (1 <= K(w) <= NMAX) or (ODD and K(w) % 2 == 0):
                continue
            comp += 1
            stack = [w]; seen[w] = comp; members = [w]
            while stack:
                x = stack.pop()
                for y in nbrs(x):
                    if y not in seen:
                        seen[y] = comp; stack.append(y); members.append(y)
            byn = defaultdict(set)
            for x in members:
                n = K(x)
                if n % 2 == 1:
                    byn[n].add(chi(x, n))
            for n, s in byn.items():
                if len(s) == 2:
                    flips += 1
                    if flips <= 10:
                        print("FLIP component", comp, "n", n, [x for x in members if K(x) == n])
print("components", comp, "numerators with flip inside a component", flips)
