"""LS7 numerics (EVIDENCE only): residue dispersion of R(M) classes through one prime p.

Full-family model: M = p*n, M = 3 mod 4, n <= NMAX with P(n) > p; class -4D (D | A^2), via triples
(u,v,t) (Lemma 1.1).  Weight w_{P(n)}/n with w_q = q^{-EPS} (toy damping; Gamma ~ 1 omitted).
Reports, per p: total mass nu, max_a mu_a with and without the height cut
min(max(u,v),4u^2t,4v^2t) > p^{1/4} (the cut used in Thm 3.1), and the top residues."""
import sys
from math import gcd
from sympy import factorint, divisors

EPS = 0.05

def run(p, NMAX):
    H0 = p ** 0.25
    mu_all, mu_cut = {}, {}
    for n in range(1, NMAX + 1):
        M = p * n
        if M % 4 != 3:
            continue
        f = factorint(n)
        Pn = max(f) if f else 1
        if Pn <= p:
            continue
        wt = Pn ** (-EPS) / n
        A = (M + 1) // 4
        for u in divisors(A):
            for v in divisors(A // u):
                if gcd(u, v) != 1:
                    continue
                t = A // (u * v)
                a = (-u * pow(v, -1, p)) % p
                mu_all[a] = mu_all.get(a, 0) + wt
                if min(max(u, v), 4 * u * u * t, 4 * v * v * t) > H0:
                    mu_cut[a] = mu_cut.get(a, 0) + wt
    nu = sum(mu_all.values())
    top_all = sorted(mu_all.items(), key=lambda x: -x[1])[:3]
    top_cut = sorted(mu_cut.items(), key=lambda x: -x[1])[:3]
    print(f"p={p} NMAX={NMAX} nu={nu:.4f} nu/p={nu/p:.2e}")
    print("  no cut : max mu_a=%.4f  (x p/nu = %.1f)  top %s" % (top_all[0][1], top_all[0][1] * p / nu,
          [(a, round(m, 4)) for a, m in top_all]))
    print("  cut    : max mu_a=%.4f  (x p/nu = %.1f)  top %s" % (top_cut[0][1], top_cut[0][1] * p / nu,
          [(a, round(m, 4)) for a, m in top_cut]))

if __name__ == "__main__":
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 10      # NMAX = K*p
    for p in map(int, sys.argv[2:] or ["101", "211", "401", "809", "1601"]):
        run(p, K * p)
