# Z2769 part 2: class-group exponent of discriminants attached to the I3 failure set F (from z52d_p2_NC3_i3fail.py, n<=2e5)
# versus a control set (non-failures in windows of the same sizes). Disc choices: D1 = -4n (n ≥ 2), D2 = -n if -n ≡ 0,1 mod 4.
import sys, random
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
F = eval(open('data/z52b/pass2/NC3/i3fail_200k.txt').read().split('failures:')[1].strip()) if False else None
NMAX = 200000
import subprocess
hit = bytearray(NMAX + 1)
for u in range(3, NMAX + 3):
    for v in range(3, NMAX + 3):
        if u*v*3 - u - v > NMAX: break
        t = 3
        while True:
            n = t*u*v - u - v
            if n > NMAX: break
            hit[n] = 1; t += 1
F = [n for n in range(2, NMAX + 1) if not hit[n]]
def expo(D):
    cyc = pari(f"quadclassunit({D}).cyc")
    cyc = [int(x) for x in cyc]
    if not cyc: return 1, 1
    e = 1
    from math import lcm
    for c in cyc: e = lcm(e, c)
    return e, len(cyc)
def stats(ns):
    out = {'n': 0, 'exp<=2': 0, 'exp<=2_D2': 0, 'rank2': 0}
    for n in ns:
        e, r = expo(-4*n)
        out['n'] += 1; out['exp<=2'] += (e <= 2)
    return out
Fs = [n for n in F if n >= 3]
random.seed(1)
ctrl = [n for n in range(3, 20000) if hit[n]]  # n representable (controls)
ctrl = random.sample(ctrl, min(len(ctrl), 400))
s1 = stats(Fs); s2 = stats(ctrl)
print("failures n>=3:", s1, " fraction exp<=2:", round(s1['exp<=2']/s1['n'],3))
print("controls (representable n<2e4, 400 sampled):", s2, " fraction exp<=2:", round(s2['exp<=2']/s2['n'],3))
# class number of -4n for failures (list small)
print("h(-4n) for failures:", [(n, expo(-4*n)[0]) for n in F[:30] if n>=3])
# size-matched controls: all n in [3, 300]: failures vs non-failures
Fl = [n for n in range(3, 301) if not hit[n]]
Cl = [n for n in range(3, 301) if hit[n]]
a = stats(Fl); b = stats(Cl)
print("size-matched n<=300: failures", len(Fl), "exp<=2 frac", round(a['exp<=2']/a['n'],3), "| representable", len(Cl), "exp<=2 frac", round(b['exp<=2']/b['n'],3))
# is h(-4n) = 1 or 2-power structure: fraction of failures with class group elementary 2-group
def elem2(D):
    cyc=[int(x) for x in pari(f"quadclassunit({D}).cyc")]
    return all(c in (1,2) for c in cyc)
print("elementary 2-group, -4n, failures n<=300:", sum(elem2(-4*n) for n in Fl), "/", len(Fl), "; representable:", sum(elem2(-4*n) for n in Cl), "/", len(Cl))
