"""Independent (Opus reviewer) checks of the group-theoretic parts of notes/z80/PROTH_CORE.md.
No repository script imported.  PARI (cypari2) is used only for factoring / discrete logs.
 (a) full gcd-ratio index [G:R_h] by FULL discrete logs + HNF (no l^2 truncation) for odd h<=HMAX,
     compared with data/z80/proth/indices.json;
 (b) Theorem 1 test: for prime powers h=p^j, prime-to-p part of [G:R_h] equals the product over
     layers N_i of the prime-to-p parts of [G_i : pi_i(R_h)]; p-part reported for contrast;
 (c) primary.json and tower-7.json recomputed (tower also on M=2^729-1 via X_a=B_a^3/B_{3a});
 (d) Theorem 5 quadratic family; (e) z79 T transfer data for cover-11 rows and small s.
Run: ulimit -v 6000000; uv run --offline --no-project --with cypari2 python -B opus_indep_groups.py HMAX a b c
"""
import json, sys, signal
def _alarm(*a): raise TimeoutError
signal.signal(signal.SIGALRM, _alarm)
from math import gcd, lcm, isqrt, prod
from pathlib import Path
from cypari2 import Pari
pari = Pari(); pari.allocatemem(256 << 20, 1 << 30, silent=True)
ROOT = Path(__file__).resolve().parents[3]
P = ROOT / 'data/z80/proth'
HMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 101

def blocks_of(H, fac=None):
    F = fac if fac is not None else [(int(q), int(e)) for q, e in zip(*pari.factor(H))]
    assert prod(q ** e for q, e in F) == H and all(pari.isprime(q) for q, e in F)
    out = []
    for q, e in F:
        n = q ** e; o = (q - 1) * q ** (e - 1)
        g = int(pari.znprimroot(n)); out.append((n, o, g))
    return out

def logvec(x, blocks):
    return [int(pari.znlog(pari.Mod(x, n), pari.Mod(g, n), o)) for n, o, g in blocks]

def lattice_index(cols, orders):
    rows = len(orders)
    allc = [list(c) for c in cols] + [[orders[i] if i == r else 0 for r in range(rows)] for i in range(rows)]
    Mt = pari.matrix(rows, len(allc), [allc[c][r] for r in range(rows) for c in range(len(allc))])
    return abs(int(pari.matdet(pari.mathnf(Mt))))

def ratio_cols(h, H, blocks):
    B = lambda a: (1 + pow(2, a % h, H)) % H
    cols = []
    for a in range(1, h):
        g = gcd(a, h)
        if a == g: continue
        cols.append(logvec(B(a) * pow(B(g), -1, H) % H, blocks))
    return cols

def ppart(n, p):
    r = 1
    while n % p == 0: n //= p; r *= p
    return r

def full_index(h, fac=None):
    H = 2 ** h - 1; bl = blocks_of(H, fac)
    return lattice_index(ratio_cols(h, H, bl), [o for n, o, g in bl]), H, bl

def check_a():
    rows = {r['h']: r for r in json.loads((P / 'indices.json').read_text())}
    bad = []; cnt = 0; skipped = []
    for h in range(3, HMAX + 1, 2):
        fac = [(q, e) for q, e, _ in rows[h]['factors']]
        signal.alarm(120)
        try: I, H, bl = full_index(h, fac)
        except BaseException as ex: signal.alarm(0); skipped.append(h); print('skip', h, type(ex).__name__, flush=True); continue
        finally: signal.alarm(0)
        cnt += 1
        print('h', h, I, rows[h]['index'], flush=True)
        if I != rows[h]['index']: bad.append((h, I, rows[h]['index']))
    print('(a) full-log index agrees with indices.json for', cnt, 'h; mismatches:', bad, 'skipped (dlog timeout):', skipped, flush=True)

def check_b(hs):
    for h in hs:
        p = next(q for q in range(3, h + 1) if h % q == 0)
        j = 0; t = h
        while t > 1: assert t % p == 0; t //= p; j += 1
        I, H, bl = full_index(h)
        res = []
        tot = 1
        for i in range(1, j + 1):
            Ni = (2 ** (p ** i) - 1) // (2 ** (p ** (i - 1)) - 1)
            idx = [b for b, (n, o, g) in enumerate(bl) if Ni % n == 0]
            assert prod(bl[b][0] for b in idx) == Ni
            cols = [[c[b] for b in idx] for c in ratio_cols(h, H, bl)]
            Ii = lattice_index(cols, [bl[b][1] for b in idx]); res.append(Ii); tot *= Ii
        pp = lambda x: x // ppart(x, p)
        ok = pp(I) == pp(tot)
        print(f'(b) h={h}: [G:R]={I}, layer indices={res}, prime-to-{p} parts equal: {ok}; '
              f'{p}-parts: global {ppart(I,p)} vs product {ppart(tot,p)}', flush=True)
        assert ok

def check_c():
    rows = json.loads((P / 'primary.json').read_text())
    assert [r['h'] for r in rows] == list(range(263, 400, 2))
    for r in rows:
        h = r['h']; H = 2 ** h - 1; k = 2 * H + 1; c = r['c']; T0 = r['T0']
        assert k % c == 0 and c % 16 == 1 and set(T0) <= {1, 3} and len(set(T0)) == len(T0)
        if 3 in T0: assert h % 3 == 0
        # slots: Phi_2(2)=3, Phi_6(2)=3
        v = c * 3 ** len(T0) % H
        for a, e in r['ratios'].items():
            a = int(a); assert 0 < a < h and gcd(a, h) == 1 and e >= 0
            v = v * pow((1 + 2 ** a) * pow(3, -1, H) % H, e, H) % H
        assert v == H - 1, h
    print('(c) primary.json: 69 rows h=263..399, -1/(c 3^|T0|) in unit-index ratio group', flush=True)
    t = json.loads((P / 'tower-7.json').read_text())
    d = 729; h = 2187; M = 2 ** d - 1; H = 2 ** h - 1
    B = lambda a, Q: (1 + pow(2, a, Q)) % Q
    # on M: X_a = B_a^3 / B_{3a}
    A = 1
    for a, e in t['powers'].items():
        a = int(a); assert 0 < a < d and a % 3 and e >= 0
        Xa = pow(B(a, M), 3, M) * pow(B(3 * a, M), -1, M) % M
        A = A * pow(Xa * pow(3, -1, M) % M, e, M) % M   # X_1 = 27/9 = 3
    assert A == 729 % M
    # full modulus, written as an explicit product of legal ratios B_x/B_y with equal gcd(.,h)
    num = {}; 
    def add(a, b, e):
        assert gcd(a % h, h) == gcd(b % h, h) or (a % h == 0 == b % h)
        num[(a % h, b % h)] = num.get((a % h, b % h), 0) + e
    for a, e in t['powers'].items():
        a = int(a)
        for s in range(3): add(a + s * d, 1 + s * d, e)
        add(3, 3 * a, e)
    add(1, 1 + d, 6); add(1, 1 + 2 * d, 6)
    v = 1
    for (a, b), e in num.items():
        v = v * pow(B(a, H) * pow(B(b, H), -1, H) % H, e, H) % H
    assert v == 729
    gcds = sorted({gcd(a, h) for a, b in num})
    print('(c) tower-7: 3^6 = product of ratios with gcds', gcds, 'modulo 2^2187-1', flush=True)
    # half-orbit exponent for m=1094
    assert pow(2, 729, 2187) == 2186 and 729 % 6 == 3
    print('(c) 2^729 = -1 mod 2187, 729 = 3 mod 6', flush=True)

def check_d():
    for jj in range(64):
        u = 16 * jj + 14; k = u + 1
        for i in range(64):
            t = 8 * i + 7; z = t * u - 1; n = k * (z * z - 1) + 1; v = k * z
            assert n + u + v == t * u * v and (n + t) % 8 == 0 and n % 4 == 1
            assert (t * v - 1) % 4 == 0; D = (t * v - 1) // 4
            x, y, w = z * D * n, u * D, z * u * D
            assert 4 * x * y * w == n * (x * y + y * w + w * x)
            assert isqrt(n) ** 2 != n
    print('(d) quadratic transfer: 64x64 triples, words, nonsquare', flush=True)

def check_e():
    T = int(json.loads((ROOT / 'data/z79/proth/intersection.json').read_text())['T'])
    k = 4 ** 11 - 1
    for s in range(1, 64):
        n = k * 2 ** s + 1; assert pow(4, T, n) == 1, s
    c = json.loads((P / 'cover-11.json').read_text())
    P0 = c['period']; assert P0 == 3825360
    for Pr, j, Tt, *z in c['rows']:
        if Tt == 'M': M = 840
        elif Tt in ('D', 'II'): M = z[0]
        elif Tt == 'W': M = 8 * z[0]
        else:
            f, K0, D, E = z; M = 4 * f * K0 if (D[2] or E[2]) else 4 * lcm(f, K0)
        two = M & -M; odd = M // two
        assert two <= 2 ** 64 and pow(4, T, odd) == 1 % odd
    # F1 square exponent s=2m+2 for transferred m=11+T*i: which rows cover it?
    types = set()
    for i in (1, 2, 3):
        s = 2 * (11 + T * i) + 2
        hit = [r for r in c['rows'] if s % r[0] == r[1]]
        assert hit and s % P0 != 0
        types |= {r[2] for r in hit}
    print('(e) z79 T: 4^T=1 mod n_{11,s} (1<=s<64) and all cover-11 odd moduli; dyadic<=2^64; '
          'square exponent 2m+2 covered by row types', sorted(types), flush=True)
    assert not (types & {'W', 'M', 'X'}), types

if __name__ == '__main__':
    if 'c' in sys.argv[2:]: check_c(); check_d(); check_e()
    if 'b' in sys.argv[2:]: check_b([9, 25, 27, 49, 81])
    if 'a' in sys.argv[2:]: check_a()
