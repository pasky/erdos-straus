"""R232 (hostile review #2 of STERILE_LOWER Comp 4.1), FROM SCRATCH (no imports of project code).
Level-1 coverage of the quadratic non-residue cells mod a prime r by the boxes of the ET families (M17 Lemma 1.1):
  P (K = 1): N-points (a,b,c,d) of Sigma^II_r: 4abcd = a + b + r c, a <= b, r ∤ cd; boxes -f, -f' mod r,
             f = 4acd - 1, f' = 4bcd - 1  (no other K reaches level 1 in non-residue cells: K odd, ceil(K/2) = 1 <=> K = 1).
  Q (k = 1): N-points of Sigma^I_r: 4abcd = r(a+b) + c, a <= b, e = (a+b)/c prime to r; boxes -4a^2 d, -4b^2 d mod r
             (-4b^2 d = -1/(4a^2 d) covers Q^{-1}).
  U (k = 1): (a,b,e), e | a+b, gcd(e,4ab)=1, 4(ab)' | e+1, (ab)_r = r; box -e and -1/e  (checked to add nothing: M17 L5.2).
No in-cell restriction beyond the definitions (a superset of boxes => survivors are a SUBSET of the true survivors;
we also report whether the restrictions r∤ab etc. ever bite)."""
import sys

def primes(n):
    s = bytearray([1]) * n; s[0:2] = b'\x00\x00'
    for p in range(2, int(n ** .5) + 1):
        if s[p]: s[p * p::p] = bytearray(len(s[p * p::p]))
    return [i for i in range(n) if s[i]]

def P_data(N):
    """all (a,b,c,d) with 4abcd = a + b + N c, 1 <= a <= b (then c(4abd - N) = a + b, so e = (a+b)/c >= 1 forces c <= a + b).
    b = (a + N c)/(4acd - 1) is decreasing in c."""
    out = []
    a = 1
    while 4 * a * a <= N + 2 * a:
        d = 1
        while 4 * a * a * d <= N + 2 * a:
            c = 1
            while True:
                f = 4 * a * c * d - 1
                num = a + N * c
                if num < a * f: break           # b < a; b decreasing in c
                if c * f > a * f + num: break   # c > a + b (e = (a+b)/c < 1); a + b - c decreasing in c
                if num % f == 0:
                    b = num // f
                    assert 4 * a * b * c * d == a + b + N * c
                    out.append((a, b, c, d))
                c += 1
            d += 1
        a += 1
    return out

def Q_data(F):
    """all (a,b,c,d) with 4abcd = F(a+b) + c, 1 <= a <= b (c | F(a+b)). f = 4acd - F = (Fa + c)/b in [1, F + 2]."""
    out = []
    a = 1
    while 4 * a <= 2 * F + 2:
        d = 1
        while 4 * a * d <= 2 * F + 2:
            c = F // (4 * a * d) + 1
            while 4 * a * c * d <= 2 * F + 2:
                f = 4 * a * c * d - F
                num = F * a + c
                if num % f == 0:
                    b = num // f
                    if b >= a:
                        assert 4 * a * b * c * d == F * (a + b) + c
                        out.append((a, b, c, d))
                c += 1
            d += 1
        a += 1
    return out

def U_boxes(r):
    """U-data at level 1: a*b = r * m with r ∤ m (one of a, b carries r once), 4m | e+1, e | a+b, gcd(e, 4ab) = 1."""
    bx = set()
    for A in range(1, 4 * r):              # A = a' (the r-free part of the factor carrying r), 4 A b | e+1 <= r A + b + 1
        if A % r == 0: continue
        b = 1
        while 4 * A * b <= r * A + b + 1:
            if b % r:
                a = r * A; m = A * b
                for e in range(4 * m - 1, a + b + 1, 4 * m):
                    if (a + b) % e == 0 and __import__('math').gcd(e, 4 * a * b) == 1:
                        bx.add((-e) % r); bx.add((-pow(e, -1, r)) % r)
            b += 1
    return bx

def survivors(r):
    cov = set(); bite = 0
    for (a, b, c, d) in P_data(r):
        if c % r == 0 or d % r == 0: continue
        if a % r == 0 or b % r == 0: bite += 1
        cov.add((-(4 * a * c * d - 1)) % r); cov.add((-(4 * b * c * d - 1)) % r)
    for (a, b, c, d) in Q_data(r):
        e = (a + b) // c
        if (a + b) % c: bite += 1; continue
        if e % r == 0: continue
        if c % r == 0: bite += 1
        cov.add((-4 * a * a * d) % r); cov.add((-4 * b * b * d) % r)
    nr = [u for u in range(1, r) if pow(u, (r - 1) // 2, r) == r - 1]
    surv = sorted(set(nr) - cov)
    ucov = U_boxes(r) if r < 200 else set()
    newU = sorted((set(nr) & ucov) - cov)
    return nr, surv, bite, newU

if __name__ == '__main__':
    hi = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    for r in primes(hi)[1:]:
        nr, surv, bite, newU = survivors(r)
        print(r, len(nr), len(surv), surv if len(surv) <= 8 else '', 'bite', bite, 'Unew', newU)
