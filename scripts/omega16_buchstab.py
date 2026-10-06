"""OMEGA16 §6 (N1): Buchstab deficit for primes in unit-class sifted sets (EVIDENCE).

For shifts H=(h_1..h_k) (even), events n ≡ -h_i (mod l) for primes 3<=l<=z (unit classes only),
count primes z<p<=x with all p+h_i z-rough, and compare with delta*(pi(x)-pi(z)), delta the
Haar density in Z^x of the avoider set. Prediction (HL + Buchstab, Prop 2.1(b)):
ratio ≈ (e^gamma*omega(u))^k, u=log x/log z.

Usage: PYTHONPATH=scripts uv run python scripts/omega16_buchstab.py X
"""
import sys, math
import numpy as np

EULER_GAMMA = 0.5772156649015329


def buchstab_omega(u, h=1e-4):
    """omega(u) for u>=1 by integrating (u*omega(u))' = omega(u-1)."""
    if u < 1:
        return 0.0
    n = int(round(1 / h))
    grid_max = max(u, 2.0)
    m = int(math.ceil(grid_max / h)) + 2
    us = np.arange(m) * h
    w = np.zeros(m)
    for i in range(m):
        if us[i] < 1 - 1e-12:
            w[i] = 0.0
        elif us[i] <= 2 + 1e-12:
            w[i] = 1.0 / us[i]
    i2 = int(round(2 / h))
    F = us[i2] * w[i2]  # u*omega(u)
    for i in range(i2 + 1, m):
        # trapezoid on omega(u-1)
        a = w[i - 1 - n]
        b = w[i - n]
        F += h * (a + b) / 2
        w[i] = F / us[i]
    return float(np.interp(u, us, w))


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = False
    return s


def main():
    X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10 ** 8
    shifts_list = [(2,), (2, 6), (2, 6, 8)]
    hmax = 8
    isprime = primes_upto(X + hmax)
    plist = np.nonzero(isprime)[0]
    print(f"X={X:.3g}  pi(X)={int(isprime[:X+1].sum())}")
    print("k  u     z        count      delta*pi     ratio   (e^g w(u))^k")
    for u in [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]:
        z = int(X ** (1 / u))
        rough = np.ones(X + hmax + 1, dtype=bool)
        for l in plist[plist <= z]:
            rough[:: int(l)] = False
        pz = plist[(plist > z) & (plist <= X)]
        npx = len(pz)
        for H in shifts_list:
            ok = np.ones(npx, dtype=bool)
            for h in H:
                ok &= rough[pz + h]
            cnt = int(ok.sum())
            # Haar density in Z^x: at each prime 3<=l<=z, exclude classes -h mod l that are units
            logd = 0.0
            for l in plist[(plist >= 3) & (plist <= z)]:
                l = int(l)
                bad = len({(-h) % l for h in H} - {0})
                logd += math.log(1 - bad / (l - 1))
            pred = math.exp(logd) * npx
            bf = (math.exp(EULER_GAMMA) * buchstab_omega(u)) ** len(H)
            print(f"{len(H)}  {u:3.1f}  {z:8d}  {cnt:9d}  {pred:11.1f}  {cnt/pred:6.3f}   {bf:6.3f}")


if __name__ == "__main__":
    main()
