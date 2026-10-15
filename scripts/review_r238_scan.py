"""R238 from-scratch scan of prime windows q*(p) and the cap there, with exact Def 1.1 check of every solution.

usage: review_r238_scan.py N   (all primes p = 1 mod 4, p <= N)
For each p: q* = least prime q with q = 4-p mod 8, (q/p) = -1 (q != p automatic).
cap(q*) = min e with -K in {prod s^{2a_s} : 0<=a_s<=b_s+e} mod q*, computed via discrete logs (bitmask rotations),
then a witness Q is backtracked, the triple built from the equation and checked against Def 1.1.
"""
import sys
from math import log
from collections import Counter
from review_r238_core import factor, is_prime, jacobi, def11_cap, solution_from_Q

PR = {}


def dlog_table(q):
    if q in PR:
        return PR[q]
    fs = factor(q - 1)
    for gen in range(2, q):
        if all(pow(gen, (q - 1) // f, q) != 1 for f in fs):
            break
    tab = {}
    v = 1
    for k in range(q - 1):
        tab[v] = k
        v = v * gen % q
    PR[q] = (gen, tab)
    return PR[q]


def rot(mask, k, N, full):
    k %= N
    return ((mask << k) | (mask >> (N - k))) & full


def prime_window_cap(n, q, emax=10**6):
    """Return (e, Q) minimal cap at prime window q, or (None, None) if -K not in <S>^2."""
    K = (n + q) // 4
    fk = factor(K)
    S = sorted(fk)
    _, tab = dlog_table(q)
    N = q - 1
    full = (1 << N) - 1
    T = tab[(-K) % q]
    L = [tab[s % q] for s in S]
    e = 0
    while e <= emax:
        layers = [1]  # bit 0 = identity
        R = 1
        for s, Ls in zip(S, L):
            R2 = 0
            for a in range(fk[s] + e + 1):
                R2 |= rot(R, 2 * a * Ls, N, full)
                if R2 == full:
                    break
            R = R2
            layers.append(R)
        if R >> T & 1:
            # backtrack
            t = T
            exps = []
            for i in range(len(S) - 1, -1, -1):
                for a in range(fk[S[i]] + e + 1):
                    tp = (t - 2 * a * L[i]) % N
                    if layers[i] >> tp & 1:
                        exps.append(a)
                        t = tp
                        break
                else:
                    raise AssertionError
            exps.reverse()
            Q = 1
            for s, a in zip(S, exps):
                Q *= s ** a
            return e, Q
        # stop if the reachable set stabilised (group generated)
        if e > N + 2:
            return None, None
        e += 1
    return None, None


def main():
    N = int(sys.argv[1])
    sieve = bytearray([1]) * (N + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    small = [q for q in range(3, 2000) if is_prime(q)]
    hist = Counter()
    maxq = (0, 0)
    maxratio = (0, 0, 0)
    ratios = []
    nchk = 0
    capmax = (0, 0, 0)
    viol = 0
    for p in range(5, N + 1, 4):
        if not sieve[p]:
            continue
        for q in small:
            if q % 8 == (4 - p) % 8 and jacobi(q, p) == -1:
                break
        else:
            raise SystemExit(f"no q* < 2000 for {p}")
        if q > maxq[0]:
            maxq = (q, p)
        r = q / log(p) ** 2
        ratios.append((r, p, q))
        e, Q = prime_window_cap(p, q)
        if e is None:
            viol += 1
            print("THM 1.1 VIOLATION", p, q)
            continue
        x, y, z = solution_from_Q(p, q, Q)
        e2 = def11_cap(p, x, y, z)
        nchk += 1
        if e2 != e:
            print("cap mismatch", p, q, e, e2)
            viol += 1
        if e > q - 3 and e > 0:
            print("cap > q-3", p, q, e)
            viol += 1
        hist[e] += 1
        if e > capmax[0]:
            capmax = (e, p, q)
    ratios.sort(reverse=True)
    print(f"primes p=1(4) <= {N}: {sum(hist.values())}; exact Def1.1 checks: {nchk}; violations: {viol}")
    print("max q*:", maxq, " top q*/log^2 p:", [(round(a, 3), b, c) for a, b, c in ratios[:5]])
    print("cap at q* histogram:", sorted(hist.items()))
    print("max cap at q*:", capmax)


if __name__ == "__main__":
    main()
