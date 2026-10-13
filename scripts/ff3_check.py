"""ff3_check.py (O173): independent check of ff3_caseB.c (different method: factor D with sympy, all divisors).
q = p prime, A = T^k.  Enumerates L' (T∤L'), j, gam <= j, g' | L', all monic divisors E of D = 1 + T^(N+1+gam) L' g'
with E == -u mod T^(N+1), E == -1 mod L'; prints the family set, checks Lemma 2.1 (l <= N+gam-2) on each, and
verifies a sample of families end to end (explicit P, X, Y, Z with A/P = 1/X+1/Y+1/Z, monic, NC).
usage: ff3_check.py p k LMAX JMAX u0 u1 ... [--cmp FILE]   (u digits low->high)"""
import sys, itertools, random
from sympy import Poly, symbols, GF
T = symbols('T')
args = sys.argv[1:]; cmpf = None
if '--cmp' in args: i = args.index('--cmp'); cmpf = args[i + 1]; args = args[:i] + args[i + 2:]
p, k, LMAX, JMAX = map(int, args[:4]); u = [int(x) % p for x in args[4:]]
def P_(c): return Poly(list(reversed(c)) or [0], T, modulus=p)          # c low->high
def tl(P):  # Poly -> canonical low->high list, coefficients in 0..p-1
    c = [int(x) % p for x in reversed(P.all_coeffs())]
    while c and c[-1] == 0: c.pop()
    return tuple(c)
def monic_divisors(P):
    lc, fl = P.factor_list(); divs = [Poly(1, T, modulus=p)]
    for f, e in fl:
        f = f.monic(); new = []
        for d in divs:
            x = d
            for _ in range(e + 1): new.append(x); x = x * f
        divs = new
    return divs
def is_monic(P): return tl(P)[-1] == 1
NMAX = k + JMAX
U = P_(u + [0] * (NMAX + 2))
fams = set(); bad21 = 0
for l in range(0, LMAX + 1):
    for t in itertools.product(range(p), repeat=l):
        Lc = list(t) + [1]
        if Lc[0] == 0: continue
        L = P_(Lc)
        gds = monic_divisors(L)
        for j in range(0, JMAX + 1):
            N = k + j - 1; TN1 = P_([0] * (N + 1) + [1])
            target = (-U).rem(TN1)
            for gam in range(0, j + 1):
                for g in gds:
                    D = P_([1]) + P_([0] * (N + 1 + gam) + [1]) * L * g
                    for E in monic_divisors(D):
                        if E.degree() < 1: continue
                        if (E - target).rem(TN1).is_zero is False: continue
                        if l > 0 and (E + 1).rem(L).is_zero is False: continue
                        fams.add((l, j, gam, tl(L), tl(g), tl(E)))
                        if not (l <= N + gam - 2): bad21 += 1
print("families:", len(fams), " Lemma 2.1 violations (only meaningful if u = 1 + cT mod T^2, c != 0):", bad21)
for f in sorted(fams)[:30]: print("FAM", f)
if cmpf:  # compare with ff3_caseB HIT lines (E or E')
    got = set()
    for line in open(cmpf):
        if not line.startswith('HIT'): continue
        w = dict(x.split('=', 1) for x in line.split()[1:])
        l, j, N, gam = int(w['l']), int(w['j']), int(w['N']), int(w['gam'])
        L = [int(x) for x in w["L'"].strip('[]').split(',')]; g = [int(x) for x in w["g'"].strip('[]').split(',')]
        D = P_([1]) + P_([0] * (N + 1 + gam) + [1]) * P_(L) * P_(g)
        if 'E' in w: E = P_([int(x) for x in w['E'].strip('[]').split(',')])
        else: E = D.exquo(P_([int(x) for x in w["E'"].strip('[]').split(',')]))
        if l <= LMAX and j <= JMAX: got.add((l, j, gam, tuple(L), tl(P_(g)), tl(E)))
    print("C-search families in range:", len(got), " equal sets:", got == fams, " missing in C:", len(fams - got), " extra in C:", len(got - fams))
# end-to-end: explicit P, then X, Y, Z for a few families (type 0 for a0 = T^gam g', type 2 for b0 = T^j L')
random.seed(1); checked = 0
def irreducible(P): return P.is_irreducible
for f in sorted(fams)[:6]:
    l, j, gam, Lc, gc, Ec = f; N = k + j - 1
    L, g, E = P_(list(Lc)), P_(list(gc)), P_(list(Ec))
    M = P_([0] * (N + 1) + [1]) * L * E      # modulus: P == u mod T^(N+1), P == 1 mod L'E (slice point)
    for tries in range(4000):
        n = M.degree() + 6
        R = P_([random.randrange(p) for _ in range(n - M.degree())] + [1])
        # CRT: find P0 mod M with P0 == u mod T^(N+1), == 1 mod L E  (brute via sympy gcdex)
        A1 = P_([0] * (N + 1) + [1]); B1 = L * E
        s_, t_, h_ = A1.gcdex(B1)       # s A1 + t B1 = 1
        P0 = (P_(list(u) + [0]) * t_ * B1 + P_([1]) * s_ * A1).rem(M)
        Pp = P0 + R * M
        if not is_monic(Pp) or not irreducible(Pp): continue
        A = P_([0] * k + [1]); X = (Pp + E).exquo(A)
        a0 = P_([0] * gam + [1]) * g; b0 = P_([0] * j + [1]) * L
        a = a0; b = X.exquo(b0); s = a + b; kap = s.exquo(E)
        Y = kap * Pp * X.exquo(a); Z = kap * Pp * X.exquo(b)
        ok = (A * X * Y * Z - Pp * (X * Y + Y * Z + Z * X)).is_zero and all(is_monic(W) for W in (X, Y, Z)) \
             and min(X.degree(), Y.degree(), Z.degree()) >= Pp.degree() - k
        print("E2E", f, "deg P", Pp.degree(), "identity+monic+NC:", ok); checked += 1; break
print("end-to-end checked:", checked)
