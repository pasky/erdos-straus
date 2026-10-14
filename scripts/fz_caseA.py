"""fz_caseA.py (O220): Case A union-bound mass for q = 3^r, r >= 2 (FF_STERILE_SMALL §2).
Exact part alpha <= AMAX: fs_caseA.caseA_mass (O216; exact rationals, six routes of FF_STERILE_PUSH Lemma 2.2).
Tail alpha > AMAX (FF_STERILE_SMALL Lemma 2.1): count(alpha) <= (alpha+1)^3 q^{(alpha-1)/2} 3^{alpha/2}, so
mass <= sum_{alpha > AMAX} (alpha+1)^3 q^{-(alpha+1)/2} 3^{alpha/2}, a geometric majorant with ratio
((AMAX+3)/(AMAX+2))^3 sqrt(3/q) < 1 for q >= 9. Upper bounds rounded up (float, x(1+1e-9)).
usage: fz_caseA.py r[,r...] [AMAX=40]"""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from fs_caseA import caseA_mass

def tail(q, AMAX):
    a0 = AMAX + 1
    rho = ((a0 + 2) / (a0 + 1))**3 * math.sqrt(3 / q)
    if rho >= 1: return float('inf')
    M0 = (a0 + 1)**3 * q**(-(a0 + 1) / 2) * 3**(a0 / 2)
    return M0 / (1 - rho) * (1 + 1e-9)

if __name__ == '__main__':
    AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    for r in [int(x) for x in sys.argv[1].split(',')]:
        q = 3**r
        tot, _ = caseA_mass(q, AMAX)
        print(f"r={r} q={q}: Case A exact-pattern mass (alpha<={AMAX}) = {float(tot)*(1+1e-12):.10e}  tail <= {tail(q, AMAX):.10e}")
