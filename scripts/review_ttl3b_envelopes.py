"""R121B: from-scratch check of the double-exponential envelopes claimed in LOGLOG3 §§5,7,9 (work in log-log)."""
import mpmath as mp
mp.mp.dps=30
L2=mp.log(2)
def logfact(p): return mp.loggamma(p+1)
def logKT2(d):
    s=d/16; p=mp.floor(2/s); A=10000*L2
    logR=100*(p+1)*L2+4*logfact(p); logD=4*2**(4/s)*mp.log(8/s)
    logP=A+logR+2*logD+4*mp.log(1+1/s); logG=(1/s)*mp.log(1+1/s)
    return 4*A+2*logP+2*logG+4*mp.log(1+1/s)
def logKLSchi(d,BW,CW):
    s=d/16; p=mp.floor(2/s); A=10000*L2; b=max(4,int(mp.ceil(BW+1)))
    logR=100*(p+1)*L2+4*logfact(p); logDb=b*2**(b/s)*mp.log(2*b/s)
    logP=A+mp.log(CW)+logR+2*logDb+4*mp.log(1+1/s); logG=(1/s)*mp.log(1+1/s)
    return 20*L2+4*A+2*logP+2*logG+4*mp.log(1+1/s), b
def lse(*xs):  # log of sum of exp
    m=max(xs); return m+mp.log(sum(mp.e**(x-m) for x in xs if x-m>-200))
def chain(d, logLS, B_LS_claim):
    e=d/4
    logK14=1200*L2+lse(0,logLS(e))+3*mp.log(1+6/e)  # log(1+K) ~ logK
    logDe=2**(1/e)*mp.log(2/e)
    A=32768*L2
    logK1=A-2*mp.log(d)+lse(0,logLS(e),logDe+logK14)
    logc=A-2*mp.log(d)+lse(0,logLS(e))
    logK2=5*L2+logLS(d)
    logQ0=max((mp.log(90)+logc)/(10*d*d), mp.log(2*mp.pi)/(2*d))
    logH=max(L2+logK2+logQ0, mp.log(10)+logK1, mp.log(200)+logc+logK1)
    return logK1,logc,logH
print("delta, loglog K_T2, 96/delta, 100/delta")
for d in [mp.mpf(1)/10, mp.mpf(1)/30, mp.mpf(1)/100, mp.mpf(1)/1000]:
    print(mp.nstr(d,3), mp.nstr(mp.log(logKT2(d)),6), mp.nstr(96/d,6))
for BW,CW in [(1,1),(3,10),(10,1e6)]:
    print("twisted B_W=%s C_W=%s"%(BW,CW))
    for d in [mp.mpf(1)/10, mp.mpf(1)/40, mp.mpf(1)/400]:
        lk,b=logKLSchi(d,BW,CW); Bchi=400+64*b+16*mp.log(2+CW)
        logK1,logc,logH=chain(d, lambda x: logKLSchi(x,BW,CW)[0], Bchi)
        print("  d=%s loglogKLS=%s (B/d=%s) | loglogK1=%s loglogc=%s (claim (4B+1)/d=%s) | loglogK7=%s (claim (4B+4)/d=%s)"%(
            mp.nstr(d,3),mp.nstr(mp.log(lk),6),mp.nstr(Bchi/d,6),mp.nstr(mp.log(logK1),6),mp.nstr(mp.log(logc),6),
            mp.nstr((4*Bchi+1)/d,6),mp.nstr(mp.log(logH),6),mp.nstr((4*Bchi+4)/d,6)))
