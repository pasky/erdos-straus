# Z2771: restricted-denominator ES. For modulus m and allowed class set S ⊂ Z/m, which primes p≡1(4) ≤ N
# have NO solution 4/p=1/x+1/y+1/z with x,y,z mod m all in S?  Input: lines "p x y z" (all unordered solutions).
import sys, itertools, collections
fn=sys.argv[1]; ms=[int(a) for a in sys.argv[2].split(',')]
sols=collections.defaultdict(list)
for l in open(fn):
    p,x,y,z=map(int,l.split()); sols[p].append((x,y,z))
P=sorted(sols)
for m in ms:
    # per prime: set of frozen class-sets used by solutions (as bitmask of classes)
    masks={p:set((1<<(t[0]%m))|(1<<(t[1]%m))|(1<<(t[2]%m)) for t in sols[p]) for p in P}
    res=[]
    for S in range(1,(1<<m)-1):
        fails=[p for p in P if not any((mk & ~S)==0 for mk in masks[p])]
        res.append((len(fails),S,fails))
    res.sort()
    print(f"== m={m}: {len(P)} primes; class sets with fewest failures (S as list of allowed classes):")
    for nf,S,fails in res[:12]:
        cls=[r for r in range(m) if S>>r&1]
        # classify failures by p mod m
        bym=collections.Counter(p%m for p in fails)
        print(f"  S={cls}: {nf} fails, last={fails[-1] if fails else None}, first={fails[:8]}, by p mod {m}: {dict(sorted(bym.items()))}")
