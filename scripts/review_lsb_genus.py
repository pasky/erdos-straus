# R136 from-scratch: for D=-4dn, count reduced primitive positive forms (h), those with chi_{-4d}(Q) = -1
# (chi evaluated at a represented value prime to 4dn), and the Type II count F_d(n) = #{(a,b,c) in N^3 :
# 4abcd = a+b+nc} (ET (2.15); enumerate a,c with f=4acd-1 | nc+a, b=(nc+a)/f).
import sys
from math import gcd, isqrt
def jacobi(a,n):
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
def forms(D):
    N=-D; out=[]
    for a in range(1,isqrt(N//3)+1):
        for b in range(-a+1,a+1):
            if (b*b-D)%(4*a): continue
            c=(b*b-D)//(4*a)
            if c<a or (c==a and b<0): continue
            if gcd(gcd(a,abs(b)),c)!=1: continue
            out.append((a,b,c))
    return out
def chi(d,Q,M):
    a,b,c=Q
    for x in range(0,40):
        for y in range(-40,41):
            k=a*x*x+b*x*y+c*y*y
            if k>0 and gcd(k,M)==1: return jacobi(-d % k if False else (-d)%k, k)
    raise Exception
def F(d,n):
    cnt=0; c=1
    while 4*c*d-1<=n*c+ (n*c)//1 and c<=n:   # need f=4acd-1 <= nc+a with a>=1 => 4cd-1<=nc+1
        a=1
        while 4*a*c*d-1<=n*c+a:
            f=4*a*c*d-1
            if (n*c+a)%f==0: cnt+=1
            a+=1
        c+=1
        if 4*c*d-1>n*c+1 and 4*c*d-1 > (n*c+1): break
    return cnt
if __name__=='__main__':
  ps=[1009,2689,4729,9601,10009]; sqs=[31**2,41**2,73**2,97**2,101**2]
  zero=0; tot=0
  for n in ps+sqs:
      row=[]
      for d in range(1,9):
          Fs=forms(-4*d*n); M=4*d*n
          hm=sum(chi(d,Q,M)==-1 for Q in Fs); f=F(d,n)
          row.append(f"d={d}: h={len(Fs)} h-={hm} F={f}")
          if n in ps:
              tot+=1; zero+=(f==0)
      print(n,' | '.join(row))
  print("F_d(p)=0 in",zero,"of",tot,"(prime,level) pairs")
