# Z2764: complex on ES words of all n' <= P (t,u,v >= 2, n' = tuv-u-v), faces = sets of words sharing a letter
# (same position, same value). By the nerve lemma K ~ nerve of the letter-class cover = 2-complex with one triangle
# {T_t,U_u,V_v} per word; since (t,u),(t,v),(u,v) each determine the word, every edge is in <=1 triangle, so
# K ~ the bipartite incidence graph (letters ∪ words). Report Z/2 Betti numbers b0, b1 (b2 = 0).
import sys
P=int(sys.argv[1])
words=[(t,u,v) for t in range(2,P+3) for u in range(2,P+3) if t*u*2-u-2<=P for v in range(2,P+3) if t*u*v-u-v<=P]
# also restrict to 4|t (ES level words) if requested
if len(sys.argv)>2: words=[w for w in words if w[0]%4==0]
letters=set()
for t,u,v in words: letters|={('t',t),('u',u),('v',v)}
# incidence graph: V = letters+words, E = 3*words
par={}
def f(x):
    while par.setdefault(x,x)!=x:
        par[x]=par[par[x]]; x=par[x]
    return x
for w in words:
    for l in (('t',w[0]),('u',w[1]),('v',w[2])): par[f(l)]=f(('w',)+w)
c=len({f(x) for x in list(par)})
V=len(letters)+len(words); E=3*len(words)
print(f"P={P} words={len(words)} letters={len(letters)} b0={c} b1={E-V+c} (Z/2 acyclic would need b0=1,b1=0)")
