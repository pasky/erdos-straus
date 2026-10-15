"""R234: Heegner-layer algebra (z9_heegner_layers (a)) and an edge-wise test of the 'class condition without ring condition'.
For each class L in G^-_p (p <= P) and t <= T: search trace-zero eps in E(L) with nrd eps = t p, trace-zero j in E(L) with
<j, eps> = 0, nrd j = A, A | tp+1, A = -1 (mod t), and i := (1+eps) j / A in E(L). Record whether moreover the ring condition
(1-i)(1-j) in t E(L) holds, and whether L is a path class."""
import sys
import review_r234_quat as Q
from review_r234_lib import *


def elt(B, x):
    return Q.from_vec([sum(x[i] * B[i][j] for i in range(4)) for j in range(4)])


def in_order(B, z):
    """z (dict) in Z-span of B (rows, C0 coords)?"""
    import sympy
    M = sympy.Matrix([[sympy.Rational(c.numerator, c.denominator) for c in r] for r in B]).T
    v = Q.to_vec(z)
    s = M.LUsolve(sympy.Matrix([sympy.Rational(c.numerator, c.denominator) for c in v]))
    return all(c.q == 1 for c in s)


def run(P, T):
    stats = dict(classes=0, path=0, cond=0, cond_nonpath=0, ring=0, ring_nonpath=0, algebra_checks=0)
    for p in primes_1mod4(5, P):
        paths = {}
        for w in words(p):
            G = path_gram(w)
            if aniso_at_p(G, p):
                paths.setdefault(canon(G), []).append(w)
        for k in [k for k in classes_det_p(p) if aniso_at_p(key_to_gram(k), p)]:
            G = key_to_gram(k); Q.GLOBAL_G = G
            B = Q.overorder(G)
            els = [Q.from_vec(b) for b in B]
            N = [[(Q.nrd(Q.add(els[i], els[j])) - Q.nrd(els[i]) - Q.nrd(els[j])) / 2 if i != j else Q.nrd(els[i]) for j in range(4)] for i in range(4)]
            maxA = max(T * p + 1, 1)
            sv = Q.short_vectors(N, maxA)
            tz = [(q, elt(B, x)) for q, x in sv]
            tz = [(q, z) for q, z in tz if Q.trd(z) == 0]
            cond = ring = False
            for t in range(1, T + 1):
                for qe, e in tz:
                    if qe != t * p:
                        continue
                    for qj, jj in tz:
                        A = qj
                        if (t * p + 1) % A or (A + 1) % t:
                            continue
                        if Q.trd(Q.mul(e, Q.rev(jj), G)) != 0:
                            continue
                        one = {(): Fr(1)}
                        i = Q.scal(Q.mul(Q.add(one, e), jj, G), Fr(1, A))
                        if not in_order(B, i):
                            continue
                        cond = True
                        # algebra checks (z9_heegner (a)) in this setting
                        assert Q.trd(i) == 0 and Q.nrd(i) == (t * p + 1) // A
                        ij = Q.mul(i, jj, G); ji = Q.mul(jj, i, G)
                        assert Q.add(ij, ji) == {(): Fr(-2)}
                        assert Q.add(e, Q.add(one, ij)) == {}  # eps = -(1 + ij)
                        stats['algebra_checks'] += 1
                        r = Q.mul(Q.add(one, Q.scal(i, -1)), Q.add(one, Q.scal(jj, -1)), G)
                        if in_order(B, Q.scal(r, Fr(1, t))):
                            ring = True
            ispath = k in paths
            stats['classes'] += 1; stats['path'] += ispath
            stats['cond'] += cond; stats['ring'] += ring
            if cond and not ispath:
                stats['cond_nonpath'] += 1; print('COND but not path:', p, k)
            if ring and not ispath:
                stats['ring_nonpath'] += 1; print('RING but not path (would contradict Cor 2.2):', p, k)
            if ispath and not cond and min(w[0] for w in paths[k]) <= T:
                print('path class with t<=T but no (eps,j) found:', p, k, paths[k])
    print('P', P, 'T', T, stats)


if __name__ == '__main__':
    run(int(sys.argv[1]), int(sys.argv[2]))
