"""R256 from-scratch Haar Monte Carlo for the certified-cap lemma (s7_certified_caps Lemma 1) on the line lnr(p) = 17.

Haar point: p = 1 (8); p mod l uniform nonzero QR for odd l < 17, uniform NR mod 17, uniform nonzero for 17 < l <= Q.
Window q (prime, q = 3 (4), 19 <= q <= Q): K_q = (p+q)/4; F = {l <= Q odd, l != q : p = -q (l)} u {2 if q = 7 (8)}.
 forced ((p/q) = -1):  cap <= e  iff  for all NR a mod q: -1 in a^{G_e} Pi_F,  and for NR l0 in F: -1 in l0^{G_e} Pi_{F-l0}
 unforced ((p/q) = +1): cap 0 iff -1 in Pi_F (ET Type II class)
G_e = {-1,0,1,3,...,2e+1};  Pi_F = {prod l^{j_l}, j in {-1,0,1}} mod q.
unforced/composite windows m <= Q: F-only cap-0 test as well.\nusage: review_r256_capdensity.py Q SAMPLES SEED
"""
import random, sys


def primes(n):
    return [l for l in range(2, n + 1) if all(l % q for q in range(2, int(l**.5) + 1))]


def prodset(F, q):
    S = {1}
    for l in F:
        li = pow(l, -1, q)
        S = {(x*y) % q for x in S for y in (1, l % q, li)}
    return S


def is_qr(a, l):
    return pow(a % l, (l-1)//2, l) == 1


def main(Q, N, seed):
    rng = random.Random(seed)
    P = primes(Q)
    odd = [l for l in P if l > 2]
    W = [q for q in P if q % 4 == 3 and q >= 19]
    cnt = {'f0': 0, 'f1': 0, 'f2': 0, 'all0': 0}
    for _ in range(N):
        r = {}
        for l in odd:
            while True:
                x = rng.randrange(1, l)
                if l < 17 and not is_qr(x, l):
                    continue
                if l == 17 and is_qr(x, l):
                    continue
                break
            r[l] = x
        best_forced, best_all = 99, 99
        for q in W:
            F = [l for l in odd if l != q and (r[l] + q) % l == 0]
            if q % 8 == 7:
                F = [2] + F
            if is_qr(r[q], q):          # unforced
                if (q - 1) in prodset(F, q):
                    best_all = 0
                continue
            for e in range(0, 3):
                G = [-1, 0, 1] + [2*k + 1 for k in range(1, e + 1)]
                PF = prodset(F, q)
                ok = all(any(((-pow(a, -g, q)) % q) in PF for g in G)
                         for a in range(1, q) if not is_qr(a, q))
                if ok:
                    for l0 in F:
                        if not is_qr(l0, q):
                            P0 = prodset([l for l in F if l != l0], q)
                            if not any(((-pow(l0, -g, q)) % q) in P0 for g in G):
                                ok = False; break
                if ok:
                    best_forced = min(best_forced, e); break
        # F-only cap-0 test on every window m = 3 (4), m <= Q (composite allowed; gcd(m, K) = 1 automatically
        # since K = p/4 (mod l) for l | m and p is a unit at l; p = 1 mod 8 so no 2 | m issue)
        for m in range(3, Q + 1, 4):
            if any(m % l == 0 and r[l] == 0 for l in odd):
                continue
            F = [l for l in odd if m % l and (r[l] + m) % l == 0]
            if m % 8 == 7:
                F = [2] + F
            if (m - 1) in prodset(F, m):
                best_all = 0; break
        best_all = min(best_all, best_forced)
        cnt['f0'] += best_forced == 0; cnt['f1'] += best_forced <= 1; cnt['f2'] += best_forced <= 2
        cnt['all0'] += best_all == 0
    print(f'Q={Q} N={N}: forced cap0 {cnt["f0"]/N:.3f}  cap<=1 {cnt["f1"]/N:.3f}  cap<=2 {cnt["f2"]/N:.3f}  '
          f'forced+unforced cap0 {cnt["all0"]/N:.3f}')


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
