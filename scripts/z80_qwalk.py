"""Endpoint Q contact: a bounded rational Vieta walk controls d even for 5∤V.
All inequalities are integer tests. Memory O(k) per pair, no root tables of size r^k.
"""
import sys

def dcut(F,m):
    # No stopping by m moves implies the next m adjacent ratios exceed S/2.
    def excluded(d):
        return (2*d>5**m+6 and (4*d-6)**(2*m)*4*d*d>9*(F+1)**2*20**m*5**(2*((m+1)//2)))
    l,u=1,F+100
    while u-l>1:
        d=(u+l)//2
        if excluded(d):u=d
        else:l=d
    # ad <= (F+1)/2 is independent of the descent.
    return min(l,(F+1)//2)

def solve(r,k,verbose=False):
    F=r**k;D,m=min((dcut(F,m),m) for m in range(1,20));pairs=0;hits=set()
    for p,q in ((1,5),(5,1)):
        for d in range(1,D+1):
            if d%r==0:continue
            # sqrt(-4pqd) then divide by 4pd; cancel the unit only at the end.
            n=-4*p*q*d;y=next((t for t in range(1,(r+1)//2) if (t*t-n)%r==0),None)
            if not y:continue
            h=1
            while h<k:
                h=min(2*h,k);mod=r**h;y=(y-(y*y-n)*pow(2*y,-1,mod))%mod
            a=y*pow(4*p*d,-1,F)%F
            for a in (a,F-a):
                if 2*a*d>F+1:continue
                assert (4*p*a*a*d+q)%F==0;pairs+=1
                s=4*a*d;V=s*a+1;f1=(-F)%s;e1=(-pow(F,-1,s))%s
                for f in {f1,V//e1}:
                    if V%f or (f+F)%s:continue
                    e=V//f;c=(f+F)//s;b=c*e-a
                    if b<a or not (e*c)%r or (p*a+q*b)%F:continue
                    assert 4*a*b*d==e*F+1;hits.add((p,a,b,c,d,e))
    if verbose:print(r,k,D,m,pairs,len(hits),flush=True)
    return hits
if __name__=='__main__':
    assert solve(13,1,True)
    for k in range(1,int(sys.argv[1])+1,2):assert not solve(17,k,True)
