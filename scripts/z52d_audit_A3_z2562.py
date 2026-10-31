"""z52d audit A3, Z2562: e-slices (LONGSHOT_PIGEONHOLE Lemma 1.1) with prime e = 3 (4), e <= EMAX, both types,
N = (p+e)/4 (II) or (pe+1)/4 (I); Q = Sigma_e(N) = prod {l^t : |t| <= v}.  Slice succeeds iff -1 in Q.
Stats: share of slices with a prime factor of N that is a primitive root mod e; P(-1 in Q | prim-root factor) vs not;
also conditioned on omega(N) and on 'some factor is a non-residue mod e' (necessary: -1 is a QNR mod e)."""
import sys
from sympy import factorint, primerange, n_order, isprime
P0 = int(sys.argv[1]); NPR = int(sys.argv[2]); EMAX = int(sys.argv[3])
def qnr(a, e): return pow(a % e, (e - 1) // 2, e) == e - 1
ps = []; p = P0
while len(ps) < NPR:
    p += 1
    if p % 840 in (1, 121, 169, 289, 361, 529) and isprime(p): ps.append(p)
es = [e for e in primerange(3, EMAX + 1) if e % 4 == 3]
from collections import defaultdict
st = defaultdict(lambda: [0, 0])  # key -> [slices, successes]
per_p = []
for p in ps:
    succ_p = 0
    for e in es:
        for T, N4 in (("II", p + e), ("I", p * e + 1)):
            if N4 % 4: continue
            N = N4 // 4
            f = factorint(N)
            Q = {1}
            for l, v in f.items():
                pw = [pow(l, t, e) for t in range(v + 1)] + [pow(pow(l, -1, e), t, e) for t in range(1, v + 1)]
                Q = {q * x % e for q in Q for x in pw}
            ok = (e - 1) in Q
            prim = any(n_order(l % e, e) == e - 1 for l in f)
            anyqnr = any(qnr(l, e) for l in f)
            om = min(len(f), 6)
            for key in [("all",), ("prim", prim), ("anyqnr", anyqnr), ("prim|qnr", prim) if anyqnr else None, ("omega", om, prim), ("qnr+omega", om, prim) if anyqnr else None]:
                if key is None: continue
                st[key][0] += 1; st[key][1] += ok
            succ_p += ok
    per_p.append(succ_p)
print(f"P0={P0} primes={len(ps)} (Mordell-hard classes) e prime=3(4) <= {EMAX}: {len(es)} values, both types")
for k in sorted(st, key=str):
    n, s = st[k]; print(k, "slices", n, "success", s, f"rate {s/n:.4f}")
print("min successes per prime", min(per_p), "mean", sum(per_p) / len(per_p))
