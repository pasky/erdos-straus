# y7 (O215): is S_M-membership of a length-3 word w=(t,u,v) of n a function of the Z-isometry class of the
# path form Q_w (Gram [[v,-1,0],[-1,t,-1],[0,-1,u]], det n)?  For M=4 it is (S_4 = {chi=-1}, a genus invariant).
# usage: uv run --with cypari2 python scripts/y7_class_test.py NMAX M1 M2 ...
import sys, cypari2
pari=cypari2.Pari()
def words(n):
    W=[]
    for t in range(1,n+2):
        for u in range(1,n+2):
            if t*u<2: continue
            if t*u-1>n+u: break
            if (n+u)%(t*u-1)==0:
                v=(n+u)//(t*u-1)
                if v>=1: W.append((t,u,v))
    return W
def inS(M,w):
    t,u,v=w
    return (t*u-1)%M==0 or (t*v-1)%M==0 or t%M==0 or u%M==0 or v%M==0
def isprime(n): return n>1 and all(n%q for q in range(2,int(n**.5)+1))
NMAX=int(sys.argv[1]); Ms=list(map(int,sys.argv[2:]))
stats={M:[0,0] for M in Ms}  # [classes with both members and non-members, classes total]
ex={}
for n in range(5,NMAX+1,2):
    if not isprime(n): continue
    W=words(n)
    G={w:pari.matrix(3,3,[w[2],-1,0,-1,w[0],-1,0,-1,w[1]]) for w in W}
    # group by theta series (cheap invariant), then refine with qfisom
    classes=[]
    for w in W:
        th=tuple(pari.qfrep(G[w],60))
        for c in classes:
            if c[0]==th and pari.qfisom(G[c[1][0]],G[w])!=0:
                c[1].append(w);break
        else: classes.append([th,[w]])
    for M in Ms:
        if n%M==0: continue
        for th,ws in classes:
            s=set(inS(M,w) for w in ws)
            stats[M][1]+=1
            if len(s)>1:
                stats[M][0]+=1
                ex.setdefault(M,(n,ws))
for M in Ms:
    print(f"M={M}: primes n<={NMAX}: isometry classes {stats[M][1]}, mixed (S_M not a class function) {stats[M][0]}; example {ex.get(M)}")
