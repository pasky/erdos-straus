# Z2811: signature of closures of 3-braid lifts of gamma_w, via spherogram's pure-python seifert_matrix (uv --with snappy).
# Convention check: sigma(K) = -sign(V+V^T) with spherogram's V (positive trefoil -> -2, T(2,5) -> -4, T(3,4) -> -6).
# Lift: T=[[1,1],[0,1]] <- s1, S'=[[0,1],[-1,0]] <- s1 s2 s1 (for the B3 -> SL2 map s1 -> T, s2 -> [[1,0],[-1,1]]);
# HJ factor [[v,-1],[1,0]] = T^v S, S = [[0,-1],[1,0]]; lift T^v S -> s1^v (s1 s2 s1)^{-1}... we check the image numerically.
import sys, itertools
import numpy as np
import spherogram
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
def sig(word):
    if not word: return None
    Lk = spherogram.Link(braid_closure=word)
    V = np.array(Lk.seifert_matrix().tolist() if hasattr(Lk.seifert_matrix(), 'tolist') else Lk.seifert_matrix(), dtype=float)
    ev = np.linalg.eigvalsh(V + V.T)
    return -int(sum(np.sign(ev)))
if __name__ == "__main__":
    print("convention:", sig([1,1,1]), sig([1]*5), sig([1,2]*4), sig([1,-2,1,-2]), sig([1,2]*3))
def lift(t, u, v):
    # gamma_w = [[v,-1],[1,0]][[t,-1],[1,0]][[u,-1],[1,0]] = [[p,-A*],[A,-t]], lift W(x) = s1^x (s1 s2 s1)^{-1}
    H = [-1, -2, -1]
    w = []
    for x in (v, t, u):
        w += [1]*x + H
    return w
def check_image(word):
    # SL2 image under s1 -> [[1,1],[0,1]], s2 -> [[1,0],[-1,1]], s^{-1} inverses
    M = np.eye(2, dtype=object)
    A = {1: np.array([[1,1],[0,1]], dtype=object), 2: np.array([[1,0],[-1,1]], dtype=object)}
    for g in word:
        mat = A[abs(g)] if g > 0 else np.array(np.round(np.linalg.inv(A[abs(g)].astype(float))), dtype=object)
        M = M.dot(mat)
    return M
if __name__ == "__main__" and len(sys.argv) > 1:
    P = int(sys.argv[1])
    from collections import Counter
    rows = []
    bad = 0
    for p in L.primes_upto(P):
        if p < 5: continue
        for (t, u, v) in L.words(p):
            w = lift(t, u, v)
            M = check_image(w)
            A = t*u-1; As = t*v-1
            if not (M[0,0] == p and M[1,0] == A and M[1,1] == -t and M[0,1] == -As):
                bad += 1
            s = sig(w)
            rows.append((p, (t, u, v), A, L.legendre(A, p), s))
    print("words", len(rows), "image mismatches", bad)
    print("signature distribution:", sorted(Counter(r[4] for r in rows).items()))
    # relation to the sign: (sig, sign)
    print("(signature, Legendre sign) counts:", sorted(Counter((r[4], r[3]) for r in rows).items()))
    print("(signature mod 4, Legendre sign):", sorted(Counter((r[4] % 4, r[3]) for r in rows).items()))
    print("(signature mod 8, p mod 8, sign):", sorted(Counter((r[4] % 8, r[0] % 8, r[3]) for r in rows).items()))
    open('data/z52b/pass2/NC3/braidsig_rows.txt', 'w').write(''.join(f'{r[0]} {r[1][0]} {r[1][1]} {r[1][2]} {r[2]} {r[3]} {r[4]}\n' for r in rows))
