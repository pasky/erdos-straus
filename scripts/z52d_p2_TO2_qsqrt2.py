# Z0518: ES over O_K = Z[√2] with totally positive variables: 4/ν = 1/ξ+1/η+1/ζ, ξ,η,ζ ∈ O_K totally positive.
# Search: ν totally positive, non-rational (rational ν are trivial: an integer ES solution is already totally positive in O_K).
# For ξ,η in a box (|a|,|b| <= H), α = 4/ν − 1/ξ − 1/η; ζ = 1/α must be totally positive in O_K.
from fractions import Fraction as F
import itertools, json, math
s2 = math.sqrt(2)
def mul(x, y): return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def conj(x): return (x[0], -x[1])
def norm(x): return x[0]*x[0] - 2*x[1]*x[1]
def inv(x):
    n = norm(x); c = conj(x); return (F(c[0], 1)/n, F(c[1], 1)/n)
def tp(x):  # totally positive (real embeddings)
    return x[0] + x[1]*s2 > 0 and x[0] - x[1]*s2 > 0
def sub(x, y): return (x[0]-y[0], x[1]-y[1])
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def scal(c, x): return (c*x[0], c*x[1])
H = 12
box = [(a, b) for a in range(-H, H+1) for b in range(-H, H+1) if tp((a, b))]
inv_box = {}
for x in box: inv_box[x] = inv(x)
# ν candidates: totally positive non-rational elements with small norm
nus = [(a, b) for a in range(-6, 7) for b in range(-6, 7) if b != 0 and tp((a, b)) and abs(norm((a, b))) <= 20]
nus = sorted(set(nus), key=lambda x: (abs(norm(x)), x))
res = {}
for nu in nus:
    n_inv = inv(nu)
    t4 = scal(F(4), n_inv)                  # 4/ν
    found = None; tried = 0
    for xi in box:
        A = sub(t4, inv_box[xi])
        for eta in box:
            tried += 1
            al = sub(A, inv_box[eta])
            if al == (0, 0): continue
            if not tp((float(al[0]), float(al[1]))): continue
            N = norm(al)
            if N == 0: continue
            z = (al[0]*0 + inv(al)[0], inv(al)[1])
            # ζ = 1/α in O_K?
            if z[0].denominator == 1 and z[1].denominator == 1 and tp((float(z[0]), float(z[1]))):
                found = (xi, eta, (int(z[0]), int(z[1])))
                break
        if found: break
    res[str(nu)] = dict(norm=norm(nu), solution=found, pairs_tried=tried)
    print(nu, 'N=', norm(nu), 'solution:', found, flush=True)
json.dump(res, open('data/z52b/pass2/TO2/qsqrt2_search.json', 'w'), indent=1)
print('nus tested', len(nus), 'with solution', sum(1 for v in res.values() if v['solution']))
