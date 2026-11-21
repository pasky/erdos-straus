"""P vicinity of point 5: exact valuation of each witnessed oriented datum.
Through L=8 full stored sets. Higher: selected slices, NOT exhaustive unless
exclusion proof specified. For 1/5 simply reflect orientation."""
import gzip,sys
from pathlib import Path
r=17

def near(L,lines,complete):
    best=-1;out=None;num=0;cnt=0
    for l in lines:
        a,b,c,d=map(int,l.split());e=4*a*b*d-r**(2*L-1)
        assert min(a,b,c,d,e)>0 and a+b==c*e and (a*b*c*d*e)%17
        for x,y in [(a,b),(b,a)]:
            n=x+5*y;v=0
            while n%17==0:n//=17;v+=1
            cnt+=1
            if v>best:best=v;out=(x,y,c,d,e);num=1
            elif v==best:num+=1
    print(L,complete,cnt,best,L-best,num,*out,flush=True)
if __name__=='__main__':
    for l in range(1,9):
        fs=gzip.open('data/z17/p15_r17.txt.gz','rt') if l==8 else open(f'data/m17b/p{2*l-1}.txt');near(l,fs,1)
    for l in map(int,sys.argv[1:]):near(l,open(f'data/z78/r2/near/L{l}.txt'),0)
