#!/usr/bin/env python3
"""z62 PARITY — GF(2) kill-test analysis for count tables (KT1 and later).

Input TSV: n, tag, then integer count columns. Rows with tag P and n = 1 mod 24 are the primes.
Finds all GF(2) combinations sum_w c_w W_w(p) that equal a function of p mod M (default 840) on the TRAIN primes
(n <= split), reports nontrivial ones (feature part nonzero) and their held-out agreement on TEST primes.
Also reports single columns that are constant on every class mod M (enough primes per class).
Usage: z62_parity_gf2.py table.tsv split [M] [mask_family_prefixes,...]
"""
import sys
import csv


def rref_nullspace(rows, ncols):
    """rows: list of int bitmasks (bit j = column j). Return basis of nullspace {x : rows.x = 0} as bitmasks."""
    piv = {}  # col -> row bitmask (reduced)
    prow = []
    for r in rows:
        for c, pr in piv.items():
            if (r >> c) & 1:
                r ^= pr
        if r == 0:
            continue
        c = (r & -r).bit_length() - 1
        # eliminate c from other pivots
        for c2 in list(piv):
            if (piv[c2] >> c) & 1:
                piv[c2] ^= r
        piv[c] = r
    free = [j for j in range(ncols) if j not in piv]
    basis = []
    for f in free:
        x = 1 << f
        for c, pr in piv.items():
            if (pr >> f) & 1:
                x |= 1 << c
        basis.append(x)
    return basis


def main():
    fn, split = sys.argv[1], int(sys.argv[2])
    M = int(sys.argv[3]) if len(sys.argv) > 3 else 840
    prefixes = sys.argv[4].split(",") if len(sys.argv) > 4 else None
    rd = csv.reader(open(fn), delimiter="\t")
    hdr = next(rd)
    data = [r for r in rd]
    cols = hdr[2:]
    if prefixes:
        keep = [i for i, c in enumerate(cols) if any(c.startswith(p) for p in prefixes)]
    else:
        keep = list(range(len(cols)))
    primes = [(int(r[0]), [int(r[2 + i]) % 2 for i in keep]) for r in data if r[1] == "P" and int(r[0]) % 24 == 1]
    names = [cols[i] for i in keep]
    classes = sorted({p % M for p, _ in primes})
    cidx = {c: j for j, c in enumerate(classes)}
    nf = len(names)
    ncl = len(classes)
    train = [(p, v) for p, v in primes if p <= split]
    test = [(p, v) for p, v in primes if p > split]
    print(f"# {fn}: {len(train)} train primes, {len(test)} test primes, {nf} feature cols, {ncl} classes mod {M}")
    # single columns
    nconst = 0
    for j, nm in enumerate(names):
        byc = {}
        for p, v in primes:
            byc.setdefault(p % M, set()).add(v[j])
        if all(len(s) == 1 for s in byc.values()):
            vals = {c: next(iter(s)) for c, s in byc.items()}
            print(f"  CONST-PER-CLASS column {nm}: values {sorted(set(vals.values()))}")
            nconst += 1
    print(f"# single columns constant on every class: {nconst}")
    rows = []
    for p, v in train:
        m = 0
        for j, b in enumerate(v):
            if b:
                m |= 1 << j
        m |= 1 << (nf + cidx[p % M])
        rows.append(m)
    basis = rref_nullspace(rows, nf + ncl)
    fmask = (1 << nf) - 1
    nontriv = [x for x in basis if x & fmask]
    print(f"# nullspace dim {len(basis)}, with nonzero feature part: {len(nontriv)}")
    # test each basis vector (and report columns)
    for x in nontriv[:60]:
        feat = [names[j] for j in range(nf) if (x >> j) & 1]
        g = {classes[k]: (x >> (nf + k)) & 1 for k in range(ncl)}
        agree = 0
        for p, v in test:
            s = sum(v[j] for j in range(nf) if (x >> j) & 1) % 2
            if p % M in g:
                agree += (s == g[p % M])
        rate = agree / max(1, len(test))
        print(f"  combo held-out agreement {rate:.3f}  feats={feat}  g-nonzero-classes={sum(g.values())}")


if __name__ == "__main__":
    main()
