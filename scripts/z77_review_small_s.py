"""z77 review: explicit ES triples for (4^m-1)2^s+1, m=4,5,6, 0<=s<32 (removes reliance on Salez)."""
def fac(n):
    f={};p=2
    while p*p<=n:
        while n%p==0:f[p]=f.get(p,0)+1;n//=p
        p+=1 if p==2 else 2
    if n>1:f[n]=f.get(n,0)+1
    return f
def divs(f):
    d=[1]
    for p,e in f.items():d=[x*p**i for x in d for i in range(e+1)]
    return d
def es(n):
    for x in range(n//4+1,n//4+2000):
        num=4*x-n;den=n*x
        f=fac(n);
        for p,e in fac(x).items():f[p]=f.get(p,0)+e
        f2={p:2*e for p,e in f.items()}
        for g in divs(f2):
            if g<=den and (g+den)%num==0:
                y=(g+den)//num;z=(den*den//g+den)//num
                assert 4*x*y*z==n*(x*y+y*z+z*x);return x,y,z
if __name__=='__main__':
    for k in (255,1023,4095):
        for s in range(32):
            n=k*2**s+1;assert es(n),(k,s)
        print(k,'s<32 explicit ES ok')
