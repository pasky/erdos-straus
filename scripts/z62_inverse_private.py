#!/usr/bin/env python3
"""z62 INVERSE test 3: are the PRIVATE parts of the u-slices coupled?  For each prime p = 1 (24) and u <= U write
p+u = s_u * c_u with s_u the z-smooth part coprime-to-4u-part ... precisely: s_u = product of prime powers l^e || p+u with
l <= z (l not dividing 4u), c_u = the part composed of primes > z.  Visible signature of slice u:
  fine:   (u, frozenset(Div(s_u) mod 4u), min(omega(c_u),3), chi_{-4u}(c_u));
  coarse: (u, [-1 in Div(s_u)], min(omega(c_u),3), k = #{d in Div(s_u): chi_{-4u}(d) = -chi_{-4u}(c_u)})
          (for prime c_u the slice hits iff c_u = -1/d for some such d, so k is the natural target count).
Independence model: P(all u <= U fail) = prod_u P(F_u | signature_u), estimated leave-one-out over all primes.
Unique signatures (n = 0 after leave-one-out) contribute factor 1. O/E >> 1 would mean the private (large-prime) layers of different slices are coupled. Usage: jointfile U z [coarse]"""
import sys, collections
import numpy as np
fn = sys.argv[1]; U = int(sys.argv[2]); z = int(sys.argv[3]); COARSE = len(sys.argv) > 4 and sys.argv[4] == 'coarse'; d_ok = COARSE
ps = []; hs = []
for l in open(fn):
    p, s = l.split(); ps.append(int(p)); hs.append(s[:U])
M = max(ps) + U + 1
spf = np.zeros(M + 1, dtype=np.int32)
for i in range(2, int(M ** 0.5) + 1):
    if spf[i] == 0:
        blk = spf[i * i::i]; blk[blk == 0] = i
spf_l = spf  # 0 means prime
def factor(n):
    out = []
    while n > 1:
        q = int(spf_l[n]) or n
        e = 0
        while n % q == 0: n //= q; e += 1
        out.append((q, e))
    return out
def kron_m4u(u, c):  # chi_{-4u}(c) for odd c coprime to u: Jacobi (-u/c) via sympy-free routine
    a, n, t = (-u) % c, c, 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0
sigs = []
for p in ps:
    row = []
    for u in range(1, U + 1):
        m = 4 * u; Div = {1}; om = 0; c = 1
        for q, e in factor(p + u):
            if m % q == 0: continue
            if q <= z:
                new = set(); pw = 1
                for _ in range(e + 1):
                    for x in Div: new.add(x * pw % m)
                    pw = pw * q % m
                Div = new
            else:
                om += e; c *= q ** e
        chi_c = kron_m4u(u, c) if c > 1 else 1
        k = sum(1 for d in Div if kron_m4u(u, d) == -chi_c) if d_ok else 0
        row.append((u, (m - 1) in Div, min(om, 3), k) if COARSE else (u, frozenset(Div), min(om, 3), chi_c))
    sigs.append(row)
cnt = collections.Counter(); fl = collections.Counter()
for row, s in zip(sigs, hs):
    for k, sg in enumerate(row):
        cnt[sg] += 1; fl[sg] += (s[k] == '0')
for UU in (8, 16, 32, 64):
    if UU > U: break
    O = 0; E = 0.0
    for row, s in zip(sigs, hs):
        pr = 1.0
        for k in range(UU):
            sg = row[k]; n = cnt[sg] - 1; f = fl[sg] - (s[k] == '0')
            pr *= (f / n) if n > 0 else 1.0
        E += pr; O += ('1' not in s[:UU])
    print(f'z={z} U={UU}: signatures={len(cnt)} O={O} E={E:.2f} O/E={O/E if E else float("nan"):.2f}')
