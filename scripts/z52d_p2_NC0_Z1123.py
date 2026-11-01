"""Z1123: combinatorial game on residual fractions (G4, NC0).
Game (3 picks, normal play, unbounded denominators):
  A picks x (1/x <= 4/p), B picks y (1/y <= residual), A picks z (1/z must equal the residual).
  A wins iff after A's last pick the residual is exactly 0. Positive unit fractions only.
  (Winning positions for A = exact ES-type decompositions, with the quantifier structure EXISTS x FORALL y EXISTS z.)
Exact: for fixed x, B wins iff some legal y makes r' - 1/y NOT a positive unit fraction, or == 0.
A-win for x is only "evidence" since the forall-y range is infinite: we test y up to YW beyond ceil(1/r').
Per prime p = 1 mod 4 we scan x in [ceil(p/4), ceil(p/4)+XW]."""
import sys, math
from fractions import Fraction

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
XW = int(sys.argv[2]) if len(sys.argv) > 2 else 400
YW = int(sys.argv[3]) if len(sys.argv) > 3 else 3000


def is_unit(q):
    return q > 0 and q.numerator == 1


def B_refutes_x(r):
    """r = residual after A's x-move (positive Fraction). Return (True, y) if B has a refuting y in range."""
    y0 = math.ceil(1 / r) if r > 0 else 1
    # legal y: 1/y <= r  <=>  y >= 1/r
    for y in range(max(1, y0), y0 + YW):
        s = r - Fraction(1, y)
        if s == 0 or not is_unit(s):
            return True, y
    return False, None


def primes(n):
    s = [True] * (n + 1); s[0] = s[1] = False
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            s[i * i::i] = [False] * len(range(i * i, n + 1, i))
    return [i for i in range(n + 1) if s[i]]


tot_A = 0
rows = []
for p in primes(PMAX):
    if p % 4 != 1 or p < 5:
        continue
    x0 = math.ceil(p / 4)
    A_wins = []
    refute_ys = []
    for x in range(x0, x0 + XW):
        r = Fraction(4, p) - Fraction(1, x)
        if r <= 0:
            continue
        ref, y = B_refutes_x(r)
        if ref:
            refute_ys.append(y)
        else:
            A_wins.append(x)
    tot_A += len(A_wins)
    rows.append((p, len(A_wins), max(refute_ys) if refute_ys else None))
print(f"primes 1 mod 4 <= {PMAX}; x-window {XW}; y-window {YW}")
print("p, #x where A survives all tested y, largest refuting y needed (sample)")
for r in rows[:12]:
    print(r)
print("total x with A surviving tested y's:", tot_A, "over", len(rows), "primes")
print("max refuting y over all primes:", max(r[2] for r in rows if r[2] is not None))
# sanity: a known 3-term decomposition (4/p = 1/x+1/y+1/z) exists for p=13: is it an A-win (exists x) ?
p = 13
print("sanity p=13: 4/13 = 1/4+1/18+1/468 ; A-survivor x=4 ?",
      B_refutes_x(Fraction(4, 13) - Fraction(1, 4)))

# Explicit B-reply (PROVED argument): r' = a/b reduced; y = k*b with k = (b+1)//a + 1 gives residual (k a - 1)/(k b),
# whose reduced numerator is (k a - 1)/gcd(k a - 1, b) > 1 because k a - 1 > b.  Check on the tested x-window:
chk = 0
for p in primes(PMAX):
    if p % 4 != 1 or p < 5:
        continue
    for x in range(math.ceil(p / 4), math.ceil(p / 4) + XW):
        r = Fraction(4, p) - Fraction(1, x)
        if r <= 0:
            continue
        a, b = r.numerator, r.denominator
        k = (b + 1) // a + 1
        s = r - Fraction(1, k * b)
        assert s > 0 and not is_unit(s) and k * b >= 1 / r
        chk += 1
print("explicit B-reply verified for", chk, "(p,x) pairs")
