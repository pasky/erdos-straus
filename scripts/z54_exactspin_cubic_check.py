# z54 EXACTSPIN: CERTIFIED check of the spin dictionary (Lemma 4.2, k = 3; Lemma 4.4, k = 4) on actual shell points.
# For each shell point (u = l prime, w, w'') with l = 1 (mod k) (dump from z54_exactspin_engine), with x = -w'' mod l:
#  k=3: pi = a + b*omega primary (pi = 2 mod 3) of norm l;  checks (x/pi)_3 == (pi/p)_3 * conj((pi/2w)_3), where
#       (pi/n)_3 = prod over primes q | n of (pi/q)_3 computed from the definition (split q: product over both primes above q;
#       inert q: pi^((q^2-1)/3) mod q), and the anticyclotomic forms (pi/q)_3 = ((pi/pibar)/Q)_3 (split) and
#       (pibar/pi)^((q+1)/3) mod q (inert).
#  k=4: pi = a + b i primary (pi = 1 mod 2+2i) of norm l; computes eps := (x/pi)_4 / [ (pi/p)_4 * conj((pi/w)_4) ] and checks that
#       eps is a function of (pi mod 16, w mod 4) only (and records the table).
# Usage: python z54_exactspin_cubic_check.py p dumpfile
import sys
from sympy import factorint, isprime
from sympy.ntheory import sqrt_mod
p = int(sys.argv[1]); pts = [tuple(map(int, l.split())) for l in open(sys.argv[2])]
# ---------- Z[omega]: elements (a, b) = a + b w, w^2 = -1 - w ----------
def emul(x, y, m=None):
    a, b = x; c, d = y
    r = (a*c - b*d, a*d + b*c - b*d)
    return (r[0] % m, r[1] % m) if m else r
def epow(x, e, m):
    r = (1, 0); x = (x[0] % m, x[1] % m)
    while e:
        if e & 1: r = emul(r, x, m)
        x = emul(x, x, m); e >>= 1
    return r
def econj(x): a, b = x; return (a - b, -b)          # conj(w) = w^2 = -1 - w
def enorm(x): a, b = x; return a*a - a*b + b*b
def eprimary(l):  # primary prime of norm l (l = 1 mod 3): a + b w = 2 mod 3
    for a in range(-int(2*l**0.5)-2, int(2*l**0.5)+3):
        # b from a*a - a b + b b = l
        disc = 4*l - 3*a*a
        if disc < 0: continue
        s = int(round(disc ** 0.5))
        for ss in (s-1, s, s+1):
            if ss >= 0 and ss*ss == disc:
                for b in ((a + ss) // 2, (a - ss) // 2):
                    if b*b - a*b + a*a == l and (a % 3, b % 3) == (2, 0): return (a, b)
    raise ValueError(l)
W = [(1, 0), (0, 1), (-1, -1)]  # 1, w, w^2
def eidx(val, m):  # val = w^j mod m (m rational modulus) -> j
    for j, z in enumerate(W):
        if ((val[0] - z[0]) % m, (val[1] - z[1]) % m) == (0, 0): return j
    raise ValueError((val, m))
def cub_sym_q(pi, q):  # (pi / q)_3 as exponent j of w, q rational prime != 3, q not dividing N(pi)
    if q % 3 == 2:  # inert
        return eidx(epow(pi, (q*q - 1) // 3, q), q)
    # split: q = Q Qbar, Q = (q, w - r), r root of x^2+x+1 mod q; (pi/Q)_3 = pi^((q-1)/3) mod Q, identify w -> r
    r = [t for t in sqrt_mod(-3, q, all_roots=True)][0]; r = ((-1 + r) * pow(2, -1, q)) % q   # root of x^2+x+1
    j = 0
    for rr in (r, (-1 - r) % q):   # Q: w -> rr ; Qbar: w -> the other root
        v = pow((pi[0] + pi[1] * rr) % q, (q - 1) // 3, q)
        jj = [t for t in range(3) if pow(rr, t, q) == v]
        assert len(jj) == 1; j += jj[0]
    return j % 3
def cub_sym_n(pi, n):
    return sum(cub_sym_q(pi, q) * e for q, e in factorint(n).items()) % 3
def anticyc_q(pi, q):  # anticyclotomic form: depends on theta = pi/pibar only
    th_num, th_den = pi, econj(pi)
    if q % 3 == 2:
        # (pibar/pi)^((q+1)/3) mod q = pibar^((q+1)/3) * pi^(-(q+1)/3); compute pi^{-1} = pibar * N(pi)^{-1}
        Ninv = pow(enorm(pi), -1, q)
        inv = ((econj(pi)[0] * Ninv) % q, (econj(pi)[1] * Ninv) % q)
        t = emul(econj(pi), inv, q)          # pibar/pi
        return eidx(epow(t, (q + 1) // 3, q), q)
    r = [t for t in sqrt_mod(-3, q, all_roots=True)][0]; r = ((-1 + r) * pow(2, -1, q)) % q
    a = (pi[0] + pi[1] * r) % q; c = econj(pi); bb = (c[0] + c[1] * r) % q
    v = pow(a * pow(bb, -1, q) % q, (q - 1) // 3, q)
    return [t for t in range(3) if pow(r, t, q) == v][0]
# ---------- Z[i] ----------
def gmul(x, y, m=None):
    a, b = x; c, d = y; r = (a*c - b*d, a*d + b*c)
    return (r[0] % m, r[1] % m) if m else r
def gpow(x, e, m):
    r = (1, 0); x = (x[0] % m, x[1] % m)
    while e:
        if e & 1: r = gmul(r, x, m)
        x = gmul(x, x, m); e >>= 1
    return r
I4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def gidx(val, m):
    for j, z in enumerate(I4):
        if ((val[0] - z[0]) % m, (val[1] - z[1]) % m) == (0, 0): return j
    raise ValueError
def gprimary(l):  # a + bi, norm l, primary: b even, a + b = 1 mod 4
    for a in range(-int(l**0.5)-1, int(l**0.5)+2):
        b2 = l - a*a
        if b2 < 0: continue
        b = int(round(b2 ** 0.5))
        for bb in (b, -b):
            if bb*bb == b2 and bb % 2 == 0 and (a + bb) % 4 == 1: return (a, bb)
    raise ValueError(l)
def quart_sym_q(pi, q):  # (pi/q)_4, q odd rational prime not dividing N(pi)
    if q % 4 == 3: return gidx(gpow(pi, (q*q - 1) // 4, q), q)
    r = sqrt_mod(-1, q); j = 0
    for rr in (r, q - r):
        v = pow((pi[0] + pi[1] * rr) % q, (q - 1) // 4, q)
        jj = [t for t in range(4) if pow(rr, t, q) == v]; assert len(jj) == 1; j += jj[0]
    return j % 4
def quart_sym_n(pi, n): return sum(quart_sym_q(pi, q) * e for q, e in factorint(n).items()) % 4
# ---------- run ----------
RHO = gprimary(p)
n3 = bad3 = badac = bad3sup = 0; t3 = {}; n3w2 = bad3w2 = 0; bad4eps = bad4b = bad4c = n4c = bad4ac = 0; n4 = 0; table = {}; bad4 = 0
for (u, w, w2, isq, hit) in pts:
    if not isprime(u): continue
    x = (-w2) % u
    if u % 3 == 1:
        pi = eprimary(u)
        # (x/pi)_3: x^((u-1)/3) mod u, with w = -a/b mod pi
        wr = (-pi[0] * pow(pi[1], -1, u)) % u
        v = pow(x, (u - 1) // 3, u); jx = [t for t in range(3) if pow(wr, t, u) == v][0]
        v3 = 1 if w % 3 == 0 else 0; w1 = w // 3 if v3 else w
        jp = cub_sym_n(pi, p); jw = cub_sym_n(pi, 2 * w1)
        # supplementary factor (3/pi)_3 (3 is ramified; cubic reciprocity needs 3 not dividing n); check it depends only on pi mod 9
        v = pow(3, (u - 1) // 3, u); j3 = [t for t in range(3) if pow(wr, t, u) == v][0]
        k9 = (pi[0] % 9, pi[1] % 9)
        if k9 in t3 and t3[k9] != j3: bad3sup += 1
        t3.setdefault(k9, j3)
        n3 += 1
        if jx != (jp - jw - v3 * j3) % 3: bad3 += 1
        if w2 % 3 != 0:                      # w'' version of 4.2(a): (x/pi)_3 = (pi/w'')_3
            n3w2 += 1
            if jx != cub_sym_n(pi, w2): bad3w2 += 1
        for q in list(factorint(2 * w1 * p).keys()):
            if cub_sym_q(pi, q) != anticyc_q(pi, q): badac += 1
    if u % 4 == 1:
        pi = gprimary(u)
        ir = (-pi[0] * pow(pi[1], -1, u)) % u   # i = -a/b mod pi
        v = pow(x, (u - 1) // 4, u); jx = [t for t in range(4) if pow(ir, t, u) == v][0]
        jp = quart_sym_n(pi, p); jw = quart_sym_n(pi, w)
        eps = (jx - jp + jw) % 4
        key = ((pi[0] % 16, pi[1] % 16), w % 4)
        if key in table and table[key] != eps: bad4 += 1
        table.setdefault(key, eps); n4 += 1
        # explicit eps formula: eps = (-1/pi)_4 (2/pi)_4^{-1} [ (-1/pi)_4^{-1} if w = 3 mod 4 ]
        jm1 = 0 if ((u - 1) // 4) % 2 == 0 else 2
        v2 = pow(2, (u - 1) // 4, u); j2 = [t for t in range(4) if pow(ir, t, u) == v2][0]
        epsf = (jm1 - j2 - (jm1 if w % 4 == 3 else 0)) % 4
        if epsf != eps: bad4eps += 1
        # 4.4(b): (pi/p)_4 = (l/rho)_4^{-1} (pi/rho)_2, rho primary of norm p, i = -a/b mod rho
        rho = RHO; irho = (-rho[0] * pow(rho[1], -1, p)) % p
        pim = (pi[0] + pi[1] * irho) % p
        jl = [t for t in range(4) if pow(irho, t, p) == pow(u, (p - 1) // 4, p)][0]
        s2 = 0 if pow(pim, (p - 1) // 2, p) == 1 else 2
        if jp != (-jl + s2) % 4: bad4b += 1
        # 4.4(c) and quartic anticyclotomic forms for every prime q | w
        for q in factorint(w):
            jq = quart_sym_q(pi, q)
            if q % 4 == 1:
                n4c += 1
                r = sqrt_mod(-1, q); a = (pi[0] + pi[1] * r) % q          # kappa = (q, i - r)
                sq = 0 if pow(a, (q - 1) // 2, q) == 1 else 2
                jmp = [t for t in range(4) if pow(r, t, q) == pow((-p) % q, (q - 1) // 4, q)][0]
                if jq != (sq - jmp) % 4: bad4c += 1
                bb = (pi[0] - pi[1] * r) % q                              # pibar mod kappa
                th = a * pow(bb, -1, q) % q
                jac = [t for t in range(4) if pow(r, t, q) == pow(th, (q - 1) // 4, q)][0]
            else:
                Ninv = pow(u, -1, q); inv = ((pi[0] * Ninv) % q, (-pi[1] * Ninv) % q)   # pi^{-1} = pibar / N
                t_ = gmul((pi[0], -pi[1]), inv, q)                                         # pibar/pi
                jac = gidx(gpow(t_, (q + 1) // 4, q), q)
            if jq != jac: bad4ac += 1
print(f'p={p} cubic: {n3} shell points (u prime = 1 mod 3), reciprocity mismatches {bad3}, anticyclotomic-form mismatches {badac}, (3/pi)_3 not a function of pi mod 9: {bad3sup}; '
      f'quartic: {n4} points, eps not a function of (pi mod 16, w mod 4): {bad4} (table size {len(table)}); '
      f'cubic w2-version: {n3w2} points, mismatches {bad3w2}; quartic explicit-eps mismatches {bad4eps}, 4.4(b) mismatches {bad4b}, '
      f'4.4(c): {n4c} split factors, mismatches {bad4c}; quartic anticyclotomic-form mismatches {bad4ac}')
