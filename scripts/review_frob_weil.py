"""R196 from-scratch checks of FROBENIUS_FIRING §2.
(1) Thm 2.1: |N_m - (q^d - r)/m| <= (n + b - 1) q^{d/2}, brute force over F_{q^d} (own arithmetic, q prime).
(2) Prop 2.2: the expansion inequality for random sets S (exact Fourier coefficients via discrete logs + FFT).
(3) Prop 2.2 examples: ||s^||_1 of exponent intervals and of 2-dim GAPs {g^(e1 + K e2)} in Z/N vs the claimed
    O(prod(1 + log(2 kappa + 1))).
(4) Prop 2.3: tau_3(N) <= 3^{deg N} on all monic N of small degree (q = 3), and the q >= 9 comparison.
"""
import itertools, random, math
import numpy as np

random.seed(1960)


# ---- F_q[T] helpers (coefficient lists, low degree first) ----
def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def pmod(a, m, q):
    a = trim(a); m = trim(m); inv = pow(m[-1], q - 2, q)
    while len(a) >= len(m):
        c = a[-1] * inv % q; sh = len(a) - len(m)
        for i, mi in enumerate(m):
            a[sh + i] = (a[sh + i] - c * mi) % q
        a = trim(a)
    return a


def pmul(a, b, q):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % q
    return trim(r)


def is_irred(f, q):
    d = len(f) - 1
    # brute: no monic factor of degree <= d//2
    for e in range(1, d // 2 + 1):
        for co in itertools.product(range(q), repeat=e):
            g = list(co) + [1]
            if not pmod(f, g, q):
                return False
    return True


def rand_monic_irred(deg, q):
    while True:
        f = [random.randrange(q) for _ in range(deg)] + [1]
        if is_irred(f, q):
            return f


class GF:
    def __init__(self, q, d):
        self.q, self.d = q, d
        self.mod = rand_monic_irred(d, q) if d > 1 else [0, 1]
        self.size = q ** d
        self.elems = [tuple(c) for c in itertools.product(range(q), repeat=d)]
        self.idx = {e: i for i, e in enumerate(self.elems)}
        # find generator and discrete log table
        N = self.size - 1
        for g in self.elems:
            if not any(g):
                continue
            x = (1,) + (0,) * (d - 1); log = {}
            for k in range(N):
                if x in log:
                    break
                log[x] = k; x = self.mul(x, g)
            if len(log) == N:
                self.log = log; break

    def mul(self, a, b):
        r = pmod(pmul(trim(a), trim(b), self.q), self.mod, self.q)
        return tuple(r + [0] * (self.d - len(r)))

    def ev(self, poly, a):  # Horner, poly low-first over F_q
        r = (0,) * self.d
        for c in reversed(poly):
            r = self.mul(r, a)
            r = tuple(((r[0] + c) % self.q,) + r[1:])
        return r


def check_thm21(q, d, n, b, trials=4):
    K = GF(q, d); N = K.size - 1; worst = 0.0; viol = 0
    for _ in range(trials):
        P = rand_monic_irred(n, q)
        while True:
            B = [random.randrange(q) for _ in range(b)] + [1]
            if pmod(B, P, q) or b == 0:
                break
        vals = []
        for a in K.elems:
            pa = K.ev(P, a); ba = K.ev(B, a)
            vals.append(None if (not any(pa) or not any(ba)) else (K.log[pa] - K.log[ba]) % N)
        r = sum(v is None for v in vals)
        for m in [x for x in range(2, N + 1) if N % x == 0]:
            Nm = sum(1 for v in vals if v is not None and v % m == 0)
            dev = abs(Nm - (K.size - r) / m); bound = (n + b - 1) * K.size ** 0.5
            worst = max(worst, dev / bound if bound else (0 if dev < 1e-9 else float('inf')))
            if dev > bound + 1e-9:
                viol += 1
    return worst, viol


def check_prop22(q, d, n, b, trials=3):
    K = GF(q, d); N = K.size - 1; worst = 0.0; viol = 0
    for _ in range(trials):
        P = rand_monic_irred(n, q); B = [random.randrange(q) for _ in range(b)] + [1]
        if b and not pmod(B, P, q):
            continue
        cnt = np.zeros(N)  # histogram of discrete logs of P/B
        r = 0
        for a in K.elems:
            pa = K.ev(P, a); ba = K.ev(B, a)
            if not any(pa) or not any(ba):
                r += 1; continue
            cnt[(K.log[pa] - K.log[ba]) % N] += 1
        for size in (1, 3, N // 10 + 1, N // 3, N // 2):
            Sset = random.sample(range(N), size)
            ind = np.zeros(N); ind[Sset] = 1
            shat = np.fft.fft(ind) / N           # coefficients of 1_S in characters chi_k(g^j) = e(jk/N)
            l1 = np.abs(shat).sum(); s1 = shat[0].real
            actual = cnt[Sset].sum(); main = size * (K.size - r) / N
            bound = (l1 - s1) * (n + b - 1) * K.size ** 0.5
            worst = max(worst, abs(actual - main) / bound if bound else 0)
            if abs(actual - main) > bound + 1e-6:
                viol += 1
    return worst, viol


def l1_interval(N, J, step=2):
    ind = np.zeros(N)
    for j in range(J):
        ind[(step * j) % N] = 1
    return np.abs(np.fft.fft(ind) / N).sum()


def l1_gap(N, K, k1, k2):
    ind = np.zeros(N); pts = set()
    for e1 in range(-k1, k1 + 1):
        for e2 in range(-k2, k2 + 1):
            pts.add((e1 + K * e2) % N)
    proper = len(pts) == (2 * k1 + 1) * (2 * k2 + 1)
    ind[list(pts)] = 1
    return np.abs(np.fft.fft(ind) / N).sum(), proper


def tau3(exps):
    return math.prod((e + 1) * (e + 2) // 2 for e in exps)


def main():
    print("(1) Thm 2.1 worst |dev|/bound, violations:")
    for (q, d, n, b) in [(3, 4, 2, 1), (3, 5, 3, 1), (3, 6, 2, 2), (5, 3, 2, 1), (5, 4, 3, 1), (7, 3, 2, 1), (7, 3, 4, 2), (2, 8, 3, 1)]:
        print(f"   q={q} d={d} n={n} b={b}:", check_thm21(q, d, n, b))
    print("(2) Prop 2.2 worst |dev|/bound, violations:")
    for (q, d, n, b) in [(3, 5, 2, 1), (5, 4, 3, 1), (7, 3, 2, 1)]:
        print(f"   q={q} d={d} n={n} b={b}:", check_prop22(q, d, n, b))
    print("(3a) exponent interval {s^{2j}: j<J} in Z/N: ||s^||_1 vs log N")
    for N in (3 ** 8 - 1, 5 ** 6 - 1, 7 ** 5 - 1):
        print("   N", N, [(J, round(l1_interval(N, J), 2)) for J in (10, 100, N // 7, N // 2 - 1)], "logN", round(math.log(N), 2))
    print("(3b) 2-dim GAPs {g^(e1+K e2)}: max ||s^||_1 / prod(1+log(2k+1)) over K (proper only)")
    N = 3 ** 9 - 1
    for (k1, k2) in [(5, 5), (20, 10), (50, 50), (3, 200)]:
        worst = 0; wK = None
        for K in random.sample(range(2, N), 600):
            l1, pr = l1_gap(N, K, k1, k2)
            if pr:
                ratio = l1 / ((1 + math.log(2 * k1 + 1)) * (1 + math.log(2 * k2 + 1)))
                if ratio > worst:
                    worst, wK = ratio, K
        print(f"   N={N} k=({k1},{k2}): worst ratio {worst:.3f} at K={wK}")
    print("(4) Prop 2.3: tau3 <= 3^Omega <= 3^D (combinatorial identity C(e+2,2) <= 3^e):",
          all((e + 1) * (e + 2) // 2 <= 3 ** e for e in range(60)))
    # q >= 9 comparison: tau3 <= 3^{d-k} <= q^{(d-k)/2} < (n+k-1) q^{d/2} / 2 for n + k >= 3
    bad = [(q, k, n, d) for q in (9, 11, 13, 16, 25) for k in range(1, 5) for n in range(1, 8) if n + k >= 3
           for d in range(k, 30) if not 3 ** (d - k) < (n + k - 1) * q ** (d / 2) / 2]
    print("   q>=9 comparison failures:", bad[:5], len(bad))


if __name__ == '__main__':
    main()
