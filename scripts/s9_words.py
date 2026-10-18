"""s9_words.py (O271): exact checks in word coordinates W(n) = {(t,u,v) >= 1 : t u v - u - v = n}.
 (a) level-c bijection: W(n) ∩ {t = c}  <->  {(T, U, 1) in W(c n) : c | T}, (c,g,s) -> (c s, (c n + 1)/(c s - 1), 1)
 (b) (★) [c=1 line: n + a + b = 4abd]  <=>  some word with 4 | t;
     b=1 line [c n + a + 1 = 4acd]       <=>  some word with 4 | v  (and, by u<->v symmetry, 4 | u)
     union <=> some word has a coordinate == 0 (mod 4)
 (c) T1 in word form: for odd squares n = m^2 no word has a coordinate == 0 (mod 4)
 (d) (★) has a word with u = 1 iff n + 1 has a divisor == 3 (mod 4)
usage: python s9_words.py NMAX SQMAX
"""
import sys
from math import isqrt

def divisors(x):
    ds = []
    for d in range(1, isqrt(x) + 1):
        if x % d == 0:
            ds.append(d)
            if d * d != x:
                ds.append(x // d)
    return ds

def words(n):
    """all (t,u,v) with t u v - u - v = n; via u: (t u - 1) | n + u."""
    W = []
    for u in range(1, n + 3):
        for e in divisors(n + u):
            if (e + 1) % u == 0:
                t = (e + 1) // u
                if t >= 1:
                    W.append((t, u, (n + u) // e))
    return W

def star_direct(n):   # n + a + b = 4abd, a,b,d >= 1
    for a in range(1, n + 1):
        if 4 * a - a - 1 > n:  # b=1,d=1 minimum value 4a-a-1
            break
        for b in range(1, n + 1):
            if 4 * a * b - a - b > n:
                break
            if (n + a + b) % (4 * a * b) == 0:
                return True
    return False

def b1_direct(n):     # c n + a + 1 = 4 a c d, a,c,d >= 1 (original definition; 4cd - 1 | n + 4d bounds c <= (n+5)/4)
    for c in range(1, (n + 5) // 4 + 1):
        for d in range(1, n + 1):
            w = 4 * c * d - 1
            if w > c * n + 1:
                break
            if (c * n + 1) % w == 0:
                return True
    return False

def main():
    NMAX = int(sys.argv[1]); SQMAX = int(sys.argv[2])
    bad = 0; cnt = 0
    for n in range(3, NMAX + 1, 2):
        W = words(n)
        S = set(W)
        assert all(t * u * v - u - v == n for t, u, v in W) and len(S) == len(W)
        # (a) bijection on a few c
        for c in (1, 2, 3, 4, 6):
            lhs = sorted((c * s, (c * n + 1) // (c * s - 1)) for (t, g, s) in W if t == c and c * s > 1)
            Wc = words(c * n) if c * n <= 4000 else None
            if Wc is not None:
                rhs = sorted((T, U) for (T, U, V) in Wc if V == 1 and T % c == 0 and T > 1)
                if lhs != rhs:
                    bad += 1; print("bij fail", n, c)
        star_w = any(t % 4 == 0 for t, u, v in W)
        b1_w = any(v % 4 == 0 for t, u, v in W)
        if star_w != star_direct(n) or b1_w != b1_direct(n):
            bad += 1; print("line fail", n, star_w, b1_w)
        u1 = any(t % 4 == 0 and u == 1 for t, u, v in W)
        if u1 != any(e % 4 == 3 for e in divisors(n + 1)):
            bad += 1; print("u=1 fail", n)
        cnt += 1
    print(f"(a,b,d) checked all odd n in [3,{NMAX}]: {cnt} values, failures {bad}")
    sqbad = 0; nsq = 0
    for m in range(1, SQMAX + 1, 2):
        n = m * m
        W = words(n)
        if any(x % 4 == 0 for w in W for x in w):
            sqbad += 1; print("T1 word fail", m)
        nsq += 1
    print(f"(c) odd squares m <= {SQMAX}: {nsq} squares, words with a coordinate == 0 (4): {sqbad}")

if __name__ == "__main__":
    main()
