"""z18: exact search for Type II families n = sigma*T*T' - T - T' (MENU_LADDER Lemma 2.2, a = lam constant)
for n = c0*Y^D + k at mu = 0.  T' = S*T1 (T1 primitive integer, deg e), T = r + U*T1 where r = -n mod T1
(so T' | n + T automatically); the remaining condition T | n + T' is solved exactly for (U, S) by resultants.
Then sigma = (n+T+T')/(T T') must be a polynomial; parameters a = lam, c = lam*sigma, d = T/(4 lam^2), b = lam(sigma T' - 1)
must be positive (leading coefficients) and integral near mu = 0 (Lemma 2.1: values at Y=1 in Z[1/2], at Y=0 in Z_(2)).
usage: z18_tt.py c0 k D e R   (T1 ranges over primitive integer polys of degree e, |coeff| <= R, positive leading coeff)"""
import sys, itertools, math
from fractions import Fraction as Fr
import cypari2
pari = cypari2.Pari(); pari.allocatemem(8*10**8, silent=True)
c0, k, D, e, R = map(int, sys.argv[1:6])
TYPE = sys.argv[6] if len(sys.argv) > 6 else 'II'   # 'I': n*T' + 1 = T*(sigma*T' - 1)  (Type I, a const, e = T')
n = pari(f'{c0}*Y^{D}+{k}')
def fr(x): return Fr(str(x))
def val(x, p):
    if x == 0: return math.inf
    v = 0; a, b = x.numerator, x.denominator
    while a % p == 0: a //= p; v += 1
    while b % p == 0: b //= p; v -= 1
    return v
def primes(xs):
    s = {2}
    for x in xs:
        if x == 0: continue
        for y in (x.numerator, x.denominator):
            if abs(y) > 1:
                for p in pari.factor(abs(y))[0]: s.add(int(p))
    return s
def integral_lam(vals):
    """vals: dict name -> (value at 1, value at 0); a=lam, c,b scale lam^1, d scales lam^-2. return lam or None"""
    lam = Fr(1)
    for p in primes([v for pr in vals.values() for v in pr]):
        i = 1 if p == 2 else 0
        lo = max(0, -val(vals['c'][i], p), -val(vals['b'][i], p))
        vd = val(vals['d'][i], p)
        if 2*lo > vd: return None
        lam *= Fr(p)**lo
    return lam
hits = 0; sols = 0
for co in itertools.product(range(-R, R+1), repeat=e):
    for lc in range(1, R+1):
        cs = list(co) + [lc]
        if math.gcd(*cs) != 1: continue
        T1 = pari.Pol(list(reversed(cs)), 'Y')
        SC = int(__import__('os').environ.get('Z18_SCALE', '0'))   # T1(Y) -> T1(2^SC * Y), made primitive
        if SC:
            T1 = pari.subst(T1, 'Y', pari(f'2^({SC})*Y')); T1 = T1/pari.content(T1)
        if D % 2 == 0 and pari.polsturm(T1) > 0: continue        # Lemma 2.3
        r = -pari.lift(pari.Mod(n, T1)) if TYPE == 'II' else pari(-1)
        T = r + pari('U')*T1
        # condition: (n + S*T1) mod T == 0 ; T has leading coeff U*lc (U != 0)
        num = n + pari('S')*T1 if TYPE == 'II' else n*pari('S')*T1 + 1
        rem = pari.Vec(pari.divrem(num, T, 'Y')[1])
        # rem coefficients are rational functions in U, S: take numerators
        eqs = [pari.numerator(x) for x in rem if x != 0]
        if not eqs: continue
        if len(eqs) == 1:
            continue  # positive-dimensional; skip (rare)
        res = pari.polresultant(eqs[0], eqs[1], 'S')
        if res == 0: continue
        for fac in pari.factor(res)[0]:
            if pari.poldegree(fac, 'U') != 1: continue
            Uv = -pari.polcoef(fac, 0, 'U')/pari.polcoef(fac, 1, 'U')
            if Uv <= 0: continue
            g = pari.gcd(pari.substvec(eqs[0], ['U'], [Uv]), pari.substvec(eqs[1], ['U'], [Uv]))
            if pari.poldegree(g, 'S') < 1: continue
            for sf in pari.factor(g)[0]:
                if pari.poldegree(sf, 'S') != 1: continue
                Sv = -pari.polcoef(sf, 0, 'S')/pari.polcoef(sf, 1, 'S')
                if Sv <= 0: continue
                Tp = Sv*T1; TT = pari.substvec(T, ['U'], [Uv])
                if TYPE == 'II':
                    q, rm = pari.divrem(n + TT + Tp, TT*Tp, 'Y')
                else:
                    q0, rm = pari.divrem(n*Tp + 1, TT, 'Y')
                    q, rm2 = pari.divrem(q0 + 1, Tp, 'Y')
                    if rm2 != 0: continue
                if rm != 0 or q == 0: continue
                sols += 1
                sig = q
                if fr(pari.pollead(sig)) <= 0: continue
                b1 = sig*Tp - 1
                vals = {'c': (fr(pari.subst(sig, 'Y', 1)), fr(pari.subst(sig, 'Y', 0))),
                        'b': (fr(pari.subst(b1, 'Y', 1)), fr(pari.subst(b1, 'Y', 0))),
                        'd': (fr(pari.subst(TT, 'Y', 1))/4, fr(pari.subst(TT, 'Y', 0))/4)}
                lam = integral_lam(vals)
                tag = 'HIT' if lam is not None else 'sol'
                if lam is not None: hits += 1
                print(f'{tag} T1={T1} U={Uv} S={Sv} T={TT} sigma={sig} lam={lam}', flush=True)
print('algebraic solutions', sols, 'hits', hits)
