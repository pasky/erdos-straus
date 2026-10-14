"""y2_witness: for each HJ length r, the smallest odd square N = M^2 having an interior word of length r with a
quiddity (short diagonal) = 0 mod 4.  Shows the zero-mod-4 locus is not inside the Jacobi -1 fibre for r != 3.
usage: y2_witness.py RMAX MMAX"""
import sys
from y2_hexagon import det


def search(r, N):
    # DFS over interior words with K = N: build path; prune with first coord <= N
    res = []

    def rec(path, word):
        if len(word) == r:
            if path[-1][0] == N:
                n = len(path)
                q = [abs(det(path[i - 1], path[(i + 1) % n])) for i in range(n)]
                if any(x % 4 == 0 for x in q):
                    res.append(tuple(word))
            return
        p, c = path[-2], path[-1]
        b = 2
        while not res:
            nxt = (b * c[0] - p[0], b * c[1] - p[1])
            if nxt[0] > N:
                break
            rec(path + [nxt], word + [b])
            b += 1
    rec([(0, -1), (1, 0)], [])
    return res


for r in range(2, int(sys.argv[1]) + 1):
    found = None
    for M in range(3, int(sys.argv[2]), 2):
        w = search(r, M * M)
        if w:
            found = (M * M, w[0]); break
    print("r =", r, "first odd-square witness:", found)
