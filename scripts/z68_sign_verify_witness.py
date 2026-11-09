# z68_sign_verify_witness.py FILE R — independent check of every witness line "W l R g=.. X/X'=.. Y/Y'=.." of
# z68_sign_profile output: rebuild the length-R word family from the two HJ fractions, take three integers n in
# {n ≡ -(X'Y+XY') (mod XY), n ≡ 1 (mod 8)} with big letter >= 2, and check K(word) = n, n ≡ g (mod l),
# n ≡ 1 (mod XY/l) [profile condition], (g/l) = -1, and Jacobi (A/n) = -1 with A = K(word[1:]).
import re, sys, math
from sympy import jacobi_symbol
from sympy.ntheory.modular import crt
def hj_word(N, D):
    w = []
    while D > 0:
        b = -(-N // D); w.append(b); N, D = D, b * D - N
    return w
def K(w):
    a, b = 1, 0
    for x in w: a, b = x * a - b, a
    return a
fn, R = sys.argv[1], int(sys.argv[2])
cnt = 0; ls = set()
for line in open(fn):
    m = re.match(r"W (\d+) (\d+) g=(\d+) X/X'=(\d+)/(\d+) Y/Y'=(\d+)/(\d+)", line)
    if not m or int(m.group(2)) != R: continue
    l, _, g, X, Xp, Y, Yp = map(int, m.groups())
    left = hj_word(X, Xp)[::-1] if Xp > 0 else []
    right = hj_word(Y, Yp) if Yp > 0 else []
    assert (Xp == 0) == (X == 1) and (Yp == 0) == (Y == 1)
    assert len(left) + len(right) == R - 1 and min(left + right + [2]) >= 2
    s = Xp * Y + X * Yp; XY = X * Y; M = XY // l
    assert XY % l == 0 and M % l != 0 and (s + 1) % M == 0 and (-s) % l == g and jacobi_symbol(g, l) == -1
    r, Lm = crt([XY, 8], [(-s) % XY, 1])
    n = int(r)
    while (n + s) // XY < 2: n += int(Lm)
    for i in range(3):
        nn = n + i * int(Lm)
        b = (nn + s) // XY
        w = left + [b] + right
        assert K(w) == nn and nn % l == g and (nn - 1) % M == 0
        assert jacobi_symbol(K(w[1:]), nn) == -1, (l, g, nn, w)
    cnt += 1; ls.add(l)
print(f"{fn}: R={R}: {cnt} witnesses verified at {len(ls)} primes l, 0 failures")
