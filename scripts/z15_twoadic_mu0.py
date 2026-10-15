# O240: 2-adic test of the descent condition at mu = 0 for n = c*2^s + 1 = c*2^j*U^e + 1 (Theorem A, MENU_STERILITY §4).
# After scaling U = rho*eta (rho = 2^(-j/e)), the condition is: eta*(eta-1) is a square in A_2 = Q_2[x]/(c x^e + 1).
# e odd: A_2 is etale over Z_2 off the component eta_0 = (-1/c)^(1/e) in Q_2 (when it exists); test squares mod 8.
import sys, itertools
c=int(sys.argv[1]); EMAX=int(sys.argv[2]); N=40; MOD=2**N
def polymod(a,f,mod):  # a, f coefficient lists low->high, f monic
    a=a[:]; df=len(f)-1
    for i in range(len(a)-1,df-1,-1):
        co=a[i]%mod
        if co:
            for k in range(df+1): a[i-df+k]=(a[i-df+k]-co*f[k])%mod
    return [x%mod for x in a[:df]]+[0]*(df-len(a[:df]))
def mul(a,b,f,mod):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for k,y in enumerate(b): r[i+k]+=x*y
    return polymod(r,f,mod)
for e in range(1,EMAX+1,2):
    # eta_0 in Z_2: eta^e = -1/c  (c odd => -1/c is a 2-adic unit; e odd => unique root in Q_2)
    t=(-pow(c,-1,MOD))%MOD; eta=1
    for _ in range(80):  # Newton on x^e - t
        eta=(eta-(pow(eta,e,MOD)-t)*pow(e*pow(eta,e-1,MOD),-1,MOD))%MOD
    x0=eta*(eta-1)%MOD; v=(x0&-x0).bit_length()-1; u0=x0>>v
    comp0 = "square" if (v%2==0 and u0%8==1) else "NONSQ(v=%d,u=%d mod 8)"%(v,u0%8)
    # other component: g = (c x^e + 1)/(x - eta) over Z/2^N, made monic
    cpoly=[1]+[0]*(e-1)+[c]          # c x^e + 1, low->high
    # synthetic division by (x - eta)
    q=[0]*e; r=0
    for i in range(e,-1,-1):
        r=(cpoly[i]+r*eta)%MOD
        if i>0: q[i-1]=r
    inv=pow(q[-1],-1,MOD); g=[(x*inv)%MOD for x in q]   # monic, degree e-1, low->high
    res="(none)"
    if e>1:
        M8=8; g8=[x%M8 for x in g]; df=e-1
        target=polymod([0,-1,1],g8,M8) if df>=2 else polymod([0,-1,1],g8,M8)
        squares=set()
        for w in itertools.product(range(M8),repeat=df):
            if all(x%2==0 for x in w): continue
            squares.add(tuple(mul(list(w),list(w),g8,M8)))
        res="square" if tuple(target) in squares else "NONSQ"
    print("c=%d e=%d  Q2-component: %s   other components: %s"%(c,e,comp0,res),flush=True)
