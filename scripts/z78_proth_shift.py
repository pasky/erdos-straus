"""Shifted degree-one word rules, including a literal representative for each successful congruence."""
from z78_proth_period import root,ds,order,dlog
from math import gcd
import json

def rows(m):
    k=4**m-1;out=[]
    for a in range(3,10):
        u=k*2**a-1;P=order(u)
        for c in ds(k):
            for b in range(0,a+1):
                C=c*2**b
                if C==k*2**a:continue # v would be 1
                tar=(-1-pow(C,-1,u))%u
                j=dlog(tar,u)
                if j is not None:
                    s0=a+j;v=k*2**a//C;out.append([a,b,c,P,s0%P,v]);assert (C*(pow(2,j,u)+1)+1)%u==0
    return out
if __name__=='__main__':
    D={}
    for m in range(1,27):
        D[m]=rows(m);print(m,len(D[m]),flush=True);(root/'shift.json').write_text(json.dumps(D,separators=(',',':'))+'\n')
