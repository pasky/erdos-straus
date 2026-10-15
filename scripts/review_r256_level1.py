"""R256: level-1 cells covered by fixed windows (some r-exponent c in {1, 2}, i.e. ball v_r(u+m) >= 1) and their Type I
mirrors (u = -1/m mod r) on the r-generic line; survivors among non-residue cells mod r.
usage: review_r256_level1.py r Mmax"""
import sys


def factor(x):
    f, q = {}, 2
    while q*q <= x:
        while x % q == 0:
            f[q] = f.get(q, 0) + 1; x //= q
        q += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f


r, Mmax = int(sys.argv[1]), int(sys.argv[2])
nr = {u for u in range(1, r) if pow(u, (r-1)//2, r) == r - 1}
cov, mir = set(), set()
for m in range(3, Mmax + 1, 4):
    if m % r == 0:
        continue
    k = (1 + m)//4
    while k % r == 0:
        k //= r
    res = {1 % m}
    for q, e in factor(k).items():
        res = {(x*pow(q, j, m)) % m for x in res for j in range(2*e + 1)}
    t = (-pow(4, -1, m)) % m
    if any((x*pow(r, c, m)) % m == t for x in res for c in (1, 2)):
        cov.add((-m) % r); mir.add((-pow(m, -1, r)) % r)
print(f"r={r} m<={Mmax}: NR cells {sorted(nr)}; window cells {sorted(cov & nr)}; mirrors {sorted(mir & nr)}; "
      f"survivors {sorted(nr - cov - mir)}")
