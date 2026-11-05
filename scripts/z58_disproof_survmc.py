# z58 DISPROOF §4.2: Monte-Carlo "surviving mass" model.  Heuristic (Assessment): (★) solutions at a generic prime p are
# pairs (u,B) with density 1/(4uB) on 4uB <= p (log-uniform on the triangle a + b <= log(p/4)), C = (p+u+B)//(4uB).
# A y-square-mimicking prime (p = 1 (8), (l/p) = +1 for odd l <= y) keeps exactly the solutions with no y-smooth modulus
# among m1 = 4uB, m2 = 4uC-1, m3 = 4BC-1 (Lemma 2.2).  surv(y,p) := P(no y-smooth modulus)/P(no 3-smooth modulus)
# (the baseline p = 1 (24) already kills 3-smooth moduli).  Validated against the exact enumeration at 1e10
# (scripts/z58_disproof_smooth.c).  Run: uv run --with numpy --with sympy python scripts/z58_disproof_survmc.py
import sys, math, random
from sympy import primerange
YS = [3, 7, 13, 31, 61, 97, 199, 499, 997]
PR = list(primerange(2, 1000))
def lpf_le(m, y):
    """True iff m is y-smooth (trial division by primes <= y)."""
    for q in PR:
        if q > y: break
        while m % q == 0: m //= q
        if m == 1: return True
    return m == 1
def sample(p, n, rng):
    X = math.log(p / 4)
    cnt = [0] * len(YS)
    for _ in range(n):
        while True:
            a, b = rng.random() * X, rng.random() * X
            if a + b <= X: break
        u = int(math.exp(a)); B = int(math.exp(b))
        if (u + B) % 2 == 0: continue_flag = True
        else: continue_flag = False
        if continue_flag: continue               # p odd forces u + B odd
        C = (p + u + B) // (4 * u * B)
        if C < 1: continue
        ms = (4 * u * B, 4 * u * C - 1, 4 * B * C - 1)
        for k, y in enumerate(YS):
            if not any(lpf_le(m, y) for m in ms): cnt[k] += 1
    return cnt
if __name__ == "__main__":
    rng = random.Random(58)
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    print("# surv(y,p) = P(no y-smooth modulus)/P(no 3-smooth modulus); N samples per p; y =", YS)
    for e in [10, 12, 14, 17, 20, 25, 30]:
        c = sample(10 ** e, N, rng)
        print(f"p=1e{e}", ' '.join(f"{c[k]/c[0]:.4f}" for k in range(len(YS))), flush=True)
