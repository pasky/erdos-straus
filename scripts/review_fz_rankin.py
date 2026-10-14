"""review_fz_rankin.py (R220, from scratch): test of FF_STERILE_SMALL Lemma 4.1 (fixed-q Rankin/knapsack divisor bound).
Exhaustive over FACTORISATION TYPES (not over polynomials): the number of monic degree-d divisors of F = prod P_i^{e_i}
is [x^d] prod S_{e_i}(x^{deg P_i}); a type is, for each degree j, a multiset of exponents of at most I'(j) distinct
irreducibles (I'(1) = q - 1: T excluded), with sum j*e = n. Every F of degree n with T not| F has such a type and every
type is realised, so max over types = max over F (exact).
Bound: for each rho on a grid, rho^{-d'} exp(V_rho(n)), V_rho = fractional knapsack (own implementation, items
(j, e) of weight j, gain log(S_e(rho^j)/S_{e-1}(rho^j)), I'(j) copies). Also compares with fz_sum.c's lRk (via a C harness)
if --fz is given.  usage: uv run python scripts/review_fz_rankin.py q NMAX"""
import sys, math
from functools import lru_cache
sys.path.insert(0, 'scripts')
from review_fz_bounds import nirr

q, NMAX = int(sys.argv[1]), int(sys.argv[2])
I = [0] + [nirr(q, j) - (1 if j == 1 else 0) for j in range(1, NMAX + 1)]


def polymul(A, B, n):
    C = [0] * (n + 1)
    for i, x in enumerate(A):
        if x:
            for k, y in enumerate(B):
                if i + k > n:
                    break
                C[i + k] += x * y
    return C


def exps_multisets(W, maxparts, maxpart):
    """multisets (non-increasing tuples) of positive ints with sum W, <= maxparts parts, parts <= maxpart."""
    if W == 0:
        yield ()
        return
    if maxparts == 0:
        return
    for e in range(min(W, maxpart), 0, -1):
        for rest in exps_multisets(W - e, maxparts - 1, e):
            yield (e,) + rest


best = [[0] * (n + 1) for n in range(NMAX + 1)]   # best[n][d] = max #divisors of degree d


# enumerate all types with total degree <= NMAX: start with full budget, record at every node
def rec2(j, budget, poly, used):
    for d in range(used + 1):
        if poly[d] > best[used][d]:
            best[used][d] = poly[d]
    if j > budget:
        return
    for W in range(1, budget // j + 1):
        for ms in exps_multisets(W, I[j], W):
            pl = poly
            for e in ms:
                pl = polymul(pl, [1 if (k % j == 0 and k // j <= e) else 0 for k in range(j * e + 1)], NMAX)
            rec2(j + 1, budget - W * j, pl, used + W * j)
    rec2(j + 1, budget, poly, used) if j + 1 <= budget else None


rec2(1, NMAX, [1] + [0] * NMAX, 0)


def V(rho, n):
    items = []
    for j in range(1, n + 1):
        y = rho**j
        Sprev = 1.0
        for e in range(1, n // j + 1):
            Se = Sprev + y**e
            items.append((math.log(Se / Sprev) / j, j, I[j]))
            Sprev = Se
    items.sort(reverse=True)
    cap, val = float(n), 0.0
    for ratio, j, cnt in items:
        take = min(cap, cnt * j)
        val += take * ratio
        cap -= take
        if cap <= 0:
            break
    return val


viol, worst = 0, 0.0
grid = [k / 64 for k in range(1, 65)] + [0.3, 0.37, 0.5, 0.9]
for n in range(1, NMAX + 1):
    for d in range(n + 1):
        dp = min(d, n - d)
        c = best[n][d]
        for rho in grid:
            bd = rho**(-dp) * math.exp(V(rho, n))
            if c > bd * (1 + 1e-9):
                viol += 1
                print("VIOLATION", q, n, d, rho, c, bd)
        bmin = min(rho**(-dp) * math.exp(V(rho, n)) for rho in grid)
        worst = max(worst, c / bmin)
print(f"q={q} n<={NMAX}: Lemma 4.1 violations={viol}, max exact/min_rho bound={worst:.4f}")
print("max divisor counts best[NMAX][d]:", best[NMAX])

# optional: compare with the author's implementation fz_sum.c lRk (min over its 64-point rho grid), via a C harness
if len(sys.argv) > 3 and sys.argv[3] == '--fz':
    import subprocess, os
    h = '/tmp/review_fz_rk_harness'
    open(h + '.c', 'w').write('#define NO_MAIN\n#include "%s/scripts/fz_sum.c"\nint main(int c,char**v){int q=atoi(v[1]),N=atoi(v[2]);'
        'init_rankin(q);for(int n=1;n<=N;n++){for(int d=0;d<=n;d++)printf("%%.12Le ",expl(lRk(n,d)));printf("\\n");}}\n' % os.getcwd())
    subprocess.run(['gcc', '-O2', '-w', '-o', h, h + '.c', '-lm'], check=True)
    out = subprocess.run([h, str(q), str(NMAX)], capture_output=True, text=True, check=True).stdout.split('\n')
    bad, w = 0, 0.0
    for n in range(1, NMAX + 1):
        vals = [float(x) for x in out[n - 1].split()]
        for d in range(n + 1):
            if best[n][d] > vals[d] * (1 + 1e-9):
                bad += 1
                print("FZ lRk VIOLATION", n, d, best[n][d], vals[d])
            w = max(w, best[n][d] / vals[d])
    print(f"fz_sum lRk vs exact max: violations={bad}, max exact/lRk={w:.4f}")
