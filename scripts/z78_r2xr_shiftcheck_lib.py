"""Factoring helpers for the round-2 review checks (copied from z78_r2xr_shiftcheck.py)."""
import math
def mr(n):
    if n<2:return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%q==0:return n==q
    d=n-1;s=0
    while d%2==0:d//=2;s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37,41):
        x=pow(a,d,n)
        if x in(1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True
def rho(n):
    if n%2==0:return 2
    for c in range(1,1000):
        x=y=2;d=1
        while d==1:
            x=(x*x+c)%n;y=(y*y+c)%n;y=(y*y+c)%n;d=math.gcd(abs(x-y),n)
        if d!=n:return d
def fac(n,out):
    for q in range(2,1000):
        while n%q==0:out[q]=out.get(q,0)+1;n//=q
    st=[n]
    while st:
        m=st.pop()
        if m==1:continue
        if mr(m):out[m]=out.get(m,0)+1;continue
        d=rho(m);st+=[d,m//d]
    return out
