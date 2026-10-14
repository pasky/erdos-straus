#!/usr/bin/env python3
"""R217 from-scratch enumeration of Case B tuples (B) of FF_STERILE_PUSH / DEPTH_ASPECT §2.1:
  m' w C = T^s + v,  w + C = g' v,  T || w, T || C, T not| m'g', v != 0, all of m', g', w, C monic.
Enumeration by (m', g', w) (route T0): E = m'g'w - 1 must divide g'T^s + w, C = (g'T^s + w)/E.
[Completeness: by DEPTH_ASPECT Lemma 2.1 (R3) every tuple arises this way, and conversely we re-check (B) directly.]
Checks Lemma 1.1 (E v = T^s + m'w^2, y + t = max(a,b), T^2 || v), records exact counts per pattern (s; a, z, y, t)
(normalised to a <= b by swapping w <-> C), and writes them as JSON for comparison with route bounds.
Usage: review_fs_tuples.py p smax out.json
"""
import sys, json, itertools

def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a

def add(a, b, p):
    n = max(len(a), len(b)); r = [0] * n
    for i, x in enumerate(a): r[i] = x
    for i, x in enumerate(b): r[i] = (r[i] + x) % p
    return trim(r)

def neg(a, p):
    return [(-x) % p for x in a]

def mul(a, b, p):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return trim(r)

def divmod_(a, m, p):
    a = list(a); dm = len(m) - 1; inv = pow(m[-1], p - 2, p)
    if len(a) - 1 < dm: return [], trim(a)
    qd = [0] * (len(a) - dm)
    for i in range(len(a) - 1, dm - 1, -1):
        c = a[i] * inv % p
        if c:
            qd[i - dm] = c
            for j, y in enumerate(m):
                a[i - dm + j] = (a[i - dm + j] - c * y) % p
    return trim(qd), trim(a[:dm])

def monic(deg, p, notT=True):
    for co in itertools.product(range(p), repeat=deg):
        f = list(co) + [1]
        if notT and deg >= 1 and f[0] == 0: continue
        yield f

def Tpow(s): return [0] * s + [1]

def main():
    p, smax, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    counts = {}
    nt = 0
    for s in range(3, smax + 1):
        Ts = Tpow(s)
        # a = deg w >= 1, z = deg m', y = deg g'; need b = s - a - z >= 1 and y <= max(a,b) - 2
        for a in range(1, s):
            for z in range(0, s - a):
                b = s - a - z
                if b < 1: continue
                for y in range(0, max(a, b) - 1):
                    for mp in monic(z, p):
                        for gp in monic(y, p):
                            Lp = mul(gp, mp, p)
                            num = add(mul(gp, Ts, p), [], p)
                            for w1 in monic(a - 1, p):
                                w = [0] + w1
                                E = add(mul(Lp, w, p), [p - 1], p)
                                C, rem = divmod_(add(num, w, p), E, p)
                                if rem: continue
                                # verify (B)
                                assert C and C[-1] == 1 and len(C) - 1 == b
                                if C[0] != 0 or C[1] == 0: continue   # T || C
                                v = add(mul(mul(mp, w, p), C, p), neg(Ts, p), p)
                                if not v: continue
                                gv = mul(gp, v, p)
                                if gv != add(w, C, p): continue
                                nt += 1
                                t = len(v) - 1
                                # Lemma 1.1 checks
                                assert mul(E, v, p) == add(Ts, mul(mp, mul(w, w, p), p), p), 'Ev'
                                assert y + t == max(a, b), ('y+t', s, a, b, y, t)
                                assert v[0] == 0 and v[1] == 0 and v[2] != 0, 'T^2||v'
                                aa, bb = min(a, b), max(a, b)
                                key = f'{s},{aa},{z},{y},{t}'
                                counts[key] = counts.get(key, 0) + (1 if a <= b else 0)
                                counts.setdefault('swapped:' + key, 0)
                                if a > b: counts['swapped:' + key] += 1
        print(f'p={p} s={s} tuples so far={nt}', flush=True)
    json.dump(counts, open(out, 'w'))
    # symmetry check: for a != b, #(a<b) == #(a>b)
    bad = 0
    for k, c in counts.items():
        if k.startswith('swapped:'): continue
        s, aa, z, y, t = map(int, k.split(','))
        bb = y + t
        if aa != bb and counts['swapped:' + k] != c: bad += 1
    print('total tuples', nt, 'symmetry violations', bad)

if __name__ == '__main__':
    main()
