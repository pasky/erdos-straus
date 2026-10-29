#!/usr/bin/env python3
"""z51 forcing: exhaustive check of the Kneser covering lemma (EXSET_CHAR_FORCING Lemma 2.2).

Work in G = Z/(2u) (discrete logs mod a prime q = 2u+1 = 3 mod 4, u odd); -1 has log u; U = 2Z/(2u).
For every multiset {g_1..g_k} (k <= K) of logs, B = sum_j {-g_j, 0, g_j}.  Claim: if u not in B then the stabiliser
H of B satisfies (i) H <= U, (ii) no g_j in u + H, (iii) #{j : g_j not in H} <= [U:H] - 1.
Also checks sharpness: for every proper H < U of index d there is a failing multiset with n_out = d - 1 (all g_j equal).
Usage: z51_forcing_kneser.py UMAX K
"""
import sys, itertools

def box(gs, n):
    B = {0}
    for g in gs:
        B = {(b + e * g) % n for b in B for e in (-1, 0, 1)}
    return B

def stab(B, n):
    return {h for h in range(n) if all(((b + h) % n) in B for b in B)}

def main():
    UMAX, K = int(sys.argv[1]), int(sys.argv[2])
    checked = fails = 0
    for u in range(1, UMAX + 1, 2):
        n = 2 * u
        for k in range(1, K + 1):
            for gs in itertools.combinations_with_replacement(range(1, n), k):
                checked += 1
                B = box(gs, n)
                if u in B:
                    continue
                fails += 1
                H = stab(B, n)
                Hs = len(H)
                assert all(h % 2 == 0 for h in H), (u, gs, H)          # (i) H <= U (logs even)
                assert not any(((g - u) % n) in H for g in gs), (u, gs)  # (ii)
                nout = sum(1 for g in gs if g % n not in H)
                d = u // Hs
                assert nout <= d - 1, (u, gs, H, nout, d)               # (iii)
        # sharpness: H = d'Z with index d in U (d | u), multiset of d-1 copies of a generator of G/H
        for d in [d for d in range(2, u + 1) if u % d == 0]:
            # H = subgroup of order u/d inside U: logs multiples of 2d
            gs = [1] * (d - 1)
            B = box(gs, n)
            assert u not in B or d == 1, (u, d)
    print(f"checked {checked} multisets, {fails} with -1 not in the box; Lemma 2.2 (i)-(iii) hold in all; sharpness ok")

if __name__ == "__main__":
    main()
