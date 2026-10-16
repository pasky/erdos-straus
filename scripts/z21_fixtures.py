"""O249 (ASTRA_BRIDGE §4): translate every Astra fixture triple (data/z21_astra_fixtures.txt, extracted verbatim
from ../erdos-straus-astra, read-only) into Claude language, with exact rational arithmetic.
For each record with a numeric triple and input N = p m^2:
  - check 4/N = 1/a + 1/b + 1/c exactly; scale to p: (a, b, c)/m^2; twist tau; slot of the square denominator;
  - at N = p (endpoints): ET type; Type II: window w = 4x - p, divisor d (d | x^2, d = -x mod w), slices g = 4y'-1,
    square-shot (d a square) flag; Type I: level e = (4H-1)/p, r = eU - H for the split, r | H^2, e | 4r+1.
"""
import re
from fractions import Fraction as F
from math import isqrt, gcd
from sympy import isprime

def ev(s):
    s = s.strip()
    if not re.fullmatch(r"[0-9*^ ()+]+", s):
        return None
    return eval(s.replace('^', '**'))

def classify_at_p(p, t):
    a = sorted(t, key=lambda v: (v % p == 0, v))
    out = []
    pdiv = [v for v in t if v % p == 0]
    if len(pdiv) == 2:
        x = [v for v in t if v % p][0]
        y1, z1 = [v // p for v in pdiv]
        w = 4 * x - p
        d = w * y1 - x
        sq = isqrt(d) ** 2 == d
        out.append(f"TypeII window w={w}{'(prime)' if isprime(w) else ''} K=x={x} d={d} d|K^2={x*x % d == 0} "
                   f"d=-K(w)={(d + x) % w == 0} square-shot={sq} slices g={4*y1-1},{4*z1-1}")
    elif len(pdiv) == 1:
        X = pdiv[0]; H = X // p; e4 = 4 * H - 1
        if e4 % p == 0:
            e = e4 // p
            U, V = sorted(v for v in t if v % p)
            for UU in (U, V):
                r = e * UU - H
                if r > 0 and (H * H) % r == 0 and (4 * r + 1) % e == 0:
                    out.append(f"TypeI level e={e} H={H} r={r} (r|H^2, e|4r+1)")
                    break
            else:
                out.append(f"TypeI x=pH, H={H}, e={e}: no (U,r) found")
        else:
            out.append(f"TypeI-shape x={X} but (4x/p-1) not divisible by p")
    else:
        out.append(f"p divides {len(pdiv)} coords")
    return "; ".join(out)

recs = []
for line in open('data/z21_astra_fixtures.txt'):
    mp = re.match(r"p=(\d+);", line)
    mt = re.search(r"triple=\(([^)]*)\)", line)
    mN = re.search(r"N=([^;]*)$", line.strip())
    if not (mp and mt and mN):
        continue
    p = int(mp.group(1))
    parts = [ev(x) for x in mt.group(1).split(',')]
    N = ev(mN.group(1))
    if None in parts or N is None or len(parts) != 3:
        continue
    recs.append((p, tuple(parts), N, line.split(';')[1].strip() + ' ' + line.split(';')[2].strip()))

seen = set()
for p, t, N, src in recs:
    key = (p, tuple(sorted(t)), N)
    if key in seen:
        continue
    seen.add(key)
    ok = F(4, N) == sum(F(1, v) for v in t)
    m2 = N // p
    m = isqrt(m2)
    if m * m * p != N:
        print(f'p={p} N={N} not p*square (record kept verbatim, skipped) |', src); continue
    pts = [F(v, m2) for v in t]
    tau = 1
    while any((tau * tau * x).denominator != 1 for x in pts):
        tau += 1
    info = f"p={p} N=p*{m}^2 triple={t} exact={ok} tau={tau}"
    if tau == 1:
        info += " ENDPOINT " + classify_at_p(p, [int(x) for x in pts])
    else:
        twisted = [i for i, x in enumerate(pts) if x.denominator != 1]
        slot = ['p-free' if pts[i].numerator % p else 'p-div' for i in twisted]
        info += f" twisted-slot={slot} dens={[pts[i].denominator for i in twisted]}"
        if len(twisted) == 1:
            i = twisted[0]; xi = pts[i]
            if xi.numerator % p:
                info += f" window(rational)=4x-p={4*xi - p}"
            others = [int(pts[j]) for j in range(3) if j != i]
            r_ = isqrt(xi.denominator)
            selfmute = all(any(o % l == 0 for o in others) for l in range(3, r_ + 1) if r_ % l == 0 and isprime(l))
            info += f" self-mute(rad tau | other coord)={selfmute}"
    print(info, "|", src)
