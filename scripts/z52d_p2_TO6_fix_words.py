"""z52d pass2 TO6 fix: Z2132 / Z2267. (1) find a product of three 2x2 CF-type matrices whose entry equals t*u*v - u - v;
(2) for primes p≡1 mod 4 (p<=10^4) enumerate words (t,u,v>=2) with tuv-u-v=p; count words up to reversal (matrix transpose
symmetry); check the record's coordinate congruence (a coordinate in 4Z ∪ (8Z-p)); report."""
import sympy as sp, itertools, json
from sympy import primerange
t,u,v=sp.symbols('t u v')
def A(k,s): return sp.Matrix([[k,s],[1,0]])
found=None
for s1,s2,s3 in itertools.product([1,-1],repeat=3):
    M=A(t,s1)*A(u,s2)*A(v,s3)
    for (i,j) in [(0,0),(0,1),(1,0),(1,1)]:
        e=sp.expand(M[i,j])
        if sp.simplify(e-(t*u*v-u-v))==0 or sp.simplify(e+(t*u*v-u-v))==0:
            found=(s1,s2,s3,i,j,sp.expand(M[i,j])); break
    if found: break
print('matrix identity found (s1,s2,s3,row,col,entry):', found, flush=True)
# words for primes
def words(p):
    out=[]
    for tt in range(2,p+2):
        for uu in range(2,p+2):
            # p = tuv - u - v  => v (t u - 1) = p + u  => v = (p+u)/(tu-1)
            d=tt*uu-1
            if d<=0: continue
            for vv in [((p+uu)//d)] if (p+uu)%d==0 else []:
                if vv>=2 and tt*uu*vv-uu-vv==p: out.append((tt,uu,vv))
    return out
res=[]
ps=[p for p in primerange(5,2000) if p%4==1]
nw=[];cong=0; nonrev=[]
for p in ps:
    W=words(p)
    canon=set(min((a,b,c),(c,b,a)) for a,b,c in W)
    nw.append(len(canon))
    ok=any(any(x%4==0 for x in w) or any((x-p)%8==0 for x in w) for w in W)
    cong+=ok
    if len(canon)==0: res.append(('no words',p))
summary=dict(primes_checked=len(ps), words_min=min(nw), words_median=sorted(nw)[len(nw)//2], words_max=max(nw),
    primes_with_zero_words=sum(1 for z in nw if z==0), primes_with_congruence_word=cong,
    matrix_identity=str(found))
print(json.dumps(summary))
json.dump(summary, open('data/z52b/pass2/TO6/words_TO6.json','w'), indent=1)
