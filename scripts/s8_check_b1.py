"""O258 independent check of the b = 1 line of ES Type II: c p + a + 1 = 4 a c d (b = 1).
Brute force over (a, d) (independent of the window/divisor code in s8_lines.c).
Usage: PYTHONPATH=scripts uv run python scripts/s8_check_b1.py n1 n2 ...
"""
import sys

def b1_solutions(n):
    sols = []
    for a in range(1, n + 2):
        dlo = (n + 1 + 4 * a - 1) // (4 * a)   # 4ad >= n+1
        dhi = (n + a + 1) // (4 * a)           # m = 4ad - n <= a + 1
        for d in range(max(1, dlo), dhi + 1):
            m = 4 * a * d - n
            if m >= 1 and (a + 1) % m == 0:
                c = (a + 1) // m
                x, y, z = a * d, a * c * d * n, c * d * n   # b = 1
                assert 4 * x * y * z == n * (x * y + y * z + z * x)
                sols.append((a, c, d))
    return sols

def c1_solutions(n):
    """c = 1 line: n + a + b = 4abd  <=>  (4ad - 1) | n + a."""
    sols = []
    for a in range(1, n + 2):
        for d in range(1, (n + a) // (4 * a - 1) + 1):
            w = 4 * a * d - 1
            if (n + a) % w == 0:
                sols.append((a, (n + a) // w, d))
    return sols

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        n = int(arg)
        s1, s2 = b1_solutions(n), c1_solutions(n)
        print(n, "b=1 line:", len(s1), s1[:3], "| c=1 line:", len(s2), s2[:3])


def line_counts_k(n, k):
    """numerator-k analogues: b=1 line c n + a + 1 = k a c d; c=1 line n + a + b = k a b d (counts)."""
    b1 = 0
    for a in range(1, n + 2):
        for d in range(max(1, -(-(n + 1) // (k * a))), (n + a + 1) // (k * a) + 1):
            m = k * a * d - n
            if m >= 1 and (a + 1) % m == 0:
                b1 += 1
    c1 = 0
    for a in range(1, n + 2):
        for d in range(1, (n + a) // (k * a - 1) + 1):
            if (n + a) % (k * a * d - 1) == 0:
                c1 += 1
    return b1, c1
