"""ff2_caseB.py (O166): search Case B families at x*_c (FUNCTIONFIELD_ES2.md §0.2).
q = p prime (odd), A = T^k.  For L' monic, T∤L', deg L' <= LMAX; j <= JMAX; g = T^gam g', g' | L', gam <= j:
D = 1 + T^(N+1) L' g, N = k+j-1; test whether rho or rho' (least CRT reps of -(1+cT) resp. -(1+cT)^{-1} mod
T^(N+1), -1 mod L') is monic and divides D with monic cofactor.  usage: ff2_caseB.py p k c LMAX JMAX"""
import sys, itertools
sys.path.insert(0, 'scripts')
from ff2_polyq import *
from ff2_crtpoint import crt
p, k, c, LMAX, JMAX = map(int, sys.argv[1:6])
U = parse(sys.argv[6], p) if len(sys.argv) > 6 else [1, c % p]  # optional u (high->low digits), polynomial
def monics(d):
    for t in itertools.product(range(p), repeat=d):
        yield list(t) + [1]
def divisors_monic(f):
    # brute: all monic d with deg<=deg f dividing f
    out = []
    for d in range(0, len(f)):
        for m in monics(d):
            if not mod(f, m, p): out.append(m)
    return out
def Tpow(e): return [0] * e + [1]
found = 0
for l in range(0, LMAX + 1):
    for Lp in monics(l):
        if Lp[0] == 0: continue
        dl = divisors_monic(Lp)
        for j in range(0, JMAX + 1):
            N = k + j - 1; TN1 = Tpow(N + 1)
            u = U
            uinv = [1]  # inverse of u mod T^(N+1) by Newton/iteration
            for _ in range(N + 2): uinv = mod(mul(uinv, sub([2], mul(u, uinv, p), p), p), TN1, p)
            assert mod(mul(u, uinv, p), TN1, p) == [1]
            rho = crt(neg(u, p), TN1, [p - 1], Lp, p) if l > 0 else mod(neg(u, p), TN1, p)
            rhop = crt(neg(uinv, p), TN1, [p - 1], Lp, p) if l > 0 else mod(neg(uinv, p), TN1, p)
            for gam in range(0, j + 1):
                for gp in dl:
                    g = mul(Tpow(gam), gp, p)
                    D = add([1], mul(mul(TN1, Lp, p), g, p), p)
                    for name, r in (('rho', rho), ('rho1', rhop)):
                        if not r or r[-1] != 1: continue
                        qq, rm = divmod_(D, r, p)
                        if rm or not qq or qq[-1] != 1: continue
                        found += 1
                        if found <= 20: print('FOUND', name, 'Lp', Lp, 'j', j, 'g', g, 'E', r, 'cof', qq, flush=True)
    print('done deg L\' =', l, 'found', found, flush=True)
