"""R38b: lower-bound family showing Cor 4.1's exponential rate 2^{-1/k} is SHARP over
general product spaces: m disjoint width-k events, each coordinate's fixed value having
probability p (p=1/q: q-ary uniform; p small: p-biased bits; p=1/2: tribes-like AND).
Exact level weights via the block polynomial
   B(z) = (1-pi)^2 + pi^2 ((1+z(1-p)/p)^k - 1),  pi=p^k,   F=prod(1-A_i)  =>  sum_d w_d z^d = B(z)^m.
Prints max_m energy(F; t) * 2^{(t+1)/k} at t = jk-1, and its ratio to 1/sqrt(2 pi j)."""
import math, numpy as np
def energy_tail(k, p, m, t):
    pi = p ** k
    B = np.array([(1 - pi) ** 2] + [pi ** 2 * math.comb(k, d) * ((1 - p) / p) ** d for d in range(1, k + 1)])
    # B^m truncated to degree t, by binary powering
    def mul(a, b):
        return np.convolve(a, b)[: t + 1]
    res, base, e = np.array([1.0]), B[: t + 1].copy(), m
    while e:
        if e & 1: res = mul(res, base)
        base = mul(base, base); e >>= 1
    total = B.sum() ** m  # = E[F^2] = E[F] = (1-pi)^m
    return total - res.sum()
for k in (1, 2, 3):
    for p in (0.5, 0.1, 1e-2, 1e-3):
        out = []
        for j in (2, 5, 10, 20, 30):
            t = j * k - 1
            pi = p ** k
            ms = sorted({max(1, int(x)) for x in np.geomspace(1, 50 * j / pi, 400)})
            best = max(energy_tail(k, p, m, t) * 2 ** ((t + 1) / k) for m in ms)
            out.append(f"j={j}: {best:.4f} (x sqrt(2pi j)={best*math.sqrt(2*math.pi*j):.3f})")
        print(f"k={k} p={p:g}: " + "; ".join(out), flush=True)
