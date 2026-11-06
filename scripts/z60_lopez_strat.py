"""z60 LOPEZ: conditional (stratified) dependence of the two branches' least witnesses.
Stratum = (p mod 5, p mod 7, p mod 11, p mod 13 QR-pattern / exact residues per option) ; pooled ratio
  sum_s #{both > X in s} / sum_s N_s P_s(A>X) P_s(B>X)   (Mantel-Haenszel-type observed/expected under conditional independence)
Usage: python z60_lopez_strat.py file [inM 0/1]"""
import sys, numpy as np
d = np.loadtxt(sys.argv[1], dtype=np.int64)
if len(sys.argv) > 2 and sys.argv[2] == '1':
    d = d[np.isin(d[:, 0] % 840, [1, 121, 169, 289, 361, 529])]
INF = 10**12; X = d.copy(); X[X == 0] = INF; p = X[:, 0]
def qr(p, l):
    return (np.array([pow(int(x), (l - 1) // 2, l) for x in (p % l)]) == 1).astype(np.int64)
# least prime non-residue (among odd primes <= 97; p ≡ 1 mod 8 in mode 0 so 2 is a QR)
small = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
res_cache = {l: qr(p, l) for l in small}
npq = np.full(len(p), 101)
for l in reversed(small):
    npq[res_cache[l] == 0] = l
strata = {
 'none': np.zeros(len(p), dtype=np.int64),
 'n_p': npq,
 'p mod 5,7,11,13 exact': (p % 5) * 10000 + (p % 7) * 1000 + (p % 11) * 20 + (p % 13),
 'exact mod 5..13 + QR 17..31': ((p % 5) * 10000 + (p % 7) * 1000 + (p % 11) * 20 + (p % 13)) * 64
      + res_cache[17] * 1 + res_cache[19] * 2 + res_cache[23] * 4 + res_cache[29] * 8 + res_cache[31] * 16,
}
print("least-odd-prime-nonresidue catch-all (n'_p > 97, coded 101):", int((npq == 101).sum()), "primes")
import os, gzip
DUMP = os.environ.get('Z60_DUMP')   # if set: write per-stratum sufficient statistics N_s, A_s, B_s, AB_s (gz)
dump = gzip.open(DUMP, 'wt') if DUMP else None
if dump: dump.write("# coord stratification X stratum_key N_s A_s(A>X) B_s(B>X) AB_s(both>X)  [only strata with A_s+B_s>0]\n")
for col, nm in ((1, 'a'), (3, 'f'), (5, 'T')):
    B = X[:, col]; A = X[:, col + 1]
    xs = sorted(set(int(np.quantile(B, q)) for q in (0.5, 0.9, 0.99, 0.999)))
    print(f"== coordinate {nm}")
    for sn, s in strata.items():
        keys, inv = np.unique(s, return_inverse=True)
        out = []
        for x in xs:
            a = (A > x).astype(float); b = (B > x).astype(float)
            Ns = np.bincount(inv); Sa = np.bincount(inv, a); Sb = np.bincount(inv, b); Sab = np.bincount(inv, a * b)
            exp = (Sa * Sb / Ns).sum(); obs = Sab.sum()
            out.append(f"X={x}: obs {int(obs)} exp {exp:.1f} ratio {obs/exp if exp else float('nan'):.3f}")
            if dump:
                for k in np.nonzero(Sa + Sb)[0]:
                    dump.write(f"{nm} {sn.replace(' ','_')} {x} {keys[k]} {Ns[k]} {int(Sa[k])} {int(Sb[k])} {int(Sab[k])}\n")
        print(f"  [{sn}] ({len(keys)} strata) " + " | ".join(out))
if dump: dump.close()
