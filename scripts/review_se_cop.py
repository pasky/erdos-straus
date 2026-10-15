"""R222: from-scratch adversarial test of STERILE_EXPLICIT Lemma 1.3 / Cor 1.4 (exact integer arithmetic).
Lemma 1.3: if w^w n^{m(m+1)/2} X^{w(w-1)/2} < D0^{mw}, X = (D1-D0)/(2s)+1/2, w = m+k, then n has <= w-1 divisors
E in [D0, D1] with E == sigma (mod s), gcd(sigma, s) = 1.
Adversarial search: for every n <= NMAX and every s <= SMAX, every unit class mod s, every run of t consecutive
divisors E_i < ... < E_{i+t-1} of n in that class, set D0 = E_i, D1 = E_{i+t-1} (the tightest window) and check that
(Cop) FAILS for every (m, k) with w-1 < t, w <= WMAX.  Any success of (Cop) there is a counterexample.
Cor 1.4 (J pieces): additionally for J = 2..4, check count <= J(w-1) whenever (Cop) holds with X_J.
Usage: uv run python scripts/review_se_cop.py NMAX SMAX WMAX"""
import sys
from math import gcd

import math
CLOSEST = [-1e9, None]
def cop_holds(n, s, D0, D1, m, w, J=1, track=False):
    # X_J = (D1-D0)/(2sJ) + 1/2 = (D1-D0+sJ)/(2sJ); (Cop) <=> w^w n^{m(m+1)/2} (D1-D0+sJ)^B < D0^{mw} (2sJ)^B
    B = w * (w - 1) // 2
    if track:   # log(RHS/LHS): > 0 would be a violation; record the closest approach
        g = (m * w * math.log(D0) + B * math.log(2 * s * J)) - (w * math.log(w) + m * (m + 1) / 2 * math.log(n) + B * math.log(D1 - D0 + s * J))
        if g > CLOSEST[0]: CLOSEST[0] = g; CLOSEST[1] = (n, s, D0, D1, m, w, J)
    return w ** w * n ** (m * (m + 1) // 2) * (D1 - D0 + s * J) ** B < D0 ** (m * w) * (2 * s * J) ** B

def main(NMAX, SMAX, WMAX):
    divs = [[] for _ in range(NMAX + 1)]
    for d in range(1, NMAX + 1):
        for k in range(d, NMAX + 1, d): divs[k].append(d)
    viol = 0; tests = 0; holds = 0; tight = 0
    for n in range(2, NMAX + 1):
        D = divs[n]
        if len(D) < 3: continue
        for s in range(1, SMAX + 1):
            cls = {}
            for E in D:
                if gcd(E, s) == 1: cls.setdefault(E % s, []).append(E)
            for L in cls.values():
                t_all = len(L)
                for i in range(t_all):
                    for t in range(2, t_all - i + 1):
                        D0, D1 = L[i], L[i + t - 1]
                        for w in range(2, min(WMAX, t) + 1):          # claim would be count <= w-1 < t
                            for m in range(1, w + 1):
                                tests += 1
                                if cop_holds(n, s, D0, D1, m, w, track=True):
                                    viol += 1; print("VIOLATION Lemma 1.3", n, s, L[i:i + t], m, w)
                        for J in (2, 3, 4):                           # Cor 1.4
                            for w in range(2, WMAX + 1):
                                if J * (w - 1) >= t: break
                                for m in range(1, w + 1):
                                    tests += 1
                                    if cop_holds(n, s, D0, D1, m, w, J, track=True):
                                        viol += 1; print("VIOLATION Cor 1.4", n, s, L[i:i + t], m, w, J)
                # positive control: single-divisor windows where (Cop) holds (count 1 <= w-1)
                for E in L:
                    for w in range(2, 4):
                        for m in range(1, w + 1):
                            if cop_holds(n, s, E, E, m, w): holds += 1
    print(f"NMAX={NMAX} SMAX={SMAX} WMAX={WMAX}: (Cop) evaluations on over-full windows {tests}, violations {viol}; "
          f"positive-control (Cop) successes on 1-divisor windows {holds}")
    print("closest approach log(RHS/LHS) on over-full windows:", CLOSEST)
    return viol

if __name__ == '__main__':
    a = [int(x) for x in sys.argv[1:4]]
    sys.exit(1 if main(*a) else 0)
