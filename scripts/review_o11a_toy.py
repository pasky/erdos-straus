"""R44a: exact-Haar toy graded systems (from scratch).

Coordinates X_l = n mod l^f_l on the fibre n=1 mod l^a_l (units if a=0), l in {3,5,7,11}.
Events fix X_l mod l^v (v>a_l) on their support, value consistent with the fibre.
Checks by full enumeration of the product of fibres:
  (1) fibre probabilities = 1/phi(l^v) (a=0) or l^{-(v-a)} (a>=1)  [Lemma 2.1];
  (2) if every event has sum_{l in supp} w_l <= c (c<=1/8), then
      P(no event) >= prod(1-2P(E)) >= exp(-(8/3) sum P(E))   [LLL as used in Lemma 2.2];
  (3) via CRT, the coordinates are independent and fibre-uniform on {n mod N: n=1 (Q)}
      (checked on small instances by enumerating n mod N directly).
Usage: review_o11a_toy.py ntrials seed
"""
import itertools, math, random, sys

PR = [3, 5, 7, 11]


def fibre(l, f, a):
    m = l ** f
    if a == 0:
        return [x for x in range(m) if x % l]
    return [x for x in range(m) if (x - 1) % (l ** a) == 0]


def trial(rng, c):
    k = rng.randint(1, 3)
    prs = rng.sample(PR, k)
    f = {l: rng.randint(1, 3 if l <= 5 else 2) for l in prs}
    a = {l: rng.randint(0, f[l] - 1) for l in prs}
    fib = {l: fibre(l, f[l], a[l]) for l in prs}
    # (1) fibre probabilities
    for l in prs:
        for v in range(a[l] + 1, f[l] + 1):
            r = rng.choice(fib[l]) % l ** v
            p = sum(1 for x in fib[l] if x % l ** v == r) / len(fib[l])
            pred = 1 / (l ** (v - 1) * (l - 1)) if a[l] == 0 else l ** (-(v - a[l]))
            assert abs(p - pred) < 1e-12
    ev = []
    for _ in range(rng.randint(1, 8)):
        s = rng.sample(prs, rng.randint(1, k))
        e = []
        for l in s:
            v = rng.randint(a[l] + 1, f[l])
            e.append((l, v, rng.choice(fib[l]) % l ** v))
        ev.append(e)

    def P(e):
        p = 1.0
        for l, v, r in e:
            p *= sum(1 for x in fib[l] if x % l ** v == r) / len(fib[l])
        return p

    Ps = [P(e) for e in ev]
    w = {l: sum(p for e, p in zip(ev, Ps) if any(x[0] == l for x in e)) for l in prs}
    if max(sum(w[x[0]] for x in e) for e in ev) > c:
        return None
    tot = 0
    good = 0
    for pt in itertools.product(*(fib[l] for l in prs)):
        X = dict(zip(prs, pt))
        tot += 1
        if not any(all(X[l] % l ** v == r for l, v, r in e) for e in ev):
            good += 1
    pn = good / tot
    lb = math.prod(1 - 2 * p for p in Ps)
    lb2 = math.exp(-8 / 3 * sum(Ps))
    assert pn >= lb - 1e-12 and lb >= lb2 - 1e-12, (pn, lb, lb2)
    return pn, lb


def crt_check(rng):
    # Q = 8*prod l^a, coordinates mod l^f; enumerate n mod N=lcm(8,prod l^f), n=1 (Q), gcd(n,N)=1
    prs = [3, 5]
    f = {3: 2, 5: 2}
    a = {3: rng.randint(0, 2), 5: rng.randint(0, 2)}
    Q = 8 * 3 ** a[3] * 5 ** a[5]
    N = 8 * 9 * 25
    cnt = {}
    for n in range(1, N, Q):
        if math.gcd(n, N) != 1:
            continue
        key = (n % 9, n % 25)
        cnt[key] = cnt.get(key, 0) + 1
    fib = [fibre(3, 2, a[3]) if a[3] < 2 else [1], fibre(5, 2, a[5]) if a[5] < 2 else [1]]
    assert set(cnt) == set(itertools.product(*fib)) and len(set(cnt.values())) == 1


if __name__ == "__main__":
    nt, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    for _ in range(50):
        crt_check(rng)
    done = 0
    worst = 9.0
    for _ in range(nt):
        r = trial(rng, 0.125)
        if r:
            done += 1
            worst = min(worst, r[0] / r[1])
    print(f"CRT/fibre-uniformity: 50 OK; LLL toy systems meeting the hypothesis: {done}, "
          f"min P(no event)/prod(1-2P) = {worst:.4f} (>=1 required)")
