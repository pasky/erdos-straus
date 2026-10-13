# check: for n = k*m^2, no word xyz-x-z=n has middle y = 0 (mod 4k); for k=1 also y != 7 (mod 8), and y != 3 (mod 4) if m even.
from sympy import divisors
def words(n):
    for x in range(2,int((n/2)**0.5)+3):
        N=n+x
        for d in divisors(N):
            if d%x==x-1 and d>=2*x-1 and N//d>=2:
                yield (x,(d+1)//x,N//d); 
                if N//d!=x: yield (N//d,(d+1)//x,x)
bad=0; tot=0
for k in [1,2,3,5,6,7]:
    for m in range(2,160):
        n=k*m*m
        for (x,y,z) in words(n):
            assert x*y*z-x-z==n; tot+=1
            if y%(4*k)==0: bad+=1; print("viol 4k",k,m,(x,y,z))
            if k==1 and (y%8==7 or (m%2==0 and y%4==3)): bad+=1; print("viol sq",m,(x,y,z))
print("words checked",tot,"violations",bad)
