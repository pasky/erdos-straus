"""U01 function-field checks over F_5[T] using scripts/bs_ff_es.py (char>=5 engine, Q=5).
Counts ES_5(A,P) = #{witnesses} (first_only=False) for monic-denominator decompositions A/P = 1/X+1/Y+1/Z.
Items: Z0355 (sign twist: A=T vs A=2T, 2 a non-square mod 5), Z0892 (P ≡ 1 mod every irreducible of deg<=1),
Z0893 (Euler-type average over irreducibles), Z0894 (P square mod every deg-1 irreducible = pseudosquare-type),
numerator A = 4 (the ES analogue)."""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bs_ff_es as E
E.Q = 5
def count(A, P):
    A, P = tuple(A), tuple(P)
    return sum(1 for _ in E.es_solutions(A, P, first_only=False))
def evalp(P, c):
    return sum(co*pow(c, i, 5) for i, co in enumerate(P)) % 5
def monic_polys(d):
    for cs in itertools.product(range(5), repeat=d):
        yield list(cs) + [1]
def quad_res_mod_lin(P, c):  # P(c) is a nonzero square in F5 (or zero handled separately)
    return evalp(P, c) in (1, 4)
degs = [3, 4]
for d in degs:
    allP = list(monic_polys(d))
    # Z0892: P(c) == 1 for c in F5 (P ≡ 1 mod all deg-1 irreducibles) and P(0)=1
    special = [P for P in allP if all(evalp(P, c) == 1 for c in range(5))]
    rest = [P for P in allP if P not in special]
    cs = [count([4], P) for P in special]
    cr = [count([4], P) for P in random.Random(1).sample(rest, min(60, len(rest)))]
    print(f"Z0892 d={d}: P≡1 on F5 ({len(special)} polys): mean #ES={sum(cs)/max(1,len(cs)):.2f}; random ({len(cr)} sampled): mean={sum(cr)/max(1,len(cr)):.2f}", flush=True)
    # Z0894 pseudosquare-type: P(c) is a nonzero square for every c in F5
    ps = [P for P in allP if all(evalp(P, c) in (1, 4) for c in range(5))]
    cp = [count([4], P) for P in ps]
    print(f"Z0894 d={d}: P(c) square for all c ({len(ps)} polys): mean #ES={sum(cp)/max(1,len(cp)):.2f}", flush=True)
    # Z0355: sign twist, A=T (c=1) vs A=2T (c=2 non-square mod 5)
    c1 = sum(count([0, 1], P) for P in allP)
    c2 = sum(count([0, 2], P) for P in allP)
    print(f"Z0355 d={d}: sum over all monic P of #ES for A=T: {c1}; A=2T (non-square twist): {c2}", flush=True)
    # Z0893: average over monic irreducible P of degree d of #ES(A=4,P)
    irr = [P for P in allP if E.is_irred(tuple(P))]
    avg = sum(count([4], P) for P in irr)/max(1,len(irr))
    print(f"Z0893 d={d}: monic irreducibles of degree {d}: {len(irr)}, mean #ES(4,P) = {avg:.3f}", flush=True)
# --- follow-up (Z0892/Z0894 need deg>=5 for P≡1 on all of F5; constant numerators) ---
print("constant numerators:", {c: sum(count([c], P) for P in monic_polys(3)) for c in (1, 2, 3, 4)}, flush=True)
d = 5
allP = list(monic_polys(d))
one = [P for P in allP if all(evalp(P, c) == 1 for c in range(5))]
ps = [P for P in allP if all(evalp(P, c) in (1, 4) for c in range(5))]
rnd = random.Random(2).sample(allP, 200)
for name, S, A in (("Z0892 P≡1 on F5, A=T", one, [0, 1]), ("Z0892 P≡1 on F5, A=2T", one, [0, 2]),
                   ("Z0894 P(c) square ∀c, A=T", ps, [0, 1]), ("random deg5 monic, A=T", rnd, [0, 1])):
    v = [count(A, P) for P in S]
    print(f"{name}: n={len(v)} mean #ES={sum(v)/max(1,len(v)):.2f}", flush=True)
