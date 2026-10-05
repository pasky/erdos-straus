"""R38b: exact checks of Cor 4.1 (energy(t) <= 2^{-(t+1)/k}) and of the stronger
C-1 (G_F(2^{1/k}) <= 1) for structured width-k DNFs on uniform bits, n<=16."""
import itertools, sys, numpy as np
from review_o10b_lib import bad_indicator, level_weights, tail_ratio

def check(name, n, events):
    k = max(len(e) for e in events)
    h = bad_indicator((2,) * n, events)
    lw = level_weights(1 - h, [np.array([.5, .5])] * n)
    G = sum(lw[d] * 2 ** (d / k) for d in range(n + 1))
    r, t = tail_ratio(lw, k)
    print(f"{name:40s} n={n:2d} k={k} m={len(events):5d} P(h)={h.mean():.4f} G={G:.6f} tailratio={r:.4f}@t={t}")
    return G, r

res = []
# tribes
for w in range(1, 6):
    for s in range(1, 16 // w + 1):
        n = w * s
        ev = [{b * w + i: 1 for i in range(w)} for b in range(s)]
        res.append(check(f"tribes w={w} s={s}", n, ev))
# threshold >=k ones (OR of all k-ANDs)
for n in (8, 12, 14):
    for k in range(1, 7):
        ev = [{v: 1 for v in S} for S in itertools.combinations(range(n), k)]
        res.append(check(f"thr>= {k} ones", n, ev))
# majority-like: >=k ones OR >=k zeros
for n in (9, 12):
    for k in range(2, 7):
        ev = [{v: c for v in S} for S in itertools.combinations(range(n), k) for c in (0, 1)]
        res.append(check(f"thr ones|zeros k={k}", n, ev))
# OR of disjoint k-parities (DNF of 2^{k-1} width-k terms each)
for k in range(1, 6):
    for s in range(1, 16 // k + 1):
        ev = []
        for b in range(s):
            for bits in itertools.product([0, 1], repeat=k):
                if sum(bits) % 2 == 1:
                    ev.append({b * k + i: bits[i] for i in range(k)})
        res.append(check(f"OR of {s} parities_{k}", k * s, ev))
# parity of n bits as DNF (k=n)
for n in range(2, 13):
    ev = [{i: b[i] for i in range(n)} for b in itertools.product([0, 1], repeat=n) if sum(b) % 2]
    res.append(check(f"parity_{n}", n, ev))
# majority n odd, width (n+1)/2
for n in (3, 5, 7, 9, 11, 13, 15):
    k = (n + 1) // 2
    ev = [{v: 1 for v in S} for S in itertools.combinations(range(n), k)]
    res.append(check(f"majority", n, ev))
# multiplexer / addressing: a address bits, 2^a data bits
for a in (1, 2, 3):
    n = a + 2 ** a
    ev = [{**{i: b[i] for i in range(a)}, a + int(''.join(map(str, b)), 2): 1}
          for b in itertools.product([0, 1], repeat=a)]
    res.append(check(f"multiplexer a={a}", n, ev))
# sunflower / overlapping: common core of size c, petals
for c in (1, 2, 3):
    for p in (1, 2):
        petals = (16 - c) // p
        ev = [{**{i: 1 for i in range(c)}, **{c + j * p + i: 1 for i in range(p)}} for j in range(petals)]
        res.append(check(f"sunflower core={c} petal={p}", c + petals * p, ev))
print("MAX G", max(g for g, r in res), "MAX tailratio", max(r for g, r in res))
