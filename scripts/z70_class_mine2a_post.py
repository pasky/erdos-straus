# z70 CLASS item 2a follow-up (post hoc; registered signal rho_l fired): is the rho_l shift a genus/local effect?
# For the least split prime l of Q(sqrt(-p)) (p == 1 mod 8): [L] lies in the principal genus iff l == 1 (4).
# Decompose ord[L] = (2-part) * (odd part); report, by stratum l mod 4: mean v2(h) - v2(ord), mean log ord_odd / log h_odd,
# and the share of l == 1 (4).  Exploration on H_train + CTRL, then H_test scored once with the same table.
import sys, math, cypari2
from sympy import factorint, jacobi_symbol, isprime
from sympy.ntheory import sqrt_mod
sys.path.insert(0, 'scripts')
from z70_class_mine2 import prime_set, h_of, form_order, v2
pari = cypari2.Pari()
def row(p):
    h = h_of(-4*p); l = 3
    while not (isprime(l) and jacobi_symbol(-p % l, l) == 1): l += 2
    r = int(sqrt_mod(-p % l, l)); o = form_order(pari.Qfb(l, 2*r, (r*r + p)//l), -4*p, h, list(factorint(h)))
    ho = h >> v2(h); oo = o >> v2(o)
    return dict(l=l, l4=l % 4, d2=v2(h) - v2(o), rodd=(math.log(oo)/math.log(ho) if ho > 1 else 1.0), rho=math.log(o)/math.log(h))
for name in sys.argv[1:]:
    R = [row(p) for p in prime_set(name)]
    out = [f"{name}: n={len(R)} share l==1(4) {sum(r['l4']==1 for r in R)/len(R):.3f} median l {sorted(r['l'] for r in R)[len(R)//2]}"]
    for s in (1, 3):
        S = [r for r in R if r['l4'] == s]
        if not S: continue
        m = lambda k: sum(r[k] for r in S)/len(S)
        out.append(f"   l=={s}(4): n={len(S)} mean rho {m('rho'):.4f}  mean v2h-v2ord {m('d2'):.3f}  mean log ord_odd/log h_odd {m('rodd'):.4f}")
    print('\n'.join(out), flush=True)
