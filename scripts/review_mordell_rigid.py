"""R80 from-scratch: is x* (x*_q = u_q at q in T, 1 elsewhere) in any II1 / I4 / II2 class whose
modulus has T-part dividing prod q^K (T-free part unrestricted)?  Re-derived rigid forms:

II1/I4 (a,b,e), modulus 4ab, F = T-part of 4ab, N = 4ab/F.  x* in class forces N | e+1
  (II1: -e = 1 mod N; I4: -1/e = 1 mod N).  Put e+1 = N i, k = (a+b)/e:  4iabk = F(a+b+k).
  WLOG-free enumeration: all ordered (a,b,k); with s = min, the other two ... we simply bound:
  4iabk = F(a+b+k) <= 3F max(a,b,k)  =>  4i * (product of the two smaller) <= 3F.
  T-part test: II1: -e = u mod F ; I4: -1/e = u mod F (u = x* mod F by CRT).
II2 (a,d,f), modulus f = F g, g T-free. x* in class: g | 4a^2 d + 1, and 4ad | f+1.
  With 4adm = f+1: g | a+m; a+m = g j:  (4dja - F)(4djm - F) = F^2 + 4 d j^2, forcing j(4d-1) <= 2F.
  T-part test: -4a^2 d = u mod F.
Exact class membership is re-verified at the end on X = x* mod modulus (CRT).
usage: review_mordell_rigid.py K q:u [q:u ...]
"""
import sys
from math import gcd
from sympy import divisors

K = int(sys.argv[1]); spec = [tuple(map(int, s.split(':'))) for s in sys.argv[2:]]
T = [q for q, _ in spec]

def tpart(n):
    F = 1
    for q in T:
        while n % q == 0: n //= q; F *= q
    return F, n

def xmod(M):
    X, mod = 0, 1
    rest = M; parts = []
    for q, u in spec:
        qq = 1
        while rest % q == 0: rest //= q; qq *= q
        parts.append((qq, u))
    parts.append((rest, 1))
    for m, r in parts:
        if m == 1: continue
        t = ((r - X) * pow(mod, -1, m)) % m
        X, mod = X + mod*t, mod*m
    return X % M

Fs = [1]
for q in T: Fs = [F*q**i for F in Fs for i in range(K+1)]
hits = []; n1 = n2 = 0
import os
FMAX = int(float(os.environ.get('FMAX', '1e30')))
for F in Fs:
    if F > FMAX: continue
    # ---- II1 / I4: 4iabk = F(a+b+k); enumerate unordered smaller pair (s<=t) with 4 i s t <= 3F
    for i in range(1, 3*F//4+1):
        for s in range(1, 3*F//(4*i)+1):
            for t in range(s, 3*F//(4*i*s)+1):
                den = 4*i*s*t - F
                if den <= 0: continue
                num = F*(s+t)
                if num % den: continue
                w = num//den
                if w < t: continue
                trip = (s, t, w)
                # (a,b,k) any assignment of the multiset; k=(a+b)/e
                for (a, b, k) in {(trip[x], trip[y], trip[z]) for x, y, z in
                                  [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]}:
                    if (a+b) % k: continue
                    e = (a+b)//k
                    M = 4*a*b
                    if gcd(e, M) != 1: continue
                    n1 += 1
                    X = xmod(M)
                    if (X + e) % M == 0: hits.append(('II1', a, b, e, M))
                    if (X*e + 1) % M == 0: hits.append(('I4', a, b, e, M))
    # ---- II2
    for d in range(1, 2*F+1):
        for j in range(1, 2*F//(4*d-1)+1 if 4*d-1 > 0 else 1):
            R = F*F + 4*d*j*j
            for u1 in divisors(R):
                u2 = R//u1
                if (u1+F) % (4*d*j) or (u2+F) % (4*d*j): continue
                a = (u1+F)//(4*d*j); m = (u2+F)//(4*d*j)
                if (a+m) % j: continue
                g = (a+m)//j
                f = F*g
                if 4*a*d*m != f+1: continue
                n2 += 1
                if (xmod(f) + 4*a*a*d) % f == 0: hits.append(('II2', a, d, f, f))
print('F list', Fs)
print('II1/I4 candidates', n1, 'II2 candidates', n2)
print('hits', len(hits), hits[:20])
