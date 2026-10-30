from math import gcd
import sys
def sols(n):
    out=[]
    for x in range(n//4+1, 3*n//4+1):
        a=4*x-n; b=n*x
        if a<=0: continue
        g=gcd(a,b); a//=g; b//=g
        # 1/y+1/z=a/b, y>=x, y<=2b/a
        for y in range(max(x,b//a+1), 2*b//a+1):
            num=a*y-b
            if num>0 and (b*y)%num==0: out.append((x,y,b*y//num))
    return out
for n in map(int,sys.argv[1:]):
    S=sols(n); print(n,len(S))
    for s in S: print('  ',s, 'mod3',[v%3 for v in s],'mod4',[v%4 for v in s],'x|z',s[2]%s[0]==0)
