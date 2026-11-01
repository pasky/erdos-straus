# Z1849: check the word invariant behind T1 (LOWERTAIL_ROUND2_FABLE §1.3): for every word n = tuv-u-v (t,u,v>=2, n odd)
# with level t in C_n = 4Z ∪ (8Z - n), the Jacobi symbol (-t / (tu-1)) equals -1 (and likewise for tv-1);
# at odd squares no such word exists. Also tabulate which other small symbol combinations are constant on words.
import sys
def jacobi(a,n):
    assert n>0 and n%2
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
N=int(sys.argv[1]); stats={}; sqwords=0
for t in range(2,N+3):
    for u in range(2,N+3):
        if t*u*2-u-2>N: break
        for v in range(2,N+3):
            n=t*u*v-u-v
            if n>N: break
            if n%2==0: continue
            inC = t%4==0 or (t+n)%8==0
            if not inC: continue
            if int(n**.5)**2==n: sqwords+=1
            d=t*u-1
            if d%2==0: key=('even d',n%8,t%8 if t%4 else 0)
            else: key=(jacobi((-t)%d, d), n%8, t%8 if t%4 else 0)
            stats[key]=stats.get(key,0)+1
print('words with level in C_n, n<=',N,':',stats,' words at odd squares:',sqwords)
