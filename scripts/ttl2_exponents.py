"""O116 sanity check (scope: q = 1, logs, ε- and sieve-losses ignored, δ ≤ 0.35 grid; it does NOT check §4)
of of the exponent bookkeeping in EXCEPTIONAL_TYPEI_LOGLOG2.md, Thm 3.1 / Cor 3.2.

Exponents of N (q = 1, logs ignored): a = N^alpha, c = N^gamma, d = N^{1-alpha-gamma}, e = N^{beta-gamma},
f = N^{1+alpha-beta}; delta = 2 alpha - 1 + gamma > 0 (D < A).  For the cusp variable F' of TTL cases
(b2) F'=e, beta in [alpha, alpha+gamma];  (b3) F'=min(e,f), beta in [alpha+gamma, 1];  (b5) F'=f, beta in [1, 1+delta/2]
the three relative-error terms of Thm 3.1 are
  T1 = (D/A)^{1/2} (1 + A/F')^{1/2},  T2 = F'^{1/2}/A,  T3 = F'^{1/4} D^{1/8} A^{-1/2}.
Claim (Cor 3.2): max(T1,T2,T3) <= N^{-delta/4} or <= N^{-1/20}, for gamma <= eta = 1/20, delta <= 0.35.
Also report the old crude-weight third term T3_crude = (lambda/Y)^{..}: q A^{-1/2}(X0^2/lambda)^{1/4} (fails in b3).
"""
import itertools

def check(eta=0.05, steps=60):
    worst = {}
    bad = []
    for gi, di, bi in itertools.product(range(steps + 1), range(1, steps + 1), range(steps + 1)):
        g = eta * gi / steps
        delta = 0.35 * di / steps
        al = (1 - g + delta) / 2
        A, D = al, 1 - al - g
        for case in ("b2", "b3", "b5"):
            if case == "b2":
                if delta < 2 * g:  # TTL (b2) is used only for k >= 2j, i.e. delta >= 2 gamma; else BT (b4)
                    continue
                lo, hi = al, al + g
            elif case == "b3":
                lo, hi = al + g, 1.0
            else:
                lo, hi = 1.0, 1.0 + delta / 2
            if hi < lo:
                continue
            be = lo + (hi - lo) * bi / steps
            e, f = be - g, 1 + al - be
            Fp = {"b2": e, "b3": min(e, f), "b5": f}[case]
            if case == "b3" and Fp < A:  # off the band: F' >= 8A
                continue
            T1 = 0.5 * (D - A) + 0.5 * max(0.0, A - Fp)
            T2 = 0.5 * Fp - A
            T3 = 0.25 * Fp + D / 8 - A / 2
            T3crude = -A / 2 + 0.25 * (2 * Fp + D / 2 - A)  # crude weight, correct DI normalisation: X0^2/lambda
            m = max(T1, T2, T3)
            target = max(-delta / 4, -1 / 20)
            key = case
            worst[key] = max(worst.get(key, -9), m - target)
            if m > target + 1e-12:
                bad.append((case, g, delta, be, T1, T2, T3))
            worst[key + "_crudeT3"] = max(worst.get(key + "_crudeT3", -9), T3crude)
    return worst, bad

if __name__ == "__main__":
    worst, bad = check()
    for k, v in sorted(worst.items()):
        print(f"{k:12s} max excess = {v:+.4f}")
    print("violations:", len(bad))
    for b in bad[:10]:
        print(b)
