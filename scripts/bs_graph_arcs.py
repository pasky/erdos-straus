"""Exhaustive 16-case arc-parity table for Theorem A.1 of BRAINSTORM/graph_cayley_moves.md.
Roots r1<..<r4 of the four coordinate forms on a real line; prints (arc types, arc parities, root distribution, #roots on type-1 arcs)."""
import itertools
# roots of l_1..l_4 at r1<r2<r3<r4 on the circle; arc j=(r_j, r_{j+1}), arc 4 = (r4, r1) through infinity (sign flip of all)
res=set()
for s in itertools.product([1,-1],repeat=4):
    arcs=[]; v=list(s)
    for j in range(4):
        arcs.append(tuple(v))
        if j<3: v[j+1]*=-1   # crossing r_{j+2}: flips l_{j+2} (0-indexed j+1)
    # arc j endpoints: start root index j (arc0 starts at r1 idx0), end root index j+1 ; arc3: start idx3, end idx0 (after projective flip)
    info=[]
    for j in range(4):
        a=j; b=(j+1)%4
        e=arcs[j]
        if j<3: ea,eb=e[a],e[b]
        else: ea,eb=e[a],-e[b]  # after passing infinity the vector is negated: compare in a consistent lift
        neg=sum(1 for x in e if x<0); typ=min(neg,4-neg)
        # parity of number of zeros of h on arc: odd iff sign of h near start != near end
        # near start: h ~ 1/l_a, l_a has sign e[a] on arc -> +inf*e[a]; near end: l_b has sign e[b] on arc
        # for arc 3 use the lift: on the arc the actual vector is e; h has sign e[a] near r4 and e[b] near r1 (same lift) 
        par=(e[a]!=e[b])
        info.append((typ,par))
    for c in itertools.product(range(4),repeat=4):
        if sum(c)!=3: continue
        if any((c[j]%2)!=info[j][1] for j in range(4)): continue
        if any(c[j]>0 and info[j][0]==0 for j in range(4)): print('root on type0 arc?!',s,c)
        omega=sum(c[j] for j in range(4) if info[j][0]==1)
        res.add((tuple(i[0] for i in info),tuple(int(i[1]) for i in info),c,omega))
for r in sorted(res): print(r)
