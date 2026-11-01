# Z2831: Gross–Zagier-type test of the Type I datum.
#  TI(p,d,m) := exists e>=1 with 4dm-1 = p e and m has a divisor a with a + m/a ≡ 0 (mod e)   [QUATERNION_ES Prop 2.1 (i),(ii)]
#  GZ(p,d,m) := p | Res(H_{-4d}, H_{-4m}) (Hilbert class polynomials of the orders of discriminants -4d, -4m; PARI polclass)
#  Scan: p ≡ 1 (24), p <= P; d <= DD, m <= DM. Pairs with TI true are all enumerated (p | 4dm-1); a control sample of
#  pairs with p ∤ 4dm-1 is drawn for comparison. Both criteria are then tabulated, also for (-d/p)=(-m/p)=-1.
import sys, random
import cypari2
pari = cypari2.Pari(); pari.allocatemem(4*10**9)
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
from collections import Counter
P = int(sys.argv[1]) if len(sys.argv) > 1 else 300
DD = int(sys.argv[2]) if len(sys.argv) > 2 else 30
DM = int(sys.argv[3]) if len(sys.argv) > 3 else 300
random.seed(3)
Hc = {}
def H(D):
    if D not in Hc: Hc[D] = pari(f"polclass({D})")
    return Hc[D]
def TI(p, d, m):
    N = 4*d*m - 1
    if N % p: return False
    e = N // p
    return any(m % a == 0 and (a + m//a) % e == 0 for a in range(1, m+1))
def GZ(p, d, m):
    res = pari.polresultant(H(-4*d), H(-4*m), 'x')
    return int(res) % p == 0
rows = []
for p in L.primes_upto(P):
    if p < 17 or p % 24 != 1: continue
    ti_pairs = []
    for d in range(1, DD+1):
        for m in range(1, DM+1):
            if (4*d*m-1) % p == 0 and TI(p, d, m):
                ti_pairs.append((d, m))
    for (d, m) in ti_pairs:
        rows.append((p, d, m, True, GZ(p, d, m), L.legendre(-d, p) == -1 and L.legendre(-m, p) == -1))
    ctrl = []
    tries = 0
    while len(ctrl) < 40 and tries < 5000:
        tries += 1
        d = random.randint(1, DD); m = random.randint(1, DM)
        if (4*d*m-1) % p == 0: continue
        ctrl.append((d, m))
    for (d, m) in ctrl:
        rows.append((p, d, m, False, GZ(p, d, m), L.legendre(-d, p) == -1 and L.legendre(-m, p) == -1))
print("rows:", len(rows), " TI-true:", sum(1 for r in rows if r[3]), " control:", sum(1 for r in rows if not r[3]))
for cond in (False, True):
    sel = [r for r in rows if (r[5] or not cond)]
    t = [r for r in sel if r[3]]; c = [r for r in sel if not r[3]]
    print(("(-d/p)=(-m/p)=-1 only: " if cond else "all: "), "P(GZ | TI) = %d/%d" % (sum(r[4] for r in t), len(t)), "  P(GZ | control) = %d/%d" % (sum(r[4] for r in c), len(c)))
print("TI-true rows where GZ fails (p,d,m,cond):", [(r[0], r[1], r[2], r[5]) for r in rows if r[3] and not r[4]][:15])
# structure check: is GZ determined by the Legendre symbols of D1 = -4d, D2 = -4m mod p (and their product)?
from collections import defaultdict
tab = defaultdict(Counter)
for (p, d, m, ti, gz, cond) in rows:
    key = (L.legendre(-d, p), L.legendre(-m, p), L.legendre((4*d*m-1) % p, p) if (4*d*m-1) % p else 0)
    tab[key][gz] += 1
print("GZ by (( -d/p), (-m/p), ((4dm-1)/p)):")
for k in sorted(tab): print("  ", k, dict(tab[k]))
