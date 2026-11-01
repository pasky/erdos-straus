#!/usr/bin/env python3
"""Z1197: elimination widths of three factor graphs for the same divisor-residue constraints.

Instance (per ES window p, x; r = 4x-p, M = p x, N = M^2, primes q_1..q_k of N, exponents 2a_i):
  variables v_i in [0, 2a_i]  (exponent of q_i in e); f has exponent 2a_i - v_i (no extra variable)
  constraints: A: prod q_i^{v_i} == -M (mod r);  B: prod q_i^{2a_i - v_i} == -M (mod r).
Three factor graphs for the SAME constraints:
  G1 global: one factor per constraint, scope = all v_i (the direct table).
  G2 chain:  auxiliary state s_i = prod_{j<=i} q_j^{v_j} mod r; factor (s_{i-1}, v_i, s_i);
             constraint A is s_k = -M, B is the same chain on the reversed exponents (t_i).
  G3 CRT:    as G2 but per prime power s^c || r (separate chains mod s^c).
For each graph: primal graph, min-fill elimination order (networkx), width = max bag - 1, and the
DP cost sum_v prod_{u in bag(v)} |D_u| (domain product of the bag at each elimination step).
Domains: |D(v_i)| = 2a_i+1, |D(s_i)| = r (or s^c). Exact treewidth is not computed (min-fill
is an upper bound).
"""
import sys, json, math
import networkx as nx
from networkx.algorithms.approximation import treewidth_min_fill_in

def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def prime_powers(n):
    out = []
    for q, a in factor(n).items():
        out.append(q ** a)
    return out

def cost_of_order(G, dom):
    """min-fill elimination on graph G; returns (width, DP cost) with domain sizes dom"""
    H = G.copy()
    width = 0; cost = 0
    while H.number_of_nodes() > 0:
        # min-fill heuristic
        best = None
        for v in H.nodes():
            nb = list(H.neighbors(v))
            fill = sum(1 for i in range(len(nb)) for j in range(i + 1, len(nb)) if not H.has_edge(nb[i], nb[j]))
            key = (fill, len(nb))
            if best is None or key < best[0]:
                best = (key, v)
        v = best[1]
        nb = list(H.neighbors(v))
        bag = [v] + nb
        width = max(width, len(nb))
        prod = 1
        for u in bag:
            prod *= dom[u]
        cost += prod
        for i in range(len(nb)):
            for j in range(i + 1, len(nb)):
                H.add_edge(nb[i], nb[j])
        H.remove_node(v)
    return width, cost

def build_graphs(qs, es, r, B_mod_list=None):
    """qs: primes of M (list), es: exponents in M (so exponents in M^2 are 2*es)."""
    k = len(qs)
    dom = {}
    G1 = nx.Graph()
    vs = [("v", i) for i in range(k)]
    for i in range(k):
        dom[("v", i)] = 2 * es[i] + 1
        G1.add_node(("v", i))
    # one factor per constraint (A, B): clique over all v_i
    for c in ("A", "B"):
        for i in range(k):
            for j in range(i + 1, k):
                G1.add_edge(("v", i), ("v", j))
    # G2: chain for A (states s_i mod r) and chain for B (states t_i mod r), both over v_i
    G2 = nx.Graph(); dom2 = {}
    for i in range(k):
        dom2[("v", i)] = 2 * es[i] + 1; G2.add_node(("v", i))
    for name in ("s", "t"):
        prev = None
        for i in range(k):
            node = (name, i); dom2[node] = r; G2.add_node(node)
            G2.add_edge(("v", i), node)
            if prev is not None:
                G2.add_edge(prev, node)
            if prev is not None:
                G2.add_edge(("v", i), prev)
            prev = node
    # G3: CRT split of r into prime powers; each prime power gets its own chains
    G3 = nx.Graph(); dom3 = {}
    for i in range(k):
        dom3[("v", i)] = 2 * es[i] + 1; G3.add_node(("v", i))
    for pp in prime_powers(r) if r > 1 else []:
        for name in ("s", "t"):
            prev = None
            for i in range(k):
                node = (name, pp, i); dom3[node] = pp; G3.add_node(node)
                G3.add_edge(("v", i), node)
                if prev is not None:
                    G3.add_edge(prev, node)
                    G3.add_edge(("v", i), prev)
                prev = node
    return (G1, dom), (G2, dom2), (G3, dom3)

def window_stats(p, x):
    r = 4 * x - p; M = p * x
    f = factor(M)
    qs = list(f.keys()); es = [f[q] for q in qs]
    (G1, d1), (G2, d2), (G3, d3) = build_graphs(qs, es, r)
    out = {}
    for name, (G, d) in (("G1_global", (G1, d1)), ("G2_chain", (G2, d2)), ("G3_crt", (G3, d3))):
        w, c = cost_of_order(G, d)
        out[name] = {"width": w, "cost": c}
    out["k"] = len(qs)
    out["r"] = r
    out["tau_M2"] = math.prod(2 * e + 1 for e in es)
    return out

def main(pmax=1000, K=6):
    ps = [p for p in range(5, pmax) if p % 4 == 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))]
    rows = []
    for p in ps:
        x0 = -(-p // 4)
        for x in range(x0, x0 + K):
            rows.append((p, x, window_stats(p, x)))
    return rows

if __name__ == "__main__":
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    rows = main(pmax, 6)
    # tiny instance for the report
    ex = [r for r in rows if r[2]["k"] >= 4][:1]
    if ex:
        p, x, st = ex[0]
        print("example p=%d x=%d r=%d k=%d tau(M^2)=%d" % (p, x, st["r"], st["k"], st["tau_M2"]))
        for name in ("G1_global", "G2_chain", "G3_crt"):
            print("  ", name, st[name])
    for name in ("G1_global", "G2_chain", "G3_crt"):
        ws = [r[2][name]["width"] for r in rows]
        cs = [r[2][name]["cost"] for r in rows]
        print(f"{name}: max width={max(ws)}  total DP cost over {len(rows)} windows={sum(cs)}  "
              f"median cost={sorted(cs)[len(cs)//2]}")
    big = max(rows, key=lambda r: r[2]["k"])
    print("max k:", big[2]["k"], "at p=%d x=%d" % (big[0], big[1]), {n: big[2][n] for n in ("G1_global", "G2_chain", "G3_crt")})
    json.dump([{"p": p, "x": x, **st} for p, x, st in rows], open(f"data/z52b/pass2/NC0/sub/Z1197_widths_{pmax}.json", "w"))
