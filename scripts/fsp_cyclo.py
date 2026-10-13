"""fsp_cyclo.py (O179, FF_STERILE_PROOF.md §3): targeted search for CYCLOTOMIC Case B solutions (r = r0 constant)
at large level K on the slice x = 1 off T, q = 3, A = T^2, and their distance to x*_c (u = 1 + cT).
Cyclotomic solution: H H' L'' = T^K + r0 (r0 = 1, 2), H + H' = T g' r0, g' monic, g'(0) != 0 (all monic).
For each K, factor T^K + r0 over F_3 (sympy), enumerate every distribution of the irreducible factors into (H, H', L''),
test (I), and report, per solution, z := v_T(H L' + c) (agreement of the covered cylinder with x*_c) versus the
needed N0 = ceil(K/2) + 1  (covers x*_c iff z >= N0).
usage: fsp_cyclo.py KMIN KMAX [CAP]   prints per K: #solutions, best z for c = 1, 2, N0, and any x* hit."""
import sys, itertools
import sympy as sp
sys.path.insert(0, 'scripts')
from fsp_enum import add, mul, trim

Tsym = sp.symbols('T')
def to_list(p):
    c = sp.Poly(p, Tsym, modulus=3).all_coeffs()[::-1]
    return trim([int(x) % 3 for x in c])

def vT(p):
    for i, x in enumerate(p):
        if x: return i
    return 10**9

def run(K, r0, cap):
    fl = sp.factor_list(Tsym**K + r0, modulus=3)[1]
    facs = [(to_list(f), m) for f, m in fl]
    # make factors monic
    mf = []
    for f, m in facs:
        inv = 1 if f[-1] == 1 else 2
        mf.append(([x * inv % 3 for x in f], m))
    opts = []
    tot = 1
    for f, m in mf:
        pw = [[1]]
        for _ in range(m): pw.append(mul(pw[-1], f))
        o = [(pw[i], pw[j], pw[m - i - j]) for i in range(m + 1) for j in range(m + 1 - i)]
        opts.append(o); tot *= len(o)
    if tot > cap: return None
    sols = []
    for combo in itertools.product(*opts):
        H, Hp, Lpp = [1], [1], [1]
        for h, hp, l in combo:
            H = mul(H, h); Hp = mul(Hp, hp); Lpp = mul(Lpp, l)
        if H[0] != (-Hp[0]) % 3: continue
        S = add(H, Hp)
        if not S or S[0] != 0: continue
        g = [x * r0 % 3 for x in S[1:]]      # g' = (H+H')/(T r0), r0^{-1} = r0
        if g[-1] != 1 or g[0] == 0: continue
        Lp = mul(g, Lpp)
        X = mul(H, Lp)
        sols.append((len(H) - 1, len(Hp) - 1, X))
    return sols

def main():
    K0, K1 = int(sys.argv[1]), int(sys.argv[2]); cap = int(sys.argv[3]) if len(sys.argv) > 3 else 200000
    for K in range(K0, K1 + 1):
        N0 = -(-K // 2) + 1
        out = []
        for r0 in (1, 2):
            s = run(K, r0, cap)
            if s is None: out.append(f"r0={r0}:SKIP"); continue
            best = {}
            for c in (1, 2):
                zs = [vT(add(X, [c])) for (a, b, X) in s]
                best[c] = max(zs) if zs else -1
                for (a, b, X), z in zip(s, zs):
                    if z >= N0: print(f"HIT x*_{c}: K={K} r0={r0} a={a} b={b}", flush=True)
            out.append(f"r0={r0}:n={len(s)} zbest(c=1,2)=({best[1]},{best[2]})")
        print(K, "N0", N0, " ".join(out), flush=True)

if __name__ == '__main__':
    main()
