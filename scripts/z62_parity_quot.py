#!/usr/bin/env python3
"""z62 PARITY — KT1 quotient test: prime-level GF(2) identities modulo per-word identities.
A prime-level identity sum_w c_w W_w(p) = g(p mod M) is TRIVIAL if g = 0 and c annihilates every per-word pattern.
Usage: z62_parity_quot.py table.tsv split M N_patterns
"""
import sys, csv
sys.path.insert(0, "scripts")
import z62_parity_river as Z
from z62_parity_gf2 import rref_nullspace


def rank(vecs):
    piv = {}
    r = 0
    for v in vecs:
        for c in sorted(piv, reverse=True):
            if (v >> c) & 1:
                v ^= piv[c]
        if v:
            piv[v.bit_length() - 1] = v
            r += 1
    return r


fn, split, M, NP = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
rd = csv.reader(open(fn), delimiter="\t"); hdr = next(rd); data = list(rd)
nf = len(hdr) - 2
seen = set(); primes = []
for r in data:  # deduplicate controls, bound by NP
    n = int(r[0])
    if r[1] == "P" and n % 24 == 1 and n <= NP and n not in seen:
        seen.add(n); primes.append((n, [int(x) % 2 for x in r[2:]]))
classes = sorted({p % M for p, _ in primes}); cidx = {c: j for j, c in enumerate(classes)}; ncl = len(classes)
rows = []
for p, v in primes:
    if p > split:
        continue
    m = sum(1 << j for j, b in enumerate(v) if b) | (1 << (nf + cidx[p % M]))
    rows.append(m)
prime_null = rref_nullspace(rows, nf + ncl)
Z.SPF = Z.spf_sieve(NP + 1000)
pats = Z.word_patterns(NP)
word_null = rref_nullspace(list(pats), nf)  # c with c.pattern = 0 for all words
print(f"# train primes {len(rows)}; prime-level nullspace dim {len(prime_null)}; per-word identity dim {len(word_null)}; distinct word patterns {len(pats)}")
# trivial subspace inside prime nullspace: word_null embedded with g = 0
r_both = rank(prime_null + word_null)
print(f"# rank(prime_null + word_null) = {r_both}; nontrivial excess dimension = {r_both - len(word_null)}")
# test the excess on held-out
test = [(p, v) for p, v in primes if p > split]
fmask = (1 << nf) - 1
for x in prime_null:
    if rank(word_null + [x & fmask]) == len(word_null) and (x >> nf) == 0:
        continue
    feat = [hdr[2 + j] for j in range(nf) if (x >> j) & 1]
    g = {classes[k]: (x >> (nf + k)) & 1 for k in range(ncl)}
    agree = sum((sum(v[j] for j in range(nf) if (x >> j) & 1) % 2) == g[p % M] for p, v in test)
    print(f"  NONTRIVIAL candidate: held-out agreement {agree/len(test):.3f} feats={feat} g1={sum(g.values())}")
