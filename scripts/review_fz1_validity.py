"""review_fz1_validity.py (R226): definition-level sanity check of the k = 1 Case B cylinder (FF_STERILE_SMALL §6):
for every tuple (B^{k=1}) found by review_fz1_tuples-style enumeration at q = 9 (s <= SMAX), with E(0) not in F_3, and for
every split s = j + 1 + gamma (0 <= gamma <= j), the family (E; 0, a0 = T^gamma g'; 2, b0 = T^j L') must be VALID at
P = x_u mod W_F for u = -E mod T^{j+1} (FUNCTIONFIELD_ES §6.2 definition: T a0, T b0 | P + E, s = a0 + X/b0 != 0, E | s,
lc(s) = lc(E)), and INVALID for every u' = u + c T^j, c != 0 (so the cylinder has depth exactly j + 1 on the slice u0 = -E(0)).
usage: review_fz1_validity.py q D SMAX"""
import sys
sys.path.insert(0, 'scripts')
from review_fz1_ff import GF

def series_inv(F, f, m):
    """inverse of f mod T^m (f(0) != 0)"""
    inv0 = F.inv[f[0]]; g = [inv0]
    for k in range(1, m):
        acc = 0
        for i in range(1, k + 1):
            if i < len(f): acc = F.add[acc][F.mul[f[i]][g[k - i]]]
        g.append(F.mul[F.neg[acc]][inv0])
    return F.trim(g)

def modT(F, f, m): return F.trim(list(f[:m]))

def main():
    q, D, SMAX = map(int, sys.argv[1:4]); F = GF(q)
    mon = {d: list(F.polys(d, monic=True, Tfree=True)) for d in range(D + 1)}
    ntest = nvalid = nbad = 0
    for z in range(D + 1):
        for a in range(D + 1 - z):
            for y in range(D + 1 - z - a):
                for m in mon[z]:
                    for g in mon[y]:
                        L = F.pmul(m, g)
                        for w in mon[a]:
                            E = F.psub(F.pmul(L, w), F.const(1))
                            if F.deg(E) < 1: continue
                            for s in range(2, SMAX + 1):
                                C, rem = F.pdivmod(F.padd(F.pmul(g, F.T(s)), w), E)
                                if rem or not C or C[-1] != 1 or C[0] == 0: continue
                                v = F.psub(F.pmul(F.pmul(m, w), C), F.T(s))
                                if not v or v[0] == 0 or F.padd(w, C) != F.pmul(g, v): continue
                                if E[0] in F.F3star: continue
                                for j in range((s - 1 + 1) // 2, s):
                                    gam = s - 1 - j
                                    if gam > j or gam < 0: continue
                                    a0 = F.pmul(F.T(gam), g); b0 = F.pmul(F.T(j), L)
                                    for c in range(q):
                                        # u = -E mod T^{j+1}, perturbed by c T^j
                                        u = F.padd(modT(F, F.pneg(E), j + 1), F.pmul(F.const(c), F.T(j)) if c else ())
                                        M = F.pmul(E, L)                 # E monic here; P = 1 mod E L'
                                        # P = 1 + M h, P = u mod T^{j+1}: h = (u - 1) M^{-1} mod T^{j+1}
                                        h0 = modT(F, F.pmul(F.psub(u, F.const(1)), series_inv(F, M, j + 1)), j + 1)
                                        h = F.padd(h0, F.T(j + 1 + 3 + F.deg(a0) + F.deg(b0)))
                                        P = F.padd(F.const(1), F.pmul(M, h))
                                        X, r1 = F.pdivmod(F.padd(P, E), F.T(1))
                                        ok = not r1 and F.pdivides(a0, X) and F.pdivides(b0, X)
                                        if ok:
                                            sv = F.padd(a0, F.pdivmod(X, b0)[0])
                                            ok = bool(sv) and F.lc(sv) == F.lc(E) and F.pdivides(E, sv)
                                        ntest += 1
                                        if (c == 0) != ok: nbad += 1; print("MISMATCH", s, j, c, m, g, w, C, ok)
                                        nvalid += ok
    print(f"q={q} D={D} s<={SMAX}: {ntest} (tuple, j, u) tests on slices E(0) not in F_3, {nvalid} valid; mismatches with the cylinder claim: {nbad}")
    sys.exit(1 if nbad else 0)
main()
