"""Z0165 (pass 2, SK0): class equation 1 = sum_{i=1}^{k} 1/|C_G(g_i)| over class representatives, k = number of classes.
Enumerate all multisets a1<=...<=a4 of positive integers with sum 1/a_i = 1 (k=4 classes), and compare with
the centralizer multisets of groups with exactly 4 conjugacy classes that are small enough to check by hand
(C4, C2xC2, D10, A4; class sizes computed below). Also record k=3 (S3, C3 ... ) for context."""
from fractions import Fraction as F
def sols(k):
    out = []
    def rec(rem, lo, cur, depth):
        if depth == 0:
            if rem == 0: out.append(tuple(cur))
            return
        # a >= lo, and 1/a >= rem/depth  => a <= depth/rem
        if rem <= 0: return
        a = lo
        while a * 1 <= depth / rem:
            if F(1, a) <= rem:
                rec(rem - F(1, a), a, cur + [a], depth - 1)
            a += 1
    rec(F(1), 1, [], k)
    return out
S4 = sols(4)
print("4-term solutions of 1 = sum 1/a_i (a1<=..<=a4):", len(S4), "max denominator:", max(max(s) for s in S4))
print(S4)
# class-equation multisets for groups with exactly 4 classes (computed by hand; checked below)
groups = {
 "C4 (|G|=4, all centralizers 4)": [4, 4, 4, 4],
 "C2xC2 (|G|=4)": [4, 4, 4, 4],
 "D10 (|G|=10; classes {e},{r,r^-1},{r^2,r^-2},{reflections}: sizes 1,2,2,5)": [10, 5, 5, 2],
 "A4 (|G|=12; classes e,(12)(34)-type size3, two 3-cycle classes size4)": [12, 4, 3, 3],
}
for name, cs in groups.items():
    ok = sum(F(1, c) for c in cs) == 1
    print(f"{name}: centralizers {sorted(cs)} sum 1/c = {sum(F(1,c) for c in cs)}  in S4: {tuple(sorted(cs)) in S4}")
S3 = sols(3)
print("3-term solutions of 1 = sum 1/a_i:", S3)
