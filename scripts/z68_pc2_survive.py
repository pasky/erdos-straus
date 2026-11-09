"""z68 PC2: exact finite-level two-prime survival and the product law  s = s1_pure * s2_pure - Gamma.

Inputs are COMPLETE cylinder lists (reduction-built, z68_pc2_events.py; complete for all levels <= the stated box):
  two-prime file  ev_L1_L2_K..txt   (k1 k2 rho1 rho2 ...)
  single-prime files for L1 (level K1) and L2 (level K2)   (k rho ...)  -> UCOVER single-prime survival s^U.
Box B = NR(L1) x NR(L2) at level (L1^K1, L2^K2); profile pi(g,h) = (g at L1, h at L2, 1 elsewhere).
Reported (all exact at the stated finite level; classes of higher level are not used):
  s       = surviving fraction of B (all classes of level <= (K1,K2))
  s1p,s2p = survival under pure classes only (modulus prime to the other prime)  -> pure product s1p*s2p
  Gamma   = s1p*s2p - s   (mass removed only by mixed classes)
  s1U,s2U = single-prime survival of e_{L,g} (all classes of level <= K)
Usage: python3 scripts/z68_pc2_survive.py L1 K1 L2 K2 TWOFILE ONEFILE1 ONEFILE2
"""
import sys
from fractions import Fraction as Fr


def nr(x, l):
    return x % l and pow(x % l, (l - 1) // 2, l) == l - 1


def load(fn, n):
    out = []
    for line in open(fn):
        if line.startswith("#"):
            continue
        out.append(tuple(map(int, line.split()[:n])))
    return out


def main():
    L1, K1, L2, K2 = map(int, sys.argv[1:5])
    two = load(sys.argv[5], 4)
    one1, one2 = load(sys.argv[6], 2), load(sys.argv[7], 2)
    M1, M2 = L1 ** K1, L2 ** K2
    G = [g for g in range(M1) if nr(g, L1)]
    H = [h for h in range(M2) if nr(h, L2)]

    def caught1(g, cyl):
        return any(g % L1 ** k == r for k, r in cyl)

    pure1 = [(k1, r1) for k1, k2, r1, r2 in two if k2 == 0]
    pure2 = [(k2, r2) for k1, k2, r1, r2 in two if k1 == 0]
    mixed = [c for c in two if c[0] >= 1 and c[1] >= 1]
    c1 = {g for g in G if caught1(g, pure1)}
    c2 = {h for h in H if any(h % L2 ** k == r for k, r in pure2)}
    u1 = {g for g in G if caught1(g, one1)}
    u2 = {h for h in H if any(h % L2 ** k == r for k, r in one2)}
    mixset = {}
    for k1, k2, r1, r2 in mixed:
        mixset.setdefault((k1, k2), set()).add((r1, r2))
    surv = 0
    mixonly = 0
    for g in G:
        for h in H:
            hit_mix = any((g % L1 ** k1, h % L2 ** k2) in s for (k1, k2), s in mixset.items())
            pure = g in c1 or h in c2
            if not pure and not hit_mix:
                surv += 1
            if not pure and hit_mix:
                mixonly += 1
    tot = len(G) * len(H)
    s = Fr(surv, tot)
    s1p, s2p = Fr(len(G) - len(c1), len(G)), Fr(len(H) - len(c2), len(H))
    s1U, s2U = Fr(len(G) - len(u1), len(G)), Fr(len(H) - len(u2), len(H))
    gam = s1p * s2p - s
    assert gam == Fr(mixonly, tot)
    print(f"(L1,L2)=({L1},{L2}) level ({L1}^{K1},{L2}^{K2}); NR box {len(G)} x {len(H)} = {tot}; "
          f"mixed cylinders {len(mixed)}")
    print(f"  s = {surv}/{tot} = {float(s):.5f};  s1_pure = {float(s1p):.5f}, s2_pure = {float(s2p):.5f}, "
          f"product = {float(s1p * s2p):.5f};  Gamma = {float(gam):.5f}")
    print(f"  single-prime s1U = {float(s1U):.5f}, s2U = {float(s2U):.5f};  s/(s1U s2U) = "
          f"{float(s / (s1U * s2U)) if s1U * s2U else float('nan'):.4f};  s/(s1p s2p) = "
          f"{float(s / (s1p * s2p)) if s1p * s2p else float('nan'):.4f}")


if __name__ == "__main__":
    main()
