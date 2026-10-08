import sys
K=int(sys.argv[1]); n=17**K
out=[]
for a in range(1,n):
    if 2*a*a>n: break
    for b in range(a, n//(2*a)+1):
        m=4*a*b; e=(-n)%m
        if e==0 or (a+b)%e: continue
        c=(a+b)//e; d=(n+e)//m
        if c%17==0 or d%17==0: continue
        assert 4*a*b*c*d==a+b+n*c
        out.append((a,b,c,d))
for s in out: print(*s)
