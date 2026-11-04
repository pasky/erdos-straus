#!/usr/bin/env python3
"""Independent data/coverage/model audit; run with uv --no-project --with mpmath.
Usage: ... script.py /tmp/xrev_CROSSF /tmp/xrev_CROSSF/sample.in
No lane modules are imported. Memory is bounded by one <=10^7-long interval.
"""
import math
import sys
from collections import Counter
from pathlib import Path
import mpmath as mp

base = Path(sys.argv[1]) / 'data/z55/crossf'
samples = [(10000169, 0)]

def interval_primes(a, b):
    limit = math.isqrt(b)
    small = bytearray(b'\1') * (limit + 1)
    small[:2] = b'\0\0'
    for q in range(2, math.isqrt(limit) + 1):
        if small[q]:
            small[q*q::q] = b'\0' * ((limit-q*q)//q + 1)
    segment = bytearray(b'\1') * (b-a+1)
    for q in range(2, limit + 1):
        if small[q]:
            first = max(q*q, ((a+q-1)//q)*q)
            if first <= b:
                segment[first-a::q] = b'\0' * ((b-first)//q + 1)
    return [p for p in range(a + (1-a) % 4, b+1, 4) if segment[p-a]]

for f in sorted(base.glob('*_1e*.txt')):
    if not f.name.startswith(('scan_', 'sample_')):
        continue
    rows = [tuple(map(int, line.split())) for line in f.read_text().splitlines() if line.strip()]
    h = Counter(k for _, k in rows)
    n = len(rows)
    mean = sum(k*v for k, v in h.items()) / n
    var = sum(k*k*v for k, v in h.items()) / n - mean*mean
    print(f'{f.name}: N={n} zeros={h[0]} mean={mean:.9f} var/mean={var/mean:.9f} '
          f'P0={h[0]/n:.9f} P0/exp(-mean)={h[0]/n*math.exp(mean):.9f}')
    if f.name.startswith('scan_'):
        k = int(f.stem.split('1e')[1])
        end = 10**k + (2_000_000 if k == 8 else 10_000_000)
        if k == 12:
            end = rows[-1][0]
        assert [p for p, _ in rows] == interval_primes(10**k, end)
        print('  complete prime coverage independently verified')
    if f.name in ('scan_1e8.txt', 'scan_1e10.txt'):
        chosen = [rows[j*(n-1)//255] for j in range(256)]
        samples.extend(chosen)
        print(f'  independent-w sample: N=256 zeros={sum(h == 0 for _, h in chosen)}')
Path(sys.argv[2]).write_text(''.join(f'{p} {h}\n' for p, h in samples))

mp.mp.dps = 45
# Complete the square, then use a Gaussian-tail integral, not the lane's s-integral.
def tail(c, L):
    z = mp.sqrt(c)*L - 1/(2*mp.sqrt(c))
    edges = [z] + [mp.mpf(t) for t in (0, 1, 2, 4, 8, 16, 32) if t > z] + [mp.inf]
    return mp.exp(1/(4*c)) * mp.quad(lambda t: mp.exp(-t*t)/(2*(t + 1/(2*mp.sqrt(c)))), edges)

def crossing(c):
    lo, hi = 1/(2*c), 2/c
    for _ in range(90):
        mid = (lo+hi)/2
        if tail(c, mid) > 1:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

for c in (1/(3*mp.pi**4), mp.mpf('.003'), mp.mpf('.1'), 1/mp.pi**4):
    L = crossing(c)
    print('MODEL c=', mp.nstr(c, 14), 'log10(E=1)=', mp.nstr(L/mp.log(10), 14))
    print('  E(1e8)=', mp.nstr(tail(c, 8*mp.log(10)), 14),
          'E(1e18)=', mp.nstr(tail(c, 18*mp.log(10)), 14),
          'E(1e100)=', mp.nstr(tail(c, 100*mp.log(10)), 14))
    print('  peak log10(p)=', mp.nstr((1+mp.sqrt(1-8*c))/(4*c*mp.log(10)), 14))
print('ALL data/coverage checks passed; sample input written to', sys.argv[2])
