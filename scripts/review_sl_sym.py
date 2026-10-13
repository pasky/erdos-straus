"""R175: check Lemma 3.1 (symmetries) and the 'height 1' remark on review_sl_caseB K<=13 output."""
import sys
sys.path.insert(0, 'scripts')
import io, contextlib
from review_sl_caseB import enum, union_measure, covered, mul, add, neg, P
with contextlib.redirect_stdout(io.StringIO()):
    sols = enum(int(sys.argv[1]))
# parity facts used implicitly by Lemma 3.1(ii)
par = [(a % 2 == b % 2, (1 + a + len(mul(g, L2)) - 1) % 2 == 0) for K, a, b, vc, (h1, h2, g, L2, r) in sols]
print("all a=b mod 2:", all(x for x, _ in par), " all deg E even:", all(y for _, y in par))
# naive 'homogeneous' transform without parity: does (I) survive for each solution after T->-T + monic rescale?
def sig(f):  # f(-T) rescaled monic
    g = [(c * (-1) ** i) % P for i, c in enumerate(f)]
    return g if g[-1] == 1 else neg(g)
m, mins = union_measure([s[3] for s in sols])
def inv_series(v, n):  # v of u^{-1}, u = 1 + T v
    u = [1] + v[:n]
    w = [1] + [0] * n
    for i in range(1, n + 1):
        w[i] = (-sum(u[j] * w[i - j] for j in range(1, i + 1))) % P
    return w[1:]
n = 30
import itertools
bad_i = bad_ii = 0
for pref in itertools.product(range(3), repeat=7):
    if pref[0] == 0: continue
    v = list(pref) + [0] * n
    c = covered(v, mins)
    # (i) u -> 1/u
    if c != covered(inv_series(v, n + 6), mins): bad_i += 1
    # (ii) u(T) -> u(-T): v(T) -> -v(-T)
    v2 = [(-x * (-1) ** i) % P for i, x in enumerate(v)]
    if c != covered(v2, mins): bad_ii += 1
print("prefix-7 test points (zero tail) violating (i):", bad_i, " (ii):", bad_ii)
# height-1 rational points u = (1+aT)/(1+bT), a != b
for a in range(3):
    for b in range(3):
        if a == b: continue
        ub = inv_series([b] + [0] * 40, 40)  # 1/(1+bT) -> v-part
        uinv = [1] + ub
        num = [1, a] + [0] * 40
        uu = [sum(num[j] * uinv[i - j] for j in range(i + 1)) % P for i in range(41)]
        v = uu[1:]
        print(f"u=(1+{a}T)/(1+{b}T): v prefix {v[:6]} covered={covered(v, mins)}")
