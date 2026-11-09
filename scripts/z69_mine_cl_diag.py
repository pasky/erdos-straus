# Diagnose the CL:vdivz / CL:eqz excess of the chi-matched (x,z)-phantom runs on H: which CL component (n_p, nq7,
# h(-4p), h(-4p)/4) divides / equals z, real vs phantom, and whether the phantoms' least non-residue differs.
import sys, json, collections
sys.path.insert(0, 'scripts')
import cypari2
pari = cypari2.Pari()
def comps(p):
    q = 2
    while pow(q, (p - 1) // 2, p) == 1: q = int(pari('nextprime(%d)' % (q + 1)))
    npq = q; q = 7
    while not (q % 8 == 7 and pow(p % q, (q - 1) // 2, q) == q - 1): q = int(pari('nextprime(%d)' % (q + 1)))
    h = int(pari('qfbclassno(%d)' % (-4 * p)))
    return {'np': npq, 'nq7': q, 'h': h, 'h/4': h // 4}
cache = {}
def C(p):
    if p not in cache: cache[p] = comps(p)
    return cache[p]
for fn in sys.argv[1:]:
    cntR = collections.Counter(); cntP = collections.Counter(); npd = collections.Counter(); n = 0
    for l in open(fn):
        rec = json.loads(l)
        if not rec['ph']: continue
        n += 1; z = rec['z']; K = len(rec['ph'])
        cr = C(rec['p'])
        for k, v in cr.items():
            if v >= 5 and z % v == 0: cntR['vdivz:' + k] += 1
            if v >= 3 and v == z: cntR['eqz:' + k] += 1
        for ph in rec['ph']:
            cp = C(ph['q'])
            for k, v in cp.items():
                if v >= 5 and z % v == 0: cntP['vdivz:' + k] += 1 / K
                if v >= 3 and v == z: cntP['eqz:' + k] += 1 / K
            npd['phantom np < real np'] += (cp['np'] < cr['np']) / K
            npd['phantom np > real np'] += (cp['np'] > cr['np']) / K
    print(fn.split('/')[-1], 'records', n)
    for k in sorted(set(cntR) | set(cntP)): print('   %-14s real %6d phantom %8.1f' % (k, cntR[k], cntP[k]))
    print('   ', {k: round(v / n, 3) for k, v in npd.items()})
