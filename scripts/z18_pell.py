"""z18: Y* (=1 at odd primes, 0 at 2) is not in the profinite closure of the Pell points 15Y^2+1 = w^2 (MENU_LADDER Thm 4.1 remark)."""
# Pell solutions w^2 - 15 Y^2 = 1: is Y* (=1 at odd primes, =0 at 2) in their profinite closure?
M = 3*5*7*11*13*17*19*23; K = 2**12
w, Y = 4, 1; seen = []
for j in range(1, 200000):
    if Y % K == 0 and Y % M == 1: print('found j', j); break
    if Y % M == 1 and j < 50: seen.append(('Y=1 mod M at j', j))
    w, Y = 4*w + 15*Y, w + 4*Y
    w %= (K*M); Y %= (K*M)
else:
    print('none up to 2e5')
# parity test at single odd primes: for each ell, which j have Y_j = 1 mod ell; and Y_j even iff j even
for ell in [3,5,7,11,13,17,19,23,29,31]:
    w, Y = 4, 1; js = []
    for j in range(1, 400):
        if Y % ell == 1: js.append(j)
        w, Y = (4*w + 15*Y) % ell, (w + 4*Y) % ell
    print(ell, js[:6])
