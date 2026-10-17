"""R268 brute-force checks (from scratch).
(1) pure triple loop over (a, c, d) of c n + a + 1 = 4acd vs the reviewer's t-form, all n = 1 (4), 5 <= n < 700;
(2) (c, d)-enumeration (numpy over d) of the b = 1 line at 193, 2521, 66529 and at neighbours;
(3) T1 controls (odd squares 9..529) and 105 for both lines;
(4) k = 8 analogues  c n + a + 1 = 8acd  and  n + a + b = 8abd  at primes < 8000.
"""
import numpy as np
from sympy import isprime, primerange


def b1_triple(n, k=4):
    # a(kcd - 1) = cn + 1 => kcd - 1 <= cn + 1 => d <= (cn + 2)/(kc);  c(kad - n) = a + 1 => c <= a + 1, a <= (n+1)/(k-1)
    sols = []
    for a in range(1, (n + 1) // (k - 1) + 2):
        for c in range(1, a + 2):
            for d in range(1, (c * n + 2) // (k * c) + 1):
                if c * n + a + 1 == k * a * c * d:
                    sols.append((a, c, d))
    return sols


def b1_tform(n):
    return [t for t in range(1, (n + 1) // 3 + 1)
            for g in [(-n) % (4 * t)] if g > 0 and (t + 1) % g == 0]


def b1_cd(n, k=4):
    """enumerate c, all d at once: need (k c d - 1) | c n + 1."""
    cnt = 0
    for c in range(1, (n + 1) // (k - 1) + 3):
        d = np.arange(1, (c * n + 2) // (k * c) + 1, dtype=np.int64)
        if len(d) == 0:
            continue
        w = k * c * d - 1
        cnt += int(((c * n + 1) % w == 0).sum())
    return cnt


def c1_count(n, k=4):
    # n + a + b = k a b d, WLOG a <= b (count unordered with a<=b): k a b <= n + 2b => a(k a - 2) <= n
    cnt = 0
    a = 1
    while a * (k * a - 2) <= n:
        for b in range(a, n + a + 1):
            if (n + a) % b:   # b | n + a necessary
                continue
            if (n + a + b) % (k * a * b) == 0:
                cnt += 1
        a += 1
    return cnt


if __name__ == "__main__":
    bad = 0
    for n in range(5, 300, 4):
        tri = len(b1_triple(n)) > 0
        tf = len(b1_tform(n)) > 0
        if tri != tf:
            bad += 1; print("MISMATCH", n)
        if not tri:
            print("  b1 fails at n =", n, "prime" if isprime(n) else "composite")
    print("(1) triple-loop vs t-form existence mismatches n<300:", bad)
    for n in [193, 2521, 66529, 197, 2549, 66541]:
        print("(2) n =", n, "b1 (c,d)-enum count:", b1_cd(n), " t-form count:", len(b1_tform(n)))
    for n in [m * m for m in range(3, 24, 2)] + [105]:
        print("(3) n =", n, "b1 count", len(b1_tform(n)), "c1 count", c1_count(n))
    fb = []; fboth = []; fb1 = []; fboth1 = []
    for p in primerange(3, 8000):
        b = b1_cd(p, 8); c = c1_count(p, 8)
        if b == 0:
            fb.append(p)
            if p % 4 == 1: fb1.append(p)
            if c == 0:
                fboth.append(p)
                if p % 4 == 1: fboth1.append(p)
    print("(4) k=8 b1 fails (all primes<8000):", len(fb), "; both fail:", len(fboth), fboth[:40])
    print("    p=1(4) only: b1 fails", len(fb1), "; both fail", len(fboth1), fboth1)
    print("    131 in both:", 131 in fboth, " 241 in both:", 241 in fboth)
