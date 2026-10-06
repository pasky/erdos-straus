"""Review R67b: from-scratch exact check of LS5 Lemma 3.1 (label partition) in
the product model, full R(M) family + selectors over a small prime pool.

Coordinates u_p uniform on Z/p, p in POOL.  Classes: for every M | prod(POOL),
M = 3 (mod 4), A=(M+1)/4, D | A^2: label lambda = -4D (D<=A) or -1/(4D') with
residue -4D mod M; plus selectors 0 mod p (label 0).  For S subset of POOL:
  LHS = P(E_S), E_S = every l in S lies in the modulus of a matched class;
  RHS = prod_{l in S} 1/l * sum_{partitions (U_j)} sum_{distinct (lambda_j)}
        P_y(for all j exists class (lambda_j, G), G cap S = Q_j subset U_j u CS_j,
            Q_j cap U_j nonempty, y = lambda_j on G minus S).
Checks LHS <= RHS exactly (Fractions), plus the pointwise construction of the
proof for every point of E_S.
"""
import itertools, sys
from fractions import Fraction as Fr
from math import prod

POOL = [int(t) for t in (sys.argv[1] if len(sys.argv) > 1 else "3,7,11,19").split(",")]
MAXS = int(sys.argv[2]) if len(sys.argv) > 2 else 3


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def res(lam, p):  # lam = (num, den) rational
    n, d = lam
    if d % p == 0:
        return None  # label not defined mod p (then p never in a modulus with it)
    return (n * pow(d, -1, p)) % p


classes = []  # (frozenset primes, label (num,den))
for k in range(1, len(POOL) + 1):
    for Ps in itertools.combinations(POOL, k):
        M = prod(Ps)
        if M % 4 != 3:
            continue
        A = (M + 1) // 4
        for D in divisors(A * A):
            lam = (-4 * D, 1) if D <= A else (-1, 4 * (A * A // D))
            assert all(res(lam, p) == (-4 * D) % p for p in Ps)
            classes.append((frozenset(Ps), lam))
for p in POOL:
    classes.append((frozenset([p]), (0, 1)))
labels = sorted({c[1] for c in classes})
print(f"pool {POOL}: {len(classes)} classes, {len(labels)} labels")


def matched(c, u):
    G, lam = c
    return all(u[p] == res(lam, p) for p in G)


def set_partitions(s):
    s = list(s)
    if not s:
        yield []
        return
    first, rest = s[0], s[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i] + [[first] + part[i]] + part[i + 1:]
        yield [[first]] + part


grid = list(itertools.product(*[range(p) for p in POOL]))
worst = 0
for k in range(1, MAXS + 1):
    for S in itertools.combinations(POOL, k):
        Sset = set(S)
        out = [p for p in POOL if p not in Sset]
        # LHS and pointwise check
        cnt = 0
        for t in grid:
            u = dict(zip(POOL, t))
            wit = {}
            for l in S:
                for c in classes:
                    if l in c[0] and matched(c, u):
                        wit[l] = c; break
            if len(wit) < len(S):
                continue
            cnt += 1
            # proof construction: group by label, check G cap S subset U_j u CS_j
            blocks = {}
            for l, c in wit.items():
                blocks.setdefault(c[1], set()).add(l)
            jof = {l: wit[l][1] for l in S}
            for lam, U in blocks.items():
                for l in U:
                    G = wit[l][0]
                    for q in G & Sset:
                        assert q in U or res(jof[q], q) == res(lam, q)
        LHS = Fr(cnt, len(grid))
        # RHS
        ygrid = list(itertools.product(*[range(p) for p in out]))
        tot = Fr(0)
        for part in set_partitions(S):
            cand = []
            for U in part:
                cand.append([lam for lam in labels if any(c[1] == lam and c[0] & set(U) for c in classes)])
            for labs in itertools.product(*cand):
                if len(set(labs)) < len(labs):
                    continue
                jl = {}
                for U, lam in zip(part, labs):
                    for q in U:
                        jl[q] = lam
                good = 0
                # classes usable by block j (CS_j depends only on partition+labels)
                usable = []
                for U, lam in zip(part, labs):
                    CS = {q for q in Sset - set(U) if res(lam, q) is not None and res(jl[q], q) == res(lam, q)}
                    usable.append([c for c in classes if c[1] == lam and (c[0] & set(U))
                                   and (c[0] & Sset) <= set(U) | CS])
                if any(not uj for uj in usable):
                    continue
                for ty in ygrid:
                    y = dict(zip(out, ty))
                    if all(any(all(y[p] == res(c[1], p) for p in c[0] - Sset) for c in uj) for uj in usable):
                        good += 1
                tot += Fr(good, len(ygrid))
        RHS = tot / prod(S)
        assert LHS <= RHS, (S, LHS, RHS)
        worst = max(worst, float(LHS / RHS) if RHS else 0)
        print(f"S={S}: P(E_S)={float(LHS):.5f}  RHS={float(RHS):.5f}  ratio={float(LHS/RHS):.3f}")
print(f"Lemma 3.1 inequality and pointwise construction verified; max LHS/RHS = {worst:.3f}")
