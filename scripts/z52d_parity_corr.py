"""z52d PARITY lane (C3 falsifier): do 2-power class-group data of Q(sqrt(-p)) predict certificate parities?

Input: output of scripts/z52d_parity_counts.c (p nE nB r4 nEA fII h mis), primes p = 1 (24).
Certificate bits Y (all mod 2):
  R2   = R(p)/2           (R(p) = #(*) triples = 2*r4; R(p) is always even, see memo Lemma 3.1)
  UII  = f_II(p)/2        (unordered Type II count; f_II ordered is always even for p = 1 (4))
  BICH = #bichromatic forest edges (= five-slice certificates)
  EA   = |E(p)|           (O152/INVOLUTION_ES ES part of the windmill set X(p))
  NE   = #forest edges = (|X(p)|-1)/2
Class / Frobenius bits Z:
  b8   = [8 | h(-4p)]     (Barrucand-Cohn: p = x^2 + 32 y^2; checked here)
  b16  = [16 | h(-4p)]
  hq   = h(-4p)/4 mod 4   (4 categories)
  q3   = [3 is a quartic residue mod p], non-abelian (D4) control
         (NOT [2 quartic]: for p = 1 (8), [8|h(-4p)] = [2 quartic] XOR [p = 9 (16)], checked below, so within p mod 16
          strata the quartic character of 2 is the same test as b8)
  c2   = [2 is a cubic residue mod p]    (p = x^2 + 27 y^2), non-abelian control
  rnd  = seeded pseudo-random bit (null control)
Tests: Cochran-Mantel-Haenszel (2x2, and generalized 2xK for hq) stratified by p mod 16 and by p mod 16*5*7*11 = 6160.
Also: is each Y congruential (dependence on p mod 16, mod 5, 7, 11, 13 classes)?
Usage: python z52d_parity_corr.py counts.txt [pmax]"""
import sys, math, random
from collections import defaultdict
import numpy as np

def load(path, pmax=None):
    rows = []
    for line in open(path):
        p, nE, nB, r4, nEA, fII, h, mis = map(int, line.split())
        if pmax and p > pmax:
            break
        assert mis == 0 and fII % 2 == 0 and h % 4 == 0
        rows.append((p, nE, nB, r4, nEA, fII, h))
    return rows

def is_x2_32y2(p):
    y = 0
    while 32 * y * y <= p:
        r = p - 32 * y * y
        s = math.isqrt(r)
        if s * s == r:
            return True
        y += 1
    return False

def cmh(y, z, strata):
    """2x2 CMH: returns (z-score, MH odds ratio)."""
    S = defaultdict(lambda: [0, 0, 0, 0])  # a=y1z1, b=y1z0, c=y0z1, d=y0z0
    for yi, zi, s in zip(y, z, strata):
        S[s][(1 - yi) * 2 + (1 - zi)] += 1
    num = var = 0.0
    R = Sx = PR = PSQR = QS = 0.0  # Robins-Breslow-Greenland variance of log OR_MH
    for a, b, c, d in S.values():
        n = a + b + c + d
        if n < 2:
            continue
        r1, c1 = a + b, a + c
        num += a - r1 * c1 / n
        var += r1 * (n - r1) * c1 * (n - c1) / (n * n * (n - 1))
        Rk, Sk, Pk, Qk = a * d / n, b * c / n, (a + d) / n, (b + c) / n
        R += Rk; Sx += Sk; PR += Pk * Rk; PSQR += Pk * Sk + Qk * Rk; QS += Qk * Sk
    zsc = num / math.sqrt(var) if var > 0 else float('nan')
    orr = R / Sx if Sx > 0 else float('nan')
    se = math.sqrt(PR / (2 * R * R) + PSQR / (2 * R * Sx) + QS / (2 * Sx * Sx)) if R > 0 and Sx > 0 else float('nan')
    return zsc, orr, se

def gcmh(y, zc, K, strata):
    """generalized CMH for binary y vs K-level zc; returns (chi2, df)."""
    S = defaultdict(lambda: np.zeros((2, K)))
    for yi, zi, s in zip(y, zc, strata):
        S[s][yi, zi] += 1
    O = np.zeros(K); E = np.zeros(K); V = np.zeros((K, K))
    for T in S.values():
        n = T.sum()
        if n < 2:
            continue
        r1 = T[1].sum(); nj = T.sum(0)
        O += T[1]; E += r1 * nj / n
        V += r1 * (n - r1) / (n * n * (n - 1)) * (n * np.diag(nj) - np.outer(nj, nj))
    d = (O - E)[:-1]; Vr = V[:-1, :-1]
    return float(d @ np.linalg.solve(Vr, d)), K - 1

def chi2_indep(y, cls):
    """chi2 of binary y vs class labels (no strata); returns (chi2, df)."""
    T = defaultdict(lambda: [0, 0])
    for yi, c in zip(y, cls):
        T[c][yi] += 1
    n = len(y); r1 = sum(y); chi = 0.0
    for a0, a1 in T.values():
        m = a0 + a1
        e1 = m * r1 / n; e0 = m - e1
        chi += (a1 - e1) ** 2 / e1 + (a0 - e0) ** 2 / e0
    return chi, len(T) - 1

from scipy.stats import chi2 as _chi2, norm as _norm

def chi2_sf(x, k):
    """exact chi-square upper tail (scipy)"""
    return float(_chi2.sf(x, k)) if k > 0 else float('nan')

def p_to_z(pv):
    """two-sided p-value -> |z| equivalent"""
    return float(_norm.isf(pv / 2))

def strat_chi2(y, z, strata):
    """sum over strata of the per-stratum 2x2 Pearson chi2 (heterogeneity-sensitive; strata with n >= 20 only); returns (chi2, df)"""
    S = defaultdict(lambda: [0, 0, 0, 0])
    for yi, zi, s in zip(y, z, strata):
        S[s][2 * yi + zi] += 1
    tot = 0.0; df = 0
    for t in S.values():
        n = sum(t); r1 = t[2] + t[3]; c1 = t[1] + t[3]
        if n < 20 or r1 in (0, n) or c1 in (0, n):  # Pearson approximation needs non-tiny strata
            continue
        df += 1
        for yi in (0, 1):
            for zi in (0, 1):
                e = (r1 if yi else n - r1) * (c1 if zi else n - c1) / n
                tot += (t[2 * yi + zi] - e) ** 2 / e
    return tot, df

def main():
    path = sys.argv[1]
    pmax = int(sys.argv[2]) if len(sys.argv) > 2 else None
    rows = load(path, pmax)
    n = len(rows)
    P = [r[0] for r in rows]
    Y = {
        'R2': [r[3] % 2 for r in rows],
        'UII': [(r[5] // 2) % 2 for r in rows],
        'BICH': [r[2] % 2 for r in rows],
        'EA': [r[4] % 2 for r in rows],
        'NE': [r[1] % 2 for r in rows],
    }
    h = [r[6] for r in rows]
    rng = random.Random(52041)
    Z = {
        'b8': [int(x % 8 == 0) for x in h],
        'b16': [int(x % 16 == 0) for x in h],
        'q3': [int(pow(3, (p - 1) // 4, p) == 1) for p in P],
        'c2': [int(pow(2, (p - 1) // 3, p) == 1) for p in P],
        'rnd': [rng.randrange(2) for _ in P],
    }
    hq = [(x // 4) % 4 for x in h]
    # Barrucand-Cohn check
    # direct x^2+32y^2 test on all p <= 1e7 and every 10th prime above (cost)
    chk = [i for i in range(n) if P[i] <= 10**7 or i % 10 == 0]
    bc_bad = sum(1 for i in chk if Z['b8'][i] != int(is_x2_32y2(P[i])))
    print(f"N = {n} primes p = 1 (24), p <= {P[-1]}; Barrucand-Cohn [8|h] == [p = x^2+32y^2] mismatches: {bc_bad} of {len(chk)} checked")
    print("frequencies:", {k: round(sum(v) / n, 4) for k, v in Y.items()}, {k: round(sum(v) / n, 4) for k, v in Z.items()},
          "hq dist", [round(hq.count(j) / n, 4) for j in range(4)])
    # Z vs p mod 16 (sanity: is b8 congruential at 16?)
    q2 = [int(pow(2, (p - 1) // 4, p) == 1) for p in P]
    idbad = sum(1 for p, b, q in zip(P, Z['b8'], q2) if b != (q ^ int(p % 16 == 9)))
    print(f"identity [8|h] == [2 quartic] XOR [p=9 (16)] mismatches: {idbad}")
    for k in ('b8', 'b16', 'q3'):
        for M in (16, 5 * 16, 7 * 16):
            c, df = chi2_indep(Z[k], [p % M for p in P])
            print(f"  {k} vs p mod {M}: chi2 = {c:.1f} (df {df}), p~{chi2_sf(c, df):.3g}")
    print("\n[A] Is each certificate bit congruential?  chi2 of Y vs p mod M (no strata)")
    for k, y in Y.items():
        out = []
        for M in (16, 5, 7, 11, 13, 16 * 5 * 7, 16 * 5 * 7 * 11):
            c, df = chi2_indep(y, [p % M for p in P])
            out.append(f"mod {M}: {c:.0f}/{df} (p~{chi2_sf(c, df):.2g})")
        print(f"  {k}: " + "; ".join(out))
    print("\n[B] CMH z-scores (Y vs Z), strata = p mod 16 | p mod 16*5*7*11 = 6160   [OR = Mantel-Haenszel odds ratio]")
    res = []
    for ky, y in Y.items():
        line = []
        for kz, z in Z.items():
            z1, or1, se1 = cmh(y, z, [p % 16 for p in P])
            z2, or2, se2 = cmh(y, z, [p % 6160 for p in P])
            line.append(f"{kz}: {z1:+.2f}/{z2:+.2f} (OR {or2:.3f}, logOR 95% CI [{math.log(or2)-1.96*se2:+.3f},{math.log(or2)+1.96*se2:+.3f}])")
            res.append((ky, kz, z1, z2, math.log(or2), se2))
        print(f"  {ky}: " + "; ".join(line))
    print("\n[B2] 16-rank beyond the 8-rank: CMH Y vs b16, strata (p mod 16, b8) | (p mod 6160, b8)")
    for ky, y in Y.items():
        z1, _, _ = cmh(y, Z['b16'], [(p % 16, b) for p, b in zip(P, Z['b8'])])
        z2, or2, se2 = cmh(y, Z['b16'], [(p % 6160, b) for p, b in zip(P, Z['b8'])])
        print(f"  {ky}: {z1:+.2f} | {z2:+.2f} (OR {or2:.3f}, logOR 95% CI [{math.log(or2)-1.96*se2:+.3f},{math.log(or2)+1.96*se2:+.3f}])")
        res.append((ky, 'b16|b8', z1, z2, math.log(or2), se2))
    print("\n[C] generalized CMH: Y vs h(-4p)/4 mod 4 (df 3), strata p mod 16 | p mod 6160")
    for ky, y in Y.items():
        c1, df = gcmh(y, hq, 4, [p % 16 for p in P])
        c2, _ = gcmh(y, hq, 4, [p % 6160 for p in P])
        print(f"  {ky}: chi2 = {c1:.2f} | {c2:.2f} (df {df}); p = {chi2_sf(c1, df):.3g} | {chi2_sf(c2, df):.3g}")
        res.append((ky, 'hq', p_to_z(chi2_sf(c1, df)), p_to_z(chi2_sf(c2, df)), None, None))
    print("\n[D] per-class tables, strata p mod 16 (P(Y=1) by b8, b16)")
    for ky, y in Y.items():
        parts = []
        for r16 in (1, 9):
            for kz in ('b8', 'b16'):
                for zv in (0, 1):
                    idx = [i for i in range(n) if P[i] % 16 == r16 and Z[kz][i] == zv]
                    parts.append(f"p%16={r16},{kz}={zv}: {sum(y[i] for i in idx) / len(idx):.4f} (n={len(idx)})")
        print(f"  {ky}: " + "; ".join(parts))
    print("\n[E] no deterministic law: classes (p mod 6160, h mod 16) in which Y takes both values; first such pair")
    for ky, y in Y.items():
        seen = {}; both = set(); first = None
        for i in range(n):
            key = (P[i] % 6160, h[i] % 16)
            if key in seen and seen[key][0] != y[i]:
                both.add(key)
                if first is None:
                    first = (seen[key][1], P[i], key)
            elif key not in seen:
                seen[key] = (y[i], P[i])
        print(f"  {ky}: {len(both)} of {len(seen)} classes non-constant; first counterexample pair {first}")
    print("\n[F] heterogeneity: sum over p mod 6160 strata of per-stratum 2x2 chi2 (detects stratum-dependent signs)")
    for ky, y in Y.items():
        parts = []
        for kz in ('b8', 'b16', 'rnd'):
            c, df = strat_chi2(y, Z[kz], [p % 6160 for p in P])
            parts.append(f"{kz}: {c:.0f}/{df} (z~{(c-df)/math.sqrt(2*df):+.2f})" if df else f"{kz}: n/a (no stratum with n >= 20)")
        print(f"  {ky}: " + "; ".join(parts))
    print("\n[G] twisted laws: Y xor Z vs p mod l, l = 13..47 prime (chi2, df l-1)")
    gz = []
    for ky, y in Y.items():
        for kz in ('b8', 'b16'):
            w = [a ^ b for a, b in zip(y, Z[kz])]
            for l in (13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
                c, df = chi2_indep(w, [p % l for p in P])
                gz.append((p_to_z(chi2_sf(c, df)), ky, kz, l))
    gz.sort(reverse=True)
    print(f"  {len(gz)} tests; largest |z|-equivalents: {[(round(a,2),b,c,d) for a,b,c,d in gz[:3]]}")
    cls = [a for a in res if a[1] != 'rnd']
    k = len(cls)
    mx = max(cls, key=lambda a: abs(a[2]))
    thr1 = _norm.isf(0.05 / (2 * k)); thr2 = _norm.isf(0.05 / (4 * k))
    print(f"\nSUMMARY: {k} class/control tests ([B] w/o rnd, [B2], [C]); max |z| (p mod 16 strata) = {abs(mx[2]):.2f} ({mx[0]} vs {mx[1]}; "
          f"6160 strata: {abs(mx[3]):.2f}); Bonferroni 5% two-sided: {thr1:.2f} ({k} tests), {thr2:.2f} (counting both stratifications, {2*k})")
    ci = [(abs(a[4]) + 1.96 * a[5], a[0], a[1]) for a in res if a[4] is not None and a[1] in ('b8', 'b16', 'b16|b8')]
    print(f"  class bits: max (|log OR| + 1.96 SE) = {max(ci)[0]:.4f} ({max(ci)[1]} vs {max(ci)[2]}); "
          f"max |log OR| = {max(abs(a[4]) for a in res if a[4] is not None and a[1] in ('b8','b16','b16|b8')):.4f}")

main()
