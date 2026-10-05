"""R48d from-scratch toy end-to-end check of POINTWISE_OMEGA13 Thm 3.4 / §5 (square-class quarantine).

Toy parameters (Lemma 1.1 needs beta<=e^{1/3}; the twist needs eta<=0.19):
  T small, beta fixed (default 1.25, eta=0.75*log beta=0.167), eligible primes ell<=Y.
For each random realisation of the square-class process we check:
  * no atom is deterministic (Lemma 3.1), r mod 840 is a unit square (Mordell class), r=1 mod 24;
  * (1.1) at all coordinates <=Y (stopping rule) and record late violations (ell>Y);
  * S_res, log Q;
and for one good realisation, by sampling n=r (Q) coprime to all ell<=T:
  * F(n) (avoid all live fibre events) == [W(n)>T] (property (I)), W computed from the definition;
  * empirical delta >= exp(-(4/3) S_res) (Lemma 1.1);
  * twist: |E[F psi]| <= eta*E[F'] for psi = Legendre mod ell_0, ell_0 not | Q (I1(b)).
Usage: review_o13d_toy.py T Y reps samples seed
"""
import math
import random
import sys
from collections import defaultdict


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors(n):
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def atoms(T):
    out = []
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        fM = factor(M)
        for D in divisors(A * A):
            out.append((M, D, fM))
    return out


def is_sq_mod_p(x, p):
    x %= p
    return x != 0 and pow(x, (p - 1) // 2, p) == 1


class State:
    def __init__(self, T, primes):
        self.T = T
        self.a = {l: 0 for l in primes if l > 2}
        self.f = {l: int(math.floor(math.log(T) / math.log(l) + 1e-12)) for l in self.a}
        self.r = {l: 0 for l in self.a}  # r mod l^a

    def mu(self, M, D, fM):
        """fibre probability of n = -4D (mod M); also returns support."""
        p = 1.0
        supp = []
        for l, v in fM.items():
            a = self.a[l]
            t = (-4 * D) % (l ** v)
            if v <= a:
                if self.r[l] % (l ** v) != t:
                    return 0.0, None
            else:
                supp.append(l)
                if a == 0:
                    p /= (l - 1) * l ** (v - 1)
                else:
                    if self.r[l] % (l ** a) != t % (l ** a):
                        return 0.0, None
                    p /= l ** (v - a)
        return p, supp

    def step(self, l, rng):
        a = self.a[l]
        if a == 0:
            sq = [x for x in range(1, l) if is_sq_mod_p(x, l)]
            self.r[l] = rng.choice(sq)
        else:
            self.r[l] = self.r[l] + (l ** a) * rng.randrange(l)
        self.a[l] = a + 1


def run_process(T, Y, beta, AT, rng, primes):
    eta = 0.75 * math.log(beta)
    st = State(T, primes)
    for l in (3, 5, 7):
        st.step(l, rng)
    nsteps = 0
    while True:
        w = defaultdict(float)
        for (M, D, fM) in AT:
            p, supp = st.mu(M, D, fM)
            if p > 0:
                assert supp, ("deterministic atom", M, D)
                x = beta ** len(supp) * p
                for l in supp:
                    w[l] += x
        cand = [l for l in st.a if l <= Y and st.a[l] < st.f[l] and w[l] > eta]
        if not cand:
            break
        st.step(max(cand, key=lambda l: w[l]), rng)
        nsteps += 1
    S = 0.0
    for (M, D, fM) in AT:
        p, supp = st.mu(M, D, fM)
        if p > 0:
            S += beta ** len(supp) * p
    late = [l for l in w if l > Y and w[l] > eta]
    Q = 8
    for l in st.a:
        Q *= l ** st.a[l]
    # CRT r mod Q
    r = 1  # mod 8
    m = 8
    for l in st.a:
        if st.a[l]:
            q = l ** st.a[l]
            # solve x=r (m), x=st.r[l] (q)
            k = ((st.r[l] - r) * pow(m, -1, q)) % q
            r = r + m * k
            m *= q
    r %= Q
    return st, w, S, late, Q, r, nsteps, eta


def main():
    T, Y, reps, samples, seed = (int(x) for x in sys.argv[1:6])
    beta = 1.25
    rng = random.Random(seed)
    primes = primes_upto(T)
    AT = atoms(T)
    msq = {x * x % 840 for x in range(840) if math.gcd(x, 840) == 1}
    assert msq == {1, 121, 169, 289, 361, 529}, msq
    print(f"T={T} Y={Y} beta={beta} atoms={len(AT)} unit squares mod 840 = {sorted(msq)}")
    good = None
    nlate = 0
    for rep in range(reps):
        st, w, S, late, Q, r, ns, eta = run_process(T, Y, beta, AT, rng, primes)
        assert Q % 840 == 0 and r % 840 in msq and r % 24 == 1
        if late:
            nlate += 1
        print(f"rep {rep}: steps={ns} logQ={math.log(Q):.1f} S_res={S:.3f} maxw<=Y="
              f"{max([w[l] for l in w if l <= Y] or [0]):.3f} late={late}")
        if not late and good is None:
            good = (st, w, S, Q, r, eta)
    print(f"late-violation frequency {nlate}/{reps}")
    if good is None:
        return
    st, w, S, Q, r, eta = good
    # sampling check
    R = {M: {(-4 * D) % M for D in divisors(((M + 1) // 4) ** 2)} for M in range(3, T + 1, 4)}
    live = []
    for (M, D, fM) in AT:
        p, supp = st.mu(M, D, fM)
        if p > 0:
            mod = 1
            for l in supp:
                mod *= l ** fM[l]
            live.append((mod, (-4 * D) % mod, supp))
    small = [l for l in primes if l > 2]
    l0 = max((l for l in small if st.a[l] == 0), key=lambda l: w.get(l, 0))
    nF = nFp = 0
    sF_psi = 0
    mism = 0
    tot = 0
    while tot < samples:
        n = r + Q * rng.randrange(1, 10 ** 12)
        if any(n % l == 0 for l in small):
            continue
        tot += 1
        W_gt = all(n % M not in R[M] for M in R)
        F = all(n % mod != t for (mod, t, supp) in live)
        Fp = all(n % mod != t for (mod, t, supp) in live if l0 not in supp)
        mism += (W_gt != F)
        nF += F
        nFp += Fp
        sF_psi += F * (1 if is_sq_mod_p(n, l0) else -1)
    d = nF / tot
    print(f"good realisation: logQ={math.log(Q):.1f} S_res={S:.3f} LLL bound exp(-4/3 S)={math.exp(-4/3*S):.4f}")
    print(f"sampled delta={d:.4f} (n={tot}); property (I) mismatches={mism}")
    print(f"twist at l0={l0}: |E[F psi]|={abs(sF_psi)/tot:.4f}, eta*E F'={eta*nFp/tot:.4f}, w~_l0={w[l0]:.4f}, "
          f"sd~{1/math.sqrt(tot):.4f}")


if __name__ == "__main__":
    main()
