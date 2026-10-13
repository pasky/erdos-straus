"""O181 DRINFELD_ES §2: Bright-Loughran classes alpha_zeta = (-u1/u3, -u2/u3)_zeta of order m | q-1 on the ES_q
surface A u1u2u3 = P(u1u2+u1u3+u2u3) over F_q(T) (q = p prime), evaluated on all monic NC solutions found by the
Lemma 1.3 divisor criterion (X of degree n - deg A). Local invariants via tame symbols, normalised as
log_w( N_{k(v)/F_q}({a,b}_v)^{(q-1)/m} ) in Z/m (Weil reciprocity: sum over all places incl. infinity = 0).
usage: bsH_bl_classes.py p gen m A n [pow]
Prints per P-group: #solutions, reciprocity failures, odd-part of inv_inf, places l not dividing AP with inv != 0,
joint distribution of (inv_P-part, inv_A-part)."""
import sys
from collections import Counter
from bsH_ff import FF

p, gen, m = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
Adig, n = sys.argv[4], int(sys.argv[5])
pw = len(sys.argv) > 6
F = FF(p)
A = tuple(int(c) for c in reversed(Adig))
kA = len(A) - 1
w = pow(gen, (p - 1) // m, p)
LOG = {pow(w, j, p): j for j in range(m)}


def inv(x):
    return pow(x, p - 2, p)


def solutions(P):
    sols = set()
    for X in F.monics(n - kA):
        E = F.sub(F.mul(A, X), P)
        if not E:
            continue
        N = F.mul(P, X)
        divs = F.monic_divisors(N)
        for a in divs:
            for b in divs:
                s = F.add(a, b)
                if not s or len(s) < len(E):
                    continue
                kap, r = F.divmod(s, E)
                if r or kap[-1] != 1:
                    continue
                Y = F.divmod(F.mul(kap, N), a)[0]
                Z = F.divmod(F.mul(kap, N), b)[0]
                sols.add((X, Y, Z))
    return sols


def val(f, l):
    v = 0
    while True:
        q_, r = F.divmod(f, l)
        if r:
            return v, f
        f, v = q_, v + 1


def sym_at(a, b, l):
    """a, b = (num, den) monic-or-scaled polys; tame symbol at finite prime l, returned in Z/m."""
    va1, an = val(a[0], l); va2, ad = val(a[1], l)
    vb1, bn = val(b[0], l); vb2, bd = val(b[1], l)
    va, vb = va1 - va2, vb1 - vb2
    def red(num, den):
        x = F.mod(num, l); y = F.mod(den, l)
        # x / y mod l
        yi = F.powmod(y, p ** (len(l) - 1) - 2, l)
        return F.mod(F.mul(x, yi), l)
    ua, ub = red(an, ad), red(bn, bd)
    # t = (-1)^{va vb} ua^{vb} / ub^{va}
    def ppow(x, e):
        if e >= 0:
            return F.powmod(x, e, l)
        xi = F.powmod(x, p ** (len(l) - 1) - 2, l)
        return F.powmod(xi, -e, l)
    t = F.mod(F.mul(ppow(ua, vb), ppow(ub, -va)), l)
    if (va * vb) % 2:
        t = F.neg(t)
    d = len(l) - 1
    Nt = F.powmod(t, (p ** d - 1) // (p - 1), l)
    assert len(Nt) == 1
    return LOG[pow(Nt[0], (p - 1) // m, p)]


def sym_inf(a, b):
    va = -((len(a[0]) - 1) - (len(a[1]) - 1)); vb = -((len(b[0]) - 1) - (len(b[1]) - 1))
    ua = a[0][-1] * inv(a[1][-1]) % p; ub = b[0][-1] * inv(b[1][-1]) % p
    t = pow(ua, vb % (p - 1), p) * pow(inv(ub), va % (p - 1), p) % p
    if (va * vb) % 2:
        t = (-t) % p
    return LOG[pow(t, (p - 1) // m, p)]


def primes_of(*polys):
    ps = set()
    for f in polys:
        for l, e in F.factor(f):
            ps.add(l)
    return ps


def run(lab, Ps):
    st = Counter(); joint = Counter(); infodd = Counter(); bad = Counter()
    for P in Ps:
        Pprimes = set(l for l, e in F.factor(P)); Aprimes = set(l for l, e in F.factor(A))
        for X, Y, Z in solutions(P):
            a = (F.neg(X), Z); b = (F.neg(Y), Z)
            tot = 0; iP = 0; iA = 0
            for l in primes_of(X, Y, Z):
                s = sym_at(a, b, l); tot += s
                if l in Pprimes:
                    iP += s
                elif l in Aprimes:
                    iA += s
                elif s:
                    bad[s] += 1
            si = sym_inf(a, b); tot += si
            st['sol'] += 1
            if tot % m:
                st['recfail'] += 1
            infodd[si] += 1
            joint[(iP % m, iA % m)] += 1
    print(f"q={p} m={m} A={Adig} n={n} {lab}: #P={len(Ps)} #sol={st['sol']} reciprocity_fail={st['recfail']} "
          f"inv_inf dist={sorted(infodd.items())} inv!=0 at l∤AP: {sorted(bad.items())} "
          f"(inv_P, inv_A) dist={sorted(joint.items())}")


if not pw:
    run('irr', [P for P in F.irreds(n) if F.mod(P, A)])
else:
    for e in sorted({3, 2}):
        if n % e:
            continue
        Ps = []
        for Q in F.irreds(n // e):
            P = (1,)
            for _ in range(e):
                P = F.mul(P, Q)
            if F.mod(P, A):
                Ps.append(P)
        run('Q^%d' % e, Ps)
