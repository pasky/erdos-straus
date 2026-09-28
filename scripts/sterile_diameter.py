"""Diameters (vertex graph, shared denominator) of dumped sterile components.
uv run python scripts/sterile_diameter.py FILE.jsonl ...   (finite description only)"""
import json, sys
from collections import Counter, deque


def diameter(comp):
    comp = [tuple(v) for v in comp]
    B = {}
    for v in comp:
        for z in set(v):
            B.setdefault(z, []).append(v)
    best = 0
    for s in comp:
        dist = {s: 0}
        q = deque([s])
        while q:
            v = q.popleft()
            for z in set(v):
                for w in B[z]:
                    if w not in dist:
                        dist[w] = dist[v] + 1
                        q.append(w)
        best = max(best, max(dist.values()))
    return best


rows = []
for fn in sys.argv[1:]:
    for line in open(fn):
        r = json.loads(line)
        for C in r.get("dumped", []):
            rows.append((diameter(C), len(C), r["p"]))
rows.sort(reverse=True)
print("diameter histogram:", sorted(Counter(d for d, _, _ in rows).items()))
print("largest diameters:", rows[:10])
