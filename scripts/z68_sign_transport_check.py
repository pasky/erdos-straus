# z68_sign_transport_check.py — Theorem 2 (no local transport L4 -> L3) input check.
# For each prime l with a UCOVER Thm S(a) certified branch list (g0 mod l containing a profile e_{l,g} caught by NO
# length-3 good family at ANY level; data/z66/ucover/stree_certified*.txt), intersect with the non-residue classes
# caught at level 1 by LENGTH-4 good families (data/z68/sign/profile_R4_B2e6.txt, exact length 4, explicit witnesses).
# Every witness is re-verified here independently (HJ lengths, level-1 congruences, non-residuosity, and a brute
# integer check: for several integers n in the class, the word built from the family has numerator n and
# Jacobi symbol (A/n) = -1).
import re, sys
from sympy import jacobi_symbol

def hj_word(N, D):
    w = []
    while D > 0:
        b = -(-N // D); w.append(b); N, D = D, b * D - N
    return w
def K(w):
    a, b = 1, 0          # K() = 1, K(len -1) = 0
    for x in w: a, b = x * a - b, a
    return a

branches = {}
for fn in ['data/z66/ucover/stree_certified.txt', 'data/z66/ucover/stree_certified_small.txt']:
    for line in open(fn):
        m = re.match(r'ell=(\d+): branches g0 mod ell proved to contain U_S-profiles e_\(ell,g\): \[([^\]]*)\]', line)
        if m:
            branches[int(m.group(1))] = [int(x) for x in m.group(2).split(',') if x.strip()]
wit = {}
for line in open('data/z68/sign/profile_R4_B2e6.txt'):
    m = re.match(r'W (\d+) 4 g=(\d+) X/X\'=(\d+)/(\d+) Y/Y\'=(\d+)/(\d+)', line)
    if m:
        l, g, X, Xp, Y, Yp = map(int, m.groups()); wit[(l, g)] = (X, Xp, Y, Yp)
ok_l = []
for l in sorted(branches):
    both = []
    for g0 in branches[l]:
        if (l, g0) not in wit: continue
        X, Xp, Y, Yp = wit[(l, g0)]
        # left part reversed: X/Xp = [[b_j..b_1]]; right part Y/Yp = [[b_{j+2}..b_r]]
        left = hj_word(X, Xp)[::-1] if Xp > 0 else []
        right = hj_word(Y, Yp) if Yp > 0 else ([] if Y == 1 else None)
        assert right is not None and len(left) + len(right) == 3, (l, g0)
        XY = X * Y; assert XY % l == 0 and (XY // l) % l != 0
        M = XY // l; s = Xp * Y + X * Yp
        assert (s + 1) % M == 0 and (-s) % l == g0 and jacobi_symbol(g0, l) == -1
        # brute: integers n ≡ 1 (mod 8M'), n ≡ g0 (mod l) in the family class; build the word and check
        import math
        Mod = math.lcm(8, XY)
        cnt = 0
        for n in range(1, 50 * Mod * l, 1):
            if n % 8 != 1 or n % l != g0 or (n + s) % XY: continue
            b = (n + s) // XY
            if b < 2: continue
            w = left + [b] + right
            assert K(w) == n, (w, n)
            A = K(w[1:])
            assert jacobi_symbol(A, n) == -1, (l, g0, n, w)
            cnt += 1
            if cnt >= 3: break
        assert cnt >= 1
        both.append(g0)
    print(f"l={l} UCOVER-branches={branches[l]} caught-at-length-4-level-1={both}")
    if both: ok_l.append(l)
print("primes l where Theorem 2 applies:", ok_l)
