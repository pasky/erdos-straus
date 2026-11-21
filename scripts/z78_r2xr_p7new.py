"""Round-2 review: distinct nonsquare P7 centres and new depth-4 cells over the
exact depth-3 alive set dumped by z78_r2xr_exact3dump.c.  Usage: r dump files..."""
import sys
r=int(sys.argv[1]);R2,R3,Q=r*r,r**3,r**4
raw=open(sys.argv[2],'rb').read();al=raw[:r];c2=raw[r:r+R2//8+1];c3=raw[r+R2//8+1:]
assert len(c3)==R3//8+1
g=lambda bm,i:bm[i>>3]>>(i&7)&1
s=set();n=0
for fn in sys.argv[3:]:
    for l in open(fn):
        x,y=map(int,l.split());assert x*y%Q==1;s|={x,y};n+=1
for x in s:assert pow(x%r,(r-1)//2,r)==r-1
new={x for x in s if al[x%r] and not g(c2,x%R2) and not g(c3,x%R3)}
print(r,'tuples',n,'distinct',len(s),'new',len(new))
