# Empirical check of Lemma 4.3 on all witnesses of H and CTRL (p <= 2e10): no witness f divides
# a, b, c, d, g, v, u [if (3/f) = 1], any Q_i (full period), T, U, T+1, T-1 (negative Pell).
import sys, json, math
sys.path.insert(0, 'scripts')
from z69_mine_scan import load_wit, pell_mod
from sympy import jacobi_symbol
viol = 0; tot = 0; Ucnt = 0
for wf, ff in (('/tmp/z69mine/H.wit', '/tmp/z69mine/H.feat.jsonl'), ('/tmp/z69mine/C.wit', '/tmp/z69mine/C.feat.jsonl')):
    W = load_wit(wf)
    for l in open(ff):
        F = json.loads(l); p = F['p']; fs = [f for f, r, y, t in W[p]]
        if not fs: continue
        # full Q set over the period
        a0 = math.isqrt(p); P, Q, aa = 0, 1, a0; Qs = set()
        while True:
            P = aa * Q - P; Q = (p - P * P) // Q; aa = (a0 + P) // Q; Qs.add(Q)
            if Q == 1: break
        PM, _ = pell_mod(p, fs)
        for f in fs:
            tot += 1
            vals = [F['a'], F['b'], F['c'], F['d'], F['g']]
            if F['u3']:
                u, v = F['u3']; vals.append(v)
                if jacobi_symbol(3, f) == 1: vals.append(u)
            T, U = PM[f]
            bad = any(x % f == 0 for x in vals) or any(q % f == 0 for q in Qs) or T % f == 0 or U % f == 0 \
                  or (T + 1) % f == 0 or (T - 1) % f == 0
            if bad:
                viol += 1; print('VIOLATION', p, f)
print('witnesses checked', tot, 'violations', viol)
