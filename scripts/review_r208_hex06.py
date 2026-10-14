"""R208: hexagon words (r = 4, interior), odd N <= X: all six quiddities even  =>  some quiddity = 0 mod 4 (tree proof)."""
import sys
sys.path.insert(0, 'scripts')
from review_r208_polygon import words, quid
X = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
n06 = bad = 0
for N in range(3, X + 1, 2):
    for b in words(4, N):
        q = quid(b)[3]
        if all(x % 2 == 0 for x in q):
            n06 += 1
            bad += not any(x % 4 == 0 for x in q)
print("X", X, "(0^6) hexagon words", n06, "without a 0-mod-4 quiddity:", bad)
