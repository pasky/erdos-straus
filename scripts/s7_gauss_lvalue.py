"""s7_gauss_lvalue: (a) Gaussian square windows: for p = a^2 + b^2 (a odd, b even), the windows
m = 2(±a)(±b) + 2(±a) + 2(±b) + 1 > 0 give K = ((±a ± b + 1)/2)^2, a forced square (budget doubled); test cap-0 rates
against ordinary windows of the same size. (b) L-value proxy: Spearman correlation of m0(p) with
P(p) = prod_{l <= 200} (1 - (p/l)/l)^{-1} (a proxy for L(1, chi_p)), overall and inside the Mordell-hard classes.
Usage: python s7_gauss_lvalue.py N
"""
import sys, math, random
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from s7_window_excess import spf_sieve, fires, m0, legendre

def two_squares(p):
    # Cornacchia-free: find x with x^2 ≡ -1, then Euclid
    for c in range(2, p):
        if pow(c, (p - 1) // 2, p) == p - 1:
            x = pow(c, (p - 1) // 4, p); break
    a, b = p, x
    while b * b > p:
        a, b = b, a % b
    c = math.isqrt(p - b * b)
    return (b, c) if b % 2 else (c, b)

def rank(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v)
    for k, i in enumerate(o): r[i] = k
    return r

def spearman(x, y):
    rx, ry = rank(x), rank(y); n = len(x)
    mx = sum(rx) / n; my = sum(ry) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    return cov / math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))

if __name__ == "__main__":
    N = int(sys.argv[1]); rng = random.Random(1)
    spf = spf_sieve(N + 10)
    isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]: isp[i * i::i] = bytearray(len(isp[i * i::i]))
    smallp = [l for l in range(3, 200) if isp[l]]
    MH = {1, 121, 169, 289, 361, 529}
    g_tot = g_fire = c_tot = c_fire = 0; M0 = []; PP = []; MHi = []
    for p in range(5, N + 1, 4):
        if not isp[p]: continue
        a, b = two_squares(p)
        for sa in (1, -1):
            for sb in (1, -1):
                A, B = sa * a, sb * b
                m = 2 * A * B + 2 * A + 2 * B + 1
                S2 = (A + B + 1)
                if m <= 0 or m % 4 != 3 or S2 % 2 or math.gcd(m, p) != 1: continue
                K = (S2 // 2) ** 2
                assert 4 * K == p + m
                g_tot += 1; g_fire += fires(K, m, spf) if K < len(spf) else 0
                mc = m + 4 * rng.randrange(-3, 4)   # control: ordinary window of similar size
                if mc > 0 and math.gcd(mc, p) == 1 and (p + mc) // 4 < len(spf):
                    c_tot += 1; c_fire += fires((p + mc) // 4, mc, spf)
        v = m0(p, spf, 4000)
        P = 1.0
        for l in smallp: P /= (1 - legendre(p, l) / l)
        M0.append(v); PP.append(P); MHi.append(p % 840 in MH)
    print("Gaussian square windows: %d, cap-0 rate %.4f; control windows of similar size: %d, rate %.4f"
          % (g_tot, g_fire / g_tot, c_tot, c_fire / c_tot))
    print("Spearman(m0, L-proxy) all primes: %.3f" % spearman(M0, PP))
    idx = [i for i in range(len(M0)) if MHi[i]]
    print("Spearman(m0, L-proxy) Mordell-hard only (%d): %.3f" % (len(idx), spearman([M0[i] for i in idx], [PP[i] for i in idx])))
