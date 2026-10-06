"""Complete enumeration of T-generic boxes of exact T-level F for families II2, II1, I4
(POINTWISE_MORDELL §2.1 rigid forms; point x_q = 1 for q not in T).

usage: mordell_rigid.py T(comma) amax  -> pickles boxes {(F, res): (fam, params)} for all
F = prod q^{a_q}, 0 <= a_q <= amax, F > 1, to /tmp/o80_rigid_<T>_<amax>.pkl
II2: (4dja-F)(4djm-F) = F^2+4dj^2, a+m = g j, f = F g, (g,T)=1, box -4a^2 d mod F.
II1/I4: 4i u v w = F(u+v+w); {a,b,k} = {u,v,w}; ab = F*n with n T-free;
        e = 4i ab/F - 1, gcd(e,4ab)=1; box -e (II1), -1/e (I4) mod F.
"""
import sys, pickle, itertools, time
from math import gcd, isqrt

def tfree(m, T):
    for q in T:
        while m % q == 0:
            m //= q
    return m

def ii2(F, T, out):
    d = 1
    while 4 * d - 1 <= 2 * F:
        jmax = (2 * F) // (4 * d - 1) + 1
        for j in range(1, jmax + 1):
            K = 4 * d * j
            P = F * F + 4 * d * j * j
            A = (-F) % K or K
            while A * A <= P:
                if P % A == 0:
                    B = P // A
                    for A1, B1 in ((A, B), (B, A)):
                        if (A1 + F) % K or (B1 + F) % K:
                            continue
                        a = (A1 + F) // K; m = (B1 + F) // K
                        if (a + m) % j:
                            continue
                        g = (a + m) // j
                        if tfree(g, T) != g:
                            continue
                        f = F * g
                        assert (f + 1) % (4 * a * d) == 0 and (4 * a * a * d + 1) % g == 0
                        key = (F, (-4 * a * a * d) % F)
                        out.setdefault(key, ('II2', (a, d, f)))
                A += K
        d += 1

def ii1(F, T, out):
    i = 1
    while 4 * i <= 3 * F + 3:
        u = 1
        while u * u * 4 * i <= 3 * F:
            v = max(u, F // (4 * i * u) + 1)
            while 4 * i * u * v <= 3 * F:
                D = 4 * i * u * v - F
                if D > 0 and (F * (u + v)) % D == 0:
                    w = F * (u + v) // D
                    if w >= v:
                        for k, a, b in ((u, v, w), (v, u, w), (w, u, v)):
                            if (a * b) % F or tfree(a * b // F, T) != a * b // F:
                                continue
                            e = 4 * i * (a * b // F) - 1
                            if (a + b) % e or gcd(e, 4 * a * b) != 1:
                                continue
                            out.setdefault((F, (-e) % F), ('II1', (a, b, e)))
                            out.setdefault((F, (-pow(e, -1, F)) % F), ('I4', (a, b, e)))
                v += 1
            u += 1
        i += 1

def main():
    T = [int(t) for t in sys.argv[1].split(',')]
    amax = int(sys.argv[2])
    out = {}
    for exps in itertools.product(range(amax + 1), repeat=len(T)):
        F = 1
        for q, e in zip(T, exps):
            F *= q ** e
        if F == 1:
            continue
        t0 = time.time()
        n0 = len(out)
        ii1(F, T, out)
        ii2(F, T, out)
        print(F, exps, len(out) - n0, f"{time.time()-t0:.0f}s", flush=True)
    pickle.dump(out, open(f"/tmp/o80_rigid_{sys.argv[1]}_{amax}.pkl", "wb"))

if __name__ == '__main__':
    main()
