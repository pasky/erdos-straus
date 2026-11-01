# z52d Pass 2 NC0 — Z1089 residue-graph homomorphisms of the certificate graph F_p.
# phi_m : F_p -> R_m, vertex u -> u mod m, edge {u,v} -> {u mod m, v mod m} (loops allowed). For each m, the realized
# residue pairs per prime, the union over primes, and the fibres of the realized pairs (which edges lie over each pair).
# "Missing lift" = residue pair that is never realized over the sampled primes.
import sys, json
from collections import defaultdict, Counter
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
N=int(sys.argv[1]) if len(sys.argv)>1 else 3000
ms=[3,4,8,12]
res={}
for m in ms:
    union=Counter(); per_p_pairs=[]; fibre_sizes=defaultdict(list)
    for p in primes14(N):
        E=fp_edges(p)
        pairs=Counter(tuple(sorted((u%m,v%m))) for u,v in E)
        union.update(pairs.keys()); per_p_pairs.append(len(pairs))
        for k,c in pairs.items(): fibre_sizes[k].append(c)
    allpairs=[tuple(sorted((a,b))) for a in range(m) for b in range(a,m)]
    never=[q for q in allpairs if union[q]==0]
    res[m]=dict(realized=sorted(union.keys()),never=never,
                per_prime_pairs_median=sorted(per_p_pairs)[len(per_p_pairs)//2],
                fibre_median={str(k):sorted(v)[len(v)//2] for k,v in fibre_sizes.items()})
    print('m',m,'realized',len(union),'of',len(allpairs),'never realized:',never)
    print('  per-prime number of residue pairs (median):',res[m]['per_prime_pairs_median'])
json.dump({str(k):v for k,v in res.items()},open('data/z52b/pass2/NC0/sub/Z1089_residue.json','w'))

# 2-adic admissibility of residue pairs (necessary condition for an edge over residues a,b mod m):
# exists integers u≡a, v≡b (mod m), p≡1 (mod 4) with v2(uv) <= v2(p+u+v)  (p taken mod 2^12; u,v in [1,2^9]).
def v2(x):
    if x==0: return 99
    c=0
    while x%2==0: x//=2; c+=1
    return c
for m in (4,8):
    adm=set()
    for u in range(1,513):
        for v in range(u+1,513):
            a,b=tuple(sorted((u%m,v%m)))
            if (a,b) in adm: continue
            for p in range(1,4096,4):
                if v2(u*v) <= v2(p+u+v): adm.add((a,b)); break
    allp=[tuple(sorted((a,b))) for a in range(m) for b in range(a,m)]
    never=[q for q in allp if res[m]['realized'] and q not in set(res[m]['realized'])]
    unexpl=[q for q in never if q in adm]
    print('m',m,'2-adically admissible pairs:',len(adm),'never-realized:',len(never),
          'never-realized but 2-adically admissible (unexplained by 2-adic):',unexpl)
