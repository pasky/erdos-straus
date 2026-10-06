"""R72 from-scratch checks of Prop 5.4/5.5 (levels alpha+2gamma = 5, 6 empty at x̂_w, w = 9 mod 16).
(a) chain F'=F+D H, H'=F'+H from (1,1) modulo 2^10 for every residue D = 7^a delta^2 (a odd, delta odd):
    which indices i have v_2(H_i) = 4 (level 6) and is m = i+1 always an odd multiple of 3?
    Level 5 (B = 2*7^a): residues of divisors mod 16.
(b) exact chain, a in {1,3,5}, odd delta < 400, i < 60: at every i with v_2(H_i) = 4 check (D+3) | H_i,
    D(D+3)^2 | X_i - 2, and an odd prime q | (D+3)/2, q != 7, with F_i = F_{i+1} = 1 (mod q).
    Also check the Pell identity X^2 - D(D+4) H^2 = 4.
(c) definition-level brute force, NO chain/Pell: for levels 5, 6, 7, all (alpha,gamma), a in {1,3}, b in {0,1},
    odd 7-free c', k' <= CMAX, all divisor pairs F<e... (both orders) of N=1+4ck^2 with
    F = -1 mod m', F = 1 mod 7^v, F = 7 mod 16 (i.e. F = -w mod 2^t for some w = 9 mod 16), and the e-role
    analogue for N/F.  Count 'odd-part certificates' (any w in 9+16Z_2).  Expect 0 at levels 5, 6.
"""
import sys
from math import gcd
from sympy import factorint, divisors


def v2(x):
    return (x & -x).bit_length() - 1 if x else 99


def part_a():
    M = 1 << 10
    Ds = sorted({(pow(7, a, M) * d * d) % M for a in range(1, 64, 2) for d in range(1, M, 2)})
    bad6 = 0; idx = set()
    for D in Ds:
        F, H = 1, 1
        seen = {}
        i = 0
        while (F, H) not in seen:
            seen[(F, H)] = i
            if H % 32 == 16:  # v2(H)=4 is determined mod 32
                m = i + 1
                idx.add(m % 6)
                if not (m % 2 == 1 and m % 3 == 0):
                    bad6 += 1
            F2 = (F + D * H) % M
            H = (F2 + H) % M
            F = F2
            i += 1
    print(f'(a) level 6: {len(Ds)} residues D mod 2^10; m mod 6 at v2(H)=4: {sorted(idx)}; violations {bad6}')
    # level 5: B = 2*7^a, F' = F + B delta^2 H ; divisors mod 16
    res5 = set()
    for a in range(1, 8, 2):
        for d in range(1, 32, 2):
            Bd = 2 * pow(7, a) * d * d
            F, H = 1, 1
            for i in range(64):
                res5.add(F % 16)
                F = F + Bd * H
                H = F + H
    print(f'(a) level 5: divisor residues mod 16 along chains: {sorted(res5)} (need 7 for a certificate)')


def part_b():
    viol = 0; hits = 0; pell_bad = 0
    for a in (1, 3, 5):
        for de in range(1, 400, 2):
            D = 7 ** a * de * de
            F, H = 1, 1
            for i in range(60):
                Fn = F + D * H
                X = F + Fn
                if X * X - D * (D + 4) * H * H != 4:
                    pell_bad += 1
                if v2(H) == 4:
                    hits += 1
                    ok = H % (D + 3) == 0 and (X - 2) % (D * (D + 3) ** 2) == 0
                    q = (D + 3) // 2
                    # smallest odd prime factor of (D+3)/2, check != 7 and sign clash
                    qq = min(factorint(q))
                    ok = ok and qq not in (2, 7) and H % qq == 0 and F % qq == 1 and Fn % qq == 1
                    if not ok:
                        viol += 1
                F, H = Fn, Fn + H
    print(f'(b) exact chains: {hits} positions with v2(H)=4, violations {viol}, Pell failures {pell_bad}')


def is_odd_cert(F, mp, r7v, role_e, t):
    if (F + 1) % mp or (F - 1) % r7v:
        return False
    # role F: F = -w mod 2^t, w = 9 mod 16  <=> F = 7 mod 16 (t >= 4)
    return F % 16 == 7


def part_c(CMAX):
    odd = [x for x in range(1, CMAX + 1, 2) if x % 7]
    for level in (5, 6, 7):
        cnt = 0; pairs = 0
        for ga in range(0, level // 2 + 1):
            al = level - 2 * ga
            t = 2 + al + ga
            for a in (1, 3):
                for b in (0, 1):
                    for c1 in odd:
                        for k1 in odd:
                            c = 2 ** al * 7 ** a * c1
                            k = 2 ** ga * 7 ** b * k1
                            N = 1 + 4 * c * k * k
                            mp = c1 * k1
                            r7v = 7 ** (a + b)
                            for F in divisors(N):
                                pairs += 1
                                if (F + 1) % mp == 0 and (F - 1) % r7v == 0 and F % 16 == 7:
                                    cnt += 1
                                    print('  level', level, 'odd-part certificate', c, k, F, file=sys.stderr)
        print(f'(c) level {level}: divisors tested {pairs}, odd-part certificates (some w=9 mod 16): {cnt}')


if __name__ == '__main__':
    part_a()
    part_b()
    part_c(int(sys.argv[1]) if len(sys.argv) > 1 else 25)
