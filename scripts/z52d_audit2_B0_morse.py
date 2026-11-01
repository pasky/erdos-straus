# Z1116: discrete-Morse / elementary-collapse test on the natural fixed-p certificate complex K(p)
# (vertices = denominators of positive solutions of 4/p, 2-cells = solutions {x,y,z}; cf. invol_topological Prop K),
# and on the "move" complex where two solutions are joined if they share a denominator (a local refactor move) and
# triangles are triples pairwise sharing a denominator. Greedy elementary collapses via free faces; report critical cells.
import sys, math, itertools
def sols(N):
    out=[]
    for x in range(N//4+1, 3*N//4+1):
        num=4*x-N; den=N*x
        g=math.gcd(num,den); num//=g; den//=g
        for y in range(max(x,den//num+1), 2*den//num+1):
            n2=num*y-den
            if n2>0 and (den*y)%n2==0: out.append((x,y,den*y//n2))
    return out
def collapse(cells):
    # cells: set of frozensets (closed under faces). greedy free-face collapses; returns remaining cells by dim
    cells=set(cells)
    cof={c:set() for c in cells}
    for c in cells:
        for v in c:
            f=c-{v}
            if f and f in cof: cof[f].add(c)
    changed=True
    while changed:
        changed=False
        for f in list(cof):
            if f in cof and len(cof[f])==1:
                (c,)=tuple(cof[f])
                # remove pair (f,c)
                for g in (f,c):
                    for v in g:
                        h=g-{v}
                        if h in cof: cof[h].discard(g)
                    del cof[g]
                changed=True
    dims={}
    for c in cof: dims[len(c)-1]=dims.get(len(c)-1,0)+1
    return dims
def closure(tops):
    S=set()
    for t in tops:
        for k in range(1,len(t)+1):
            for s in itertools.combinations(sorted(t),k): S.add(frozenset(s))
    return S
for p in map(int,sys.argv[1:]):
    s=sols(p)
    K=closure([frozenset(t) for t in s])
    # move complex
    idx={t:i for i,t in enumerate(s)}
    share=lambda a,b: bool(set(a)&set(b))
    edges=[(i,j) for i,j in itertools.combinations(range(len(s)),2) if share(s[i],s[j])]
    adj={i:set() for i in range(len(s))}
    for i,j in edges: adj[i].add(j); adj[j].add(i)
    tris=[(i,j,k) for i,j in edges for k in adj[i]&adj[j] if k>j]
    M=closure([frozenset(t) for t in tris]+[frozenset(e) for e in edges]+[frozenset([i]) for i in range(len(s))])
    print(p,'f=',len(s),'K(p) critical cells by dim after greedy collapse:',collapse(K),' move complex:',collapse(M),flush=True)
