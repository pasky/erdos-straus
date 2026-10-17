"""Determined-lift recombination gate (O253 §3).
Source: a prime n' with p = alpha*n' + beta.  A source ET witness w' (modulus H') pins p mod alpha*H'.
Any lift whose output modulus H divides alpha*H' (the only part of p visible from w') succeeds iff
p has an ET witness with H | alpha*H'.  This script computes, for each source witness, whether that holds
(an upper bound for every congruence-mediated lift), i.e. whether the law 'W(n') != {} => W(p) != {}'
can be total through determined lifts.
Usage: z25_gate.py fixtures | mordell N
"""
import sys
from math import gcd
from sympy import isprime, primerange, divisors
from z25_common import W


def et_reps(n, sols):
    """all (type, a, b, c, d, H) ET representations of the solutions of 4/n (n prime)."""
    out = []
    for idx, s in enumerate(sols):
        dv = [t % n == 0 for t in s]
        if sum(dv) == 1:      # Type I: x = n a b d, y = a c d, z = b c d
            typ = 'I'
            X = [t for t, f in zip(s, dv) if f][0] // n
            Y, Z = [t for t, f in zip(s, dv) if not f]
        elif sum(dv) == 2:    # Type II: x = a b d, y = n a c d, z = n b c d
            typ = 'II'
            X = [t for t, f in zip(s, dv) if not f][0]
            Y, Z = [t // n for t, f in zip(s, dv) if f]
        else:
            continue
        for m in divisors(gcd(Y, Z)):         # m = c d
            a, b = Y // m, Z // m
            if X % (a * b):
                continue
            d = X // (a * b)
            if m % d:
                continue
            c = m // d
            if (a + b) % c == 0:
                out.append((typ, a, b, c, d, 4 * a * b, idx))
    return out


def Hset(n):
    sols = W(n)
    reps = et_reps(n, sols)
    assert len({(r[0],) for r in reps}) >= 1 or not sols
    return sols, reps


def gate(p, src, alpha):
    _, rp = Hset(p)
    Hp = sorted({r[5] for r in rp})
    _, rs = Hset(src)
    wit = {}
    for r in rs:   # group reps by witness index; a witness passes if any of its reps passes
        ok = any((alpha * r[5]) % H == 0 for H in Hp)
        wit[r[6]] = wit.get(r[6], False) or ok
    npass = sum(wit.values())
    return len(wit), npass


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'fixtures':
        for p in [97, 193, 313, 3361, 5209, 233689]:
            srcs = []
            for j in range(-12, 13):
                if j and isprime(p + j) and p + j > 3:
                    srcs.append((p + j, 1))
            for g in (2, 3, 4, 6, 8, 12):
                for j in range(-12, 13):
                    if (p + j) % g == 0 and isprime((p + j) // g) and (p + j) // g > 3:
                        srcs.append(((p + j) // g, g))
            if p > 10000:
                srcs = [s for s in srcs if s[1] >= 2][:4]
            res = []
            for src, g in srcs:
                n, k = gate(p, src, g)
                res.append(f"{src}(x{g}):{k}/{n}")
            print(p, ' '.join(res), flush=True)
    else:
        N = int(sys.argv[2])
        M = {1, 121, 169, 289, 361, 529}
        tot = full = zero = 0
        for p in primerange(5, N):
            if p % 840 not in M:
                continue
            v = (p + 1) // 2
            if not isprime(v):
                continue
            n, k = gate(p, v, 2)
            tot += 1
            full += (k == n)
            zero += (k == 0)
            print(p, v, f"{k}/{n}", flush=True)
        print('primes p in Mordell classes with v=(p+1)/2 prime:', tot, 'gate total:', full, 'gate empty:', zero)


def joint_fixture(p, srcs):
    """Joint (multi-source) determined lifts: the tuple of source witnesses pins p mod L = lcm(alpha_i H'_i).
    Law total iff for EVERY tuple p has an ET witness with H | L.  Search for an adversarial tuple (DFS)."""
    from math import lcm
    _, rp = Hset(p)
    Hp = sorted({r[5] for r in rp})
    opts = []
    for src, g in srcs:
        _, rs = Hset(src)
        mods = {}
        for r in rs:
            mods.setdefault(r[6], set()).add(g * r[5])
        # a witness is usable by the adversary only through the lcm of all its reps' moduli? no: the
        # prover may pick any rep, so the information is the lcm of all its rep moduli
        ms = sorted({lcm(*v) for v in mods.values()})
        opts.append([m for m in ms if not any(m % H == 0 for H in Hp)])
    if any(not o for o in opts):
        return None
    opts.sort(key=len)
    sys.setrecursionlimit(10000)
    def dfs(i, L):
        if any(L % H == 0 for H in Hp):
            return None
        if i == len(opts):
            return []
        for m in opts[i]:
            r = dfs(i + 1, lcm(L, m))
            if r is not None:
                return [m] + r
        return None
    return dfs(0, 1)
