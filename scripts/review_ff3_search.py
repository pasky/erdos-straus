"""review_ff3_search.py (R173): independent Case B search at slice points x = 1 off T, x = u mod T^inf.

Method (deliberately different from scripts/ff3_caseB.c): for each monic L' (T not | L'), each j, each branch,
the least CRT residue rho_N = L' * h_N - 1 with h_N = (1 - w)/L' mod T^(N+1) (w = u or u^{-1}) is read off ONE
power series per (L', branch).  Then every monic divisor g' of L' (enumerated by factoring L') and every
gamma <= j is tested directly: rho | 1 + T^(N+1+gamma) L' g'  <=>  T^(N+1) L' g' T^gamma == -1 (mod rho).
No modular inverse, no solving for g'.

mode 'brute' (small ranges): for every (L', j, gamma, g' | L') factor D = 1 + T^(N+1+gamma) L' g' completely and
test every monic divisor E (no CRT shortcut, no Lemma 1.2); compare family sets.

usage: review_ff3_search.py p k LMIN LMAX JMAX mode u0 u1 ...   (JMAX = -1: j <= 4l - k)
"""
import sys
import time
import review_ff3_poly as F


def search(p, k, lmin, lmax, jmax, u, log=print, brute=False):
    F.setp(p)
    nmax = k + (jmax if jmax >= 0 else 4 * lmax) + 2
    U = F.trunc(u + [0] * nmax, nmax + 1)
    assert U and U[0] == 1, "needs u(0)=1"
    Ui = F.series_inv(U, nmax + 1)
    fams = set()
    tested = 0
    minus1 = [p - 1]
    for l in range(lmin, lmax + 1):
        t0 = time.time()
        nl = 0
        for L in F.all_monic(l):
            if L[0] == 0:
                continue
            JM = jmax if jmax >= 0 else 4 * l - k
            divs = F.divisors(L)
            if brute:
                for j in range(0, JM + 1):
                    N = k + j - 1
                    mN = N + 1
                    for gam in range(0, j + 1):
                        for g in divs:
                            D = F.add([1], F.mul(F.Tpow(N + 1 + gam), F.mul(L, g)))
                            for E in F.divisors(D):
                                if len(E) < 2:
                                    continue
                                # E == -u mod T^(N+1), E == -1 mod L'
                                if F.trunc(F.add(E, U), mN):
                                    continue
                                if l > 0 and F.mod(F.add(E, [1]), L):
                                    continue
                                fams.add((l, tuple(L), j, gam, tuple(g), tuple(E)))
                                nl += 1
                continue
            Li = F.series_inv(L, nmax + 1)
            for br, W in ((0, U), (1, Ui)):
                omw = F.sub([1], W)
                hfull = F.trunc(F.mul(omw, Li), nmax + 1)
                for j in range(0, JM + 1):
                    N = k + j - 1
                    h = F.trunc(hfull, N + 1)
                    if not h:
                        continue
                    rho = F.add(F.mul(L, h), minus1)
                    if len(rho) < 2 or rho[-1] != 1:
                        continue
                    tested += 1
                    x = F.mod(F.mul(F.Tpow(N + 1), L), rho)
                    for g in divs:
                        y = F.mod(F.mul(x, g), rho)
                        for gam in range(0, j + 1):
                            if y == minus1:
                                D = F.add([1], F.mul(F.Tpow(N + 1 + gam), F.mul(L, g)))
                                if br == 0:
                                    E = rho
                                else:
                                    E, r = F.divmod_(D, rho)
                                    assert not r
                                # independent re-verification of the congruences
                                assert not F.trunc(F.add(E, U), N + 1)
                                assert l == 0 or not F.mod(F.add(E, [1]), L)
                                assert not F.mod(D, E) and F.monic(E)
                                key = (l, tuple(L), j, gam, tuple(g), tuple(E))
                                if key not in fams:
                                    fams.add(key)
                                    nl += 1
                            y = F.mod([0] + y, rho) if y else []
        log(f"l={l} families_l={nl} total={len(fams)} rho_tested={tested} time={time.time()-t0:.1f}s")
    return fams


if __name__ == "__main__":
    p, k, lmin, lmax, jmax = map(int, sys.argv[1:6])
    mode = sys.argv[6]
    u = [int(x) % p for x in sys.argv[7:]]
    print(f"# review_ff3_search p={p} k={k} l={lmin}..{lmax} jmax={jmax} mode={mode} u={u}", flush=True)
    fams = search(p, k, lmin, lmax, jmax, u, log=lambda s: print(s, flush=True), brute=(mode == "brute"))
    for f in sorted(fams):
        print("FAM l=%d L'=%s j=%d gam=%d g'=%s E=%s" % (f[0], list(f[1]), f[2], f[3], list(f[4]), list(f[5])))
