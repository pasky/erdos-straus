# Z2794 part 1: the Rhind 2/n table (Wikipedia transcription of Chace/Clagett) checked against the scribes' rule
#   2/p = 1/a + sum_i 1/(p*a/d_i),  2a - p = sum of distinct divisors d_i of a   (Gillings/Bruins/Abdulaziz; mathpages kmath340)
# i.e. p divides every denominator except the first; this is the e-slice shape with kappa = 1 (exact sum, not a multiple).
from fractions import Fraction as F
T = """3:2,6 5:3,15 7:4,28 9:6,18 11:6,66 13:8,52,104 15:10,30 17:12,51,68 19:12,76,114 21:14,42 23:12,276 25:15,75
27:18,54 29:24,58,174,232 31:20,124,155 33:22,66 35:30,42 37:24,111,296 39:26,78 41:24,246,328 43:42,86,129,301 45:30,90
47:30,141,470 49:28,196 51:34,102 53:30,318,795 55:30,330 57:38,114 59:36,236,531 61:40,244,488,610 63:42,126 65:39,195
67:40,335,536 69:46,138 71:40,568,710 73:60,219,292,365 75:50,150 77:44,308 79:60,237,316,790 81:54,162 83:60,332,415,498
85:51,255 87:58,174 89:60,356,534,890 91:70,130 93:62,186 95:60,380,570 97:56,679,776 99:66,198 101:101,202,303,606"""
def isp(n): return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
ok = 0; rule = 0; rows = []
for tok in T.split():
    n, ds = tok.split(':'); n = int(n); ds = [int(x) for x in ds.split(',')]
    assert sum(F(1, d) for d in ds) == F(2, n), n
    ok += 1
    if isp(n):
        a = ds[0]; rest = ds[1:]
        shape = all(d % n == 0 for d in rest) and a % n != 0
        parts = [n * a // d for d in rest] if shape and all((n * a) % d == 0 for d in rest) else None
        rr = shape and parts is not None and all(a % x == 0 for x in parts) and sum(parts) == 2 * a - n
        rule += rr
        rows.append((n, a, 2 * a - n, parts, rr))
print(f"table entries verified exactly: {ok}/50")
print(f"prime entries following the scribes' rule (first denominator a with p∤a, 2a-p = sum of the listed parts, all dividing a): {rule}/{len(rows)}")
for r in rows: print("  p=%d a=%d 2a-p=%d parts=%s rule=%s" % r)
