"""O250 CAP_BOUNDED §5: caps at FORCED windows vs unforced ones, and explicit (discrete-log-free) witnesses.

For primes p = 1 (mod 8), p <= N.  Prime windows q = 3 (mod 4), q <= Q0, q != p:
  forced  : (q/p) = -1  (CAP_DOWN Thm 1.2: every such q is a window with finite cap when p = 1 mod 8)
  unforced: (q/p) = +1
Exact Lemma-3.1 cap (delta_p included) is computed up to EMAX (larger caps recorded as > EMAX).
Explicit witnesses at a forced window (no discrete logs):
  W13 = CAP_DOWN Prop 1.3: min over odd s | K' with b_s odd, (s/q) = -1 of max(0, (ord_q(s)/2 - b_s)/2)
  W23 = CAP_BOUNDED Prop 2.3 (K odd only): (o-1)/2 * max b_s, o = odd part of ord_q(p/4)
usage: z22_forced_caps.py N Q0 EMAX KFIRST VER [HARD]   (HARD=1: only Mordell-hard p mod 840)
"""
import sys
from math import isqrt
from sympy import primerange, n_order
from z22_common import best_cap, verify

N, Q0, EMAX, KF, VER = map(int, sys.argv[1:6]); HARD = int(sys.argv[6]) if len(sys.argv) > 6 else 0
LIM = (N + Q0) // 4 + 2
spf = list(range(LIM + 1))
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == i:
        for j in range(i * i, LIM + 1, i):
            if spf[j] == j:
                spf[j] = i


def fac(k):
    f = {}
    while k > 1:
        s = spf[k]; f[s] = f.get(s, 0) + 1; k //= s
    return f


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


Qs = [q for q in primerange(3, Q0 + 1) if q % 4 == 3]
P = [p for p in primerange(5, N + 1) if p % 8 == 1 and (not HARD or p % 840 in (1, 121, 169, 289, 361, 529))]
st = {'f_tot': 0, 'f_cap0': 0, 'f_cap1': 0, 'u_tot': 0, 'u_cap0': 0, 'u_cap1': 0}
bins = {}  # q-bin -> [forced n, forced cap0, unforced n, unforced cap0]
first_f0 = {}; firstidx0 = {}; best_first = {}; Whist = {}; W23hist = {}; nver = 0; noforced = 0
rec = []
for p in P:
    nf = 0; f0 = None; i0 = None; bestk = None; W = None; W23b = None
    for q in Qs:
        if q == p:
            continue
        forced = pow(p, (q - 1) // 2, q) == q - 1
        if forced and nf >= KF:
            continue
        K = (p + q) // 4
        fK = fac(K)
        c = best_cap(p, q, EMAX, usep=True, fK=fK)
        bn = min(q // 100, 9)
        bb = bins.setdefault(bn, [0, 0, 0, 0])
        if forced:
            nf += 1
            st['f_tot'] += 1; bb[0] += 1
            if c is not None and c[0] == 0:
                st['f_cap0'] += 1; bb[1] += 1
                if f0 is None:
                    f0, i0 = q, nf
            if c is not None and c[0] <= 1:
                st['f_cap1'] += 1
            if nf == 1:
                bestk = c[0] if c is not None else EMAX + 1
            # explicit witnesses
            Kp = K; t = 0
            while Kp % 2 == 0:
                Kp //= 2; t += 1
            w13 = None
            for s, b in fK.items():
                if s != 2 and b % 2 == 1 and pow(s, (q - 1) // 2, q) == q - 1:
                    o = n_order(s, q)
                    w = max(0, (o // 2 - b + 1) // 2)
                    w13 = w if w13 is None else min(w13, w)
            w23 = None
            if t == 0:
                o = oddpart(n_order(p * pow(4, -1, q) % q, q))
                w23 = (o - 1) // 2 * max(fK.values())
                W23b = w23 if W23b is None else min(W23b, w23)
            ws = [w for w in (w13, w23) if w is not None]
            if ws:
                W = min(ws) if W is None else min(W, min(ws))
            if VER and c is not None and nver < VER:
                verify(p, q, c[1], c[0]); nver += 1
        else:
            st['u_tot'] += 1; bb[2] += 1
            if c is not None and c[0] == 0:
                st['u_cap0'] += 1; bb[3] += 1
            if c is not None and c[0] <= 1:
                st['u_cap1'] += 1
    if nf == 0:
        noforced += 1; continue
    key = 'none<=%d' % KF if i0 is None else i0
    firstidx0[key] = firstidx0.get(key, 0) + 1
    best_first[bestk] = best_first.get(bestk, 0) + 1
    Whist[W] = Whist.get(W, 0) + 1
    W23hist[W23b] = W23hist.get(W23b, 0) + 1
    if i0 is None or (W is not None and W >= 3):
        rec.append((p, i0, W))
print('N', N, 'Q0', Q0, 'EMAX', EMAX, 'first forced windows used', KF, 'primes', len(P), 'no forced window <= Q0', noforced,
      'verified', nver)
print('rates: forced windows %d, cap0 %.4f, cap<=1 %.4f | unforced %d, cap0 %.4f, cap<=1 %.4f' % (
    st['f_tot'], st['f_cap0'] / st['f_tot'], st['f_cap1'] / st['f_tot'], st['u_tot'], st['u_cap0'] / st['u_tot'],
    st['u_cap1'] / st['u_tot']))
print('cap0 rate by q-bin (x100): forced/unforced', {k: (round(v[1] / max(1, v[0]), 3), round(v[3] / max(1, v[2]), 3))
                                                      for k, v in sorted(bins.items())})
print('cap at the least forced window (>EMAX as EMAX+1):', dict(sorted(best_first.items())))
print('index of first forced window with cap 0:', dict(sorted(firstidx0.items(), key=lambda t: str(t[0]))))
print('best explicit witness cap W over first forced windows:', dict(sorted(Whist.items(), key=lambda t: str(t[0]))))
print('best odd-order witness (Prop 2.3, K odd windows):', dict(sorted(W23hist.items(), key=lambda t: str(t[0]))))
print('primes with no cap-0 among first forced windows or W>=3 (first 30):', rec[:30], 'total', len(rec))
print('no cap-0 among the first forced windows:', [r for r in rec if r[1] is None])
print('max W:', max((r for r in rec if r[2] is not None), key=lambda r: r[2], default=None))
