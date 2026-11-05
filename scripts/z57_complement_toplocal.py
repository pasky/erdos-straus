# z57 COMPLEMENT: are the negative top-band correlations (e.g. STAR z8 vs c3 z9) pure local (CRT) data?
# Top-band families are congruence families: with pair sets of bounded size they are sums of indicators 1[p ≡ a_i (mod q_i)].
#   STAR_top(Y):  pairs (u,v), u,v >= 1, uv <= Y:  word (t,u,v) with 4 | t  <=>  p ≡ -(u+v) (mod 4uv)
#   QR_top(Y):    pairs (u,v), u,v >= 2, uv <= Y:  word exists (uv | p+u+v) and t,u,v in no certificate cell
#   c3_top(Y):    pairs (a,b), ab <= Y: 12ab | 3p + a + b  <=>  3 | a+b and p ≡ -(a+b)/3 (mod 4ab)
#   c2_top(Y):    8ab | 2p + a + b <=> 2 | a+b and p ≡ -(a+b)/2 (mod 4ab)
# For each family the list of (modulus, residue-set) is exact. The CRT (local) model: p uniform on units mod lcm;
# P(p ≡ a mod q, p ≡ a' mod q') = 1[a ≡ a' mod gcd]/phi(lcm)  (for residues prime to the moduli).
# Compares the empirical covariance over primes with the CRT-model covariance.
# usage: python z57_complement_toplocal.py LO COUNT Y1 Y2 [YLO]   (STAR pairs YLO < uv <= Y1; B1, c2, c3, QR pairs <= Y2)
import sys, math
from math import gcd
import numpy as np
from sympy import nextprime, totient

def star_events(Y, Ylo=0):
    ev = []
    for u in range(1, Y + 1):
        for v in range(1, Y // u + 1):
            if u * v <= Ylo: continue
            q = 4 * u * v; a = (-(u + v)) % q
            if gcd(a, q) == 1: ev.append((q, a))
    return ev

def cline_events(c, Y):
    ev = []
    for a in range(1, Y + 1):
        for b in range(1, Y // a + 1):
            if (a + b) % c: continue
            q = 4 * a * b; r = (-((a + b) // c)) % q
            if gcd(r, q) == 1: ev.append((q, r))
    return ev

def qr_events(Y):
    # word (t,u,v), u,v >= 2: uv | p+u+v; t = (p+u+v)/(uv); cell by (t,u,v) mod 4 and t*u, t*v mod 4.
    # p mod 4uv determines t mod 4; enumerate residues r mod 4uv with r ≡ -(u+v) (mod uv), p ≡ 1 (mod 4)
    ev = []
    for u in range(2, Y + 1):
        for v in range(2, Y // u + 1):
            q = 4 * u * v
            for k in range(4):
                r = (-(u + v) + k * u * v) % q
                if gcd(r, q) != 1 or r % 4 != 1: continue
                t = k % 4  # t ≡ (r+u+v)/(uv) mod 4
                t = ((r + u + v) // (u * v)) % 4 if (r + u + v) % (u * v) == 0 else None
                if t is None: continue
                s = t % 4 == 0; b1 = u % 4 == 0 or v % 4 == 0; i1 = (t * u) % 4 == 1 or (t * v) % 4 == 1
                if not (s or b1 or i1): ev.append((q, r))
    return ev

def b1_events(Y):
    # word (t,u,v) with 4 | u or 4 | v exists iff uv | p + u + v; residue class mod uv (a multiple of 4)
    ev = []
    for u in range(1, Y + 1):
        for v in range(1, Y // u + 1):
            if u % 4 and v % 4: continue
            q = u * v; a = (-(u + v)) % q
            if gcd(a, q) == 1 and a % 4 == 1: ev.append((q, a))
    return ev

def phi(n): return int(totient(n))

def crt_cov(E1, E2):
    # sum over event pairs of P(both) - P(1)P(2), units only, p ≡ 1 mod 4 imposed: all moduli are multiples of 4 and
    # residues ≡ 1 mod 4 (checked), so condition on p ≡ 1 (4): P(p ≡ a mod q | p ≡ 1 mod 4) = 2/phi(q).
    tot = 0.0
    for (q, a) in E1:
        for (q2, a2) in E2:
            g = gcd(q, q2); l = q // g * q2
            both = (2.0 / phi(l)) if (a - a2) % g == 0 else 0.0
            tot += both - (2.0 / phi(q)) * (2.0 / phi(q2))
    return tot

def counts(ps, E):
    out = np.zeros(len(ps))
    for (q, a) in E: out += (ps % q == a)
    return out

def main():
    lo, cnt, Y1, Y2 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    Ylo = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    ps = []; p = lo
    while len(ps) < cnt:
        p = nextprime(p)
        if p % 4 == 1: ps.append(p)
    ps = np.array(ps, dtype=object).astype(np.int64)
    fams = {'STAR': [e for e in star_events(Y1, Ylo) if e[1] % 4 == 1], 'B1': b1_events(Y2), 'c3': [e for e in cline_events(3, Y2) if e[1] % 4 == 1],
            'c2': [e for e in cline_events(2, Y2) if e[1] % 4 == 1], 'QR': qr_events(Y2)}
    C = {k: counts(ps, v) for k, v in fams.items()}
    print(f'# {len(ps)} primes p ≡ 1 (4) from {lo}; STAR_top {Ylo} < uv <= {Y1}, others <= {Y2}; events: ' + ', '.join(f'{k} {len(v)}' for k, v in fams.items()))
    for k in fams: print(f'  {k}: mean {C[k].mean():.4f}  model mean {sum(2.0 / phi(q) for q, a in fams[k]):.4f}')
    for a, b in [('STAR', 'c3'), ('STAR', 'c2'), ('STAR', 'B1'), ('STAR', 'QR'), ('c2', 'c3')]:
        emp = np.cov(C[a], C[b])[0, 1]; mod = crt_cov(fams[a], fams[b])
        sd = math.sqrt(C[a].var() * C[b].var())
        print(f'  {a}-{b}: empirical cov {emp:+.5f} (corr {emp / sd:+.3f}, s.e.~{1 / math.sqrt(len(ps)):.3f})  CRT-model cov {mod:+.5f} (corr {mod / sd:+.3f})')

if __name__ == '__main__':
    main()
