"""z52d_p2_TO5_hard.py — Z1802 / Z1803 / Z1869 on the hard-prime set H = {p ≡ 1 (mod 4), p <= 1e6, R(p)/M_BM(p) < THR}.
Z1802: chi-square of residues mod 840 (unit classes ≡1 mod 4) of H vs all p≡1 mod 4 (classes equally weighted by Dirichlet).
Z1803: quartic symbols (2/p)_4,(3/p)_4,(5/p)_4,(7/p)_4 on H vs all p≡1 mod 840-compatible (p≡1 mod 8 only, controls).
Z1869: writes the 100 hardest primes (min R/M_BM, p>=5) to data/z52b/pass2/TO5/hardest_100.tsv.
usage: python3 scripts/z52d_p2_TO5_hard.py THR"""
import sys, math, collections
D='data/z52b/pass2/TO5/'
THR=float(sys.argv[1]) if len(sys.argv)>1 else 0.25
rows=[]
for l in open(D+'mbm_1e6.txt'):
    if l.startswith('#'): continue
    a=l.split()
    if len(a)<6 or int(a[1])==0: continue
    n,R,M0,MB=int(a[0]),int(a[2]),float(a[3]),float(a[4])
    if n%4==1 and n>=5 and MB>0: rows.append((n,R,MB,R/MB))
H=[r for r in rows if r[3]<THR]
print("p≡1(4) ≤1e6: %d ; hard set (R/M<%.2f): %d"%(len(rows),THR,len(H)))
# Z1802: residues mod 840 among units ≡1 mod 4 (classes: 840=8*3*5*7; units ≡1(4) -> 96/2=... just use p mod 840 directly)
cnt_all=collections.Counter(r[0]%840 for r in rows); cnt_H=collections.Counter(r[0]%840 for r in H)
classes=sorted(cnt_all)
nA=len(rows); nH=len(H)
chi2=0.0; worst=(0,0,0)
for c in classes:
    e=nH*cnt_all[c]/nA
    if e>0:
        chi2+=(cnt_H.get(c,0)-e)**2/e
        dev=(cnt_H.get(c,0)-e)/math.sqrt(e)
        if abs(dev)>abs(worst[0]): worst=(dev,c,cnt_H.get(c,0))
print("Z1802 chi^2 over %d classes mod 840 (df=%d): %.1f ; worst class %d z=%+.2f (obs %d)"%(len(classes),len(classes)-1,chi2,worst[1],worst[0],worst[2]))
# Z1803: quartic symbols for p≡1 mod 8 (quartic symbol needs p≡1 mod 4)
def qs4(a,p):
    v=pow(a,(p-1)//4,p)
    return {1:'+1',p-1:'-1'}.get(v, '+i/-i')
for a in (2,3,5,7):
    cH=collections.Counter(qs4(a,r[0]) for r in H if r[0]%8==1)
    cA=collections.Counter(qs4(a,r[0]) for r in rows if r[0]%8==1)
    nHh=sum(cH.values()); nAa=sum(cA.values())
    print("Z1803 (%d/p)_4 among p≡1(8): hard %s  all %s"%(a,{k:round(v/nHh,3) for k,v in cH.items()},{k:round(v/nAa,3) for k,v in cA.items()}))
# Z1869: hardest 100
rows.sort(key=lambda r: r[3])
with open(D+'hardest_100.tsv','w') as f:
    f.write("p\tR\tM_BM\tR_over_M\tp_mod_840\n")
    for r in rows[:100]: f.write("%d\t%d\t%.4f\t%.4f\t%d\n"%(r[0],r[1],r[2],r[3],r[0]%840))
print("Z1869 hardest 5:",[(r[0],r[1],round(r[3],4)) for r in rows[:5]])

# ---- Z1802 follow-up: hard-prime frequency by Legendre-symbol cells (q/p), q in {3,5,7,11,13} and p mod 8 ----
def leg(q,p):  # (q/p) for odd prime p, via Euler criterion
    v=pow(q%p,(p-1)//2,p); return 1 if v==1 else -1
def cell(p): return (leg(3,p),leg(5,p),leg(7,p))
cA=collections.Counter(cell(r[0]) for r in rows); cH=collections.Counter(cell(r[0]) for r in H)
nA=len(rows); nH=len(H)
print("Z1802b cell (3/p),(5/p),(7/p): all-count, hard-count, hard-rate, expected")
for k in sorted(cA):
    print("  %s all %6d hard %3d rate %.4f expected %.2f"%(k,cA[k],cH.get(k,0),cH.get(k,0)/cA[k],nH*cA[k]/nA))
# within-(7/p)=-1 : is class 409 still over-represented?
