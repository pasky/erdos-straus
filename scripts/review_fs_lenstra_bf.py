#!/usr/bin/env python3
"""R217 from-scratch brute force of FF_STERILE_PUSH Lemmas 1.4 (FF Lenstra) and 1.5 (FF Coppersmith).

For F over F_p (product of known irreducibles, so all divisors are known), every degree d, every monic Q of degree rho
(rho in a range), we compute max over unit classes sigma mod Q of #{divisors E of F (monic OR NOT), deg E = d, E = sigma mod Q}
and compare with the claimed bounds:
  L1.4:  d < rho or n - d < rho  =>  <= 1 ;   3 rho > n  =>  <= 2
  L1.5:  rho <= d <= n, X = d - rho, (m,k) with Delta(m,k) < (m+k+1) m d  =>  <= m + k
Also reports the tightness (how often bound is attained).
Usage: review_fs_lenstra_bf.py p nmax trials seed
"""
import sys, random, itertools

def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a

def mul(a, b, p):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return trim(r)

def polmod(a, m, p):
    a = list(a)
    inv = pow(m[-1], p - 2, p)
    dm = len(m) - 1
    while len(a) - 1 >= dm and a:
        c = a[-1] * inv % p
        sh = len(a) - 1 - dm
        for i, y in enumerate(m):
            a[sh + i] = (a[sh + i] - c * y) % p
        trim(a)
    return a

def gcd(a, b, p):
    a, b = trim(list(a)), trim(list(b))
    while b:
        a, b = b, polmod(a, b, p)
    return a

def monic_polys(deg, p):
    for coeffs in itertools.product(range(p), repeat=deg):
        yield list(coeffs) + [1]

def irreducibles(deg, p):
    out = []
    for f in monic_polys(deg, p):
        ok = True
        for d in range(1, deg // 2 + 1):
            for g in monic_polys(d, p):
                if not polmod(f, g, p):
                    ok = False; break
            if not ok:
                break
        if ok:
            out.append(f)
    return out

def delta(n, d, X, m, k):
    return n * m * (m + 1) // 2 + X * (m * (m + 1) // 2 + k * m + k * (k + 1) // 2)

def cop_bound(n, d, rho, mmax=12, kmax=40):
    if d < rho or rho < 1:
        return None
    X = d - rho
    best = None
    for m in range(1, mmax + 1):
        for k in range(0, kmax + 1):
            if delta(n, d, X, m, k) < (m + k + 1) * m * d:
                if best is None or m + k < best:
                    best = m + k
    return best

# special highly factorable F: all monic irreducibles of degree 1 and 2 (= (T^(p^2)-T)), with/without squares
SPECIAL = {
    3: [lambda irr: irr[1] + irr[2], lambda irr: irr[1] + irr[1] + irr[2], lambda irr: irr[1] * 3 + irr[2][:2],
        lambda irr: irr[1] + irr[2] + irr[3][:1]],
    5: [lambda irr: irr[1] + irr[2][:3], lambda irr: irr[1] * 2 + irr[2][:1]],
    7: [lambda irr: irr[1] + irr[2][:2], lambda irr: irr[1] * 2],
}

def main():
    p, nmax, trials, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    rng = random.Random(seed)
    irr = {1: irreducibles(1, p), 2: irreducibles(2, p), 3: irreducibles(3, p)}
    viol = 0; groups = 0; attained = {}
    Qcache = {}
    for tr in range(trials):
        # random highly factorable F: product of random small irreducibles (repetition allowed)
        n = rng.randint(4, nmax)
        facs = []; deg = 0
        while deg < n:
            dd = rng.choice([1, 1, 1, 2, 2, 3])
            if deg + dd > n:
                dd = n - deg
                if dd > 3: dd = 1
            facs.append(rng.choice(irr[dd])); deg += dd
        if tr < len(SPECIAL.get(p, [])):
            facs = SPECIAL[p][tr](irr); n = sum(len(f) - 1 for f in facs)
        # divisors as monic products of sub-multisets
        from collections import Counter
        cnt = Counter(tuple(f) for f in facs)
        items = list(cnt.items())
        divs = set()
        for exps in itertools.product(*[range(e + 1) for _, e in items]):
            D = [1]
            for (f, _), e in zip(items, exps):
                for _ in range(e):
                    D = mul(D, list(f), p)
            divs.add(tuple(D))
        bydeg = {}
        for D in divs:
            bydeg.setdefault(len(D) - 1, []).append(list(D))
        rhomax = min(n, 5 if p == 3 else 3)
        for rho in range(1, rhomax + 1):
            if rho not in Qcache:
                Qcache[rho] = list(monic_polys(rho, p))
            for Q in Qcache[rho]:
                for d, Ds in bydeg.items():
                    classes = {}
                    for D in Ds:
                        r0 = polmod(D, Q, p)
                        if len(gcd(r0, Q, p)) != 1:   # not a unit mod Q
                            continue
                        for lam in range(1, p):
                            r = tuple(x * lam % p for x in r0)
                            classes[r] = classes.get(r, 0) + 1
                    if not classes:
                        continue
                    M = max(classes.values())
                    groups += 1
                    bounds = []
                    if d < rho or n - d < rho:
                        bounds.append(('triv', 1))
                    if 3 * rho > n:
                        bounds.append(('L14', 2))
                    cb = cop_bound(n, d, rho)
                    if cb is not None:
                        bounds.append(('L15', cb))
                    if 3 * rho <= n and cb is not None and not (d < rho or n - d < rho):
                        key = ('L15only', cb, M)
                        attained[key] = attained.get(key, 0) + 1
                    for name, b in bounds:
                        if M > b:
                            viol += 1
                            print('VIOLATION', name, 'p', p, 'n', n, 'd', d, 'rho', rho, 'M', M, 'bound', b, 'F', facs, 'Q', Q)
                        elif M == b and M >= 2:
                            attained[name] = attained.get(name, 0) + 1
    print(f'p={p} trials={trials} groups={groups} violations={viol} attained(>=2)={attained}')

if __name__ == '__main__':
    main()
