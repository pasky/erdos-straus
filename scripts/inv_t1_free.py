"""Free-model certificate search for the T1 obstruction (O158).

Residues are formal powers a^j of a single unit a (j in Z, no relations), h = a^2.
Variables: phi(i, 2-i) (pairs u<v, u = a^i, v = a^(2-i)) and psi(1) (square term u = a).
Rows: D(m^2) = 0 for generic patterns m = prod q_i^{e_i}, q_1 << q_2 << ..., with q_i = a^{j_i},
sum j_i e_i = 1 (so m = a, m^2 = h); target row: phi(0,2) = 1 (D(p)=1 for p = h).
A certificate (set of rows summing to 0 = 1) is valid for EVERY modulus M and EVERY unit a,
because specialising residues only identifies variables.

usage: inv_t1_free.py kmax emax jmin jmax
"""
import sys, itertools

def rows_for(js, exps):
    """return dict var->coeff mod 2 for D(m^2), m pattern (residue exponents js, prime exponents exps)."""
    k = len(js)
    acc = {}
    for f in itertools.product(*[range(0, 2 * e + 1) for e in exps]):
        g = tuple(2 * e - x for e, x in zip(exps, f))
        if f == g:
            continue
        small = None
        for i in range(k - 1, -1, -1):
            if f[i] != g[i]:
                small = f[i] < g[i]
                break
        if not small:
            continue
        r = sum(j * x for j, x in zip(js, f))
        key = ('phi', r)
        acc[key] = acc.get(key, 0) ^ 1
    acc[('psi',)] = acc.get(('psi',), 0) ^ 1
    return {k: v for k, v in acc.items() if v}

def main():
    kmax, emax, jmin, jmax = map(int, sys.argv[1:5])
    rows = []
    for k in range(1, kmax + 1):
        for js in itertools.product(range(jmin, jmax + 1), repeat=k):
            for exps in itertools.product(range(1, emax + 1), repeat=k):
                if sum(j * e for j, e in zip(js, exps)) != 1:
                    continue
                rows.append(((js, exps), rows_for(js, exps)))
    varnames = sorted({v for _, r in rows for v in r} | {('phi', 0)}, key=str)
    vid = {v: i for i, v in enumerate(varnames)}
    nv = len(varnames)
    # augmented: bits 0..nv-1 vars, bit nv = rhs, bits nv+1.. = row provenance
    allrows = [(1 << vid[('phi', 0)]) | (1 << nv), ('TARGET',)]
    allrows = [allrows]
    for lab, r in rows:
        m = 0
        for v in r:
            m |= 1 << vid[v]
        allrows.append([m, lab])
    piv = {}
    cert = None
    for t, (m, lab) in enumerate(allrows):
        prov = 1 << t
        while True:
            vm = m & ((1 << nv) - 1)
            if not vm:
                if m >> nv & 1:
                    cert = prov
                break
            b = vm.bit_length() - 1
            if b in piv:
                pm, pp = piv[b]
                m ^= pm; prov ^= pp
            else:
                piv[b] = (m, prov)
                break
        if cert:
            break
    print(f"rows={len(allrows)} vars={nv}")
    if cert is None:
        print("consistent (no certificate in this range)")
        return
    print("CERTIFICATE (rows summing to 0=1):")
    for t in range(len(allrows)):
        if cert >> t & 1:
            lab = allrows[t][1]
            print("  ", lab, rows_for(*lab) if lab != ('TARGET',) else 'phi(0,2)=1')

if __name__ == '__main__':
    main()
