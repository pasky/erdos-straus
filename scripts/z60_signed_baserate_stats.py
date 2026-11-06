#!/usr/bin/env python3
"""z60 SIGNED: compare ellrank outcomes of the L = 420 survivor twists at the 7 (*)-zero primes of M beyond the two that
motivated the test (5569, 9601) with effort-matched base rates (data/z60/signed/baserate_effort3.txt, same script and
efforts 0..3 as data/z60/signed/zeros_rank_420.txt). Poisson-binomial tails.
Usage: python3 scripts/z60_signed_baserate_stats.py"""
import re, collections
rows = [l for l in open('data/z60/signed/baserate_effort3.txt') if l.startswith('p=')]
st = collections.defaultdict(collections.Counter)
for l in rows:
    m = re.match(r'p=(\d+) mod840=\d+ (chi\d+): ellrank bounds \[(\d+),(\d+)\]', l)
    p, ln, lo, hi = int(m[1]), m[2], int(m[3]), int(m[4])
    band = 1 if p < 5e5 else (2 if p < 3e6 else 3)
    st[(ln, band)]['n'] += 1; st[(ln, band)]['lo2'] += lo >= 2; st[(ln, band)]['hi0'] += hi == 0
for k in sorted(st):
    print(k, dict(st[k]), 'rate(lo>=2) %.3f rate(hi=0) %.3f' % (st[k]['lo2'] / st[k]['n'], st[k]['hi0'] / st[k]['n']))
zr = {}
for l in open('data/z60/signed/zeros_rank_420.txt'):
    m = re.match(r'p=(\d+) mod840=\d+ (chi\d+): ellrank bounds \[(\d+),(\d+)\]', l)
    if m:
        zr[(int(m[1]), m[2])] = (int(m[3]), int(m[4]))
zeros = {83449: 1, 102001: 1, 712321: 2, 1724209: 2, 1726201: 2, 5212561: 3, 8813281: 3}


def tail(ps, k):
    dist = [1.0]
    for p in ps:
        nd = [0] * (len(dist) + 1)
        for i, x in enumerate(dist):
            nd[i] += x * (1 - p); nd[i + 1] += x * p
        dist = nd
    return sum(dist[k:])


for ln in ('chi21', 'chi105'):
    ps = [st[(ln, zeros[z])]['lo2'] / st[(ln, zeros[z])]['n'] for z in zeros]
    k = sum(zr[(z, ln)][0] >= 2 for z in zeros)
    qs = [st[(ln, zeros[z])]['hi0'] / st[(ln, zeros[z])]['n'] for z in zeros]
    k0 = sum(zr[(z, ln)][1] == 0 for z in zeros)
    print(f"{ln}: rank>=2 proven at {k}/7 zeros, expected {sum(ps):.2f}, P(>= {k}) = {tail(ps, k):.4f};  "
          f"Selmer-rank 0 at {k0}/7, expected {sum(qs):.2f}, P(<= {k0}) = {1 - tail(qs, k0 + 1):.4f}")
