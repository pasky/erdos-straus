"""R97 from-scratch numerical checks of the elementary lemmas of paper/es-mn-short-note.tex.

(1) harmonic remainder: |sum_{i<=y} 1/i - log y - gamma| <= 1/y for real y >= 1 (Lemma hm(a) proof);
(2) Lemma hm (a)-(d) for many m, K up to 2e5 (incl. primorial / highly composite m);
(3) Lemma smooth (b),(c): smooth-divisor chain and Rankin bound, exact sums for small y;
(4) Lemma localmean + Lemma indep: exact identity on random windows for a random signed class combo;
(5) Cor D algebra: monotonicity threshold, f(L0) bound, sqrt2*log(N/2) >= log N for N >= 16;
(6) eq:ratio: phi(m) loglog(3m)/m bounded below (so the displayed >> is absolute), m <= 2e6.
EVIDENCE only; independent of the author's scripts.
"""
import math, random
from fractions import Fraction

random.seed(970)
G = 0.5772156649015329


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def phi_table(n):
    ph = list(range(n + 1))
    for p in range(2, n + 1):
        if ph[p] == p:
            for j in range(p, n + 1, p):
                ph[j] -= ph[j] // p
    return ph


def check_harmonic():
    worst = 0.0
    Hn = 0.0
    for n in range(1, 20001):
        Hn += 1.0 / n
        for frac in (0.0, 0.25, 0.5, 0.75, 0.999999):
            y = n + frac
            worst = max(worst, abs(Hn - math.log(y) - G) * y)
    return worst


def check_hm(PH):
    KMAX = 200000
    ms = list(range(4, 61)) + [210, 2310, 30030, 720720 // 1, 5040, 9699690]
    out = []
    for m in ms:
        rad = [p for p in primes_upto(max(m, 2)) if m % p == 0]
        phim = m
        for p in rad:
            phim = phim // p * (p - 1)
        cop = bytearray([1]) * (KMAX + 1)
        for p in rad:
            cop[p::p] = bytearray(len(cop[p::p]))
        S = [0.0] * (KMAX + 1)
        h = [0.0] * (KMAX + 1)
        for j in range(1, KMAX + 1):
            S[j] = S[j - 1] + (1.0 / j if cop[j] else 0.0)
            h[j] = h[j - 1] + (PH[j] / j / j if cop[j] else 0.0)
        fa = fb = 0
        rmin, rmax, hr = 9, 0, 9
        for K in list(range(2, KMAX + 1, 997)) + [KMAX]:
            if K >= m * m and S[K] < phim / m * math.log(K):
                fa += 1
            if h[K] < 0.54 * S[K]:
                fb += 1
            if K >= max(m, 3):
                r = S[K] / (phim / m * math.log(K))
                rmin, rmax = min(rmin, r), max(rmax, r)
            hr = min(hr, h[K] / S[K])
        # (c) for a few primes p not dividing m
        fc = 0
        for p in [2, 3, 5, 7, 11, 101, 997]:
            if m % p == 0:
                continue
            for K in [1000, 50000, KMAX]:
                lhs = sum(PH[k] / k / k for k in range(p, K + 1, p) if cop[k])
                if lhs > S[K] / p + 1e-12:
                    fc += 1
        out.append((m, fa, fb, fc, round(rmin, 3), round(rmax, 3), round(hr, 3)))
    return out


def smooth_numbers(y, limit):
    P = [p for p in primes_upto(y)]
    res = [1]
    for p in P:
        new = []
        for d in res:
            x = d
            while x <= limit:
                new.append(x)
                x *= p
        res = new
    return sorted(res)


def check_rankin():
    rows = []
    for y in [2, 3, 5, 7, 11, 13]:
        sm = smooth_numbers(y, 10 ** 13)
        for D0 in [10, 1e3, 1e5, 1e7]:
            tail = sum(1.0 / d for d in sm if d > D0)  # truncated at 1e13: lower bound for tail
            bound = D0 ** -0.5 * math.exp(4 * math.sqrt(y))
            prod = D0 ** -0.5
            for p in primes_upto(y):
                prod /= (1 - p ** -0.5)
            rows.append((y, D0, tail, prod, bound, tail <= prod <= bound))
    # (b): every smooth d > D0 has a smooth divisor in (D0, y D0]
    bad = 0
    for y in [3, 7, 13]:
        sm = smooth_numbers(y, 10 ** 7)
        sset = set(sm)
        for D0 in [5, 50, 500]:
            for d in sm:
                if d > D0:
                    ok = any(d % e == 0 for e in sm if D0 < e <= y * D0)
                    bad += not ok
    return rows, bad


def check_localmean():
    # random signed combination of classes with moduli dividing Mm
    Mm = 2 * 3 * 5 * 7 * 4 * 11
    divs = [q for q in range(1, Mm + 1) if Mm % q == 0]
    worst = 0.0
    for trial in range(40):
        terms = [(random.choice([-1, 1, 2]), random.randrange(0, 10 ** 6), random.choice(divs)) for _ in range(12)]
        nu = [sum(e for e, a, q in terms if (n - a) % q == 0) for n in range(Mm)]
        T = sum(abs(e) for e, a, q in terms)
        for _ in range(25):
            Q = random.choice([1, 13, 17 * 13, 6, 77, 4 * 13])
            beta = random.randrange(0, 1000)
            L = Mm * Q // math.gcd(Mm, Q)
            mean = Fraction(sum(nu[n % Mm] for n in range(L) if (n - beta) % Q == 0), L)
            z = Fraction(random.randrange(-10 ** 6, 10 ** 6), random.randrange(1, 50))
            H = Fraction(random.randrange(1, 40000), random.randrange(1, 7))
            lo = math.floor(z) + 1
            hi = math.floor(z + H)
            S = sum(nu[n % Mm] for n in range(lo, hi + 1) if (n - beta) % Q == 0)
            theta = (S - H * mean) / T
            worst = max(worst, abs(float(theta)))
    # Lemma indep: Q2 coprime to Mm, nu >= 0
    nu = [random.randrange(0, 5) for _ in range(Mm)]
    viol = 0
    for Q1, Q2 in [(4, 13), (6, 17 * 13), (1, 19), (35, 23)]:
        Q = Q1 * Q2
        L = Mm * Q // math.gcd(Mm, Q)
        En = Fraction(sum(nu), Mm)
        for beta in range(0, 60, 7):
            lhs = Fraction(sum(nu[n % Mm] for n in range(L) if (n - beta) % Q == 0), L)
            if lhs > En / Q2:
                viol += 1
    return worst, viol


def check_corD():
    out = []
    for c in [0.01, 0.1, 1.0]:
        for C in [10.0, 1e6]:
            A0 = (8 / (3 * c)) ** (4 / 3) * math.log(4) ** (-4 / 3)
            A = A0
            while c * A ** 0.75 - 10 / 3 - 2 * math.log(A) / math.log(4) < math.log(2 * C) / math.log(4):
                A *= 1.05
            worst = 1e9
            for m in [4, 5, 10, 100, 10 ** 4, 10 ** 8, 10 ** 15]:
                L0 = A * m ** (1 / 3) * math.log(m) ** (4 / 3)
                for L in [L0, 1.5 * L0, 10 * L0, 1e3 * L0]:
                    f = c * L ** 0.75 * m ** -0.25 - 2 * math.log(L)
                    worst = min(worst, f - math.log(2 * C))
            out.append((c, C, round(A, 2), worst >= 0))
    # sqrt2 log(N/2) >= log N threshold
    N = 2.0
    while math.sqrt(2) * math.log(N / 2) < math.log(N):
        N += 0.01
    return out, N


def check_ratio(PH, MMAX):
    best = 9
    arg = None
    for m in range(4, MMAX + 1):
        v = PH[m] * math.log(math.log(3 * m)) / m
        if v < best:
            best, arg = v, m
    return best, arg


def main():
    print("harmonic remainder max |theta_y| (need <= 1):", round(check_harmonic(), 4))
    MM = 2_000_000
    PH = phi_table(MM)
    print("hm lemma: (m, fails a, fails b, fails c, min/max S/((phi/m)logK), min h/S)")
    for row in check_hm(PH):
        print("  ", row)
    rows, bad = check_rankin()
    print("Rankin rows (y, D0, tail, euler-bound, e^{4sqrt y}-bound, ok):")
    for r in rows:
        print("  ", r[0], r[1], f"{r[2]:.3g} {r[3]:.3g} {r[4]:.3g}", r[5])
    print("smooth (b) failures:", bad)
    w, v = check_localmean()
    print("localmean max |theta| (need <= 1):", round(w, 4), " indep violations:", v)
    out, N = check_corD()
    print("Cor D (c, C, A, f(L)>=log 2C on grid):", out, " sqrt2 log(N/2)>=log N from N ~", round(N, 2))
    print("min phi(m) loglog(3m)/m over 4<=m<=2e6:", check_ratio(PH, MM))


if __name__ == "__main__":
    main()
