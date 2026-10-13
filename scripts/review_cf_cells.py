"""R198: cell census mod 8 from scratch. chi(cell) := -eps2 via brute force mod 8 (see review_cf_hasse.py).
Counts odd-n cells, splits by n mod 8, and cross-checks against DEDEKIND 8.1 (n = 1 mod 4: +1 exactly on five classes mod 4)."""
from itertools import product
from review_cf_hasse import eps2_brute
cells = {}
for t, u, v in product(range(8), repeat=3):
    n = (t * u * v - u - v) % 8
    if n % 2:
        cells[(t, u, v)] = (n, -eps2_brute(t, u, v))
print("odd-n cells:", len(cells))
for r in (1, 3, 5, 7):
    c = [k for k, (n, x) in cells.items() if n == r]
    print(f"n=={r} mod 8: cells {len(c)}, chi=-1: {sum(1 for k in c if cells[k][1] == -1)}")
# DK 8.1: for n = 1 mod 4, chi depends on (t,u,v) mod 4, +1 exactly on five classes
plus = {(1, 2, 3), (1, 3, 2), (2, 1, 2), (2, 2, 1), (3, 1, 1)}
ok = all((cells[k][1] == 1) == (tuple(x % 4 for x in k) in plus) for k in cells if cells[k][0] % 4 == 1)
print("DK 8.1 five-class law on n=1 mod 4 cells:", ok)
