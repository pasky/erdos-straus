"""Z0047: ES over F_3[T] with pairwise DISTINCT monic denominators: T/P = 1/X+1/Y+1/Z, X,Y,Z monic, pairwise distinct.
Method A (complete, lemma-based): every solution has a denominator of degree n-1 (lemma of bs_ff_es / FUNCTIONFIELD_ES Lemma 1.3,
  validated below by brute force for n<=3). For each monic X of degree n-1: 1/Y+1/Z = E/(PX), E = TX-P; solve by divisors
  of (PX)^2: (E Y - D)(E Z - D) = D^2, D = PX.  Y,Z monic, distinct from each other and from X.
Method B (brute force, validation): all monic X<=Y of degree <= n+1, Z solved exactly.
Usage: python3 scripts/z52d_p2_NC0_Z0047.py NMAX"""
import sys, itertools, time, collections
sys.path.insert(0, 'scripts')
import bs_ff_es as E
E.Q = 3
Q = 3
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
A = (0, 1)

def monic_list(d):
    return [tuple(low) + (1,) for low in itertools.product(range(Q), repeat=d)]

def solve_two_term(N, D, fD2=None):
    """all monic (Y,Z) with 1/Y+1/Z = N/D, N,D nonzero polys, D monic. Returns list of (Y,Z) (Y<=Z not enforced; both orders)."""
    out = []
    f = dict(E.factor(D))
    f2 = {r: 2 * e for r, e in f.items()}
    divs = E.divisors_from(f2)
    D2 = E.mul(D, D)
    for c in range(1, Q):
        for m in divs:
            d = tuple((c * x) % Q for x in m)
            # Y = (D + d)/N must be a monic polynomial
            num_y = E.add(D, d)
            qy, ry = E.divmod_(num_y, N)
            if ry or not qy or qy[-1] != 1:
                continue
            q2, r2 = E.divmod_(D2, d)
            if r2:
                continue
            num_z = E.add(D, q2)
            qz, rz = E.divmod_(num_z, N)
            if rz or not qz or qz[-1] != 1:
                continue
            out.append((qy, qz))
    return out

def sols_lemma(P):
    """all (X,Y,Z) monic solutions of T/P = 1/X+1/Y+1/Z where X has degree n-1 (complete by the lemma)."""
    n = len(P) - 1
    res = []
    for X in monic_list(n - 1):
        N = E.sub(E.mul(A, X), P)
        if not N:
            continue
        D = E.mul(P, X)
        for Y, Z in solve_two_term(N, D):
            # exact check of the identity T*X*Y*Z = P*(XY+YZ+ZX)
            lhs = E.mul(A, E.mul(X, E.mul(Y, Z)))
            rhs = E.mul(P, E.add(E.add(E.mul(X, Y), E.mul(Y, Z)), E.mul(X, Z)))
            assert lhs == rhs, (X, Y, Z, P)
            res.append((X, Y, Z))
    return res

def sols_brute(P, maxdeg):
    n = len(P) - 1
    res = []
    polys = [p for d in range(1, maxdeg + 1) for p in monic_list(d)]
    for i, X in enumerate(polys):
        for Y in polys[i:]:
            num = E.sub(E.mul(A, E.mul(X, Y)), E.mul(P, E.add(X, Y)))
            if not num:
                continue
            Dn = E.mul(P, E.mul(X, Y))
            q, r = E.divmod_(Dn, num)
            if r or not q or q[-1] != 1:
                continue
            res.append((X, Y, q))
    return res

def distinct(t):
    X, Y, Z = t
    return X != Y and Y != Z and X != Z

if __name__ == "__main__":
    # validation of Method A against Method B for n = 2, 3 (all P with T∤P)
    for n in (2, 3):
        irr = [p for p in E.irreducibles(n) if E.divmod_(p, A)[1]]
        bad = 0
        for P in irr:
            a = set(tuple(sorted(map(tuple, s))) for s in [(x, y, z) for x, y, z in sols_lemma(P)])
            b_all = sols_brute(P, n + 1)
            b = set(tuple(sorted(map(tuple, s))) for s in [(x, y, z) for x, y, z in b_all])
            # brute force finds solutions with all denominators of degree <= n+1; compare sets of multisets
            if not b <= a:
                bad += 1
                print("MISMATCH (brute solution not found by lemma method)", n, P, flush=True)
            if (len(a) > 0) != (len(b) > 0):
                print("(expected: brute search bounded to deg<=n+1 for X,Y only) existence differs", n, P, len(a), len(b), flush=True)
        print(f"validation n={n}: irreducible={len(irr)} brute-solution-not-in-lemma-set={bad}", flush=True)
    t0 = time.time()
    for n in range(2, NMAX + 1):
        irr = [p for p in E.irreducibles(n) if E.divmod_(p, A)[1]]
        nd_ok = 0; any_sol = 0
        ex_dist = []
        for P in irr:
            S = sols_lemma(P)
            if S: any_sol += 1
            if any(distinct(s) for s in S):
                nd_ok += 1
            else:
                ex_dist.append(P)
        print(f"n={n}: irreducible P (T∤P)={len(irr)}; with any solution={any_sol}; with a DISTINCT-denominator solution={nd_ok}; "
              f"no distinct solution={len(ex_dist)}  time={time.time()-t0:.1f}s", flush=True)
        for P in ex_dist[:6]:
            print("   no-distinct P (low->high):", list(P), " any-solution:", len(sols_lemma(P)) > 0, flush=True)
