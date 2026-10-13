"""FF_MUTE (O195): check Lemma 3.2 (sign formulas) on every f, and Theorem 3.5's lower bound for G(d).

usage: fm_count.py p A s d P1 [P2 ...]   (digit strings high->low)
For each P: enumerates all monic irreducible f of degree d, f = -1 mod A, f not dividing M = A P s, and
 * checks (ii) [-P/A square mod f, Euler criterion in R/f] <=> (f/P) == tau  (Legendre via Euler mod P),
 * checks for each prime l | p-1: [s^{(p^d-1)/l} == 1 mod f] <=> [f^{(p^h-1)/l} mod s == eps_l^{dh}],
 * counts G(d) = #{f with (i),(ii),(iii)} (primitivity by exact order of s mod f),
 and prints G(d), main term delta*p^d/d, and the Theorem 3.5 lower bound.
"""
import sys, math
from fm_poly import Fp, parse, show

p = int(sys.argv[1]); F = Fp(p)
A = parse(sys.argv[2]); s = parse(sys.argv[3]); d = int(sys.argv[4])
k = len(A) - 1; h = len(s) - 1


def primes_of(m):
    out = []; x = 2
    while x * x <= m:
        if m % x == 0:
            out.append(x)
            while m % x == 0:
                m //= x
        x += 1
    if m > 1:
        out.append(m)
    return out


Qd = p ** d
eps = 1 if (p - 1) // 2 % 2 == 0 else -1
lq = primes_of(p - 1)
lQ = primes_of(Qd - 1)
PhiA = 1
for g in [A]:
    pass
# Phi(A) by brute count of units mod A
PhiA = sum(1 for a in range(p ** k) if len(F.gcd(A, F.trim([(a // p ** i) % p for i in range(k)]) or (0,))) == 1) if k else 1
delta = math.prod(1 - 1 / l for l in lq) / ((2 if p % 2 else 1) * PhiA)  # c_q = 1 in char 2 (R195 M4)
minus1 = F.mod((p - 1,), A)

fs = [f for f in F.irreducibles(d) if F.mod(f, A) == minus1]

for Pstr in sys.argv[5:]:
    P = parse(Pstr); n = len(P) - 1
    tau = eps ** (d * (1 + n + k) + k)
    G = 0; mism = 0; tested = 0
    for f in fs:
        if not F.mod(P, f) or not F.mod(s, f) or f == P:
            continue
        tested += 1
        Ainv = F.egcd_inv(A, f)
        t = F.mod(F.neg(F.mul(P, Ainv)), f)
        if p % 2:
            sq = F.powmod(t, (Qd - 1) // 2, f) == (1,)
            leg = F.powmod(f, (p ** n - 1) // 2, P)
            legv = 1 if leg == (1,) else -1
            mism += (sq != (legv == tau))
        else:
            sq = True  # char 2: every element of F_{2^d} is a square
        for l in lq:
            pw = F.powmod(s, (Qd - 1) // l, f) == (1,)
            sym = F.powmod(f, (p ** h - 1) // l, s)
            el = (-1) ** (((p - 1) // l) * d * h)
            mism += (pw != (sym == ((el % p),)))
        prim = all(F.powmod(s, (Qd - 1) // l, f) != (1,) for l in lQ)
        G += sq and prim
    D = k + n + h
    md = math.floor(d * math.log(p) / math.log(2 * d + 1))
    Ld = (1 + math.log(max(md, 1))) / (2 * d)
    om = len(lq)
    lb = ((delta - Ld) * Qd - Qd ** 0.5 * (2 * delta + 2 ** om * (D + 1) + md * (h - 1)) - delta * D) / d
    print(f"q={p} A={show(A)} s={show(s)} d={d} P={Pstr}: f tested={tested} lemma3.2 mismatches={mism} "
          f"G(d)={G} main={delta * Qd / d:.1f} bound={lb:.1f}")
