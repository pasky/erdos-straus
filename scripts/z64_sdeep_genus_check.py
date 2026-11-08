"""z64 SDEEP: check whether the word sign chi_n(A) is an invariant of the proper SL2(Z)-class of the form [n, A*-A, -t]
(disc s^2-4, s = A+A*), split by s mod 4. All words of non-square n == 1 (4), n < 3000 (primitive forms).
Output: comparisons with an earlier word of the same (D, class) and sign disagreements, by s mod 4.
Run: python3 scripts/z64_sdeep_genus_check.py  (about 1 min)."""
import math
def jac(a,n):
    s=1;a%=n
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): s=-s
        a,n=n,a
        if a%4==3 and n%4==3: s=-s
        a%=n
    return s if n==1 else 0
def isqrt(n): return math.isqrt(n)
def rho(f,D):
    a,b,c=f; r=isqrt(D)
    # b' == -b mod 2c, choose in (r-2|c|, r] for reducedness-friendly normalization
    m=2*abs(c)
    bp=(-b)%m
    # shift into interval (r - m, r]
    k=(r-bp)//m
    bp+=k*m
    if bp>r: bp-=m
    return (c,bp,(bp*bp-D)//(4*c))
def isred(f,D):
    a,b,c=f; r=math.sqrt(D)
    return 0<b<r and r-b<2*abs(a)<r+b
def canon(f,D):
    g=f
    for _ in range(10000):
        if isred(g,D): break
        g=rho(g,D)
    else: raise Exception("no reduce")
    cyc=[g]; h=rho(g,D)
    while h!=g:
        cyc.append(h); h=rho(h,D)
        if len(cyc)>100000: raise Exception("cycle")
    return min(cyc)
cls={}
bad={0:0,1:0,2:0,3:0}; tot={0:0,1:0,2:0,3:0}
for n in range(5,3000,4):
    if math.isqrt(n)**2==n: continue
    u=2
    while 2*u*(u-1)<=n:
        m=n+u
        for d in range(2*u-1,m//u+1):
            if m%d==0 and (d+1)%u==0:
                v=m//d; t=(d+1)//u; A=d; As=t*v-1; s=A+As
                f=(n,As-A,-t); D=(As-A)**2+4*n*t
                assert D==s*s-4
                if math.gcd(math.gcd(n,As-A),t)!=1: continue
                key=(D,canon(f,D)); sg=jac(A,n)
                if key in cls:
                    tot[s%4]+=1
                    if cls[key][0]!=sg: bad[s%4]+=1; 
                else: cls[key]=(sg,n,(t,u,v))
        u+=1
print("comparisons by s mod 4:",tot," sign disagreements:",bad)
