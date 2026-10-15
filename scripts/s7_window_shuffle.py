"""s7_window_shuffle: are cap-0 window failures independent across windows beyond congruences?
Conditional permutation test. For each prime p ≡ 1 (4) ≤ N and window m ≤ MW (m ≡ 3 mod 4), split K_m = (p+m)/4 = S·R
(S = part on primes ≤ B, R = rough part). Within groups (block of BS consecutive primes, m, R mod m, bit length of R) permute R among
primes; fake K' = S·R' keeps K' ≡ K (mod m) and the whole small-prime (congruence / Haar-CRT) structure of p, but
makes the rough parts of different windows independent. Compare tail counts #(m0 > M) actual vs shuffled.
Usage: python s7_window_shuffle.py N [B] [reps]
"""
import sys, random, math, collections
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from s7_window_excess import spf_sieve, factor

def fires_f(fac, K, m):
    target = (-K) % m
    S = {1 % m}
    if target in S:
        return True
    for s, b in fac.items():
        r = s % m; pw = {1}; x = 1
        for _ in range(2 * b):
            x = x * r % m; pw.add(x)
        S = {u * v % m for u in S for v in pw}
        if target in S:
            return True
    return False

if __name__ == "__main__":
    N = int(sys.argv[1]); B = int(sys.argv[2]) if len(sys.argv) > 2 else 13
    reps = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    MW = 63; BS = 2000
    spf = spf_sieve(N // 4 + MW + 10)
    isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = bytearray(len(isp[i * i::i]))
    primes = [p for p in range(5, N + 1, 4) if isp[p]]
    wins = list(range(3, MW + 1, 4))
    # per prime per window: (S_fac, S, R_fac, R)
    split = {}
    for i, p in enumerate(primes):
        for m in wins:
            if math.gcd(m, p) != 1:
                continue
            K = (p + m) // 4; f = factor(K, spf)
            Sf = {s: e for s, e in f.items() if s <= B}; Rf = {s: e for s, e in f.items() if s > B}
            S = 1
            for s, e in Sf.items():
                S *= s ** e
            split[(i, m)] = (Sf, S, Rf, K // S)

    def m0_of(getter):
        out = []
        for i, p in enumerate(primes):
            v = None
            for m in wins:
                if (i, m) not in split:
                    continue
                Sf, S, Rf, R = getter(i, m)
                fac = dict(Sf); fac.update(Rf)
                if fires_f(fac, S * R, m):
                    v = m; break
            out.append(v)
        return out

    def tails(ms):
        return [sum(1 for v in ms if v is None or v > M) for M in (3, 7, 11, 19, 27, 35, 47)]
    act = m0_of(lambda i, m: split[(i, m)])
    print("N", N, "B", B, "primes", len(primes))
    print("M =        ", (3, 7, 11, 19, 27, 35, 47))
    print("actual     ", tails(act))
    rng = random.Random(1)
    for rep in range(reps):
        groups = collections.defaultdict(list)
        for (i, m), (Sf, S, Rf, R) in split.items():
            groups[(i // BS, m, R % m, R.bit_length())].append(i)
        perm = {}
        for g, idx in groups.items():
            sh = idx[:]; rng.shuffle(sh)
            for a, b in zip(idx, sh):
                perm[(a, g[1])] = b
        def getter(i, m):
            Sf, S, _, _ = split[(i, m)]
            _, _, Rf, R = split[(perm[(i, m)], m)]
            return Sf, S, Rf, R
        print("shuffled %d " % rep, tails(m0_of(getter)))
