# z70 GEN item 1b — canonical representation fibres a_c (p = x^2 + d w^2, w = 2 a_c): barren (Lemma REP)?  + comparison fibres.
import sys, math
sys.path.insert(0, 'scripts')
import z70_gen_core as C
pari = C.pari
def good_fibre(p, d, a):
    Na = p + 4 * a * a * d; m = 4 * a * d
    return any(A % m == m - 1 for A in C.divisors(Na))
def rep(p, d):
    # p = x^2 + d w^2 via qfbsolve on the form [1, 0, d]
    s = pari.qfbsolve(pari.Qfb(1, 0, d), p)
    if not s: return None
    x, w = abs(int(s[0])), abs(int(s[1]))
    if d == 1 and w % 2: x, w = w, x
    if x * x + d * w * w != p: return None
    return x, w
out = open(sys.argv[1], 'w')
for (P0, P1, lab) in ((100000, 130000, 'W1'), (1000000, 1030000, 'W2'), (10000000, 10200000, 'W3')):
    ps = [int(q) for q in pari.primes([P0, P1]) if int(q) % 24 == 1]
    for d in (1, 2, 3, 5, 7):
        n = barren = viol = 0; cmpf = 0.0; ncmp = 0; noRep = 0
        for p in ps:
            r = rep(p, d)
            if r is None: noRep += 1; continue
            x, w = r
            if w % 2: noRep += 1; continue
            a = w // 2; n += 1
            if good_fibre(p, d, a): viol += 1
            else: barren += 1
            lo, hi = max(1, a // 2), 2 * a
            cs = [b for b in range(lo, hi + 1) if b != a]
            if len(cs) > 40: cs = cs[:: max(1, len(cs) // 40)]
            g = sum(good_fibre(p, d, b) for b in cs)
            cmpf += g / len(cs); ncmp += 1
        out.write('%s d=%d: primes with a canonical fibre %d (no rep / odd w: %d) | canonical fibre good: %d (barren %d) | comparison fibres a in [a_c/2, 2a_c]: mean good fraction %.4f\n'
                  % (lab, d, n, noRep, viol, barren, cmpf / max(1, ncmp)))
        out.flush()
